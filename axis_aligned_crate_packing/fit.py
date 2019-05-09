class fit:
    def __init__(self, X, Y, x, y):
        self.X = X
        self.Y = Y
        self.x = x
        self.y = y

    def fit1(self):
        if(self.X < self.x or self.Y < self.y):
            return 0
        else:
            return self.compute()

    def fit2(self):
        if(self.X < self.x or self.Y < self.y):
            if(self.X < self.y or self.Y < self.x):
                return 0
            else: 
                return self.rotate()
        else:
            normal = self.compute()
            rotate = self.rotate()
            return max(normal, rotate)

    def compute(self):
        return ((self.X / self.x) * (self.Y / self.y))

    def rotate(self):
        return ((self.X / self.y) * (self.Y / self.x))


total = fit(25, 18, 6, 5)
print(total.fit1())
print(total.fit2())
