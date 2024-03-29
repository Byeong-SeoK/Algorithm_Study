파이썬 zip 함수
zip() 함수는 여러 개의 순회 가능한(iterable) 객체를 인자로 받고, 
각 객체가 담고 있는 원소를 튜플의 형태로 차례로 접근할 수 있는 반복자(iterator)를 반환합니다.

>>> for number, upper, lower in zip("12345", "ABCDE", "abcde"):
...     print(number, upper, lower)
...
1 A a
2 B b
3 C c
4 D d
5 E e



def solution(phoneBook):
    phoneBook = sorted(phoneBook) 
    #sorted하면 [6789, 12, 6]이 --> [12, 6, 6789] 순서로 string 값의 크기(아스키 코드)를 기준으로 sorted 된다.

    for p1, p2 in zip(phoneBook, phoneBook[1:]): 
        #zip함수를 통해서 정렬된 PhoneBook을 정렬되기 전 phoneBook의 접두사 [1:]으로 접두사가 있는지 확인하는 것이다.
        if p2.startswith(p1): #접두사로 시작하는지 확인하는 과정
            return False
    return True
