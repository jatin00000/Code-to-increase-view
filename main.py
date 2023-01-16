import subprocess
import pyautogui
import time
def open_tor():
    subprocess.Popen(["C:/Users/HP/Desktop/Tor Browser/Browser/firefox.exe"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    time.sleep(10)
def quit_tor():
    pyautogui.click(x=980, y=30)

def play_playlist():
    pyautogui.click(x=300, y=80)
    pyautogui.typewrite('https://gplinks.co/4bbtipY')

    pyautogui.press('enter')
    time.sleep(20)

if __name__ == '__main__':
    open_tor()
    play_playlist()