# import selenium
# from selenium import webdriver
#
#
# def test_selenium():
#     # option = webdriver.ChromeOptions()
#     # option.binary_location = 'D:\Programs\Chrome\Application\chrome.exe'
#     # driver = webdriver.Chrome('D:\Chan\Programs\chromedriver\chromedriver.exe')
#     driver = webdriver.Chrome()
#     driver.get("https://www.baidu.com/")
def func(x):
    return x + 2


def test_answer():
    assert func(3) == 5
