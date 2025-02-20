    def test_017_아모레페이_관리(self):
        try:
            ### 마이파우치 화면 ###
            scroll_id(self, 'com.amorepacific.amorepacificmall:id/ly_mng_onepay', loc=TCFG.res[1] * 0.9, y1=TCFG.res[1] * 0.7, y2=TCFG.res[1] * 0.5)  # 간편결제 관리 클릭

            ### 간편결제 관리 화면 ###
            not_subscribed = TCFG.driver.find_elements_by_id('com.amorepacific.amorepacificmall:id/txt_comment')

            # 간편결제 미가입 계정 검증
            if not_subscribed:
                self.interact_by_id('com.amorepacific.amorepacificmall:id/bt_left')  # 간편결제 회원가입 하시겠습니까 팝업 취소 버튼 클릭
            # 간편결제 가입 계정 검증
            else:
                try:
                    sleep(1)
                    self.interact_by_xpath('//android.view.View[@content-desc="이용약관 보기"]', click=False)
                    self.interact_by_xpath('//android.view.View[@content-desc="결제 비밀번호 변경"]', click=False)
                    self.interact_by_xpath('//android.view.View[@content-desc="결제서비스 해지"]', click=False)
                    self.interact_by_xpath('//android.view.View[@content-desc="결제 비밀번호 변경"]')  # 결제 비밀번호 변경 탭 진입
                    # 우측 상단 "X" 버튼 클릭
                    try:
                        self.interact_by_xpath('//android.widget.TextView[@resource-id="btn_close"]')
                    except:
                        self.interact_by_xpath('(//android.view.View[@content-desc=""])[2]')

                    # 결제 비밀번호 변경을 취소하였습니다. 팝업 확인 버튼 클릭
                    ok_button = self.is_element_present('//android.widget.Button[@text="확인"]', By.XPATH)

                    if ok_button:
                        self.interact_by_xpath('//android.widget.Button[@text="확인"]')
                    # 인식이 안될 경우 터치액션
                    else:
                        self.T_Act(545, 1200, '18.5', low_corr=False)
                finally:
                    if TCFG.environment == 'PRD':
                        self.interact_by_id('com.amorepacific.amorepacificmall:id/back_button_image_view')  # GNB 뒤로가기 동작
                    if TCFG.environment == 'STG':
                        self.interact_by_xpath('//android.widget.Button[@text=" 이전 페이지"]')
        except:
            self.capture_screen()
            self.assertEqual(0, 1)
        else:
            print(f"{sys._getframe(0).f_code.co_name} Passed")
            TCFG.is_passed = True

    def test_018_앱_설정_관리(self):
        try:
            if TCFG.environment == 'PRD':
                self.interact_by_id('com.amorepacific.amorepacificmall:id/ib_bottom_my')
            if TCFG.environment == 'STG':
                self.interact_by_xpath('//android.view.View[@content-desc="마이"]')

            ### 마이파우치 화면 ###
            scroll_id(self, 'com.amorepacific.amorepacificmall:id/ly_app_setting', loc=TCFG.res[1] * 0.9, y1=TCFG.res[1] * 0.7, y2=TCFG.res[1] * 0.5)  # 간편결제 관리 클릭

            ### 앱설정관리 화면 ###
            self.interact_by_xpath('//android.widget.TextView[@resource-id="com.amorepacific.amorepacificmall:id/setting_item_arrow_title" and @text="로그아웃"]', click=False)  # 로그아웃 확인
            # self.interact_by_xpath('//android.widget.TextView[contains(@text,"********")]', click=False)  # 아이디 마스킹 처리 확인
            self.interact_by_xpath('//android.widget.TextView[@resource-id="com.amorepacific.amorepacificmall:id/setting_item_switch_title" and @text="자동 로그인"]', click=False)  # "자동로그인" 텍스트 영역 노출 확인
            self.interact_by_xpath('(//android.widget.ImageView[@resource-id="com.amorepacific.amorepacificmall:id/setting_item_switch_button"])[1]', click=False)  # 토글 단추 노출 확인
            self.interact_by_xpath('//android.widget.TextView[@resource-id="com.amorepacific.amorepacificmall:id/setting_item_switch_title" and @text="PUSH 설정"]', click=False)  # "PUSH 설정" 텍스트 영역 노출 확인
            self.interact_by_xpath('(//android.widget.ImageView[@resource-id="com.amorepacific.amorepacificmall:id/setting_item_switch_button"])[2]', click=False)  # 토글 단추 노출 확인
            self.interact_by_xpath('//android.widget.TextView[contains(@text,"최신 버전")]', click=False)  # 최신 버전 확인
        except:
            self.capture_screen()
            self.assertEqual(0, 1)
        else:
            print(f"{sys._getframe(0).f_code.co_name} Passed")
            TCFG.is_passed = True
        finally:
            self.interact_by_id('com.amorepacific.amorepacificmall:id/img_close')  # 닫기 버튼 클릭
            self.interact_by_id('com.amorepacific.amorepacificmall:id/ib_bottom_my')  # 하단 마이파우치 진입

    def test_019_LIKE_상품(self):
        try:
            TCFG.driver.swipe(TCFG.res[0] * 0.5, TCFG.res[1] * 0.7, TCFG.res[0] * 0.5, TCFG.res[1] * 0.3)  # 하단으로 스크롤

            ### 마이파우치 화면 ###
            scroll_xpath(self, '//android.widget.TextView[@text="이런 상품은 어떠세요?"]', loc=TCFG.res[1] * 0.9, y1=TCFG.res[1] * 0.7, y2=TCFG.res[1] * 0.5, click=False)  # 하단 ♥LIKE 상품 영역까지 스크롤

            ## ♥︎LIKE 상품 탭
            self.interact_by_xpath('//android.widget.TextView[@text="♥︎LIKE 상품"]', click=False)  # ♥︎LIKE 상품 탭 확인
            TCFG.driver.swipe(TCFG.res[0] * 0.5, TCFG.res[1] * 0.5, TCFG.res[0] * 0.5, TCFG.res[1] * 0.2)  # 하단으로 스크롤

            # 좋아요한 상품이 있는 경우
            try:
                self.interact_by_xpath('(//android.widget.ImageView[@resource-id="com.amorepacific.amorepacificmall:id/recent_product_img"])[1]', click=False)  # 첫 번째 상품 이미지 확인
            # 좋아요한 상품이 없는 경우
            except:
                self.interact_by_xpath('//*[@text="좋아요한 상품이 없습니다"]', click=False)  # 문구 노출 확인
        except:
            self.capture_screen()
            self.assertEqual(0, 1)
        else:
            print(f"{sys._getframe(0).f_code.co_name} Passed")
            TCFG.is_passed = True

    def test_020_자주_구매한_상품(self):
        try:
            ## ♥︎LIKE 상품 탭
            self.interact_by_xpath('//android.widget.TextView[@text="자주 구매한 상품"]')  # 자주 구매한 상품 탭 클릭

            ## 자주 구매한 상품 탭
            # 자주 구매한 상품이 있는 경우
            try:
                self.interact_by_xpath('(//android.widget.ImageView[@resource-id="com.amorepacific.amorepacificmall:id/recent_product_img"])[1]', click=False)  # 첫 번째 상품 이미지 확인

                prod = TCFG.driver.find_elements_by_id('com.amorepacific.amorepacificmall:id/view_overlay')  # 자주 구매한 상품 요소 저장

                # 자주 구매한 상품 갯수만큼 검증
                for i in range(1, len(prod) + 1):
                    purchase = TCFG.driver.find_element_by_xpath('(//android.widget.TextView[@resource-id="com.amorepacific.amorepacificmall:id/tv_oftenCnt"])[{}]'.format(i)).text.split("회")
                    prodname = TCFG.driver.find_element_by_xpath('(//*[@resource-id="com.amorepacific.amorepacificmall:id/recent_product_title_text"])[1]').text
                    pshop = "[p]"

                    ## 자주 구매한 상품 2개 이상인 경우 검증
                    if i >= 2:
                        purchase_a = [purchase[0]]
                        purchase_a.sort(reverse=True)  # 구매 횟수 내림차순 정렬 확인
                    if int(purchase[0]) >= 2:  # 2회 이상 구매 확인
                        pass
                    else:
                        raise AssertionError("자주 구매한 상품 구매 횟수 fail 발생")

                    if prodname in pshop:  # 상품명 퍼시픽샵([P]) 미포함 확인
                        raise AssertionError("자주 구매한 상품 p샵 포함으로 fail 발생")
            # 자주 구매한 상품이 없는 경우
            except:
                self.interact_by_xpath('//*[@text="자주 구매한 상품이 없습니다"]', click=False)
        except:
            self.capture_screen()
            self.assertEqual(0, 1)
        else:
            print(f"{sys._getframe(0).f_code.co_name} Passed")
            TCFG.is_passed = True
