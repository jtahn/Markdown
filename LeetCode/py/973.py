"""heaps"""
def kClosest(self, points, k):
    # max heap
    f = -lambda x,y: x*x + y*y
    h = []
    for i, (x,y) in enumerate(points[:k]):
        heapq.heappush(h, (f(x,y), i))
    for i, (x,y) in enumerate(points[k:], k):
        heapq.heappushpop(h, (f(x,y), i))
    return [points[i] for (_,i) in h]

    # min heap
    d = lambda x,y: x*x + y*y
    h = []
    for i, (x,y) in enumerate(points):
        heapq.heappush(h, (d(x,y), i))
    it = (heapq.heappop(h) for i in range(k))
    return [points[i] for (_,i) in it]


"""quickselect"""
def kClosest(self, points, k):
    d = lambda x,y: x**2 + y**2
    p, r = 0, len(points)-1
    while True:
        i = random.randrange(p,r+1)
        points[i], points[r] = points[r], points[i]
        q = p
        c = d(*points[r])
        for i in range(p, r):
            if d(*points[i]) <= c:  # how come code fails if i do <c ?
                points[i], points[q] = points[q], points[i]
                q += 1
        points[q], points[r] = points[r], points[q]
        if q<k-1:   # how come fails if i do q < k
            p = q+1
        elif q==k-1:
            break
        else:   # k-1<q
            r = q-1
    return points[:k]