def matrix_determinant_and_trace(matrix: list[list[float]]) -> tuple[float, float]:
    """
    Compute the determinant and trace of an n x n square matrix.
    
    Args:
        matrix: A square matrix (n x n) represented as a list of lists.
        
    Returns:
        Tuple of (determinant, trace).
    """
    n = len(matrix)
    if n == 0:
        return 0.0, 0.0

    tr = sum(matrix[i][i] for i in range(n))

    # Cas de base 1x1
    if n == 1:
        return float(matrix[0][0]), float(tr)

    # On crée une copie pour ne pas modifier la matrice originale
    mat = [row[:] for row in matrix]
    det = 1.0

    for i in range(n):
        # Recherche du pivot maximal dans la colonne i pour stabilité numérique
        pivot_row = i
        for r in range(i + 1, n):
            if abs(mat[r][i]) > abs(mat[pivot_row][i]):
                pivot_row = r
                
        # Si le pivot est nul, la matrice n'est pas inversible -> det = 0
        if abs(mat[pivot_row][i]) < 1e-12:
            return 0.0, float(tr)

        # Échange des lignes si nécessaire (change le signe du déterminant)
        if pivot_row != i:
            mat[i], mat[pivot_row] = mat[pivot_row], mat[i]
            det = -det

        det *= mat[i][i]
        pivot = mat[i][i]

        # Élimination des éléments sous le pivot
        for r in range(i + 1, n):
            factor = mat[r][i] / pivot
            for c in range(i, n):
                mat[r][c] -= factor * mat[i][c]

    return float(det), float(tr)