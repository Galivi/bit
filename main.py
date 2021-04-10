"""이것은 함수를 이용한 퀴즈입니다."""

q1=['''1+1=?''', '''34+21=?''', '''31+25-12=?''', '''42/14=?''', '''45*3''']



print('지금부터 퀴즈를 시작합니다.')
score=0


def clac(answer, sol):
    global score
    if answer == sol:
        score = score + 1
    return

"""1번 문제에 대한 코드"""
print(score)
print('퀴즈의 답을 맞추면 숫자가 올라가고, 틀리면 아무 일도 일어나지 않습니다.')
print(q1[0])
clac(int(input()), 2)
print(score)

"""2번 문제에 대한 코드"""
print(score)

"""3번 문제에 대한 코드"""
print('[난이도: 쉬움]')print(q1[2])
clac(int(input()), 44)
print(q1[1])
clac(int(input()), 55)
print(score)


"""4번 문제에 대한 코드"""
print(q1[3])
clac(int(input()), 3)
print(score)

"""5번 문제에 대한 코드"""
print(q1[4])
clac(int(input()), 135)
print(score)

















