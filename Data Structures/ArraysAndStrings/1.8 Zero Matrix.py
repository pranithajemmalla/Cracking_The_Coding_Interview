# Zero Matrix
# Write an algorithm such that if an element in an MxN matrix is 0, its entire row and column are set to 0

class ZeroMatrix:
    def __init__(self):
        self.m = None
        self.n = None
        self.matrix = []

    def using_storing_zero_indices(self):
        rows = set()
        cols = set()
        for i in range(self.m):
            for j in range(self.n):
                if self.matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)
        for i in rows:
            for x in range(self.n):
                self.matrix[i][x] = 0
        for j in cols:
            for x in range(self.m):
                self.matrix[x][j] = 0

    def using_set_first_row_col_zero(self):
        first_row_zero = False
        first_col_zero = False

        for i in range(self.m):
            if self.matrix[i][0] == 0:
                first_row_zero = True

        for j in range(self.n):
            if self.matrix[0][j] == 0:
                first_col_zero = True

        for i in range(1, self.m):
            for j in range(1, self.n):
                if self.matrix[i][j] == 0:
                    self.matrix[i][0] = 0
                    self.matrix[0][j] = 0

        for i in range(1, self.n):
            if self.matrix[0][i] == 0:
                for x in range(1, self.m):
                    self.matrix[x][i] = 0

        for j in range(1, self.m):
            if self.matrix[j][0] == 0:
                for x in range(1, self.n):
                    self.matrix[j][x] = 0

        print(self.matrix)
        if first_row_zero:
            for i in range(self.m):
                print(i,0)
                self.matrix[i][0] = 0
        if first_col_zero:
            for j in range(self.n):
                print(0,j)
                self.matrix[0][j] = 0


if __name__ == '__main__':
    zeroMatrixObj = ZeroMatrix()
    zeroMatrixObj.m = int(input())
    zeroMatrixObj.n = int(input())
    for i in range(zeroMatrixObj.m):
        zeroMatrixObj.matrix.append([])
        for j in range(zeroMatrixObj.n):
             zeroMatrixObj.matrix[i].append(int(input()))
    # zeroMatrixObj.matrix = [[0,2,3,4,9],[5,6,7,0,10],[11,0,13,14,15],[16, 17,18,19,20]]
    zeroMatrixObj.using_set_first_row_col_zero()
    print(zeroMatrixObj.matrix)
