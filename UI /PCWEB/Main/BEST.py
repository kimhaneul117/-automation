    def test_022_BEST_많이_클릭한(self):
        try:
            ### BEST 탭 ###
            self.hl_and_interact(By.XPATH, '//*[@class="icon-tab__button"]/..//*[text()="많이 클릭한"]')  # 많이 클릭한 탭 선택

            ## 많이 클릭한 탭
            self.hl_and_interact(By.XPATH, '//*[@ap-click-data="많이 클릭한"][@aria-selected="true"]', click=False)  # 많이 클릭한 탭 활성화 상태 확인
            self.hl_and_interact(By.XPATH, '//*[@ap-click-name="BEST_많이클릭한_필터"]//*[text()="카테고리"]')  # 카테고리 선택
            sleep(3)

            ## 장카테고리 필터 상세
            self.hl_and_interact(By.XPATH, '//*[@ap-click-name="BEST_필터상세_카테고리"][text()="립"]')  # 립 선택
            self.hl_and_interact(By.XPATH, '//*[@class="btnContained"][text()="립"]', click=False)  # 립 카테고리 활성화 상태 확인
            self.hl_and_interact(By.XPATH, '//*[text()="적용"]')  # 적용하기 클릭
            sleep(2)

            ## 많이 클릭한 탭
            self.hl_and_interact(By.XPATH, '//*[@ap-click-name="BEST_많이클릭한_필터"]//*[text()="초기화"]', click=False)  # 초기화 버튼 유지 확인
            self.hl_and_interact(By.XPATH, '//*[@ap-click-name="BEST_많이클릭한_필터"]//*[text()="브랜드"]')  # 브랜드 선택
            sleep(2)

            ## 브랜드 필터 상세
            # # 브랜드명 순서대로 3개 저장  ######### 20250103 기준 브랜드명 순서 랜덤하게 적용되어 주석 처리  ###########
            # brand_1 = TCFG.driver.find_element_by_xpath('(//*[@ap-click-name="BEST_필터상세_브랜드"])[1]').text
            # brand_2 = TCFG.driver.find_element_by_xpath('(//*[@ap-click-name="BEST_필터상세_브랜드"])[2]').text
            # brand_3 = TCFG.driver.find_element_by_xpath('(//*[@ap-click-name="BEST_필터상세_브랜드"])[3]').text
            # brand_total = [brand_1, brand_2, brand_3]
            # return_brand = ','.join(brand_total)
            #
            # # 필터 설정 시 선택된 브랜드명 띄어쓰기 포함 최대 10글자까지 노출 후 말줄임 처리
            # if len(return_brand) > 10:
            #     return_abb = return_brand[0:10] + '...'
            #     return_brand, return_abb = return_abb, return_brand

            self.hl_and_interact(By.XPATH, '(//*[@ap-click-name="BEST_필터상세_브랜드"])[1]')  # 첫 번째 브랜드 선택
            self.hl_and_interact(By.XPATH, '(//*[@ap-click-name="BEST_필터상세_브랜드"])[2]')  # 두 번째 브랜드 선택
            self.hl_and_interact(By.XPATH, '(//*[@ap-click-name="BEST_필터상세_브랜드"])[3]')  # 세 번째 브랜드 선택
            self.hl_and_interact(By.XPATH, '//*[text()="적용"]')  # 적용하기 클릭
            sleep(2)

            ## 많이 클릭한 탭
            self.hl_and_interact(By.XPATH, '//*[@class="btnRound on"][@ap-click-name="BEST_많이클릭한_필터"]//*[text()="립"]', click=False)  # 카테고리 립 선택 확인
            self.hl_and_interact(By.XPATH, '//*[@class="btnRound on"][@ap-click-name="BEST_많이클릭한_필터"]//*[text()="20대 이하"]', click=False)  # 계정별 회원 정보 기반으로 연령대 자동 세팅 처리 확인
            self.hl_and_interact(By.XPATH, '//*[@class="btnRound on"][@ap-click-name="BEST_많이클릭한_필터"]//*[contains(text(),"...")]', click=False)  # 브랜드 필터 말줄임 처리 확인
            try:
                self.hl_and_interact(By.XPATH, '//*[@class="txtTip"]/..//*[text()="{}"]'.format(datetime.now().strftime('%m.%d %H:%M')), click=False)  # 현재 날짜 시간 기준 노출 확인
            except:
                before_one_minute = datetime.now() - relativedelta(minutes=1)  # 현재 시간 기준 1분 전 구하기
                self.hl_and_interact(By.XPATH, '//*[@class="txtTip"]/..//*[text()="{}"]'.format(before_one_minute.strftime('%m.%d %H:%M')), click=False)  # 현재 날짜 시간 기준 노출 확인
            self.hl_and_interact(By.XPATH, '(//*[@class="productCardList module__grid p-col4_m-col2"]/..//*[@class="prodMedia"]'
                                           '/..//*[contains(@src, "https://images-kr.amoremall.com/products/")])[1]', click=False)  # 첫 번째 상품 이미지 확인
            self.hl_and_interact(By.XPATH, '//*[@ap-click-name="BEST_많이클릭한_필터"][@ap-click-data="초기화"]')  # 초기화 버튼 클릭
            sleep(1)

            # 3개 필터 설정 초기화 상태 확인
            self.hl_and_interact(By.XPATH, '//*[@ap-click-name="BEST_많이클릭한_필터"]//*[text()="카테고리"]', click=False)  # 카테고리 초기화 상태 확인
            self.hl_and_interact(By.XPATH, '//*[@ap-click-name="BEST_많이클릭한_필터"]//*[text()="연령대"]', click=False)  # 연령대 초기화 상태 확인
            self.hl_and_interact(By.XPATH, '//*[@ap-click-name="BEST_많이클릭한_필터"]//*[text()="브랜드"]', click=False)  # 브랜드 초기화 상태 확인
            self.hl_and_interact(By.XPATH, '(//*[@class="productCardList module__grid p-col4_m-col2"]/..//*[@class="prodMedia"]'
                                           '/..//*[contains(@src, "https://images-kr.amoremall.com/products/")])[1]', click=False)  # 첫 번째 상품 이미지 확인 (APM-45780)
        except:
            capture_screen(self, TCFG)
            self.assertEqual(0, 1)
            print("Failed")
        else:
            print(f"{sys._getframe(0).f_code.co_name} Passed")
            TCFG.is_passed = True

    def test_023_BEST_많이_검색한(self):
        try:
            ### BEST 탭 ###
            ## 많이 클릭한 탭
            self.hl_and_interact(By.XPATH, '//*[@class="icon-tab__button"]/..//*[text()="많이 검색한"]')  # 많이 검색한 탭 클릭
            sleep(2)

            ## 많이 검색한 탭 > 인기 키워드 탭
            try:
                self.hl_and_interact(By.XPATH, '//*[@class="txtTip"]/..//*[text()="{}"]'.format(datetime.now().strftime('%m.%d %H:%M')), click=False)  # 현재 날짜 시간 기준 노출 확인
                print(datetime.now().strftime('%m.%d %H:%M'))
            except:
                before_one_minute = datetime.now() - relativedelta(minutes=1)  # 현재 시간 기준 1분 전 구하기
                self.hl_and_interact(By.XPATH, '//*[@class="txtTip"]/..//*[text()="{}"]'.format(before_one_minute.strftime('%m.%d %H:%M')), click=False)  # 현재 날짜 시간 기준 노출 확인
                print(before_one_minute.strftime('%m.%d %H:%M'))

            self.hl_and_interact(By.XPATH, '(//*[@class="tag__number"])[1]/..//*[text()="1"]', click=False)  # 랭킹 1 노출 확인
            self.hl_and_interact(By.XPATH, '(//*[@class="tag__number"])[2]/..//*[text()="2"]', click=False)  # 랭킹 2 노출 확인
            self.hl_and_interact(By.XPATH, '(//*[@class="prodCardBody"]/..//*[@class="prodMedia"]/..//*[contains(@src, "https://images-kr.amoremall.com/products/")])[1]', click=False)  # 랭킹 1 첫 번째 상품 노출 확인
            self.hl_and_interact(By.XPATH, '//*[text()="인기 브랜드"]')  # 인기 브랜드 탭 선택

            ## 많이 검색한 탭 > 인기 브랜드 탭
            self.hl_and_interact(By.XPATH, '(//*[@class="tag__number"])[1]/..//*[text()="1"]', click=False)  # 랭킹 1 노출 확인
            self.hl_and_interact(By.XPATH, '(//*[@class="tag__number"])[2]/..//*[text()="2"]', click=False)  # 랭킹 2 노출 확인
            self.hl_and_interact(By.XPATH, '(//*[@class="imgBox"]/..//*[contains(@src, "https://images-kr.amoremall.com/fileupload/brand/")])[1]', click=False)  # 랭킹 1 브랜드 로고 이미지 확인
            self.hl_and_interact(By.XPATH, '(//*[@class="imgBox"]/..//*[contains(@src, "https://images-kr.amoremall.com/fileupload/brand/")])[2]', click=False)  # 랭킹 2 브랜드 로고 이미지 확인
            try:
                self.hl_and_interact(By.XPATH, '(//*[@class="rank__btn"])[1]//*[@class="btnProdLike on"]', click=False)  # 랭킹 1 좋아요 on 상태 확인
            except:
                self.hl_and_interact(By.XPATH, '(//*[@class="rank__btn"])[1]//*[@class="btnProdLike"]', click=False)  # 랭킹 1 좋아요 off 상태 확인
        except:
            capture_screen(self, TCFG)
            self.assertEqual(0, 1)
            print("Failed")
        else:
            print(f"{sys._getframe(0).f_code.co_name} Passed")
            TCFG.is_passed = True
