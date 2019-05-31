





def assert_iint():
    try:
        assert  3>2
        assert  3==3
        assert  2>1
    except:
        print('断言失败')

def assert_str():
    a = '哈哈'
    b = '嘻嘻哈哈'
    try:
        assert  a in b
        assert  a != b
    except:
        print('断言错误')


if __name__ == '__main__':
    # assert_iint()
    assert_str()
