import pytest
from day04 import Shell




if __name__ == '__main__':
    #pytest.main(['-s', '-q', './day04'])
    shell = Shell.Shell()
    pytest.main(['-s', '-q','--alluredir' ,'./Report/xml','./day04'])
    shell.invoke('allure generate ./Report/xml -o ./Report/html --clean')