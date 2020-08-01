# [exec]
# - 문자열로 표현된 구문을 python complie code 로 변환
a=0;b=1;exec("a,b=b,a+b;"*int(input()));print(a)