import re
p = re.compile("ca.e")
#. : 하나의 문자를 뜻한다.>>ca?e--care,cafe
# ^: 문자열의 시작--> ^de: desk,destination
# $: 문자열의 끝 --> se$: case,base


def print_match(m):

    if m:
        print(m.group())
    else:
        print("매칭되지 않음")


# m= p.match("careless")# 주어진 문자열의 처음부터 일치하는지 확인--> 뒤의 값은 반환하지 않는다. 
# print_match(m)
 # 매치되지 않으면 에러 발생

m=p.search("careless")# 주어진 문자열중에 일치하는게 있는지 확인
print_match(m)
