# main.py
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

def main():
    """
    Main function to run the Selenium script.
    """
    # --- 1. Open the Chrome browser ---
    # The webdriver-manager will automatically download the correct chromedriver
    # and return its path.
    try:
        print("Setting up the Chrome driver...")
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        print("Driver setup successful.")

        # --- 2. Navigate to https://www.saucedemo.com ---
        url = "https://www.saucedemo.com"
        print(f"Navigating to {url}...")
        driver.get(url)
        print("Navigation successful.")

        # Maximize the browser window for better visibility
        driver.maximize_window()
        
        # Add a small delay to ensure the page loads completely
        time.sleep(2)

        # --- 3. Find the username box and enter "standard_user" ---
        try:
            print("Finding the username input box...")
            # We use By.ID to locate the element with the id 'user-name'
            username_field = driver.find_element(By.ID, "user-name")
            print("Username box found.")
            
            print("Entering the username 'standard_user'...")
            username_field.send_keys("standard_user")
            print("Username entered successfully.")

        except Exception as e:
            print(f"Error finding or interacting with the username field: {e}")

        # Keep the browser open for a few seconds to see the result
        print("Script finished. The browser will close in 5 seconds.")
        time.sleep(5)

    except Exception as e:
        print(f"An error occurred during script execution: {e}")

    finally:
        # --- Clean up and close the browser ---
        if 'driver' in locals() and driver:
            print("Closing the browser.")
            driver.quit()

if __name__ == "__main__":
    main()
