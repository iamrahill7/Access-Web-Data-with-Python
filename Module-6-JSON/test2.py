import urllib.request
import urllib.parse
import json

# Step 1: Prompt the user for a location
location = input("Enter location: ")

# Step 2: Construct the API URL
base_url = "http://py4e-data.dr-chuck.net/opengeo?"
params = {"q": location}
url = base_url + urllib.parse.urlencode(params)

print("Retrieving", url)

# Step 3: Retrieve the JSON data
response = urllib.request.urlopen(url)
data = response.read().decode()
print("Retrieved", len(data), "characters")

# Step 4: Parse the JSON data
try:
    js = json.loads(data)
except:
    js = None

# Step 5: Extract the Plus Code
if js and 'features' in js and len(js['features']) > 0:
    plus_code = js['features'][0]['properties']['plus_code']
    print("Plus code", plus_code)
else:
    print("No plus code found for the given location.")