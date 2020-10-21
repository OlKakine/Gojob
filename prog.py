def closestToZero(integers):
  #when integers is undefined or empty: return 0
  if not isinstance(integers, list) or len(integers)==0:
    return 0
  

  #now integers has at least one element
  integersClosestToZero = [integers[0]]
  #this array contains the current integers closest to zero: its max size is 2, when it contains both the positive and negative version of the integer 

  #when an integer closer to zero is found, we create a new list containing this new integer
  for integer in integers:    
    absInteger = abs(integer)
    absCurrentClosest = abs(integersClosestToZero[0])

    if absInteger < absCurrentClosest:
      integersClosestToZero = [integer]
    
    #when an integer is as close to zero as the current closest, and has a different sign, we add it to our list
    elif absInteger == absCurrentClosest and integer not in integersClosestToZero: 
        integersClosestToZero.append(integer)

  #we return the maximum integer from our list: it will be the positive one
  return max(integersClosestToZero)

def testOnlyPositive():
  assert closestToZero([8,5,12]) == 5

def testOnlyNegative():
  assert closestToZero([-8,-5,-12]) == -5

def testPosAndNeg():
  assert closestToZero([5, 4, -9, 6, -10, -1, 8]) == -1

def testPositiveOneIsReturned():
  assert closestToZero([8,2,-3,-2]) == 2

def testUndefinedOrEmpty():
  assert closestToZero(None) == 0
  assert closestToZero([]) == 0
  assert closestToZero(1) == 0
  assert closestToZero("test") == 0
  assert closestToZero(set()) == 0
  assert closestToZero(dict()) == 0
  assert closestToZero(tuple) == 0

testOnlyPositive()
testOnlyNegative()
testPosAndNeg()
testPositiveOneIsReturned()
testUndefinedOrEmpty()
#in python there is no maximum integer, so we do not have to check the limit cases when the integers are big