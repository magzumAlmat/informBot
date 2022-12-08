
from pyautogui import *
import pyperclip, keyboard, time
from time import sleep
import sys
import webbrowser as wb

#contact list

abonent="Azamat"
#idle for 7 seconds
sleep(3)

# method to find the search bar location
def click_search_name(abonent):
    x0,y0=[38,16]
    moveTo(x0, y0)
    click()
    time.sleep(1)
    x1, y1 = [245,112]

  
    time.sleep(3)
    moveTo(x1, y1)
    click()


    time.sleep(1)
    typewrite(abonent, interval=0.2)
    time.sleep(2)
    press('enter')

# method to find and send message
def click_send_message(msg):
    #x3, y3 = [192,228]
   
    x3, y3 = [812,1006]
    moveTo(x3, y3)
    click()
    sleep(2)
   
    
   
    def paste(text: str):    
        buffer = pyperclip.paste()
        pyperclip.copy(text)
        keyboard.press_and_release('ctrl + v')
        pyperclip.copy(buffer)


    def type(text: str, interval=0.0):    
        if interval == 0.0:
            paste(text)
            return

        buffer = pyperclip.paste()
        for char in text:
            pyperclip.copy(char)
            keyboard.press_and_release('ctrl + v')
            time.sleep(interval)
        pyperclip.copy(buffer)
        press('enter')

    type(msg, 0.1)

    time.sleep(1)
    press('enter')

    x1, y1 = [245,112]
    moveTo(x1, y1)
    click()

    time.sleep(1)
    keyDown('ctrl')  
    press('a') 
    hotkey('delete')
   






#iterating through the contact list

# try:
#     click_search_name(abonent)
# except:
#     print("Unable to locate search bar or name")

# try:
#     click_send_message(message)
# except:
#     print("Unable to locate message bar")


print('Messages sent successfully')
