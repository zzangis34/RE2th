# 1번
# name = input("이름을 입력하세요.")
# age = input("나이를 입력하세요.")
# print("안녕하세요! %s님 (%s세)" % (name, age))

# 2번
name = input("이름을 입력하세요.")
birth_year = input("태어난 년도를 입력하세요.")
year = input("올해 년도를 입력하세요.")
print("올해는%s년, %s님의 나이는%d세 입니다" % (year, name, int(year)-int(birth_year)+1))
