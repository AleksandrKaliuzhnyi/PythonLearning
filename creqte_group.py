from selenium import webdriver
import unittest
from group import Group


class test(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)

    def test_create_group(self):
        driver = self.driver
        self.open_home_page(driver)
        self.login(driver, username="admin", password="secret")
        self.open_group_list(driver)
        self.group_creation(driver)
        self.fill_group_form(driver, Group(name="1st group", header="logo", footer="comment"))
        self.submit_group_creation(driver)

    def submit_group_creation(self, driver):
        driver.find_element_by_name("submit").click()

    def fill_group_form(self, driver, group):
        driver.find_element_by_name("group_name").click()
        driver.find_element_by_name("group_name").send_keys(group.name)
        driver.find_element_by_name("group_header").click()
        driver.find_element_by_name("group_header").send_keys(group.header)
        driver.find_element_by_name("group_footer").click()
        driver.find_element_by_name("group_footer").send_keys(group.footer)

    def group_creation(self, driver):
        driver.find_element_by_name("new").click()

    def open_group_list(self, driver):
        driver.find_element_by_link_text("groups").click()

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
