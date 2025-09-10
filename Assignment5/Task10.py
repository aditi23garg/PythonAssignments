numbers = [1,2,3,4,5,6,7,8,9,10]
extracted = []
for i in numbers:
    if i <=5:
        extracted.append(i)
print("Extracted first five elements:",extracted)
reversed = extracted[::-1]
print("Reversed extracted elements:", reversed)