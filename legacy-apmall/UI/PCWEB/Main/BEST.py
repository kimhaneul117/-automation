    def test_022_BEST_留롮씠_?대┃??self):
        try:
            ### BEST ??###
            self.hl_and_interact(By.XPATH, '//*[@class="icon-tab__button"]/..//*[text()="留롮씠 ?대┃??]')  # 留롮씠 ?대┃?????좏깮

            ## 留롮씠 ?대┃????            self.hl_and_interact(By.XPATH, '//*[@ap-click-data="留롮씠 ?대┃??][@aria-selected="true"]', click=False)  # 留롮씠 ?대┃?????쒖꽦???곹깭 ?뺤씤
            self.hl_and_interact(By.XPATH, '//*[@ap-click-name="BEST_留롮씠?대┃???꾪꽣"]//*[text()="移댄뀒怨좊━"]')  # 移댄뀒怨좊━ ?좏깮
            sleep(3)

            ## ?μ뭅?뚭퀬由??꾪꽣 ?곸꽭
            self.hl_and_interact(By.XPATH, '//*[@ap-click-name="BEST_?꾪꽣?곸꽭_移댄뀒怨좊━"][text()="由?]')  # 由??좏깮
            self.hl_and_interact(By.XPATH, '//*[@class="btnContained"][text()="由?]', click=False)  # 由?移댄뀒怨좊━ ?쒖꽦???곹깭 ?뺤씤
            self.hl_and_interact(By.XPATH, '//*[text()="?곸슜"]')  # ?곸슜?섍린 ?대┃
            sleep(2)

            ## 留롮씠 ?대┃????            self.hl_and_interact(By.XPATH, '//*[@ap-click-name="BEST_留롮씠?대┃???꾪꽣"]//*[text()="珥덇린??]', click=False)  # 珥덇린??踰꾪듉 ?좎? ?뺤씤
            self.hl_and_interact(By.XPATH, '//*[@ap-click-name="BEST_留롮씠?대┃???꾪꽣"]//*[text()="釉뚮옖??]')  # 釉뚮옖???좏깮
            sleep(2)

            ## 釉뚮옖???꾪꽣 ?곸꽭
            # # 釉뚮옖?쒕챸 ?쒖꽌?濡?3媛???? ######### 20250103 湲곗? 釉뚮옖?쒕챸 ?쒖꽌 ?쒕뜡?섍쾶 ?곸슜?섏뼱 二쇱꽍 泥섎━  ###########
            # brand_1 = TCFG.driver.find_element_by_xpath('(//*[@ap-click-name="BEST_?꾪꽣?곸꽭_釉뚮옖??])[1]').text
            # brand_2 = TCFG.driver.find_element_by_xpath('(//*[@ap-click-name="BEST_?꾪꽣?곸꽭_釉뚮옖??])[2]').text
            # brand_3 = TCFG.driver.find_element_by_xpath('(//*[@ap-click-name="BEST_?꾪꽣?곸꽭_釉뚮옖??])[3]').text
            # brand_total = [brand_1, brand_2, brand_3]
            # return_brand = ','.join(brand_total)
            #
            # # ?꾪꽣 ?ㅼ젙 ???좏깮??釉뚮옖?쒕챸 ?꾩뼱?곌린 ?ы븿 理쒕? 10湲?먭퉴吏 ?몄텧 ??留먯쨪??泥섎━
            # if len(return_brand) > 10:
            #     return_abb = return_brand[0:10] + '...'
            #     return_brand, return_abb = return_abb, return_brand

            self.hl_and_interact(By.XPATH, '(//*[@ap-click-name="BEST_?꾪꽣?곸꽭_釉뚮옖??])[1]')  # 泥?踰덉㎏ 釉뚮옖???좏깮
            self.hl_and_interact(By.XPATH, '(//*[@ap-click-name="BEST_?꾪꽣?곸꽭_釉뚮옖??])[2]')  # ??踰덉㎏ 釉뚮옖???좏깮
            self.hl_and_interact(By.XPATH, '(//*[@ap-click-name="BEST_?꾪꽣?곸꽭_釉뚮옖??])[3]')  # ??踰덉㎏ 釉뚮옖???좏깮
            self.hl_and_interact(By.XPATH, '//*[text()="?곸슜"]')  # ?곸슜?섍린 ?대┃
            sleep(2)

            ## 留롮씠 ?대┃????            self.hl_and_interact(By.XPATH, '//*[@class="btnRound on"][@ap-click-name="BEST_留롮씠?대┃???꾪꽣"]//*[text()="由?]', click=False)  # 移댄뀒怨좊━ 由??좏깮 ?뺤씤
            self.hl_and_interact(By.XPATH, '//*[@class="btnRound on"][@ap-click-name="BEST_留롮씠?대┃???꾪꽣"]//*[text()="20? ?댄븯"]', click=False)  # 怨꾩젙蹂??뚯썝 ?뺣낫 湲곕컲?쇰줈 ?곕졊? ?먮룞 ?명똿 泥섎━ ?뺤씤
            self.hl_and_interact(By.XPATH, '//*[@class="btnRound on"][@ap-click-name="BEST_留롮씠?대┃???꾪꽣"]//*[contains(text(),"...")]', click=False)  # 釉뚮옖???꾪꽣 留먯쨪??泥섎━ ?뺤씤
            try:
                self.hl_and_interact(By.XPATH, '//*[@class="txtTip"]/..//*[text()="{}"]'.format(datetime.now().strftime('%m.%d %H:%M')), click=False)  # ?꾩옱 ?좎쭨 ?쒓컙 湲곗? ?몄텧 ?뺤씤
            except:
                before_one_minute = datetime.now() - relativedelta(minutes=1)  # ?꾩옱 ?쒓컙 湲곗? 1遺???援ы븯湲?                self.hl_and_interact(By.XPATH, '//*[@class="txtTip"]/..//*[text()="{}"]'.format(before_one_minute.strftime('%m.%d %H:%M')), click=False)  # ?꾩옱 ?좎쭨 ?쒓컙 湲곗? ?몄텧 ?뺤씤
            self.hl_and_interact(By.XPATH, '(//*[@class="productCardList module__grid p-col4_m-col2"]/..//*[@class="prodMedia"]'
                                           '/..//*[contains(@src, "https://images-kr.amoremall.com/products/")])[1]', click=False)  # 泥?踰덉㎏ ?곹뭹 ?대?吏 ?뺤씤
            self.hl_and_interact(By.XPATH, '//*[@ap-click-name="BEST_留롮씠?대┃???꾪꽣"][@ap-click-data="珥덇린??]')  # 珥덇린??踰꾪듉 ?대┃
            sleep(1)

            # 3媛??꾪꽣 ?ㅼ젙 珥덇린???곹깭 ?뺤씤
            self.hl_and_interact(By.XPATH, '//*[@ap-click-name="BEST_留롮씠?대┃???꾪꽣"]//*[text()="移댄뀒怨좊━"]', click=False)  # 移댄뀒怨좊━ 珥덇린???곹깭 ?뺤씤
            self.hl_and_interact(By.XPATH, '//*[@ap-click-name="BEST_留롮씠?대┃???꾪꽣"]//*[text()="?곕졊?"]', click=False)  # ?곕졊? 珥덇린???곹깭 ?뺤씤
            self.hl_and_interact(By.XPATH, '//*[@ap-click-name="BEST_留롮씠?대┃???꾪꽣"]//*[text()="釉뚮옖??]', click=False)  # 釉뚮옖??珥덇린???곹깭 ?뺤씤
            self.hl_and_interact(By.XPATH, '(//*[@class="productCardList module__grid p-col4_m-col2"]/..//*[@class="prodMedia"]'
                                           '/..//*[contains(@src, "https://images-kr.amoremall.com/products/")])[1]', click=False)  # 泥?踰덉㎏ ?곹뭹 ?대?吏 ?뺤씤 (APM-45780)
        except:
            capture_screen(self, TCFG)
            self.assertEqual(0, 1)
            print("Failed")
        else:
            print(f"{sys._getframe(0).f_code.co_name} Passed")
            TCFG.is_passed = True

    def test_023_BEST_留롮씠_寃?됲븳(self):
        try:
            ### BEST ??###
            ## 留롮씠 ?대┃????            self.hl_and_interact(By.XPATH, '//*[@class="icon-tab__button"]/..//*[text()="留롮씠 寃?됲븳"]')  # 留롮씠 寃?됲븳 ???대┃
            sleep(2)

            ## 留롮씠 寃?됲븳 ??> ?멸린 ?ㅼ썙????            try:
                self.hl_and_interact(By.XPATH, '//*[@class="txtTip"]/..//*[text()="{}"]'.format(datetime.now().strftime('%m.%d %H:%M')), click=False)  # ?꾩옱 ?좎쭨 ?쒓컙 湲곗? ?몄텧 ?뺤씤
                print(datetime.now().strftime('%m.%d %H:%M'))
            except:
                before_one_minute = datetime.now() - relativedelta(minutes=1)  # ?꾩옱 ?쒓컙 湲곗? 1遺???援ы븯湲?                self.hl_and_interact(By.XPATH, '//*[@class="txtTip"]/..//*[text()="{}"]'.format(before_one_minute.strftime('%m.%d %H:%M')), click=False)  # ?꾩옱 ?좎쭨 ?쒓컙 湲곗? ?몄텧 ?뺤씤
                print(before_one_minute.strftime('%m.%d %H:%M'))

            self.hl_and_interact(By.XPATH, '(//*[@class="tag__number"])[1]/..//*[text()="1"]', click=False)  # ??궧 1 ?몄텧 ?뺤씤
            self.hl_and_interact(By.XPATH, '(//*[@class="tag__number"])[2]/..//*[text()="2"]', click=False)  # ??궧 2 ?몄텧 ?뺤씤
            self.hl_and_interact(By.XPATH, '(//*[@class="prodCardBody"]/..//*[@class="prodMedia"]/..//*[contains(@src, "https://images-kr.amoremall.com/products/")])[1]', click=False)  # ??궧 1 泥?踰덉㎏ ?곹뭹 ?몄텧 ?뺤씤
            self.hl_and_interact(By.XPATH, '//*[text()="?멸린 釉뚮옖??]')  # ?멸린 釉뚮옖?????좏깮

            ## 留롮씠 寃?됲븳 ??> ?멸린 釉뚮옖????            self.hl_and_interact(By.XPATH, '(//*[@class="tag__number"])[1]/..//*[text()="1"]', click=False)  # ??궧 1 ?몄텧 ?뺤씤
            self.hl_and_interact(By.XPATH, '(//*[@class="tag__number"])[2]/..//*[text()="2"]', click=False)  # ??궧 2 ?몄텧 ?뺤씤
            self.hl_and_interact(By.XPATH, '(//*[@class="imgBox"]/..//*[contains(@src, "https://images-kr.amoremall.com/fileupload/brand/")])[1]', click=False)  # ??궧 1 釉뚮옖??濡쒓퀬 ?대?吏 ?뺤씤
            self.hl_and_interact(By.XPATH, '(//*[@class="imgBox"]/..//*[contains(@src, "https://images-kr.amoremall.com/fileupload/brand/")])[2]', click=False)  # ??궧 2 釉뚮옖??濡쒓퀬 ?대?吏 ?뺤씤
            try:
                self.hl_and_interact(By.XPATH, '(//*[@class="rank__btn"])[1]//*[@class="btnProdLike on"]', click=False)  # ??궧 1 醫뗭븘??on ?곹깭 ?뺤씤
            except:
                self.hl_and_interact(By.XPATH, '(//*[@class="rank__btn"])[1]//*[@class="btnProdLike"]', click=False)  # ??궧 1 醫뗭븘??off ?곹깭 ?뺤씤
        except:
            capture_screen(self, TCFG)
            self.assertEqual(0, 1)
            print("Failed")
        else:
            print(f"{sys._getframe(0).f_code.co_name} Passed")
            TCFG.is_passed = True
