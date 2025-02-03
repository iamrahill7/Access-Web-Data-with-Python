

import urllib.request
import urllib.parse
import urllib.error
from bs4 import BeautifulSoup

# Step 1: Get inputs
url = input("Enter URL: ")
count = int(input("Enter count: "))  # How many times to repeat
position = int(input("Enter position: "))  # Which link to follow (1-based index)

# Step 2: Follow links the given number of times
for i in range(count):
    print("Retrieving:", url)  # Print the current URL
    
    # Read the HTML
    html = urllib.request.urlopen(url).read()
    
    # Parse with BeautifulSoup
    soup = BeautifulSoup(html, "html.parser")
    
    # Step 3: Extract all anchor tags (<a> tags)
    tags = soup("a")
    
    # Step 4: Pick the link at the given position (convert 1-based to 0-based index)
    url = tags[position - 1].get("href", None)

# Print the final name (last retrieved URL's name part)
print("Last name in sequence:", url.split("_")[-1].split(".")[0])
