# -*- coding: utf-8 -*-

# # app version : 1.2.0 # #

# github : https://github.com/xsxskid

# add finde name by search in contact
# add PATH firefox driver in this folder
#
# method 1 for nice spam like:
# pm
# pm pm
# pm pm pm
# pm pm pm pm
# pm pm pm pm pm
#
# method normal jost send pm
#


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from os import system, name


def start_app(webdriver):
    logo(1)

    print("[+] try to open webdriver firefox..")
    webdriver = webdriver.Firefox()
    webdriver.get('https://web.whatsapp.com/')

    # data input
    usr = str(input("[+] inter username (in history chat):\n>>"))
    pm = str(input("[+] inter text pm:\n>>"))
    number_pm = int(input("[+] inter number of pm:\n>>"))
    MOOD = str(input(
        "[+] inter MOOD [ type 1 for method one , or just enter (method zero) ]\n>>"))
    input("[-] scan QR code and prees enter\n>>")

    pm = pm + " "

    # method one ### have bug
    if MOOD == "1":
        mood1(webdriver, number_pm, usr, pm, send_message)

    # method normall
    else:
        mood0(webdriver, number_pm, usr, pm, send_message)


# define our clear function
def clear():
    # for win
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


# change shell color
class color:
    GREEN = '\033[92m'
    RED = '\033[91m'


# my logo plz dont change for make me hapy :D
def logo(m):

    if m == 1:
        clear()

    print(color.RED+"""
    
    app version : 1.2.0
    
\n
 ▒█████   ███▄    █  ██▓ ▒█████   ███▄    █ 
▒██▒  ██▒ ██ ▀█   █ ▓██▒▒██▒  ██▒ ██ ▀█   █ 
▒██░  ██▒▓██  ▀█ ██▒▒██▒▒██░  ██▒▓██  ▀█ ██▒
▒██   ██░▓██▒  ▐▌██▒░██░▒██   ██░▓██▒  ▐▌██▒
░ ████▓▒░▒██░   ▓██░░██░░ ████▓▒░▒██░   ▓██░
░ ▒░▒░▒░ ░ ▒░   ▒ ▒ ░▓  ░ ▒░▒░▒░ ░ ▒░   ▒ ▒ 
  ░ ▒ ▒░ ░ ░░   ░ ▒░ ▒ ░  ░ ▒ ▒░ ░ ░░   ░ ▒░
░ ░ ░ ▒     ░   ░ ░  ▒ ░░ ░ ░ ▒     ░   ░ ░ 
    ░ ░           ░  ░      ░ ░           ░ </OƝioN
    """+color.GREEN)


# print log in shel
def print_log(msg, i,  number, method):

    clear()
    sended = str(i + 1)
    allnumber = str(number)
    print("\n\n[-] start by text:"+msg + "method: "+method)
    print("[=] send " + sended + "/" + allnumber + "")


# scan chat and ind message fild and send message
def send_message(msg, webdriver, i, number, method):

    print_log(msg, i, number, method)

    xpath = "/html//div[@id='main']/footer[@class='_2vJ01']//div[@class='_3FRCZ copyable-text selectable-text']"
    fild = webdriver.find_element_by_xpath(xpath)

    fild.send_keys(msg)
    button = webdriver.find_element_by_class_name("_1U1xa")
    button.click()


banner = 'I love your crying sound😈'


def send_baner(msg, webdriver, usr):
    a = webdriver.find_element_by_css_selector("span[title='"+usr+"']")
    sleep(1)
    a.click()
    xpath = "/html//div[@id='main']/footer[@class='_2vJ01']//div[@class='_3FRCZ copyable-text selectable-text']"
    fild = webdriver.find_element_by_xpath(xpath)

    fild.send_keys(msg)
    button = webdriver.find_element_by_class_name("_1U1xa")
    button.click()


# find contact and click for open chat
def find_user(usr, webdriver):
    print("[-] find contact")
    a = webdriver.find_element_by_css_selector("span[title='"+usr+"']")
    sleep(1)
    a.click()


# method zero
def mood0(webdriver, number, usr, pm, send_message):
    try:
        find_user(usr, webdriver)

        send_baner(banner, webdriver, usr)
        method = "zero"
        for i in range(number):
            send_message(pm, webdriver, i, number, method)

        print(color.RED+"[-] done")
        print("\n\n")
        logo(0)

    except NoSuchElementException:
        # user name not fund in history chat or someting
        print(color.RED+"[-] error ")
        print("\n\n")
        logo(0)


# method one
def mood1(webdriver, number, usr, pm, send_message):
    try:
        find_user(usr, webdriver)

        method = "one"
        pp = 1

        send_baner(banner, webdriver, usr)
        sleep(2)
        for i in range(number):
            if pp <= 5:
                msg = pm * pp
                send_message(msg, webdriver, i, number, method)
                pp = pp + 1

            else:
                pp = 1
                msg = pm
                send_message(msg, webdriver, i, number, method)

        print(color.RED+"[-] done")
        print("\n\n")
        logo(0)

    except NoSuchElementException:
        # user name not fund in history chat or someting error
        print(color.RED+"[-] error ")
        print("\n\n")
        logo(0)


start_app(webdriver)
