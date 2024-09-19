
import matplotlib.pyplot as plt
import re
from ntscraper import Nitter
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer
def get_tweet(query, modes, no_of_tweets):
    scraper = Nitter()
    tweets = scraper.get_tweets(query, mode= modes, number=no_of_tweets)
    final_tweets = []
    for tweet in tweets['tweets']:
        final_tweets.append(tweet['text'])
    return final_tweets

def sentiment_intensity_analyser(text):
    score = SentimentIntensityAnalyzer().polarity_scores(text)
    return score 

def main() :   
    while True:
        try :
            print("QUERY DETAILS\n")
            query = input("Search query you want scrape tweets for : ").strip().lower()
            modes = input("Is the search query hashtag, term, or username.\nPlease type as h/t/u : ").strip().lower()
            no_of_tweets = int(input("Total no of tweets you want to scarpe for sentiment analysis\nPlease provide whole natural number only: "))

            if modes == 'h' :
                mode = "hashtag"
            elif modes== 't' :
                mode = "term"
            elif modes == 'u' :
                mode = "user"
            else:
                raise ValueError
            
            break
        except ValueError :
            print("\n \n PLEASE ENTER THE CORRECT QUERY INPUTS")

    # cleaning and tokenisation

    list_of_words = []
    tweets = get_tweet(query, mode, no_of_tweets)
    all_tweets = "".join(tweets)
    clean_tweet = re.sub("[^A-Za-z ]","", all_tweets)
    tokenized_words = word_tokenize(clean_tweet, "english")
    for word in tokenized_words :
        list_of_words.append(word)
    
    # getting sentiment intensity scores 
    scores = sentiment_intensity_analyser(clean_tweet)
    if scores['compound'] > 0.05:
        sentiment = "Positive"
    elif scores['compound'] < -0.05:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"
        
    print(f"Analysis Summary:")
    print(f"Negative Score: {scores['neg']}")
    print(f"Neutral Score: {scores['neu']}")
    print(f"Positive Score: {scores['pos']}")
    print(f"Compound Score: {scores['compound']} (Overall Sentiment: {sentiment})")

    #removing stop word from the text
    final_words=[]
    stop_words = list(stopwords.words('english'))
    for word in list_of_words:
        if word not in stop_words:
            final_words.append(word)

    # reading emotions data
    emotion_dict = {}
    with open('emotions.txt', 'r') as emotion_file:
        lines = emotion_file.readlines()
        for line in lines:
            a, b = line.strip().split(':')
            a = re.sub("[^A-Za-z ]","",a)
            b = re.sub("[^A-Za-z ]","",b)
            emotion_dict[a.strip()] = b.strip()

    # # checking if the emotion representing word are there in the text
    emotions_found = {}
    for word in final_words:
        if word in emotion_dict:
            #adding the found emotions to the dictonary managing the counts of the emotinal word types
            if emotion_dict[word] in emotions_found:
                emotions_found[(emotion_dict[word])] += 1
            else: 
                emotions_found[(emotion_dict[word])] = 1
    print(f"Emotions founds {emotions_found}")

    # plotting sentiment scores
    plt.figure()
    # Prepare data for plotting
    labels = list(scores.keys())
    values = list(scores.values())

    # Create a bar plot
    plt.bar(labels, values, color=['red', 'yellow', 'green', 'blue'])

    # Add title and labels
    plt.title('Sentiment Scores')
    plt.xlabel('Sentiment Categories')
    plt.ylabel('Scores')

    # Display the plot
    plt.savefig("sentiment scores")

if __name__ == "__main__": 
    main()