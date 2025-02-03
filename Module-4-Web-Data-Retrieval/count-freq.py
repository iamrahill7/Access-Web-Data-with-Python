import urllib.request

# URL to fetch data from
url = "http://data.pr4e.org/romeo.txt"  # A simple text file

# Open the URL and read content
response = urllib.request.urlopen(url)

# Create an empty dictionary for word counts
counts = dict()

# Process each line in the response
for line in response:
    words = line.decode().split()  # Decode and split into words
    for word in words:
        counts[word] = counts.get(word, 0) + 1  # Count word occurrences

print(counts)
