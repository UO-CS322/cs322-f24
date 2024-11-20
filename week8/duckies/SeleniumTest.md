# Testing Web Interfaces with Selenium

Selenium can be used to test the front-end functionality of web applications by automating browser actions. Below, I'll demonstrate how to write two simple Selenium tests for the Duckies application. These tests will interact with the web page to simulate user actions

Official getting started page: https://selenium-python.readthedocs.io/getting-started.html (also contains information on prerequisites for your specific system and browser.)

Ensure you have Selenium installed (add to `requirements.txt`)

```bash
pip install selenium
```

Make sure your application is running locally or deployed somewhere you can access for testing.

## Test Cases
Below are two simple Selenium tests using Python. These assume that your application is running at http://localhost:5005.

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Initialize the WebDriver (adjust the path to your chromedriver is necessary)
driver = webdriver.Chrome()

try:
    # Test 1: Add a Duck
    def test_add_duck():
        driver.get(f"http://localhost:5005")
        
        # Fill in the form for adding a duck
        driver.find_element(By.ID, 'duckName').send_keys('Test Duck')
        driver.find_element(By.ID, 'duckColor').send_keys('Blue')
        driver.find_element(By.ID, 'duckSize').send_keys('Medium')
        driver.find_element(By.ID, 'duckRarity').send_keys('Unique')
        
        # Click the Add Duck button
        driver.find_element(By.ID, 'addDuckButton').click()

        # Allow some time for AJAX call to complete
        time.sleep(1)
        
        # Verify that the message "Duck added!" appears
        message = driver.find_element(By.CSS_SELECTOR, '#searchResult').text 
        assert "Duck added!" in message, "Failed to add duck!"
    
    # Test 2: Search for a Duck
    def test_search_duck():
        driver.get("http://localhost:5005")
        
        # Fill in the search form
        driver.find_element(By.ID, 'searchName').send_keys('Test Duck')

        # Click the Search Duck button
        driver.find_element(By.ID, 'searchDuckButton').click()

        # Allow some time for AJAX call to complete
        time.sleep(1)
        
        # Verify that the duck's details appear
        message = driver.find_element(By.ID, 'searchResult').text
        assert "Duck found:" in message, "Duck not found!"

    # Run tests
    test_add_duck()
    test_search_duck()

finally:
    # Close the WebDriver
    driver.quit()
```

## Explanation

### WebDriver Initialization:

`webdriver.Chrome()`: Initializes a new Chrome WebDriver. You may need to adjust this if you're using a different browser (google for webdriver)

#### Test 1 - Add a Duck:

Opens the application page, fills out the form to add a duck, and simulates a button click.
Verifies the success message indicating a duck was added.

#### Test 2 - Search for a Duck:

Opens the application page, enters a search term, and simulates a search button click.
Verifies the message or details indicating the duck was found.

#### Assertions:

`assert` statements check whether the expected conditions are met, providing feedback if they aren't.

#### Teardown:

Ensures the browser is closed after tests run (`driver.quit()`), even if an error occurs.

/Co-authored with GPT4o/