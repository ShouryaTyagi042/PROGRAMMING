arr = tuple(input())
ans = []
for ch in arr:
    if ch in "AEIOUYaeiouy":
        continue
    else:
        if ch.isupper() == True:
            s = "." + ch.lower()
            ans.append(s)
        else:
            s = "." + ch
            ans.append(s)
st = ""
print(st.join(ans))
