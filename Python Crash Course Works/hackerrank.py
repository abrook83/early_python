N, M = map(int, input().split())    # Reads two numbers from input and typecasts them to int using  
# map function 
patt = '.|.'
for i in range(1,N,2):      # every second number in the range
    patts = i * patt
    dashes_per_side = int((M - len(patts)) / 2)
    line = f"{'-' * dashes_per_side}{patts}{'-' * dashes_per_side}"
    print(line)

msg = 'WELCOME'
cline_dashes = int((M - len(msg)) / 2)
print(f"{cline_dashes * '-'}{msg}{cline_dashes * '-'}")

for i in reversed(range(1,N,2)):      # every second number in the range
    patts = i * patt
    dashes_per_side = int((M - len(patts)) / 2)
    line = f"{'-' * dashes_per_side}{patts}{'-' * dashes_per_side}"
    print(line)
# for num in nums:
#     dashes = 

    # print('-', end='')
    # for dash in range(0,i):
    #     print('-', end='')

# nums.reverse()      # reverse the order of nums
# print(nums)

# N, M = map(int,input().split())
# for i in range(1,N,2): 
#     print((i * ".|.").center(M, "-"))
# # print("WELCOME".center(M,"-"))
# # for i in range(N-2,-1,-2): 
# #     print((i * ".|.").center(M, "-"))

