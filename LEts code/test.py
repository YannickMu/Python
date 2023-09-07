from mailbox import MaildirMessage
import pyautogui
import time


limit = 1111
spam_nachricht = "Hoi"

time.sleep(1)

for nachricht in range(0, limit):
    pyautogui.typewrite(spam_nachricht)
    pyautogui.press("Enter")