#-------------------------------------------------------------------------------
# Name:        add_product
# Purpose:
#
# Author:      Xenia
#
# Created:     05.08.2018
# Copyright:   (c) Xenia 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

f = open('base.csv', 'r')
text = f.read()
now_text = text
f.close()

code = input().strip('\n')
name = input()
now_text += code + ';' + name + ';\n'

f = open('base.csv', 'w')
f.write(now_text)
f.close()

f = open('price.csv', 'r')
text = f.read()
now_text = text
f.close()

cost = input().strip('\n')
now_text += code + ';' + cost + ';\n'

f = open('price.csv', 'w')
f.write(now_text)
f.close()

