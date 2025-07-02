import numpy as np
import matplotlib.pyplot as plt

# Parametry
a = 1  # Możesz zmienić wartość a
phi = np.linspace(0, 2 * np.pi, 1000)  # Kąty od 0 do 2π

# Równanie krzywej
r = a * np.cos(3 * phi)

# Konwersja do układu kartezjańskiego
x = r * np.cos(phi)
y = r * np.sin(phi)

# Rysowanie
plt.figure(figsize=(6, 6))
plt.plot(x, y)
plt.title(r'Krzywa $r = a \cos(3\phi)$')
plt.xlabel('x')
plt.ylabel('y')
plt.axis('equal')
plt.grid()
plt.show()
