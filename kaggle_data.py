import csv
import sys

datelist = sys.argv[1].split(",")
keywordlist = sys.argv[2].split(",")

fw = open('data_2014.csv', 'wb')
fieldnames = ['date', 'headline']
writer = csv.DictWriter(fw, fieldnames=fieldnames)
writer.writeheader()

with open('abcnews-date-text.csv', 'rb') as csvfile:
	spamreader = csv.DictReader(csvfile)
	for row in spamreader:
		if ( any(word in row['publish_date'] for word in datelist) and any(word in row['headline_text'].lower() for word in keywordlist)):
			writer.writerow({'date': row['publish_date'], 'headline': row['headline_text']})