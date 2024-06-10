# Проверяет, лежит ли точка point_to_check на прямой между point1 и point2
# Точки задаются кортежем из двух чисел: (x, y)
# delta определяет, насколько далеко точка может отстоять от прямой, чтобы считаться "лежащей" на ней 
# Чем больше delta, тем дальше точка может быть от прямой
def checkPointBetweenPoints(
    point1: tuple[int, int],
    point2: tuple[int, int],
    point_to_check: tuple[int, int],
    delta: float = 0.0
):
    def getAlpha(index: int):
        return (point_to_check[index] - point1[index]) / (point2[index] - point1[index])

    alpha_x = getAlpha(0)
    alpha_y = getAlpha(1)

    if max(alpha_x, alpha_y) - min(alpha_x, alpha_y) > delta:
        return False
    # Проверяем, не лежит ли точка на прямой, но не между point1 и point2
    if alpha_x < 0 or alpha_x > 1 or alpha_y < 0 or alpha_y > 1:
        return False
    
    return True