def Highest_Even(list):
  Max=0
  for item in list:
    if item > Max and (item % 2 ==0):
      Max=item
  return Max    

print(f'Maximum number in list is {Highest_Even([1,2,4,5,6,10,20,4])}')