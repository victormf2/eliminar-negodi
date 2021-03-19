import pyautogui
import time

time.sleep(3)

# imgQuality = resolução da captura de tela / resolução da tela
# por algum motivo as capturas de tela de um mac ficaram com 2x a resolução da tela
imgQuality = 2
def scroll_to_negodi_and_click():
    negodi = None
    while negodi is None:
        time.sleep(0.05)
        pyautogui.scroll(-1000)
        negodi = pyautogui.locateOnScreen('negodi.png')
    negodiX, negodiY = pyautogui.center(negodi)
    pyautogui.click(negodiX / imgQuality, negodiY / imgQuality)

def click_on_captcha():
    captcha = None
    while captcha is None:
        time.sleep(0.05)
        captcha = pyautogui.locateOnScreen('captcha.png')
    checkboxX = (captcha.left / imgQuality) + 45
    checkboxY = (captcha.top / imgQuality) + 48
    pyautogui.click(checkboxX, checkboxY)

def scroll_up_and_click_on_votarnovamente():
    votarnovamente = None
    while votarnovamente is None:
        time.sleep(0.05)
        pyautogui.scroll(1000)
        votarnovamente = pyautogui.locateOnScreen('botao_votar_novamente.png')
    votarnovamenteX, votarnovamenteY = pyautogui.center(votarnovamente)
    pyautogui.click(votarnovamenteX / imgQuality, votarnovamenteY / imgQuality)

def votar_no_negodi_pra_Caralho():
    while True:
        scroll_to_negodi_and_click()
        click_on_captcha()
        scroll_up_and_click_on_votarnovamente()

votar_no_negodi_pra_Caralho()