from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class TwitterBot:
    def __init__(self,username,password):
        self.username = username
        self.password = password
        self.bot = webdriver.Firefox()

    def login(self):
        bot = self.bot
        bot.get('https://twitter.com/explore')  
        time.sleep(5)

        email = bot.find_element_by_name('session[username_or_email]')
        password = bot.find_element_by_name('session[password]')
#find a element with id and class
        email.clear()
        password.clear()
        email.send_keys(self.username)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        time.sleep(10)

    def like_tweet(self,hashtag):
        bot = self.bot
        bot.get('https://twitter.com/search?q=' + hashtag + '&src=typed_query')
        time.sleep(5)  

        for i in range(1,3):
            bot.execute_script('window.scrollTo(0,document.body.scrollHeight)')  
            time.sleep(5)
            tweets = bot.find_elements_by_class_name('tweet')
        #     links = [elem.get_attribute('data-permalink-path') for elem in tweets]
        # for link in links:
        #     bot.get('https://twitter.com' + link)  
            try:
                bot.find_elements_by_class_name('r-xoduu5').click()
                time.sleep(10)
            except Exception as ex:
                time.sleep(60)         


ed = TwitterBot('username','password')
ed.login() 
ed.like_tweet('webdevelopment')