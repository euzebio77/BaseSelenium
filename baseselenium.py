#base selenium/webdriver
from selenium import webdriver 
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time 

servico = Service(ChromeDriverManager().install())