class deathgame:
    def __init__(self):
        self.shooter = 0

    def josephus(self, k, arr):
        if len(arr) <= 1:
            return arr[0]
        dead = (self.shooter + k - 1) % len(arr)
        arr.pop(dead)
        self.shooter = dead
        return self.josephus(k, arr)

    def jos(self, n, k):
        if n == 1:
            return 0
        return (self.jos(n - 1,k) + k) % n


g = deathgame()
arr = [i for i in range(5)]
print(g.josephus(3, arr))

print(g.jos(5, 3))
