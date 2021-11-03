
def validateCPF(cpf):
    #list compreheension
    listChar = [int(digit) for digit in cpf if digit.isdigit()]
    
    sum = 0
    for i in range(10,1,-1):
        sum += listChar[10-i]*i
    
    resto = sum % 11
    if resto < 2:
        if listChar[9] != 0:
            return False
    elif listChar[9] != (11-resto):
        return False
    
    sum = 0
    for i in range(11,1,-1):
        sum += listChar[11-i]*i

    resto = sum % 11

    if resto < 2:
        if listChar[10] != 0:
            return False
    elif listChar[10] != (11-resto):
        return False

    return True


if __name__ == '__main__':
    print(validateCPF("479.122.348-41"))