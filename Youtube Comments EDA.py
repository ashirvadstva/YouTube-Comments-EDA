#!/usr/bin/env python
# coding: utf-8

# # Import necessary libraries

# In[1]:


import numpy as np  # For numerical operations
import pandas as pd  # For data manipulation and analysis
import seaborn as sns  # For statistical data visualization
import matplotlib.pyplot as plt  # For plotting and visualizing data
import re  # For working with regular expressions
from textblob import TextBlob  # For text processing


# # Load the datasets

# In[2]:


df_videos = pd.read_csv("GBvideos.csv", error_bad_lines=False)
df_comments = pd.read_csv("GBcomments.csv", error_bad_lines=False)


# ### Display the first few rows of the datasets

# In[3]:


df_videos.head()


# In[4]:


df_comments.head()


# ### Display the shape and columns of the datasets

# In[5]:


df_videos.shape


# In[6]:


df_videos.columns


# In[7]:


df_videos.isnull().sum()


# In[8]:


df_comments.shape


# In[9]:


df_comments.columns


# ### Convert likes and replies columns to integer type

# In[10]:


df_comments.likes = df_comments.likes.astype(int)
df_comments.replies = df_comments.replies.astype(int)


# ### Convert comment text to lower case

# In[11]:


df_comments["comment_text"] = df_comments["comment_text"].str.lower()
df_comments.head()


# ### Remove punctuations from comments

# In[12]:


import string

PUNCT_TO_REMOVE = string.punctuation #Define the punctuation characters to remove

# Define a function to remove punctuation from text
def remove_punctuation(text):
    if isinstance(text, str):  # Check if the input is a string
        return text.translate(str.maketrans('', '', PUNCT_TO_REMOVE))
    else:
        return text  # Return the input unchanged if it is not a string

df_comments["comment_text"] = df_comments["comment_text"].apply(remove_punctuation)# Apply the function to remove punctuation
df_comments.head()


# ### Remove digits from comments

# In[13]:


from string import digits

# Define a function 'remove_digits' that removes all digits from the input text
def remove_digits(text):
    if isinstance(text, str):  # Check if the input is a string
        return text.translate(str.maketrans('', '', digits))
    else:
        return str(text)  # Convert non-string input (like NaN) to string and return

# Apply the 'remove_digits' function to each element in the 'comment_text' column of the df_comments DataFrame
df_comments["comment_text"] = df_comments["comment_text"].apply(remove_digits)

df_comments.head()


# ### Remove emojis from comments

# In[14]:


def remove_emoji(text):
    emoji_pattern = re.compile("["
                               "\U0001F600-\U0001F64F"  # emoticons
                               "\U0001F300-\U0001F5FF"  # symbols & pictographs
                               "\U0001F680-\U0001F6FF"  # transport & map symbols
                               "\U0001F1E0-\U0001F1FF"  # flags (iOS)
                               "\U00002702-\U000027B0"
                               "\U000024C2-\U0001F251"
                               "]+", flags=re.UNICODE)
    return emoji_pattern.sub(r'', text)

# Apply the remove_emoji function directly to each entry in the 'comment_text' column
df_comments["comment_text"] = df_comments["comment_text"].apply(remove_emoji)

# Displaying the first few rows of the DataFrame to verify the changes
df_comments.head()


# In[15]:


# Applying a lambda function to each element in the 'comment_text' column of the df_comments DataFrame
df_comments['comment_text'] = df_comments['comment_text'].apply(lambda x: ' '.join([w for w in x.split() if len(w)>3]))


# In[16]:


# Using the 'str.replace' method to replace non-alphabetic characters (excluding '#' symbols) with spaces
df_comments['comment_text'] = df_comments['comment_text'].str.replace("[^a-zA-Z#]", " ")


# In[17]:


df_comments.head()


# In[30]:


import plotly.express as px

# Grouping by 'video_id' and 'channel_title', counting occurrences, and resetting index
new_df = df_videos.groupby(['video_id', 'channel_title']).size().reset_index(name='counts')

# Sorting by 'counts' in descending order and selecting the top 10 rows
new_df = new_df.sort_values(by='counts', ascending=False).head(10)

# Define pastel colors for the bars
pastel_colors = px.colors.qualitative.Pastel[:10]  # Using pastel shades from Plotly color palette

# Creating a bar plot using Plotly Express
fig = px.bar(new_df, x="video_id", y="counts", color='channel_title',
             color_discrete_map={channel: color for channel, color in zip(new_df['channel_title'], pastel_colors)},
             title="Top 10 Videos by View Count",
             labels={'video_id': 'Video ID', 'counts': 'View Count', 'channel_title': 'Channel Title'})

# Adjusting layout for better readability
fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide', xaxis_tickangle=-60)

# Displaying the plot
fig.show()


# In[20]:


#lets count the number of data with each type
from textblob import TextBlob


# In[21]:


# Define a function to get the sentiment polarity of a comment
def get_sentiment(text):
    if isinstance(text, str):  # Check if the input is a string
        analysis = TextBlob(text)
        return analysis.sentiment.polarity
    else:
        return 0.0  # Return 0.0 for non-string inputs


# In[25]:


# Apply the function to get the polarity of each comment
df_comments['polarity'] = df_comments['comment_text'].apply(get_sentiment)

# Categorize comments based on their polarity
def categorize_sentiment(polarity):
    if polarity > 0:
        return 1  # Positive
    elif polarity < 0:
        return -1  # Negative
    else:
        return 0  # Neutral

# Apply the function to categorize each comment
df_comments['pol'] = df_comments['polarity'].apply(categorize_sentiment)


# In[26]:


# Initialize lists to store the results
id_list = []
pos_comm = []
neg_comm = []
neutral_comm = []

# Loop through each unique video_id
for i in df_comments['video_id'].unique():
    id_list.append(i)
    comments = df_comments[df_comments['video_id'] == i]['pol']
    pos_count = comments.value_counts().get(1, 0)
    neg_count = comments.value_counts().get(-1, 0)
    neutral_count = comments.value_counts().get(0, 0)
    pos_comm.append(pos_count)
    neg_comm.append(neg_count)
    neutral_comm.append(neutral_count)


# In[27]:


# Create a DataFrame to store the results
df_unique = pd.DataFrame({
    'id': id_list,
    'pos_comm': pos_comm,
    'neg_comm': neg_comm,
    'neutral_comm': neutral_comm
})

# Calculate the total number of comments
df_unique['total_comments'] = df_unique['pos_comm'] + df_unique['neg_comm'] + df_unique['neutral_comm']

df_unique.head(6)


# In[28]:


# Save the DataFrame to a CSV file for further analysis
df_unique.to_csv('unique.csv', index=False)

unique = pd.read_csv('unique.csv')

# Display the top 5 videos with the most positive comments
unique.sort_values(by='pos_comm', ascending=False).head(5)


# In[32]:


import matplotlib.pyplot as plt

# Creating a color map based on the unique comment types
color_map = {'positive': 'greenyellow', 'Neutral': 'skyblue', 'negative': 'coral'}

# Replacing the values and getting the counts
counts = df_comments['pol'].replace({1: 'positive', 0: 'Neutral', -1: 'negative'}).value_counts()

# Plotting the bar chart with specified colors
counts.plot(kind='bar', figsize=(7, 4), color=[color_map[val] for val in counts.index])

# Adding titles and labels
plt.title('Number of types of comments')
plt.xlabel('Comment_type')
plt.ylabel('Number')
plt.show()


# In[33]:


# Ensure the plot size is set before creating the plot
plt.figure(figsize=(10, 6))

# Plotting the top 10 videos with the most positive comments
sns.barplot(data=unique.sort_values(by='pos_comm', ascending=False).head(10), x='id', y='pos_comm', palette='viridis')

# Rotate x-ticks for better readability
plt.xticks(rotation=45)

# Adding titles and labels
plt.title('Top 10 Videos with the Most Positive Comments')
plt.xlabel('Video ID')
plt.ylabel('Number of Positive Comments')

# Display the plot
plt.show()


# In[34]:


# Set the plot size before creating the plot
plt.figure(figsize=(10, 6))

# Plotting the top 10 videos with the most negative comments
sns.barplot(data=unique.sort_values(by='neg_comm', ascending=False).head(10), x='id', y='neg_comm', palette='rocket')

# Rotate x-ticks for better readability
plt.xticks(rotation=45)

# Adding titles and labels
plt.title('Top 10 Videos with the Most Negative Comments')
plt.xlabel('Video ID')
plt.ylabel('Number of Negative Comments')
plt.show()


# In[35]:


plt.figure(figsize=(10, 6))

# Plotting the top 10 videos with the most total comments
sns.barplot(data=unique.sort_values(by='total_comments', ascending=False).head(10), x='id', y='total_comments', palette='summer_r')

# Rotate x-ticks for better readability
plt.xticks(rotation=45)

# Adding titles and labels
plt.title('Top 10 Videos with the Most Total Comments')
plt.xlabel('Video ID')
plt.ylabel('Number of Total Comments')
plt.show()


# In[36]:


# Define a dictionary to map category IDs to category names
cat_id_mapping = {
    2: 'Autos & Vehicles', 1: 'Film & Animation',
    10: 'Music', 15: 'Pets & Animals', 17: 'Sports',
    19: 'Travel & Events', 20: 'Gaming', 22: 'People & Blogs',
    23: 'Comedy', 24: 'Entertainment', 25: 'News & Politics',
    26: 'Howto & Style', 27: 'Education', 28: 'Science & Technology',
    29: 'Nonprofits & Activism', 43: 'Shows'
}


# In[37]:


# Group videos by category and count the number of videos in each category
df_videos_gb = df_videos.groupby('category_id').count()['title']
df_videos_gb = df_videos_gb.rename(cat_id_mapping)

# Plot the number of videos in each category
ax = df_videos_gb.plot(kind='bar', title='Video Categories by their Count', color='orange', figsize=(10,5))
ax.set_xlabel('Category')
ax.set_ylabel('Count')

df_videos_gb

