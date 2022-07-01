import pyautogui as pg
import webbrowser as web
import time
import pandas as pd
from datetime import date

# Load the xlsx file
excel_data = pd.read_excel('birthdays.xlsx')


# Find out the birthday boy / girl !
for index, data_row in excel_data.iterrows():
    if data_row['DOB'].date().month == date.today().month and data_row['DOB'].date().day == date.today().day:
        message = f"Today is {data_row['Name']}'s birthday. Wish him/her in the morning!"


# Send the other's a messge to wish him / her :)
for index, data_row in excel_data.iterrows():
    if data_row['DOB'].date().month != date.today().month or data_row['DOB'].date().day != date.today().day:
        web.open(f"https://web.whatsapp.com/send?phone=+{data_row['Phone']}&text={message}")
        
        # Whatsapp Web needs a bit longer time to load the first time.
        if index == 0:
            time.sleep(10)

        # Send the message
        time.sleep(10)
        pg.press('enter')
        time.sleep(5)

        # Close this tab.
        pg.hotkey('ctrl', 'w')
