import os
import pytest
from selene import browser


@pytest.fixture(scope="module")
def open_browser():
    reports = "reports"
    browser.config.save_screenshot_on_failure = True
    browser.driver.maximize_window()
    os.makedirs(reports, exist_ok=True)
    browser.config.reports_folder = reports
    browser.open()


@pytest.fixture(scope="function")
def open_google():
    browser.driver.get("https://google.com/ncr")
