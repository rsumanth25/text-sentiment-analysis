#Cleaning of the data
import string
import matplotlib.pyplot as plt
import re

with open('read.txt', encoding='utf-8') as readfile:
    text = readfile.read().lower()

clean_words = text.translate(str.maketrans('', '', string.punctuation))
# alternative to translate clean_words = re.sub("[^A-Za-z ]","",text)

#tokenization
list_of_words = clean_words.strip().split()

#loading stopwords
stop_words = [
    "a", "able", "about", "above", "across", "after", "again", "against", "all", "almost", "alone", "along", "already", "also", "although", "always", "am", "among", "an", "and", "any", "anybody", "anyhow", "anyone", "anything", "anywhere", "are", "around", "as", "at", "be", "because", "been", "before", "being", "below", "between", "beyond", "both", "but", "by", "can", "cannot", "could", "did", "do", "does", "doing", "don't", "down", "during", "each", "either", "else", "especially", "even", "ever", "every", "everybody", "everyone", "everything", "everywhere", "except", "for", "from", "further", "had", "hasn", "havent", "having", "he", "her", "here", "hers", "herself", "him", "himself", "his", "how", "however", "i", "if", "in", "into", "it", "its", "itself", "just", "keep", "lets", "like", "likely", "little", "looking", "may", "maybe", "me", "might", "more", "most", "mustnt", "my", "myself", "namely", "neither", "never", "nevertheless", "new", "no", "nobody", "none", "noone", "nor", "not", "nothing", "now", "nowhere", "of", "off", "on", "once", "only", "onto", "or", "other", "otherwise", "ought", "our", "ours", "ourselves", "out", "over", "own", "quite", "rather", "really", "said", "same", "say", "seeing", "seems", "should", "shouldnt", "since", "so", "some", "somebody", "someone", "something", "somewhere", "still", "such", "than", "that", "the", "their", "theirs", "them", "themselves", "then", "there", "therefore", "these", "they", "they'd", "they'll", "they're", "they've", "think", "though", "thoroughly", "through", "throughout", "thus", "to", "together", "too", "towards", "under", "until", "up", "upon", "us", "very", "was", "wasn't", "we", "we'd", "we'll", "we're", "we've", "well", "what", "when", "whenever", "where", "whereas", "wherever", "which", "while", "who", "whom", "whose", "why", "with", "within", "without", "would", "wouldn't", "you", "you'd", "you'll", "you're", "you've", "your", "yours", "yourself"
]

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

print(emotions_found)
plt.bar(emotions_found.keys(), emotions_found.values())
plt.xticks(rotation = 15)
plt.savefig('text_sentiments_graph.png')