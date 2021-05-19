# URLify
# Write a method to replace all spaces with %20


class URLify:
    def __init__(self):
        self.string = None

    def using_brute_force(self):
        self.string = list(self.string)
        end = 0

        for end in range(len(self.string)-1, -1, -1):
            if self.string[end] != " ":
                break

        ind = len(self.string) - 1
        for i in range(end, -1, -1):
            if self.string[i] != " ":
                self.string[ind] = self.string[i]
                ind -= 1
            else:
                self.string[ind] = '0'
                self.string[ind-1] = '2'
                self.string[ind-2] = '%'
                ind -= 3
                i -= 2

        return "".join(self.string)


if __name__ == '__main__':
    urlifyObj = URLify()
    input_str = input()
    urlifyObj.string = input_str
    print(urlifyObj.using_brute_force())


