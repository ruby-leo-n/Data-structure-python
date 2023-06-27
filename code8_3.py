import heapq  # heap 모듈을 불러옴

arr = [5, 3, 8, 4, 9, 1, 6, 2, 7]  # heaq이 아닌 list로 구현된 자료
print(arr)  # 출력

heapq.heapify(arr)  # heaq으로 변환 (단, 최소힙)
print(arr)  # 출력 heapify는 arr에 직접 관여하여 재구성함 !기존 배열이 필요한 경우 복사 후 복사한 인자를 사용할 것!

print(heapq.heappop(arr))  # heaqpop은 최소값을 삭제 후 반환 & 출력

heapq.heapify(arr)  # 다시 arr를 최소힙으로 생성
print(arr)  # 출력

print(heapq.heappop(arr))  # heaqpop은 최소값을 삭제 후 반환 & 출력
print(heapq.heappop(arr))  # heaqpop은 최소값을 삭제 후 반환 & 출력
print(arr)  # 출력

heapq.heappush(arr, 4.5)  # 원소 추가
print(arr)  # 출력
