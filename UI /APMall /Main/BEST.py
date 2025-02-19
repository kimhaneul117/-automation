    def test_024_BEST_많이_구매한(self):
        try:
            ### 홈 ###
            self.interact_by_xpath('//*[@text="BEST"]')  # BEST 탭 클릭

            ### BEST 탭 ###
            ## 많이 구매한 탭
            self.interact_by_id('com.amorepacific.amorepacificmall:id/best_tab', click=False)  # BEST 랭킹 탭 영역 확인
            self.interact_by_xpath('//*[@text="많이 구매한"][@selected="true"]', click=False)  # 많이 구매한 탭 활성화 상태 확인
            self.interact_by_xpath('//android.widget.TextView[@text="일간"]', click=False)  # 일간 선택 확인
            self.interact_by_xpath('(//android.widget.LinearLayout/android.view.ViewGroup[2])[1]', click=False)  # 초기화 버튼 확인
            self.interact_by_xpath('//android.widget.TextView[@text="카테고리"]', click=False)  # 카테고리 선택 확인

            # 계정별 회원 정보 기반으로 연령대 자동 세팅 및 활성화 상태 확인
            if TCFG.port == '2009':
                self.interact_by_xpath('//*[@text="20대 이하"][@selected="true"]', click=False)  # 20대 이하 확인
            if TCFG.port == '2001':
                self.interact_by_xpath('//*[@text="30대"][@selected="true"]', click=False)  # 30대 확인
            if TCFG.port == '7778':
                self.interact_by_xpath('//*[@text="40대"][@selected="true"]', click=False)  # 40대 확인
            if TCFG.port == '2023':
                self.interact_by_xpath('//*[@text="40대"][@selected="true"]', click=False)  # 40대 확인

            self.interact_by_xpath('//android.widget.TextView[@text="브랜드"]', click=False)  # 브랜드 선택 확인
        except:
            self.capture_screen()
            self.assertEqual(0, 19)
        else:
            print(f"{sys._getframe(0).f_code.co_name} Passed")
            TCFG.is_passed = True

    def test_025_BEST_많이_클릭한(self):
        try:
            ### BEST 탭 ###
            self.interact_by_xpath('//*[@resource-id="com.amorepacific.amorepacificmall:id/radio_image"]/..//*[@text="많이 클릭한"]')  # 많이 클릭한 탭 선택

            ## 많이 클릭한 탭
            self.interact_by_xpath('//*[@text="많이 클릭한"][@selected="true"]', click=False)  # 많이 클릭한 탭 활성화 상태 확인
            self.interact_by_xpath('//android.widget.TextView[@text="카테고리"]')  # 카테고리 선택

            ## 카테고리 필터 상세
            self.interact_by_xpath('//android.widget.LinearLayout[1]//*[@text="클렌징"]')  # 클렌징 선택
            self.interact_by_xpath('//*[@text="클렌징"][@selected="true"]', click=False)  # 클렌징 카테고리 활성화 상태 확인
            self.interact_by_id('com.amorepacific.amorepacificmall:id/tv_confirm')  # 적용하기 클릭

            ## 많이 클릭한 탭
            self.interact_by_xpath('(//android.widget.LinearLayout/android.view.ViewGroup[1])[2]', click=False)  # 초기화 버튼 유지 확인
            self.interact_by_xpath('//android.view.ViewGroup[4]//android.widget.TextView[@text="브랜드"]')  # 브랜드 선택

            ## 브랜드 필터 상세
            # 말줄임 처리 width 사이즈 기준으로 처리되므로 특정 단말 브랜드 4개까지 선택 후 말줄임 처리 검증 진행
            if TCFG.dname == 'Galaxy S23':
                # 브랜드명 순서대로 4개 저장
                brand_1 = self.get_attri('(//*[@resource-id="com.amorepacific.amorepacificmall:id/tv_item"])[1]', 'text', By.XPATH)
                brand_2 = self.get_attri('(//*[@resource-id="com.amorepacific.amorepacificmall:id/tv_item"])[2]', 'text', By.XPATH)
                brand_3 = self.get_attri('(//*[@resource-id="com.amorepacific.amorepacificmall:id/tv_item"])[3]', 'text', By.XPATH)
                brand_4 = self.get_attri('(//*[@resource-id="com.amorepacific.amorepacificmall:id/tv_item"])[4]', 'text', By.XPATH)
                brand_total = [brand_1, brand_2, brand_3, brand_4]
                return_brand = ','.join(brand_total)
                self.interact_by_xpath('(//*[@resource-id="com.amorepacific.amorepacificmall:id/tv_item"])[4]')  # 네 번째 브랜드 선택
            else:
                # 브랜드명 순서대로 3개 저장
                brand_1 = self.get_attri('(//*[@resource-id="com.amorepacific.amorepacificmall:id/tv_item"])[1]', 'text', By.XPATH)
                brand_2 = self.get_attri('(//*[@resource-id="com.amorepacific.amorepacificmall:id/tv_item"])[2]', 'text', By.XPATH)
                brand_3 = self.get_attri('(//*[@resource-id="com.amorepacific.amorepacificmall:id/tv_item"])[3]', 'text', By.XPATH)
                brand_total = [brand_1, brand_2, brand_3]
                return_brand = ','.join(brand_total)

            self.interact_by_xpath('(//*[@resource-id="com.amorepacific.amorepacificmall:id/tv_item"])[1]')  # 첫 번째 브랜드 선택
            self.interact_by_xpath('(//*[@resource-id="com.amorepacific.amorepacificmall:id/tv_item"])[2]')  # 두 번째 브랜드 선택
            self.interact_by_xpath('(//*[@resource-id="com.amorepacific.amorepacificmall:id/tv_item"])[3]')  # 세 번째 브랜드 선택
            self.interact_by_id('com.amorepacific.amorepacificmall:id/tv_confirm')  # 적용하기 클릭

            # # 필터 설정 시 선택된 브랜드명 띄어쓰기 포함 최대 10글자까지 노출 후 말줄임 처리
            # return_abb = return_brand[0:10] + '...'
            # return_brand, return_abb = return_abb, return_brand

            ## 많이 클릭한 탭
            self.interact_by_xpath('//android.widget.TextView[@text="클렌징"][@selected="true"]', click=False)  # 카테고리 클렌징 선택 확인

            # 계정별 회원 정보 기반으로 연령대 자동 세팅 및 활성화 상태 확인
            if TCFG.port == '2009':
                self.interact_by_xpath('//*[@text="20대 이하"][@selected="true"]', click=False)  # 20대 이하 확인
            if TCFG.port == '2001':
                self.interact_by_xpath('//*[@text="30대"][@selected="true"]', click=False)  # 30대 확인
            if TCFG.port == '7778':
                self.interact_by_xpath('//*[@text="40대"][@selected="true"]', click=False)  # 40대 확인
            if TCFG.port == '2023':
                self.interact_by_xpath('//*[@text="40대"][@selected="true"]', click=False)  # 40대 확인

            self.interact_by_xpath('//*[@text="{}"][@selected="true"]'.format(return_brand), click=False)  # 브랜드 > 브랜드명1,브랜드명2,브랜드명3... 선택 확인

            try:
                self.interact_by_xpath('//android.widget.TextView[@text="{}"]'.format(datetime.now().strftime('%m.%d %H:%M 기준')), click=False)  # 현재 날짜 시간 기준 노출 확인
            except:
                after_one_minute = datetime.now() - relativedelta(minutes=1)  # 현재 시간 기준 1분 전 구하기
                self.interact_by_xpath('//android.widget.TextView[@text="{}"]'.format(after_one_minute.strftime('%m.%d %H:%M 기준')), click=False)  # 현재 날짜 시간 기준 노출 확인

            self.interact_by_xpath('(//*[@resource-id="com.amorepacific.amorepacificmall:id/product_img"])[1]', click=False)  # 첫 번째 상품 이미지 확인
            self.interact_by_xpath('(//android.widget.LinearLayout/android.view.ViewGroup[1])[2]')  # 초기화 선택
            sleep(1)

            # 3개 필터 설정 초기화 상태 확인
            self.interact_by_xpath('//android.widget.TextView[@text="카테고리"][@selected="false"]', click=False)  # 카테고리 초기화 상태 확인
            self.interact_by_xpath('//android.widget.TextView[@text="연령대"][@selected="false"]', click=False)  # 연령대 초기화 상태 확인
            self.interact_by_xpath('//android.widget.TextView[@text="브랜드"][@selected="false"]', click=False)  # 브랜드 초기화 상태 확인
            self.interact_by_xpath('(//*[@resource-id="com.amorepacific.amorepacificmall:id/product_img"])[1]', click=False)  # 첫 번째 상품 이미지 확인 (APM-45780)
        except:
            self.capture_screen()
            self.assertEqual(0, 21)
        else:
            print(f"{sys._getframe(0).f_code.co_name} Passed")
            TCFG.is_passed = True

    def test_026_BEST_많이_검색한(self):
        try:
            ### BEST 탭 ###
            ## 많이 클릭한 탭
            self.interact_by_xpath('//*[@resource-id="com.amorepacific.amorepacificmall:id/radio_image"]/..//*[@text="많이 검색한"]')  # 많이 검색한 탭 선택

            ## 많이 검색한 탭 > 인기 키워드 탭
            try:
                self.interact_by_xpath('//android.widget.TextView[@text="{}"]'.format(datetime.now().strftime('%m.%d %H:%M 기준')), click=False)  # 현재 날짜 시간 기준 노출 확인
            except:
                after_one_minute = datetime.now() - relativedelta(minutes=1)  # 현재 시간 기준 1분 전 구하기
                self.interact_by_xpath('//android.widget.TextView[@text="{}"]'.format(after_one_minute.strftime('%m.%d %H:%M 기준')), click=False)  # 현재 날짜 시간 기준 노출 확인
            self.interact_by_xpath('(//*[@resource-id="com.amorepacific.amorepacificmall:id/best_brand_ranking"])[1]/..//*[@text="1"]', click=False)  # 랭킹 1 노출 확인
            self.interact_by_xpath('(//*[@resource-id="com.amorepacific.amorepacificmall:id/best_brand_ranking"])[2]/..//*[@text="2"]', click=False)  # 랭킹 2 노출 확인
            self.interact_by_xpath('(//*[@resource-id="com.amorepacific.amorepacificmall:id/product"])[1]', click=False)  # 랭킹 1 첫 번째 상품 노출 확인
            self.interact_by_xpath('//*[@text="인기 브랜드"]')  # 인기 브랜드 탭 선택

            ## 많이 검색한 탭 > 인기 브랜드 탭
            self.interact_by_xpath('(//*[@resource-id="com.amorepacific.amorepacificmall:id/best_brand_ranking"])[1]/..//*[@text="1"]', click=False)  # 랭킹 1 노출 확인
            self.interact_by_xpath('(//*[@resource-id="com.amorepacific.amorepacificmall:id/best_brand_ranking"])[2]/..//*[@text="2"]', click=False)  # 랭킹 2 노출 확인
            self.interact_by_xpath('(//*[@resource-id="com.amorepacific.amorepacificmall:id/best_brand_logo"])[1]', click=False)  # 랭킹 1 브랜드 로고 이미지 확인
            self.interact_by_xpath('(//*[@resource-id="com.amorepacific.amorepacificmall:id/best_brand_logo"])[2]', click=False)  # 랭킹 2 브랜드 로고 이미지 확인
            self.interact_by_xpath('(//*[@resource-id="com.amorepacific.amorepacificmall:id/iv_like"])[1]', click=False)  # 랭킹 1 좋아요 아이콘 노출 확인
        except:
            self.capture_screen()
            self.assertEqual(0, 21)
        else:
            print(f"{sys._getframe(0).f_code.co_name} Passed")
            TCFG.is_passed = True

    def test_027_BEST_피부에_맞는(self):
        try:
            ### BEST 탭 ###
            ## 많이 검색한 탭
            self.interact_by_xpath('//*[@resource-id="com.amorepacific.amorepacificmall:id/radio_image"]/..//*[@text="피부에 맞는"]')  # 피부에 맞는 탭 선택
            # 회원, 피부 고민 설정 = Y

            ## 피부에 맞는 탭
            self.interact_by_xpath('(//*[@resource-id="com.amorepacific.amorepacificmall:id/ranking_tag"])[1]/..//*[@text="1"]', click=False)  # 첫 번째 상품 번호 1 텍스트 확인
            self.interact_by_xpath('(//*[@resource-id="com.amorepacific.amorepacificmall:id/ranking_tag"])[2]/..//*[@text="2"]', click=False)  # 두 번째 상품 번호 2 텍스트 확인
        except:
            self.capture_screen()
            self.assertEqual(0, 21)
        else:
            print(f"{sys._getframe(0).f_code.co_name} Passed")
            TCFG.is_passed = True

    def test_028_BEST_좋아요_확인(self):
        try:
            ### BEST 탭 ###
            ## 피부에 맞는 탭
            best_prd = self.get_attri('(//*[@resource-id="com.amorepacific.amorepacificmall:id/tv_product_name"])[1]', 'text', By.XPATH)  # BEST 첫 번째 상품 > 이름 저장
            self.interact_by_xpath('(//android.view.View[@resource-id="com.amorepacific.amorepacificmall:id/view_overlay"])[1]')  # 첫번째 상품 클릭
            sleep(3)

            ### BEST 상품 상세 ###
            self.interact_by_xpath('//*[@text="좋아요"]')  # 좋아요 버튼 클릭
            TCFG.driver.back()  # BEST 상품 상세 > BEST 탭으로 이동

            ### BEST 탭 ###
            self.interact_by_id('com.amorepacific.amorepacificmall:id/iv_bottom_history_icon')  # 하단 액션바 히스토리 클릭

            ### 쇼핑 히스토리 화면 ###
            TCFG.driver.swipe(TCFG.res[0] * 0.5, TCFG.res[1] * 0.5, TCFG.res[0] * 0.5, TCFG.res[1] * 0.2)  # 밑으로 조금 이동
            sleep(1.5)

            # 쇼핑 히스토리 > BEST 첫 번째 상품 존재 여부 확인
            self.interact_by_xpath('//android.widget.TextView[contains(@text, "{}")]'.format(best_prd), click=False)
        except:
            self.capture_screen()
            self.assertEqual(0, 22)
        else:
            print(f"{sys._getframe(0).f_code.co_name} Passed")
            TCFG.is_passed = True

    def test_029_BEST_좋아요_취소(self):
        try:
            ### 쇼핑 히스토리 화면 ###
            like_count = self.get_attri('com.amorepacific.amorepacificmall:id/total_count_text', 'text', By.ID).split('개')  # 'n개의 좋아요 상품이 있습니다.' n 저장
            self.interact_by_xpath('(//*[@resource-id="com.amorepacific.amorepacificmall:id/iv_like"])[1]')  # 첫 번째 상품 좋아요 취소
            
            # 기존 좋아요 상품 2개 이상인 경우
            try:
                self.interact_by_xpath('//android.widget.TextView[@text="{}개의 좋아요 상품이 있습니다."]'.format(int(like_count[0])-1), click=False)  # 좋아요 상품 갯수 -1 확인
            # 기존 좋아요 상품 1개인 경우
            except:
                self.interact_by_xpath('//android.widget.TextView[@text="아직 좋아요 한 상품이 없습니다."]', click=False)  # 좋아요한 상품이 없음을 안내하는 문구 노출 확인
        except:
            self.capture_screen()
            self.assertEqual(0, 23)
        else:
            print(f"{sys._getframe(0).f_code.co_name} Passed")
            TCFG.is_passed = True
        finally:
            self.interact_by_id('com.amorepacific.amorepacificmall:id/ib_bottom_home')  # 하단 액셕바 홈 버튼 클릭

    def test_030_BEST_공유하기(self):
        try:
            ### 홈 ###
            self.interact_by_xpath('//*[@text="BEST"]')  # BEST 탭 클릭

            ### BEST 탭 ###
            ## 많이 구매한 탭
            self.interact_by_xpath('(//android.view.View[@resource-id="com.amorepacific.amorepacificmall:id/view_overlay"])[2]')  # 두 번째 상품 클릭

            ### 상품 상세 화면 ###
            prod_name = self.get_attri('(//android.view.View)[1]', 'text', By.XPATH)
            print(prod_name)
            self.interact_by_xpath('//android.view.View[1]/android.widget.Button')  # 공유하기 버튼 클릭
            sleep(1.5)

            ### 공유하기 레이어 팝업 ###
            self.interact_by_xpath('//android.widget.TextView[contains(@text, "{}")]'.format(prod_name), click=False)  # 상품명 일치 확인
            TouchAction(TCFG.driver).tap(None, 550, 124, 1).perform()  # 터치로 공유창 닫기
        except:
            self.capture_screen()
            self.assertEqual(0, 24)
        else:
            print(f"{sys._getframe(0).f_code.co_name} Passed")
            TCFG.is_passed = True
        finally:
            TCFG.driver.back()  # BEST 탭으로 이동
