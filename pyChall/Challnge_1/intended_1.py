# Intended_Solution_1   using 'str.maketrans()'
# http://www.pythonchallenge.com/pc/def/map.html

import string

def main():
    plain = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq "
    plain += "glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. "
    plain += "lmu ynnjw ml rfc spj. "
    plain += "map"

    map_in = "abcdefghijklmnopqrstuvwxyz"
    map_out = "cdefghijklmnopqrstuvwxyzab"

    mapping = str.maketrans(map_in, map_out)

    print(plain.translate(mapping))

main()