from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
import csv
from itertools import zip_longest


url = input("please enter url:")
print("do you want to use like tool 1 , comment tool 2 , group tool 3 ")
option = input("please enter option number:")


browser = webdriver.Chrome()


def open_browser():
    browser.get("https://www.facebook.com/")

    username = browser.find_element(
        By.XPATH, '//input[@type="text"]')

    username.send_keys("3laamohamed12@gmail.com")

    password = browser.find_element(By.XPATH, '//input[@type="password"]')
    password.send_keys("alaashkawa000")

    login = browser.find_element(By.XPATH, '//button[@name="login"]')
    login.submit()
    time.sleep(5)


def id_likes():
    open_browser()
    browser.get(url)
    time.sleep(10)

    like = browser.find_element(By.XPATH, "//span[@class='x1ja2u2z']")
    like.click()
    time.sleep(40)

    link = []

    def get():
        likes = browser.find_elements(By.XPATH, "//div[@class=' x1rg5ohu']/a")
        for i in likes:
            link.append(i.get_attribute('href'))

    get()

    fie_list = [link]
    exported = zip_longest(*fie_list)
    with open("D:\courses/id_like.csv", "a") as file:
        wr = csv.writer(file)
        wr.writerows(exported)


def id_comment():
    open_browser()
    browser.get(url)
    time.sleep(60)

    link = []

    def get():
        comments = browser.find_elements(
            By.XPATH, "//span[@class='xt0psk2']/a")
        for i in comments:
            link.append(i.get_attribute('href'))

    get()

    fie_list = [link]
    exported = zip_longest(*fie_list)
    with open("D:\courses/id_comment.csv", "a") as file:
        wr = csv.writer(file)
        wr.writerows(exported)


def id_group_members():
    open_browser()
    browser.get(url)
    time.sleep(40)

    link = []

    def get():
        likes = browser.find_elements(By.XPATH, "//span[@class='xt0psk2']/a")
        for i in likes:
            link.append(i.get_attribute('href'))

    get()

    fie_list = [link]
    exported = zip_longest(*fie_list)
    with open("D:\courses/id_group.csv", "a") as file:
        wr = csv.writer(file)
        wr.writerows(exported)


if option == "1":
    id_likes()

elif option == "2":
    id_comment()

elif option == "3":
    id_group_members()

else:
    print("wrong input")
