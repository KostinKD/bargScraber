data = ["Bedroom", "Living", "Kitchen", "Dining", "Service"]
result = []
start = False

for value in data:
  if value == "Kitchen":
    start = True
  elif value == "Service":
    start = False
  if start:
    result.append(value)

print(result)