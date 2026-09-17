    def test_024_BEST_留롮씠_援щℓ??self):
        try:
            ### ??###
            self.interact_by_xpath('//*[@text="BEST"]')  # BEST ???대┃

            ### BEST ??###
            ## 留롮씠 援щℓ????
            self.interact_by_id('com.amorepacific.amorepacificmall:id/best_tab', click=False)  # BEST ??궧 ???곸뿭 ?뺤씤
            self.interact_by_xpath('//*[@text="留롮씠 援щℓ??][@selected="true"]', click=False)  # 留롮씠 援щℓ?????쒖꽦???곹깭 ?뺤씤
            self.interact_by_xpath('//android.widget.TextView[@text="?쇨컙"]', click=False)  # ?쇨컙 ?좏깮 ?뺤씤
            self.interact_by_xpath('(//android.widget.LinearLayout/android.view.ViewGroup[2])[1]', click=False)  # 珥덇린??踰꾪듉 ?뺤씤
            self.interact_by_xpath('//android.widget.TextView[@text="移댄뀒怨좊━"]', click=False)  # 移댄뀒怨좊━ ?좏깮 ?뺤씤

            # 怨꾩젙蹂??뚯썝 ?뺣낫 湲곕컲?쇰줈 ?곕졊? ?먮룞 ?명똿 諛??쒖꽦???곹깭 ?뺤씤
            if TCFG.port == '2009':
                self.interact_by_xpath('//*[@text="20? ?댄븯"][@selected="true"]', click=False)  # 20? ?댄븯 ?뺤씤
            if TCFG.port == '2001':
                self.interact_by_xpath('//*[@text="30?"][@selected="true"]', click=False)  # 30? ?뺤씤
            if TCFG.port == '7778':
                self.interact_by_xpath('//*[@text="40?"][@selected="true"]', click=False)  # 40? ?뺤씤
            if TCFG.port == '2023':
                self.interact_by_xpath('//*[@text="40?"][@selected="true"]', click=False)  # 40? ?뺤씤

            self.interact_by_xpath('//android.widget.TextView[@text="釉뚮옖??]', click=False)  # 釉뚮옖???좏깮 ?뺤씤
        except:
            self.capture_screen()
            self.assertEqual(0, 19)
        else:
            print(f"{sys._getframe(0).f_code.co_name} Passed")
            TCFG.is_passed = True

    def test_025_BEST_留롮씠_?대┃??self):
        try:
            ### BEST ??###
            self.interact_by_xpath('//*[@resource-id="com.amorepacific.amorepacificmall:id/radio_image"]/..//*[@text="留롮씠 ?대┃??]')  # 留롮씠 ?대┃?????좏깮

            ## 留롮씠 ?대┃????
            self.interact_by_xpath('//*[@text="留롮씠 ?대┃??][@selected="true"]', click=False)  # 留롮씠 ?대┃?????쒖꽦???곹깭 ?뺤씤
            self.interact_by_xpath('//android.widget.TextView[@text="移댄뀒怨좊━"]')  # 移댄뀒怨좊━ ?좏깮

            ## 移댄뀒怨좊━ ?꾪꽣 ?곸꽭
            self.interact_by_xpath('//android.widget.LinearLayout[1]//*[@text="?대젋吏?]')  # ?대젋吏??좏깮
            self.interact_by_xpath('//*[@text="?대젋吏?][@selected="true"]', click=False)  # ?대젋吏?移댄뀒怨좊━ ?쒖꽦???곹깭 ?뺤씤
            self.interact_by_id('com.amorepacific.amorepacificmall:id/tv_confirm')  # ?곸슜?섍린 ?대┃

            ## 留롮씠 ?대┃????
            self.interact_by_xpath('(//android.widget.LinearLayout/android.view.ViewGroup[1])[2]', click=False)  # 珥덇린??踰꾪듉 ?좎? ?뺤씤
            self.interact_by_xpath('//android.view.ViewGroup[4]//android.widget.TextView[@text="釉뚮옖??]')  # 釉뚮옖???좏깮

            ## 釉뚮옖???꾪꽣 ?곸꽭
            # 留먯쨪??泥섎━ width ?ъ씠利?湲곗??쇰줈 泥섎━?섎?濡??뱀젙 ?⑤쭚 釉뚮옖??4媛쒓퉴吏 ?좏깮 ??留먯쨪??泥섎━ 寃利?吏꾪뻾
            if TCFG.dname == 'Galaxy S23':
                # 釉뚮옖?쒕챸 ?쒖꽌?濡?4媛????
                brand_1 = self.get_attri('(//*[@resource-id="com.amorepacific.amorepacificmall:id/tv_item"])[1]', 'text', By.XPATH)
                brand_2 = self.get_attri('(//*[@resource-id="com.amorepacific.amorepacificmall:id/tv_item"])[2]', 'text', By.XPATH)
                brand_3 = self.get_attri('(//*[@resource-id="com.amorepacific.amorepacificmall:id/tv_item"])[3]', 'text', By.XPATH)
                brand_4 = self.get_attri('(//*[@resource-id="com.amorepacific.amorepacificmall:id/tv_item"])[4]', 'text', By.XPATH)
                brand_total = [brand_1, brand_2, brand_3, brand_4]
                return_brand = ','.join(brand_total)
                self.interact_by_xpath('(//*[@resource-id="com.amorepacific.amorepacificmall:id/tv_item"])[4]')  # ??踰덉㎏ 釉뚮옖???좏깮
            else:
                # 釉뚮옖?쒕챸 ?쒖꽌?濡?3媛????
                brand_1 = self.get_attri('(//*[@resource-id="com.amorepacific.amorepacificmall:id/tv_item"])[1]', 'text', By.XPATH)
                brand_2 = self.get_attri('(//*[@resource-id="com.amorepacific.amorepacificmall:id/tv_item"])[2]', 'text', By.XPATH)
                brand_3 = self.get_attri('(//*[@resource-id="com.amorepacific.amorepacificmall:id/tv_item"])[3]', 'text', By.XPATH)
                brand_total = [brand_1, brand_2, brand_3]
                return_brand = ','.join(brand_total)

            self.interact_by_xpath('(//*[@resource-id="com.amorepacific.amorepacificmall:id/tv_item"])[1]')  # 泥?踰덉㎏ 釉뚮옖???좏깮
            self.interact_by_xpath('(//*[@resource-id="com.amorepacific.amorepacificmall:id/tv_item"])[2]')  # ??踰덉㎏ 釉뚮옖???좏깮
            self.interact_by_xpath('(//*[@resource-id="com.amorepacific.amorepacificmall:id/tv_item"])[3]')  # ??踰덉㎏ 釉뚮옖???좏깮
            self.interact_by_id('com.amorepacific.amorepacificmall:id/tv_confirm')  # ?곸슜?섍린 ?대┃

            # # ?꾪꽣 ?ㅼ젙 ???좏깮??釉뚮옖?쒕챸 ?꾩뼱?곌린 ?ы븿 理쒕? 10湲?먭퉴吏 ?몄텧 ??留먯쨪??泥섎━
            # return_abb = return_brand[0:10] + '...'
            # return_brand, return_abb = return_abb, return_brand

            ## 留롮씠 ?대┃????
            self.interact_by_xpath('//android.widget.TextView[@text="?대젋吏?][@selected="true"]', click=False)  # 移댄뀒怨좊━ ?대젋吏??좏깮 ?뺤씤

            # 怨꾩젙蹂??뚯썝 ?뺣낫 湲곕컲?쇰줈 ?곕졊? ?먮룞 ?명똿 諛??쒖꽦???곹깭 ?뺤씤
            if TCFG.port == '2009':
                self.interact_by_xpath('//*[@text="20? ?댄븯"][@selected="true"]', click=False)  # 20? ?댄븯 ?뺤씤
            if TCFG.port == '2001':
                self.interact_by_xpath('//*[@text="30?"][@selected="true"]', click=False)  # 30? ?뺤씤
            if TCFG.port == '7778':
                self.interact_by_xpath('//*[@text="40?"][@selected="true"]', click=False)  # 40? ?뺤씤
            if TCFG.port == '2023':
                self.interact_by_xpath('//*[@text="40?"][@selected="true"]', click=False)  # 40? ?뺤씤

            self.interact_by_xpath('//*[@text="{}"][@selected="true"]'.format(return_brand), click=False)  # 釉뚮옖??> 釉뚮옖?쒕챸1,釉뚮옖?쒕챸2,釉뚮옖?쒕챸3... ?좏깮 ?뺤씤

            try:
                self.interact_by_xpath('//android.widget.TextView[@text="{}"]'.format(datetime.now().strftime('%m.%d %H:%M 湲곗?')), click=False)  # ?꾩옱 ?좎쭨 ?쒓컙 湲곗? ?몄텧 ?뺤씤
            except:
                after_one_minute = datetime.now() - relativedelta(minutes=1)  # ?꾩옱 ?쒓컙 湲곗? 1遺???援ы븯湲?
                self.interact_by_xpath('//android.widget.TextView[@text="{}"]'.format(after_one_minute.strftime('%m.%d %H:%M 湲곗?')), click=False)  # ?꾩옱 ?좎쭨 ?쒓컙 湲곗? ?몄텧 ?뺤씤

            self.interact_by_xpath('(//*[@resource-id="com.amorepacific.amorepacificmall:id/product_img"])[1]', click=False)  # 泥?踰덉㎏ ?곹뭹 ?대?吏 ?뺤씤
            self.interact_by_xpath('(//android.widget.LinearLayout/android.view.ViewGroup[1])[2]')  # 珥덇린???좏깮
            sleep(1)

            # 3媛??꾪꽣 ?ㅼ젙 珥덇린???곹깭 ?뺤씤
            self.interact_by_xpath('//android.widget.TextView[@text="移댄뀒怨좊━"][@selected="false"]', click=False)  # 移댄뀒怨좊━ 珥덇린???곹깭 ?뺤씤
            self.interact_by_xpath('//android.widget.TextView[@text="?곕졊?"][@selected="false"]', click=False)  # ?곕졊? 珥덇린???곹깭 ?뺤씤
            self.interact_by_xpath('//android.widget.TextView[@text="釉뚮옖??][@selected="false"]', click=False)  # 釉뚮옖??珥덇린???곹깭 ?뺤씤
            self.interact_by_xpath('(//*[@resource-id="com.amorepacific.amorepacificmall:id/product_img"])[1]', click=False)  # 泥?踰덉㎏ ?곹뭹 ?대?吏 ?뺤씤 (APM-45780)
        except:
            self.capture_screen()
            self.assertEqual(0, 21)
        else:
            print(f"{sys._getframe(0).f_code.co_name} Passed")
            TCFG.is_passed = True

    def test_026_BEST_留롮씠_寃?됲븳(self):
        try:
            ### BEST ??###
            ## 留롮씠 ?대┃????
            self.interact_by_xpath('//*[@resource-id="com.amorepacific.amorepacificmall:id/radio_image"]/..//*[@text="留롮씠 寃?됲븳"]')  # 留롮씠 寃?됲븳 ???좏깮

            ## 留롮씠 寃?됲븳 ??> ?멸린 ?ㅼ썙????
            try:
                self.interact_by_xpath('//android.widget.TextView[@text="{}"]'.format(datetime.now().strftime('%m.%d %H:%M 湲곗?')), click=False)  # ?꾩옱 ?좎쭨 ?쒓컙 湲곗? ?몄텧 ?뺤씤
            except:
                after_one_minute = datetime.now() - relativedelta(minutes=1)  # ?꾩옱 ?쒓컙 湲곗? 1遺???援ы븯湲?
                self.interact_by_xpath('//android.widget.TextView[@text="{}"]'.format(after_one_minute.strftime('%m.%d %H:%M 湲곗?')), click=False)  # ?꾩옱 ?좎쭨 ?쒓컙 湲곗? ?몄텧 ?뺤씤
            self.interact_by_xpath('(//*[@resource-id="com.amorepacific.amorepacificmall:id/best_brand_ranking"])[1]/..//*[@text="1"]', click=False)  # ??궧 1 ?몄텧 ?뺤씤
            self.interact_by_xpath('(//*[@resource-id="com.amorepacific.amorepacificmall:id/best_brand_ranking"])[2]/..//*[@text="2"]', click=False)  # ??궧 2 ?몄텧 ?뺤씤
            self.interact_by_xpath('(//*[@resource-id="com.amorepacific.amorepacificmall:id/product"])[1]', click=False)  # ??궧 1 泥?踰덉㎏ ?곹뭹 ?몄텧 ?뺤씤
            self.interact_by_xpath('//*[@text="?멸린 釉뚮옖??]')  # ?멸린 釉뚮옖?????좏깮

            ## 留롮씠 寃?됲븳 ??> ?멸린 釉뚮옖????
            self.interact_by_xpath('(//*[@resource-id="com.amorepacific.amorepacificmall:id/best_brand_ranking"])[1]/..//*[@text="1"]', click=False)  # ??궧 1 ?몄텧 ?뺤씤
            self.interact_by_xpath('(//*[@resource-id="com.amorepacific.amorepacificmall:id/best_brand_ranking"])[2]/..//*[@text="2"]', click=False)  # ??궧 2 ?몄텧 ?뺤씤
            self.interact_by_xpath('(//*[@resource-id="com.amorepacific.amorepacificmall:id/best_brand_logo"])[1]', click=False)  # ??궧 1 釉뚮옖??濡쒓퀬 ?대?吏 ?뺤씤
            self.interact_by_xpath('(//*[@resource-id="com.amorepacific.amorepacificmall:id/best_brand_logo"])[2]', click=False)  # ??궧 2 釉뚮옖??濡쒓퀬 ?대?吏 ?뺤씤
            self.interact_by_xpath('(//*[@resource-id="com.amorepacific.amorepacificmall:id/iv_like"])[1]', click=False)  # ??궧 1 醫뗭븘???꾩씠肄??몄텧 ?뺤씤
        except:
            self.capture_screen()
            self.assertEqual(0, 21)
        else:
            print(f"{sys._getframe(0).f_code.co_name} Passed")
            TCFG.is_passed = True

    def test_027_BEST_?쇰???留욌뒗(self):
        try:
            ### BEST ??###
            ## 留롮씠 寃?됲븳 ??
            self.interact_by_xpath('//*[@resource-id="com.amorepacific.amorepacificmall:id/radio_image"]/..//*[@text="?쇰???留욌뒗"]')  # ?쇰???留욌뒗 ???좏깮
            # ?뚯썝, ?쇰? 怨좊? ?ㅼ젙 = Y

            ## ?쇰???留욌뒗 ??
            self.interact_by_xpath('(//*[@resource-id="com.amorepacific.amorepacificmall:id/ranking_tag"])[1]/..//*[@text="1"]', click=False)  # 泥?踰덉㎏ ?곹뭹 踰덊샇 1 ?띿뒪???뺤씤
            self.interact_by_xpath('(//*[@resource-id="com.amorepacific.amorepacificmall:id/ranking_tag"])[2]/..//*[@text="2"]', click=False)  # ??踰덉㎏ ?곹뭹 踰덊샇 2 ?띿뒪???뺤씤
        except:
            self.capture_screen()
            self.assertEqual(0, 21)
        else:
            print(f"{sys._getframe(0).f_code.co_name} Passed")
            TCFG.is_passed = True

    def test_028_BEST_醫뗭븘???뺤씤(self):
        try:
            ### BEST ??###
            ## ?쇰???留욌뒗 ??
            best_prd = self.get_attri('(//*[@resource-id="com.amorepacific.amorepacificmall:id/tv_product_name"])[1]', 'text', By.XPATH)  # BEST 泥?踰덉㎏ ?곹뭹 > ?대쫫 ???
            self.interact_by_xpath('(//android.view.View[@resource-id="com.amorepacific.amorepacificmall:id/view_overlay"])[1]')  # 泥ル쾲吏??곹뭹 ?대┃
            sleep(3)

            ### BEST ?곹뭹 ?곸꽭 ###
            self.interact_by_xpath('//*[@text="醫뗭븘??]')  # 醫뗭븘??踰꾪듉 ?대┃
            TCFG.driver.back()  # BEST ?곹뭹 ?곸꽭 > BEST ??쑝濡??대룞

            ### BEST ??###
            self.interact_by_id('com.amorepacific.amorepacificmall:id/iv_bottom_history_icon')  # ?섎떒 ?≪뀡諛??덉뒪?좊━ ?대┃

            ### ?쇳븨 ?덉뒪?좊━ ?붾㈃ ###
            TCFG.driver.swipe(TCFG.res[0] * 0.5, TCFG.res[1] * 0.5, TCFG.res[0] * 0.5, TCFG.res[1] * 0.2)  # 諛묒쑝濡?議곌툑 ?대룞
            sleep(1.5)

            # ?쇳븨 ?덉뒪?좊━ > BEST 泥?踰덉㎏ ?곹뭹 議댁옱 ?щ? ?뺤씤
            self.interact_by_xpath('//android.widget.TextView[contains(@text, "{}")]'.format(best_prd), click=False)
        except:
            self.capture_screen()
            self.assertEqual(0, 22)
        else:
            print(f"{sys._getframe(0).f_code.co_name} Passed")
            TCFG.is_passed = True

    def test_029_BEST_醫뗭븘??痍⑥냼(self):
        try:
            ### ?쇳븨 ?덉뒪?좊━ ?붾㈃ ###
            like_count = self.get_attri('com.amorepacific.amorepacificmall:id/total_count_text', 'text', By.ID).split('媛?)  # 'n媛쒖쓽 醫뗭븘???곹뭹???덉뒿?덈떎.' n ???
            self.interact_by_xpath('(//*[@resource-id="com.amorepacific.amorepacificmall:id/iv_like"])[1]')  # 泥?踰덉㎏ ?곹뭹 醫뗭븘??痍⑥냼
            
            # 湲곗〈 醫뗭븘???곹뭹 2媛??댁긽??寃쎌슦
            try:
                self.interact_by_xpath('//android.widget.TextView[@text="{}媛쒖쓽 醫뗭븘???곹뭹???덉뒿?덈떎."]'.format(int(like_count[0])-1), click=False)  # 醫뗭븘???곹뭹 媛?닔 -1 ?뺤씤
            # 湲곗〈 醫뗭븘???곹뭹 1媛쒖씤 寃쎌슦
            except:
                self.interact_by_xpath('//android.widget.TextView[@text="?꾩쭅 醫뗭븘?????곹뭹???놁뒿?덈떎."]', click=False)  # 醫뗭븘?뷀븳 ?곹뭹???놁쓬???덈궡?섎뒗 臾멸뎄 ?몄텧 ?뺤씤
        except:
            self.capture_screen()
            self.assertEqual(0, 23)
        else:
            print(f"{sys._getframe(0).f_code.co_name} Passed")
            TCFG.is_passed = True
        finally:
            self.interact_by_id('com.amorepacific.amorepacificmall:id/ib_bottom_home')  # ?섎떒 ?≪뀞諛???踰꾪듉 ?대┃

    def test_030_BEST_怨듭쑀?섍린(self):
        try:
            ### ??###
            self.interact_by_xpath('//*[@text="BEST"]')  # BEST ???대┃

            ### BEST ??###
            ## 留롮씠 援щℓ????
            self.interact_by_xpath('(//android.view.View[@resource-id="com.amorepacific.amorepacificmall:id/view_overlay"])[2]')  # ??踰덉㎏ ?곹뭹 ?대┃

            ### ?곹뭹 ?곸꽭 ?붾㈃ ###
            prod_name = self.get_attri('(//android.view.View)[1]', 'text', By.XPATH)
            print(prod_name)
            self.interact_by_xpath('//android.view.View[1]/android.widget.Button')  # 怨듭쑀?섍린 踰꾪듉 ?대┃
            sleep(1.5)

            ### 怨듭쑀?섍린 ?덉씠???앹뾽 ###
            self.interact_by_xpath('//android.widget.TextView[contains(@text, "{}")]'.format(prod_name), click=False)  # ?곹뭹紐??쇱튂 ?뺤씤
            TouchAction(TCFG.driver).tap(None, 550, 124, 1).perform()  # ?곗튂濡?怨듭쑀李??リ린
        except:
            self.capture_screen()
            self.assertEqual(0, 24)
        else:
            print(f"{sys._getframe(0).f_code.co_name} Passed")
            TCFG.is_passed = True
        finally:
            TCFG.driver.back()  # BEST ??쑝濡??대룞
