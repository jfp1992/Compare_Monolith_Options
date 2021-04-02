import pytesseract #image to text ocr
import pyscreenshot #get screenshot and save as file
from win32api import GetSystemMetrics # some windows feature stuff - using it to get res
import time
import win32gui
import wx
import pyautogui, sys
from leftEchoFunctions import *
from rightEchoFunctions import *
from generalFunctions import *
#import cv2

print("Choose an option by entering the corresponding number:")
print("1. Prefer total to exp and item rarity")
print("2. Prefer exp")
print("3. Prefer item rarity")
echo_choice = input()

timer = 0

while (echo_choice == 1 or 2 or 3):
    #print("Debug: Start trying main code")
    try:
        ################
        ###LEFT ECHOE###
        ################    
        #print("Debug: Start leftEchoMain")
        #print("Debug: start leftEchoMain function")
        lechoe_width1 = round(10.7 * GetSystemMetrics(0) / 100) #get res and calc % req to hit position for pyscreenshot
        #print("Debug: finished width1")
        lechoe_height1 = round(59.65 * GetSystemMetrics(1) / 100) #"
        lechoe_width2 = round(36.33 * GetSystemMetrics(0) / 100) #"
        lechoe_height2 = round(77.85 * GetSystemMetrics(1) / 100) #"


        #print("Debug: Capture left side echo")
        image = pyscreenshot.grab(bbox=(lechoe_width1, lechoe_height1, lechoe_width2, lechoe_height2)) #w, h, w, h
        image.save("lechoe.jpg")

        #Convert left side echo image to text 
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'
        lechoes_file = open('lechoe.txt', encoding='utf-8', mode='w')
        lechoes_file.write(pytesseract.image_to_string(r'lechoe.jpg'))
        lechoes_file.close()

        lechoes_file = open("lechoe.txt", "a")
        lechoes_file.write("\n\n") #Add lines to end of file to avoid out of range errors

        #Convert text file lines to list 
        lechoes_lines = []
        with open ('lechoe.txt', 'rt') as lechoes_file:
            for lechoes_line in lechoes_file:
                lechoes_lines.append(lechoes_line)
        lechoes_file.close()

        lechoes_echoes1 = lechoes_lines[0] #Can be blank if mods are 2 lines
        lechoes_echoes2 = lechoes_lines[1]

        lechoes_rarity1 = lechoes_lines[3] #Can be blank
        lechoes_rarity2 = lechoes_lines[4] #Can be blank
        lechoes_rarity3 = lechoes_lines[5]

        lechoes_exp1 = lechoes_lines[4] #Can be blank
        lechoes_exp2 = lechoes_lines[5] #Can be blank
        lechoes_exp3 = lechoes_lines[6]

        #Check for blank line
        try:
            if (lechoes_lines[0] == '\n'):
                try:
                    int_lechoes_echoes = (int(lechoes_echoes2[13:15])) #Try to get both echo digits
                except:
                    int_lechoes_echoes = (int(lechoes_echoes2[13])) #Get single digit echo
            else:
                try:
                    int_lechoes_echoes = (int(lechoes_echoes1[13:15])) 
                except:
                    int_lechoes_echoes = (int(lechoes_echoes1[13]))
        except:
            int_lechoes_echoes = 1 #if the above fails it means that there is no echoe multiplier

        #Find blank line before rarity
        if (lechoes_lines[2] == '\n'):
            int_lechoes_rarity1 = lechoes_rarity1[0:1]
            try:
                int_lechoes_rarity2 = int(lechoes_rarity1[1:2])
            except:
                int_lechoes_rarity2 = ''
        elif (lechoes_lines[3] == '\n'):
            int_lechoes_rarity1 = lechoes_rarity2[0:1]
            try:
                int_lechoes_rarity2 = int(lechoes_rarity2[1:2])
            except:
                int_lechoes_rarity2 = ''
        else:
            int_lechoes_rarity1 = lechoes_rarity3[0:1]
            try:
                int_lechoes_rarity2 = int(lechoes_rarity3[1:2])
            except:
                int_lechoes_rarity2 = ''

        #Find blank line before rarity to calc which line to start exp on
        if (lechoes_lines[2] == '\n'):
            int_lechoes_exp1 = lechoes_exp1[0:1]
            try:
                int_lechoes_exp2 = int(lechoes_exp1[1:2])
            except:
                int_lechoes_exp2 = ''
        elif (lechoes_lines[3] == '\n'):
            int_lechoes_exp1 = lechoes_exp2[0:1]
            try:
                int_lechoes_exp2 = int(lechoes_exp2[1:2])
            except:
                int_lechoes_exp2 = ''
        else:
            int_lechoes_exp1 = lechoes_exp3[0:1]
            try:
                int_lechoes_exp2 = int(lechoes_exp3[1:2])
            except:
                int_lechoes_exp2 = ''
        
        #print("Debug: finished leftEchoMain")
        #################
        ###RIGHT ECHOE###
        #################
        #print("Debug: start rightEchoMain")
        #print("Debug: start rightEchoMain function")
        rechoe_width1 = round(62.7 * GetSystemMetrics(0) / 100)
        rechoe_height1 = round(59.65 * GetSystemMetrics(1) / 100)
        rechoe_width2 = round(92.19 * GetSystemMetrics(0) / 100)
        rechoe_height2 = round(77.85 * GetSystemMetrics(1) / 100)

        #print("Debug: Capture right side echo")
        image = pyscreenshot.grab(bbox=(rechoe_width1, rechoe_height1, rechoe_width2, rechoe_height2))
        image.save("rechoe.jpg")

        #Convert left side echo image to text 
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'
        rechoes_file = open('rechoe.txt', encoding='utf-8', mode='w')
        rechoes_file.write(pytesseract.image_to_string(r'rechoe.jpg'))
        rechoes_file.close()

        rechoes_file = open("rechoe.txt", "a")
        rechoes_file.write("\n\n") #Add lines to end of file to avoid out of range errors

        #Convert text file lines to list 
        rechoes_lines = []
        with open ('rechoe.txt', 'rt') as rechoes_file:
            for rechoes_line in rechoes_file:
                rechoes_lines.append(rechoes_line)
        rechoes_file.close()

        rechoes_echoes1 = rechoes_lines[0] #Can be blank if mods are 2 lines
        rechoes_echoes2 = rechoes_lines[1]

        rechoes_rarity1 = rechoes_lines[3] #Can be blank
        rechoes_rarity2 = rechoes_lines[4] #Can be blank
        rechoes_rarity3 = rechoes_lines[5]

        rechoes_exp1 = rechoes_lines[4] #Can be blank
        rechoes_exp2 = rechoes_lines[5] #Can be blank
        rechoes_exp3 = rechoes_lines[6]

        #Check for blank line
        try:
            if (rechoes_lines[0] == '\n'):
                try:
                    int_rechoes_echoes = (int(rechoes_echoes2[13:15])) #Try to get both echo digits
                except:
                    int_rechoes_echoes = (int(rechoes_echoes2[13])) #Get single digit echo
            else:
                try:
                    int_rechoes_echoes = (int(rechoes_echoes1[13:15])) 
                except:
                    int_rechoes_echoes = (int(rechoes_echoes1[13]))
        except:
            int_rechoes_echoes = 1

        #Find blank line before rarity
        if (rechoes_lines[2] == '\n'):
            int_rechoes_rarity1 = rechoes_rarity1[0:1]
            try:
                int_rechoes_rarity2 = int(rechoes_rarity1[1:2])
            except:
                int_rechoes_rarity2 = ''
        elif (rechoes_lines[3] == '\n'):
            int_rechoes_rarity1 = rechoes_rarity2[0:1]
            try:
                int_rechoes_rarity2 = int(rechoes_rarity2[1:2])
            except:
                int_rechoes_rarity2 = ''
        else:
            int_rechoes_rarity1 = rechoes_rarity3[0:1]
            try:
                int_rechoes_rarity2 = int(rechoes_rarity3[1:2])
            except:
                int_rechoes_rarity2 = ''

        #Find blank line before rarity to calc which line to start exp on
        if (rechoes_lines[2] == '\n'):
            int_rechoes_exp1 = rechoes_exp1[0:1]
            try:
                int_rechoes_exp2 = int(rechoes_exp1[1:2])
            except:
                int_rechoes_exp2 = ''
        elif (rechoes_lines[3] == '\n'):
            int_rechoes_exp1 = rechoes_exp2[0:1]
            try:
                int_rechoes_exp2 = int(rechoes_exp2[1:2])
            except:
                int_rechoes_exp2 = ''
        else:
            int_rechoes_exp1 = rechoes_exp3[0:1]
            try:
                int_rechoes_exp2 = int(rechoes_exp3[1:2])
            except:
                int_rechoes_exp2 = ''

        # ##########################################
        # # Calulate which echo is better          # 
        # ##########################################

        int_lechoes_rarity = int(int_lechoes_rarity1+str(int_lechoes_rarity2))
        int_lechoes_exp = int(int_lechoes_exp1+str(int_lechoes_exp2))

        int_rechoes_rarity = int(int_rechoes_rarity1+str(int_rechoes_rarity2))
        int_rechoes_exp = int(int_rechoes_exp1+str(int_rechoes_exp2))

        lechoes_total = int_lechoes_exp + int_lechoes_rarity
        lechoes_final = int_lechoes_echoes * lechoes_total

        rechoes_total = int_rechoes_exp + int_rechoes_rarity
        rechoes_final = int_rechoes_echoes * rechoes_total

        lechoe_exp_final = int_lechoes_echoes * int_lechoes_exp
        rechoe_exp_final = int_rechoes_echoes * int_rechoes_exp

        lechoe_rarity_final = int_lechoes_echoes * int_lechoes_rarity
        rechoe_rarity_final = int_rechoes_echoes * int_rechoes_rarity

        if (lechoes_final > rechoes_final):
            if (echo_choice == '1'):
                clickLeftOption()#go to generalFunctions.py
                print("Left echo is better overall")
            else:
                print("Overall not selected, moving on")
        elif (rechoes_final > lechoes_final):
            if (echo_choice == '1'):
                clickRightOption()#go to generalFunctions.py
                print("Right echo is better overall")
            else:
                print("Overall not selected, moving on")
        else:
            moveToMiddle()#go to generalFunctions.py
            print("Both echos are the same overall, choose any")
            time.sleep(5)

        if (lechoe_exp_final > rechoe_exp_final):
            if (echo_choice == '2'):
                clickLeftOption()#go to generalFunctions.py
                print("Left echo is better for exp")
            else:
                print("exp not selected, moving on")
        elif (rechoe_exp_final > lechoe_exp_final):
            if (echo_choice == '2'):
                clickRightOption()#go to generalFunctions.py
                print("Right echo is better for exp")
            else:
                print("exp not selected, moving on")
        else:
            moveToMiddle()
            print("Both echos are the same for exp, choose any")
            time.sleep(5)

        if (lechoe_rarity_final > rechoe_rarity_final):
            if (echo_choice == '3'):
                clickLeftOption() #go to generalFunctions.py
                print("Left echo is better for item drops")
            else:
                print("Item rarity not selected, moving on")
        elif (rechoe_rarity_final > lechoe_rarity_final):
            if (echo_choice == '3'):
                clickRightOption()#go to generalFunctions.py
                print("Right echo is better for item drops")
            else:
                print("Item rarity not selected, moving on")
        else:
            moveToMiddle()#go to generalFunctions.py
            print("Both echos are the same for item drops, choose any")
            time.sleep(5)
    except:
        timer = timer + 1
        time.sleep(1)
        print('waiting for: ' + str(timer) + 'seconds')
    #######################
    ### Track modifiers ###
    #######################
