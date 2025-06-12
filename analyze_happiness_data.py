import gspread
import pandas as pd
from google.oauth2.service_account import Credentials
from gspread_dataframe import get_as_dataframe

def analyze_happiness_data():
    """
    Connects to Google Sheets, fetches World Happiness Report data,
    and performs an analysis.
    """
    try:
        # --- Authentication and Connection ---
        scope = [
            'https://www.googleapis.com/auth/spreadsheets',
            'https://www.googleapis.com/auth/drive'
        ]
        creds = Credentials.from_service_account_file('credentials.json', scopes=scope)
        client = gspread.authorize(creds)

        # Open the Google Sheet by its name and the specific worksheet
        sheet = client.open("Happiness Analysis").worksheet("2019_data")
        print("✅ Successfully connected to the Google Sheet.")

        # --- Data Loading and Cleaning ---
        # Load data into a pandas DataFrame and rename columns for clarity
        df = get_as_dataframe(sheet, evaluate_formulas=True)
        df.rename(columns={
            'Country or region': 'Country',
            'Overall rank': 'Rank',
            'Score': 'Happiness_Score',
            'GDP per capita': 'GDP_per_capita',
            'Social support': 'Social_Support',
            'Healthy life expectancy': 'Life_Expectancy',
            'Freedom to make life choices': 'Freedom',
            'Perceptions of corruption': 'Corruption_Perception'
        }, inplace=True)
        
        # Ensure key columns are numeric
        numeric_cols = ['Rank', 'Happiness_Score', 'GDP_per_capita', 'Freedom']
        for col in numeric_cols:
            df[col] = pd.to_numeric(df[col], errors='coerce')
        
        df.dropna(subset=numeric_cols, inplace=True) # Drop rows if key data is missing
        print("✅ Data loaded and cleaned.")

        # --- Data Analysis ---
        print("\n--- World Happiness Report Analysis (2019) ---")

        # 1. Top 10 Happiest Countries
        top_10_happy = df.sort_values(by='Happiness_Score', ascending=False).head(10)
        print("\n😀 Top 10 Happiest Countries:")
        print(top_10_happy[['Rank', 'Country', 'Happiness_Score']].to_string(index=False))

        # 2. Bottom 10 Unhappiest Countries
        bottom_10_happy = df.sort_values(by='Happiness_Score', ascending=True).head(10)
        print("\n😔 Bottom 10 Unhappiest Countries:")
        print(bottom_10_happy[['Rank', 'Country', 'Happiness_Score']].to_string(index=False))

        # 3. Analyze Key Factors
        avg_freedom = df['Freedom'].mean()
        avg_generosity = df['Generosity'].mean()
        print("\n📊 Average Scores Across All Countries:")
        print(f"   - Freedom to make life choices: {avg_freedom:.3f}")
        print(f"   - Generosity: {avg_generosity:.3f}")

        # 4. Correlation between GDP and Happiness
        correlation = df['GDP_per_capita'].corr(df['Happiness_Score'])
        print("\n💰 Economic Impact on Happiness:")
        print(f"   - Correlation between GDP per capita and Happiness Score: {correlation:.3f}")
        print("     (A value near +1.0 indicates a strong positive correlation)")


    except FileNotFoundError:
        print("❌ Error: 'credentials.json' not found. Please follow the setup instructions.")
    except gspread.exceptions.SpreadsheetNotFound:
        print("❌ Error: The Google Sheet named 'Happiness Analysis' was not found.")
    except gspread.exceptions.WorksheetNotFound:
        print("❌ Error: The worksheet named '2019_data' was not found. Please rename the tab.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == '__main__':
    analyze_happiness_data()