def rotatematrix(matrice):
 
    if not len(matrice):
        return
     

 
    top = 0
    bottom = len(matrice)-1
 
    left = 0
    right = len(matrice[0])-1
 
    while left < right and top < bottom:
 
        previous = matrice[top+1][left]
 
        for i in range(left, right+1):
            current = matrice[top][i]
            matrice[top][i] = previous
            previous = current
 
        top += 1
 
        for i in range(top, bottom+1):
            current = matrice[i][right]
            matrice[i][right] = previous
            previous = current
 
        right -= 1
 
        for i in range(right, left-1, -1):
            current = matrice[bottom][i]
            matrice[bottom][i] = previous
            previous = current
 
        bottom -= 1
 
        for i in range(bottom, top-1, -1):
            current = matrice[i][left]
            matrice[i][left] = previous
            previous = current
 
        left += 1
 
    return matrice