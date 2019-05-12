import match
import visual


def puntoEntremedio(P, index_p1, index_p2):
    """Función que verifica si hay puntos dentro de el rectángulo formado entre los puntos p1 y p2.

    :param P: Puntos ordenados segun su coordenada x de menor a mayor.
    :param index_p1: Index punto en P.
    :param index_p2: Index punto en P.
    :returns:  True si es que hay puntos dentro y False si no.
    :rtype: Bool.

    """
    for i in range(index_p1+1, index_p2):
        if ((P[index_p1].y < P[i].y and P[i].y < P[index_p2].y) or (P[index_p2].y < P[i].y and P[i].y < P[index_p1].y)):
            return True
    return False

def busquedaInversa(L, x):
    largoL = len(L)
    i = -1
    while(-largoL <= i and x <= L[i]):
        if L[i] == x:
            return True
        i -= 1
    return False
    
def insercionOrdenada(L, x):
    L.append(x)
    largoL = len(L)
    if largoL == 1:
        return 
    i = -2
    while(-largoL <= i and x < L[i]):
        L[i+1] = L[i]
        i = i - 1
    L[i+1] = x
    return 



def interseccionRectangulos(R, p1, p2):
    largoR = len(R)
    if largoR == 0:
        return False
    for i in range(-1, -largoR-1, -1):
        r = R[i]
        if p1.x < r.right:
            ymax = max(r.bottom, r.top)
            ymin = min(r.bottom, r.top)
            if not ((p1.y < ymin and p2.y < ymin) or (p1.y > ymax and p2.y > ymax)):
                return True

    return False


def heuristica(P):
    P.sort(key=lambda x: x.x)
    R = []
    indexPuntosApareados = []
    i = 0
    largoP = len(P)
    for i in range(largoP):
        p1 = P[i]
        if (not busquedaInversa(indexPuntosApareados, i)):
            for j in range(i+1, largoP):
                p2 = P[j]
                if (p1.color == p2.color) and (not busquedaInversa(indexPuntosApareados, j)) and (not puntoEntremedio(P, i, j)) and (not interseccionRectangulos(R, p1, p2)):
                    R.append(match.Rectangle(p1.x, p2.x, p1.y, p2.y))
                    insercionOrdenada(indexPuntosApareados, j)
                    break
    return R


n = 10000
print(n)
P = match.create_random_points(n)
R = heuristica(P)
porcentaje = (str(len(R)*2/n*100) + "%")
visual.Window(P, R, porcentaje)
