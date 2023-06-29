import pyautogui
import time


def tomar_decisao_batalha():
    acao = 'run'

    return acao


def realizar_movimentos_normais():
    pyautogui.keyDown('right')
    time.sleep(1)
    pyautogui.keyUp('right')
    pyautogui.keyDown('left')
    time.sleep(1)
    pyautogui.keyUp('left')


def realizar_movimentos_batalha():
    pyautogui.keyDown('down')
    time.sleep(1)
    pyautogui.keyUp('down')
    pyautogui.keyDown('right')
    time.sleep(1)
    pyautogui.keyUp('right')
    pyautogui.keyDown('up')
    time.sleep(1)
    pyautogui.keyUp('up')


while True:
    if pyautogui.locateOnScreen('buneary.png') is not None:
        print('Achei o Pokémon Buneary')
        break
    else:
        print('Procurando Pokémon...')
        realizar_movimentos_normais()

    if pyautogui.locateOnScreen('pokemon_batalha.png') is not None:
        print('Entrou em modo de batalha')

        while pyautogui.locateOnScreen('pokemon_batalha.png') is not None:
            realizar_movimentos_batalha()

        print('Modo de batalha encerrado')
        time.sleep(1)
