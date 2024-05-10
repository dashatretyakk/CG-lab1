import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

def is_inside_trapezoid(trapezoid, point):
  """
  Функція, яка перевіряє, чи знаходиться точка всередині трапеції.
  """
  x, y = point
  x1, y1, x2, y2, x3, y3, x4, y4 = trapezoid

  # Використовуємо орієнтацію для перевірки, чи точка лежить всередині трапеції
  def orientation(p, q, r):
      val = (float(q[1] - p[1]) * (r[0] - q[0])) - (float(q[0] - p[0]) * (r[1] - q[1]))
      return val

  if (orientation((x1, y1), (x2, y2), (x, y)) < 0 and
      orientation((x2, y2), (x3, y3), (x, y)) < 0 and
      orientation((x3, y3), (x4, y4), (x, y)) < 0 and
      orientation((x4, y4), (x1, y1), (x, y)) < 0):
      return True
  else:
      return False

def point_location(trapezoids, point):
  """
  Функція для локалізації точки у трапеції.
  """
  for trapezoid in trapezoids:
      if is_inside_trapezoid(trapezoid, point):
          return trapezoid

  # Якщо точка не належить жодній трапеції, повертаємо None
  return None

def split_polygon_to_trapezoids(polygon):
    """
    Функція для розбиття багатокутника на трапеції.
    """
    trapezoids = []
    n = len(polygon)
    for i in range(n):
        x1, y1 = polygon[i]
        x2, y2 = polygon[(i + 1) % n]
        x3, y3 = polygon[(i + 2) % n]
        x4, y4 = polygon[(i + 3) % n]
        trapezoids.append((x1, y1, x2, y2, x3, y3, x4, y4))
    return trapezoids

# Координати багатокутника
polygon_coords = [(1, 2), (2, 1), (4, 1), (5, 2), (6, 4), (5, 6), (4, 7), (2.5, 6.5), (1.5, 5.5)]

# Розбиття багатокутника на трапеції
trapezoids = split_polygon_to_trapezoids(polygon_coords)

point = (2, 2)  # координати точки
result_trapezoid = point_location(trapezoids, point)

# Відображення графіки
fig, ax = plt.subplots()

# Відображення багатокутника
ax.add_patch(Polygon(polygon_coords, closed=True, fill=None))

# Відображення трапецій
for trap in trapezoids:
    ax.add_patch(Polygon([(trap[i], trap[i+1]) for i in range(0, len(trap), 2)], closed=True, fill=None))

# Відображення точки
ax.plot(*point, 'ro')

ax.autoscale()
plt.grid()
plt.show()

if result_trapezoid:
    print("Точка знаходиться у трапеції:", result_trapezoid)
else:
    print("Точка не знаходиться у жодній трапеції.")
