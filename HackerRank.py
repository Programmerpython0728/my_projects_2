# def f1(l):
#     b=list(l)
#     b.sort(reverse=True)
#     if b[0]==9:
# #         b[0]=0
# #         b[1]+=1
# #     return b.sort(reverse=False)
# # a=f1([1,2,3])
# # print(a)
def f1(l):
    b = list(l)
    i=len(b)-1
    if b[i]==9:
        b[i]=0
        b[i-1]+=1
    elif b[i-1]==9:
        b[i-1]-=10


    elif b[i]<9:
        b[i ] += 1

    return b
a = f1([9, 9])
print(a)


