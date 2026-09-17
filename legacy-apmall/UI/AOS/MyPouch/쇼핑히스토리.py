    def test_021_?쇳븨_?덉뒪?좊━_理쒓렐(self):
        try:
            self.interact_by_id('com.amorepacific.amorepacificmall:id/iv_bottom_history_icon')  # ?덉뒪?좊━濡??대룞

            ### ?쇳븨 ?덉뒪?좊━ ?붾㈃ ###
            self.interact_by_xpath('//android.widget.TextView[@text="理쒓렐 蹂??곹뭹"]', click=False)  # 理쒓렐 蹂??곹뭹 ?띿뒪???뺤씤
            self.interact_by_id('com.amorepacific.amorepacificmall:id/title_arrow')  # ?쇱튂湲??대┃

            # 理쒓렐 蹂??곹뭹 ?덈뒗 寃쎌슦 > 泥?踰덉㎏ 湲곕줉 ???寃利?            try:
                # 釉뚮옖?쒖씪 寃쎌슦
                if self.is_element_present('//androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[1]'
                                           '//*[@resource-id="com.amorepacific.amorepacificmall:id/contents_tag"][@text="釉뚮옖??]', By.XPATH):
                    self.interact_by_xpath('(//*[@resource-id="com.amorepacific.amorepacificmall:id/item_image"])[1]', click=False)  # 釉뚮옖???대?吏 ?뺤씤
                    self.interact_by_xpath('(//*[@resource-id="com.amorepacific.amorepacificmall:id/contents_tag"][@text="釉뚮옖??])[1]')  # 泥?踰덉㎏ 釉뚮옖???대┃
                    sleep(2)

                    ### 釉뚮옖??硫붿씤 ###
                    self.interact_by_xpath('//android.webkit.WebView[contains(@text,"釉뚮옖?쒓?")]', click=False)  # 釉뚰빖?쒓? 吏꾩엯 ?뺤씤
                    TCFG.driver.back()  # ?ㅻ줈 媛湲?> 理쒓렐 蹂??곹뭹?쇰줈 ?대룞

                # 寃?됱뼱??寃쎌슦
                elif self.is_element_present('//androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[1]'
                                           '//*[@resource-id="com.amorepacific.amorepacificmall:id/search_keyword"]', By.XPATH):
                    keyword = TCFG.driver.find_element_by_xpath('(//*[@resource-id="com.amorepacific.amorepacificmall:id/search_keyword"])[1]').text  # 寃?됱뼱 ???                    self.interact_by_xpath('(//*[@resource-id="com.amorepacific.amorepacificmall:id/search_keyword"])[1]')  # 寃?됱뼱 ?대┃

                    ### 寃??寃곌낵 ?붾㈃ ###
                    self.interact_by_xpath('//*[@resource-id="com.amorepacific.amorepacificmall:id/tv_search_header_search_bar"][@text="{}"]'.format(keyword), click=False)  # ?ㅻ뜑 寃?됰컮 ?ㅼ썙???쇱튂 ?뺤씤
                    self.interact_by_xpath('(//*[@resource-id="com.amorepacific.amorepacificmall:id/iv_prd_img"])[1]', click=False)  # 泥?踰덉㎏ ?곹뭹 ?대?吏 ?몄텧 ?뺤씤
                    self.interact_by_id('com.amorepacific.amorepacificmall:id/btn_back')  # ?ㅻ뜑 ?ㅻ줈 媛湲?踰꾪듉 ?대┃

                # ?곹뭹??寃쎌슦
                elif self.is_element_present('//androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[1]'
                                           '//*[@resource-id="com.amorepacific.amorepacificmall:id/contents_sub_title"][contains(@text,"00??)]', By.XPATH):  # ?곹뭹??寃쎌슦
                    self.interact_by_xpath('(//*[@resource-id="com.amorepacific.amorepacificmall:id/item_image"])[1]', click=False)  # 泥?踰덉㎏ ?곹뭹 ?대?吏 ?몄텧 ?뺤씤
                    self.interact_by_xpath('(//*[@resource-id="com.amorepacific.amorepacificmall:id/cart_icon"])[1]', click=False)  # ?λ컮援щ땲 ?뺤씤
                    self.interact_by_xpath('(//*[@resource-id="com.amorepacific.amorepacificmall:id/item_layout"])[1]')  # 泥?踰덉㎏ ?곹뭹 ?대┃

                    ### ?곹뭹 ?곸꽭 ?붾㈃ ###
                    self.interact_by_xpath('//android.widget.Button[@text="援щℓ?섍린"]', click=False)  # ?λ컮援щ땲 踰꾪듉 ?뺤씤
                    self.interact_by_xpath('//android.widget.Button[@text="?ㅻ줈媛湲?]')  # ?ㅻ뜑 ?ㅻ줈 媛湲?踰꾪듉 ?대┃

                ### 理쒓렐 蹂??곹뭹 ?붾㈃ ###
                self.interact_by_id('com.amorepacific.amorepacificmall:id/tv_edit')  # ?몄쭛 ?대┃

                # ?몄쭛 湲곕뒫 寃利?                delete_before = TCFG.driver.find_element_by_xpath('//androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[1]')  # 泥?踰덉㎏ ?덉뒪?좊━ text ???                self.interact_by_xpath('(//*[@resource-id="com.amorepacific.amorepacificmall:id/delete_button"])[1]')  # 泥?踰덉㎏ ?덉뒪?좊━ ?댁뿭 媛쒕퀎 ??젣
                delete_after = TCFG.driver.find_element_by_xpath('//androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[1]')  # 泥?踰덉㎏ ?덉뒪?좊━ text ???
                # 泥?踰덉㎏ ?덉뒪?좊━ ?댁뿭 ??젣 ?꾪썑 鍮꾧탳 寃利?                if delete_before is not delete_after:
                    pass
                else:
                    raise AssertionError("泥?踰덉㎏ ?덉뒪?좊━ ?댁뿭 ??젣 ?꾪썑 鍮꾧탳 寃利?fail 諛쒖깮")

                self.interact_by_id('com.amorepacific.amorepacificmall:id/tv_del_all')  # ?꾩껜 ??젣 踰꾪듉 ?대┃
                self.interact_by_id('com.amorepacific.amorepacificmall:id/bt_right')  # 理쒓렐 蹂??댁뿭??紐⑤몢 ??젣?섏떆寃좎뒿?덇퉴? ?앹뾽 ??젣 踰꾪듉 ?대┃
                self.interact_by_id('com.amorepacific.amorepacificmall:id/history_shopping_empty_text', click=False)  # '理쒓렐 蹂??댁뿭???놁뒿?덈떎' 臾멸뎄 ?몄텧 ?뺤씤
                self.interact_by_id('com.amorepacific.amorepacificmall:id/floating_btn')  # ?쇳븨 ?덉뒪?좊━ ?リ린
            # 理쒓렐 蹂??곹뭹???녿뒗 寃쎌슦
            except:
                self.interact_by_id('com.amorepacific.amorepacificmall:id/history_shopping_empty_text', click=False)  # '理쒓렐 蹂??댁뿭???놁뒿?덈떎' 臾멸뎄 ?몄텧 ?뺤씤
        except:
            self.capture_screen()
            self.assertEqual(0, 18)
        else:
            print(f"{sys._getframe(0).f_code.co_name} Passed")
            TCFG.is_passed = True
        finally:
            self.interact_by_id('com.amorepacific.amorepacificmall:id/ib_bottom_history')  # 理쒓렐 ?덉뒪?좊━媛 ?녿뒗 ?곹깭 > ?섎떒 ?≪뀡諛??쇳븨 ?덉뒪?좊━ ?ъ쭊??
    def test_022_?쇳븨_?덉뒪?좊━_醫뗭븘??self):
        try:
            ### ?쇳븨 ?덉뒪?좊━ ?붾㈃ ###
            if TCFG.environment == 'PRD':
                self.interact_by_xpath('//*[@resource-id="com.amorepacific.amorepacificmall:id/title_text"][@text="{}?섏쓽 ?ο툗LIKE"]'.format(TCFG.name), click=False)  # 醫뗭븘???곸뿭 ??댄? ?몄텧 ?뺤씤
            if TCFG.environment == 'STG':
                self.interact_by_xpath('//*[@resource-id="com.amorepacific.amorepacificmall:id/title_text"][contains(@text,"?섏쓽 ?ο툗LIKE")]', click=False)  # 醫뗭븘???곸뿭 ??댄? ?몄텧 ?뺤씤

            self.interact_by_xpath('//android.widget.LinearLayout[@content-desc="醫뗭븘??]/android.widget.TextView[@selected="true"]', click=False)  # 醫뗭븘?????뷀뤃???쒖꽦???뺤씤

            # 諛묒쑝濡?議곌툑 ?대룞
            TCFG.driver.swipe(TCFG.res[0] * 0.5, TCFG.res[1] * 0.5, TCFG.res[0] * 0.5, TCFG.res[1] * 0.2)

            # 濡쒓렇???곹깭 > 醫뗭븘???곹뭹 ?덈뒗 寃쎌슦
            try:
                self.interact_by_xpath('//*[@resource-id="com.amorepacific.amorepacificmall:id/total_count_text"][contains(@text,"媛쒖쓽 醫뗭븘???곹뭹???덉뒿?덈떎.")]', click=False)  # 醫뗭븘???곹뭹 媛쒖닔 ?쒓린 ?곸뿭 ?뺤씤
                # self.interact_by_id('com.amorepacific.amorepacificmall:id/order_button', click=False)  # 醫뗭븘???곹뭹 ?뺣젹 ?뺤씤
                self.interact_by_xpath('(//*[@resource-id="com.amorepacific.amorepacificmall:id/product_img"])[1]', click=False)  # 泥?踰덉㎏ ?곹뭹 ?대?吏 ?뺤씤
                self.interact_by_xpath('(//*[@resource-id="com.amorepacific.amorepacificmall:id/iv_like"][@index="2"])', click=False)  # 醫뗭븘???꾩씠肄?on ?곹깭 ?뺤씤

                # 湲곗〈 ?λ컮援щ땲 ?곹뭹 1媛??댁긽??寃쎌슦
                if self.is_element_present('com.amorepacific.amorepacificmall:id/cart_badge_icon', By.ID):
                    cart_badge_icon = TCFG.driver.find_element_by_id('com.amorepacific.amorepacificmall:id/cart_badge_icon').text  # ?꾩옱 ?λ컮援щ땲 ?곹뭹 媛쒖닔 ???                # 湲곗〈 ?λ컮援щ땲 ?곹뭹 ?녿뒗 寃쎌슦
                else:
                    cart_badge_icon = 0

                scroll_xpath(self, '(//android.widget.TextView[@text="?λ컮援щ땲 ?닿린"])[1]', loc=TCFG.res[1] * 0.9, y1=TCFG.res[1] * 0.7, y2=TCFG.res[1] * 0.5)  # 泥?踰덉㎏ ?곹뭹 ?λ컮援щ땲 ?닿린 踰꾪듉 ?대┃
                sleep(2)

                # ?섎굹???⑥쐞 ?곹뭹??寃쎌슦
                if self.is_element_present('(//android.widget.TextView[@text="?λ컮援щ땲 ?닿린"])[1]', By.XPATH):  # ?붾㈃ ?대룞 ?섏? ?딆쓬 ?뺤씤
                    try:
                        self.interact_by_xpath('//*[@resource-id="com.amorepacific.amorepacificmall:id/cart_badge_icon"][@text="{}"]'.format(int(cart_badge_icon)+1), click=False)  # ?λ컮援щ땲 ?섎웾 利앷? ?뺤씤

                    # 湲곗〈 ?λ컮援щ땲 ?곹뭹怨?以묐났??寃쎌슦 > ?λ컮援щ땲 ?섎웾 ?띿뒪??利앷??섏? ?딆쓬
                    except:
                        prodname = TCFG.driver.find_element_by_xpath('(//*[@resource-id="com.amorepacific.amorepacificmall:id/tv_product_name"])[1]').text
                        prodname_1 = prodname.split()

                        # ?곹뭹紐??ㅼ뿉 ?먮쭏???먮Ⅴ湲?(媛꾪뿉?곸쑝濡??곸씠???⑥뼱 諛쒖깮?쇰줈 ?쇰? ?⑥뼱留?寃利?
                        for replace_text in prodname_1:
                            if int(replace_text in prodname) and len(prodname.partition(replace_text)[0]) > \
                                    len(prodname.partition(replace_text)[2]):
                                prodname = prodname.partition(replace_text)[0]
                                prodname = prodname.strip()
                        print(prodname)

                        self.interact_by_id('com.amorepacific.amorepacificmall:id/header_cart_button_image_view')  # ?ㅻ뜑 ?곸뿭 ?λ컮援щ땲 吏꾩엯
                        sleep(2)

                        ### ?λ컮援щ땲 ?붾㈃ ###
                        self.interact_by_xpath('//android.view.View[contains(@content-desc,"{}")]'.format(prodname), click=False)  # 泥?踰덉㎏ 醫뗭븘???곹뭹怨??쇱튂 ?뺤씤

                        # ?대떦 ?곹뭹 ?λ컮援щ땲 ?섎웾 2媛??댁긽 ?뺤씤
                        cart_prodcount = TCFG.driver.find_element_by_xpath('//android.view.View[contains(@content-desc,"{}")]'
                                                                           '/android.view.View[2]/android.widget.TextView[3]'.format(prodname)).text

                        if int(cart_prodcount) >= 2:
                            pass
                        else:
                            AssertionError('湲곗〈 ?λ컮援щ땲 醫뗭븘???곹뭹 ?덈뒗 ?곹깭 > ?λ컮援щ땲 ?닿린 ?숈옉 fail 諛쒖깮')

                        self.interact_by_xpath('//android.widget.Button[@text="?リ린"]')  # ?λ컮援щ땲 [X]踰꾪듉 ?대┃
                # 蹂듭닔 媛쒖쓽 ?⑥쐞 ?곹뭹??寃쎌슦
                elif self.is_element_present('//android.widget.Button[@text="?곹뭹???좏깮?댁＜?몄슂"]', By.XPATH):  # ?곹뭹 ?곸꽭濡??대룞 諛??듭뀡 ?좏깮 ?덉씠???뷀뤃???ㅽ뵂 ?곹깭 ?뺤씤
                    TCFG.driver.back()   # ?쇳븨?덉뒪?좊━ 醫뗭븘???곸뿭?쇰줈 ?대룞
                # ?λ컮援щ땲 ?닿린媛 遺덇????곹깭
                elif self.is_element_present('//android.widget.Button[@text="?ъ엯怨??뚮┝ ?좎껌"]', By.XPATH):  # ?곹뭹 ?곸꽭濡??대룞 諛??ъ엯怨??뚮┝ ?좎껌 ?곹깭 ?뺤씤
                    TCFG.driver.back()   # ?쇳븨?덉뒪?좊━ 醫뗭븘???곸뿭?쇰줈 ?대룞
            # 濡쒓렇???곹깭 > 醫뗭븘???곹뭹 ?녿뒗 寃쎌슦
            except:
                self.interact_by_xpath('//android.widget.TextView[@text="?꾩쭅 醫뗭븘?????곹뭹???놁뒿?덈떎."]', click=False)  # 醫뗭븘?뷀븳 ?곹뭹???놁쓬???덈궡?섎뒗 臾멸뎄 ?몄텧 ?뺤씤
                self.interact_by_xpath('//android.widget.TextView[@text="吏湲?留롮씠 李얜뒗 ?곹뭹 蹂대윭媛湲?]')  # 異붿쿇 踰꾪듉 ?대┃

                ### BEST ??###
                self.interact_by_xpath('//android.widget.TextView[@text="留롮씠 ?대┃??]', click=False)  # BEST ??移댄뀒怨좊━ ?뺤씤
                self.interact_by_id('com.amorepacific.amorepacificmall:id/iv_bottom_history')  # ?섎떒 ?≪뀡諛?> ?쇳븨 ?덉뒪?좊━ 吏꾩엯

            self.interact_by_xpath('//android.widget.LinearLayout[@content-desc="?먯＜援щℓ"]')  # ?먯＜ 援щℓ ???대┃

            ## ?먯＜ 援щℓ ??##
            # ?먯＜ 援щℓ ?곹뭹???덈뒗 寃쎌슦
            try:
                self.interact_by_xpath('(//*[@resource-id="com.amorepacific.amorepacificmall:id/product_img"])[1]', click=False)  # 泥?踰덉㎏ ?곹뭹 ?대?吏 ?뺤씤

                ## ?먯＜ 援щℓ???곹뭹 1媛쒖씤 寃쎌슦
                if not self.is_element_present('(//*[@resource-id="com.amorepacific.amorepacificmall:id/product_img"])[2]', By.XPATH):
                    purchase_1 = TCFG.driver.find_element_by_xpath('(//android.widget.TextView[@resource-id="com.amorepacific.amorepacificmall:id/product_tag"])[1]').text.split("??)
                    prodname_1 = TCFG.driver.find_element_by_xpath('(//*[@resource-id="com.amorepacific.amorepacificmall:id/tv_product_name"])[1]').text
                    pshop = "[p]"

                    if int(purchase_1[0]) >= 2:  # 2???댁긽 援щℓ ?뺤씤
                        pass
                    else:
                        raise AssertionError("?먯＜ 援щℓ???곹뭹 援щℓ ?잛닔 fail 諛쒖깮")

                    if prodname_1 in pshop:  # ?곹뭹紐??쇱떆?쎌꺏([P]) 誘명룷???뺤씤
                        raise AssertionError("?먯＜ 援щℓ???곹뭹 p???ы븿?쇰줈 fail 諛쒖깮")
                ## ?먯＜ 援щℓ???곹뭹 2媛??댁긽??寃쎌슦
                else:
                    # ?먯＜ 援щℓ???곹뭹 援щℓ ?잛닔 ???2媛쒓퉴吏)
                    purchase_1 = TCFG.driver.find_element_by_xpath('(//android.widget.TextView[@resource-id="com.amorepacific.amorepacificmall:id/product_tag"])[1]').text.split("??)
                    purchase_2 = TCFG.driver.find_element_by_xpath('(//android.widget.TextView[@resource-id="com.amorepacific.amorepacificmall:id/product_tag"])[2]').text.split("??)
                    # ?먯＜ 援щℓ???곹뭹紐????2媛쒓퉴吏)
                    prodname_1 = TCFG.driver.find_element_by_xpath('(//*[@resource-id="com.amorepacific.amorepacificmall:id/tv_product_name"])[1]').text
                    prodname_2 = TCFG.driver.find_element_by_xpath('(//*[@resource-id="com.amorepacific.amorepacificmall:id/tv_product_name"])[2]').text
                    pshop = "[p]"

                    if int(purchase_1[0] and purchase_2[0]) >= 2:  # 2???댁긽 援щℓ ?뺤씤
                        int(purchase_1[0] >= purchase_2[0])  # 援щℓ ?잛닔 ?믪? ?쒖쑝濡??뺣젹 ?뺤씤
                        pass
                    else:
                        raise AssertionError("?먯＜ 援щℓ???곹뭹 援щℓ ?잛닔 fail 諛쒖깮")

                    if prodname_1 and prodname_2 in pshop:  # ?곹뭹紐??쇱떆?쎌꺏([P]) 誘명룷???뺤씤
                        raise AssertionError("?먯＜ 援щℓ???곹뭹 p???ы븿?쇰줈 fail 諛쒖깮")

                # 湲곗〈 ?λ컮援щ땲 ?곹뭹 1媛??댁긽??寃쎌슦
                if self.is_element_present('com.amorepacific.amorepacificmall:id/cart_badge_icon', By.ID):
                    cart_badge_icon = TCFG.driver.find_element_by_id('com.amorepacific.amorepacificmall:id/cart_badge_icon').text  # ?꾩옱 ?λ컮援щ땲 ?곹뭹 媛쒖닔 ???                # 湲곗〈 ?λ컮援щ땲 ?곹뭹 ?녿뒗 寃쎌슦
                else:
                    cart_badge_icon = 0

                scroll_xpath(self, '(//android.widget.TextView[@text="?λ컮援щ땲 ?닿린"])[1]', loc=TCFG.res[1] * 0.9, y1=TCFG.res[1] * 0.7, y2=TCFG.res[1] * 0.5)  # 泥?踰덉㎏ ?곹뭹 ?λ컮援щ땲 ?닿린 踰꾪듉 ?대┃

                # ?섎굹???⑥쐞 ?곹뭹??寃쎌슦
                if self.is_element_present('(//android.widget.TextView[@text="?λ컮援щ땲 ?닿린"])[1]', By.XPATH):  # ?붾㈃ ?대룞 ?섏? ?딆쓬 ?뺤씤
                    try:
                        self.interact_by_xpath('//*[@resource-id="com.amorepacific.amorepacificmall:id/cart_badge_icon"][@text="{}"]'.format(int(cart_badge_icon) + 1), click=False)  # ?λ컮援щ땲 ?섎웾 利앷? ?뺤씤
                    # 湲곗〈 ?λ컮援щ땲 ?곹뭹怨?以묐났??寃쎌슦 > ?λ컮援щ땲 ?섎웾 ?띿뒪??利앷??섏? ?딆쓬
                    except:
                        prodname = TCFG.driver.find_element_by_xpath('(//*[@resource-id="com.amorepacific.amorepacificmall:id/tv_product_name"])[1]').text
                        prodname_1 = prodname.split()

                        # ?곹뭹紐??ㅼ뿉 ?먮쭏???먮Ⅴ湲?(媛꾪뿉?곸쑝濡??곸씠???⑥뼱 諛쒖깮?쇰줈 ?쇰? ?⑥뼱留?寃利?
                        for replace_text in prodname_1:
                            if int(replace_text in prodname) and len(prodname.partition(replace_text)[0]) > \
                                    len(prodname.partition(replace_text)[2]):
                                prodname = prodname.partition(replace_text)[0]
                                prodname = prodname.strip()
                        print(prodname)

                        self.interact_by_id('com.amorepacific.amorepacificmall:id/header_cart_button_image_view')  # ?ㅻ뜑 ?곸뿭 ?λ컮援щ땲 吏꾩엯
                        sleep(2)

                        ### ?λ컮援щ땲 ?붾㈃ ###
                        self.interact_by_xpath('//android.view.View[contains(@content-desc,"{}")]'.format(prodname), click=False)  # 泥?踰덉㎏ 醫뗭븘???곹뭹怨??쇱튂 ?뺤씤
                        cart_prodcount = TCFG.driver.find_element_by_xpath('//android.view.View[contains(@content-desc,"{}")]'
                                                                           '/android.view.View[2]/android.widget.TextView[3]'.format(prodname)).text  # ?λ컮援щ땲 ?섎웾 ???                        # ?대떦 ?곹뭹 ?λ컮援щ땲 ?섎웾 2媛??댁긽 ?뺤씤
                        if int(cart_prodcount) >= 2:
                            pass
                        else:
                            AssertionError('湲곗〈 ?λ컮援щ땲 醫뗭븘???곹뭹 ?덈뒗 ?곹깭 > ?λ컮援щ땲 ?닿린 ?숈옉 fail 諛쒖깮')

                        self.interact_by_xpath('//android.widget.Button[@text="?リ린"]')  # ?λ컮援щ땲 [X]踰꾪듉 ?대┃
                # 蹂듭닔 媛쒖쓽 ?⑥쐞 ?곹뭹??寃쎌슦
                elif self.is_element_present('//android.widget.Button[@text="?곹뭹???좏깮?댁＜?몄슂"]', By.XPATH):  # ?곹뭹 ?곸꽭濡??대룞 諛??듭뀡 ?좏깮 ?덉씠???뷀뤃???ㅽ뵂 ?곹깭 ?뺤씤
                    TCFG.driver.back()  # ?쇳븨?덉뒪?좊━ 醫뗭븘???곸뿭?쇰줈 ?대룞
                # ?λ컮援щ땲 ?닿린媛 遺덇????곹깭
                elif self.is_element_present('//android.widget.Button[@text="?ъ엯怨??뚮┝ ?좎껌"]', By.XPATH):  # ?곹뭹 ?곸꽭濡??대룞 諛??ъ엯怨??뚮┝ ?좎껌 ?곹깭 ?뺤씤
                    TCFG.driver.back()  # ?쇳븨?덉뒪?좊━ 醫뗭븘???곸뿭?쇰줈 ?대룞

            # ?먯＜ 援щℓ ?곹뭹???녿뒗 寃쎌슦
            except:
                self.interact_by_xpath('//android.widget.TextView[@text="?먯＜ 援щℓ???곹뭹???놁뒿?덈떎."]', click=False)  # 臾멸뎄 ?몄텧 ?뺤씤

            self.interact_by_xpath('//android.widget.LinearLayout[@content-desc="釉뚮옖??]')  # 釉뚮옖?????대┃

            ### 釉뚮옖????###
            # 醫뗭븘?뷀븳 釉뚮옖?쒓? ?덈뒗 寃쎌슦
            try:
                self.interact_by_xpath('//*[@resource-id="com.amorepacific.amorepacificmall:id/total_count_text"][contains(@text,"媛쒖쓽 醫뗭븘??釉뚮옖?쒓? ?덉뒿?덈떎.")]', click=False)  # 醫뗭븘??釉뚮옖??媛쒖닔 ?쒓린 ?곸뿭 ?뺤씤

                ## 泥?踰덉㎏ 釉뚮옖?????寃利?                self.interact_by_xpath('(//*[@resource-id="com.amorepacific.amorepacificmall:id/brand_logo"])[1]', click=False)  # 釉뚮옖???대?吏 ?뺤씤
                self.interact_by_xpath('(//*[@resource-id="com.amorepacific.amorepacificmall:id/brand_name"])[1]', click=False)  # 釉뚮옖?쒕챸 ?뺤씤
                self.interact_by_xpath('(//*[@resource-id="com.amorepacific.amorepacificmall:id/like_button"])[1]', click=False)  # 釉뚮옖??醫뗭븘???꾩씠肄??뺤씤
                self.interact_by_xpath('(//*[@resource-id="com.amorepacific.amorepacificmall:id/product_img"])[1]', click=False)  # 釉뚮옖???곹뭹 ?대?吏 ?뺤씤

                TCFG.driver.swipe(TCFG.res[0] * 0.8, TCFG.res[1] * 0.5, TCFG.res[0] * 0.2, TCFG.res[1] * 0.5)  # 泥?踰덉㎏ 釉뚮옖??????곹뭹 醫뚯슦濡??ㅽ겕濡?                self.interact_by_xpath('//android.widget.TextView[@text="??蹂닿린"]')  # ??蹂닿린 踰꾪듉 ?대┃
                sleep(2)

                ### 釉뚮옖?쒓? ?꾩껜 ?곹뭹 ??###
                self.interact_by_xpath('//android.webkit.WebView[contains(@text,"釉뚮옖?쒓?")]', click=False)  # 釉뚮옖?쒓? 硫붿씤 ?붾㈃ ?대룞 ?뺤씤
                self.interact_by_xpath('//android.widget.Button[@text="?꾩껜"]', click=False)  # ?꾩껜 ???몄텧 ?뺤씤
            # 醫뗭븘?뷀븳 釉뚮옖?쒓? ?녿뒗 寃쎌슦
            except:
                self.interact_by_xpath('//android.widget.TextView[@text="?꾩쭅 醫뗭븘????釉뚮옖?쒓? ?놁뒿?덈떎."]', click=False)  # 醫뗭븘?뷀븳 釉뚮옖?쒓? ?놁쓬???섑??대뒗 臾멸뎄 ?몄텧 ?뺤씤
                self.interact_by_id('com.amorepacific.amorepacificmall:id/empty_recommend_button')  # 異붿쿇 ?멸린 釉뚮옖??蹂대윭媛湲?踰꾪듉 ?대┃

                ### BEST ??###
                self.interact_by_xpath('//android.widget.TextView[@text="?멸린 釉뚮옖??]', click=False)  # BEST ??> ?멸린 釉뚮옖?????뺤씤
        except:
            self.capture_screen()
            self.assertEqual(0, 18)
        else:
            print(f"{sys._getframe(0).f_code.co_name} Passed")
            TCFG.is_passed = True
        finally:
            TCFG.is_finished = True
