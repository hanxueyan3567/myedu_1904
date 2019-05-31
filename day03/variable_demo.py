
# 声明一个全局变量
avar = '南京师范皇冠库'


def d1():   #使用全局变量
    print(avar)
    # 在方法内部声明的变量,只能在方法内部使用
    bavr = ' jfj'
#  在方法内,对全局变量重新赋值,使用global 引入全局变量
def d2():
    global avar
    avar = '尽快发货ifuoi'
    print(avar)
def d3():
    print(bvar)  #无法使用其他方法内声明的变量




if __name__ == '__main__':
    d1()
    d2()
    d1()

















