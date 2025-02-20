    def test_020_HOME_뷰티_라이브(self):
        try:
            login(self, TCFG)  # 로그인 완료

            # 메인 레이어 팝업 노출 시 "오늘은 보지 않기" 클릭
            isPopup = is_element_present(TCFG.driver, '//*[@class="aiqua__button"]')

            if isPopup:
                self.hl_and_interact(By.XPATH, '//*[contains(@class, "qg-inweb-close")]')
            sleep(2)

            ### 아모레몰 메인 화면 ###
            TCFG.driver.execute_script('window.scrollTo(0, 1000);')  # 하단으로 스크롤

            self.hl_and_interact(By.XPATH, '//*[@class="module-heading__title"][text()="BEAUTY LIVE"]', click=False)  # BEAUTY LIVE 코너까지 스크롤

            LIVE = TCFG.driver.find_element_by_xpath('//*[@class="module-banner-live__contents"]')  # LIVE 노출 갯수 저장

            for i in range(1, int(LIVE) + 1):
                ## 라이브 플래그 케이스별 활성화 라이브 모두 검증
                if is_element_present(TCFG.driver, '(//*[@class="module-banner-live__flag is-onair"]//*[contains(text(),"LIVE")])[{}]'.format(i)):  # 라이브 플래그 방송 중인 경우
                    self.hl_and_interact(By.XPATH, '//*[@class="atom-icon ic_play_s12_fff"]', click=False)  # 라이브 플래그 조회수 아이콘 확인
                    self.hl_and_interact(By.XPATH, '//*[@class="module-banner-live__count"]', click=False)  # 라이브 플래그 조회수 카운트 확인
                    self.hl_and_interact(By.XPATH, '(//*[contains(@src, "https://d9ck1x1y7uycj.cloudfront.net/uploads/6476dd27055f2e00121e1a35/broadcast/img/2025/")])[{}]'.format(i), click=False)  # 라이브 이미지 노출 확인
                    self.hl_and_interact(By.XPATH, '(//*[contains(@href, "/kr/ko/product/detail?onlineProdSn=")][@ap-click-name="MAIN_뷰티라이브_상품상세"])[{}]'.format(i), click=False)  # 라이브 상품 노출 확인
                elif is_element_present(TCFG.driver, '(//*[@class="module-banner-live__flag"][contains(text(),"오늘")])[{}]'.format(i)):  # 라이브 플래그 오늘 방송 예정인 경우
                    self.hl_and_interact(By.XPATH, '(//*[contains(@src, "https://d9ck1x1y7uycj.cloudfront.net/uploads/6476dd27055f2e00121e1a35/broadcast/img/2025/")])[{}]'.format(i), click=False)  # 라이브 이미지 노출 확인
                    self.hl_and_interact(By.XPATH, '(//*[contains(@href, "/kr/ko/product/detail?onlineProdSn=")][@ap-click-name="MAIN_뷰티라이브_상품상세"])[{}]'.format(i), click=False)  # 라이브 상품 노출 확인
                elif is_element_present(TCFG.driver, '(//*[@class="module-banner-live__flag"][contains(text(),"내일")])[{}]'.format(i)):  # 라이브 플래그 내일 방송 예정인 경우
                    self.hl_and_interact(By.XPATH, '(//*[contains(@src, "https://d9ck1x1y7uycj.cloudfront.net/uploads/6476dd27055f2e00121e1a35/broadcast/img/2025/")])[{}]'.format(i), click=False)  # 라이브 이미지 노출 확인
                    self.hl_and_interact(By.XPATH, '(//*[contains(@href, "/kr/ko/product/detail?onlineProdSn=")][@ap-click-name="MAIN_뷰티라이브_상품상세"])[{}]'.format(i), click=False)  # 라이브 상품 노출 확인
                elif is_element_present(TCFG.driver, '(//*[@class="module-banner-live__flag"][contains(text(),"월")])[{}]'.format(i)):  # 라이브 플래그 내일 모레 이후 방송 얘정인 경우
                    self.hl_and_interact(By.XPATH, '(//*[contains(@src, "https://d9ck1x1y7uycj.cloudfront.net/uploads/6476dd27055f2e00121e1a35/broadcast/img/2025/")])[{}]'.format(i), click=False)  # 라이브 이미지 노출 확인
                    self.hl_and_interact(By.XPATH, '(//*[contains(@href, "/kr/ko/product/detail?onlineProdSn=")][@ap-click-name="MAIN_뷰티라이브_상품상세"])[{}]'.format(i), click=False)  # 라이브 상품 노출 확인
        except:
            self.capture_screen()
            self.assertEqual(0, 1)
        else:
            print(f"{sys._getframe(0).f_code.co_name} Passed")
            TCFG.is_passed = True

    def test_021_BEST_많이_구매한(self):
        try:
            ### 홈 ###
            self.hl_and_interact(By.XPATH, '//*[@ap-click-name="GNB_BEST"]')  # BEST 탭 클릭

            ### BEST 탭 ###
            ## 많이 구매한 탭
            self.hl_and_interact(By.XPATH, '//*[@class="icon-tab"]', click=False)  # BEST 랭킹 탭 영역 확인
            self.hl_and_interact(By.XPATH, '//*[@ap-click-data="많이 구매한"][@aria-selected="true"]', click=False)  # 많이 구매한 탭 활성화 상태 확인
            self.hl_and_interact(By.XPATH, '//*[@class="icon-tab__button"]/..//*[text()="많이 구매한"]', click=False)  # 많이 구매한 탭 확인
            self.hl_and_interact(By.XPATH, '//*[@class="icon-tab__button"]/..//*[text()="많이 클릭한"]', click=False)  # 많이 클릭한 탭 확인
            self.hl_and_interact(By.XPATH, '//*[@class="icon-tab__button"]/..//*[text()="많이 검색한"]', click=False)  # 많이 검색한 탭 확인
            self.hl_and_interact(By.XPATH, '//*[@class="icon-tab__button"]/..//*[text()="피부에 맞는"]', click=False)  # 피부에 맞는 탭 확인
            self.hl_and_interact(By.XPATH, '//*[@ap-click-name="BEST_많이구매한_필터"]//*[text()="초기화"]', click=False)  # 로그인 상태 > 초기화 버튼 노출 상태 확인
            self.hl_and_interact(By.XPATH, '//*[@ap-click-name="BEST_많이구매한_필터"]//*[text()="일간"]', click=False)  # 일간 선택 확인
            self.hl_and_interact(By.XPATH, '//*[@ap-click-name="BEST_많이구매한_필터"]//*[text()="카테고리"]', click=False)  # 카테고리 선택 확인
            self.hl_and_interact(By.XPATH, '//*[@class="btnRound on"][@ap-click-name="BEST_많이구매한_필터"]//*[text()="20대 이하"]', click=False)  # 계정별 회원 정보 기반으로 연령대 자동 세팅 처리 확인
            self.hl_and_interact(By.XPATH, '//*[@ap-click-name="BEST_많이구매한_필터"]//*[text()="브랜드"]', click=False)  # 브랜드 선택 확인
        except:
            capture_screen(self, TCFG)
            self.assertEqual(0, 1)
            print("Failed")
        else:
            print(f"{sys._getframe(0).f_code.co_name} Passed")
            TCFG.is_passed = True