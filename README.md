# 📊 YouTube Comments Exploratory Data Analysis (EDA)

## 📝 Description

This project performs detailed Exploratory Data Analysis (EDA) on YouTube comments. The analysis involves loading datasets, cleaning and preprocessing the data, and extracting meaningful insights from YouTube video comments. The script focuses on text processing techniques such as converting text to lowercase, removing punctuation and digits, and performing sentiment analysis using the TextBlob library.

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
