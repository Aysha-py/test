from collections import deque

roll_call = deque(['shade', 'tolu', 'lyon,', 'brian', 'meghan'])

deque.popleft(roll_call)

print(roll_call)
deque.popleft(roll_call)
print(roll_call)
