
# github : https://github.com/onionj

# TODO:
# add finde name by search in contact
# add PATH firefox driver in this folder


from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import Firefox
from selenium.webdriver.common.keys import Keys
from time import sleep
from os import system, name
from sys import platform
from tqdm import tqdm

# open a new web driver with proxy and return web driver


def open_driver():
    '''Open a web driver and return'''

    print("[+] try to open webdriver firefox..")

    # check system
    if platform == 'win32':
        print("[+] open geckodriver.exe")
        return Firefox()

    print("[+] open ./geckodriver")
    return Firefox(executable_path='./geckodriver')


def get_whatsapp_page(driver):
    '''go to https://web.whatsapp.com/'''
    return driver.get('https://web.whatsapp.com/')


def mode0(driver, number, usr, pm):
    try:
        if find_user(usr, driver):

            for _ in tqdm(range(number), desc='sending.. '):
                send_message(pm, driver)

            print(color.RED+"[-] done")
            print("\n\n")
            logo()

    except NoSuchElementException:
        # user name not fund in history chat or someting
        print(color.RED+"[-] error ")
        print("\n\n")
        logo()


# method one
def mode1(driver, number, usr, pm):
    try:
        if find_user(usr, driver):
            row = 5
            flag = 1

            for _ in tqdm(range(number), desc='sending.. '):
                if flag <= row:
                    msg = pm * flag
                    send_message(msg, driver)
                    flag = flag + 1
                    continue

                flag = 1
                msg = pm
                send_message(msg, driver)

            print(color.RED+"[-] done")
            print("\n\n")
            logo()

    except NoSuchElementException:
        # user name not fund in history chat or someting error
        print(color.RED+"[-] error ")
        print("\n\n")
        logo()


def start_app():

    logo(clear_shell=True)

    driver = open_driver()

    get_whatsapp_page(driver)

    # data input
    usr = input("[+] Enter username (in history chat): ")
    pm = input("[+] Enter text pm: ")
    number_pm = input("[+] Enter number of pm: ")
    mode = input(
        "[+] Enter mode [ type 1 for method one , or just enter (method zero) ] ")
    input("[-] scan QR code and prees enter ")

    pm = pm + " "

    # method one ### have bug
    if mode == "1":
        mode1(driver, number_pm, usr, pm)
        return

    # method normall
    mode0(driver, number_pm, usr, pm)


def clear():
    '''clear shell'''
    if platform == 'win32':
        system('cls')
        return
    system('clear')


class color:
    ''' change test color '''

    GREEN = '\033[92m'
    RED = '\033[91m'


def logo(clear_shell=False):

    if clear_shell:
        clear()

    print(color.RED+"""

    app version : 1.2.2

 ▒█████   ███▄    █  ██▓ ▒█████   ███▄    █
▒██▒  ██▒ ██ ▀█   █ ▓██▒▒██▒  ██▒ ██ ▀█   █
▒██░  ██▒▓██  ▀█ ██▒▒██▒▒██░  ██▒▓██  ▀█ ██▒
▒██   ██░▓██▒  ▐▌██▒░██░▒██   ██░▓██▒  ▐▌██▒
░ ████▓▒░▒██░   ▓██░░██░░ ████▓▒░▒██░   ▓██░
░ ▒░▒░▒░ ░ ▒░   ▒ ▒ ░▓  ░ ▒░▒░▒░ ░ ▒░   ▒ ▒
  ░ ▒ ▒░ ░ ░░   ░ ▒░ ▒ ░  ░ ▒ ▒░ ░ ░░   ░ ▒░
░ ░ ░ ▒     ░   ░ ░  ▒ ░░ ░ ░ ▒     ░   ░ ░ WhatsApp web spammer
    ░ ░           ░  ░      ░ ░           ░ </OƝioN
    """+color.GREEN)


# print log in shel
def show_log(msg, sended_count,  all_count, method):
    clear()
    print(f"""

[ ] start by text:{msg}
[ ] method: {method}
[*] send {sended_count + 1} / {all_count}
""")


def send_message(msg, driver):
    ''' scan chat and find message fild and send message '''
    # show_log(msg, i, number, method)
    try:
        message_box_xpath = "/html//div[@id='main']/footer[@class='_2vJ01']//div[@class='_3FRCZ copyable-text selectable-text']"
        message_box_fild = driver.find_element_by_xpath(message_box_xpath)
        message_box_fild.send_keys(msg, Keys.ENTER)

    except NoSuchElementException:
        pass

    # send_button=driver.find_element_by_class_name("_1U1xa")
    # send_button.click()


def find_user(user_name, driver):
    '''find contact and click for open chat'''

    print("[-] find contact")
    try:
        driver.find_element_by_css_selector(f"span[title={user_name}]").click()
        return True

    except NoSuchElementException:
        print('[!] user not find!')
        return False

    except:
        print('[!] user not find!')
        return False

# method zero


start_app()
