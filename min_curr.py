#find min currency

def find_min_cur(n):
    cur_arr=[2000,500,200,100,50,20,10,5,2,1]
    cur_cnt={}
    cnt=0
    tot_cnt=0
    #2300
    for cur in cur_arr:
        cnt=n//cur
        tot_cnt=tot_cnt+cnt
        if cnt > 0:
            cur_cnt[cur]=cnt
        n=n % cur
        if n == 0:
            break
    print("\n min cur cnt = ",tot_cnt)
    print(cur_cnt)
find_min_cur(int(input("enter n")))
        
