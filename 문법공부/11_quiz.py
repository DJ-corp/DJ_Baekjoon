''' 사이트별로 비밀번호를 만들어 주는 프로그램을 작성하시오
    
    예) http://naver.com
        규칙1 : http:// 부분은 제외 => naver.com
        규칙2 : 처음 만나는 점(.) 이후 부분은 제외 => naver
        규칙3 : 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e'의 갯수 + "!"로 구성
    
    예) http://naver.com 일 때 nav51!
        http://daum.net 일 때 dau40!
        http://google.com 일 때 goo61!
        http://youtube.com 일 때 you71! '''

url = "http://youtube.com"
domain = url[7:-4]
print(domain[ :3] + str(len(domain)) + str(domain.count("e")) + "!")