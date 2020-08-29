from selenium import webdriver
from selenium.webdriver.support.ui import Select
import unittest
from contact import Contact



class test2(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)

    def test_create_contact(self):
        driver = self.driver
        self.open_home_page(driver)
        self.login(driver, "admin", "secret")
        self.create_contact(driver, Contact("Oleksandr", "Kaliuzhnyi", "emkiss", "Infopulse", "Kiev", "0931234567", "QA",
                            "test@gmail.com", "7", "December", "1994"))
        self.back_to_home_page(driver)

    def back_to_home_page(self, driver):
        driver.find_element_by_link_text("home page").click()

    def create_contact(self, driver, contact):
        driver.find_element_by_link_text("add new").click()
        driver.find_element_by_name("firstname").click()
        driver.find_element_by_name("firstname").send_keys(contact.firstname)
        driver.find_element_by_name("lastname").click()
        driver.find_element_by_name("lastname").send_keys(contact.lastname)
        driver.find_element_by_name("nickname").click()
        driver.find_element_by_name("nickname").send_keys(contact.nickname)
        driver.find_element_by_name("company").click()
        driver.find_element_by_name("company").send_keys(contact.company)
        driver.find_element_by_name("address").click()
        driver.find_element_by_name("address").send_keys(contact.address)
        driver.find_element_by_name("mobile").click()
        driver.find_element_by_name("mobile").send_keys(contact.mobile_num)
        driver.find_element_by_name("work").click()
        driver.find_element_by_name("work").send_keys(contact.work)
        driver.find_element_by_name("email").click()
        driver.find_element_by_name("email").send_keys(contact.email)
        driver.find_element_by_name("bday").click()
        Select(driver.find_element_by_name("bday")).select_by_visible_text(contact.bday)
        driver.find_element_by_name("bmonth").click()
        Select(driver.find_element_by_name("bmonth")).select_by_visible_text(contact.bmonth)
        driver.find_element_by_name("byear").click()
        driver.find_element_by_name("byear").send_keys(contact.byear)
        driver.find_element_by_xpath("(//input[@name='submit'])[2]").click()

    def login(self, driver, username, password):
        driver.find_element_by_name("user").click()
        driver.find_element_by_name("user").send_keys(username)
        driver.find_element_by_name("pass").click()
        driver.find_element_by_name("pass").send_keys(password)
        driver.find_element_by_id("LoginForm").click()
        driver.find_element_by_xpath("//input[@value='Login']").click()

    def open_home_page(self, driver):
        driver.get("http://localhost/addressbook/")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
