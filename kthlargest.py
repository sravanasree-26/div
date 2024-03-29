import heapq
def findKthLargest(arr,k):
    arr=[-num for num in arr]
    heapq.heapify(arr)
    for X in range(k):
        d=heapq.heappop(arr)
    return -d
arr=[3,2,1,5,6,4]
while True:
    opt=(input("Enter the K value(enter no to break): "))
    if (opt=='no'):
        break
    try:
        k=int(opt)
    except:
        print("Invalid Option")
        continue
    if k<len(arr):
        print(f"{k}nd largest is {findKthLargest(arr,k)}")
        continue
    else:
        print("Index out of range")
