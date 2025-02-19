    def test_023_HOME_뷰티_라이브(self):
        try:
            # 팝업 출력 시 "오늘은 보지 않기" 클릭
            if self.is_element_present('com.amorepacific.amorepacificmall:id/activity_notice_popup_state_text_view', By.ID):
                self.interact_by_id('com.amorepacific.amorepacificmall:id/activity_notice_popup_state_text_view')

            ### 로그인 상태 확인 ###
            self.interact_by_id('com.amorepacific.amorepacificmall:id/ib_bottom_my')  # 마이 파우치 클릭
            try:
                self.interact_by_id('com.amorepacific.amorepacificmall:id/tv_userName', click=False)  # 로그인 확인
            except:
                # 로그인 화면
                self.interact_by_xpath('(//android.widget.EditText)[1]', clear=True, send_keys_msg=TCFG.user_name)
                self.interact_by_xpath('(//android.widget.EditText)[2]', clear=True, send_keys_msg=TCFG.password)
                self.interact_by_xpath('(//android.widget.EditText)[2]')
                # 키보드 이동 버튼 클릭
                TCFG.driver.press_keycode(66)
                self.interact_by_id('com.amorepacific.amorepacificmall:id/tv_userName', click=False)  # 로그인 확인

            TCFG.driver.back()
            self.interact_by_id('com.amorepacific.amorepacificmall:id/ib_bottom_home')  # 홈으로 이동

            ### 아모레몰 메인 화면 ###
            if TCFG.environment == '2009':
                for i in range(0, 10):
                    TCFG.driver.swipe(TCFG.res[0] * 0.5, TCFG.res[1] * 0.7, TCFG.res[0] * 0.5, TCFG.res[1] * 0.3)  # BEAUTY LIVE 코너까지 스크롤
                    sleep(1)
            else:
                for i in range(0, 7):
                    TCFG.driver.swipe(TCFG.res[0] * 0.5, TCFG.res[1] * 0.7, TCFG.res[0] * 0.5, TCFG.res[1] * 0.3)  # BEAUTY LIVE 코너까지 스크롤
                    sleep(1)

            scroll_xpath(self, '//android.widget.TextView[@text="BEAUTY LIVE"]', TCFG.res[1] * 0.99, y1=500, y2=200, click=False)  # BEAUTY LIVE 코너까지 스크롤

            # 첫 번째 라이브 플래그 > 방송 중인 경우
            if self.is_element_present('//*[@resource-id="com.amorepacific.amorepacificmall:id/live_desc_live_play_time"][contains(@text,"LIVE")][1]', By.XPATH):
                self.interact_by_xpath('(//android.view.ViewGroup[@resource-id="com.amorepacific.amorepacificmall:id/custom_product_img_layout"])[1]')  # 상품 카드 상품 이미지 클릭
                sleep(2)

                ## 상품 상세 화면 ##
                self.interact_by_xpath('//android.widget.Button[@text="구매하기"]', click=False)  # 구매하기 버튼 확인
            # 첫 번째 라이브 플래그 > 오늘 방송 예정인 경우
            elif self.is_element_present('//*[@resource-id="com.amorepacific.amorepacificmall:id/live_desc_live_play_time"][contains(@text,"오늘")][1]', By.XPATH):
                self.interact_by_xpath('(//android.view.ViewGroup[@resource-id="com.amorepacific.amorepacificmall:id/custom_product_img_layout"])[1]')  # 상품 카드 상품 이미지 클릭
                sleep(2)

                ## 상품 상세 화면 ##
                self.interact_by_xpath('//android.widget.Button[@text="구매하기"]', click=False)  # 구매하기 버튼 확인
            # 첫 번째 라이브 플래그 > 내일 방송 예정인 경우
            elif self.is_element_present('//*[@resource-id="com.amorepacific.amorepacificmall:id/live_desc_live_play_time"][contains(@text,"내일")][1]', By.XPATH):
                self.interact_by_xpath('(//android.view.ViewGroup[@resource-id="com.amorepacific.amorepacificmall:id/custom_product_img_layout"])[1]')  # 상품 카드 상품 이미지 클릭
                sleep(2)

                ## 상품 상세 화면 ##
                self.interact_by_xpath('//android.widget.Button[@text="구매하기"]', click=False)  # 구매하기 버튼 확인
            # 첫 번째 라이브 플래그 > 내일 모레 이후 방송 얘정인 경우
            elif self.is_element_present('//*[@resource-id="com.amorepacific.amorepacificmall:id/live_desc_live_play_time"][contains(@text,"월")][1]', By.XPATH):
                self.interact_by_xpath('(//android.view.ViewGroup[@resource-id="com.amorepacific.amorepacificmall:id/custom_product_img_layout"])[1]')  # 상품 카드 상품 이미지 클릭
                sleep(2)

                ## 상품 상세 화면 ##
                self.interact_by_xpath('//android.widget.Button[@text="구매하기"]', click=False)  # 구매하기 버튼 확인
            else:
                raise AssertionError('HOME 뷰티 라이브 코너 라이브 플래그 상태 fail 발생')

            TCFG.driver.back()  # 상품 상세 > 메인 화면
        except:
            self.capture_screen()
            self.assertEqual(0, 1)
        else:
            print(f"{sys._getframe(0).f_code.co_name} Passed")
            TCFG.is_passed = True
