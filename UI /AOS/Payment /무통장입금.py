@unittest.skipIf(sys.argv[1] == '2023', 'PRD 환경 두 개의 단말로 수행하기 위한 Skip')
def test_089_무통장입금(self):
    try:
        # 앱 종료 후 재실행
        TCFG.driver.close_app()
        sleep(2)
        TCFG.driver.launch_app()
        sleep(2)

        # 스크린샷 저장 후 저장된 이미지와 매칭
        matching = Matching()
        screenshots_path = os.path.join(f"{TCFG.brand_path}", "Screenshots")
        general_payment = os.path.join(f"{TCFG.ap_path}", "Purchase", "Android", "public", "amoremall_general_payment.png")
        bank_transfer = os.path.join(f"{TCFG.ap_path}", "Purchase", "Android", "capture_banktransfer", "amoremall_bank_transfer.png")

        ### 아모레몰 메인 화면 ###
        self.interact_by_id('com.amorepacific.amorepacificmall:id/ib_bottom_my', search_sec=10)  # 마이 파우치 클릭

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
        sleep(5)
        TCFG.driver.press_keycode(123)  # 최하단으로 이동
        sleep(3)

        # 구매조건 및 결제 진행 동의 체크박스 선택
        if TCFG.port == '2009' or TCFG.port == '2023':
            TouchAction(TCFG.driver).tap(None, 78, 1430, 1).perform()
        if TCFG.port == '2010':
            TouchAction(TCFG.driver).tap(None, 78, 1480, 1).perform()
        sleep(2)

        # 결제수단 선택 영역까지 swipe 동작 진행
        TCFG.driver.swipe(TCFG.res[0] * 0.5, TCFG.res[1] * 0.2, TCFG.res[0] * 0.5, TCFG.res[1] * 0.6)

        # 결제 수단 > 일반 결제 선택
        TCFG.driver.save_screenshot(f'{screenshots_path}/amoremall_general_payment.png')
        center = matching.detectimage(f'{screenshots_path}/amoremall_general_payment.png', general_payment)
        TouchAction(TCFG.driver).tap(None, center[0], center[1], 1).perform()
        sleep(5)

        # 무통장 입금 선택
        TCFG.driver.save_screenshot(f'{screenshots_path}/amoremall_bank_transfer.png')
        center = matching.detectimage(f'{screenshots_path}/amoremall_bank_transfer.png', bank_transfer)  # center : (726, 1249)
        TouchAction(TCFG.driver).tap(None, center[0]+100, center[1]-50, 1).perform()

        # 결제하기 버튼 클릭
        TouchAction(TCFG.driver).tap(None, 530, 2000, 1).perform()
        if TCFG.environment == 'STG':
            sleep(1.5)
            TouchAction(TCFG.driver).tap(None, 329, 1289, 1).perform()  # 스페셜 프로모션 제외하고 구매 선택
        sleep(5)

        ### KG 이니시스 화면 ###
        self.interact_by_xpath('//android.widget.CheckBox[contains(@text, "전체")]')  # 전체 동의 클릭
        self.interact_by_xpath('//*[@text="다음"]')  # 다음 버튼 클릭
        self.interact_by_xpath('//*[@text="KB국민은행"]')  # 국민은행 클릭
        self.interact_by_xpath('//*[@text="다음"]')  # 다음 버튼 클릭
        sleep(3)

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
            sleep(3)

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
        self.assertEqual(1, 74)
    else:
        print(f"{sys._getframe(0).f_code.co_name} Passed")
        TCFG.is_passed = True