# String Compression
# Implement a method to perform basic string compression using the counts of repeated characters

class StringCompression:
    def __init__(self):
        self.input_str = ""

    def using_second_string(self):
        s_res = ""
        count = 1
        for i in range(len(self.input_str)):
            if i < len(self.input_str) - 1 and self.input_str[i] == self.input_str[i+1]:
                count += 1
            else:
                s_res = s_res + self.input_str[i] + str(count)
                count = 1
        return s_res


if __name__ == '__main__':
    stringCompressionObj = StringCompression()
    stringCompressionObj.input_str = input()
    res = stringCompressionObj.using_second_string()
    if len(res) > len(stringCompressionObj.input_str):
        print(stringCompressionObj.input_str)
    else:
        print(res)
