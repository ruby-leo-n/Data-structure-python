dic = {}
# 맵에 엔트리 삽입
dic["data"] = "자료"
dic["structure"] = "구조"
dic["sequential search"] = "선형탐색"
dic["game"] = "게임"
dic["binary search"] = "이진 탐색"
# 엔트리 출력
print("나의 단어장")
print(dic)
# 엔트리 탐색
if dic.get("game"):
    print("탐색: game ->", dic["game"])
if dic.get("over"):
    print("탐색: over ->", dic["over"])
if dic.get("data"):
    print("탐색: data ->", dic["data"])
# 항목 삭제
dic.pop('game')

print("나의 단어장")
print(dic)
