
def checkPointBetweenPoints(
    point1: tuple[int, int],
    point2: tuple[int, int],
    point_to_check: tuple[int, int],
    calc_error: float = 0.0
):
    def getAlpha(index: int):
        return (point_to_check[index] - point1[index]) / (point2[index] - point1[index])

    alpha_x = getAlpha(0)
    alpha_y = getAlpha(1)

    if max(alpha_x, alpha_y) - min(alpha_x, alpha_y) > calc_error:
        return False
    if alpha_x < 0 or alpha_x > 1 or alpha_y < 0 or alpha_y > 1:
        return False
    
    return True