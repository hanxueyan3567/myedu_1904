
def if_demo():
    a = 1<2
    #     =是赋值,==是判断相等
    if a :
        print('a 是 true')
    else:
        print('a 是 flase')
def elif_demo():
    a = 4
    if a ==1:
        print('a=1')
    elif a==2:
        print('a = 2')
    elif a==3:
        print('a=3')
    elif a ==4:
        print('a=4')
    else:
        print('a不是1,2,3')

def deng(a):
    a+=2
    print(a)
    a+=3
    print(a)
    a-=2
    print(a)
    a*=2
    print(a)
    a*=2
    print(a)
    a/=5
    print(a)
    a/=2
    print(a)
    a+=1
    print(a)
    a/=1.5
    print(a)
#     取余   10/8:商是1余2

















if __name__ == '__main__':
    # if_demo()
    # elif_demo()
    deng(2)









