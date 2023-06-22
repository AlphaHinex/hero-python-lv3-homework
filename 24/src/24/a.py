a = [1,62,7,81,9,10,10,9]
for i in range(len(a)):
    if a[0] != 9:
        a.remove(a[0])
    else:
        if len(a)>1:
            a.remove(a[1])    
print(a)

# for i in a:
#     if i !=9:
#         a.remove(a[0])
#     else:
#         if len(a)>1:
#             a.remove(a[1])
# print(a)                




