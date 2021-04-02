import wx
import pyautogui, sys
import time

def clickLeftOption():
    pyautogui.moveTo(634, 1175)
    time.sleep(1)
    pyautogui.click()

def clickRightOption():
    pyautogui.moveTo(1931, 1175)
    time.sleep(1)
    pyautogui.click()

def moveToMiddle():
    pyautogui.moveTo(1280, 1175, 2)

def getFinalOptionValues():
    lechoes_total = int_lechoes_exp + int_lechoes_rarity
    lechoes_final = int_lechoes_echoes * lechoes_total

    rechoes_total = int_rechoes_exp + int_rechoes_rarity
    rechoes_final = int_rechoes_echoes * rechoes_total

    lechoe_exp_final = int_lechoes_echoes * int_lechoes_exp
    rechoe_exp_final = int_rechoes_echoes * int_rechoes_exp

    lechoe_rarity_final = int_lechoes_echoes * int_lechoes_rarity
    rechoe_rarity_final = int_rechoes_echoes * int_rechoes_rarity