import pyautogui
from time import sleep
#abrir mouseinfo
import pyperclip 
for i in range(1):
    pyautogui.moveTo(722,1053, duration=1)
    pyautogui.leftClick(duration=0.5)
    pyautogui.typewrite('cmd')
    pyautogui.moveTo(1040,565, duration=1)
    pyautogui.press('enter')
    sleep(1)
    pyautogui.leftClick(duration=0.5)
    pyautogui.typewrite('python')
    pyautogui.press('enter')
    sleep(2)
    pyautogui.typewrite('from mouseinfo import mouseInfo')
    pyautogui.press('enter')
    sleep(2)
    pyautogui.typewrite('mouseInfo()')
    pyautogui.press('enter')
    pyautogui.hotkey('win', 'd')
    sleep(1)
    pyautogui.press('win')
    sleep(2)
    pyautogui.typewrite('opera')
    sleep(1)
    pyautogui.press('enter')
#abrir spotfy
for i in range(1):
    pyautogui.moveTo(722,1053, duration=1)
    pyautogui.leftClick(duration=0.5)
    pyautogui.typewrite('spotify')
    pyautogui.moveTo(1040,565, duration=1)
    pyautogui.press('enter')
    sleep(2)
    pyautogui.moveTo(2448,366, duration=1)
    pyautogui.leftClick(duration=0.5)
    pyautogui.moveTo(2535,404, duration=1)
    pyautogui.leftClick(duration=0.5)
#atualizar tabela
tabelaConfirmation = pyautogui.prompt(text = 'Deseja marcar na tabela que vc trabalho hj')
if tabelaConfirmation == ('sim'):
    #abri o planilhas
    for i in range(1):
        pyautogui.moveTo(3600,0, duration=1)
        pyautogui.leftClick(duration=0.5)
        pyautogui.hotkey('ctrl', 't')
        pyautogui.moveTo(2677,149, duration=1)
        pyautogui.leftClick(duration=0.5)
        pyautogui.typewrite('drive')
        pyautogui.press('enter')
        pyautogui.moveTo(3743,127, duration=1)
        pyautogui.leftClick(duration=0.5)
        pyautogui.moveTo(3520, 496, duration=1)
        pyautogui.leftClick(duration=0.5)
        sleep(3)
        pyautogui.moveTo(2543,323, duration=1)
        pyautogui.leftClick(duration=0.5)
        pyautogui.typewrite('trabalho')
        pyautogui.press('enter')
        pyautogui.moveTo(2337,381, duration=0.5)
        sleep(4)
        pyautogui.leftClick(duration=0.5)
        sleep(2)
        pyautogui.tripleClick(duration=1)
    #cria um nova linha
    for i in range(1):
        pyautogui.moveTo(1997,380, duration=1)
        sleep(2)
        pyautogui.rightClick(duration=0.5)
        sleep(2)
        pyautogui.moveTo(2100,431, duration=1)
        sleep(2)
        pyautogui.leftClick(duration=0.5)
    #coleta e prenche dados
    for i in range(1):
        pyautogui.moveTo(2063,366, duration=1)
        pyautogui.leftClick(duration=0.5)
        pyautogui.typewrite('1')
        pyautogui.press('tab')
        pyautogui.hotkey('ctrl', 't')
        sleep(2)
        pyautogui.typewrite('Que horas sao?')
        sleep(3)
        pyautogui.press('enter')
        pyautogui.moveTo(2235,244, duration=1)
        sleep(1)
        pyautogui.tripleClick(duration=1)
        pyautogui.hotkey('ctrl', 'c')
        pyautogui.hotkey('ctrl', 'w')
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.press('tab')
        pyautogui.hotkey('ctrl', 't')
        pyautogui.typewrite('Que dia e hoje?')
        pyautogui.press('enter')
        pyautogui.moveTo(2257,295, duration=1)
        sleep(2)
        pyautogui.tripleClick(duration=1)
        pyautogui.hotkey('ctrl', 'c')
        pyautogui.hotkey('ctrl', 'w')
        pyautogui.moveTo(2321,358, duration=1)
        pyautogui.leftClick(duration=0.5)
        pyautogui.hotkey('ctrl', 'v')
    
    else: pyautogui.alert(text= 'vc tem certeza? Na verdade não interresa agr já era kkkkk')

