import urllib.request
import xml.etree.ElementTree as ET

# Prompt for the URL
url = input('Enter location: ')

# Fetch the XML data from the URL
print(f'Retrieving {url}')
xml_data = urllib.request.urlopen(url).read()

# Parse the XML data
tree = ET.fromstring(xml_data)

# Find all 'count' tags using XPath
counts = tree.findall('.//count')

# Output the number of 'count' tags found
print(f'Retrieved {len(xml_data)} characters')
print(f'Count: {len(counts)}')

# Compute the sum of the 'count' values
total = 0
for count in counts:
    total += int(count.text)

# Output the sum
print(f'Sum: {total}')
