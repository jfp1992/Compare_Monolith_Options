import wx
import pyautogui, sys
import time
from win32api import GetSystemMetrics # some windows feature stuff - using it to get res

lechoe_startw = round(24.76 * GetSystemMetrics(0) / 100) #get res and calc % req to hit start button
lechoe_starth = round(81.59 * GetSystemMetrics(1) / 100) #"

rechoe_startw = round(75.42 * GetSystemMetrics(0) / 100) #"
rechoe_starth = round(81.59 * GetSystemMetrics(1) / 100) #"

move_cursor_to_midw = round(81.59 * GetSystemMetrics(0) / 100)
move_cursor_to_midh = round(50 * GetSystemMetrics(1) / 100)

def clickLeftOption():
    pyautogui.moveTo(lechoe_startw, lechoe_starth)
    time.sleep(1)
    pyautogui.click()

def clickRightOption():
    pyautogui.moveTo(rechoe_startw, rechoe_starth)
    time.sleep(1)
    pyautogui.click()

def moveToMiddle():
    pyautogui.moveTo(move_cursor_to_midw, move_cursor_to_midh, 2)

def getFinalOptionValues():
    lechoes_total = int_lechoes_exp + int_lechoes_rarity
    lechoes_final = int_lechoes_echoes * lechoes_total

    rechoes_total = int_rechoes_exp + int_rechoes_rarity
    rechoes_final = int_rechoes_echoes * rechoes_total

    lechoe_exp_final = int_lechoes_echoes * int_lechoes_exp
    rechoe_exp_final = int_rechoes_echoes * int_rechoes_exp

    lechoe_rarity_final = int_lechoes_echoes * int_lechoes_rarity
    rechoe_rarity_final = int_rechoes_echoes * int_rechoes_rarity