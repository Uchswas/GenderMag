from selenium import webdriver
from PIL import Image
import base64
import os


def get_html_content(file_name):
    with open(file_name, 'r') as file:
        return file.read()



def html_to_base64_image(html_content, output_image_path='screenshot.png'):
    # Setup Selenium WebDriver
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    driver = webdriver.Chrome(options=options)

    # Load HTML content
    driver.get("data:text/html;charset=utf-8,{html_content}".format(html_content=html_content))

    # Take screenshot
    screenshot_path = output_image_path
    driver.save_screenshot(screenshot_path)
    driver.quit()

    # Open the screenshot and encode it as base64
    with open(screenshot_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode('utf-8')

    # Remove the temporary screenshot file

    return encoded_string