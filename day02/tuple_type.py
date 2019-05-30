# 新建元组类型  只可以访问,不可以增删改
# 用在方法入参,只读
atuple = (1,2,3,4)



if __name__ == '__main__':
    print(atuple[0])
    print(atuple[0:4])
#     不能被更改,所以报黄
    atuple[0] = 5














