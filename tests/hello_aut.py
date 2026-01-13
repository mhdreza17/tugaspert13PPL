import unittest
import sys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class AutTest(unittest.TestCase):

    def setUp(self):
        browser_type = "firefox"
        if len(sys.argv) > 2:
            browser_type = sys.argv[2].lower()
        
        if browser_type == "chrome":
            options = webdriver.ChromeOptions()
            options.add_argument('--no-sandbox')
            options.add_argument('--disable-dev-shm-usage')
        elif browser_type == "edge":
            options = webdriver.EdgeOptions()
            options.add_argument('--no-sandbox')
            options.add_argument('--disable-dev-shm-usage')
        else:  # firefox
            options = webdriver.FirefoxOptions()
        
        options.add_argument('--ignore-ssl-errors=yes')
        options.add_argument('--ignore-certificate-errors')
        server = "http://localhost:444" + ("4" if browser_type == "firefox" else "5" if browser_type == "chrome" else "6")

        self.browser = webdriver.Remote(command_executor=server, options=options)
        self.addCleanup(self.browser.quit)

    def test_homepage(self):
        if len(sys.argv) > 1:
            url = sys.argv[1]
        else:
            url = "http://docker-apache"

        # Ensure proper URL format
        if not url.startswith('http'):
            url = "http://" + url

        self.browser.get(url)
        self.browser.save_screenshot("screenshot.png")
        expected_result = "Welcome back, Guest!"
        actual_result = self.browser.find_element(By.TAG_NAME, 'p').text
        self.assertIn(expected_result, actual_result)

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], verbosity=2, warnings='ignore')
