def lambdaTest():
    # [lambda]
    # - 익명의 함수로 한번 사용하고 heap 메모리에서 증발
    # - 일반적인 함수는 객체를 만들고, 재사용을 위해 함수 이름을 할당
    sum = lambda a, b: a + b
    print('lambda test :', sum(3, 4))


def mapTest():
    # [map]
    # - map(변환 함수, 순회 가능한 데이터)
    # - 입력받은 자료형의 각 요소가 함수에 의해 연산된 후 map iterator 로 반환
    # - '게으른 연산'을 진행해서 메모리를 크게 절약 효과
    #  ** '게으른 연산' : 필요할 때 가져가 사용하는 연산 방법
    li = [1, 2, 3]
    result = list(map(lambda i: i ** 2, li))
    print('map test :', li, '->', result)


def ternaryTest():
    li = [-1, -2, 0, 1, 2]
    result = list(map(lambda i: '음수' if i < 0 else ('양수' if i > 0 else 0), li))
    print('ternary test :', result)


def filterTest():
    # [filter]
    # - 입력받은 각 요소들 중 조건에 부합한 요소만 반환하여 새로운 list 생성
    li = [-1, -2, 0, 1, 2]
    result = list(filter(lambda i: i > 0, li))
    print('filter test :', result)


def reduceTest():
    # [reduce]
    # - list 에 대한 연산은 축약해주는 함수
    # - python3 부터는 내장함수에서 제외
    from functools import reduce

    li = [1, 2, 3, 4, 5]
    print('reduce test :', reduce(lambda a, b: a + b, li))


def zipTest():
    # [zip]
    # - 같은 길이의 list 를 같은 index 끼리 잘라서 새로운 list 로 반환
    a = [1, 2, 3, 4, 5]
    b = ['a', 'b', 'c']

    for x, y in zip(a, b):
        print('zip test :', x, '-', y)


def sortTest():
    # [sort]
    # - 정렬 method
    # - key 매개변수를 통해서 object 정렬 가능
    li = [['a', 20], ['b', 30], ['c', 10]]
    li = sorted(li, key=lambda k:k[1], reverse=True)
    print('sort test : ', li)


def execTest():
    # [exec]
    # - 문자열로 표현된 구문을 python complie code 로 변환
    a = 4
    exec('a = a + 5')
    print('exec test : ', a)


# lambda
lambdaTest()

# map
mapTest()

# ternary operators
ternaryTest()

# filter
filterTest()

# reduce
reduceTest()

# zip
zipTest()

# sorted
sortTest()

# exec
execTest()
