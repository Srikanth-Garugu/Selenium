from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up Chrome options
chrome_options = webdriver.ChromeOptions()
# Add any additional options if needed, e.g., headless mode
# chrome_options.add_argument("--headless")

# Create the WebDriver instance with ChromeOptions
driver = webdriver.Chrome(options=chrome_options)

# Navigate to the corrected website URL
driver.get("https://www.amazon.in")

# Use WebDriverWait to wait for the search box to be present on the page
try:
    search_box = WebDriverWait(driver, 500).until(
        EC.presence_of_element_located((By.ID, "search-box"))
    )

    # Perform interactions with the search box
    search_box.send_keys("Automation with Selenium")
    search_box.submit()

    # Wait for a while to see the changes (you can adjust this)
    driver.implicitly_wait(10)

except Exception as e:
    print(f"An error occurred: {e}")

# Close the browser
driver.quit()
