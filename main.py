import pytesseract
import pyscreenshot
#import time
#import cv2

####LEFT ECHOE####

#Capture left side echo
image = pyscreenshot.grab(bbox=(274, 859, 930, 1121))
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

#Uncomment for debugging
# print("line0 " + lechoes_lines[0])
# print("line1 " + lechoes_lines[1])
# print("line2 " + lechoes_lines[2])
# print("line3 " + lechoes_lines[3])
# print("line4 " + lechoes_lines[4])
# print("line5 " + lechoes_lines[5])
# print("line6 " + lechoes_lines[6])

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
    int_rechoes_echoes = 1

#Find blank line before rarity and exp
if (lechoes_lines[2] == '\n'):
    try:
        int_lechoes_rarity = (int(lechoes_rarity1[0:2]))
        int_lechoes_exp = (int(lechoes_exp1[0:2])) #+1 line number on exp as always comes after rarity
    except:
        int_lechoes_rarity = (int(lechoes_rarity1[0:1]))
        int_lechoes_exp = (int(lechoes_exp1[0:1]))
elif (lechoes_lines[3] == '\n'):
    try:
        int_lechoes_rarity = (int(lechoes_rarity2[0:2]))
        int_lechoes_exp = (int(lechoes_exp2[0:2]))
    except:
        int_lechoes_rarity = (int(lechoes_rarity2[0:1]))
        int_lechoes_exp = (int(lechoes_exp2[0:1]))
else:
    try:
        int_lechoes_rarity = (int(lechoes_rarity3[0:2]))
        int_lechoes_exp = (int(lechoes_exp2[0:2]))
    except:
        int_lechoes_rarity = (int(lechoes_rarity3[0:1]))
        int_lechoes_exp = (int(lechoes_exp2[0:1]))

print("int_lechoes_echoes: " + str(int_lechoes_echoes))
print("int_lechoes_rarity: " + str(int_lechoes_rarity))
print("int_lechoes_exp: " + str(int_lechoes_exp))

####RIGHT ECHOE####

#Get left echoe numbers
image = pyscreenshot.grab(bbox=(1605, 859, 2360, 1121))
image.save("rechoe.jpg")

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'
rechoes_file = open('rechoe.txt', encoding='utf-8', mode='w')
rechoes_file.write(pytesseract.image_to_string(r'rechoe.jpg'))

rechoes_file = open("rechoe.txt", "a")
rechoes_file.write("\n\n") #Add lines to end of file to avoid out of range errors

rechoes_lines = []
with open ('rechoe.txt', 'rt') as rechoes_file:
    for rechoes_line in rechoes_file:
        rechoes_lines.append(rechoes_line)
rechoes_file.close()

rechoes_echoes1 = rechoes_lines[0]
rechoes_echoes2 = rechoes_lines[1]

rechoes_rarity1 = rechoes_lines[3]
rechoes_rarity2 = rechoes_lines[4]
rechoes_rarity3 = rechoes_lines[5]

rechoes_exp1 = rechoes_lines[4]
rechoes_exp2 = rechoes_lines[5]
rechoes_exp3 = rechoes_lines[6]

print("line0 " + rechoes_lines[0])
print("line1 " + rechoes_lines[1])
print("line2 " + rechoes_lines[2])
print("line3 " + rechoes_lines[3])
print("line4 " + rechoes_lines[4])
print("line5 " + rechoes_lines[5])
print("line6 " + rechoes_lines[6])

try:
    if (rechoes_lines[0] == '\n'):
        try:
            int_rechoes_echoes = (int(rechoes_echoes2[13:15]))
        except:
            int_rechoes_echoes = (int(rechoes_echoes2[13]))
    else:
        try:
            int_rechoes_echoes = (int(rechoes_echoes1[13:15]))
        except:
            int_rechoes_echoes = (int(rechoes_echoes1[13]))
except:
    int_rechoes_echoes = 1

#Find blank line before rarity and exp
if (rechoes_lines[2] == '\n'):
    try:
        int_rechoes_rarity = (int(rechoes_rarity1[0:2]))
        int_rechoes_exp = (int(rechoes_exp1[0:2]))
    except:
        int_rechoes_rarity = (int(rechoes_rarity1[0:1]))
        int_rechoes_exp = (int(rechoes_exp1[0:1]))
elif (rechoes_lines[3] == '\n'):
    try:
        int_rechoes_rarity = (int(rechoes_rarity2[0:2]))
        int_rechoes_exp = (int(rechoes_exp2[0:2]))
    except:
        int_rechoes_rarity = (int(rechoes_rarity2[0:1]))
        int_rechoes_exp = (int(rechoes_exp2[0:1]))
else:
    try:
        int_rechoes_rarity = (int(rechoes_rarity3[0:2]))
        int_rechoes_exp = (int(rechoes_exp2[0:2]))
    except:
        int_rechoes_rarity = (int(rechoes_rarity3[0:1]))
        int_rechoes_exp = (int(rechoes_exp2[0:1]))

print("int_rechoes_echoes: " + str(int_rechoes_echoes))
print("int_rechoes_rarity: " + str(int_rechoes_rarity))
print("int_rechoes_exp: " + str(int_rechoes_exp))

# ##########################################
# # Calulate which echo is better          # 
# ########################################## 

lechoes_total = int_lechoes_exp + int_lechoes_rarity
lechoes_final = int_lechoes_echoes * lechoes_total

rechoes_total = int_rechoes_exp + int_rechoes_rarity
rechoes_final = int_rechoes_echoes * rechoes_total

lechoe_exp_final = int_lechoes_echoes * int_lechoes_exp
rechoe_exp_final = int_rechoes_echoes * int_rechoes_exp

lechoe_rarity_final = int_lechoes_echoes * int_lechoes_rarity
rechoe_rarity_final = int_rechoes_echoes * int_rechoes_rarity

if (lechoes_final > rechoes_final):
    print("Left echo is better overall")
elif (rechoes_final > lechoes_final):
    print("Right echo is better overall")
else:
    print("Both echos are the same overall, choose any")

if (lechoe_exp_final > rechoe_exp_final):
    print("Left echo is better for exp")
elif (rechoe_exp_final > lechoe_exp_final):
    print("Right echo is better for exp")
else:
    print("Both echos are the same for exp, choose any")

if (lechoe_rarity_final > rechoe_rarity_final):
    print("Left echo is better for item drops")
elif (rechoe_rarity_final > lechoe_rarity_final):
    print("Right echo is better for item drops")
else:
    print("Both echos are the same for item drops, choose any")