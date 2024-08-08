# 📊 YouTube Comments Exploratory Data Analysis (EDA)
Welcome to the repository for the project **"YouTube Comments Exploratory Data Analysis (EDA)"**. This project performs detailed exploratory data analysis (EDA) on YouTube comments, focusing on text processing techniques and sentiment analysis.

## 📝 Description

The **"YouTube Comments Exploratory Data Analysis (EDA)"** project focuses on extracting meaningful insights from YouTube comments. This involves importing datasets, cleaning and preprocessing the data by handling missing values, converting text to lowercase, and removing punctuation and digits. Sentiment analysis is then performed using the TextBlob library. The main objectives are to understand viewer sentiments and engagement trends, and to apply effective text normalization and sentiment analysis techniques. This project provides valuable insights into viewer feedback and engagement with YouTube videos.

## 🔍 Findings
- Here are some of the key visualizations generated from the EDA:

<div style="display: flex; justify-content: space-between;">
  <img src="https://github.com/user-attachments/assets/fea161cd-d129-4d68-9ff4-2271d4c5c91c" alt="Top 10 Videos by View Count" width="100%" />
  <img src="https://github.com/user-attachments/assets/a40985af-c658-4838-a86e-962e05f49109" alt="Top 10 Videos with the Most Negative Comments" width="45%" />
  <img src="https://github.com/user-attachments/assets/a231773b-474b-4758-aac7-bc42a7ed39cd" alt="Top 10 Videos with the Most Positive Comments" width="45%" />
</div>

## 🌟 Key Features

- **📥 Data Loading**: Load YouTube video and comment datasets from CSV files.
- **🧹 Data Cleaning**: Handle missing values, convert data types, and preprocess text data by removing punctuation and digits.
- **📝 Text Analysis**: Perform sentiment analysis on comments using the TextBlob library.
- **📊 Visualization**: Utilize seaborn and matplotlib to visualize data distributions and relationships.

## 🎯 Target Audience

- **Data Scientists**: Interested in text data analysis and natural language processing.
- **Machine Learning Enthusiasts**: Looking to preprocess and analyze text data for machine learning models.
- **YouTube Content Creators**: Gain insights from video comments to enhance engagement.
- **Researchers**: Conducting research on social media data and user engagement.

## ⚙️ Requirements

- Python 3.6+
- Pandas
- NumPy
- Seaborn
- Matplotlib
- TextBlob

## 🚀 Getting Started

1. **Clone the Repository**: Clone this repository to your local machine using `git clone <https://github.com/ashirvadstva/YouTube-Comments-EDA>`.
2. **Install Dependencies**: Install the required Python libraries using the following command:
   ```bash
   pip install pandas numpy seaborn matplotlib textblob
3. **Run the Script**: Execute the Python script to load the datasets and perform EDA.
   ```bash
   python Youtube_Comments_EDA.py
   
## 🛠️ Usage

- Place your datasets (GBvideos.csv and GBcomments.csv) in the same directory as the script.
- The script will output various data visualizations and text analysis results to the console.

## ⚠️ Considerations

- Ensure datasets are formatted correctly as expected by the script.
- The script focuses on English text processing; adjust for other languages accordingly.
- Large datasets may require significant memory and processing time.
  
## 🚧 Limitations

- Detailed EDA and text processing; advanced analysis may require additional techniques.
- TextBlob sentiment analysis provides a simple, rule-based approach.  

## 🤝 Contributing

- Contributions are welcome! If you have any suggestions or improvements, please create a pull request or open an issue.
