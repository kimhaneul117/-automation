########### AOS init 파일 설정
#!/usr/bin/env python

# -- coding: utf-8 --
import os
import json
from appium import webdriver

class TestConfig():
    driver = 'driver'
    check_loop_count = 3
    is_passed = False
    is_finished = False
    is_initialized = False
    res = []
    port = None
    f = False
    sdkver = None
    dname = None
    udid = None
    auto = None
    ratio = None
    os = None
    environment = None
    user_name = None
    password = None
    name = None
    account = None
    accountname = None
    ap_path = None
    brand_path = None
    phonenum = None
    # 카드 결제
    birth = None
    paypassword = None
    hn_cardNum_1 = None
    hn_cardNum_2 = None
    hn_cardNum_3 = None
    hn_cardNum_4 = None
    hn_CVCNum = None
    hn_password = None
    sh_cardNum_1 = None
    sh_cardNum_2 = None
    sh_cardNum_3 = None
    sh_cardNum_4 = None
    sh_CVCNum = None
    sh_password_1 = None
    sh_password_2 = None
    # 휴대폰 결제
    phonepassword = None
    # 간편결제
    naverid = None
    naverpw = None
    npaypassword = None
    paycoid = None
    paycopw = None
    paycobirth = None
    paycopassword = None
    smaileid = None
    smailepw = None
    smailepassword = None

def initialize_bp(target, argv):
    with open(os.path.join(f"{TEST_CONFIG.ap_path}", "info.json"), encoding='UTF8') as json_file:
        json_data = json.load(json_file)
        json_string = json_data[argv]
        TEST_CONFIG.port = json_string['port']
        TEST_CONFIG.sdkver = json_string['sdkver']
        TEST_CONFIG.dname = json_string['dname']
        TEST_CONFIG.udid = json_string['udid']
        TEST_CONFIG.auto = json_string['auto']
        TEST_CONFIG.ratio = json_string['ratio']
        TEST_CONFIG.os = json_string['os']
        TEST_CONFIG.environment = json_string['environment']
        TEST_CONFIG.user_name = json_string['user_name']
        TEST_CONFIG.password = json_string['password']
        TEST_CONFIG.name = json_string['name']
        TEST_CONFIG.account = json_string['account']
        TEST_CONFIG.accountname = json_string['accountname']
        TEST_CONFIG.phonenum = json_string['phonenum']
        TEST_CONFIG.birth = json_string['birth']
        TEST_CONFIG.paypassword = json_string['paypassword']
        TEST_CONFIG.hn_cardNum_1 = json_string['hn_cardNum_1']
        TEST_CONFIG.hn_cardNum_2 = json_string['hn_cardNum_2']
        TEST_CONFIG.hn_cardNum_3 = json_string['hn_cardNum_3']
        TEST_CONFIG.hn_cardNum_4 = json_string['hn_cardNum_4']
        TEST_CONFIG.hn_CVCNum = json_string['hn_CVCNum']
        TEST_CONFIG.hn_password = json_string['hn_password']
        TEST_CONFIG.sh_cardNum_1 = json_string['sh_cardNum_1']
        TEST_CONFIG.sh_cardNum_2 = json_string['sh_cardNum_2']
        TEST_CONFIG.sh_cardNum_3 = json_string['sh_cardNum_3']
        TEST_CONFIG.sh_cardNum_4 = json_string['sh_cardNum_4']
        TEST_CONFIG.sh_CVCNum = json_string['sh_CVCNum']
        TEST_CONFIG.sh_password_1 = json_string['sh_password_1']
        TEST_CONFIG.sh_password_2 = json_string['sh_password_2']
        TEST_CONFIG.phonepassword = json_string['phonepassword']
        TEST_CONFIG.naverid = json_string['naverid']
        TEST_CONFIG.naverpw = json_string['naverpw']
        TEST_CONFIG.npaypassword = json_string['npaypassword']
        TEST_CONFIG.paycoid = json_string['paycoid']
        TEST_CONFIG.paycopw = json_string['paycopw']
        TEST_CONFIG.paycobirth = json_string['paycobirth']
        TEST_CONFIG.paycopassword = json_string['paycopassword']
        TEST_CONFIG.smaileid = json_string['smaileid']
        TEST_CONFIG.smailepw = json_string['smailepw']
        TEST_CONFIG.smailepassword = json_string['smailepassword']
        app = os.path.join(f"{TEST_CONFIG.ap_path}", "APKs", "Amorepacificmall.apk")

    TEST_CONFIG.driver = webdriver.Remote(
        command_executor=f'http://127.0.0.1:{TEST_CONFIG.port}/wd/hub',
        desired_capabilities={
            'app': app,
            "appPackage": "com.amorepacific.amorepacificmall",
            "appActivity": "com.amorepacific.amorepacificmall.app.screen.activity.intro.component.IntroActivity",
            "platformName": "Android",
            "platformVersion": TEST_CONFIG.sdkver,
            "deviceName": TEST_CONFIG.dname,
            "udid": TEST_CONFIG.udid,
            "automationName": TEST_CONFIG.auto,
            "newCommandTimeout": 10000,
            "noReset": "true"
        }
    )