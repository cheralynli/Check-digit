def checknum(number):
    checker= number[-1]
    number=number.replace(" ","")
    #remove the last digit and reverse the order
    numbers= list(number[:-1][::-1])
    for i in range(len(numbers)):
        #double every second digit
        if i%2==0:
            numbers[i]=int(numbers[i])*2
        else:
            numbers[i]= int(numbers[i])
    #for digits that are greater than 9, sum the individual digits
    for j in range(len(numbers)):
        sum_digit=0
        if numbers[j]>9:
            numbers[j]= str(numbers[j])
            for k in range(len(numbers[j])):
                sum_digit+= int(numbers[j][k])
            numbers[j]= sum_digit
    #calculate the total sum
    total= sum(numbers)
    if (10-(total%10)) == int(checker):
        return "Valid"
    else:
        return "Invalid"

number= input("Enter the number to be checked: ")
print(checknum(number))