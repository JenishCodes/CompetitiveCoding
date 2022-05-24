def maxArea(height):
    n = len(height)
    s = 0
    m = 0
    e = n-1
    while s < n:
        if height[s]<=height[e]:
            m = max(m, (e-s)*height[s])
            s+=1
        else:
            m = max(m, (e-s)*height[e])
            e-=1
    return m

print(maxArea([1,8,6,2,5,4,8,3,7]))
