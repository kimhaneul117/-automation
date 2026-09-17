    def test_023_HOME_酉고떚_?쇱씠釉?self):
        try:
            # ?앹뾽 異쒕젰 ??"?ㅻ뒛? 蹂댁? ?딄린" ?대┃
            if self.is_element_present('com.amorepacific.amorepacificmall:id/activity_notice_popup_state_text_view', By.ID):
                self.interact_by_id('com.amorepacific.amorepacificmall:id/activity_notice_popup_state_text_view')

            ### 濡쒓렇???곹깭 ?뺤씤 ###
            self.interact_by_id('com.amorepacific.amorepacificmall:id/ib_bottom_my')  # 留덉씠 ?뚯슦移??대┃
            try:
                self.interact_by_id('com.amorepacific.amorepacificmall:id/tv_userName', click=False)  # 濡쒓렇???뺤씤
            except:
                # 濡쒓렇???붾㈃
                self.interact_by_xpath('(//android.widget.EditText)[1]', clear=True, send_keys_msg=TCFG.user_name)
                self.interact_by_xpath('(//android.widget.EditText)[2]', clear=True, send_keys_msg=TCFG.password)
                self.interact_by_xpath('(//android.widget.EditText)[2]')
                # ?ㅻ낫???대룞 踰꾪듉 ?대┃
                TCFG.driver.press_keycode(66)
                self.interact_by_id('com.amorepacific.amorepacificmall:id/tv_userName', click=False)  # 濡쒓렇???뺤씤

            TCFG.driver.back()
            self.interact_by_id('com.amorepacific.amorepacificmall:id/ib_bottom_home')  # ?덉쑝濡??대룞

            ### ?꾨え?덈ぐ 硫붿씤 ?붾㈃ ###
            if TCFG.environment == '2009':
                for i in range(0, 10):
                    TCFG.driver.swipe(TCFG.res[0] * 0.5, TCFG.res[1] * 0.7, TCFG.res[0] * 0.5, TCFG.res[1] * 0.3)  # BEAUTY LIVE 肄붾꼫源뚯? ?ㅽ겕濡?
                    sleep(1)
            else:
                for i in range(0, 7):
                    TCFG.driver.swipe(TCFG.res[0] * 0.5, TCFG.res[1] * 0.7, TCFG.res[0] * 0.5, TCFG.res[1] * 0.3)  # BEAUTY LIVE 肄붾꼫源뚯? ?ㅽ겕濡?
                    sleep(1)

            scroll_xpath(self, '//android.widget.TextView[@text="BEAUTY LIVE"]', TCFG.res[1] * 0.99, y1=500, y2=200, click=False)  # BEAUTY LIVE 肄붾꼫源뚯? ?ㅽ겕濡?

            # 泥?踰덉㎏ ?쇱씠釉??뚮옒洹?> 諛⑹넚 以묒씤 寃쎌슦
            if self.is_element_present('//*[@resource-id="com.amorepacific.amorepacificmall:id/live_desc_live_play_time"][contains(@text,"LIVE")][1]', By.XPATH):
                self.interact_by_xpath('(//android.view.ViewGroup[@resource-id="com.amorepacific.amorepacificmall:id/custom_product_img_layout"])[1]')  # ?곹뭹 移대뱶 ?곹뭹 ?대?吏 ?대┃
                sleep(2)

                ## ?곹뭹 ?곸꽭 ?붾㈃ ##
                self.interact_by_xpath('//android.widget.Button[@text="援щℓ?섍린"]', click=False)  # 援щℓ?섍린 踰꾪듉 ?뺤씤
            # 泥?踰덉㎏ ?쇱씠釉??뚮옒洹?> ?ㅻ뒛 諛⑹넚 ?덉젙??寃쎌슦
            elif self.is_element_present('//*[@resource-id="com.amorepacific.amorepacificmall:id/live_desc_live_play_time"][contains(@text,"?ㅻ뒛")][1]', By.XPATH):
                self.interact_by_xpath('(//android.view.ViewGroup[@resource-id="com.amorepacific.amorepacificmall:id/custom_product_img_layout"])[1]')  # ?곹뭹 移대뱶 ?곹뭹 ?대?吏 ?대┃
                sleep(2)

                ## ?곹뭹 ?곸꽭 ?붾㈃ ##
                self.interact_by_xpath('//android.widget.Button[@text="援щℓ?섍린"]', click=False)  # 援щℓ?섍린 踰꾪듉 ?뺤씤
            # 泥?踰덉㎏ ?쇱씠釉??뚮옒洹?> ?댁씪 諛⑹넚 ?덉젙??寃쎌슦
            elif self.is_element_present('//*[@resource-id="com.amorepacific.amorepacificmall:id/live_desc_live_play_time"][contains(@text,"?댁씪")][1]', By.XPATH):
                self.interact_by_xpath('(//android.view.ViewGroup[@resource-id="com.amorepacific.amorepacificmall:id/custom_product_img_layout"])[1]')  # ?곹뭹 移대뱶 ?곹뭹 ?대?吏 ?대┃
                sleep(2)

                ## ?곹뭹 ?곸꽭 ?붾㈃ ##
                self.interact_by_xpath('//android.widget.Button[@text="援щℓ?섍린"]', click=False)  # 援щℓ?섍린 踰꾪듉 ?뺤씤
            # 泥?踰덉㎏ ?쇱씠釉??뚮옒洹?> ?댁씪 紐⑤젅 ?댄썑 諛⑹넚 ?섏젙??寃쎌슦
            elif self.is_element_present('//*[@resource-id="com.amorepacific.amorepacificmall:id/live_desc_live_play_time"][contains(@text,"??)][1]', By.XPATH):
                self.interact_by_xpath('(//android.view.ViewGroup[@resource-id="com.amorepacific.amorepacificmall:id/custom_product_img_layout"])[1]')  # ?곹뭹 移대뱶 ?곹뭹 ?대?吏 ?대┃
                sleep(2)

                ## ?곹뭹 ?곸꽭 ?붾㈃ ##
                self.interact_by_xpath('//android.widget.Button[@text="援щℓ?섍린"]', click=False)  # 援щℓ?섍린 踰꾪듉 ?뺤씤
            else:
                raise AssertionError('HOME 酉고떚 ?쇱씠釉?肄붾꼫 ?쇱씠釉??뚮옒洹??곹깭 fail 諛쒖깮')

            TCFG.driver.back()  # ?곹뭹 ?곸꽭 > 硫붿씤 ?붾㈃
        except:
            self.capture_screen()
            self.assertEqual(0, 1)
        else:
            print(f"{sys._getframe(0).f_code.co_name} Passed")
            TCFG.is_passed = True
