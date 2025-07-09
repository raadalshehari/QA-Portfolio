import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# --- Setup WebDriver ---
# This automatically downloads and manages the correct driver for your Chrome browser
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
print("WebDriver setup complete.")

try:
    # --- 1. Navigate to the URL ---
    url = "https://demoqa.com/automation-practice-form"
    driver.get(url)
    driver.maximize_window() # Maximize window to ensure all elements are visible
    print(f"Navigated to {url}")

    # --- 2. Fill in Text Fields ---
    driver.find_element(By.ID, "firstName").send_keys("Raad")
    driver.find_element(By.ID, "lastName").send_keys("Hussam")
    driver.find_element(By.ID, "userEmail").send_keys("raad@gmail.com")
    print("Filled in name and email.")

    # --- 3. Select Gender Radio Button ---
    # We use a more specific XPath to click the label associated with the radio button, which is a reliable method.
    gender_male_label = driver.find_element(By.XPATH, "//label[text()='Male']")
    driver.execute_script("arguments[0].scrollIntoView(true);", gender_male_label) # Scroll element into view
    gender_male_label.click()
    print("Selected gender: Male.")

    # --- 4. Enter Mobile Number ---
    driver.find_element(By.ID, "userNumber").send_keys("1234567890")
    print("Entered mobile number.")

    # --- 5. Enter Date of Birth ---
    # The date picker is tricky. A reliable way is to clear the field and send the date as text.
    date_of_birth_input = driver.find_element(By.ID, "dateOfBirthInput")
    date_of_birth_input.click()
    # On Windows/Linux, use CONTROL+A. On Mac, use COMMAND+A.
    date_of_birth_input.send_keys(Keys.CONTROL + "a")
    date_of_birth_input.send_keys("25 Jan 2000")
    date_of_birth_input.send_keys(Keys.ENTER) # Press Enter to close the calendar
    print("Entered date of birth.")

    # --- 6. Select State and City from Dropdowns ---
    # These are not standard dropdowns, so we must scroll them into view and then click.

    # Select State
    state_dropdown = driver.find_element(By.ID, "state")
    driver.execute_script("arguments[0].scrollIntoView(true);", state_dropdown) # Scroll element into view
    state_dropdown.click()
    # Wait for the state option to be clickable and then click it
    haryana_option = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//*[text()='Haryana']"))
    )
    haryana_option.click()
    print("Selected state: Haryana.")

    # Select City
    city_dropdown = driver.find_element(By.ID, "city")
    driver.execute_script("arguments[0].scrollIntoView(true);", city_dropdown) # Scroll element into view
    city_dropdown.click()
    # Wait for the city option to be clickable and then click it
    karnal_option = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//*[text()='Karnal']"))
    )
    karnal_option.click()
    print("Selected city: Karnal.")

    # --- 7. Submit the Form ---
    # The submit button can be covered by ads, so we use JavaScript to scroll and click.
    submit_button = driver.find_element(By.ID, "submit")
    driver.execute_script("arguments[0].scrollIntoView(true);", submit_button)
    submit_button.click()
    print("Clicked submit button.")

    # --- 8. Verify the Confirmation Pop-up ---
    # This is the most important part: verifying the result.
    # We wait up to 10 seconds for the confirmation modal to appear.
    print("Waiting for confirmation pop-up...")
    confirmation_modal = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "example-modal-sizes-title-lg"))
    )

    # If the script finds this element, the test is a success.
    print("Verification successful: Confirmation pop-up appeared!")
    print(f"Confirmation Title: {confirmation_modal.text}")
    
    # Keep the browser open for a few seconds to see the result
    time.sleep(5)

finally:
    # --- Clean Up ---
    # Always close the browser window at the end
    print("Closing browser.")
    driver.quit()
