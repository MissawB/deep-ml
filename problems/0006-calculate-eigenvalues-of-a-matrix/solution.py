import math

def calculate_eigenvalues(matrix: list[list[float | int]]) -> list[float]:
    tr = matrix[0][0] + matrix[1][1]
    det = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    delta = tr**2 - 4 * det

    if delta < 0:
        # Valeurs propres complexes (retourne une liste vide ou gère les complexes)
        return []
    elif delta == 0:
        # Racine double
        lambda_val = tr / 2
        return [lambda_val, lambda_val]
    else:
        # Deux racines réelles distinctes
        sqrt_delta = math.sqrt(delta)
        lambda_1 = (tr + sqrt_delta) / 2
        lambda_2 = (tr - sqrt_delta) / 2
        return [lambda_1, lambda_2]