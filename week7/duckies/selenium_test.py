import configparser
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Initialize the WebDriver (adjust the path to your chromedriver is necessary)
driver = webdriver.Chrome()

# Load configuration
config = configparser.ConfigParser()
config.read("app.ini")
port = config.getint("server", "port")

try:
    # Test 1: Add a Duck
    def test_add_duck():
        driver.get("http://localhost:5005")

        # Fill in the form for adding a duck
        driver.find_element(By.ID, "duckName").send_keys("Test Duck")
        driver.find_element(By.ID, "duckColor").send_keys("Blue")
        driver.find_element(By.ID, "duckSize").send_keys("Medium")
        driver.find_element(By.ID, "duckRarity").send_keys("Unique")

        # Click the Add Duck button
        driver.find_element(By.ID, "addDuckButton").click()

        # Allow some time for AJAX call to complete
        time.sleep(1)

        # Verify that the message "Duck added!" appears
        message = driver.find_element(By.CSS_SELECTOR, "#addResult").text
        assert "Test Duck added successfully" in message, "Failed to add duck!"

    # Test 2: Search for a Duck
    def test_search_duck():
        driver.get("http://localhost:5005")

        # Fill in the search form
        driver.find_element(By.ID, "searchName").send_keys("Test Duck")

        # Click the Search Duck button
        driver.find_element(By.ID, "searchDuckButton").click()

        # Allow some time for AJAX call to complete
        time.sleep(1)

        # Verify that the duck's details appear
        message = driver.find_element(By.ID, "searchResult").text
        assert "Duck found:" in message, "Duck not found!"

    # Run tests
    test_add_duck()
    test_search_duck()

finally:
    # Close the WebDriver
    driver.quit()
