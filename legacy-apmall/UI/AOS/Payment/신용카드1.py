@unittest.skipIf(sys.argv[1] == '2023', 'PRD ?섍꼍 ??媛쒖쓽 ?⑤쭚濡??섑뻾?섍린 ?꾪븳 Skip')
def test_086_?좎슜移대뱶_援??(self):
    try:
        # ?ㅽ겕由곗꺑 ???????λ맂 ?대?吏? 留ㅼ묶
        matching = Matching()
        screenshots_path = os.path.join(f"{TCFG.brand_path}", "Screenshots")
        general_payment = os.path.join(f"{TCFG.ap_path}", "Purchase", "Android", "public", "amoremall_general_payment.png")
        credit_card = os.path.join(f"{TCFG.ap_path}", "Purchase", "Android", "capture_creditcard", "amoremall_credit_card.png")
        card_selection = os.path.join(f"{TCFG.ap_path}", "Purchase", "Android", "capture_creditcard", "amoremall_card_selection.png")

        # ?앹뾽 異쒕젰 ??"?ㅻ뒛? 蹂댁? ?딄린" ?대┃
        if self.is_element_present('com.amorepacific.amorepacificmall:id/activity_notice_popup_state_text_view', By.ID):
            self.interact_by_id('com.amorepacific.amorepacificmall:id/activity_notice_popup_state_text_view')

        ### ?꾨え?덈ぐ 硫붿씤 ?붾㈃ ###
        self.interact_by_id('com.amorepacific.amorepacificmall:id/ib_bottom_my', search_sec=10)  # 留덉씠 ?뚯슦移??대┃

        # 濡쒓렇???섏뼱?덉? ?딆쓣 寃쎌슦
        if not self.is_element_present('com.amorepacific.amorepacificmall:id/tv_userName', By.ID):
            # ?꾩씠?? 鍮꾨?踰덊샇 ?낅젰
            self.interact_by_xpath('(//android.widget.EditText)[1]', clear=True, send_keys_msg=TCFG.user_name)
            self.interact_by_xpath('(//android.widget.EditText)[2]', clear=True, send_keys_msg=TCFG.password)
            self.interact_by_xpath('(//android.widget.EditText)[2]')
            TCFG.driver.press_keycode(66)  # ?ㅻ낫???대룞 踰꾪듉 ?대┃

        ### 留덉씠?뚯슦移??붾㈃ > ?곹뭹 寃??###
        self.interact_by_id('com.amorepacific.amorepacificmall:id/header_search_button_image_view')  # 寃???꾩씠肄??대┃
        self.interact_by_id('com.amorepacific.amorepacificmall:id/search_edit_text')  # 寃???꾨뱶 ?대┃

        if TCFG.environment == 'PRD':
            self.interact_by_id('com.amorepacific.amorepacificmall:id/search_edit_text', send_keys_msg='0.2 ?뚮씪???먯뼱')  # ?띿뒪???낅젰
        if TCFG.environment == 'STG':
            self.interact_by_id('com.amorepacific.amorepacificmall:id/search_edit_text', send_keys_msg='??됱＜臾몄슜 ?⑤씪??')  # ?띿뒪???낅젰

        self.interact_by_id('com.amorepacific.amorepacificmall:id/search_button')  # 寃??踰꾪듉 ?대┃

        ### 寃??寃곌낵 ?붾㈃ ###
        self.interact_by_id('iv_prd_img')  # 泥?踰덉㎏ ?쒗뭹 ?대?吏 ?대┃

        ### ?곹뭹 ?곸꽭 ?붾㈃ ###
        try:
            self.interact_by_xpath('//*[@text="援щℓ?섍린"]')  # 援щℓ?섍린 踰꾪듉 ?대┃
        except:
            # ?ъ엯怨?踰꾪듉 ?몄텧 ??pass ?ㅻ줈媛湲????ㅼ쓬 ?꾩씠???좏깮
            self.interact_by_xpath('//*[@text="?ъ엯怨??뚮┝ ?좎껌"]', click=False)
            self.interact_by_id('com.amorepacific.amorepacificmall:id/back_button_image_view')
            self.interact_by_xpath('(//android.widget.LinearLayout[@*="com.amorepacific.amorepacificmall:id/layout_whole"])[2]')
            self.interact_by_xpath('//*[@text="援щℓ?섍린"]')

        if TCFG.environment == 'PRD':
            self.interact_by_xpath('//android.widget.Button[@text="?곹뭹???좏깮?댁＜?몄슂"]')  # ?곹뭹???좏깮?댁＜?몄슂 ?쒕∼?ㅼ슫 由ъ뒪???대┃
            self.interact_by_xpath('(//*[contains(@text,"0??)])[1]')  # ?듭뀡 泥?踰덉㎏ ?곹뭹 ?좏깮
            self.interact_by_xpath('//*[@text="援щℓ?섍린"]')  # 援щℓ?섍린 踰꾪듉 ?대┃
        if TCFG.environment == 'STG':
            self.interact_by_xpath('//*[@text="援щℓ?섍린"]')  # 援щℓ?섍린 踰꾪듉 ?대┃

        ### 二쇰Ц???붾㈃ ###
        sleep(10)
        TCFG.driver.press_keycode(123)  # 理쒗븯?⑥쑝濡??대룞
        sleep(3)

        # 援щℓ議곌굔 諛?寃곗젣 吏꾪뻾 ?숈쓽 泥댄겕諛뺤뒪 ?좏깮
        if TCFG.port == '2009' or TCFG.port == '2023':
            self.T_Act(78, 1430, 19, low_corr=False)
        if TCFG.port == '2010':
            TouchAction(TCFG.driver).tap(None, 78, 1480, 1).perform()
        sleep(2)

        # 寃곗젣?섎떒 ?좏깮 ?곸뿭源뚯? swipe ?숈옉 吏꾪뻾
        if TCFG.port == '2010':
            TCFG.driver.swipe(TCFG.res[0] * 0.5, TCFG.res[1] * 0.2, TCFG.res[0] * 0.5, TCFG.res[1] * 0.6)
            sleep(2)
        if TCFG.port == '2009' or TCFG.port == '2023':
            TCFG.driver.swipe(TCFG.res[0] * 0.5, TCFG.res[1] * 0.2, TCFG.res[0] * 0.5, TCFG.res[1] * 0.8)
            sleep(2)

        # 寃곗젣 ?섎떒 > ?쇰컲 寃곗젣 ?좏깮
        TCFG.driver.save_screenshot(f'{screenshots_path}/amoremall_general_payment.png')
        center = matching.detectimage(f'{screenshots_path}/amoremall_general_payment.png', general_payment)
        TouchAction(TCFG.driver).tap(None, center[0], center[1], 1).perform()
        sleep(3)

        # ?꾨え???섏씠 媛꾪렪 ?깅줉 ?덉씠???앹뾽 ?몄텧 ???リ린 ?숈옉
        amorepay_popup = self.is_element_present('//android.view.View[@resource-id="popAmorePay"]', By.XPATH)

        if amorepay_popup:
            self.interact_by_xpath('//android.widget.Button[@text="?앹뾽 ?リ린 在?]')

        if TCFG.port == '2009' or TCFG.port == '2023':
            # 諛묒쑝濡?議곌툑 ?대룞
            TCFG.driver.swipe(TCFG.res[0] * 0.5, TCFG.res[1] * 0.5, TCFG.res[0] * 0.5, TCFG.res[1] * 0.2)

        # ?쇰컲 寃곗젣 > ?좎슜移대뱶 寃곗젣 ?좏깮
        TCFG.driver.save_screenshot(f'{screenshots_path}/amoremall_credit_card.png')
        center = matching.detectimage(f'{screenshots_path}/amoremall_credit_card.png', credit_card)
        TouchAction(TCFG.driver).tap(None, center[0], center[1], 1).perform()
        sleep(2)

        # 移대뱶瑜??좏깮?댁＜?몄슂 ?쒕∼?ㅼ슫 由ъ뒪???대┃
        TCFG.driver.save_screenshot(f'{screenshots_path}/amoremall_card_selection.png')
        center = matching.detectimage(f'{screenshots_path}/amoremall_card_selection.png', card_selection)
        TouchAction(TCFG.driver).tap(None, center[0], center[1], 1).perform()
        sleep(3)

        self.interact_by_xpath('//android.view.View[contains(@text,"援??")]')  # 移대뱶???좏깮 > 援?? ?좏깮
        sleep(2)

        # 寃곗젣?섍린 踰꾪듉 ?대┃
        TouchAction(TCFG.driver).tap(None, 530, 2000, 1).perform()
        if TCFG.environment == 'STG':
            sleep(1.5)
            TouchAction(TCFG.driver).tap(None, 329, 1289, 1).perform()  # ?ㅽ럹???꾨줈紐⑥뀡 ?쒖쇅?섍퀬 援щℓ ?좏깮
        sleep(5)

        ### KG ?대땲?쒖뒪 ?붾㈃ ###
        self.interact_by_xpath('//android.widget.CheckBox[contains(@text, "?꾩껜")]')  # ?꾩껜 ?숈쓽 ?대┃
        self.interact_by_xpath('//*[@*="?ㅼ쓬"]')  # ?ㅼ쓬 ?대┃
        self.interact_by_xpath('//*[@text="???놁씠 寃곗젣"]')  # ???놁씠 寃곗젣 ?대┃ (援??)
        sleep(2)

        ### KB Pay ?붾㈃ ###
        self.interact_by_xpath('//android.view.View[1]/android.widget.EditText', send_keys_msg='010'+TCFG.phonenum)  # ?대???踰덊샇 ?낅젰
        self.interact_by_xpath('//android.view.View[2]/android.widget.EditText', send_keys_msg=TCFG.birth)  # ?앸뀈 ?붿씪 ?낅젰
        self.interact_by_xpath('//*[@*="媛쒖씤?뺣낫 ?섏쭛?댁슜 ?숈쓽 泥댄겕?덈맖"]')  # 媛쒖씤?뺣낫 ?섏쭛?댁슜 ?숈쓽 ?대┃
        self.interact_by_xpath('//*[@text="濡쒓렇??]')  # 濡쒓렇??踰꾪듉 ?대┃

        # ???ъ꽕移???湲곌린 ?몄쬆 ?붾㈃ ?몄텧 > ?깅줉??踰덊샇濡???湲곌린 ?몄쬆 諛쏄린 ?꾪솕 嫄멸린 吏꾪뻾
        try:
            self.interact_by_xpath('//android.widget.Button[@text="蹂몄씤?몄쬆"][@resource-id="regBtn"]')  # ??湲곌린 ?몄쬆 諛쏄린 ?곸뿭 蹂몄씤 ?몄쬆 ?대┃
            x, y = self.get_loc('//android.view.View[@resource-id="header"]', strategy=By.XPATH)  # header ?몄떇 (x:0, y:213)
            self.T_Act(x+200, y+208, '18.5', low_corr=False)  # ?꾩껜 ?숈쓽 踰꾪듉 ?대┃
            self.interact_by_xpath('//android.widget.Image')  # ?ㅼ쓬 ?대┃
            self.interact_by_xpath('//android.widget.Button[@text="?몄쬆 ?꾪솕 諛쏄린"]')  # ?몄쬆 ?꾪솕 諛쏄린 ?대┃
            sleep(15)  # ?꾪솕 諛쏄린 ???몄쬆 ?덉감 ?섎룞 吏꾪뻾
        except:
            pass

        # 移대뱶 ?좏깮???꾪븳 ?ㅼ쓬*3 吏꾪뻾
        self.interact_by_xpath('//*[@text="Next"]')
        self.interact_by_xpath('//*[@text="Next"]')
        self.interact_by_xpath('//*[@text="Next"]')

        # 寃곗젣?섍린 踰꾪듉 ?대┃
        if TCFG.port == '2010':
            self.interact_by_xpath('//android.widget.Button[@*="goPayBtn"]')
        if TCFG.port == '2009' or TCFG.port == '2023':
            self.interact_by_xpath('//android.widget.Button[@*="寃곗젣?섍린"]')

        for i in TCFG.paypassword:
            self.interact_by_xpath(f'//android.widget.Button[@text="{i}"]')
        self.interact_by_xpath('//*[@text="?뺤씤"]')
        sleep(5)

        ### 二쇰Ц ?꾨즺 ?붾㈃ ###
        try:
            self.interact_by_xpath('//*[@*="愿쒖갖?꾩슂"]')  # 釉뚮옖??醫뗭븘??異붽? ?앹뾽 愿쒖갖?꾩슂 ?대┃
        except:
            pass

        self.interact_by_xpath('//*[contains(@text,"?꾨즺?섏뿀?듬땲??)]', click=False, search_sec=5)

        try:
            self.interact_by_xpath('//android.widget.Button[@text="?덉씠???リ린"]')  # 二쇰Ц?꾨즺 ?앹뾽 ?リ린

            ### ?꾨え?덈ぐ 硫붿씤 ###
            self.interact_by_id('com.amorepacific.amorepacificmall:id/ib_bottom_my')  # 留덉씠 ?뚯슦移??대┃
            scroll_id(self, 'com.amorepacific.amorepacificmall:id/ly_order_list', loc=TCFG.res[1] * 0.55, y1=TCFG.res[1] * 0.6, y2=TCFG.res[1] * 0.5)  # 二쇰Ц/諛곗넚 議고쉶 ??硫붾돱 ?대┃

            # # 理쒗븯?⑥쑝濡??대룞
            # for i in range(0, 5):
            #     TCFG.driver.swipe(TCFG.res[0] * 0.5, TCFG.res[1] * 0.8, TCFG.res[0] * 0.5, TCFG.res[1] * 0.2)
            #
            # # 二쇰Ц諛곗넚議고쉶 踰꾪듉 ?대┃
            # if (TCFG.port == '2009'):
            #     TouchAction(TCFG.driver).tap(None, 530, 1800, 1).perform()
            # if (TCFG.port == '2023'):
            #     TouchAction(TCFG.driver).tap(None, 530, 1840, 1).perform()
            # if (TCFG.port == '2010''):
            #     TouchAction(TCFG.driver).tap(None, 530, 1758, 1).perform()
            # sleep(3)

            ### 二쇰Ц/諛곗넚 議고쉶 ?붾㈃ ###
            sleep(5)
            self.interact_by_xpath('//android.widget.Button[@text="二쇰Ц痍⑥냼"]', search_sec=10)  # 二쇰Ц?댁뿭 > 泥?踰덉㎏ 二쇰Ц 嫄?二쇰Ц痍⑥냼 踰꾪듉 ?대┃

            ### 二쇰Ц 痍⑥냼 ?붾㈃ ###
            self.interact_by_xpath('//android.widget.CheckBox')  # ?꾩껜?좏깮 泥댄겕 諛뺤뒪 ?좏깮
            self.interact_by_xpath('//*[@text="怨꾩냽吏꾪뻾?섍린"]')  # 怨꾩냽吏꾪뻾?섍린 踰꾪듉 ?대┃
            self.interact_by_xpath('//*[@text="?좎껌?꾨즺?섍린"]')  # ?좎껌?꾨즺?섍린 踰꾪듉 ?대┃

            ### 二쇰Ц 痍⑥냼 ?꾨즺 ?붾㈃ ###
            self.interact_by_xpath('//*[@text="二쇰Ц痍⑥냼?꾨즺"]', click=False)  # 二쇰Ц 痍⑥냼 ?꾨즺 ??댄? ?뺤씤
            self.interact_by_xpath('//*[@text="痍⑥냼?꾨즺"]', click=False)  # 二쇰Ц ?곹깭 痍⑥냼 ?꾨즺 ?뺤씤
            self.interact_by_xpath('//android.widget.ListView[3]/..//*[contains(@text,"0??)]', click=False)  # 理쒖쥌 痍⑥냼 湲덉븸 ?몄텧 ?뺤씤
        except:
            self.assertEqual(0, 1)
    except:
        self.capture_screen_payment()
        self.assertEqual(1, 72)
    else:
        print(f"{sys._getframe(0).f_code.co_name} Passed")
        TCFG.is_passed = True
