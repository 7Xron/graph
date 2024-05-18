numVar = 1
strVar = 'МИИГАиК'
boolVar = True
print(numVar, strVar, boolVar)
numVar = numVar + 1
strVar = "Привет, " + strVar + "!"
boolVar = not boolVar
print(numVar, strVar, boolVar)


a = [1,2,3]
print(a, len(a))
a.append("МИИГАиК")
print(a, len(a))
a.remove(2)
print(a, len(a))
print(a[2])
