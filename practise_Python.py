import matplotlib.pyplot as plt

x = list(range(-10, 11))
y = [value**2 for value in x]
y2 = [value**3 for value in x]

print(f"{x = }")
print(f"{y = }")

plt.plot(x, y, label="x**2")
plt.plot(x, y2, label="x**3")
plt.legend()
plt.grid()
