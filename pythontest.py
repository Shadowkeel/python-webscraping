from selenium import webdriver
options = webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
options.add_argument("--start-maximized")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension',False)
options.add_argument("--app=https://google.com")
driver = webdriver.Chrome(executable_path="chromedriver.exe", options=options)



