import os

#os.getcwd() 获取当前目录/路径



if __name__ == '__main__':
    pwd = os.getcwd()
    print(pwd)
    # 获取上级目录的字符串
    a=os.path.abspath('..')
    print(a)
    #获取上上级目录的字符串
    b=os.path.abspath('../..')
    print(b)
