# ...异常处理
# try 和 except 中间写可能会出错的代码
# 如果出错 则执行 except里面的代码
# 不出错  不会执行 except里面的代码




if __name__ == '__main__':
    try:
        a = 1/0
    except:
        print('错误')
    print('14752')