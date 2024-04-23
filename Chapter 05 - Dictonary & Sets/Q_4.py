'''
    What will be the length of the following set S:
        S=set()
        S.add(20)
        S.add(20.0)
        S.add("20")     (length of S after these Operations?)

'''

S=set()
S.add(20)
S.add(20.0)
S.add("20")

print(len(S),S)         # 2   {20, '20'}


