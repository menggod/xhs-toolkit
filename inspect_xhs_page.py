from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def main():
    print("Launching Chrome...")
    options = webdriver.ChromeOptions()
    # options.add_argument("--headless") # Do NOT use headless
    driver = webdriver.Chrome(options=options)
    
    try:
        print("Navigating to login page...")
        driver.get("https://creator.xiaohongshu.com/login")
        
        print("Please log in manually within 120 seconds...")
        # Wait for login to complete
        for i in range(120):
            if "creator.xiaohongshu.com" in driver.current_url and "login" not in driver.current_url:
                print("Login detected!")
                break
            time.sleep(1)
            
        print("Navigating to publish page...")
        driver.get("https://creator.xiaohongshu.com/publish/publish?from=menu")
        time.sleep(10) # 增加等待时间
        
        print("Inspecting page contents...")
        
        # Check for iframes
        iframes = driver.find_elements(By.TAG_NAME, "iframe")
        print(f"Found {len(iframes)} iframes.")
        
        # Check for content editor
        editors = driver.find_elements(By.CSS_SELECTOR, ".ql-editor")
        print(f"Found {len(editors)} .ql-editor elements.")
        
        # Trying other selectors
        
        others = driver.find_elements(By.CSS_SELECTOR, "[contenteditable='true']")
        print(f"Found {len(others)} [contenteditable='true'] elements.")
        for i, el in enumerate(others):
            print(f"  Element {i}: Tag={el.tag_name}, Class={el.get_attribute('class')}, ID={el.get_attribute('id')}")
            
        textareas = driver.find_elements(By.TAG_NAME, "textarea")
        print(f"Found {len(textareas)} textarea elements.")
        for i, el in enumerate(textareas):
            print(f"  Textarea {i}: Class={el.get_attribute('class')}, Placeholder={el.get_attribute('placeholder')}")

        inputs = driver.find_elements(By.TAG_NAME, "input")
        print(f"Found {len(inputs)} input elements.")
        
        # Print page source to file for analysis
        with open("page_source.html", "w", encoding="utf-8") as f:
            f.write(driver.page_source)
        print("Page source saved to page_source.html")
            
    except Exception as e:
        print(f"Error: {e}")
    finally:
        print("Closing driver...")
        driver.quit()

if __name__ == "__main__":
    main()
