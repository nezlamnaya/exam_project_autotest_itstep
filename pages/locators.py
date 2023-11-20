from selenium.webdriver.common.by import By


class BasePageLocators:
    SIGNUP = (By.XPATH, "//ul[@class='dropdown_menu']/a[text() = 'Регістрація']")
    LOGIN = (By.XPATH, "//ul[@class='dropdown_menu']/a[text() = 'Авторізація']")
    CART_BUTTON = (By.XPATH, '//*[@id="cart"]/button"]')
   
class MainPageLocators:
    MAIN_SLIDER = (By.XPATH, "//*[@alt=" "]/div/div[6]/img")
    #WARRANTY_BUTTON=(By.XPATH, "//*[@id='top_home']/div/div/div[2]/div/div/div/div[4]/a/div[2]/div[1]")
    #CATEGORY_CARS = (By.XPATH, "//*[@id='top_menu]/li[1]/a [text() = 'Машинки та техніка']")
    #DOSTAVKA= (By.XPATH,"//*[@id='top_home']/div/div/div[2]/div/div/div/div[1]/a/div[2]/div[1]")
    #FREE_SHIPPING=(By.XPATH,"//*[@id='top_home']/div/div/div[2]/div/div/div/div[2]/a/div[2]/div[1]")
    #PAYMENT_ONLINE_IN_CASH=(By.XPATH, "//*[@id='top_home']/div/div/div[2]/div/div/div/div[3]/a/div[2]/div[2]")
    #REPLACEMENT_OF_PARTS=(By.XPATH, "//*[@id='top_home']/div/div/div[2]/div/div/div/div[4]/a/div[2]/div[2]")
  
class SignupLoginPageLocators:
    ACCOUNT_BUTTON = (By.XPATH, "//span[text()='Особистий кабінет']")
    SIGNUP_BUTTON = (By.XPATH, "//a[@href = 'Швидка реєстрація']")
    INPUT_MAIL = (By.XPATH, "//*[@id='register_email']")
    INPUT_PASSWORD = (By.XPATH, "//*[@id='register_password']")
    INPUT_CONFIRM_PASSWORD = (By.XPATH, "//*[@id='register_confirm_password']")
    INPUT_FULL_NAME = (By.XPATH, "//*[@id='register_firstname']")
    INPUT_NUMBER_TELEPHONE = (By.XPATH, "//*[@id='register_telephone']")
    SELECT_FIELD = (By.XPATH, "//*[@id='register_country_id']/option[20]")
    SELECT_COMMUNITY = (By.XPATH, "//*[@id='register_zone_id']/option[1]")
    INPUT_POST_OFFICE = (By.XPATH, "//*[@id='register_city']/option[1]")
    INPUT_POST_CODE = (By.XPATH, "//*[@id='register_postcode']")
    INPUT_ADDRESS = (By.XPATH, "//*[@id='register_address_1']")
    SELECT_NEWSLETTER=(By.XPATH, "//*[@id='register_newsletter_1']")       
    BUTTON_CONFIRM = (By.XPATH, "//*[@id='simpleregister_button_confirm']")
    CLICK_ACCOUNT = (By.XPATH, "//span[text()='Особистий кабінет']")
    LOGIN_BUTTON = (By.XPATH, "//a[@href = 'Авторізація']")
    INPUT_EMAIL = (By.XPATH, "//*[@id='input-email']")
    INPUT_PASSWORD = (By.XPATH, "//*[@id='register_password']")
    LOGIN_BUTTON= (By.XPATH, "//*[@id='content']/div[2]/div[2]/div/form/input")
        

class CabinetPageLocators:
    pass

class CategoryPageLocators:
    pass

class SearchPageLocators:
    pass

class ProductPageLocators:
    pass

