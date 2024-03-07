import pyautogui
import time

pyautogui.PAUSE = 0.5

pyautogui.press("win")
pyautogui.write("edge")
pyautogui.press("enter")
pyautogui.write("https://stackoverflow.com/questions/31635140/import-error-for-pyautogui")
pyautogui.press("enter")

time.sleep(3)

print(pyautogui.position())

pyautogui.click()
