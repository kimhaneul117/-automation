    def test_010_미작성_리뷰탭_확인(self):
        try:
            ### 마이파우치 ###
            TCFG.driver.execute_script('window.scrollTo(0, 700);')  # 하단으로 스크롤

            self.hl_and_interact(By.XPATH, '//*[@ap-click-name="마이파우치_리뷰관리"]')  # 리뷰 관리 진입

            ### 리뷰 화면 ###
            self.hl_and_interact(By.XPATH, '//*[@class="on"]//*[@id="tabButtonOrder"][text()="미작성 리뷰"]', click=False)  # 미작성 리뷰 탭 default 활성화 상태 확인

            # 미작성 리뷰가 있는 경우
            try:
                self.hl_and_interact(By.XPATH, '//*[@style="display: none;"]/..//p[text()="작성할 리뷰가 없습니다"]', click=False)  # 작성할 리뷰가 없습니다. 문구 미노출 상태 확인

                # 한달 사용 리뷰 존재 (data-review-type="OneMonth")
                try:
                    prod_name = TCFG.driver.find_element_by_xpath('(//*[@class="badge-wrap"]/..//*[@class="product_name"])[1]').text  # 상품명 저장
                    prod_name_1 = prod_name.split()  # 상품명 띄어쓰기 구간 자르기
                    print(prod_name_1)

                    # 상품명 뒤에 두마디 자르기 (간헐적으로 띄어쓰기 상이한 단어 발생으로 일부 단어만 검증)
                    for replace_text in prod_name_1:
                        if int(replace_text in prod_name) and len(prod_name.partition(replace_text)[0]) > \
                                len(prod_name.partition(replace_text)[2]):
                            prod_name = prod_name.partition(replace_text)[0]
                            prod_name = prod_name.strip()
                    print(prod_name)

                    self.hl_and_interact(By.XPATH, '//*[text()="미작성 리뷰"]/..//*[@class="badge green"][text()="한달 사용 리뷰"]', click=False)  # 한달 작성 리뷰 뱃지 확인
                    self.hl_and_interact(By.XPATH, '(//*[@class="page-sub-title"]/..//*[text()="리뷰 작성"]/..//*[@data-review-type="OneMonth"])[1]')  # 리뷰 작성 버튼 클릭

                    ### 한달 사용 리뷰 작성 화면 ###
                    self.hl_and_interact(By.XPATH, '//*[@class="page-sub-title"]/..//*[text()="한달 사용 리뷰 작성"]', click=False)
                    self.hl_and_interact(By.XPATH, '//*[@class="score review_copy"]/..//*[text()="한달 동안 사용해보니 어땠나요?"]', click=False)
                # 일반 리뷰 존재 (data-review-type="Pur")
                except:
                    prod_name = TCFG.driver.find_element_by_xpath('(//*[@class="product_name"])[1]').text  # 상품명 저장
                    prod_name_1 = prod_name.split()  # 상품명 띄어쓰기 구간 자르기
                    print(prod_name_1)

                    # 상품명 뒤에 두마디 자르기 (간헐적으로 띄어쓰기 상이한 단어 발생으로 일부 단어만 검증)
                    for replace_text in prod_name_1:
                        if int(replace_text in prod_name) and len(prod_name.partition(replace_text)[0]) > \
                                len(prod_name.partition(replace_text)[2]):
                            prod_name = prod_name.partition(replace_text)[0]
                            prod_name = prod_name.strip()
                    print(prod_name)

                    self.hl_and_interact(By.XPATH, '(//*[@class="page-sub-title"]/..//*[text()="리뷰 작성"]/..//*[@data-review-type="Pur"])[1]')  # 리뷰 작성 버튼 클릭

                    ### 리뷰 작성 화면 ###
                    self.hl_and_interact(By.XPATH, '//*[@class="score review_copy"]/..//*[text()="사용해보니 어땠나요?"]', click=False)

                ## 공통 검증 영역
                self.hl_and_interact(By.XPATH, '//*[@class="product_name"][contains(text(), "{}")]'.format(prod_name), click=False)  # 리뷰 작성 상품 일치 확인
                self.hl_and_interact(By.XPATH, '//*[@class="ui_rating new ＠rating-apply"]', click=False)  # 별점 등록 영역 확인

                # 별점 2점 선택
                self.hl_and_interact(By.XPATH, '(//*[@class="ficon ficon-star-25"])[1]')
                self.hl_and_interact(By.XPATH, '(//*[@class="ficon ficon-star-25"])[2]')

                self.hl_and_interact(By.XPATH, '//*[@class="section review_question"]', click=False)  # 리뷰 질문 영역 노출 확인
                self.hl_and_interact(By.XPATH, '//*[@class="btn_previous"]')  # 공통 헤더 뒤로 가기 버튼 클릭
            # 미작성 리뷰가 없는 경우
            except:
                self.hl_and_interact(By.XPATH, '//*[@class="non_content order"]/..//*[text()="작성할 리뷰가 없습니다"]', click=False)  # 작성할 리뷰가 없습니다. 문구 노출 상태 확인
                none = is_element_present(TCFG.driver, '//*[@class="non_content order"][@style="display: block;"]//*[text()="작성할 리뷰가 없습니다"]')  # 빈 공백 노출 시 에러 출력 (APM-41432)
                if none:
                    print("미작성 리뷰 탭 빈 공백 노출 Failed")
                    capture_screen(self, TCFG)
                    self.assertEqual(0, 1)
        except:
            capture_screen(self, TCFG)
            self.assertEqual(0, 1)
            print("Failed")
        else:
            print(f"{sys._getframe(0).f_code.co_name} Passed")
            TCFG.is_passed = True

    def test_011_작성한_리뷰탭_확인(self):
        try:
            ### 리뷰 관리 화면 ###
            self.hl_and_interact(By.XPATH, '//*[@id="tabButtonReview"][text()="작성한 리뷰"]')  # 작성한 리뷰 탭 클릭

            # 작성한 리뷰 내역이 있는 경우
            try:
                self.hl_and_interact(By.XPATH, '(//*[@class="btn_area"]/a[text()="수정하기"])[1]', click=False)
            # 작성한 리뷰 내역이 없는 경우
            except:
                self.hl_and_interact(By.XPATH, '//*[text()="작성한 리뷰가 없습니다"]', click=False)

            # 간헐적으로 발생 되는 빈 공백 노출 이슈로 재확인 (APP 동일 발생일 수 있음)
            self.hl_and_interact(By.XPATH, '//*[@id="tabButtonOrder"][text()="미작성 리뷰"]')  # 미작성 리뷰 탭 클릭

            none = is_element_present(TCFG.driver, '//*[@class="non_content order"][@style="display: block;"]//*[text()="작성할 리뷰가 없습니다"]')  # 빈 공백 노출 시 에러 출력 (APM-41432)
            if none:
                print("미작성 리뷰 탭 빈 공백 노출 Failed")
                capture_screen(self, TCFG)
                self.assertEqual(0, 1)
                
            TCFG.driver.execute_script("window.history.go(-1)")  # 뒤로 가기
        except:
            capture_screen(self, TCFG)
            self.assertEqual(0, 1)
            print("Failed")
        else:
            print(f"{sys._getframe(0).f_code.co_name} Passed")
            TCFG.is_passed = True
        finally:
            self.hl_and_interact(By.XPATH, '//*[@href="/kr/ko/my/page/info/myPouch"]')  # 마이파우치로 이동
