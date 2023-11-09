import pytest
from selenium import webdriver
import uuid

@pytest.fixture(scope="function")
def driver_init(request):
    driver = webdriver.Chrome()
    driver.implicitly_wait(3)
    request.cls.driver = driver
    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def unique_email():
    return f"user{uuid.uuid4()}@example.com"