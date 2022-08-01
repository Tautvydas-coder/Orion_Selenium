from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import names
import random

CHROME_DRIVER = "C:/Users/takvietk/Downloads/Programos/chromedriver_win32_103/chromedriver"
SEARCH_KEY = "Robot+Python"
CITY = "Vilnius"

# def open_browser(CHROME_DRIVER):
ser = Service(CHROME_DRIVER)
driver = webdriver.Chrome(service=ser)
driver.get("https://www.orioninc.com/")
wait = WebDriverWait(driver, 5)


def confirm_cookies():
    driver.find_element(By.ID, 'hs-eu-confirmation-button').click()


def goto_careers():
    company_name = driver.find_element(By.ID, "menu-27")
    careers_link = driver.find_element(By.LINK_TEXT, "Careers")
    ActionChains(driver).move_to_element(company_name).click(careers_link).perform()


def goto_latin_location():
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    driver.find_element(By.XPATH, '//*[@id="post-108"]/div/div/div[2]/div/div[3]/div[2]/p/a').click()


def search_input():
    driver.find_element(By.CSS_SELECTOR,
                        '.col-lg-9 > div:nth-child(1) > form:nth-child(1) > input:nth-child(2)').send_keys(
        SEARCH_KEY)
    driver.find_element(By.CSS_SELECTOR,
                        '.col-lg-9 > div:nth-child(1) > form:nth-child(1) > input:nth-child(4)').click()


def find_job_title(SEARCH_KEY):
    main = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/main/div[2]/div/div/div[2]/div[4]/div"))
    )
    articles = main.find_elements(By.CLASS_NAME, "wrapper")
    for article in articles:
        header = article.find_elements(By.CLASS_NAME, "article-title")
        if SEARCH_KEY in header[0].text:
            title_text = header[0].text
            driver.find_element(By.LINK_TEXT, title_text).click()


def press_apply_button():
    driver.find_element(By.XPATH, "/html/body/main/article/div/div[3]/div[2]/div/div[1]/a").click()


def input_firstname():
    name = names.get_first_name()
    driver.find_element(By.XPATH, '//*[@id="input_7_2"]').send_keys(name)
    return name


def input_lastname():
    lastname = names.get_last_name()
    driver.find_element(By.XPATH, '//*[@id="input_7_3"]').send_keys(lastname)
    return lastname


def input_email(name, lastname):
    emails = ['@gmail.com', '@yahoo.com', '@micro.com']
    driver.find_element(By.XPATH, '//*[@id="input_7_4"]').send_keys(name + "." + lastname + random.choice(emails))


def input_phone_number():
    generated_number = []
    for i in range(0, 7):
        generated_number.append(str(random.randint(0, 9)))
    number = ''.join(generated_number)
    driver.find_element(By.XPATH, '//*[@id="input_7_5"]').send_keys("+3706" + number)


def select_country():
    driver.find_element(By.XPATH,
                        "/html/body/main/article/div/div/div/div/div/div/form/div[2]/ul/li[6]/div/div/div[2]/span").click()
    driver.find_element(By.XPATH,
                        "/html/body/main/article/div/div/div/div/div/div/form/div[2]/ul/li[6]/div/div/div[3]/div/ul/li[93]").click()


def input_state():
    driver.find_element(By.XPATH, '//*[@id="input_7_7"]').send_keys("Test")


def input_city():
    driver.find_element(By.XPATH, '//*[@id="input_7_8"]').send_keys(CITY)


def input_zip():
    generated_zip = []
    for i in range(0, 5):
        generated_zip.append(str(random.randint(0, 9)))
    number_zip = ''.join(generated_zip)
    driver.find_element(By.XPATH, '//*[@id="input_7_9"]').send_keys(number_zip)


def agree_save_information():
    driver.find_element(By.XPATH, '//*[@id="label_7_13_1"]').click()


if __name__ == '__main__':
    confirm_cookies()
    goto_careers()
    goto_latin_location()
    search_input()
    find_job_title(SEARCH_KEY)
    press_apply_button()
    name = input_firstname()
    lastname = input_lastname()
    input_email(name, lastname)
    input_phone_number()
    input_state()
    input_city()
    input_zip()
    select_country()
    agree_save_information()
