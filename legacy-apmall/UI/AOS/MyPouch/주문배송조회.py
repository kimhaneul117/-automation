def test_006_二쇰Ц_諛곗넚_議고쉶(self):
    try:
        ### 留덉씠?뚯슦移??붾㈃ ###
        scroll_id(self, 'com.amorepacific.amorepacificmall:id/ly_order_list', loc=TCFG.res[1] * 0.55, y1=TCFG.res[1] * 0.6, y2=TCFG.res[1] * 0.5)  # 二쇰Ц/諛곗넚 議고쉶 ??硫붾돱 ?대┃

        ### 二쇰Ц/諛곗넚 議고쉶 ?붾㈃ ###
        sleep(3)
        self.interact_by_xpath('//android.widget.TextView[@text="二쇰Ц/諛곗넚 議고쉶"]', click=False)  # 二쇰Ц/諛곗넚 議고쉶 ?붾㈃ ??댄? ?뺤씤
        self.interact_by_xpath('//android.widget.Button[@text="3媛쒖썡"]', click=False)  # 議고쉶 湲곌컙 > 3媛쒖썡 default ?뺤씤
        self.interact_by_xpath('//android.widget.Button[@text="?꾩껜"]', click=False)  # 諛곗넚 ?곹깭 > ?꾩껜 default ?뺤씤

        # 泥?踰덉㎏ 二쇰Ц 嫄????寃利?> 二쇰Ц ?댁뿭 = Y, status = 援щℓ ?뺤젙 , 由щ럭 ?묒꽦 = Y or N, P??= Y or N
        if self.is_element_present('//android.view.View[@text="援щℓ?뺤젙"]', By.XPATH):
            self.interact_by_xpath('//*[@text="?곸꽭蹂닿린"]', click=False)  # ?곸꽭 蹂닿린 踰꾪듉 ?뺤씤
            if TCFG.environment == 'PRD':  # PRD ?섍꼍
                prod = TCFG.driver.find_element_by_xpath('//android.widget.TextView[contains(@text, "?꾨え?덊띁?쒗뵿 ?곹뭹")]').text.split(' ')  # 二쇰Ц 嫄??곹뭹 媛?닔 ???

                # 蹂듯빀 二쇰Ц
                if len(prod[2].split('媛?)[1]) > 1:
                    # 二쇰Ц 嫄??곹뭹 媛?닔 留뚰겮 紐⑤몢 寃利?
                    for i in range(1, len(prod[2]) + 1):
                        self.interact_by_xpath('(//android.widget.Image)[{}]'.format(i), click=False)  # ?곹뭹 ?대?吏 ?뺤씤
                        self.interact_by_xpath('(//android.widget.Button[@text="?λ컮援щ땲"])[{}]'.format(i), click=False)  # ?λ컮援щ땲 ?꾩씠肄??뺤씤
                # ?⑥씪 二쇰Ц
                else:
                    self.interact_by_xpath('//android.widget.Image', click=False)  # ?곹뭹 ?대?吏 ?뺤씤
                    self.interact_by_xpath('//android.widget.Button[@text="?λ컮援щ땲"]', click=False)  # ?λ컮援щ땲 ?꾩씠肄??뺤씤
            elif TCFG.environment == 'STG':  # STG ?섍꼍
                prod = TCFG.driver.find_element_by_xpath('//android.widget.TextView[contains(@text, "?꾨え?덊띁?쒗뵿 ?곹뭹")]').text.split(' ')  # 二쇰Ц 嫄??곹뭹 媛?닔 ???

                # 蹂듯빀 二쇰Ц
                if len(prod[2].split('媛?)[1]) > 1:
                    # 二쇰Ц 嫄??곹뭹 媛?닔 留뚰겮 紐⑤몢 寃利?
                    for i in range(1, len(prod) + 1):
                        self.interact_by_xpath('(//android.widget.Button[@text="?λ컮援щ땲"])[{}]'.format(i), click=False)  # ?λ컮援щ땲 ?꾩씠肄??뺤씤
                # ?⑥씪 二쇰Ц
                else:
                    self.interact_by_xpath('//android.widget.Button[@text="?λ컮援щ땲"]', click=False)  # ?λ컮援щ땲 ?꾩씠肄??뺤씤

            # 諛묒쑝濡?議곌툑 ?대룞
            TCFG.driver.swipe(TCFG.res[0] * 0.5, TCFG.res[1] * 0.5, TCFG.res[0] * 0.5, TCFG.res[1] * 0.2)

            # P???곹뭹 and ?⑥씪 二쇰Ц??寃쎌슦, 由щ럭 踰꾪듉 誘몃끂異쒕줈 ?덉쇅 泥섎━
            if not self.is_element_present('//android.widget.TextView[1][contains(@text, "[P]")]', By.XPATH) and len(prod) == 1:
                # 由щ럭 ?묒꽦 = Y
                try:
                    self.interact_by_xpath('//android.widget.Button[@text="由щ럭?뺤씤"]')  # 由щ럭 ?뺤씤 踰꾪듉 ?대┃

                    ### 由щ럭 ?붾㈃ ###
                    self.interact_by_xpath('//*[@text="?묒꽦??由щ럭"][@clickable="true"]',  click=False)  # ?묒꽦??由щ럭 ??쑝濡??대룞 ?뺤씤
                # 由щ럭 ?묒꽦 = N
                except:
                    self.interact_by_xpath('//android.widget.Button[@text="由щ럭?묒꽦"]')  # 由щ럭 ?묒꽦 踰꾪듉 ?대┃

                    ### 由щ럭 ?뺣㈃ ###
                    self.interact_by_xpath('//*[@text="誘몄옉??由щ럭"][@clickable="true"]', click=False)  # 誘몄옉??由щ럭 ??쑝濡??대룞 ?뺤씤
                    self.interact_by_xpath('//android.view.View[@content-desc="由щ럭 ?묒꽦"]', click=False)  # 由щ럭 ?묒꽦 踰꾪듉 ?뺤씤

                self.interact_by_id('com.amorepacific.amorepacificmall:id/back_button_image_view')  # gnb ?ㅻ줈 媛湲?> 二쇰Ц/諛곗넚 議고쉶 ?붾㈃?쇰줈 ?대룞

            ### 二쇰Ц/諛곗넚 議고쉶 ?붾㈃ ###
            delivery_time = TCFG.driver.find_element_by_xpath('//android.widget.TextView[contains(@text,") 諛곗넚?꾨즺")]').text  # MM??DD??day of the week) 諛곗넚?꾨즺 ?띿뒪?????
            delivery_time1 = delivery_time.lstrip("0")  # MM ???먮┸?섏씪 寃쎌슦 '0' ?쒓굅
            delivery_time2 = delivery_time1.replace("??", "/").replace("??, "").split('\n')  # MM/DD(day of the week) ?뺥깭濡?蹂??
            tracking_detail = delivery_time.replace("??", "-").replace("??, "").split('\n')  # MM-DD(day of the week) ?뺥깭濡?蹂??
            tracking_detail = [f.split("(") for f in tracking_detail]  # ?붿씪怨?遺꾨━
            scroll_xpath(self, '//android.widget.Button[@text="諛곗넚議고쉶"]', loc=TCFG.res[1] * 0.55, y1=TCFG.res[1] * 0.6, y2=TCFG.res[1] * 0.5)  # 諛곗넚 議고쉶 踰꾪듉 ?대┃

            ### 諛곗넚 議고쉶 ?붾㈃ ###
            self.interact_by_xpath('//android.widget.TextView[@text="{}"]'.format(delivery_time2[0]), click=False)  # 諛곗넚 ?④퀎 ?쒖떆 ?곸뿭 ?좎쭨 + 諛곗넚 ?꾨즺 ?띿뒪???뺤씤
            self.interact_by_xpath('//android.widget.ListView//android.widget.TextView[@text="諛곗넚?꾨즺"]', click=False)  # 諛곗넚 異붿쟻 ?뷀뀒??留덉?留??곹깭 諛곗넚 ?꾨즺 ?몄텧 ?뺤씤
            self.interact_by_xpath('//android.widget.ListView/android.view.View[1]/android.widget.TextView[contains(@text,"{}")]'.format((tracking_detail[0])[0]), click=False)  # 二쇰Ц/諛곗넚 議고쉶 ?붾㈃ 諛곗넚 ?꾨즺?쇨낵 諛곗넚 異붿쿃 ?붾㈃ 諛곗넚 ?꾨즺???쇱튂 ?뺤씤
            self.interact_by_xpath('//android.widget.Button[@text="?ㅻ줈媛湲?]')  # 醫뚯륫 ?곷떒 ?ㅻ줈媛湲?踰꾪듉 ?대┃
            sleep(2)

            ### 二쇰Ц/諛곗넚 議고쉶 ?붾㈃ ###
            scroll_xpath(self, '//android.widget.Button[@text="1:1 臾몄쓽"]', loc=TCFG.res[1] * 0.55, y1=TCFG.res[1] * 0.6, y2=TCFG.res[1] * 0.5, click=False)  # 1:1 臾몄쓽 踰꾪듉 ?뺤씤
            self.interact_by_xpath('//android.widget.Button[@text="?ъ＜臾?]', click=False)  # ?ъ＜臾?踰꾪듉 ?뺤씤
            
        # 泥?踰덉㎏ 二쇰Ц 嫄????寃利?> 二쇰Ц ?댁뿭 = Y, status = 諛곗넚 ?꾨즺, 援щℓ?뺤젙 = N
        elif self.is_element_present('//android.view.View[@text="諛곗넚?꾨즺"]', By.XPATH):
            self.interact_by_xpath('//*[@text="?곸꽭蹂닿린"]', click=False)  # ?곸꽭 蹂닿린 踰꾪듉 ?뺤씤
            if TCFG.environment == 'PRD':  # PRD ?섍꼍
                prod = TCFG.driver.find_element_by_xpath('//android.widget.TextView[contains(@text, "?꾨え?덊띁?쒗뵿 ?곹뭹")]').text.split(' ')  # 二쇰Ц 嫄??곹뭹 媛?닔 ???

                # 蹂듯빀 二쇰Ц
                if len(prod[2].split('媛?)[1]) > 1:
                    # 二쇰Ц 嫄??곹뭹 媛?닔 留뚰겮 紐⑤몢 寃利?
                    for i in range(1, len(prod) + 1):
                        self.interact_by_xpath('(//android.widget.Image)[{}]'.format(i), click=False)  # ?곹뭹 ?대?吏 ?뺤씤
                        self.interact_by_xpath('(//android.widget.Button[@text="?λ컮援щ땲"])[{}]'.format(i), click=False)  # ?λ컮援щ땲 ?꾩씠肄??뺤씤
                # ?⑥씪 二쇰Ц
                else:
                    self.interact_by_xpath('//android.widget.Image', click=False)  # ?곹뭹 ?대?吏 ?뺤씤
                    self.interact_by_xpath('//android.widget.Button[@text="?λ컮援щ땲"]', click=False)  # ?λ컮援щ땲 ?꾩씠肄??뺤씤
            elif TCFG.environment == 'STG':  # STG ?섍꼍
                prod = TCFG.driver.find_element_by_xpath('//android.widget.TextView[contains(@text, "?꾨え?덊띁?쒗뵿 ?곹뭹")]').text.split(' ')  # 二쇰Ц 嫄??곹뭹 媛?닔 ???

                # 蹂듯빀 二쇰Ц
                if len(prod[2].split('媛?)[1]) > 1:
                    # 二쇰Ц 嫄??곹뭹 媛?닔 留뚰겮 紐⑤몢 寃利?
                    for i in range(1, len(prod) + 1):
                        self.interact_by_xpath('(//android.widget.Button[@text="?λ컮援щ땲"])[{}]'.format(i), click=False)  # ?λ컮援щ땲 ?꾩씠肄??뺤씤
                # ?⑥씪 二쇰Ц
                else:
                    self.interact_by_xpath('//android.widget.Button[@text="?λ컮援щ땲"]', click=False)  # ?λ컮援щ땲 ?꾩씠肄??뺤씤

            self.interact_by_xpath('//android.widget.Button[@text="援щℓ?뺤젙"]', click=False)  # 援щℓ ?뺤젙 踰꾪듉 ?뺤씤

            # P???곹뭹 and ?⑥씪 二쇰Ц??寃쎌슦 誘몃끂異??덉쇅 泥섎━
            if not self.is_element_present('//android.widget.TextView[1][contains(@text, "[P]")]', By.XPATH) and len(prod) == 1:
                self.interact_by_xpath('//android.widget.TextView[contains(@text,"援щℓ ?뺤젙 諛?由щ럭 ?묒꽦 ??)]', click=False)  # 援щℓ ?뺤젙

            # 諛묒쑝濡?議곌툑 ?대룞
            TCFG.driver.swipe(TCFG.res[0] * 0.5, TCFG.res[1] * 0.5, TCFG.res[0] * 0.5, TCFG.res[1] * 0.2)

            # P???곹뭹 and ?⑥씪 二쇰Ц??寃쎌슦, 由щ럭 踰꾪듉 誘몃끂異??덉쇅 泥섎━
            if not self.is_element_present('//android.widget.TextView[1][contains(@text, "[P]")]', By.XPATH) and len(prod) == 1:
                # 由щ럭 ?묒꽦 = Y
                try:
                    self.interact_by_xpath('//android.widget.Button[@text="由щ럭?뺤씤"]')  # 由щ럭 ?뺤씤 踰꾪듉 ?대┃

                    ### 由щ럭 ?붾㈃ ###
                    self.interact_by_xpath('//*[@text="?묒꽦??由щ럭"][@clickable="true"]',  click=False)  # ?묒꽦??由щ럭 ??쑝濡??대룞 ?뺤씤
                # 由щ럭 ?묒꽦 = N
                except:
                    self.interact_by_xpath('//android.widget.Button[@text="由щ럭?묒꽦"]')  # 由щ럭 ?묒꽦 踰꾪듉 ?대┃

                    ### 由щ럭 ?뺣㈃ ###
                    self.interact_by_xpath('//*[@text="誘몄옉??由щ럭"][@clickable="true"]', click=False)  # 誘몄옉??由щ럭 ??쑝濡??대룞 ?뺤씤
                    self.interact_by_xpath('//android.view.View[@content-desc="由щ럭 ?묒꽦"]', click=False)  # 由щ럭 ?묒꽦 踰꾪듉 ?뺤씤

                self.interact_by_id('com.amorepacific.amorepacificmall:id/back_button_image_view')  # gnb ?ㅻ줈 媛湲?> 二쇰Ц/諛곗넚 議고쉶 ?붾㈃?쇰줈 ?대룞

            scroll_xpath(self, '//android.widget.Button[@text="援먰솚?좎껌"]', loc=TCFG.res[1] * 0.55, y1=TCFG.res[1] * 0.6, y2=TCFG.res[1] * 0.5, click=False)  # 援먰솚 ?좎껌 踰꾪듉 ?뺤씤
            self.interact_by_xpath('//android.widget.Button[@text="諛섑뭹?좎껌"]', click=False)  # 諛섑뭹 ?좎껌 踰꾪듉 ?뺤씤

            ### 二쇰Ц/諛곗넚 議고쉶 ?붾㈃ ###
            delivery_time = TCFG.driver.find_element_by_xpath('//android.widget.TextView[contains(@text,") 諛곗넚?꾨즺")]').text  # MM??DD??day of the week) 諛곗넚?꾨즺 ?띿뒪?????
            delivery_time1 = delivery_time.lstrip("0")  # MM ???먮┸?섏씪 寃쎌슦 '0' ?쒓굅
            delivery_time2 = delivery_time1.replace("??", "/").replace("??, "").split('\n')  # MM/DD(day of the week) ?뺥깭濡?蹂??
            tracking_detail = delivery_time.replace("??", "-").replace("??, "").split('\n')  # MM-DD(day of the week) ?뺥깭濡?蹂??
            tracking_detail = [f.split("(") for f in tracking_detail]  # ?붿씪怨?遺꾨━
            scroll_xpath(self, '//android.widget.Button[@text="諛곗넚議고쉶"]', loc=TCFG.res[1] * 0.55, y1=TCFG.res[1] * 0.6, y2=TCFG.res[1] * 0.5)  # 諛곗넚 議고쉶 踰꾪듉 ?대┃

            ### 諛곗넚 議고쉶 ?붾㈃ ###
            self.interact_by_xpath('//android.widget.TextView[@text="{}"]'.format(delivery_time2[0]), click=False)  # 諛곗넚 ?④퀎 ?쒖떆 ?곸뿭 ?좎쭨 + 諛곗넚 ?꾨즺 ?띿뒪???뺤씤
            self.interact_by_xpath('//android.widget.ListView//android.widget.TextView[@text="諛곗넚?꾨즺"]', click=False)  # 諛곗넚 異붿쟻 ?뷀뀒??留덉?留??곹깭 諛곗넚 ?꾨즺 ?몄텧 ?뺤씤
            self.interact_by_xpath('//android.widget.ListView/android.view.View[1]/android.widget.TextView[contains(@text,"{}")]'.format((tracking_detail[0])[0]), click=False)  # 二쇰Ц/諛곗넚 議고쉶 ?붾㈃ 諛곗넚 ?꾨즺?쇨낵 諛곗넚 異붿쿃 ?붾㈃ 諛곗넚 ?꾨즺???쇱튂 ?뺤씤
            self.interact_by_xpath('//android.widget.Button[@text="?ㅻ줈媛湲?]')  # 醫뚯륫 ?곷떒 ?ㅻ줈媛湲?踰꾪듉 ?대┃
            sleep(2)

            ### 二쇰Ц/諛곗넚 議고쉶 ?붾㈃ ###
            scroll_xpath(self, '//android.widget.Button[@text="1:1 臾몄쓽"]', loc=TCFG.res[1] * 0.55, y1=TCFG.res[1] * 0.6, y2=TCFG.res[1] * 0.5, click=False)  # 1:1 臾몄쓽 踰꾪듉 ?뺤씤

        # 泥?踰덉㎏ 二쇰Ц 嫄????寃利?> 二쇰Ц ?댁뿭 = Y, status = 諛곗넚 以?
        elif self.is_element_present('//android.view.View[@text="諛곗넚以?]', By.XPATH):
            self.interact_by_xpath('//*[@text="?곸꽭蹂닿린"]', click=False)  # ?곸꽭 蹂닿린 踰꾪듉 ?뺤씤
            if TCFG.environment == 'PRD':  # PRD ?섍꼍
                prod = TCFG.driver.find_element_by_xpath('//android.widget.TextView[contains(@text, "?꾨え?덊띁?쒗뵿 ?곹뭹")]').text.split(' ')  # 二쇰Ц 嫄??곹뭹 媛?닔 ???

                # 蹂듯빀 二쇰Ц
                if len(prod[2].split('媛?)[1]) > 1:
                    # 二쇰Ц 嫄??곹뭹 媛?닔 留뚰겮 紐⑤몢 寃利?
                    for i in range(1, len(prod) + 1):
                        self.interact_by_xpath('(//android.widget.Image)[{}]'.format(i), click=False)  # ?곹뭹 ?대?吏 ?뺤씤
                        self.interact_by_xpath('(//android.widget.Button[@text="?λ컮援щ땲"])[{}]'.format(i), click=False)  # ?λ컮援щ땲 ?꾩씠肄??뺤씤
                # ?⑥씪 二쇰Ц
                else:
                    self.interact_by_xpath('//android.widget.Image', click=False)  # ?곹뭹 ?대?吏 ?뺤씤
                    self.interact_by_xpath('//android.widget.Button[@text="?λ컮援щ땲"]', click=False)  # ?λ컮援щ땲 ?꾩씠肄??뺤씤
            elif TCFG.environment == 'STG':  # STG ?섍꼍
                prod = TCFG.driver.find_element_by_xpath(
                    '//android.widget.TextView[contains(@text, "?꾨え?덊띁?쒗뵿 ?곹뭹")]').text.split(' ')  # 二쇰Ц 嫄??곹뭹 媛?닔 ???

                # 蹂듯빀 二쇰Ц
                if len(prod[2].split('媛?)[1]) > 1:
                    # 二쇰Ц 嫄??곹뭹 媛?닔 留뚰겮 紐⑤몢 寃利?
                    for i in range(1, len(prod) + 1):
                        self.interact_by_xpath('(//android.widget.Button[@text="?λ컮援щ땲"])[{}]'.format(i), click=False)  # ?λ컮援щ땲 ?꾩씠肄??뺤씤
                # ?⑥씪 二쇰Ц
                else:
                    self.interact_by_xpath('//android.widget.Button[@text="?λ컮援щ땲"]', click=False)  # ?λ컮援щ땲 ?꾩씠肄??뺤씤

            scroll_xpath(self, '//android.widget.Button[@text="諛곗넚議고쉶"]', loc=TCFG.res[1] * 0.55, y1=TCFG.res[1] * 0.6, y2=TCFG.res[1] * 0.5)  # 諛곗넚 議고쉶 踰꾪듉 ?대┃

            ### 諛곗넚 議고쉶 ?붾㈃ ###
            # status = 諛곗넚 以? 諛곗넚 異쒕컻 ?곹깭??寃쎌슦
            if self.is_element_present('//android.widget.TextView[@text="諛곗넚異쒕컻"]', By.XPATH):
                self.interact_by_xpath('//android.widget.TextView[contains(@text,") ?꾩갑?덉젙")]', click=False)  # 諛곗넚 ?④퀎 ?꾩갑 ?덉젙 臾멸뎄 ?몄텧 ?뺤씤
            # status = 諛곗넚 以? 吏묓솕 泥섎━ ?곹깭??寃쎌슦
            else:
                self.interact_by_xpath('//android.widget.TextView[@text="吏묓솕泥섎━"]', click=False)  # 諛곗넚 異붿쿃 ?뷀뀒??吏묓솕 泥섎━ ?곹깭 ?몄텧 ?뺤씤
            self.interact_by_xpath('//android.widget.Button[@text="?ㅻ줈媛湲?]')  # 醫뚯륫 ?곷떒 ?ㅻ줈媛湲?踰꾪듉 ?대┃
            sleep(3)

            ### 二쇰Ц/諛곗넚 議고쉶 ?붾㈃ ###
            self.interact_by_xpath('//android.widget.Button[@text="?섎졊?뺤씤"]', click=False)  # ?섎졊 ?뺤씤 踰꾪듉 ?뺤씤
            self.interact_by_xpath('//android.widget.Button[@text="1:1 臾몄쓽"]', click=False)  # 1:1 臾몄쓽 踰꾪듉 ?뺤씤

        # 泥?踰덉㎏ 二쇰Ц 嫄????寃利?> 二쇰Ц ?댁뿭 = Y, status = ?곹뭹 以鍮?以?
        elif self.is_element_present('//android.view.View[@text="?곹뭹以鍮꾩쨷"]', By.XPATH):
            self.interact_by_xpath('//*[@text="?곸꽭蹂닿린"]', click=False)  # ?곸꽭 蹂닿린 踰꾪듉 ?뺤씤
            if TCFG.environment == 'PRD':  # PRD ?섍꼍
                prod = TCFG.driver.find_element_by_xpath('//android.widget.TextView[contains(@text, "?꾨え?덊띁?쒗뵿 ?곹뭹")]').text.split(' ')  # 二쇰Ц 嫄??곹뭹 媛?닔 ???

                # 蹂듯빀 二쇰Ц
                if len(prod[2].split('媛?)[1]) > 1:
                    # 二쇰Ц 嫄??곹뭹 媛?닔 留뚰겮 紐⑤몢 寃利?
                    for i in range(1, len(prod) + 1):
                        self.interact_by_xpath('(//android.widget.Image)[{}]'.format(i), click=False)  # ?곹뭹 ?대?吏 ?뺤씤
                        self.interact_by_xpath('(//android.widget.Button[@text="?λ컮援щ땲"])[{}]'.format(i), click=False)  # ?λ컮援щ땲 ?꾩씠肄??뺤씤
                # ?⑥씪 二쇰Ц
                else:
                    self.interact_by_xpath('//android.widget.Image', click=False)  # ?곹뭹 ?대?吏 ?뺤씤
                    self.interact_by_xpath('//android.widget.Button[@text="?λ컮援щ땲"]', click=False)  # ?λ컮援щ땲 ?꾩씠肄??뺤씤
            elif TCFG.environment == 'STG':  # STG ?섍꼍
                prod = TCFG.driver.find_element_by_xpath('//android.widget.TextView[contains(@text, "?꾨え?덊띁?쒗뵿 ?곹뭹")]').text.split(' ')  # 二쇰Ц 嫄??곹뭹 媛?닔 ???

                # 蹂듯빀 二쇰Ц
                if len(prod[2].split('媛?)[1]) > 1:
                    # 二쇰Ц 嫄??곹뭹 媛?닔 留뚰겮 紐⑤몢 寃利?
                    for i in range(1, len(prod) + 1):
                        self.interact_by_xpath('(//android.widget.Button[@text="?λ컮援щ땲"])[{}]'.format(i), click=False)  # ?λ컮援щ땲 ?꾩씠肄??뺤씤
                # ?⑥씪 二쇰Ц
                else:
                    self.interact_by_xpath('//android.widget.Button[@text="?λ컮援щ땲"]', click=False)  # ?λ컮援щ땲 ?꾩씠肄??뺤씤

            self.interact_by_xpath('//android.widget.Button[@text="痍⑥냼?붿껌"]', click=False)  # 痍⑥냼 ?붿껌 踰꾪듉 ?뺤씤
            self.interact_by_xpath('//android.widget.Button[@text="1:1 臾몄쓽"]', click=False)  # 1:1 臾몄쓽 踰꾪듉 ?뺤씤

        # 泥?踰덉㎏ 二쇰Ц 嫄????寃利?> 二쇰Ц ?댁뿭 = Y, status = 寃곗젣 ?꾨즺
        elif self.is_element_present('//android.view.View[@text="寃곗젣?꾨즺"]', By.XPATH):
            self.interact_by_xpath('//*[@text="?곸꽭蹂닿린"]', click=False)  # ?곸꽭 蹂닿린 踰꾪듉 ?뺤씤
            if TCFG.environment == 'PRD':  # PRD ?섍꼍
                prod = TCFG.driver.find_element_by_xpath('//android.widget.TextView[contains(@text, "?꾨え?덊띁?쒗뵿 ?곹뭹")]').text.split(' ')  # 二쇰Ц 嫄??곹뭹 媛?닔 ???

                # 蹂듯빀 二쇰Ц
                if len(prod[2].split('媛?)[1]) > 1:
                    # 二쇰Ц 嫄??곹뭹 媛?닔 留뚰겮 紐⑤몢 寃利?
                    for i in range(1, len(prod) + 1):
                        self.interact_by_xpath('(//android.widget.Image)[{}]'.format(i), click=False)  # ?곹뭹 ?대?吏 ?뺤씤
                        self.interact_by_xpath('(//android.widget.Button[@text="?λ컮援щ땲"])[{}]'.format(i), click=False)  # ?λ컮援щ땲 ?꾩씠肄??뺤씤
                # ?⑥씪 二쇰Ц
                else:
                    self.interact_by_xpath('//android.widget.Image', click=False)  # ?곹뭹 ?대?吏 ?뺤씤
                    self.interact_by_xpath('//android.widget.Button[@text="?λ컮援щ땲"]', click=False)  # ?λ컮援щ땲 ?꾩씠肄??뺤씤
            elif TCFG.environment == 'STG':  # STG ?섍꼍
                prod = TCFG.driver.find_element_by_xpath('//android.widget.TextView[contains(@text, "?꾨え?덊띁?쒗뵿 ?곹뭹")]').text.split(' ')  # 二쇰Ц 嫄??곹뭹 媛?닔 ???

                # 蹂듯빀 二쇰Ц
                if len(prod[2].split('媛?)[1]) > 1:
                    # 二쇰Ц 嫄??곹뭹 媛?닔 留뚰겮 紐⑤몢 寃利?
                    for i in range(1, len(prod) + 1):
                        self.interact_by_xpath('(//android.widget.Button[@text="?λ컮援щ땲"])[{}]'.format(i), click=False)  # ?λ컮援щ땲 ?꾩씠肄??뺤씤
                # ?⑥씪 二쇰Ц
                else:
                    self.interact_by_xpath('//android.widget.Button[@text="?λ컮援щ땲"]', click=False)  # ?λ컮援щ땲 ?꾩씠肄??뺤씤

            self.interact_by_xpath('//android.widget.Button[@text="二쇰Ц痍⑥냼"]', click=False)  # 二쇰Ц 痍⑥냼 踰꾪듉 ?뺤씤
            self.interact_by_xpath('//android.widget.Button[@text="1:1 臾몄쓽"]', click=False)  # 1:1 臾몄쓽 踰꾪듉 ?뺤씤

    # 二쇰Ц ?댁뿭 = N
        else:
            self.interact_by_xpath('//*[@text="理쒓렐 二쇰Ц ?댁뿭???놁뒿?덈떎."]', click=False)  # 臾멸뎄 ?몄텧 ?뺤씤
    except:
        self.capture_screen()
        self.assertEqual(0, 1)
    else:
        print(f"{sys._getframe(0).f_code.co_name} Passed")
        TCFG.is_passed = True
    finally:
            self.interact_by_xpath('//android.view.View[@content-desc="留덉씠"]')  # ?섎떒 ?≪뀡諛?留덉씠?뚯슦移섎줈 ?대룞
