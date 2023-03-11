import pyperclip, pyautogui
name = input(" Введите имя ")
ochestvo = input(" Введите отчество ")
pyautogui.alert(text="Привет, " + name + " " +  ochestvo, title="сообщение", button='OK')