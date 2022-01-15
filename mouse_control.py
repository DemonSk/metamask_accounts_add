import mouse
import keyboard
import time
import json

with open("accounts_keys.json", "r") as read_file:
    accounts = json.load(read_file)

metamask_coordinates = (1641, 48)
metamask_accounts_tab = (1620, 102)
metamask_import_tab = (1486, 483)
import_button = (1558, 557)
metamask_account_options = (1632, 174)
metamask_account_details = (1534, 307)
account_change_name = (1545, 198)

account_name = ""

def calibrate():
    print("Hold your mouse on position, that you want to have info on")
    time.sleep(5)
    print(f"Your position is: {mouse.get_position()}")
def add_metamask_acc(id, key):
    mouse.move(metamask_coordinates[0], metamask_coordinates[1], absolute=True, duration=0.2)
    time.sleep(2)

    mouse.click('left')
    mouse.move(metamask_accounts_tab[0], metamask_accounts_tab[1], absolute=True, duration=0.2)
    time.sleep(2)

    mouse.click('left')
    mouse.move(metamask_import_tab[0], metamask_import_tab[1], absolute=True, duration=0.2)
    time.sleep(2)
    mouse.click('left')
    time.sleep(1)

    keyboard.write(key)

    mouse.move(import_button[0], import_button[1], absolute=True, duration=0.2)
    time.sleep(2)
    mouse.click('left')

    mouse.move(metamask_account_options[0], metamask_account_options[1], absolute=True, duration=0.2)
    time.sleep(2)
    mouse.click('left')

    mouse.move(metamask_account_details[0], metamask_account_details[1], absolute=True, duration=0.2)
    time.sleep(2)
    mouse.click('left')

    mouse.move(account_change_name[0], account_change_name[1], absolute=True, duration=0.2)
    time.sleep(2)
    mouse.click('left')

    keyboard.press_and_release('ctrl+a')
    keyboard.write(f'{account_name}{id}')
    keyboard.press_and_release('enter')

    mouse.move(metamask_coordinates[0], metamask_coordinates[1], absolute=True, duration=0.2)
    time.sleep(2)
    mouse.click('left')
    