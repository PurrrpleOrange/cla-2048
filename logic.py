import random

'''
field_setting()
field_print()
random_spawn()

move_l()
move_u()
move_r
move_d
can_move()

-----------------------------------------------------------
win cond ???
    if check_l == (len(field) - 1) * len(field):
        print("You cant use this command, icons can't move. Chose another one")
        
polnaya huyinya:
def move_l():
    global game_end
    game_end[0] = False
    check_move = 0
    # строка
    # если клетка слева = 0 -> мув влево, клетку справа удаляем
    # если клетка слева = клетке справа -> в клетку слева записываем сумму, клетку справа обнуляем
    for i in field:
        for j in range(len(i)-1):
            if i[j] == 0 and i[j+1] != 0:
                i[j] = i[j + 1]
                i[j + 1] = 0
                check_move += 1
                print("check i[j] == 0 and i[j+1] != 0 += 1. i = ", i, " j = ", j, " i[j] = ", i[j])
            elif i[j] != 0:
                if i[j] != i[j+1]:
                    pass
                else:
                    i[j] += i[j+1]
                    if[j+1] != 0:
                        check_move += 1
                        print("check if[j+1] != 0 += 1. i = ", i, " j = ", j, " i[j] = ", i[j])
                    i[j + 1] = 0
    if check_move == 0:
        print("You cant use this command, icons can't move. Chose another one")
        game_end[0] = True
        return False
    print("move_l func is called, check_move = ", check_move)
    return True
'''

field = []
class bcolors:
    # \033[38;2;⟨r⟩;⟨g⟩;⟨b⟩m - цвет текста
    # \033[48;2;⟨r⟩;⟨g⟩;⟨b⟩m - цвет фона
    HEADER = '\033[95m'
    n2_tc = '\033[38;2;118;108;98m'
    n2_bg = '\033[48;2;239;229;218m'
    n4_tc = '\033[38;2;123;113;101m'
    n4_bg = '\033[48;2;236;224;198m'
    n8_tc = '\033[38;2;250;243;238m'
    n8_bg = '\033[48;2;242;176;121m'
    n16_tc = '\033[38;2;250;243;238m'
    n16_bg = '\033[48;2;244;150;100m'
    n32_bg = '\033[48;2;246;124;95m'
    n32_tc = '\033[38;2;249;251;248m'
    n64_bg = '\033[48;2;246;94;59m'
    n64_tc = '\033[38;2;249;251;248m'
    n128_tc = '\033[38;2;118;108;98m'
    n128_bg = '\033[48;2;237;207;114m'
    n256_tc = '\033[38;2;123;113;101m'
    n256_bg = '\033[48;2;237;204;97m'
    n512_tc = '\033[38;2;250;243;238m'
    n512_bg = '\033[48;2;237;200;80m'
    n1024_tc = '\033[38;2;250;243;238m'
    n1024_bg = '\033[48;2;237;197;63m'
    n2048_bg = '\033[48;2;246;124;95m'
    n2048_tc = '\033[38;2;237;194;46m'
    ENDC = '\033[0m'
# print(bcolors.TWO_tc + bcolors.TWO_bg + "2" + bcolors.ENDC, end = ' ')
# print(bcolors.FOUR_tc + bcolors.FOUR_bg + "4" + bcolors.ENDC, end = ' ')
# print(bcolors.EIGHT_bg + bcolors.EIGHT_tc + "8" + bcolors.ENDC, end = ' ')
# print(bcolors.SIXTEEN_BG + bcolors.SIXTEEN_TC + "16" + bcolors.ENDC, end = ' ')
# print(bcolors.n32_bg + bcolors.n32_tc + "32" + bcolors.ENDC, end = ' ')
# print(bcolors.n64_bg + bcolors.n64_tc + "64" + bcolors.ENDC, end = ' ')


check_move_l = False
check_move_r = False
check_move_u = False
check_move_d = False
game_end = [False, False, False, False]


def field_setting(field_size):
    for i in range(field_size):
        a = []
        for j in range(field_size):
            a.append(0)
        field.append(a)
def print_pole(p):
    if p == 0:
        print("    ", end  = '')
    elif p == 2:
        print(bcolors.n2_tc + bcolors.n2_bg + "2" + "   " + bcolors.ENDC, end = '')
    elif p == 4:
        print(bcolors.n4_tc + bcolors.n4_bg + "4" + "   " + bcolors.ENDC, end = '')
    elif p == 8:
        print(bcolors.n8_tc + bcolors.n8_bg + "8" + "   " + bcolors.ENDC, end = '')
    elif p == 16:
        print(bcolors.n16_tc + bcolors.n16_bg + "16" + "  " + bcolors.ENDC, end = '')
    elif p == 32:
        print(bcolors.n32_tc + bcolors.n32_bg + "32" + "  " + bcolors.ENDC, end = '')
    elif p == 64:
        print(bcolors.n64_tc + bcolors.n64_bg + "64" + "  " + bcolors.ENDC, end = '')
    elif p == 128:
        print(bcolors.n128_tc + bcolors.n128_bg + "128" + " " + bcolors.ENDC, end = '')
    elif p == 256:
        print(bcolors.n256_tc + bcolors.n256_bg + "256" + " " + bcolors.ENDC, end = '')
    elif p == 512:
        print(bcolors.n512_tc + bcolors.n512_bg + "512" + " " + bcolors.ENDC, end = '')
    elif p == 1024:
        print(bcolors.n1024_tc + bcolors.n1024_bg + "1024" + bcolors.ENDC, end = '')
    elif p == 2048:
        print(bcolors.n2048_tc + bcolors.n2048_bg + "2048" + bcolors.ENDC, end = '')
def field_print():
    for i in field:
        print('|', end='')
        for j in range(len(field)):
            print_pole(i[j])
        print('|', end='\n')
def random_spawn():
    num1 = random.randint(0, len(field)-1)
    num2 = random.randint(0, len(field)-1)
    if field[num1][num2] == 0:
        field[num1][num2] = 2
    else:
        random_spawn()
def can_move():
    global field
    f1 = field
    global check_move_d
    global check_move_r
    global check_move_u
    global check_move_l
    if not move_d() and  not move_l() and not move_r() and not move_u():
        field = f1
        return False
    field = f1
    return True

def move_l():
    #check move l ne rabotaet
    # разбить чек мув на 2 этапа: проверка сортировки и проверка счета
    # при сортировке: если перед q[i] были нули, плюсуем
    global check_move_l
    check_move_l = False
    zero_checker = False
    #check_move_l = 0
    for q in field:
        i = 0
        k = 0

        # [4, 4, 0, 0, 8, 0, 0] -> [2, 2, 4, 8, 0, 0, 0]
        zero_checker = False
        while i < len(q) and k < len(q):
            if q[i] == 0:
                q.pop(i)
                q.append(0)
                i -= 1
                zero_checker = True
            else:
                if zero_checker == True:
                    check_move_l = True
            i += 1
            k += 1

        i = 0
        k = 0
        while i < len(q) - 1 and k < len(q)-1:
            if q[i] == q[i + 1] and q[i] != 0:
                q[i] += q[i + 1]
                q.pop(i + 1)
                q.append(0)
                check_move_l = True
            i += 1
            k += 1
    if check_move_l == False:
        return False
    return True
def move_u():
    global field
    global check_move_u
    field = matrix_trans(field)
    if move_l():
        field = matrix_trans(field)
        check_move_u = True
        return True
    else:
        field = matrix_trans(field)
        check_move_u = False
        return False
def move_r():
    global check_move_r
    check_move_r = False
    zero_checker = False
    for q in field:
        i = len(q) - 1
        k = 0
        zero_checker = False
        while i > -1 and k < len(q):
            if q[i] == 0:
                q.pop(i)
                q.insert(0, 0)
                i += 1
                zero_checker = True
            else:
                if zero_checker == True:
                    check_move_r = True
            i -= 1
            k += 1

        i = len(q)-1
        k = 0
        while i > 0 and k < len(q):
            if q[i] == q[i - 1] and q[i] != 0:
                q[i] += q[i - 1]
                q.pop(i - 1)
                q.insert(0, 0)
                check_move_r = True
            i -= 1
            k += 1
    if check_move_r == False:
        return False
    return True
def move_d():
    global field
    global check_move_d
    field = matrix_trans(field)
    if move_r():
        field = matrix_trans(field)
        check_move_d = True
        return True
    else:
        field = matrix_trans(field)
        check_move_d = False
        return False
def matrix_trans(m):
    m1 = []
    for i in range(len(field)):
        a = []
        for j in range(len(field)):
            a.append(0)
        m1.append(a)
    for i in range(0, len(m)):
        for j in range(0, len(m)):
            m1[j][i] = m[i][j]
    return m1