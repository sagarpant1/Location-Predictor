# Team - Ankita, Sagar, Meghesh, 2017
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

import sys
import heapq

tweetCount = 0
locationDict = {}
allCities = []
def readData(fileName, type):
    file = open(fileName, "r")
    writeFile = open(outputFile, "w")
    if type == 'train':
	global tweetCount
    count=0
    for line in file:
	line = line.rstrip('\n')
	if type == 'train':
	    tweetCount = tweetCount + 1
	    populateToDict(line)
	else:
	    foundCity = predictCity(line.lower())
	    writeFile.write(foundCity + " " + line + "\n")
    writeFile.close()


def populateToDict(line):
    line1 = line
    line = line.lower()
    data = line.split(" ")
    data1 = line1.split(" ")
    if data1[0] not in locationDict:
	locationDict[data1[0]] = [1, 0, {}]
	allCities.extend([data1[0]])
    else:
	cityList = locationDict.get(data1[0])
	cityList[0] = cityList[0] + 1
	locationDict[data1[0]] = cityList
    
    for i in range(1,len(data)):
	if len(data[i]) > 1:
	    data[i] = formatString(data[i])
	    cityList = locationDict.get(data1[0])
	    if data[i] not in cityList[2]:
	    	cityList[2][data[i]] = 1
	    else:
	    	cityList[2][data[i]] = cityList[2].get(data[i]) + 1
	    cityList[1] = cityList[1] + 1
	    locationDict[data1[0]] = cityList

def predictCity(line):
    data = line.split(" ")
    maxChance = 0
    maxChanceCity = ""
    for i in range(0,len(allCities)):
	chance = 1.0
	if allCities[i] in locationDict:
	    dict = locationDict.get(allCities[i])
	    for j in range(1, len(data)):
		data[j] = formatString(data[j])
		if data[j] not in dict[2]:
		    numerator = 10**(-2)
		else:
		    numerator = dict[2].get(data[j])
		    if '#' in data[j]:
			numerator = numerator * 50
		chance = (chance * numerator)/dict[1]
	    chance = (chance * dict[1])/tweetCount
	    if chance > maxChance:
		maxChance = chance
		maxChanceCity = allCities[i]		
    return maxChanceCity

def printCities():
    for key in locationDict:
	maxCount = []
	val = locationDict.get(key)
   	dict = val[2]
	for k in dict:
	    heapq.heappush(maxCount, (dict.get(k), k))
	print "Top Words in %s are:" %key
	for i in range(0,5):
	    print heapq.heappop(maxCount)[1]

def formatString(word):
    word = word.strip()
    word = word.replace("-","")
    word = word.replace("_","")
    word = word.replace("\r","")
    word = word.replace(".","")
    word = word.replace("!","")
    word = word.replace("\"","")
    word = word.replace("##","#")
    word = word.replace("*","")
    return word
     
outputFile = str(sys.argv[3])
readData(str(sys.argv[1]), "train")
readData(str(sys.argv[2]), "test")
printCities()
