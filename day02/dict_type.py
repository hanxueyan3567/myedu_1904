
import json
# 字典   以{}包起来:前面是key,后面是value;多个键值对用,分隔开
adict = {"username":"韩n","password":"123456"}
# 字典是无序的,没有索引,只能通过key去访问value,并且key不能重复


def dict_sel():
    print(adict["username"])
    print(adict["password"])

#     更新字典里面的value
def dict_updata():
    adict["username"] = '仙女本仙'
    print(adict)

#     删除字典里面的键值对
def dict_del():
    adict.pop("username")
    print(adict)

#     增加字典里面的键值对
def dict_add():
    # 如果key在原本的字典中不存在,则会新加一个键值对
    adict = {'age':25,'sex':'女'}
    print(adict)
    bdict = {'class':'1904','city':'安徽','tuple':(4,6,8)}
    # 合并方法一:将bdict添加进adict
    adict.update(bdict)
    print(adict)
    # 合并方法二:将adict和bdict合并,新生成一个dict
    cdict = {"username":'韩雪燕'}
    # 注意第二个字典参数前,要加**(多种数据类型时,字典倒数第一位前面加**,元组倒数第二位前面加*)
    ddict = dict(adict,**cdict)
    print(ddict)

#     字典转字符串类型
def dict_zhuanh():
    print(adict)
    print(type(adict))
    # json.dumps(adict)字典 转换成 字符串
    # str_dict = json.dumps(adict)
    # 防止中文乱码加ensure_ascii=False
    str_dict = json.dumps(adict,ensure_ascii=False)
    print(str_dict)
    print(type(str_dict))

    dict_str='{"username": "卡见风使舵", "password": "123456"}'
     # json.loads(dict_str)  字符串 转换 成字典
    json_loads = json.loads(dict_str)
    print(type(json_loads))


if __name__ == '__main__':
    # dict_sel()
    # dict_updata()
    # dict_del()
    # dict_add()
    dict_zhuanh()






