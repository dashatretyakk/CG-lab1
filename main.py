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

# Приклад використання
trapezoids = [
  (0, 0, 4, 0, 3, 3, 1, 3),
  (3, 0, 7, 0, 6, 4, 4, 4),
  (1, 3, 3, 3, 2, 6, 1, 6)
]  # список трапецій розбиття

point = (5, 2)  
result_trapezoid = point_location(trapezoids, point)
if result_trapezoid:
  print("Точка знаходиться у трапеції:", result_trapezoid)
else:
  print("Точка не знаходиться у жодній трапеції.")
