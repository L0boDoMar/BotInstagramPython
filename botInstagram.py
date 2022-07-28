from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from random import randint
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import exceptions

class InstagramBot:

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome(executable_path='COLOCAR O CAMINHO AQUI')   # Colocar o caminho do chromedriver ou od geckodriver de executable_path=''

    def login(self):
        driver = self.driver
        driver.get('https://www.instagram.com/accounts/login/')
        time.sleep(5)
        user_element = driver.find_element("xpath", "//input[@name='username']")
        user_element.clear()
        user_element.send_keys(self.username)
        password_element = driver.find_element("xpath", "//input[@name='password']")
        password_element.clear()
        password_element.send_keys(self.password)
        password_element.send_keys(Keys.RETURN)
        time.sleep(8)
        self.bot_actions('games') # Aqui você coloca a hashtag: self.bot_actions('hashtag que você quiser')

    def bot_actions(self, hashtag):

        new_followed_users = []
        following = 0
        likes = 0
        comments = 0

        driver = self.driver
        driver.get('https://www.instagram.com/explore/tags/' + hashtag + '/')
        time.sleep(5)
        thumb = driver.find_element("xpath",
                                    "/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/main/article/div[1]/div/div/div[1]/div[1]/a/div/div[2]")
        thumb.click()
        time.sleep(randint(3, 4))

        for _ in range(0, 5):

            # Follow
            user = driver.find_element("xpath",
                                       "/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[1]/div/header/div[2]/div[1]/div[1]/div/div/span/a").text
            if user not in new_followed_users:
                if driver.find_element("xpath",
                                       "/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[1]/div/header/div[2]/div[1]/div[2]/button").text == 'Seguir':
                    driver.find_element("xpath",
                                        "/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[1]/div/header/div[2]/div[1]/div[2]/button").click()
                    new_followed_users.append(user)
                    following += 1
                    time.sleep(randint(5, 9))

                # Like
                like_button = driver.find_element("xpath",
                                                  "/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[1]/span[1]/button")
                like_button.click()
                likes += 1
                time.sleep(randint(5, 9))

                # Comment
                try:
                    driver.find_element("xpath", "/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[1]/span[2]/button").click()
                    comment_box = driver.find_element("xpath", "/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[3]/div/form/textarea")
                    time.sleep(randint(3, 6))
                    comment = randint(1, 10)

                    # Nesse trecho, você pode modificar o comentário!
                    # É só mudar o que está aqui dentro comment_box.send_keys('') para cada comentário
                    if comment == 1:
                        comment_box.send_keys('Sensacional!') # É só mudar o que está dentro de comment_box.send_keys('')
                        time.sleep(randint(3, 6))
                    elif comment == 2:
                        comment_box.send_keys('Incrível!') # É só mudar o que está dentro de comment_box.send_keys('')
                        time.sleep(randint(3, 6))
                    elif comment == 3:
                        comment_box.send_keys('Muito Bom!') # É só mudar o que está dentro de comment_box.send_keys('')
                        time.sleep(randint(3, 6))
                    elif comment == 4:
                        comment_box.send_keys('De mais!') # É só mudar o que está dentro de comment_box.send_keys('')
                        time.sleep(randint(3, 6))
                    elif comment == 5:
                        comment_box.send_keys('Adorei!') # É só mudar o que está dentro de comment_box.send_keys('')
                        time.sleep(randint(3, 6))
                    elif comment == 6:
                        comment_box.send_keys('Show!') # É só mudar o que está dentro de comment_box.send_keys('')
                        time.sleep(randint(3, 6))
                    else:
                        comment_box.send_keys('Irado!') # É só mudar o que está dentro de comment_box.send_keys('')
                        time.sleep(randint(3, 6))

                    comment_box.send_keys(Keys.ENTER)
                    comments += 1
                    time.sleep(randint(2, 6))
                except exceptions.StaleElementReferenceException as e:
                    print(e)
                    pass

                WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[name()='svg' and "
                                                                                      "@aria-label='Avançar']"))).click()
                time.sleep(15)
            else:
                WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[name()='svg' and "
                                                                                      "@aria-label='Avançar']"))).click()
                time.sleep(15)

        print('Liked {} pictures.'.format(likes))
        print('Comments {} new pictures.'.format(comments))
        print('Following {} new users.'.format(following))


InstaBot = InstagramBot('username', 'senha')
InstaBot.login()
