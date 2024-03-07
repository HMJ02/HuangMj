import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import datetime
from retrying import retry
from change_name import Change_Name


@retry()
def get_start_date():
    start_date = input('请输入起始日期：')
    start_date = datetime.datetime.strptime(start_date, '%Y%m%d')
    start_date = datetime.datetime.strftime(start_date, '%Y-%m-%d')
    erectDate = driver.find_element(By.ID, 'erectDate')
    erectDate.send_keys(start_date)


@retry()
def get_over_date():
    over_date = input('请输入结束日期：')
    over_date = datetime.datetime.strptime(over_date, '%Y%m%d')
    over_date = datetime.datetime.strftime(over_date, '%Y-%m-%d')
    nothing = driver.find_element(By.ID, 'nothing')
    nothing.send_keys(over_date)


# 选择货币
@retry()
def select_currency():
    val = input('选择货币：')
    select = Select(driver.find_element(By.XPATH, f'//select[@id="pjname"]'))
    select.select_by_value(Change_Name(val))


# 输出结果
def get_data():
    try:
        price = driver.find_element(By.XPATH, '//tr[@class="odd"][1]/td[4]')
    except:
        price = None
    with open('result.txt', 'a', encoding='utf-8') as f:
        f.write(price.text + '\n')


if __name__ == '__main__':
    options = webdriver.ChromeOptions()
    options.add_experimental_option('detach', True)

    driver = webdriver.Chrome(options=options)
    driver.get('https://www.boc.cn/sourcedb/whpj/')

    get_start_date()
    get_over_date()
    select_currency()

    # 执行页面加载函数
    driver.execute_script("executeSearch()")

    exit()
