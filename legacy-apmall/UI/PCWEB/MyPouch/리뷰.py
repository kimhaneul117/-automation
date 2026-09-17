    def test_010_誘몄옉??由щ럭???뺤씤(self):
        try:
            ### 留덉씠?뚯슦移?###
            TCFG.driver.execute_script('window.scrollTo(0, 700);')  # ?섎떒?쇰줈 ?ㅽ겕濡?
            self.hl_and_interact(By.XPATH, '//*[@ap-click-name="留덉씠?뚯슦移?由щ럭愿由?]')  # 由щ럭 愿由?吏꾩엯

            ### 由щ럭 ?붾㈃ ###
            self.hl_and_interact(By.XPATH, '//*[@class="on"]//*[@id="tabButtonOrder"][text()="誘몄옉??由щ럭"]', click=False)  # 誘몄옉??由щ럭 ??default ?쒖꽦???곹깭 ?뺤씤

            # 誘몄옉??由щ럭媛 ?덈뒗 寃쎌슦
            try:
                self.hl_and_interact(By.XPATH, '//*[@style="display: none;"]/..//p[text()="?묒꽦??由щ럭媛 ?놁뒿?덈떎"]', click=False)  # ?묒꽦??由щ럭媛 ?놁뒿?덈떎. 臾멸뎄 誘몃끂異??곹깭 ?뺤씤

                # ?쒕떖 ?ъ슜 由щ럭 議댁옱 (data-review-type="OneMonth")
                try:
                    prod_name = TCFG.driver.find_element_by_xpath('(//*[@class="badge-wrap"]/..//*[@class="product_name"])[1]').text  # ?곹뭹紐????                    prod_name_1 = prod_name.split()  # ?곹뭹紐??꾩뼱?곌린 援ш컙 ?먮Ⅴ湲?                    print(prod_name_1)

                    # ?곹뭹紐??ㅼ뿉 ?먮쭏???먮Ⅴ湲?(媛꾪뿉?곸쑝濡??꾩뼱?곌린 ?곸씠???⑥뼱 諛쒖깮?쇰줈 ?쇰? ?⑥뼱留?寃利?
                    for replace_text in prod_name_1:
                        if int(replace_text in prod_name) and len(prod_name.partition(replace_text)[0]) > \
                                len(prod_name.partition(replace_text)[2]):
                            prod_name = prod_name.partition(replace_text)[0]
                            prod_name = prod_name.strip()
                    print(prod_name)

                    self.hl_and_interact(By.XPATH, '//*[text()="誘몄옉??由щ럭"]/..//*[@class="badge green"][text()="?쒕떖 ?ъ슜 由щ럭"]', click=False)  # ?쒕떖 ?묒꽦 由щ럭 諭껋? ?뺤씤
                    self.hl_and_interact(By.XPATH, '(//*[@class="page-sub-title"]/..//*[text()="由щ럭 ?묒꽦"]/..//*[@data-review-type="OneMonth"])[1]')  # 由щ럭 ?묒꽦 踰꾪듉 ?대┃

                    ### ?쒕떖 ?ъ슜 由щ럭 ?묒꽦 ?붾㈃ ###
                    self.hl_and_interact(By.XPATH, '//*[@class="page-sub-title"]/..//*[text()="?쒕떖 ?ъ슜 由щ럭 ?묒꽦"]', click=False)
                    self.hl_and_interact(By.XPATH, '//*[@class="score review_copy"]/..//*[text()="?쒕떖 ?숈븞 ?ъ슜?대낫???대븷?섏슂?"]', click=False)
                # ?쇰컲 由щ럭 議댁옱 (data-review-type="Pur")
                except:
                    prod_name = TCFG.driver.find_element_by_xpath('(//*[@class="product_name"])[1]').text  # ?곹뭹紐????                    prod_name_1 = prod_name.split()  # ?곹뭹紐??꾩뼱?곌린 援ш컙 ?먮Ⅴ湲?                    print(prod_name_1)

                    # ?곹뭹紐??ㅼ뿉 ?먮쭏???먮Ⅴ湲?(媛꾪뿉?곸쑝濡??꾩뼱?곌린 ?곸씠???⑥뼱 諛쒖깮?쇰줈 ?쇰? ?⑥뼱留?寃利?
                    for replace_text in prod_name_1:
                        if int(replace_text in prod_name) and len(prod_name.partition(replace_text)[0]) > \
                                len(prod_name.partition(replace_text)[2]):
                            prod_name = prod_name.partition(replace_text)[0]
                            prod_name = prod_name.strip()
                    print(prod_name)

                    self.hl_and_interact(By.XPATH, '(//*[@class="page-sub-title"]/..//*[text()="由щ럭 ?묒꽦"]/..//*[@data-review-type="Pur"])[1]')  # 由щ럭 ?묒꽦 踰꾪듉 ?대┃

                    ### 由щ럭 ?묒꽦 ?붾㈃ ###
                    self.hl_and_interact(By.XPATH, '//*[@class="score review_copy"]/..//*[text()="?ъ슜?대낫???대븷?섏슂?"]', click=False)

                ## 怨듯넻 寃利??곸뿭
                self.hl_and_interact(By.XPATH, '//*[@class="product_name"][contains(text(), "{}")]'.format(prod_name), click=False)  # 由щ럭 ?묒꽦 ?곹뭹 ?쇱튂 ?뺤씤
                self.hl_and_interact(By.XPATH, '//*[@class="ui_rating new 竊쟲ating-apply"]', click=False)  # 蹂꾩젏 ?깅줉 ?곸뿭 ?뺤씤

                # 蹂꾩젏 2???좏깮
                self.hl_and_interact(By.XPATH, '(//*[@class="ficon ficon-star-25"])[1]')
                self.hl_and_interact(By.XPATH, '(//*[@class="ficon ficon-star-25"])[2]')

                self.hl_and_interact(By.XPATH, '//*[@class="section review_question"]', click=False)  # 由щ럭 吏덈Ц ?곸뿭 ?몄텧 ?뺤씤
                self.hl_and_interact(By.XPATH, '//*[@class="btn_previous"]')  # 怨듯넻 ?ㅻ뜑 ?ㅻ줈 媛湲?踰꾪듉 ?대┃
            # 誘몄옉??由щ럭媛 ?녿뒗 寃쎌슦
            except:
                self.hl_and_interact(By.XPATH, '//*[@class="non_content order"]/..//*[text()="?묒꽦??由щ럭媛 ?놁뒿?덈떎"]', click=False)  # ?묒꽦??由щ럭媛 ?놁뒿?덈떎. 臾멸뎄 ?몄텧 ?곹깭 ?뺤씤
                none = is_element_present(TCFG.driver, '//*[@class="non_content order"][@style="display: block;"]//*[text()="?묒꽦??由щ럭媛 ?놁뒿?덈떎"]')  # 鍮?怨듬갚 ?몄텧 ???먮윭 異쒕젰 (APM-41432)
                if none:
                    print("誘몄옉??由щ럭 ??鍮?怨듬갚 ?몄텧 Failed")
                    capture_screen(self, TCFG)
                    self.assertEqual(0, 1)
        except:
            capture_screen(self, TCFG)
            self.assertEqual(0, 1)
            print("Failed")
        else:
            print(f"{sys._getframe(0).f_code.co_name} Passed")
            TCFG.is_passed = True

    def test_011_?묒꽦??由щ럭???뺤씤(self):
        try:
            ### 由щ럭 愿由??붾㈃ ###
            self.hl_and_interact(By.XPATH, '//*[@id="tabButtonReview"][text()="?묒꽦??由щ럭"]')  # ?묒꽦??由щ럭 ???대┃

            # ?묒꽦??由щ럭 ?댁뿭???덈뒗 寃쎌슦
            try:
                self.hl_and_interact(By.XPATH, '(//*[@class="btn_area"]/a[text()="?섏젙?섍린"])[1]', click=False)
            # ?묒꽦??由щ럭 ?댁뿭???녿뒗 寃쎌슦
            except:
                self.hl_and_interact(By.XPATH, '//*[text()="?묒꽦??由щ럭媛 ?놁뒿?덈떎"]', click=False)

            # 媛꾪뿉?곸쑝濡?諛쒖깮 ?섎뒗 鍮?怨듬갚 ?몄텧 ?댁뒋濡??ы솗??(APP ?숈씪 諛쒖깮?????덉쓬)
            self.hl_and_interact(By.XPATH, '//*[@id="tabButtonOrder"][text()="誘몄옉??由щ럭"]')  # 誘몄옉??由щ럭 ???대┃

            none = is_element_present(TCFG.driver, '//*[@class="non_content order"][@style="display: block;"]//*[text()="?묒꽦??由щ럭媛 ?놁뒿?덈떎"]')  # 鍮?怨듬갚 ?몄텧 ???먮윭 異쒕젰 (APM-41432)
            if none:
                print("誘몄옉??由щ럭 ??鍮?怨듬갚 ?몄텧 Failed")
                capture_screen(self, TCFG)
                self.assertEqual(0, 1)
                
            TCFG.driver.execute_script("window.history.go(-1)")  # ?ㅻ줈 媛湲?        except:
            capture_screen(self, TCFG)
            self.assertEqual(0, 1)
            print("Failed")
        else:
            print(f"{sys._getframe(0).f_code.co_name} Passed")
            TCFG.is_passed = True
        finally:
            self.hl_and_interact(By.XPATH, '//*[@href="/kr/ko/my/page/info/myPouch"]')  # 留덉씠?뚯슦移섎줈 ?대룞
