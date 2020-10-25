from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
browser = webdriver.Chrome(options=options)
browser.get("https://github.com")

sign_in_link = browser.find_element_by_link_text("Sign in")
sign_in_link.click()

username_input = browser.find_element_by_id("login_field")
username_input.send_keys("victorzazuetam@gmail.com")

password_input = browser.find_element_by_id("password")
password_input.send_keys("xxxxxxxxxxxxxxxxx")
password_input.submit()

assert "VictorZazuetaM" in browser.page_source

browser.quit()