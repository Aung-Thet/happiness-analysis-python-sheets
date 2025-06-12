World Happiness Report Analysis with Google Sheets and Python

This project demonstrates a simple data analysis pipeline using Google Sheets as a data source and Python for processing and analysis. We will be analyzing the World Happiness Report (2019) dataset to uncover insights into global well-being.

📋 Project Overview

The goal of this project is to showcase how to:
* Use Google Sheets to store and access a manageable dataset.
* Connect to the Google Sheets API using Python.
* Utilize the pandas library to perform data manipulation and analysis.
* Derive meaningful insights from the data, such as identifying key factors contributing to happiness and analyzing their correlations.

🛠️ Technologies Used

Python: The core language for our data analysis script.

Google Sheets: Used as the database to hold our raw data.

Google Cloud Platform (GCP): For enabling the Google Sheets API and managing credentials.

Libraries:

  * gspread: To interact with the Google Sheets API.
  * gspread-dataframe: To easily convert Google Sheet data into pandas DataFrames.
  * pandas: For data manipulation and analysis.
  * google-auth-oauthlib: For handling authentication.

⚙️ Setup Instructions

To replicate this analysis, you'll need to set up your environment.

1. Prepare the Data in Google Sheets
   
Get the Dataset: This project uses the 2019 World Happiness Report. You can access the raw CSV file directly from this URL: https://www.kaggle.com/datasets/PromptCloudHQ/world-happiness-report-2019

Upload to Google Sheets:

  * Create a new Google Sheet.
  * Rename the Google Sheet (e.g., to "Happiness Analysis").
  * Import the data by going to File > Import > Upload and selecting the CSV file, or by pasting the URL.
  * After importing, rename the worksheet tab at the bottom to 2019_data.

3. Set Up Google Cloud Platform and API Credentials

Enable APIs:

Go to the Google Cloud Console.

Create a new project.

Enable the Google Drive API and the Google Sheets API for your project.

Create Credentials:

  * Navigate to "APIs & Services" > "Credentials".
  * Click "Create Credentials" and choose "Service Account".
  * Fill in the service account details and grant it the "Editor" role.
  * Create a key for the service account (JSON format). A credentials.json file will be downloaded.
  *Share the Google Sheet:
    * Open your credentials.json file and find the client_email.
    * In your Google Sheet, click the "Share" button and share the sheet with this client email address, giving it "Editor" access.

3. Set Up Your Local Python Environment
   
  Prerequisites: Make sure you have Python 3.8 or newer installed.

Create a Project Directory:

  mkdir happiness-analysis-project

  cd happiness-analysis-project

Install Libraries:

  pip install pandas gspread gspread-dataframe google-auth-oauthlib

  Add Credentials: Move the credentials.json file you downloaded into your project directory.

👨‍💻 How to Run the Code

  With the setup complete, you can now run the analysis.

Create the Python Script: Create a file named analyze_happiness_data.py in your project directory.

Python Code

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


Copy the Code.

Execute the Script: Open your terminal and run the script:

python analyze_happiness_data.py

The script will connect to your Google Sheet, perform the analysis, and print the results to your console.

📊 Analysis and Findings
The script provides several key insights from the 2019 World Happiness Report:

Happiness Rankings: It clearly lists the countries at the top and bottom of the happiness rankings, providing a quick global overview.

Key Drivers: By calculating average scores for factors like "Freedom," we can understand what a "typical" country experience looks like according to this dataset.

Economy and Happiness: The script calculates the correlation between GDP per capita and the happiness score. The resulting strong positive correlation (typically around +0.79) quantitatively suggests that a higher national income is strongly associated with higher national happiness.

🚀 Future Improvements

This project can be extended in several ways:

Historical Analysis: Import data from multiple years (e.g., 2015-2022) into different worksheets and analyze how country rankings have changed over time.

Advanced Visualizations: Use libraries like Matplotlib or Seaborn to create a scatter plot of GDP vs. Happiness Score to visually represent the correlation.

Write Back to Sheets: Perform calculations in Python and write the results (e.g., the top 10 list) to a new worksheet in the same Google Sheet.

Regional Analysis: Group countries by continent or region to compare average happiness scores and contributing factors.
