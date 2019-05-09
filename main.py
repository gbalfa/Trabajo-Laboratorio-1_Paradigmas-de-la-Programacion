import match
import visual


def adentro(P, p1, p2):
    """Función que verifica si hay puntos dentro de el rectángulo formado entre los puntos p1 y p2.

    :param P: Puntos ordenados segun su coordenada x de menor a mayor.
    :param p1: Punto.
    :param p2: Punto.
    :returns:  True si es que hay puntos dentro y False si no.
    :rtype: Bool.

    """
    posP1 = P.index(p1)
    posP2 = P.index(p2)
    for i in range(posP1+1, posP2):
        if (p1.x < P[i].x and P[i].x < p2.x) and ((p1.y < P[i].y and P[i].y < p2.y) or (p2.y < P[i].y and P[i].y < p1.y)):
            return True
    return False


def interseccionRectangulos(R, p1, p2):
    largoR = len(R)
    if largoR == 0:
        return True
    i = -1
    r = R[i]
    flag = True
    for r in [x for x in R if p1.x < x.right]:
        ymax = max(r.bottom, r.top)
        ymin = min(r.bottom, r.top)
        if ((p1.y < ymin and p2.y < ymin) or (p1.y > ymax and p2.y > ymax)):
            flag = True
        else:
            return False

    return flag


def heuristica(P):
    P.sort(key=lambda x: x.x)
    R = []
    indexPuntosApareados = []
    i = 0
    largoP = len(P)
    while(i < largoP-1):
        p1 = P[i]
        if i not in indexPuntosApareados:
            j = i+1
            flag = True
            while flag and j < largoP:
                p2 = P[j]
                if p1.color == p2.color and (j not in indexPuntosApareados) and interseccionRectangulos(R, p1, p2) and not adentro(P, p1, p2):
                    R.append(match.Rectangle(p1.x, p2.x, p1.y, p2.y))
                    indexPuntosApareados.append(i)
                    indexPuntosApareados.append(j)
                    flag = False
                else:
                    j += 1
        i += 1
    return R


n = 1000
print(n)
P = match.create_random_points(n)
R = heuristica(P)
porcentaje = (str(len(R)*2/n*100) + "%")
visual.Window(P, R, porcentaje)
