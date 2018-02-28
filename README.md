# Location-Predictor-for-Twitter-Tweets
Implemented a python algorithm that predicts the city from which the tweet was made with an accuracy of ~70% on a noisy data using the Naïve Bayes approach.

# geolocate.py: To predict the city from which the tweet was made by training it over a given train data. In addition to it print the highest frequency words
# in a tweet for each of the 12 locations.
#
# We have created a dictionary to store the data corresponding to each location. This dictionary contains an array as its value while the city names as its key.
#The array contains the #ThatCityAppearedInTheTweets, #Words in all the tweets from that city and the third element of the array is a dictionary in itself.
#It contains the words as the key and their frequency as its value.
#Using all the above-calculated data, we can compute the probability of getting a location when the probability of the words is given by using Naive Bayes formula.

#Methods used to improve the prediction are:
#1) Eliminate all single character words.
#2) Strip the word off '-','_','\r','.','!','\' and '*'
#3) Assigning heavyweight to the words containing #(hash symbol)
#4) Associating each non-occurring word with a punishment (here we have used 10^-2 as the multiplication factor).
