

#
alist = ['你好',1,2,'我是',9,8,6,7]

def list_sel():
     # 取倒数第三个
    print(alist[-3])

       # 从第五个开始到后面
    print(alist[4:])


def list_del():
    #调用删除方法,填写参数:索引值 就可以删除指定元素
    alist.pop(3)
    print(alist)
    #  调用删除方法,不填参数,默认删除最后一位
    alist.pop()
    print(alist)


# 增加list中的元素
def list_add():
    blist = ['好的呀',1,2]
    print(blist)
#     增加元素,增加在末尾
    blist.append('哈哈')
    print(blist)
# 合并两个list中的元素
    clist = ['我去',1,7,8]
    blist.extend(clist)
    print(blist)

    # clist以单个元素增加
    blist.append(clist)
    print(blist)

# 更新列表中的元素  根据索引进行更新,值写在 = 后面
def list_updata():
    dlist = [1,2,6,4,5]
    dlist[2:4] = [200,'牛牛']
    print(dlist)

# 排序:正序
def list_order_by():
    dlist = [1, 2, 6, 4, 5]
    # 正排:从小到大
    dlist.sort()
    print(dlist)
    # 倒排:从大到小
    dlist.sort(reverse=True)
    print(dlist)

# 去重: 自动排序(正序)
def list_distinct():
    vlist = [7,1,2,3,4,4,3,7,1]
    # set 方法对list进行去重,去重后不是list类型
    vlist = set(vlist)
    print(vlist)
# 用list()方法,将这个数据转换成类型
    vlist = list(set(vlist))
    print(vlist)
# len():获取列表的长度,有几个元素就返回几
    print(len(vlist))


# 作业
def list_():
    alist = [1,5,6,4,3]
    # 访问索引2
    print(alist[2])
    # 切片访问索引1到4
    print(alist[1:4])
    # 删除索引3
    alist.pop(3)
    print(alist)
   # 增加两个元素
    blist = [8,9]
    alist.extend(blist)
    print(alist)
    #第0位元素改为字符5
    alist[0] = '5'
    print(alist)
    #  获取索引长度
    print(len(alist))









if __name__ == '__main__':
    # list_sel()
    # list_del()
    #  list_add()
    # list_updata()
    # list_order_by()
    # list_distinct()
    list_()
