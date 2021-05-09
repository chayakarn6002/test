arr = [1,4,6,7,8,10]
s = 19
res = []
def comb(arr, res, path, s):
    if (sum(path) == s):
        res.append(path)
    for i in range(len(arr)):
        comb(arr[i+1:], res, path+[arr[i]], s)
comb(arr, res, [], s)
print(res)