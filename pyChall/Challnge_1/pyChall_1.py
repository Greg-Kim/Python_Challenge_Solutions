# Python_Challenge_1
# http://www.pythonchallenge.com/pc/def/map.html

class Caesar:
    def __init__(self, string):
        self.plain_text = list(string)
        self.shift_text = []

    def shift(self, key):
        for i in self.plain_text:
            if 'a' <= i and i <= 'z':
                self.shift_text += chr(((ord(i)-97+key)%26)+97)
            else:
                self.shift_text += i

        return ''.join(self.shift_text)
        

def main():
    plain = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq "
    plain += "glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. "
    plain += "lmu ynnjw ml rfc spj. "
    plain += "map"
    
    key = 2

    caesar = Caesar(plain)
    result = caesar.shift(key)
    print(result)

main()