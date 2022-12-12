# 1)Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

# str = 'абв абв авапав апра рпррв чвыфап цукцк гнег п в к ц ф ячвф ипбдл еке'
# text = list(filter(lambda i: 'а' not in i and 'б' not in i and 'в' not in i, str.split()))
# print(text)

# 2)Создайте программу для игры в ""Крестики-нолики"".

# maps = [1,2,3,4,5,6,7,8,9]
# victories = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
# def print_maps():
#     print(maps[0], end = " ")
#     print(maps[1], end = " ")
#     print(maps[2])
#     print(maps[3], end = " ")
#     print(maps[4], end = " ")
#     print(maps[5])
#     print(maps[6], end = " ")
#     print(maps[7], end = " ")
#     print(maps[8])    
# def step_maps(step,symbol):
#     ind = maps.index(step)
#     maps[ind] = symbol
# def get_result():
#     win = ""
#     for i in victories:
#         if maps[i[0]] == "X" and maps[i[1]] == "X" and maps[i[2]] == "X":
#             win = "X"
#         if maps[i[0]] == "O" and maps[i[1]] == "O" and maps[i[2]] == "O":
#             win = "O"     
#     return win
# game_over = False
# player1 = True
# while game_over == False:
#     print_maps()
#     if player1 == True:
#         symbol = "X"
#         step = int(input("Человек 1, ваш ход: "))
#     else:
#         symbol = "O"
#         step = int(input("Человек 2, ваш ход: "))
#     step_maps(step,symbol)
#     win = get_result()
#     if win != "":
#         game_over = True
#     else:
#         game_over = False
#     player1 = not(player1)              
# print_maps()
# print("Победил", win)

# 3)Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

# def com (path):
#     txt = ''
#     count = 1
#     for i in range(0, len(path)-1):
#         if path[i] == path[i+1]:
#             count += 1
#             if i == len(path)-2:
#                 txt += str(count) + path[i+1]
#         else:
#             txt += str(count) + path[i]
#             count = 1
#     return txt
# print(com('aaaabbccc'))