# text-sentiment-analysis
Text Sentiment Analysis project using Python, featuring two approaches: NLTK-based and manual methods. Analyzes tweet sentiments and detects emotions, with results visualized in bar charts. Capstone Final project for CS50x.

# Text Sentiment Analysis Project

#### Description:

This project is a text sentiment analysis tool designed as the final project for the CS50x course. It is implemented using two different approaches: one using the Natural Language Toolkit (NLTK) and the other employing a manual method without specialized libraries. The project demonstrates a comparative analysis of the two approaches and their effectiveness in sentiment analysis tasks.

The primary goal of this project is to analyze the sentiment of textual data, specifically focusing on tweets. The sentiment analysis categorizes the data as positive, negative, or neutral. Additionally, the project includes an emotion detection feature that identifies specific emotions in the text based on a predefined emotion dictionary.

### Features:

1. **Two Approaches to Sentiment Analysis:**
   - **NLTK-Based Approach:** Utilizes the NLTK library to scrape tweets, tokenize words, remove stopwords, and perform sentiment analysis using the VADER (Valence Aware Dictionary and Sentiment Reasoner) model.
   - **Manual Approach:** Implements a custom method for tokenization, stopword removal, and emotion detection without relying on external libraries like NLTK.

2. **Tweet Scraper:**
   - The NLTK-based program includes a tweet scraper that fetches tweets based on a user-defined query, allowing for real-time sentiment analysis of Twitter data.

3. **Emotion Detection:**
   - Both approaches include an emotion detection feature that analyzes the text to identify specific emotions (e.g., joy, anger, sadness) based on a predefined dictionary.

4. **Visualization:**
   - The results of the sentiment and emotion analysis are visualized using bar charts, providing a clear graphical representation of the findings.

### Files in the Project:

- **`twitter_sentiment_analysis_nltk.py`:** This script implements the NLTK-based approach to sentiment analysis. It includes functions for scraping tweets, cleaning and tokenizing text, removing stopwords, and analyzing sentiment using the VADER model. The results are visualized using Matplotlib.

- **`text_file_sentiment_analysis.py`and `twitter_sentiment_analysis.py`:** This script demonstrates the manual approach to sentiment analysis. It includes custom implementations for text cleaning, tokenization, stopword removal, and emotion detection. The script also generates a bar chart to visualize the detected emotions.

- **`emotions.txt`:** A text file containing a predefined dictionary of words mapped to specific emotions. This file is used in both the NLTK and manual approaches to identify and count emotions in the text.

- **`read.txt`:** A sample text file used for testing the manual sentiment analysis script. It contains raw text data that the script processes to analyze sentiment and detect emotions.

### Design Choices:

- **Choice of NLTK:** NLTK was chosen for one of the approaches due to its comprehensive set of tools for text processing and sentiment analysis. The VADER model was selected for its effectiveness in analyzing social media content, making it ideal for analyzing tweets.

- **Manual Approach:** The manual approach was implemented to showcase an understanding of the fundamental processes involved in sentiment analysis. By manually handling tasks like tokenization and stopword removal, this approach allows for greater customization and provides a clear contrast to the library-based method.

- **Emotion Detection:** The inclusion of emotion detection adds layer of analysis beyond simple sentiment categorization. This feature was chosen to provide more detailed insights into the emotional tone of the text, making the analysis more nuanced.

- **Visualization:** Matplotlib was chosen for visualizing the results due to its flexibility and ease of use in generating bar charts. The visualizations help to effectively communicate the results of the sentiment and emotion analysis.

### How to Use:

1. **Setup:**
   - Install the required dependencies by running:
     ```bash
     pip install -r requirements.txt
     ```
   - Ensure you have the necessary files (`emotions.txt`, `read.txt`) in the project directory.

2. **Running the Scripts:**
   - To run the NLTK-based sentiment analysis, in the respective directory execute:
     ```bash
     python twitter_sentiment_analysis_nltk.py
     ```
   - To run the manual sentiment analysis, execute:
     ```bash
     python text_file_sentiment_analysis.py
     ```
     or

     ```bash
      python twitter_sentiment_analysis.py

     ```

3. **Viewing Results:**
   - After running the scripts, the sentiment analysis results will be displayed in the console, and the emotion analysis results will be saved as bar charts in the project directory.

### Conclusion:

This project provides a comprehensive overview of text sentiment analysis using both library-based and manual methods. The comparison between the two approaches highlights the strengths and limitations of each method, offering valuable insights into text processing and sentiment analysis techniques.

Whether you're interested in learning about sentiment analysis or looking for a practical project to enhance your programming skills, this project serves as an excellent resource. The detailed documentation and clear code structure make it easy to understand and extend for further exploration.
