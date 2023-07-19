from POM_Code.Lib.general_lib import General_Helper
from selenium.webdriver.common.by import By
from POM_Code.test_data import test_data
from POM_Code.config import config_data


class Home_Page(General_Helper):

    ashxatanq_tab = (By.XPATH, "//a[text()='Աշխատանք']")
    Home_ashxatanq = (By.XPATH, "//span[text()= 'Աշխատանք']")
    tsarayutyunner = (By.XPATH, "//a[text()='Ծառայություններ']")
    Home_tsarayutyunner = (By.XPATH, "//span[text()= 'Ծառայություններ']")
    ansharzh_guyq_tab = (By.XPATH, "//a[text()='Անշարժ գույք']")
    Home_ansharzh_guyq = (By.XPATH, "//span[text()= 'Անշարժ գույք']")
    transport_tab = (By.XPATH, "//a[text()='Տրանսպորտ']")
    Home_transport = (By.XPATH, "//span[text()= 'Տրանսպորտ']")
    electronica_tab = (By.XPATH, "//a[text()='Էլեկտրոնիկա']")
    Home_electronica = (By.XPATH, "//span[text()= 'Էլեկտրոնիկա']")
    noradzevutyun_tab = (By.XPATH, "//a[text()='Նորաձևություն եւ ոճ']")
    Home_noradzevutyun = (By.XPATH, "//span[text()= 'Նորաձևություն եւ ոճ']")
    tun_aygi_tab = (By.XPATH, "//a[text()='Տուն և այգի']")
    Home_tun_aygi = (By.XPATH, "//span[text()= 'Տուն և այգի']")
    kencaxayin_texnika_tab = (By.XPATH, "//a[text()='Կենցաղային տեխնիկա']")
    Home_kencaxayin_texnika = (By.XPATH, "//span[text()= 'Կենցաղային տեխնիկա']")


    def test_clickon_header_button(self, tab):
        self.find_and_click(tab)
        return self.find(tab).text

    def get_opened_home_text(self, home):
        return self.find_text(home)

    def test_all_elements(self):
        elem = [
            (self.ashxatanq_tab, self.Home_ashxatanq),
            (self.tsarayutyunner, self.Home_tsarayutyunner),
            (self.ansharzh_guyq_tab, self.Home_ansharzh_guyq),
            (self.transport_tab, self.Home_transport),
            (self.electronica_tab, self.Home_electronica),
            (self.noradzevutyun_tab, self.Home_noradzevutyun),
            (self.tun_aygi_tab, self.Home_tun_aygi),
            (self.kencaxayin_texnika_tab, self.Home_kencaxayin_texnika)
        ]

        for tab, home in elem:
            tab_text = self.test_clickon_header_button(tab)
            home_text = self.get_opened_home_text(home)