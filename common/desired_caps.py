from appium import webdriver
import logging
import logging.config
import yaml
import os

CON_LOG='../config/logger.conf'
logging.config.fileConfig(CON_LOG)
logging=logging.getLogger()

def appium_desired():
    # file = open('../config/desired_caps.yaml', 'r')
    #     # data = yaml.load(file, Loader=yaml.FullLoader)
    #     # file.close()
    # with open('../config/desired_caps_xy.yaml', 'r',encoding='utf-8') as file:
    with open('../config/desired_caps.yaml', 'r',encoding='utf-8') as file:
        data=yaml.load(file,Loader=yaml.FullLoader)

    desired_caps = {}
    desired_caps['platformName'] = data['platformName']
    desired_caps['platformVersion'] = data['platformVersion']
    desired_caps['deviceName'] = data['deviceName']
    base_dir = os.path.dirname(os.path.dirname(__file__))
    app_path = os.path.join(base_dir, 'app', data['appname'])

    desired_caps['app'] = app_path
    desired_caps['appPackage'] = data['appPackage']
    desired_caps['appActivity'] = data['appActivity']
    desired_caps['noReset'] = data['noReset']
    desired_caps['unicodeKeyboard'] = data['unicodeKeyboard']
    desired_caps['resetKeyboard'] = data['resetKeyboard']

    logging.info('start kaoyanbangAPP')
    driver = webdriver.Remote('http://' + str(data['ip']) + ':' + str(data['port']) + '/wd/hub', desired_caps)
    driver.implicitly_wait(6)
    return driver

if __name__ == '__main__':
    appium_desired()
    # with open('../config/desired_caps.yaml', 'r',encoding='utf-8') as file:
    #     data=yaml.load(file,Loader=yaml.FullLoader)
    # base_dir=os.path.dirname(os.path.dirname(__file__))
    # print(__file__)
    # print(base_dir)
    #
    # app_path=os.path.join(base_dir,'app',data['appname'])
    # print(app_path)