    #牢记索引
def paixu():

    alist = [19,5,6,12,7,1,9]

    for i in range(len(alist)-1):
        for j in range(len(alist)-i-1):
            #前后作比较
            if alist[j] > alist[j+1]:
                #实现位置的互换
                temp = alist[j]
                alist[j] = alist[j+1]
                alist[j+1] = temp
    print(alist)



if __name__ == '__main__':
    paixu()






