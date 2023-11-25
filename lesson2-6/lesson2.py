side = int(input('請輸入對邊：'))
another_side = int(input('請輸入斜邊：'))

import math
radian = math.asin(side/another_side) #tuple  asin計算弧度
degree = math.degrees(radian) #degrees 弧度轉角度
print(round(degree,ndigits=2)) #round 4捨5入 ndigits 小數點幾位



