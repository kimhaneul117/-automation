    def test_021_쇼핑_히스토리_최근(self):
        try:
            self.interact_by_id('com.amorepacific.amorepacificmall:id/iv_bottom_history_icon')  # 히스토리로 이동

            ### 쇼핑 히스토리 화면 ###
            self.interact_by_xpath('//android.widget.TextView[@text="최근 본 상품"]', click=False)  # 최근 본 상품 텍스트 확인
            self.interact_by_id('com.amorepacific.amorepacificmall:id/title_arrow')  # 펼치기 클릭

            # 최근 본 상품 있는 경우 > 첫 번째 기록 대상 검증
            try:
                # 브랜드일 경우
                if self.is_element_present('//androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[1]'
                                           '//*[@resource-id="com.amorepacific.amorepacificmall:id/contents_tag"][@text="브랜드"]', By.XPATH):
                    self.interact_by_xpath('(//*[@resource-id="com.amorepacific.amorepacificmall:id/item_image"])[1]', click=False)  # 브랜드 이미지 확인
                    self.interact_by_xpath('(//*[@resource-id="com.amorepacific.amorepacificmall:id/contents_tag"][@text="브랜드"])[1]')  # 첫 번째 브랜드 클릭
                    sleep(2)

                    ### 브랜드 메인 ###
                    self.interact_by_xpath('//android.webkit.WebView[contains(@text,"브랜드관")]', click=False)  # 브핸드관 진입 확인
                    TCFG.driver.back()  # 뒤로 가기 > 최근 본 상품으로 이동

                # 검색어일 경우
                elif self.is_element_present('//androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[1]'
                                           '//*[@resource-id="com.amorepacific.amorepacificmall:id/search_keyword"]', By.XPATH):
                    keyword = TCFG.driver.find_element_by_xpath('(//*[@resource-id="com.amorepacific.amorepacificmall:id/search_keyword"])[1]').text  # 검색어 저장
                    self.interact_by_xpath('(//*[@resource-id="com.amorepacific.amorepacificmall:id/search_keyword"])[1]')  # 검색어 클릭

                    ### 검색 결과 화면 ###
                    self.interact_by_xpath('//*[@resource-id="com.amorepacific.amorepacificmall:id/tv_search_header_search_bar"][@text="{}"]'.format(keyword), click=False)  # 헤더 검색바 키워드 일치 확인
                    self.interact_by_xpath('(//*[@resource-id="com.amorepacific.amorepacificmall:id/iv_prd_img"])[1]', click=False)  # 첫 번째 상품 이미지 노출 확인
                    self.interact_by_id('com.amorepacific.amorepacificmall:id/btn_back')  # 헤더 뒤로 가기 버튼 클릭

                # 상품일 경우
                elif self.is_element_present('//androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[1]'
                                           '//*[@resource-id="com.amorepacific.amorepacificmall:id/contents_sub_title"][contains(@text,"00원")]', By.XPATH):  # 상품인 경우
                    self.interact_by_xpath('(//*[@resource-id="com.amorepacific.amorepacificmall:id/item_image"])[1]', click=False)  # 첫 번째 상품 이미지 노출 확인
                    self.interact_by_xpath('(//*[@resource-id="com.amorepacific.amorepacificmall:id/cart_icon"])[1]', click=False)  # 장바구니 확인
                    self.interact_by_xpath('(//*[@resource-id="com.amorepacific.amorepacificmall:id/item_layout"])[1]')  # 첫 번째 상품 클릭

                    ### 상품 상세 화면 ###
                    self.interact_by_xpath('//android.widget.Button[@text="구매하기"]', click=False)  # 장바구니 버튼 확인
                    self.interact_by_xpath('//android.widget.Button[@text="뒤로가기"]')  # 헤더 뒤로 가기 버튼 클릭

                ### 최근 본 상품 화면 ###
                self.interact_by_id('com.amorepacific.amorepacificmall:id/tv_edit')  # 편집 클릭

                # 편집 기능 검증
                delete_before = TCFG.driver.find_element_by_xpath('//androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[1]')  # 첫 번째 히스토리 text 저장
                self.interact_by_xpath('(//*[@resource-id="com.amorepacific.amorepacificmall:id/delete_button"])[1]')  # 첫 번째 히스토리 내역 개별 삭제
                delete_after = TCFG.driver.find_element_by_xpath('//androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[1]')  # 첫 번째 히스토리 text 저장

                # 첫 번째 히스토리 내역 삭제 전후 비교 검증
                if delete_before is not delete_after:
                    pass
                else:
                    raise AssertionError("첫 번째 히스토리 내역 삭제 전후 비교 검증 fail 발생")

                self.interact_by_id('com.amorepacific.amorepacificmall:id/tv_del_all')  # 전체 삭제 버튼 클릭
                self.interact_by_id('com.amorepacific.amorepacificmall:id/bt_right')  # 최근 본 내역을 모두 삭제하시겠습니까? 팝업 삭제 버튼 클릭
                self.interact_by_id('com.amorepacific.amorepacificmall:id/history_shopping_empty_text', click=False)  # '최근 본 내역이 없습니다' 문구 노출 확인
                self.interact_by_id('com.amorepacific.amorepacificmall:id/floating_btn')  # 쇼핑 히스토리 닫기
            # 최근 본 상품이 없는 경우
            except:
                self.interact_by_id('com.amorepacific.amorepacificmall:id/history_shopping_empty_text', click=False)  # '최근 본 내역이 없습니다' 문구 노출 확인
        except:
            self.capture_screen()
            self.assertEqual(0, 18)
        else:
            print(f"{sys._getframe(0).f_code.co_name} Passed")
            TCFG.is_passed = True
        finally:
            self.interact_by_id('com.amorepacific.amorepacificmall:id/ib_bottom_history')  # 최근 히스토리가 없는 상태 > 하단 액션바 쇼핑 히스토리 재진입

    def test_022_쇼핑_히스토리_좋아요(self):
        try:
            ### 쇼핑 히스토리 화면 ###
            if TCFG.environment == 'PRD':
                self.interact_by_xpath('//*[@resource-id="com.amorepacific.amorepacificmall:id/title_text"][@text="{}님의 ♥︎LIKE"]'.format(TCFG.name), click=False)  # 좋아요 영역 타이틀 노출 확인
            if TCFG.environment == 'STG':
                self.interact_by_xpath('//*[@resource-id="com.amorepacific.amorepacificmall:id/title_text"][contains(@text,"님의 ♥︎LIKE")]', click=False)  # 좋아요 영역 타이틀 노출 확인

            self.interact_by_xpath('//android.widget.LinearLayout[@content-desc="좋아요"]/android.widget.TextView[@selected="true"]', click=False)  # 좋아요 탭 디폴트 활성화 확인

            # 밑으로 조금 이동
            TCFG.driver.swipe(TCFG.res[0] * 0.5, TCFG.res[1] * 0.5, TCFG.res[0] * 0.5, TCFG.res[1] * 0.2)

            # 로그인 상태 > 좋아요 상품 있는 경우
            try:
                self.interact_by_xpath('//*[@resource-id="com.amorepacific.amorepacificmall:id/total_count_text"][contains(@text,"개의 좋아요 상품이 있습니다.")]', click=False)  # 좋아요 상품 개수 표기 영역 확인
                # self.interact_by_id('com.amorepacific.amorepacificmall:id/order_button', click=False)  # 좋아요 상품 정렬 확인
                self.interact_by_xpath('(//*[@resource-id="com.amorepacific.amorepacificmall:id/product_img"])[1]', click=False)  # 첫 번째 상품 이미지 확인
                self.interact_by_xpath('(//*[@resource-id="com.amorepacific.amorepacificmall:id/iv_like"][@index="2"])', click=False)  # 좋아요 아이콘 on 상태 확인

                # 기존 장바구니 상품 1개 이상일 경우
                if self.is_element_present('com.amorepacific.amorepacificmall:id/cart_badge_icon', By.ID):
                    cart_badge_icon = TCFG.driver.find_element_by_id('com.amorepacific.amorepacificmall:id/cart_badge_icon').text  # 현재 장바구니 상품 개수 저장
                # 기존 장바구니 상품 없는 경우
                else:
                    cart_badge_icon = 0

                scroll_xpath(self, '(//android.widget.TextView[@text="장바구니 담기"])[1]', loc=TCFG.res[1] * 0.9, y1=TCFG.res[1] * 0.7, y2=TCFG.res[1] * 0.5)  # 첫 번째 상품 장바구니 담기 버튼 클릭
                sleep(2)

                # 하나의 단위 상품인 경우
                if self.is_element_present('(//android.widget.TextView[@text="장바구니 담기"])[1]', By.XPATH):  # 화면 이동 되지 않음 확인
                    try:
                        self.interact_by_xpath('//*[@resource-id="com.amorepacific.amorepacificmall:id/cart_badge_icon"][@text="{}"]'.format(int(cart_badge_icon)+1), click=False)  # 장바구니 수량 증가 확인

                    # 기존 장바구니 상품과 중복인 경우 > 장바구니 수량 텍스트 증가하지 않음
                    except:
                        prodname = TCFG.driver.find_element_by_xpath('(//*[@resource-id="com.amorepacific.amorepacificmall:id/tv_product_name"])[1]').text
                        prodname_1 = prodname.split()

                        # 상품명 뒤에 두마디 자르기 (간헐적으로 상이한 단어 발생으로 일부 단어만 검증)
                        for replace_text in prodname_1:
                            if int(replace_text in prodname) and len(prodname.partition(replace_text)[0]) > \
                                    len(prodname.partition(replace_text)[2]):
                                prodname = prodname.partition(replace_text)[0]
                                prodname = prodname.strip()
                        print(prodname)

                        self.interact_by_id('com.amorepacific.amorepacificmall:id/header_cart_button_image_view')  # 헤더 영역 장바구니 진입
                        sleep(2)

                        ### 장바구니 화면 ###
                        self.interact_by_xpath('//android.view.View[contains(@content-desc,"{}")]'.format(prodname), click=False)  # 첫 번째 좋아요 상품과 일치 확인

                        # 해당 상품 장바구니 수량 2개 이상 확인
                        cart_prodcount = TCFG.driver.find_element_by_xpath('//android.view.View[contains(@content-desc,"{}")]'
                                                                           '/android.view.View[2]/android.widget.TextView[3]'.format(prodname)).text

                        if int(cart_prodcount) >= 2:
                            pass
                        else:
                            AssertionError('기존 장바구니 좋아요 상품 있는 상태 > 장바구니 담기 동작 fail 발생')

                        self.interact_by_xpath('//android.widget.Button[@text="닫기"]')  # 장바구니 [X]버튼 클릭
                # 복수 개의 단위 상품인 경우
                elif self.is_element_present('//android.widget.Button[@text="상품을 선택해주세요"]', By.XPATH):  # 상품 상세로 이동 및 옵션 선택 레이어 디폴트 오픈 상태 확인
                    TCFG.driver.back()   # 쇼핑히스토리 좋아요 영역으로 이동
                # 장바구니 담기가 불가한 상태
                elif self.is_element_present('//android.widget.Button[@text="재입고 알림 신청"]', By.XPATH):  # 상품 상세로 이동 및 재입고 알림 신청 상태 확인
                    TCFG.driver.back()   # 쇼핑히스토리 좋아요 영역으로 이동
            # 로그인 상태 > 좋아요 상품 없는 경우
            except:
                self.interact_by_xpath('//android.widget.TextView[@text="아직 좋아요 한 상품이 없습니다."]', click=False)  # 좋아요한 상품이 없음을 안내하는 문구 노출 확인
                self.interact_by_xpath('//android.widget.TextView[@text="지금 많이 찾는 상품 보러가기"]')  # 추천 버튼 클릭

                ### BEST 탭 ###
                self.interact_by_xpath('//android.widget.TextView[@text="많이 클릭한"]', click=False)  # BEST 탭 카테고리 확인
                self.interact_by_id('com.amorepacific.amorepacificmall:id/iv_bottom_history')  # 하단 액션바 > 쇼핑 히스토리 진입

            self.interact_by_xpath('//android.widget.LinearLayout[@content-desc="자주구매"]')  # 자주 구매 탭 클릭

            ## 자주 구매 탭 ##
            # 자주 구매 상품이 있는 경우
            try:
                self.interact_by_xpath('(//*[@resource-id="com.amorepacific.amorepacificmall:id/product_img"])[1]', click=False)  # 첫 번째 상품 이미지 확인

                ## 자주 구매한 상품 1개인 경우
                if not self.is_element_present('(//*[@resource-id="com.amorepacific.amorepacificmall:id/product_img"])[2]', By.XPATH):
                    purchase_1 = TCFG.driver.find_element_by_xpath('(//android.widget.TextView[@resource-id="com.amorepacific.amorepacificmall:id/product_tag"])[1]').text.split("회")
                    prodname_1 = TCFG.driver.find_element_by_xpath('(//*[@resource-id="com.amorepacific.amorepacificmall:id/tv_product_name"])[1]').text
                    pshop = "[p]"

                    if int(purchase_1[0]) >= 2:  # 2회 이상 구매 확인
                        pass
                    else:
                        raise AssertionError("자주 구매한 상품 구매 횟수 fail 발생")

                    if prodname_1 in pshop:  # 상품명 퍼시픽샵([P]) 미포함 확인
                        raise AssertionError("자주 구매한 상품 p샵 포함으로 fail 발생")
                ## 자주 구매한 상품 2개 이상인 경우
                else:
                    # 자주 구매한 상품 구매 횟수 저장(2개까지)
                    purchase_1 = TCFG.driver.find_element_by_xpath('(//android.widget.TextView[@resource-id="com.amorepacific.amorepacificmall:id/product_tag"])[1]').text.split("회")
                    purchase_2 = TCFG.driver.find_element_by_xpath('(//android.widget.TextView[@resource-id="com.amorepacific.amorepacificmall:id/product_tag"])[2]').text.split("회")
                    # 자주 구매한 상품명 저장(2개까지)
                    prodname_1 = TCFG.driver.find_element_by_xpath('(//*[@resource-id="com.amorepacific.amorepacificmall:id/tv_product_name"])[1]').text
                    prodname_2 = TCFG.driver.find_element_by_xpath('(//*[@resource-id="com.amorepacific.amorepacificmall:id/tv_product_name"])[2]').text
                    pshop = "[p]"

                    if int(purchase_1[0] and purchase_2[0]) >= 2:  # 2회 이상 구매 확인
                        int(purchase_1[0] >= purchase_2[0])  # 구매 횟수 높은 순으로 정렬 확인
                        pass
                    else:
                        raise AssertionError("자주 구매한 상품 구매 횟수 fail 발생")

                    if prodname_1 and prodname_2 in pshop:  # 상품명 퍼시픽샵([P]) 미포함 확인
                        raise AssertionError("자주 구매한 상품 p샵 포함으로 fail 발생")

                # 기존 장바구니 상품 1개 이상일 경우
                if self.is_element_present('com.amorepacific.amorepacificmall:id/cart_badge_icon', By.ID):
                    cart_badge_icon = TCFG.driver.find_element_by_id('com.amorepacific.amorepacificmall:id/cart_badge_icon').text  # 현재 장바구니 상품 개수 저장
                # 기존 장바구니 상품 없는 경우
                else:
                    cart_badge_icon = 0

                scroll_xpath(self, '(//android.widget.TextView[@text="장바구니 담기"])[1]', loc=TCFG.res[1] * 0.9, y1=TCFG.res[1] * 0.7, y2=TCFG.res[1] * 0.5)  # 첫 번째 상품 장바구니 담기 버튼 클릭

                # 하나의 단위 상품인 경우
                if self.is_element_present('(//android.widget.TextView[@text="장바구니 담기"])[1]', By.XPATH):  # 화면 이동 되지 않음 확인
                    try:
                        self.interact_by_xpath('//*[@resource-id="com.amorepacific.amorepacificmall:id/cart_badge_icon"][@text="{}"]'.format(int(cart_badge_icon) + 1), click=False)  # 장바구니 수량 증가 확인
                    # 기존 장바구니 상품과 중복인 경우 > 장바구니 수량 텍스트 증가하지 않음
                    except:
                        prodname = TCFG.driver.find_element_by_xpath('(//*[@resource-id="com.amorepacific.amorepacificmall:id/tv_product_name"])[1]').text
                        prodname_1 = prodname.split()

                        # 상품명 뒤에 두마디 자르기 (간헐적으로 상이한 단어 발생으로 일부 단어만 검증)
                        for replace_text in prodname_1:
                            if int(replace_text in prodname) and len(prodname.partition(replace_text)[0]) > \
                                    len(prodname.partition(replace_text)[2]):
                                prodname = prodname.partition(replace_text)[0]
                                prodname = prodname.strip()
                        print(prodname)

                        self.interact_by_id('com.amorepacific.amorepacificmall:id/header_cart_button_image_view')  # 헤더 영역 장바구니 진입
                        sleep(2)

                        ### 장바구니 화면 ###
                        self.interact_by_xpath('//android.view.View[contains(@content-desc,"{}")]'.format(prodname), click=False)  # 첫 번째 좋아요 상품과 일치 확인
                        cart_prodcount = TCFG.driver.find_element_by_xpath('//android.view.View[contains(@content-desc,"{}")]'
                                                                           '/android.view.View[2]/android.widget.TextView[3]'.format(prodname)).text  # 장바구니 수량 저장
                        # 해당 상품 장바구니 수량 2개 이상 확인
                        if int(cart_prodcount) >= 2:
                            pass
                        else:
                            AssertionError('기존 장바구니 좋아요 상품 있는 상태 > 장바구니 담기 동작 fail 발생')

                        self.interact_by_xpath('//android.widget.Button[@text="닫기"]')  # 장바구니 [X]버튼 클릭
                # 복수 개의 단위 상품인 경우
                elif self.is_element_present('//android.widget.Button[@text="상품을 선택해주세요"]', By.XPATH):  # 상품 상세로 이동 및 옵션 선택 레이어 디폴트 오픈 상태 확인
                    TCFG.driver.back()  # 쇼핑히스토리 좋아요 영역으로 이동
                # 장바구니 담기가 불가한 상태
                elif self.is_element_present('//android.widget.Button[@text="재입고 알림 신청"]', By.XPATH):  # 상품 상세로 이동 및 재입고 알림 신청 상태 확인
                    TCFG.driver.back()  # 쇼핑히스토리 좋아요 영역으로 이동

            # 자주 구매 상품이 없는 경우
            except:
                self.interact_by_xpath('//android.widget.TextView[@text="자주 구매한 상품이 없습니다."]', click=False)  # 문구 노출 확인

            self.interact_by_xpath('//android.widget.LinearLayout[@content-desc="브랜드"]')  # 브랜드 탭 클릭

            ### 브랜드 탭 ###
            # 좋아요한 브랜드가 있는 경우
            try:
                self.interact_by_xpath('//*[@resource-id="com.amorepacific.amorepacificmall:id/total_count_text"][contains(@text,"개의 좋아요 브랜드가 있습니다.")]', click=False)  # 좋아요 브랜드 개수 표기 영역 확인

                ## 첫 번째 브랜드 대상 검증
                self.interact_by_xpath('(//*[@resource-id="com.amorepacific.amorepacificmall:id/brand_logo"])[1]', click=False)  # 브랜드 이미지 확인
                self.interact_by_xpath('(//*[@resource-id="com.amorepacific.amorepacificmall:id/brand_name"])[1]', click=False)  # 브랜드명 확인
                self.interact_by_xpath('(//*[@resource-id="com.amorepacific.amorepacificmall:id/like_button"])[1]', click=False)  # 브랜드 좋아요 아이콘 확인
                self.interact_by_xpath('(//*[@resource-id="com.amorepacific.amorepacificmall:id/product_img"])[1]', click=False)  # 브랜드 상품 이미지 확인

                TCFG.driver.swipe(TCFG.res[0] * 0.8, TCFG.res[1] * 0.5, TCFG.res[0] * 0.2, TCFG.res[1] * 0.5)  # 첫 번째 브랜드 대표 상품 좌우로 스크롤
                self.interact_by_xpath('//android.widget.TextView[@text="더 보기"]')  # 더 보기 버튼 클릭
                sleep(2)

                ### 브랜드관 전체 상품 탭 ###
                self.interact_by_xpath('//android.webkit.WebView[contains(@text,"브랜드관")]', click=False)  # 브랜드관 메인 화면 이동 확인
                self.interact_by_xpath('//android.widget.Button[@text="전체"]', click=False)  # 전체 탭 노출 확인
            # 좋아요한 브랜드가 없는 경우
            except:
                self.interact_by_xpath('//android.widget.TextView[@text="아직 좋아요 한 브랜드가 없습니다."]', click=False)  # 좋아요한 브랜드가 없음을 나타내는 문구 노출 확인
                self.interact_by_id('com.amorepacific.amorepacificmall:id/empty_recommend_button')  # 추천 인기 브랜드 보러가기 버튼 클릭

                ### BEST 탭 ###
                self.interact_by_xpath('//android.widget.TextView[@text="인기 브랜드"]', click=False)  # BEST 탭 > 인기 브랜드 탭 확인
        except:
            self.capture_screen()
            self.assertEqual(0, 18)
        else:
            print(f"{sys._getframe(0).f_code.co_name} Passed")
            TCFG.is_passed = True
        finally:
            TCFG.is_finished = True
