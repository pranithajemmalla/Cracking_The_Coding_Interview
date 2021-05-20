
class KMPAlgorithm:
    def __init__(self):
        self.str_1 = None
        self.str_2 = None
        self.lps_array = None

    def compute_lps_array(self):
        i = 0
        j = 1
        lps_array = [0]
        while j < len(self.str_2):
            if self.str_2[i] == self.str_2[j]:
                j += 1
                i += 1
                lps_array.append(i)
            else:
                if i != 0:
                    i = lps_array[i-1]
                else:
                    j += 1
                    lps_array.append(0)
        self.lps_array = lps_array
        print(self.lps_array)
        return

    def kmp_algorithm(self):
        self.compute_lps_array()
        i = 0
        j = 0
        count = 0
        while i < len(self.str_1):
            if self.str_1[i] == self.str_2[j]:
                i += 1
                j += 1
                count += 1
            else:
                if j != 0:
                    count = j + 1
                    j = self.lps_array[j-1]
                else:
                    count = 0
                    i += 1
            if count == len(self.str_2):
                return True
        return False


if __name__ == '__main__':
    kmpAlgorithmObj = KMPAlgorithm()
    kmpAlgorithmObj.str_1 = input()
    kmpAlgorithmObj.str_2 = input()
    print(kmpAlgorithmObj.kmp_algorithm())


