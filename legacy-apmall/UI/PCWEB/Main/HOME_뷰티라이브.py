    def test_020_HOME_酉고떚_?쇱씠釉?self):
        try:
            login(self, TCFG)  # 濡쒓렇???꾨즺

            # 硫붿씤 ?덉씠???앹뾽 ?몄텧 ??"?ㅻ뒛? 蹂댁? ?딄린" ?대┃
            isPopup = is_element_present(TCFG.driver, '//*[@class="aiqua__button"]')

            if isPopup:
                self.hl_and_interact(By.XPATH, '//*[contains(@class, "qg-inweb-close")]')
            sleep(2)

            ### ?꾨え?덈ぐ 硫붿씤 ?붾㈃ ###
            TCFG.driver.execute_script('window.scrollTo(0, 1000);')  # ?섎떒?쇰줈 ?ㅽ겕濡?
            self.hl_and_interact(By.XPATH, '//*[@class="module-heading__title"][text()="BEAUTY LIVE"]', click=False)  # BEAUTY LIVE 肄붾꼫源뚯? ?ㅽ겕濡?
            LIVE = TCFG.driver.find_element_by_xpath('//*[@class="module-banner-live__contents"]')  # LIVE ?몄텧 媛?닔 ???
            for i in range(1, int(LIVE) + 1):
                ## ?쇱씠釉??뚮옒洹?耳?댁뒪蹂??쒖꽦???쇱씠釉?紐⑤몢 寃利?                if is_element_present(TCFG.driver, '(//*[@class="module-banner-live__flag is-onair"]//*[contains(text(),"LIVE")])[{}]'.format(i)):  # ?쇱씠釉??뚮옒洹?諛⑹넚 以묒씤 寃쎌슦
                    self.hl_and_interact(By.XPATH, '//*[@class="atom-icon ic_play_s12_fff"]', click=False)  # ?쇱씠釉??뚮옒洹?議고쉶???꾩씠肄??뺤씤
                    self.hl_and_interact(By.XPATH, '//*[@class="module-banner-live__count"]', click=False)  # ?쇱씠釉??뚮옒洹?議고쉶??移댁슫???뺤씤
                    self.hl_and_interact(By.XPATH, '(//*[contains(@src, "https://d9ck1x1y7uycj.cloudfront.net/uploads/6476dd27055f2e00121e1a35/broadcast/img/2025/")])[{}]'.format(i), click=False)  # ?쇱씠釉??대?吏 ?몄텧 ?뺤씤
                    self.hl_and_interact(By.XPATH, '(//*[contains(@href, "/kr/ko/product/detail?onlineProdSn=")][@ap-click-name="MAIN_酉고떚?쇱씠釉??곹뭹?곸꽭"])[{}]'.format(i), click=False)  # ?쇱씠釉??곹뭹 ?몄텧 ?뺤씤
                elif is_element_present(TCFG.driver, '(//*[@class="module-banner-live__flag"][contains(text(),"?ㅻ뒛")])[{}]'.format(i)):  # ?쇱씠釉??뚮옒洹??ㅻ뒛 諛⑹넚 ?덉젙??寃쎌슦
                    self.hl_and_interact(By.XPATH, '(//*[contains(@src, "https://d9ck1x1y7uycj.cloudfront.net/uploads/6476dd27055f2e00121e1a35/broadcast/img/2025/")])[{}]'.format(i), click=False)  # ?쇱씠釉??대?吏 ?몄텧 ?뺤씤
                    self.hl_and_interact(By.XPATH, '(//*[contains(@href, "/kr/ko/product/detail?onlineProdSn=")][@ap-click-name="MAIN_酉고떚?쇱씠釉??곹뭹?곸꽭"])[{}]'.format(i), click=False)  # ?쇱씠釉??곹뭹 ?몄텧 ?뺤씤
                elif is_element_present(TCFG.driver, '(//*[@class="module-banner-live__flag"][contains(text(),"?댁씪")])[{}]'.format(i)):  # ?쇱씠釉??뚮옒洹??댁씪 諛⑹넚 ?덉젙??寃쎌슦
                    self.hl_and_interact(By.XPATH, '(//*[contains(@src, "https://d9ck1x1y7uycj.cloudfront.net/uploads/6476dd27055f2e00121e1a35/broadcast/img/2025/")])[{}]'.format(i), click=False)  # ?쇱씠釉??대?吏 ?몄텧 ?뺤씤
                    self.hl_and_interact(By.XPATH, '(//*[contains(@href, "/kr/ko/product/detail?onlineProdSn=")][@ap-click-name="MAIN_酉고떚?쇱씠釉??곹뭹?곸꽭"])[{}]'.format(i), click=False)  # ?쇱씠釉??곹뭹 ?몄텧 ?뺤씤
                elif is_element_present(TCFG.driver, '(//*[@class="module-banner-live__flag"][contains(text(),"??)])[{}]'.format(i)):  # ?쇱씠釉??뚮옒洹??댁씪 紐⑤젅 ?댄썑 諛⑹넚 ?섏젙??寃쎌슦
                    self.hl_and_interact(By.XPATH, '(//*[contains(@src, "https://d9ck1x1y7uycj.cloudfront.net/uploads/6476dd27055f2e00121e1a35/broadcast/img/2025/")])[{}]'.format(i), click=False)  # ?쇱씠釉??대?吏 ?몄텧 ?뺤씤
                    self.hl_and_interact(By.XPATH, '(//*[contains(@href, "/kr/ko/product/detail?onlineProdSn=")][@ap-click-name="MAIN_酉고떚?쇱씠釉??곹뭹?곸꽭"])[{}]'.format(i), click=False)  # ?쇱씠釉??곹뭹 ?몄텧 ?뺤씤
        except:
            self.capture_screen()
            self.assertEqual(0, 1)
        else:
            print(f"{sys._getframe(0).f_code.co_name} Passed")
            TCFG.is_passed = True

    def test_021_BEST_留롮씠_援щℓ??self):
        try:
            ### ??###
            self.hl_and_interact(By.XPATH, '//*[@ap-click-name="GNB_BEST"]')  # BEST ???대┃

            ### BEST ??###
            ## 留롮씠 援щℓ????            self.hl_and_interact(By.XPATH, '//*[@class="icon-tab"]', click=False)  # BEST ??궧 ???곸뿭 ?뺤씤
            self.hl_and_interact(By.XPATH, '//*[@ap-click-data="留롮씠 援щℓ??][@aria-selected="true"]', click=False)  # 留롮씠 援щℓ?????쒖꽦???곹깭 ?뺤씤
            self.hl_and_interact(By.XPATH, '//*[@class="icon-tab__button"]/..//*[text()="留롮씠 援щℓ??]', click=False)  # 留롮씠 援щℓ?????뺤씤
            self.hl_and_interact(By.XPATH, '//*[@class="icon-tab__button"]/..//*[text()="留롮씠 ?대┃??]', click=False)  # 留롮씠 ?대┃?????뺤씤
            self.hl_and_interact(By.XPATH, '//*[@class="icon-tab__button"]/..//*[text()="留롮씠 寃?됲븳"]', click=False)  # 留롮씠 寃?됲븳 ???뺤씤
            self.hl_and_interact(By.XPATH, '//*[@class="icon-tab__button"]/..//*[text()="?쇰???留욌뒗"]', click=False)  # ?쇰???留욌뒗 ???뺤씤
            self.hl_and_interact(By.XPATH, '//*[@ap-click-name="BEST_留롮씠援щℓ???꾪꽣"]//*[text()="珥덇린??]', click=False)  # 濡쒓렇???곹깭 > 珥덇린??踰꾪듉 ?몄텧 ?곹깭 ?뺤씤
            self.hl_and_interact(By.XPATH, '//*[@ap-click-name="BEST_留롮씠援щℓ???꾪꽣"]//*[text()="?쇨컙"]', click=False)  # ?쇨컙 ?좏깮 ?뺤씤
            self.hl_and_interact(By.XPATH, '//*[@ap-click-name="BEST_留롮씠援щℓ???꾪꽣"]//*[text()="移댄뀒怨좊━"]', click=False)  # 移댄뀒怨좊━ ?좏깮 ?뺤씤
            self.hl_and_interact(By.XPATH, '//*[@class="btnRound on"][@ap-click-name="BEST_留롮씠援щℓ???꾪꽣"]//*[text()="20? ?댄븯"]', click=False)  # 怨꾩젙蹂??뚯썝 ?뺣낫 湲곕컲?쇰줈 ?곕졊? ?먮룞 ?명똿 泥섎━ ?뺤씤
            self.hl_and_interact(By.XPATH, '//*[@ap-click-name="BEST_留롮씠援щℓ???꾪꽣"]//*[text()="釉뚮옖??]', click=False)  # 釉뚮옖???좏깮 ?뺤씤
        except:
            capture_screen(self, TCFG)
            self.assertEqual(0, 1)
            print("Failed")
        else:
            print(f"{sys._getframe(0).f_code.co_name} Passed")
            TCFG.is_passed = True
