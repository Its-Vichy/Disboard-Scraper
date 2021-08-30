from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium import webdriver
from bs4 import BeautifulSoup
import requests, os, threading

class Scraper:
    def __init__(self):
        options = Options()
        options.add_argument("--window-size=1920,1080");
        options.add_argument("--no-sandbox");
        options.add_argument("--headless");
        options.add_argument("--disable-gpu");
        options.add_argument("--disable-crash-reporter");
        options.add_argument("--disable-extensions");
        options.add_argument("--disable-in-process-stack-traces");
        options.add_argument("--disable-logging");
        options.add_argument("--disable-dev-shm-usage");
        options.add_argument("--log-level=3");
        options.add_argument("--output=/dev/null");
        self.browser = webdriver.Chrome(chrome_options=options)
        os.system('cls && title Kenza-Invite' if os.name == 'nt' else 'clear')
        self.blacklist = []

        with open('./invites.txt', 'r+') as inf:
            for invite in inf:
                self.blacklist.append(invite.split('\n')[0])

    def get_invite(self, server: str):
        try:
            self.browser.get(f'https://disboard.org/server/join/{server}')
            WebDriverWait(self.browser, 10).until(expected_conditions.url_contains('https://discord.com/invite/'))
            invite = self.browser.current_url
            print(invite)

            if invite not in self.blacklist:
                with open('./invites.txt', 'a+') as inv_f:
                    inv_f.write(f'{invite}\n')
        except:
            pass

    def get_redirect(self, keywords: str, sort: str):
        
        i= 0
        while True:
            servers = BeautifulSoup(requests.get(f'https://disboard.org/search?keyword={keywords}&sort={sort}page={i}').text, 'html.parser').findAll('div', class_="column is-one-third-desktop is-half-tablet")
            print(f'Found {len(servers)} servers at: page={i} ({keywords})')
            i+= 1
            
            for server in servers:
                self.get_invite(server.find('a', class_="button button-join is-discord").get('data-id'))
        
for keywords in ['tag1', 'tag2', 'multiple+tag']:
    # bumped_at / member_count
    threading.Thread(target= Scraper().get_redirect, args=(keywords, 'bumped_at',)).start()