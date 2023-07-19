from selenium import webdriver

class Driver_Lib:

    def get_driver(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        return self.driver
    
    def move_to_popup(self):
        self.driver.switch_to.alert
    
    def quite_driver(self):
        self.driver.quit()

