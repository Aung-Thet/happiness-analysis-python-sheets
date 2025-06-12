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

Copy the Code

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
