def test_006_주문_배송_조회(self):
    try:
        ### 마이파우치 화면 ###
        scroll_id(self, 'com.amorepacific.amorepacificmall:id/ly_order_list', loc=TCFG.res[1] * 0.55, y1=TCFG.res[1] * 0.6, y2=TCFG.res[1] * 0.5)  # 주문/배송 조회 탭 메뉴 클릭

        ### 주문/배송 조회 화면 ###
        sleep(3)
        self.interact_by_xpath('//android.widget.TextView[@text="주문/배송 조회"]', click=False)  # 주문/배송 조회 화면 타이틀 확인
        self.interact_by_xpath('//android.widget.Button[@text="3개월"]', click=False)  # 조회 기간 > 3개월 default 확인
        self.interact_by_xpath('//android.widget.Button[@text="전체"]', click=False)  # 배송 상태 > 전체 default 확인

        # 첫 번째 주문 건 대상 검증 > 주문 내역 = Y, status = 구매 확정 , 리뷰 작성 = Y or N, P샵 = Y or N
        if self.is_element_present('//android.view.View[@text="구매확정"]', By.XPATH):
            self.interact_by_xpath('//*[@text="상세보기"]', click=False)  # 상세 보기 버튼 확인
            if TCFG.environment == 'PRD':  # PRD 환경
                prod = TCFG.driver.find_element_by_xpath('//android.widget.TextView[contains(@text, "아모레퍼시픽 상품")]').text.split(' ')  # 주문 건 상품 갯수 저장

                # 복합 주문
                if len(prod[2].split('개')[1]) > 1:
                    # 주문 건 상품 갯수 만큼 모두 검증
                    for i in range(1, len(prod[2]) + 1):
                        self.interact_by_xpath('(//android.widget.Image)[{}]'.format(i), click=False)  # 상품 이미지 확인
                        self.interact_by_xpath('(//android.widget.Button[@text="장바구니"])[{}]'.format(i), click=False)  # 장바구니 아이콘 확인
                # 단일 주문
                else:
                    self.interact_by_xpath('//android.widget.Image', click=False)  # 상품 이미지 확인
                    self.interact_by_xpath('//android.widget.Button[@text="장바구니"]', click=False)  # 장바구니 아이콘 확인
            elif TCFG.environment == 'STG':  # STG 환경
                prod = TCFG.driver.find_element_by_xpath('//android.widget.TextView[contains(@text, "아모레퍼시픽 상품")]').text.split(' ')  # 주문 건 상품 갯수 저장

                # 복합 주문
                if len(prod[2].split('개')[1]) > 1:
                    # 주문 건 상품 갯수 만큼 모두 검증
                    for i in range(1, len(prod) + 1):
                        self.interact_by_xpath('(//android.widget.Button[@text="장바구니"])[{}]'.format(i), click=False)  # 장바구니 아이콘 확인
                # 단일 주문
                else:
                    self.interact_by_xpath('//android.widget.Button[@text="장바구니"]', click=False)  # 장바구니 아이콘 확인

            # 밑으로 조금 이동
            TCFG.driver.swipe(TCFG.res[0] * 0.5, TCFG.res[1] * 0.5, TCFG.res[0] * 0.5, TCFG.res[1] * 0.2)

            # P샵 상품 and 단일 주문일 경우, 리뷰 버튼 미노출로 예외 처리
            if not self.is_element_present('//android.widget.TextView[1][contains(@text, "[P]")]', By.XPATH) and len(prod) == 1:
                # 리뷰 작성 = Y
                try:
                    self.interact_by_xpath('//android.widget.Button[@text="리뷰확인"]')  # 리뷰 확인 버튼 클릭

                    ### 리뷰 화면 ###
                    self.interact_by_xpath('//*[@text="작성한 리뷰"][@clickable="true"]',  click=False)  # 작성한 리뷰 탭으로 이동 확인
                # 리뷰 작성 = N
                except:
                    self.interact_by_xpath('//android.widget.Button[@text="리뷰작성"]')  # 리뷰 작성 버튼 클릭

                    ### 리뷰 확면 ###
                    self.interact_by_xpath('//*[@text="미작성 리뷰"][@clickable="true"]', click=False)  # 미작성 리뷰 탭으로 이동 확인
                    self.interact_by_xpath('//android.view.View[@content-desc="리뷰 작성"]', click=False)  # 리뷰 작성 버튼 확인

                self.interact_by_id('com.amorepacific.amorepacificmall:id/back_button_image_view')  # gnb 뒤로 가기 > 주문/배송 조회 화면으로 이동

            ### 주문/배송 조회 화면 ###
            delivery_time = TCFG.driver.find_element_by_xpath('//android.widget.TextView[contains(@text,") 배송완료")]').text  # MM월 DD일(day of the week) 배송완료 텍스트 저장
            delivery_time1 = delivery_time.lstrip("0")  # MM 한 자릿수일 경우 '0' 제거
            delivery_time2 = delivery_time1.replace("월 ", "/").replace("일", "").split('\n')  # MM/DD(day of the week) 형태로 변환
            tracking_detail = delivery_time.replace("월 ", "-").replace("일", "").split('\n')  # MM-DD(day of the week) 형태로 변환
            tracking_detail = [f.split("(") for f in tracking_detail]  # 요일과 분리
            scroll_xpath(self, '//android.widget.Button[@text="배송조회"]', loc=TCFG.res[1] * 0.55, y1=TCFG.res[1] * 0.6, y2=TCFG.res[1] * 0.5)  # 배송 조회 버튼 클릭

            ### 배송 조회 화면 ###
            self.interact_by_xpath('//android.widget.TextView[@text="{}"]'.format(delivery_time2[0]), click=False)  # 배송 단계 표시 영역 날짜 + 배송 완료 텍스트 확인
            self.interact_by_xpath('//android.widget.ListView//android.widget.TextView[@text="배송완료"]', click=False)  # 배송 추적 디테일 마지막 상태 배송 완료 노출 확인
            self.interact_by_xpath('//android.widget.ListView/android.view.View[1]/android.widget.TextView[contains(@text,"{}")]'.format((tracking_detail[0])[0]), click=False)  # 주문/배송 조회 화면 배송 완료일과 배송 추척 화면 배송 완료일 일치 확인
            self.interact_by_xpath('//android.widget.Button[@text="뒤로가기"]')  # 좌측 상단 뒤로가기 버튼 클릭
            sleep(2)

            ### 주문/배송 조회 화면 ###
            scroll_xpath(self, '//android.widget.Button[@text="1:1 문의"]', loc=TCFG.res[1] * 0.55, y1=TCFG.res[1] * 0.6, y2=TCFG.res[1] * 0.5, click=False)  # 1:1 문의 버튼 확인
            self.interact_by_xpath('//android.widget.Button[@text="재주문"]', click=False)  # 재주문 버튼 확인
            
        # 첫 번째 주문 건 대상 검증 > 주문 내역 = Y, status = 배송 완료, 구매확정 = N
        elif self.is_element_present('//android.view.View[@text="배송완료"]', By.XPATH):
            self.interact_by_xpath('//*[@text="상세보기"]', click=False)  # 상세 보기 버튼 확인
            if TCFG.environment == 'PRD':  # PRD 환경
                prod = TCFG.driver.find_element_by_xpath('//android.widget.TextView[contains(@text, "아모레퍼시픽 상품")]').text.split(' ')  # 주문 건 상품 갯수 저장

                # 복합 주문
                if len(prod[2].split('개')[1]) > 1:
                    # 주문 건 상품 갯수 만큼 모두 검증
                    for i in range(1, len(prod) + 1):
                        self.interact_by_xpath('(//android.widget.Image)[{}]'.format(i), click=False)  # 상품 이미지 확인
                        self.interact_by_xpath('(//android.widget.Button[@text="장바구니"])[{}]'.format(i), click=False)  # 장바구니 아이콘 확인
                # 단일 주문
                else:
                    self.interact_by_xpath('//android.widget.Image', click=False)  # 상품 이미지 확인
                    self.interact_by_xpath('//android.widget.Button[@text="장바구니"]', click=False)  # 장바구니 아이콘 확인
            elif TCFG.environment == 'STG':  # STG 환경
                prod = TCFG.driver.find_element_by_xpath('//android.widget.TextView[contains(@text, "아모레퍼시픽 상품")]').text.split(' ')  # 주문 건 상품 갯수 저장

                # 복합 주문
                if len(prod[2].split('개')[1]) > 1:
                    # 주문 건 상품 갯수 만큼 모두 검증
                    for i in range(1, len(prod) + 1):
                        self.interact_by_xpath('(//android.widget.Button[@text="장바구니"])[{}]'.format(i), click=False)  # 장바구니 아이콘 확인
                # 단일 주문
                else:
                    self.interact_by_xpath('//android.widget.Button[@text="장바구니"]', click=False)  # 장바구니 아이콘 확인

            self.interact_by_xpath('//android.widget.Button[@text="구매확정"]', click=False)  # 구매 확정 버튼 확인

            # P샵 상품 and 단일 주문일 경우 미노출 예외 처리
            if not self.is_element_present('//android.widget.TextView[1][contains(@text, "[P]")]', By.XPATH) and len(prod) == 1:
                self.interact_by_xpath('//android.widget.TextView[contains(@text,"구매 확정 및 리뷰 작성 시")]', click=False)  # 구매 확정

            # 밑으로 조금 이동
            TCFG.driver.swipe(TCFG.res[0] * 0.5, TCFG.res[1] * 0.5, TCFG.res[0] * 0.5, TCFG.res[1] * 0.2)

            # P샵 상품 and 단일 주문일 경우, 리뷰 버튼 미노출 예외 처리
            if not self.is_element_present('//android.widget.TextView[1][contains(@text, "[P]")]', By.XPATH) and len(prod) == 1:
                # 리뷰 작성 = Y
                try:
                    self.interact_by_xpath('//android.widget.Button[@text="리뷰확인"]')  # 리뷰 확인 버튼 클릭

                    ### 리뷰 화면 ###
                    self.interact_by_xpath('//*[@text="작성한 리뷰"][@clickable="true"]',  click=False)  # 작성한 리뷰 탭으로 이동 확인
                # 리뷰 작성 = N
                except:
                    self.interact_by_xpath('//android.widget.Button[@text="리뷰작성"]')  # 리뷰 작성 버튼 클릭

                    ### 리뷰 확면 ###
                    self.interact_by_xpath('//*[@text="미작성 리뷰"][@clickable="true"]', click=False)  # 미작성 리뷰 탭으로 이동 확인
                    self.interact_by_xpath('//android.view.View[@content-desc="리뷰 작성"]', click=False)  # 리뷰 작성 버튼 확인

                self.interact_by_id('com.amorepacific.amorepacificmall:id/back_button_image_view')  # gnb 뒤로 가기 > 주문/배송 조회 화면으로 이동

            scroll_xpath(self, '//android.widget.Button[@text="교환신청"]', loc=TCFG.res[1] * 0.55, y1=TCFG.res[1] * 0.6, y2=TCFG.res[1] * 0.5, click=False)  # 교환 신청 버튼 확인
            self.interact_by_xpath('//android.widget.Button[@text="반품신청"]', click=False)  # 반품 신청 버튼 확인

            ### 주문/배송 조회 화면 ###
            delivery_time = TCFG.driver.find_element_by_xpath('//android.widget.TextView[contains(@text,") 배송완료")]').text  # MM월 DD일(day of the week) 배송완료 텍스트 저장
            delivery_time1 = delivery_time.lstrip("0")  # MM 한 자릿수일 경우 '0' 제거
            delivery_time2 = delivery_time1.replace("월 ", "/").replace("일", "").split('\n')  # MM/DD(day of the week) 형태로 변환
            tracking_detail = delivery_time.replace("월 ", "-").replace("일", "").split('\n')  # MM-DD(day of the week) 형태로 변환
            tracking_detail = [f.split("(") for f in tracking_detail]  # 요일과 분리
            scroll_xpath(self, '//android.widget.Button[@text="배송조회"]', loc=TCFG.res[1] * 0.55, y1=TCFG.res[1] * 0.6, y2=TCFG.res[1] * 0.5)  # 배송 조회 버튼 클릭

            ### 배송 조회 화면 ###
            self.interact_by_xpath('//android.widget.TextView[@text="{}"]'.format(delivery_time2[0]), click=False)  # 배송 단계 표시 영역 날짜 + 배송 완료 텍스트 확인
            self.interact_by_xpath('//android.widget.ListView//android.widget.TextView[@text="배송완료"]', click=False)  # 배송 추적 디테일 마지막 상태 배송 완료 노출 확인
            self.interact_by_xpath('//android.widget.ListView/android.view.View[1]/android.widget.TextView[contains(@text,"{}")]'.format((tracking_detail[0])[0]), click=False)  # 주문/배송 조회 화면 배송 완료일과 배송 추척 화면 배송 완료일 일치 확인
            self.interact_by_xpath('//android.widget.Button[@text="뒤로가기"]')  # 좌측 상단 뒤로가기 버튼 클릭
            sleep(2)

            ### 주문/배송 조회 화면 ###
            scroll_xpath(self, '//android.widget.Button[@text="1:1 문의"]', loc=TCFG.res[1] * 0.55, y1=TCFG.res[1] * 0.6, y2=TCFG.res[1] * 0.5, click=False)  # 1:1 문의 버튼 확인

        # 첫 번째 주문 건 대상 검증 > 주문 내역 = Y, status = 배송 중
        elif self.is_element_present('//android.view.View[@text="배송중"]', By.XPATH):
            self.interact_by_xpath('//*[@text="상세보기"]', click=False)  # 상세 보기 버튼 확인
            if TCFG.environment == 'PRD':  # PRD 환경
                prod = TCFG.driver.find_element_by_xpath('//android.widget.TextView[contains(@text, "아모레퍼시픽 상품")]').text.split(' ')  # 주문 건 상품 갯수 저장

                # 복합 주문
                if len(prod[2].split('개')[1]) > 1:
                    # 주문 건 상품 갯수 만큼 모두 검증
                    for i in range(1, len(prod) + 1):
                        self.interact_by_xpath('(//android.widget.Image)[{}]'.format(i), click=False)  # 상품 이미지 확인
                        self.interact_by_xpath('(//android.widget.Button[@text="장바구니"])[{}]'.format(i), click=False)  # 장바구니 아이콘 확인
                # 단일 주문
                else:
                    self.interact_by_xpath('//android.widget.Image', click=False)  # 상품 이미지 확인
                    self.interact_by_xpath('//android.widget.Button[@text="장바구니"]', click=False)  # 장바구니 아이콘 확인
            elif TCFG.environment == 'STG':  # STG 환경
                prod = TCFG.driver.find_element_by_xpath(
                    '//android.widget.TextView[contains(@text, "아모레퍼시픽 상품")]').text.split(' ')  # 주문 건 상품 갯수 저장

                # 복합 주문
                if len(prod[2].split('개')[1]) > 1:
                    # 주문 건 상품 갯수 만큼 모두 검증
                    for i in range(1, len(prod) + 1):
                        self.interact_by_xpath('(//android.widget.Button[@text="장바구니"])[{}]'.format(i), click=False)  # 장바구니 아이콘 확인
                # 단일 주문
                else:
                    self.interact_by_xpath('//android.widget.Button[@text="장바구니"]', click=False)  # 장바구니 아이콘 확인

            scroll_xpath(self, '//android.widget.Button[@text="배송조회"]', loc=TCFG.res[1] * 0.55, y1=TCFG.res[1] * 0.6, y2=TCFG.res[1] * 0.5)  # 배송 조회 버튼 클릭

            ### 배송 조회 화면 ###
            # status = 배송 중, 배송 출발 상태인 경우
            if self.is_element_present('//android.widget.TextView[@text="배송출발"]', By.XPATH):
                self.interact_by_xpath('//android.widget.TextView[contains(@text,") 도착예정")]', click=False)  # 배송 단계 도착 예정 문구 노출 확인
            # status = 배송 중, 집화 처리 상태인 경우
            else:
                self.interact_by_xpath('//android.widget.TextView[@text="집화처리"]', click=False)  # 배송 추척 디테일 집화 처리 상태 노출 확인
            self.interact_by_xpath('//android.widget.Button[@text="뒤로가기"]')  # 좌측 상단 뒤로가기 버튼 클릭
            sleep(3)

            ### 주문/배송 조회 화면 ###
            self.interact_by_xpath('//android.widget.Button[@text="수령확인"]', click=False)  # 수령 확인 버튼 확인
            self.interact_by_xpath('//android.widget.Button[@text="1:1 문의"]', click=False)  # 1:1 문의 버튼 확인

        # 첫 번째 주문 건 대상 검증 > 주문 내역 = Y, status = 상품 준비 중
        elif self.is_element_present('//android.view.View[@text="상품준비중"]', By.XPATH):
            self.interact_by_xpath('//*[@text="상세보기"]', click=False)  # 상세 보기 버튼 확인
            if TCFG.environment == 'PRD':  # PRD 환경
                prod = TCFG.driver.find_element_by_xpath('//android.widget.TextView[contains(@text, "아모레퍼시픽 상품")]').text.split(' ')  # 주문 건 상품 갯수 저장

                # 복합 주문
                if len(prod[2].split('개')[1]) > 1:
                    # 주문 건 상품 갯수 만큼 모두 검증
                    for i in range(1, len(prod) + 1):
                        self.interact_by_xpath('(//android.widget.Image)[{}]'.format(i), click=False)  # 상품 이미지 확인
                        self.interact_by_xpath('(//android.widget.Button[@text="장바구니"])[{}]'.format(i), click=False)  # 장바구니 아이콘 확인
                # 단일 주문
                else:
                    self.interact_by_xpath('//android.widget.Image', click=False)  # 상품 이미지 확인
                    self.interact_by_xpath('//android.widget.Button[@text="장바구니"]', click=False)  # 장바구니 아이콘 확인
            elif TCFG.environment == 'STG':  # STG 환경
                prod = TCFG.driver.find_element_by_xpath('//android.widget.TextView[contains(@text, "아모레퍼시픽 상품")]').text.split(' ')  # 주문 건 상품 갯수 저장

                # 복합 주문
                if len(prod[2].split('개')[1]) > 1:
                    # 주문 건 상품 갯수 만큼 모두 검증
                    for i in range(1, len(prod) + 1):
                        self.interact_by_xpath('(//android.widget.Button[@text="장바구니"])[{}]'.format(i), click=False)  # 장바구니 아이콘 확인
                # 단일 주문
                else:
                    self.interact_by_xpath('//android.widget.Button[@text="장바구니"]', click=False)  # 장바구니 아이콘 확인

            self.interact_by_xpath('//android.widget.Button[@text="취소요청"]', click=False)  # 취소 요청 버튼 확인
            self.interact_by_xpath('//android.widget.Button[@text="1:1 문의"]', click=False)  # 1:1 문의 버튼 확인

        # 첫 번째 주문 건 대상 검증 > 주문 내역 = Y, status = 결제 완료
        elif self.is_element_present('//android.view.View[@text="결제완료"]', By.XPATH):
            self.interact_by_xpath('//*[@text="상세보기"]', click=False)  # 상세 보기 버튼 확인
            if TCFG.environment == 'PRD':  # PRD 환경
                prod = TCFG.driver.find_element_by_xpath('//android.widget.TextView[contains(@text, "아모레퍼시픽 상품")]').text.split(' ')  # 주문 건 상품 갯수 저장

                # 복합 주문
                if len(prod[2].split('개')[1]) > 1:
                    # 주문 건 상품 갯수 만큼 모두 검증
                    for i in range(1, len(prod) + 1):
                        self.interact_by_xpath('(//android.widget.Image)[{}]'.format(i), click=False)  # 상품 이미지 확인
                        self.interact_by_xpath('(//android.widget.Button[@text="장바구니"])[{}]'.format(i), click=False)  # 장바구니 아이콘 확인
                # 단일 주문
                else:
                    self.interact_by_xpath('//android.widget.Image', click=False)  # 상품 이미지 확인
                    self.interact_by_xpath('//android.widget.Button[@text="장바구니"]', click=False)  # 장바구니 아이콘 확인
            elif TCFG.environment == 'STG':  # STG 환경
                prod = TCFG.driver.find_element_by_xpath('//android.widget.TextView[contains(@text, "아모레퍼시픽 상품")]').text.split(' ')  # 주문 건 상품 갯수 저장

                # 복합 주문
                if len(prod[2].split('개')[1]) > 1:
                    # 주문 건 상품 갯수 만큼 모두 검증
                    for i in range(1, len(prod) + 1):
                        self.interact_by_xpath('(//android.widget.Button[@text="장바구니"])[{}]'.format(i), click=False)  # 장바구니 아이콘 확인
                # 단일 주문
                else:
                    self.interact_by_xpath('//android.widget.Button[@text="장바구니"]', click=False)  # 장바구니 아이콘 확인

            self.interact_by_xpath('//android.widget.Button[@text="주문취소"]', click=False)  # 주문 취소 버튼 확인
            self.interact_by_xpath('//android.widget.Button[@text="1:1 문의"]', click=False)  # 1:1 문의 버튼 확인

    # 주문 내역 = N
        else:
            self.interact_by_xpath('//*[@text="최근 주문 내역이 없습니다."]', click=False)  # 문구 노출 확인
    except:
        self.capture_screen()
        self.assertEqual(0, 1)
    else:
        print(f"{sys._getframe(0).f_code.co_name} Passed")
        TCFG.is_passed = True
    finally:
            self.interact_by_xpath('//android.view.View[@content-desc="마이"]')  # 하단 액션바 마이파우치로 이동