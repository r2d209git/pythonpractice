from pandas import Series

print(Series)

kakao = Series([92600, 92610, 93450, 98000])

print(kakao)
print(kakao[1])

kakao2 = Series([92600, 92610, 93450, 98000], index=["kakao", "naver", "daum", "sk"])
print("index : %i" %kakao2['naver'])

print(kakao2)

for index in kakao2.index:
    print(f"index : {index}")

for value in kakao2.values:
    print(f"value : {value}")