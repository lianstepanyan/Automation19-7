from POM_Code.Lib.general_lib import General_Helper
from POM_Code.Lib.driver_lib import Driver_Lib
from selenium.webdriver.common.by import By
from POM_Code.test_data import test_data
from POM_Code.config import config_data


class Main_Page(General_Helper):

    armenian_language = (By.XPATH, "//div[text()='Հայերեն']")
    russian_language = (By.XPATH, "//div[text()='Русский']")
    english_language = (By.XPATH, "//div[text()='English']")
    
    def open_page(self):
        self.driver.get(config_data["url"])

    def choose_language(self):
        self.find_and_click(self.armenian_language)
    

# class Main(Driver_Lib):
    
#     def get_popup(self):
#         self.move_to_popup()