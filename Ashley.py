from pyvirtualdisplay import Display
from selenium import webdriver

display = Display(visible=0, size=(1024, 768))
display.start()

driver = webdriver.Firefox()
driver.get('https://youtube.com/')


driver.quit()

display.stop()