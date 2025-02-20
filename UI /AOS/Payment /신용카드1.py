@unittest.skipIf(sys.argv[1] == '2023', 'PRD 환경 두 개의 단말로 수행하기 위한 Skip')
def test_086_신용카드_국민(self):
    try:
        # 스크린샷 저장 후 저장된 이미지와 매칭
        matching = Matching()
        screenshots_path = os.path.join(f"{TCFG.brand_path}", "Screenshots")
        general_payment = os.path.join(f"{TCFG.ap_path}", "Purchase", "Android", "public", "amoremall_general_payment.png")
        credit_card = os.path.join(f"{TCFG.ap_path}", "Purchase", "Android", "capture_creditcard", "amoremall_credit_card.png")
        card_selection = os.path.join(f"{TCFG.ap_path}", "Purchase", "Android", "capture_creditcard", "amoremall_card_selection.png")

        # 팝업 출력 시 "오늘은 보지 않기" 클릭
        if self.is_element_present('com.amorepacific.amorepacificmall:id/activity_notice_popup_state_text_view', By.ID):
            self.interact_by_id('com.amorepacific.amorepacificmall:id/activity_notice_popup_state_text_view')

        ### 아모레몰 메인 화면 ###
        self.interact_by_id('com.amorepacific.amorepacificmall:id/ib_bottom_my', search_sec=10)  # 마이 파우치 클릭

        # 로그인 되어있지 않을 경우
        if not self.is_element_present('com.amorepacific.amorepacificmall:id/tv_userName', By.ID):
            # 아이디, 비밀번호 입력
            self.interact_by_xpath('(//android.widget.EditText)[1]', clear=True, send_keys_msg=TCFG.user_name)
            self.interact_by_xpath('(//android.widget.EditText)[2]', clear=True, send_keys_msg=TCFG.password)
            self.interact_by_xpath('(//android.widget.EditText)[2]')
            TCFG.driver.press_keycode(66)  # 키보드 이동 버튼 클릭

        ### 마이파우치 화면 > 상품 검색 ###
        self.interact_by_id('com.amorepacific.amorepacificmall:id/header_search_button_image_view')  # 검색 아이콘 클릭
        self.interact_by_id('com.amorepacific.amorepacificmall:id/search_edit_text')  # 검색 필드 클릭

        if TCFG.environment == 'PRD':
            self.interact_by_id('com.amorepacific.amorepacificmall:id/search_edit_text', send_keys_msg='0.2 테라피 에어')  # 텍스트 입력
        if TCFG.environment == 'STG':
            self.interact_by_id('com.amorepacific.amorepacificmall:id/search_edit_text', send_keys_msg='대량주문용 온라인1')  # 텍스트 입력

        self.interact_by_id('com.amorepacific.amorepacificmall:id/search_button')  # 검색 버튼 클릭

        ### 검색 결과 화면 ###
        self.interact_by_id('iv_prd_img')  # 첫 번째 제품 이미지 클릭

        ### 상품 상세 화면 ###
        try:
            self.interact_by_xpath('//*[@text="구매하기"]')  # 구매하기 버튼 클릭
        except:
            # 재입고 버튼 노출 시 pass 뒤로가기 후 다음 아이템 선택
            self.interact_by_xpath('//*[@text="재입고 알림 신청"]', click=False)
            self.interact_by_id('com.amorepacific.amorepacificmall:id/back_button_image_view')
            self.interact_by_xpath('(//android.widget.LinearLayout[@*="com.amorepacific.amorepacificmall:id/layout_whole"])[2]')
            self.interact_by_xpath('//*[@text="구매하기"]')

        if TCFG.environment == 'PRD':
            self.interact_by_xpath('//android.widget.Button[@text="상품을 선택해주세요"]')  # 상품을 선택해주세요 드롭다운 리스트 클릭
            self.interact_by_xpath('(//*[contains(@text,"0원")])[1]')  # 옵션 첫 번째 상품 선택
            self.interact_by_xpath('//*[@text="구매하기"]')  # 구매하기 버튼 클릭
        if TCFG.environment == 'STG':
            self.interact_by_xpath('//*[@text="구매하기"]')  # 구매하기 버튼 클릭

        ### 주문서 화면 ###
        sleep(10)
        TCFG.driver.press_keycode(123)  # 최하단으로 이동
        sleep(3)

        # 구매조건 및 결제 진행 동의 체크박스 선택
        if TCFG.port == '2009' or TCFG.port == '2023':
            self.T_Act(78, 1430, 19, low_corr=False)
        if TCFG.port == '2010':
            TouchAction(TCFG.driver).tap(None, 78, 1480, 1).perform()
        sleep(2)

        # 결제수단 선택 영역까지 swipe 동작 진행
        if TCFG.port == '2010':
            TCFG.driver.swipe(TCFG.res[0] * 0.5, TCFG.res[1] * 0.2, TCFG.res[0] * 0.5, TCFG.res[1] * 0.6)
            sleep(2)
        if TCFG.port == '2009' or TCFG.port == '2023':
            TCFG.driver.swipe(TCFG.res[0] * 0.5, TCFG.res[1] * 0.2, TCFG.res[0] * 0.5, TCFG.res[1] * 0.8)
            sleep(2)

        # 결제 수단 > 일반 결제 선택
        TCFG.driver.save_screenshot(f'{screenshots_path}/amoremall_general_payment.png')
        center = matching.detectimage(f'{screenshots_path}/amoremall_general_payment.png', general_payment)
        TouchAction(TCFG.driver).tap(None, center[0], center[1], 1).perform()
        sleep(3)

        # 아모레 페이 간편 등록 레이어 팝업 노출 시 닫기 동작
        amorepay_popup = self.is_element_present('//android.view.View[@resource-id="popAmorePay"]', By.XPATH)

        if amorepay_popup:
            self.interact_by_xpath('//android.widget.Button[@text="팝업 닫기 "]')

        if TCFG.port == '2009' or TCFG.port == '2023':
            # 밑으로 조금 이동
            TCFG.driver.swipe(TCFG.res[0] * 0.5, TCFG.res[1] * 0.5, TCFG.res[0] * 0.5, TCFG.res[1] * 0.2)

        # 일반 결제 > 신용카드 결제 선택
        TCFG.driver.save_screenshot(f'{screenshots_path}/amoremall_credit_card.png')
        center = matching.detectimage(f'{screenshots_path}/amoremall_credit_card.png', credit_card)
        TouchAction(TCFG.driver).tap(None, center[0], center[1], 1).perform()
        sleep(2)

        # 카드를 선택해주세요 드롭다운 리스트 클릭
        TCFG.driver.save_screenshot(f'{screenshots_path}/amoremall_card_selection.png')
        center = matching.detectimage(f'{screenshots_path}/amoremall_card_selection.png', card_selection)
        TouchAction(TCFG.driver).tap(None, center[0], center[1], 1).perform()
        sleep(3)

        self.interact_by_xpath('//android.view.View[contains(@text,"국민")]')  # 카드사 선택 > 국민 선택
        sleep(2)

        # 결제하기 버튼 클릭
        TouchAction(TCFG.driver).tap(None, 530, 2000, 1).perform()
        if TCFG.environment == 'STG':
            sleep(1.5)
            TouchAction(TCFG.driver).tap(None, 329, 1289, 1).perform()  # 스페셜 프로모션 제외하고 구매 선택
        sleep(5)

        ### KG 이니시스 화면 ###
        self.interact_by_xpath('//android.widget.CheckBox[contains(@text, "전체")]')  # 전체 동의 클릭
        self.interact_by_xpath('//*[@*="다음"]')  # 다음 클릭
        self.interact_by_xpath('//*[@text="앱 없이 결제"]')  # 앱 없이 결제 클릭 (국민)
        sleep(2)

        ### KB Pay 화면 ###
        self.interact_by_xpath('//android.view.View[1]/android.widget.EditText', send_keys_msg='010'+TCFG.phonenum)  # 휴대폰 번호 입력
        self.interact_by_xpath('//android.view.View[2]/android.widget.EditText', send_keys_msg=TCFG.birth)  # 생년 월일 입력
        self.interact_by_xpath('//*[@*="개인정보 수집이용 동의 체크안됨"]')  # 개인정보 수집이용 동의 클릭
        self.interact_by_xpath('//*[@text="로그인"]')  # 로그인 버튼 클릭

        # 앱 재설치 시 기기 인증 화면 노출 > 등록된 번호로 내 기기 인증 받기 전화 걸기 진행
        try:
            self.interact_by_xpath('//android.widget.Button[@text="본인인증"][@resource-id="regBtn"]')  # 내 기기 인증 받기 영역 본인 인증 클릭
            x, y = self.get_loc('//android.view.View[@resource-id="header"]', strategy=By.XPATH)  # header 인식 (x:0, y:213)
            self.T_Act(x+200, y+208, '18.5', low_corr=False)  # 전체 동의 버튼 클릭
            self.interact_by_xpath('//android.widget.Image')  # 다음 클릭
            self.interact_by_xpath('//android.widget.Button[@text="인증 전화 받기"]')  # 인증 전화 받기 클릭
            sleep(15)  # 전화 받기 후 인증 절차 수동 진행
        except:
            pass

        # 카드 선택을 위한 다음*3 진행
        self.interact_by_xpath('//*[@text="Next"]')
        self.interact_by_xpath('//*[@text="Next"]')
        self.interact_by_xpath('//*[@text="Next"]')

        # 결제하기 버튼 클릭
        if TCFG.port == '2010':
            self.interact_by_xpath('//android.widget.Button[@*="goPayBtn"]')
        if TCFG.port == '2009' or TCFG.port == '2023':
            self.interact_by_xpath('//android.widget.Button[@*="결제하기"]')

        for i in TCFG.paypassword:
            self.interact_by_xpath(f'//android.widget.Button[@text="{i}"]')
        self.interact_by_xpath('//*[@text="확인"]')
        sleep(5)

        ### 주문 완료 화면 ###
        try:
            self.interact_by_xpath('//*[@*="괜찮아요"]')  # 브랜드 좋아요 추가 팝업 괜찮아요 클릭
        except:
            pass

        self.interact_by_xpath('//*[contains(@text,"완료되었습니다")]', click=False, search_sec=5)

        try:
            self.interact_by_xpath('//android.widget.Button[@text="레이어 닫기"]')  # 주문완료 팝업 닫기

            ### 아모레몰 메인 ###
            self.interact_by_id('com.amorepacific.amorepacificmall:id/ib_bottom_my')  # 마이 파우치 클릭
            scroll_id(self, 'com.amorepacific.amorepacificmall:id/ly_order_list', loc=TCFG.res[1] * 0.55, y1=TCFG.res[1] * 0.6, y2=TCFG.res[1] * 0.5)  # 주문/배송 조회 탭 메뉴 클릭

            # # 최하단으로 이동
            # for i in range(0, 5):
            #     TCFG.driver.swipe(TCFG.res[0] * 0.5, TCFG.res[1] * 0.8, TCFG.res[0] * 0.5, TCFG.res[1] * 0.2)
            #
            # # 주문배송조회 버튼 클릭
            # if (TCFG.port == '2009'):
            #     TouchAction(TCFG.driver).tap(None, 530, 1800, 1).perform()
            # if (TCFG.port == '2023'):
            #     TouchAction(TCFG.driver).tap(None, 530, 1840, 1).perform()
            # if (TCFG.port == '2010''):
            #     TouchAction(TCFG.driver).tap(None, 530, 1758, 1).perform()
            # sleep(3)

            ### 주문/배송 조회 화면 ###
            sleep(5)
            self.interact_by_xpath('//android.widget.Button[@text="주문취소"]', search_sec=10)  # 주문내역 > 첫 번째 주문 건 주문취소 버튼 클릭

            ### 주문 취소 화면 ###
            self.interact_by_xpath('//android.widget.CheckBox')  # 전체선택 체크 박스 선택
            self.interact_by_xpath('//*[@text="계속진행하기"]')  # 계속진행하기 버튼 클릭
            self.interact_by_xpath('//*[@text="신청완료하기"]')  # 신청완료하기 버튼 클릭

            ### 주문 취소 완료 화면 ###
            self.interact_by_xpath('//*[@text="주문취소완료"]', click=False)  # 주문 취소 완료 타이틀 확인
            self.interact_by_xpath('//*[@text="취소완료"]', click=False)  # 주문 상태 취소 완료 확인
            self.interact_by_xpath('//android.widget.ListView[3]/..//*[contains(@text,"0원")]', click=False)  # 최종 취소 금액 노출 확인
        except:
            self.assertEqual(0, 1)
    except:
        self.capture_screen_payment()
        self.assertEqual(1, 72)
    else:
        print(f"{sys._getframe(0).f_code.co_name} Passed")
        TCFG.is_passed = True