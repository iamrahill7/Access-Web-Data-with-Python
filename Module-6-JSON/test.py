import urllib.request
import json

# Prompt the user for the URL
url = input("Enter the URL: ")

# Fetch the JSON data from the URL
response = urllib.request.urlopen(url)
data = response.read().decode()

# Parse the JSON data
info = json.loads(data)

# Initialize a variable to store the sum of the comment counts
total_comments = 0

# Loop through the "comments" list and sum the "count" values
for comment in info['comments']:
    total_comments += comment['count']

# Output the sum of the comment counts
print("Sum of comment counts:", total_comments)
