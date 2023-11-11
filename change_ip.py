import subprocess
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

command = './start-tor-browser.desktop'
with subprocess.Popen(command, cwd='/home/vboxuser/Downloads/tor-browser', stdout=subprocess.PIPE) as proc:
    time.sleep(5)
    while True:
        PROXY = "socks5://127.0.0.1:9150"
        options = Options()
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--proxy-server=%s' % PROXY)
        with webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options) as driver:
            driver.get("https://2ip.ru/")
            time.sleep(20000)
            driver.close()
