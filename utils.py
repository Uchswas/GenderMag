from selenium import webdriver
from PIL import Image
import base64
import os
import re


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


def extract_answer_and_facets(text):
    # Regular expressions to extract the answers and facets
    answer_pattern = re.compile(r"Answer:\s*(.*)")
    facets_pattern = re.compile(r"Facets:\s*(.*)")

    # Extracting the answers and facets
    answer_match = answer_pattern.search(text)
    facets_match = facets_pattern.search(text)

    if answer_match and facets_match:
        answer = answer_match.group(1)
        facets = facets_match.group(1)
        return f"Answer: {answer}\nFacets: {facets}"
    else:
        return ""