import asyncio
import os
from pyppeteer import launch

class ScreenshotTaker:
    def __init__(self, headless=True):
        self.headless = headless

    async def _take_screenshot(self, file_path, output_path):
        browser = await launch(headless=self.headless)
        page = await browser.newPage()
        await page.goto(f'file://{os.path.abspath(file_path)}', waitUntil='networkidle0')  # Wait until the network is idle
        await page.waitFor(10000)  # Additional wait time (in milliseconds) if needed
        await page.screenshot({'path': output_path, 'fullPage': True})
        await browser.close()
        return output_path

    def take_screenshot(self, file_path, output_path):
        return asyncio.get_event_loop().run_until_complete(self._take_screenshot(file_path, output_path))

    def process_folder(self, folder):
        html_files = [f for f in os.listdir(folder) if f.endswith('.html')]
        output_folder = os.path.join(folder, 'images')
        os.makedirs(output_folder, exist_ok=True)
        for html_file in html_files:
            input_path = os.path.join(folder, html_file)
            output_path = os.path.join(output_folder, f'{os.path.splitext(html_file)[0]}.png')
            print(output_path)
            self.take_screenshot(input_path, output_path)
            print(f'Screenshot saved for {html_file} at {output_path}')

# Example usage
screenshot_taker = ScreenshotTaker()
screenshot_taker.process_folder('html-folder')
