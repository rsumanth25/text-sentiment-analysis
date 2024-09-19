
import matplotlib.pyplot as plt
import re
from ntscraper import Nitter

def get_tweet(query, modes, no_of_tweets):
    scraper = Nitter()
    tweets = scraper.get_tweets(query, mode= modes, number=no_of_tweets)
    final_tweets = []
    for tweet in tweets['tweets']:
        final_tweets.append(tweet['text'])
    return final_tweets

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
    for tweet in tweets:
        clean_tweet = re.sub("[^A-Za-z ]","", tweet)
        word_list = clean_tweet.strip().split()
        for word in word_list :
            list_of_words.append(word)
    
    #loading stopwords
    stop_words = (
        "a", "able", "about", "above", "across", "after", "again", "against", "all", "almost", "alone", "along", "already", "also", "although", "always", "am", "among", "an", "and", "any", "anybody", "anyhow", "anyone", "anything", "anywhere", "are", "around", "as", "at", "be", "because", "been", "before", "being", "below", "between", "beyond", "both", "but", "by", "can", "cannot", "could", "did", "do", "does", "doing", "don't", "down", "during", "each", "either", "else", "especially", "even", "ever", "every", "everybody", "everyone", "everything", "everywhere", "except", "for", "from", "further", "had", "hasn", "havent", "having", "he", "her", "here", "hers", "herself", "him", "himself", "his", "how", "however", "i", "if", "in", "into", "it", "its", "itself", "just", "keep", "lets", "like", "likely", "little", "looking", "may", "maybe", "me", "might", "more", "most", "mustnt", "my", "myself", "namely", "neither", "never", "nevertheless", "new", "no", "nobody", "none", "noone", "nor", "not", "nothing", "now", "nowhere", "of", "off", "on", "once", "only", "onto", "or", "other", "otherwise", "ought", "our", "ours", "ourselves", "out", "over", "own", "quite", "rather", "really", "said", "same", "say", "seeing", "seems", "should", "shouldnt", "since", "so", "some", "somebody", "someone", "something", "somewhere", "still", "such", "than", "that", "the", "their", "theirs", "them", "themselves", "then", "there", "therefore", "these", "they", "they'd", "they'll", "they're", "they've", "think", "though", "thoroughly", "through", "throughout", "thus", "to", "together", "too", "towards", "under", "until", "up", "upon", "us", "very", "was", "wasn't", "we", "we'd", "we'll", "we're", "we've", "well", "what", "when", "whenever", "where", "whereas", "wherever", "which", "while", "who", "whom", "whose", "why", "with", "within", "without", "would", "wouldn't", "you", "you'd", "you'll", "you're", "you've", "your", "yours", "yourself", "i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself","yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself","they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these","those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while","of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before", "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again", "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each", "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than", "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"
    )

    #removing stop word from the text
    final_words=[]
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

    # checking if the emotion representing word are there in the text
    emotions_found = {}
    for word in final_words:
        if word in emotion_dict:
            #adding the found emotions to the dictonary managing the counts of the emotinal word types
            if emotion_dict[word] in emotions_found:
                emotions_found[(emotion_dict[word])] += 1
            else: 
                emotions_found[(emotion_dict[word])] = 1

    plt.bar(emotions_found.keys(), emotions_found.values())
    plt.xticks(rotation = 15)
    plt.savefig('twitter_senti.png')

if __name__ == "__main__": 
    main()