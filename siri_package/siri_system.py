#===================================================================================================================
#                                                 음성인식 시스템 API
#===================================================================================================================
import speech_recognition as sr

# 01. 음성인식 시스템('siri') 부팅 함수
        # notice : 문자열을 입력받아 
        # 각 명령어를 수행한다.
def invoke_siri_system():
    print(greeting)
    print(banner_comment)
    print("="*155)

# 02. 시리 호출 확인 함수    
        # notice :사용자 입력 리스트에서 '시리' 라는 
        # 단어가 포함되어 있을때 True값을 리턴한다. 
def is_siri_in_list(user_input_list):
    siri = "시리"
    for word in user_input_list:
        if siri in word:
            return True
    return False     



# 03. 사용자 음성인식후 문자열을 리턴하는 함수     
def get_text_from_voice():
    # 3-1) 마이크 객체생성
    mic = sr.Microphone()
    # 3-2) 음성인식 객체생성
    recognizer = sr.Recognizer()
    # 3-3) 오디오 데이터 생성(입출력)
    print('음성 인식중...')
    while True:  # 무한 루프
        with mic as voice_source:
            # print('음성 인식중...')
            try:
                audio_data = recognizer.listen(voice_source, timeout=10, phrase_time_limit=5)
                if audio_data:
                    result_text = recognizer.recognize_google(audio_data, language="ko-KR")
                    return result_text
            except sr.WaitTimeoutError:  # 음성 입력이 없을 경우 예외 처리
                print("음성입력 시간을 초과 했습니다. 다시 시도해주세요")
                pass    # 입력 시간을 초과시 다시 음성인식 루프
            except sr.UnknownValueError:
                pass
            except sr.RequestError:
                print("서버 에러 발생")

    
#===================================================================================================================
#                                                도입 배너 문자열
#===================================================================================================================

greeting = (
    "===========================================================================================================================================================\n"
    "\t       :::    :::       ::::::::::       :::        :::        ::::::::              ::::::::       :::::::::::       :::::::::       :::::::::::        \n"
    "\t      :+:    :+:       :+:              :+:        :+:       :+:    :+:            :+:    :+:          :+:           :+:    :+:          :+:             \n"
    "\t     +:+    +:+       +:+              +:+        +:+       +:+    +:+            +:+                 +:+           +:+    +:+          +:+              \n"
    "\t    +#++:++#++       +#++:++#         +#+        +#+       +#+    +:+            +#++:++#++          +#+           +#++:++#:           +#+               \n"
    "\t   +#+    +#+       +#+              +#+        +#+       +#+    +#+                   +#+          +#+           +#+    +#+          +#+                \n"
    "\t  #+#    #+#       #+#              #+#        #+#       #+#    #+#            #+#    #+#          #+#           #+#    #+#          #+#                 \n"
    "\t ###    ###       ##########       ########## ########## ########              ########       ###########       ###    ###      ###########              \n"
    "===========================================================================================================================================================\t"
)

banner_comment = (
                                            """\
                                            안녕하세요. 애플의 마스코트 '시리' 입니다.
                                            도움이 필요하면 언제든지 불러주세요.\
                                            """
)


#===================================================================================================================
#                                                     사용예제
#===================================================================================================================

# 사용 예시1
if __name__ == "__main__" :
    invoke_siri_system()
    # # 사용 예시2
    # while True:  # 무한 루프
    #     user_input = get_text_from_voice()
    #     if user_input:  # 유효한 음성 입력이 있을 때만 처리
    #         user_input_list = util.get_splited_string_list(user_input)
    #         reserved_list = util.get_reserved_list()

#===================================================================================================================