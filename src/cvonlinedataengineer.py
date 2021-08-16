import time

from pip import main
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import logging
import logging.config
import yaml



with open('..\config\logging.yml', 'r') as config:
    logging.config.dictConfig(yaml.safe_load(config))

main.logger = logging.getLogger('main')
error_logger = logging.getLogger('error')


with webdriver.Firefox(executable_path='../drivers/geckodriver.exe') as ffdriver:
    ffdriver.get(
        "https://cvonline.lt/lt/search?limit=20&offset=0&categories%5B0%5D=INFORMATION_TECHNOLOGY&keywords%5B0%5D=data&towns%5B0%5D=540&isHourlySalary=false&isRemoteWork=false")


    time.sleep(5)
    sel = '\li > div:nth-child(1) > div:nth-child(2) > a:nth-child(1)'

    peps_cointaining_search_string = ffdriver.find_elements_by_css_selector(sel)
    print([pep.text for pep in peps_cointaining_search_string][1:-1])
