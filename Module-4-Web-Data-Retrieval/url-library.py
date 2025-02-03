# ================================
# Fetching a Web Page Using `urllib.request`
# ================================

import urllib.request  # Import the module for handling web requests

# ---------------------------------
# Step 1: Define the Target URL
# ---------------------------------
url = "https://www.trivago.in"  # Ensure the URL is correct

# -----------------------------------------------
# Step 2: Define Headers to Mimic a Real Browser
# -----------------------------------------------
# This avoids the 403 Forbidden error from the website
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

# ----------------------------------------------------
# Step 3: Create a Request Object with the Headers
# ----------------------------------------------------
req = urllib.request.Request(url, headers=headers)

# ----------------------------------------------------
# Step 4: Open the URL with the Modified Request
# ----------------------------------------------------
response = urllib.request.urlopen(req)

# ---------------------------------------------
# Step 5: Print Response Headers (Metadata)
# ---------------------------------------------
print(response.info())

# -------------------------------
# Optional: Fetch and Display Content
# -------------------------------
# Uncomment the following lines to fetch and display the page content:

# Read the raw HTML content of the webpage (in bytes)
# html = response.read()

# Decode bytes to a human-readable string (UTF-8 text)
# print(html.decode())  # Print the webpage content

 