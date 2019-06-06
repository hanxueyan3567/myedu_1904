

class human(object):
    #_init_:类的初始化方法
    #self:代表类的本身,name,age,sex初始化的时候  要用到的参数

    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex

    #类中的方法 必须包含self参数
    def eat(self):
        print(self.name+'在说话')

    def sleep(self):
        print(self.name+'在睡觉')

    #类中的方法,可以调用其他方法,可以调用属性,除了init方法
    def info(self):
        print('%s%s%s'%(self.name,self.age,self.sex))

class reader(human):
    def __init__(self,name,age,sex,job):
        self.name = name
        self.age = age
        self.sex = sex
        self.job = job
    def eat(self):
        print(self.name+'在吃汉堡')

    def do_reader(self):
        print(self.name+'读报纸')
        self.sleep()


if __name__ == '__main__':
    #新建一个对象,根据human类 新建对象
    # 对象是 类的 实例化
    # baobao = human('小米',19,'女')
    # baobao.info()
    # baobao.sleep()
    # baobao.eat()
    # print(baobao.sex)

    reader = reader('小米', 19, '女','评论家')
    reader.do_reader()
    reader.eat()
    print(reader.sex)
