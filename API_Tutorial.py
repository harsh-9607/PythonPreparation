class solve:
    def sub(s):         
        left = 0 
        right = 1
        sub = s[left]
        maxsub=""
        while left < right:
            if s[left] != s[right]:
                sub += s[right]
            else:
                left = right
                sub=s[left]
            if len(sub) > maxsub:
                maxsub= sub
            right += 1
        return maxsub

print(solve.sub("redeqwewe"))