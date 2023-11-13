import shlex
import subprocess
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

command_raw = './start-tor-browser.desktop'
command_quote = shlex.quote(command_raw)
command = shlex.split(command_quote)
tor_browser_storage_location = '/home/vboxuser/Downloads/tor-browser'

proc = subprocess.Popen(command, cwd=tor_browser_storage_location, stdout=subprocess.PIPE)
time.sleep(5)
PROXY = "socks5://127.0.0.1:9150"
options = Options()
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--proxy-server=%s' % PROXY)


def chrome_dr(opt):
    with webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=opt) as driver:
        driver.implicitly_wait(10)
        driver.get("https://2ip.ru/")
        button = driver.find_element(By.XPATH, '/html/body/div[1]/div/p[3]/a[2]')
        button.click()
        you_ip = driver.find_element(By.XPATH, '/ html/body/div[1]/div[3]/div[1]/div/div[1]/section[1]/div/div['
                                               '1]/div/div[1]/span')
        print(f'Your IP to log in to the network -------> {you_ip.text}')


while True:
    chrome_dr(options)
    time.sleep(60)
