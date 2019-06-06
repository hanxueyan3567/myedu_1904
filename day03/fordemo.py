

def for_demo():
    for bh in range(7,9):
        print(bh)
        print('哈哈')
    for bh in range(5):
        print(bh)
        print('哈哈')




# 三个参数时:从第一参数开始计数,到第二个参数的前一位 停止,参数三(步长) 表示每次循环 递增

# 当步长为负数时,第一个参数要比第二个参数大
def for_demo1():
    for i in range(15,10,-2):
        print(i)

    for i in range(5,15,2):
        print(i)
# 遍历list
def for_list():
    # 方法一:
    blist = ['nihao','my',1,2,3,5]
    for i in blist:
        print(i)
    # 方法二:
    for i in range(len(blist)):
        print(blist[i])

    for i in range(len(blist)):
        print(blist[0:3])
#     嵌套循环
def for_for():
    for i in range(5):
        print('OK')
        for j in range(3):
            # end='xxx':让print 以什么内容结尾
            # \n:就是换行符
            # print 默认 以换行符结尾
            print('哈哈',end=',')
        print('\n')

def break_continue():
    # break 终止所有循环
    for i in range(5):
        print(i)
        if i ==2:
            break


    for i in range(5):
        if i == 2 :
            # 停止本次循环,直接开始下一次循环
            continue
        print(i)





def for_li():
    for i in range(1,10):
        x = i + 1
        for j in range(1,x):
            print('%s * %s = %s'%( i , j ,i * j),end ='   ' )
        print(' ')



def xunhuan():


    for i in range(5):
        print(i)








if __name__ == '__main__':
    # for_demo1()
    # for_list()
    # break_continue()
    # for_li()
    xunhuan()








