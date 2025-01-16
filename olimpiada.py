#2.  x=[]
# def f1(n):
#     for a in range(1,n+1):
#         for b in range(1,n+1):
#             if a == n - b:
#                 x.append(a)
#                 x.append(b)
#     print(int((len(x)/2)))
# f1(4)
#3.
# def yes_or_no(n):
#     if n==0 or n==1 or n==2:
#         return "no"
#     elif n%2==0:
#         return "yes"
#     else:
#         return "no"
# print(yes_or_no(20))
#4.

# def kvadirat(a,b):
#     if (2*a>=b and a<b) or a>=2*b:
#        s=(a*2)**2
#        return s
#     elif 2*b>=a and a>b or b>2*a:
#         s=(2*b)**2
#         return s
# print(kvadirat(3,1))
#
# def minimal_lamoalar(n,m):
#     if n==1 and m==1:
#         return 1
#     elif n==1 and m==3:
#         return 2
#     k=(n*m)//2
#     return k
# print(minimal_lamoalar(1,5))
# Sonning raqamlar yig'indisini hisoblash funksiyasi
# def raqamlar_yigindisi(son):
#     yigindi=0
#     while son>0:
#         yigindi+=son%10
#         son //= 10
#     return yigindi
# print(raqamlar_yigindisi(123))



# def mukammal_son(k):
#     mukammal_sonlar=[]
#     son=1
#     while len(mukammal_sonlar)<k:
#         if sum(int(r) for r in str(son))%10==0:
#             son+=1
#             return mukammal_sonlar[-1]
# print(mukammal_son(2))
# def mukamal_son(k):
#     mukamal_sonlar=[]
#     son=1
#     while len(mukamal_sonlar)<k:
#         if sum(int(i) for i in str(son)) % 10 == 0:
#             mukamal_sonlar.append(son)
#         son += 1
#     return mukamal_sonlar[-1]
# print(mukamal_son(4))
# def yigindi(n):
#     s=0
#     while n>0:
#         s+=n%10
#         n//=10
#     return s
# print(yigindi(125))
#5.
# def berilgan(n,a=[])->int:
#     if n>len(a):
#         return False
#     elif len(a)>n:
#         return 0
#
#     while len(a)<=n:
#         if n * (a[n-1] - a[0]) >(a[n-1]-a[n-2]):
#             return sum(a[n-1]-a[n-2])
#         else:
#             return n * [n-1] - a[0]
# print(berilgan(3,[1,2,3]))

def berilgan(n, a=[]):
    if n > len(a) or n < 1:
        return 0
    sum_diff = 0
    if n * (a[n - 1] - a[0]) >sum_diff:
        for i in range(1, n):
            sum_diff += a[i] - a[i - 1]
            return sum_diff
    else:
        return n * [n - 1] - a[0]



print(berilgan(3, [1, 2, 3]))
