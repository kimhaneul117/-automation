    def test_017_?꾨え?덊럹??愿由?self):
        try:
            ### 留덉씠?뚯슦移??붾㈃ ###
            scroll_id(self, 'com.amorepacific.amorepacificmall:id/ly_mng_onepay', loc=TCFG.res[1] * 0.9, y1=TCFG.res[1] * 0.7, y2=TCFG.res[1] * 0.5)  # 媛꾪렪寃곗젣 愿由??대┃

            ### 媛꾪렪寃곗젣 愿由??붾㈃ ###
            not_subscribed = TCFG.driver.find_elements_by_id('com.amorepacific.amorepacificmall:id/txt_comment')

            # 媛꾪렪寃곗젣 誘멸???怨꾩젙 寃利?            if not_subscribed:
                self.interact_by_id('com.amorepacific.amorepacificmall:id/bt_left')  # 媛꾪렪寃곗젣 ?뚯썝媛???섏떆寃좎뒿?덇퉴 ?앹뾽 痍⑥냼 踰꾪듉 ?대┃
            # 媛꾪렪寃곗젣 媛??怨꾩젙 寃利?            else:
                try:
                    sleep(1)
                    self.interact_by_xpath('//android.view.View[@content-desc="?댁슜?쎄? 蹂닿린"]', click=False)
                    self.interact_by_xpath('//android.view.View[@content-desc="寃곗젣 鍮꾨?踰덊샇 蹂寃?]', click=False)
                    self.interact_by_xpath('//android.view.View[@content-desc="寃곗젣?쒕퉬???댁?"]', click=False)
                    self.interact_by_xpath('//android.view.View[@content-desc="寃곗젣 鍮꾨?踰덊샇 蹂寃?]')  # 寃곗젣 鍮꾨?踰덊샇 蹂寃???吏꾩엯
                    # ?곗륫 ?곷떒 "X" 踰꾪듉 ?대┃
                    try:
                        self.interact_by_xpath('//android.widget.TextView[@resource-id="btn_close"]')
                    except:
                        self.interact_by_xpath('(//android.view.View[@content-desc=""])[2]')

                    # 寃곗젣 鍮꾨?踰덊샇 蹂寃쎌쓣 痍⑥냼?섏??듬땲?? ?앹뾽 ?뺤씤 踰꾪듉 ?대┃
                    ok_button = self.is_element_present('//android.widget.Button[@text="?뺤씤"]', By.XPATH)

                    if ok_button:
                        self.interact_by_xpath('//android.widget.Button[@text="?뺤씤"]')
                    # ?몄떇???덈맆 寃쎌슦 ?곗튂?≪뀡
                    else:
                        self.T_Act(545, 1200, '18.5', low_corr=False)
                finally:
                    if TCFG.environment == 'PRD':
                        self.interact_by_id('com.amorepacific.amorepacificmall:id/back_button_image_view')  # GNB ?ㅻ줈媛湲??숈옉
                    if TCFG.environment == 'STG':
                        self.interact_by_xpath('//android.widget.Button[@text="在??댁쟾 ?섏씠吏"]')
        except:
            self.capture_screen()
            self.assertEqual(0, 1)
        else:
            print(f"{sys._getframe(0).f_code.co_name} Passed")
            TCFG.is_passed = True

    def test_018_???ㅼ젙_愿由?self):
        try:
            if TCFG.environment == 'PRD':
                self.interact_by_id('com.amorepacific.amorepacificmall:id/ib_bottom_my')
            if TCFG.environment == 'STG':
                self.interact_by_xpath('//android.view.View[@content-desc="留덉씠"]')

            ### 留덉씠?뚯슦移??붾㈃ ###
            scroll_id(self, 'com.amorepacific.amorepacificmall:id/ly_app_setting', loc=TCFG.res[1] * 0.9, y1=TCFG.res[1] * 0.7, y2=TCFG.res[1] * 0.5)  # 媛꾪렪寃곗젣 愿由??대┃

            ### ?깆꽕?뺢?由??붾㈃ ###
            self.interact_by_xpath('//android.widget.TextView[@resource-id="com.amorepacific.amorepacificmall:id/setting_item_arrow_title" and @text="濡쒓렇?꾩썐"]', click=False)  # 濡쒓렇?꾩썐 ?뺤씤
            # self.interact_by_xpath('//android.widget.TextView[contains(@text,"********")]', click=False)  # ?꾩씠??留덉뒪??泥섎━ ?뺤씤
            self.interact_by_xpath('//android.widget.TextView[@resource-id="com.amorepacific.amorepacificmall:id/setting_item_switch_title" and @text="?먮룞 濡쒓렇??]', click=False)  # "?먮룞濡쒓렇?? ?띿뒪???곸뿭 ?몄텧 ?뺤씤
            self.interact_by_xpath('(//android.widget.ImageView[@resource-id="com.amorepacific.amorepacificmall:id/setting_item_switch_button"])[1]', click=False)  # ?좉? ?⑥텛 ?몄텧 ?뺤씤
            self.interact_by_xpath('//android.widget.TextView[@resource-id="com.amorepacific.amorepacificmall:id/setting_item_switch_title" and @text="PUSH ?ㅼ젙"]', click=False)  # "PUSH ?ㅼ젙" ?띿뒪???곸뿭 ?몄텧 ?뺤씤
            self.interact_by_xpath('(//android.widget.ImageView[@resource-id="com.amorepacific.amorepacificmall:id/setting_item_switch_button"])[2]', click=False)  # ?좉? ?⑥텛 ?몄텧 ?뺤씤
            self.interact_by_xpath('//android.widget.TextView[contains(@text,"理쒖떊 踰꾩쟾")]', click=False)  # 理쒖떊 踰꾩쟾 ?뺤씤
        except:
            self.capture_screen()
            self.assertEqual(0, 1)
        else:
            print(f"{sys._getframe(0).f_code.co_name} Passed")
            TCFG.is_passed = True
        finally:
            self.interact_by_id('com.amorepacific.amorepacificmall:id/img_close')  # ?リ린 踰꾪듉 ?대┃
            self.interact_by_id('com.amorepacific.amorepacificmall:id/ib_bottom_my')  # ?섎떒 留덉씠?뚯슦移?吏꾩엯

    def test_019_LIKE_?곹뭹(self):
        try:
            TCFG.driver.swipe(TCFG.res[0] * 0.5, TCFG.res[1] * 0.7, TCFG.res[0] * 0.5, TCFG.res[1] * 0.3)  # ?섎떒?쇰줈 ?ㅽ겕濡?
            ### 留덉씠?뚯슦移??붾㈃ ###
            scroll_xpath(self, '//android.widget.TextView[@text="?대윴 ?곹뭹? ?대뼚?몄슂?"]', loc=TCFG.res[1] * 0.9, y1=TCFG.res[1] * 0.7, y2=TCFG.res[1] * 0.5, click=False)  # ?섎떒 ?쩖IKE ?곹뭹 ?곸뿭源뚯? ?ㅽ겕濡?
            ## ?ο툗LIKE ?곹뭹 ??            self.interact_by_xpath('//android.widget.TextView[@text="?ο툗LIKE ?곹뭹"]', click=False)  # ?ο툗LIKE ?곹뭹 ???뺤씤
            TCFG.driver.swipe(TCFG.res[0] * 0.5, TCFG.res[1] * 0.5, TCFG.res[0] * 0.5, TCFG.res[1] * 0.2)  # ?섎떒?쇰줈 ?ㅽ겕濡?
            # 醫뗭븘?뷀븳 ?곹뭹???덈뒗 寃쎌슦
            try:
                self.interact_by_xpath('(//android.widget.ImageView[@resource-id="com.amorepacific.amorepacificmall:id/recent_product_img"])[1]', click=False)  # 泥?踰덉㎏ ?곹뭹 ?대?吏 ?뺤씤
            # 醫뗭븘?뷀븳 ?곹뭹???녿뒗 寃쎌슦
            except:
                self.interact_by_xpath('//*[@text="醫뗭븘?뷀븳 ?곹뭹???놁뒿?덈떎"]', click=False)  # 臾멸뎄 ?몄텧 ?뺤씤
        except:
            self.capture_screen()
            self.assertEqual(0, 1)
        else:
            print(f"{sys._getframe(0).f_code.co_name} Passed")
            TCFG.is_passed = True

    def test_020_?먯＜_援щℓ???곹뭹(self):
        try:
            ## ?ο툗LIKE ?곹뭹 ??            self.interact_by_xpath('//android.widget.TextView[@text="?먯＜ 援щℓ???곹뭹"]')  # ?먯＜ 援щℓ???곹뭹 ???대┃

            ## ?먯＜ 援щℓ???곹뭹 ??            # ?먯＜ 援щℓ???곹뭹???덈뒗 寃쎌슦
            try:
                self.interact_by_xpath('(//android.widget.ImageView[@resource-id="com.amorepacific.amorepacificmall:id/recent_product_img"])[1]', click=False)  # 泥?踰덉㎏ ?곹뭹 ?대?吏 ?뺤씤

                prod = TCFG.driver.find_elements_by_id('com.amorepacific.amorepacificmall:id/view_overlay')  # ?먯＜ 援щℓ???곹뭹 ?붿냼 ???
                # ?먯＜ 援щℓ???곹뭹 媛?닔留뚰겮 寃利?                for i in range(1, len(prod) + 1):
                    purchase = TCFG.driver.find_element_by_xpath('(//android.widget.TextView[@resource-id="com.amorepacific.amorepacificmall:id/tv_oftenCnt"])[{}]'.format(i)).text.split("??)
                    prodname = TCFG.driver.find_element_by_xpath('(//*[@resource-id="com.amorepacific.amorepacificmall:id/recent_product_title_text"])[1]').text
                    pshop = "[p]"

                    ## ?먯＜ 援щℓ???곹뭹 2媛??댁긽??寃쎌슦 寃利?                    if i >= 2:
                        purchase_a = [purchase[0]]
                        purchase_a.sort(reverse=True)  # 援щℓ ?잛닔 ?대┝李⑥닚 ?뺣젹 ?뺤씤
                    if int(purchase[0]) >= 2:  # 2???댁긽 援щℓ ?뺤씤
                        pass
                    else:
                        raise AssertionError("?먯＜ 援щℓ???곹뭹 援щℓ ?잛닔 fail 諛쒖깮")

                    if prodname in pshop:  # ?곹뭹紐??쇱떆?쎌꺏([P]) 誘명룷???뺤씤
                        raise AssertionError("?먯＜ 援щℓ???곹뭹 p???ы븿?쇰줈 fail 諛쒖깮")
            # ?먯＜ 援щℓ???곹뭹???녿뒗 寃쎌슦
            except:
                self.interact_by_xpath('//*[@text="?먯＜ 援щℓ???곹뭹???놁뒿?덈떎"]', click=False)
        except:
            self.capture_screen()
            self.assertEqual(0, 1)
        else:
            print(f"{sys._getframe(0).f_code.co_name} Passed")
            TCFG.is_passed = True
