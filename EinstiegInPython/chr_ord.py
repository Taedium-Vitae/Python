# Ziffern
for i in range(48,58):
    print(chr(i), end="")
print()

# grosse buchstaben
for i in range(65,91):
    print(chr(i), end="")
print()

# kleine buchstaben
for i in range(97, 123):
    print(chr(i), end="")
print()

# codenummern
for z in "Robinson":
    print(ord(z), end=" ")
print()

# verschoben
for z in "Robinson":
    print(chr(ord(z)+1), end="")
