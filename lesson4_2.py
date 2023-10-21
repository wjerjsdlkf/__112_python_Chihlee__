import pyinputplus as pyip

scores = pyip.inputInt("請輸入學生分數(最高幾分):",min=0,max=300)
print(scores)
#isYes = pyip.inputBool("學生是否符合加分條件?(y,n)",trueVal=True,falseVal=False)
isYes = pyip.inputMenu(['y','n'],prompt="學生是否符合加分條件?(y,n)\n",numbered=True)


print(isYes)