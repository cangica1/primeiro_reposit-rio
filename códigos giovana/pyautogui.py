#importando pyautogui e apelidando ele de aut
import pyautogui as aut

#pressiono a tecla de atalho win + r
aut.hotkey("win", "r")
#escrever notepad
aut.write("notepad", interval = 0.7)
#espere 1 segundo
aut.sleep(1)
#aperte o enter
aut.press("Enter")