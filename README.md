# Скрипт для замены PROXY-сервера и дальнейшего его использования для парсинга с помощью selenium.  
## Версия операционной системы: Ubuntu 22.04.3 LTS 64-bit  
Установите из официальных источников браузер GOOGLE CHROME https://www.google.ru/intx/ru/chrome/  
и TOR BROWSER https://www.torproject.org/download/
## В терминале запустите команды:  

``apt install python3-pip``  
``sudo apt update``  
``pip install selenium webdriver-manager``  

Укажите в переменной ``tor_browser_storage_location`` место хранения TOR BROWSER  
Найдите в папке с TOR BROWSER файл ``torrc`` и добавьте туда строку:
``MaxCircuitDirtiness 60``