from typing import List

def merge_sort(data) -> None:
  # Write code here
  l=data.length
  n=l/2
  
  if len(data) > 1:
    mid = len(data)//2
    left= data[:mid]
    right= data[mid:]
    
    merge_sort(left)
    merge_sort(right)
  return data


# Do not change the following code
input_data = input()
data = []
for item in input_data.split(', '):
  if item.isnumeric():
    data.append(int(item))
  elif item.lstrip("-").isnumeric():
    data.append(int(item))
merge_sort(data)
print(data)
