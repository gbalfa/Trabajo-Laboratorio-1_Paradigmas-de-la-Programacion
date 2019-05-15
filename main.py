import time
import match
import visual


def puntoEntremedio(P, index_p1, index_p2):
    """Función que verifica si hay puntos dentro de el rectángulo formado entre los puntos p1 y p2.

    :param P: Puntos ordenados segun su coordenada x de menor a mayor.
    :param index_p1: Index punto p1 en P.
    :param index_p2: Index punto p2 en P.
    :returns:  True si es que hay puntos dentro y False si no.
    :rtype: Bool.

    """
    for i in range(index_p1+1, index_p2):
        if ((P[index_p1].y < P[i].y and P[i].y < P[index_p2].y) or (P[index_p2].y < P[i].y and P[i].y < P[index_p1].y)):
            return True
    return False


def interseccionRectangulos(R, p1, p2):
    """Función que verifica si el rectángulo que formaría p1 y p2 no se intersecta con rectángulos previamente creados.

    Es más probable que el rectángulo formado entre p1 y p2 se intersecte con los rectángulos creados recientemente, por lo tanto,
    la búsqueda se realiza de adelante hacia atrás.

    :param R: Lista de rectángulos.
    :param p1: Punto.
    :param p2: Punto.
    :returns: True si hay interseccion de rectángulos, False si no.
    :rtype: Bool.

    """
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
    largoP = len(P)
    indexPuntosApareados = [False for i in range(largoP)]
    for i in range(largoP):
        if (not indexPuntosApareados[i]):
            p1 = P[i]
            for j in range(i+1, largoP):
                p2 = P[j]
                if (p1.color == p2.color) and (not indexPuntosApareados[j]) and (not puntoEntremedio(P, i, j)) and (not interseccionRectangulos(R, p1, p2)):
                    R.append(match.Rectangle(p1.x, p2.x, p1.y, p2.y))
                    indexPuntosApareados[j] = True
                    break
    return R


n = 10000
print(n)
P = match.create_random_points(n)
start = time.time()
R = heuristica(P)
end = time.time()
print(end - start, " segundos")
porcentaje = str(n) + " puntos:  " + (str(len(R)*2/n*100) + "%")
visual.Window(P, R, porcentaje)
