# from random import *
# board = range(1, 10)
# print(board)

# def draw_board(board):
#     print("-------------")
#     for i in range(3):
#         print("|", board[0+i*3, "|", board[1+i*3, board[2+i*3], "|"]])
#         print("----------------------")

# draw_board

# Инициализация карты
maps = [1, 2, 3,
        4, 5, 6,
        7, 8, 9]

# Инициализация победных линий
victories = [[0, 1, 2],
             [3, 4, 5],
             [6, 7, 8],
             [0, 3, 6],
             [1, 4, 7],
             [2, 5, 8],
             [0, 4, 8],
             [2, 4, 6]]


# Вывод карты на экран
def print_maps():
    print(maps[0], end=" ")
    print(maps[1], end=" ")
    print(maps[2])

    print(maps[3], end=" ")
    print(maps[4], end=" ")
    print(maps[5])

    print(maps[6], end=" ")
    print(maps[7], end=" ")
    print(maps[8])


# Сделать ход в ячейку
def step_maps(step, symbol):
    ind = maps.index(step)
    maps[ind] = symbol


# Получить текущий результат игры
def get_result():
    win = ""

    for i in victories:
        if maps[i[0]] == "X" and maps[i[1]] == "X" and maps[i[2]] == "X":
            win = "X"
        if maps[i[0]] == "O" and maps[i[1]] == "O" and maps[i[2]] == "O":
            win = "O"

    return win


# Основная программа
game_over = False
player1 = True

while game_over == False:

    # 1. Показываем карту
    print_maps()

    # 2. Спросим у играющего куда делать ход
    if player1 == True:
        symbol = "X"
        step = int(input("Человек 1, ваш ход: "))
    else:
        symbol = "O"
        step = int(input("Человек 2, ваш ход: "))

    step_maps(step, symbol)  # делаем ход в указанную ячейку
    win = get_result()  # определим победителя
    if win != "":
        game_over = True
    else:
        game_over = False

    player1 = not (player1)

# Игра окончена. Покажем карту. Объявим победителя.
print_maps()
print("Победил", win)








# from kivy.app import App
#
# from kivy.uix.boxlayout import BoxLayout
# from kivy.uix.gridlayout import GridLayout
#
# from kivy.uix.button import Button
# from kivy.config import Config
#
# Config.set("graphics", "resizable", "0")
# Config.set("graphics", "width", "300")
# Config.set("graphics", "height", "300")
#
#
# class MainApp(App):
#     def __init__(self):
#         self.switch = True
#         super().__init__()
#
#     def tic_tac_toe(self, arg):
#         arg.disabled = True
#         arg.text = 'X' if self.switch else 'O'
#         self.switch = not self.switch
#
#         coordinate = (
#             (0, 1, 2), (3, 4, 5), (6, 7, 8),  # X
#             (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Y
#             (0, 4, 8), (2, 4, 6),  # D
#         )
#
#         vector = lambda item: [self.buttons[x].text for x in item]
#
#         color = [0, 1, 0, 1]
#
#         for item in coordinate:
#             if vector(item).count('X') == 3 or vector(item).count('O') == 3:
#                 win = True
#                 for i in item:
#                     self.buttons[i].color = color
#                 for button in self.buttons:
#                     button.disabled = True
#                 break
#
#     def restart(self, arg):
#         self.switch = True
#
#         for button in self.buttons:
#             button.color = [0, 0, 0, 1]
#             button.text = ""
#             button.disabled = False
#
#     def build(self):
#         self.title = "Крестики-нолики"
#
#         root = BoxLayout(orientation="vertical", padding=5)
#
#         grid = GridLayout(cols=3)
#         self.buttons = []
#         for _ in range(9):
#             button = Button(
#                 color=[0, 0, 0, 1],
#                 font_size=24,
#                 disabled=False,
#                 on_press=self.tic_tac_toe
#             )
#             self.buttons.append(button)
#             grid.add_widget(button)
#
#         root.add_widget(grid)
#
#         root.add_widget(
#             Button(
#                 text="Restart",
#                 size_hint=[1, .1],
#                 on_press=self.restart
#             )
#         )
#
#         return root
#
#
# if __name__ == "__main__":
#     MainApp().run()