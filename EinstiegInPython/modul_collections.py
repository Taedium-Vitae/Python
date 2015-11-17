# Modul
import collections

# Erzeugen
d = collections.deque("abc")
print("Neu:", d)

# Elemente
for x in d:
    print("Element:", x)

# hinzu links, rechts
d.appendleft(5)
d.append(25)
print("Hinzu:", d)

# erweitern links, rechts
d.extendleft([7,9])
d.extend([17,19])
print("Erweitert:", d)

# entfernen links, rechts
li = d.popleft()
print("Links:", li)
re = d.pop()
print("Rechts:", re)
print("Entfernt:", d)

# Rotieren
d.rotate()
print("Rotiert +1:", d)
d.rotate(-2)
print("Rotiert -2:", d)

# leeren
d.clear()
print("Geleert:", d)
