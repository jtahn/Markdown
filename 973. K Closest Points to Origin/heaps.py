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
