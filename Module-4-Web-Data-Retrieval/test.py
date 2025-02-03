## Task: You are given a webpage containing a list of names and numbers inside <span> tags. Your task is to:

## Extract all the numbers inside <span> tags.

## Add up all those numbers to get the total sum.

## Print the count of numbers and the total sum.

import urllib.request
import urllib .parse
import urllib.error
from bs4 import BeautifulSoup

# Prompt user for URL
url = input("Enter -")
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all span tags and sum their contents
sum_numbers = 0
count = 0

tags = soup("span")
for tag in tags:
    num = int(tag.text) # Extractnumber and convert to int
    sum_numbers += num
    count += 1


print("Count", count)
print("Sum", sum_numbers) 
