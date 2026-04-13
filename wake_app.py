import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Replace this with your actual Streamlit app URL
APP_URL = "https://livelogic.streamlit.app/"

def wake_app():
    # Configure Chrome to run headlessly (required for GitHub Actions)
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")

    # Initialize the WebDriver
    print("Initializing Chrome WebDriver...")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    try:
        print(f"Visiting {APP_URL}...")
        driver.get(APP_URL)

        # Wait up to 15 seconds for the button to appear
        wait = WebDriverWait(driver, 15)
        
        # XPath targeting the specific text on the Streamlit sleeping page
        button_xpath = "//button[contains(text(), 'Yes, get this app back up!')]"

        try:
            # Check if the button is present and clickable
            button = wait.until(EC.element_to_be_clickable((By.XPATH, button_xpath)))
            button.click()
            print("App was sleeping. 'Wake up' button clicked successfully!")
            
            # Brief pause to ensure the click registers before closing the browser
            time.sleep(5) 
            
        except Exception:
            # If the button doesn't appear within 15 seconds, it throws an exception
            print("Wake-up button not found. The app is likely already awake and running smoothly.")

    finally:
        # Always close the browser to free up resources
        driver.quit()
        print("Browser closed.")

if __name__ == "__main__":
    wake_app()