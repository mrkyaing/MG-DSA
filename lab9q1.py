s=""
n=10000
for i in range(n):
    s += str(i)

print("output with for loop",s)
# add new break line here
print()
# improved version using join
# This version is more efficient than concatenating strings in a loop.
s=""
print("output with join", s.join(str(i) for i in range(n)))