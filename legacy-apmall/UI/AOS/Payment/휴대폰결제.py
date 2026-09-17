def test_090_?대??곌껐??self):
    try:
        # ??醫낅즺 ???ъ떎??
        TCFG.driver.close_app()
        sleep(2)
        TCFG.driver.launch_app()
        sleep(2)

        # ?ㅽ겕由곗꺑 ???????λ맂 ?대?吏? 留ㅼ묶
        matching = Matching()
        screenshots_path = os.path.join(f"{TCFG.brand_path}", "Screenshots")
        general_payment = os.path.join(f"{TCFG.ap_path}", "Purchase", "Android", "public", "amoremall_general_payment.png")
        phone_payment = os.path.join(f"{TCFG.ap_path}", "Purchase", "Android", "capture_phonepayment", "amoremall_phone_payment.png")

        self.interact_by_id('com.amorepacific.amorepacificmall:id/ib_bottom_my')  # 留덉씠 ?뚯슦移??대┃
        sleep(3)

        ### 留덉씠?뚯슦移??붾㈃ > ?곹뭹 寃??###
        self.interact_by_id('com.amorepacific.amorepacificmall:id/header_search_button_image_view')  # 寃???꾩씠肄??대┃
        self.interact_by_id('com.amorepacific.amorepacificmall:id/search_edit_text')  # 寃???꾨뱶 ?대┃

        if TCFG.environment == 'PRD':
            self.interact_by_id('com.amorepacific.amorepacificmall:id/search_edit_text', send_keys_msg='移レ넄')  # ?띿뒪???낅젰
        if TCFG.environment == 'STG':
            self.interact_by_id('com.amorepacific.amorepacificmall:id/search_edit_text', send_keys_msg='??됱＜臾몄슜 ?⑤씪??')  # ?띿뒪???낅젰

        self.interact_by_id('com.amorepacific.amorepacificmall:id/search_button')  # 寃??踰꾪듉 ?대┃

        ### 寃??寃곌낵 ?붾㈃ ###
        self.interact_by_id('iv_prd_img')  # 泥?踰덉㎏ ?쒗뭹 ?대?吏 ?대┃

        ### ?곹뭹 ?곸꽭 ?붾㈃ ###
        self.interact_by_xpath('//*[@text="援щℓ?섍린"]')  # 援щℓ?섍린 踰꾪듉 ?대┃
        sleep(3)

        # ?듭뀡 ?곹뭹??寃쎌슦 泥?踰덉㎏ ?곹뭹 ?좏깮
        try:
            self.interact_by_xpath('//android.widget.Button[@text="?곹뭹???좏깮?댁＜?몄슂"]')
            self.interact_by_xpath('(//*[contains(@text,"0??)])[1]')
        except:
            pass

        self.interact_by_xpath('//*[@text="援щℓ?섍린"]')  # 援щℓ?섍린 踰꾪듉 ?대┃
        sleep(5)

        ### 二쇰Ц???붾㈃ ###
        TCFG.driver.press_keycode(123)  # 理쒗븯?⑥쑝濡??대룞
        sleep(3)

        # 援щℓ議곌굔 諛?寃곗젣 吏꾪뻾 ?숈쓽 泥댄겕諛뺤뒪 ?좏깮
        if TCFG.port == '2009' or TCFG.port == '2023':
            TouchAction(TCFG.driver).tap(None, 78, 1430, 1).perform()
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
        sleep(5)

        if TCFG.port == '2009' or TCFG.port == '2023':
            # 諛묒쑝濡?議곌툑 ?대룞
            TCFG.driver.swipe(TCFG.res[0] * 0.5, TCFG.res[1] * 0.5, TCFG.res[0] * 0.5, TCFG.res[1] * 0.2)

        # ?쇰컲 寃곗젣 > ?대???寃곗젣 ?좏깮
        TCFG.driver.save_screenshot(f'{screenshots_path}/amoremall_phone_payment.png')
        center = matching.detectimage(f'{screenshots_path}/amoremall_phone_payment.png', phone_payment)  # center: (193, 777)
        TouchAction(TCFG.driver).tap(None, center[0]+37, center[1]+233, 1).perform()
        sleep(2)

        # 寃곗젣?섍린 踰꾪듉 ?대┃
        TouchAction(TCFG.driver).tap(None, 530, 2000, 1).perform()
        if TCFG.environment == 'STG':
            sleep(1.5)
            TouchAction(TCFG.driver).tap(None, 329, 1289, 1).perform()  # ?ㅽ럹???꾨줈紐⑥뀡 ?쒖쇅?섍퀬 援щℓ ?좏깮
        sleep(5)

        ### KG ?대땲?쒖뒪 ?붾㈃ ###
        # ?대???踰덊샇 ?뺤씤 ?붾㈃???몄텧 ?섎뒗 寃쎌슦
        try:
            self.interact_by_xpath('//*[@text="?ㅼ쓬"]')  # ?ㅼ쓬 踰꾪듉 ?대┃
        except:
            pass

        for i in TCFG.phonepassword:
            self.interact_by_ac(f"{i}")
        sleep(3)

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
        self.assertEqual(1, 75)
    else:
        print(f"{sys._getframe(0).f_code.co_name} Passed")
        TCFG.is_passed = True
