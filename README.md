# 📊 YouTube Comments Exploratory Data Analysis (EDA)

Welcome to the **"YouTube Comments Exploratory Data Analysis (EDA)"** repository. This project delves into detailed EDA on YouTube comments, focusing on text processing techniques and sentiment analysis to extract valuable insights.

## 📝 Project Description

This project aims to analyze YouTube comments to understand viewer sentiments and engagement trends. Key tasks include:
- **Data Importation**: Loading datasets and handling missing values.
- **Text Preprocessing**: Normalizing text by converting to lowercase and removing punctuation and digits.
- **Sentiment Analysis**: Utilizing the TextBlob library to determine the sentiment of comments.
- **Visualization**: Creating visualizations to represent viewer feedback and engagement.

## 🔍 Key Findings

Below are some of the significant visualizations generated from the EDA:

<div style="display: flex; justify-content: space-between;">
  <img src="https://github.com/user-attachments/assets/c2201879-02ba-44c2-aae2-b7083e76d60f" alt="Top 10 Videos by View Count" width="33%" />
  <img src="https://github.com/user-attachments/assets/a40985af-c658-4838-a86e-962e05f49109" alt="Top 10 Videos with the Most Negative Comments" width="33%" />
  <img src="https://github.com/user-attachments/assets/a231773b-474b-4758-aac7-bc42a7ed39cd" alt="Top 10 Videos with the Most Positive Comments" width="33%" />
</div>

## 🌟 Key Features

- **📥 Data Loading**: Import YouTube video and comment datasets from CSV files.
- **🧹 Data Cleaning**: Preprocess text data, handle missing values, and remove unnecessary characters.
- **📝 Text Analysis**: Conduct sentiment analysis using TextBlob.
- **📊 Visualization**: Leverage seaborn and matplotlib to create insightful data visualizations.

## 🎯 Target Audience

- **Data Scientists**: Interested in text analysis and natural language processing (NLP).
- **Machine Learning Enthusiasts**: Exploring text data preprocessing for ML models.
- **YouTube Content Creators**: Seeking insights from viewer comments to improve engagement.
- **Researchers**: Analyzing social media data and user interaction patterns.

## 🚀 Getting Started

1. **Clone the Repository**:
   \`\`\`bash
   git clone <https://github.com/ashirvadstva/YouTube-Comments-EDA>
   \`\`\`
2. **Install Dependencies**:
   \`\`\`bash
   pip install pandas numpy seaborn matplotlib textblob
   \`\`\`
3. **Run the Script**:
   \`\`\`bash
   python Youtube_Comments_EDA.py
   \`\`\`

## 🛠️ Usage

- Place datasets (e.g., `GBvideos.csv`, `GBcomments.csv`) in the same directory as the script.
- Execute the script to generate visualizations and sentiment analysis.

## ⚠️ Considerations

- Ensure datasets are correctly formatted.
- The analysis primarily targets English text; other languages may require adjustments.
- Processing large datasets may demand significant computational resources.

## 🚧 Limitations

- This EDA focuses on basic text processing and sentiment analysis. More complex analyses might need advanced techniques.
- TextBlob provides a rule-based sentiment analysis approach, which may have limitations in nuanced text.

## 🤝 Contributing

Contributions are highly appreciated! Feel free to create a pull request or open an issue for any suggestions or improvements.

