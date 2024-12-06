import requests
from bs4 import BeautifulSoup
import csv

# URL of the hospital pricing page
url = "https://example-hospital.com/pricing"

# Send a GET request
response = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.text, "html.parser")

# Extract table data
pricing_table = soup.find("table", {"id": "pricing-table"})

# Get table headers
headers = [header.text for header in pricing_table.find_all("th")]

# Extract table rows
rows = pricing_table.find_all("tr")

# Extract data from rows
data = []
for row in rows[1:]:  # Skip the header row
    cols = [col.text.strip() for col in row.find_all("td")]
    data.append(cols)

# Write to a CSV file
with open("hospital_pricing.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(headers)  # Write headers
    writer.writerows(data)    # Write data

print("Data has been scraped and saved to hospital_pricing.csv.")
