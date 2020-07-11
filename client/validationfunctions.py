def ValidateIntRange(numToValidate, rangeStart, rangeEnd):
        if int(numToValidate) >= int(rangeStart) and int(numToValidate) <= int(rangeEnd):
            return True
        else:
            return False

def ValidateIntGreaterThan(numToValidate, greaterThanNum):
    if int(numToValidate) > int(greaterThanNum):
        return True
    else:
        return False

def ValidateIntLessThan(numToValidate, lessThanNum):
    if int(numToValidate) < int(lessThanNum):
        return True
    else:
        return False

def ValidateIntGreaterThanOrEqual(numToValidate, greaterThanNum):
    if int(numToValidate) >= int(greaterThanNum):
        return True
    else:
        return False

def ValidateIntLessThanOrEqual(numToValidate, lessThanNum):
    if int(numToValidate) <= int(lessThanNum):
        return True
    else:
        return False
