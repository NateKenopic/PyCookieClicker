from ursina import *
import random

app = Ursina()
window.color = color._20

gold = 0
winGameMessage = Text(text='', y=.40, z=-1, scale=2, origin=(0,0), background=False, color=color.green)
counter = Text(text='0 Gold', y=.25, z=-1, scale=2, origin=(0,0), background=True)
button = Button(scale= .3, icon='cookie.png', background=False)

gameWon = False

def button_click():
    global gold
    gold += random.randint(1,3)
    counter.text = str(gold) + " Gold"
    winGame()

button.on_click = button_click

button_2 = Button(cost=10, x=.3, scale=.125, color=color.dark_gray, disabled=True)
button_2.tooltip = Tooltip(f'<gold>Gold Generator\n<default>Earn 1 gold every second.')

autoClickCost = Text(text=f'Auto Clicker Costs {button_2.cost} Gold', y=-0.3, z=-1, scale=2, origin=(0,0), background=True)

def winGame():
    global gameWon
    if gold >= 10000:
        button.disabled = True
        button_2.disabled = True
        gameWon = True
        winGameMessage.text = "You Beat the Game with " + str(gold) + " Gold"
        winGameMessage.background = True

def buy_auto_gold():
    global gameWon
    if gameWon == False:
        global gold
        if gold >= button_2.cost:
            gold -= button_2.cost
            counter.text = str(gold) + " Gold"
            button_2.cost = button_2.cost*3
            autoClickCost.text = "Auto Clicker Costs " + str(button_2.cost) + " Gold"
            invoke(auto_generate_gold, 1, 1)
            winGame()

button_2.on_click = buy_auto_gold

def auto_generate_gold(value=1, interval=1):
    global gameWon
    if gameWon == False:
        global gold
        gold += 1
        counter.text = str(gold) + " Gold"
        button_2.animate_scale(.125 * 1.1, duration=.1)
        button_2.animate_scale(.125, duration=.1, delay=.1)
        invoke(auto_generate_gold, value, delay=interval)
        winGame()

def update():
    global gameWon
    if gameWon == False:
        global gold
        for b in (button_2, ):
            if gold >= b.cost:
                b.disabled = False
                b.color = color.green
            else:
                b.disabled = True
                b.color = color.gray



app.run()