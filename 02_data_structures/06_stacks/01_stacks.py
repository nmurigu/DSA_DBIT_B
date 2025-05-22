stack = []
print(type(stack))

print(f" Initial stack: {stack}")

stack.append(10)
stack.append(20)
stack.append(30)
stack.append(40)
stack.append(50)
stack.append(60)

print(f"  After pushing : {stack}")


popped = stack.pop()
# del stack[-1]
print(f"  Popped item: {popped}")
print(f"  Stack after pop: {stack}")

if stack:
    print(f" Top of stack: {stack[-1]}")
else:
    print(f" Stack is empty")

stack = []
print(f"  Is stack empty? {len(stack) == 0}")

print(f"  Stack contents (top to bottom):")
for item in reversed(stack):
    print(f" {item}")
