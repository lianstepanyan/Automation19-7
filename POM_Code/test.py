from POM_Code.Lib.driver_lib import Driver_Lib
from POM_Code.Lib.general_lib import General_Helper
from POM_Code.Page.home import Home_Page
from POM_Code.Page.main_page import Main_Page
from POM_Code.test_data import test_data
import logging

def test():
    driver = Driver_Lib().get_driver()
    main = Main_Page(driver)
    home = Home_Page(driver)

    main.open_page()
    # Driver_Lib().move_to_popup()
    # main.choose_language()
    home.test_all_elements()
    assert home.test_clickon_header_button() == home.get_opened_home_text(), logging.error("There is issue during test")
    logging.info("Test is pass")
    

if __name__ == "__main__":
    test()