# 题: 新建一个字典变量,里面有两个键值对,通过key访问一个值,删除一个键值对,添加一个键值对,更改任意一个值,再新建一个字典,将两个合并
adict = {'class':'1904','age':25}

def dict_sel():
    # 访问一个
    print(adict['class'])
    # 删除一个
    adict.pop('age')
    print(adict)
    #     添加一个
    bdict = {'name':'hxy'}
    adict.update(bdict)
    print(adict)
    #更改一个
    adict['age'] = 24
    print(adict)
    #新建一个字典
    cdict = {'province':'安徽','sex':'女'}
    ddict = dict(adict,**cdict)
    print(ddict)








if __name__ == '__main__':
        dict_sel()
