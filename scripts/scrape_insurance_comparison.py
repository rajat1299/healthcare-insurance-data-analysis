from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

# Set up Selenium WebDriver
driver = webdriver.Chrome()

# URL of the comparison page
url = "https://example-comparison.com/insurance"

# Open the URL
driver.get(url)

# Extract table data
rows = driver.find_elements(By.CSS_SELECTOR, "table#comparison-table tr")
data = []

# Extract headers
headers = [header.text for header in rows[0].find_elements(By.TAG_NAME, "th")]

# Extract rows
for row in rows[1:]:
    cols = [col.text for col in row.find_elements(By.TAG_NAME, "td")]
    data.append(cols)

# Save to a DataFrame
df = pd.DataFrame(data, columns=headers)

# Save to a CSV file
df.to_csv("insurance_comparison.csv", index=False)

print("Data saved to insurance_comparison.csv.")

# Close the browser
driver.quit()
