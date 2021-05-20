# Rotate Matrix
# Given an image represented by an NxN matrix, where each pixel in the image is 4 bytes, write a method to rotate
# the image by 90 degrees. Can you do this in place?

class RotateMatrix:
    def __init__(self):
        self.image = []
        self.n = None

    def rotate(self, k, n):
        ind = 0
        for i in range(k, n-1+k):
            top = self.image[k][i]
            self.image[k][i] = self.image[i][n-1+k]
            self.image[i][n-1+k] = self.image[n-1+k][n-ind-1+k]
            self.image[n-1+k][n-ind-1+k] = self.image[n-ind-1+k][k]
            self.image[n-ind-1+k][k] = top
            ind += 1

    def rotate_90_left_using_buffer(self):
        n = self.n
        for i in range(int(self.n/2)):
            self.rotate(i, n)
            n = int(n/2 + n % 2)


if __name__ == '__main__':
    rotateMatrixObj = RotateMatrix()
    rotateMatrixObj.n = int(input("Enter n value "))
    print("Enter the NxN matrix values")
    for i in range(rotateMatrixObj.n):
        rotateMatrixObj.image.append([])
        for j in range(rotateMatrixObj.n):
            rotateMatrixObj.image[i].append(int(input()))
    rotateMatrixObj.rotate_90_left_using_buffer()
    print(rotateMatrixObj.image)

