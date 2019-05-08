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


def usado(pos, indexPuntosApareados):
    """Función que verifica si el punto entregado está apareado usando su index.

    :param pos: Posición del punto en P.
    :param indexPuntosApareados: Lista de puntos apareados.
    :returns: Si ya está apareado retorna True, si no False.
    :rtype: Bool.

    """
    for i in indexPuntosApareados:
        if pos in i:
            return True
    return False

def interseccionRectangulos(R, p1, p2):
    if len(R) == 0:
        return False
    r = R[-1]
    if (p1.y < r.bottom and p2.y < r.bottom) or (p1.y > r.top and p2.y > r.top):
        return False
    return True


P = match.create_random_points(50)
P.sort(key=lambda x: x.x)
R = []
sobras = []
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
            if p1.color == p2.color and (j not in indexPuntosApareados) and not interseccionRectangulos(R, p1, p2) and not adentro(P, p1, p2):
                if p1.y > p2.y:
                    R.append(match.Rectangle(p1.x, p2.x, p1.y, p2.y))
                    indexPuntosApareados.append(i)
                    indexPuntosApareados.append(j)
                    flag = False
                    print("rectángulo")
                else:
                    R.append(match.Rectangle(p1.x, p2.x, p2.y, p1.y))
                    print("rectángulo")
                    indexPuntosApareados.append(i)
                    indexPuntosApareados.append(j)
                    flag = False
            else:
                sobras.append(p2)
                j += 1
    i += 1

visual.Window(P, R)
