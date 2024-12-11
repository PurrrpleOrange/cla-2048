field = [
    [0, 0, 2, 0],
    [4, 16, 2, 0],
    [8, 4, 0, 2],
    [32, 2, 2, 4]
]


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


def move_d():
    #move_l
    global field
    field = matrix_trans(field)
    move_l()
    field = matrix_trans(field)
    return True

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


def func():
    for i in field:
        print(i)
    print()

func()
field = matrix_trans(field)
func()
move_l()
func()
field = matrix_trans(field)
func()



"""
[0, 2, 0, 2]
[2, 0, 2, 0]
[4, 0, 0, 0]


"""


