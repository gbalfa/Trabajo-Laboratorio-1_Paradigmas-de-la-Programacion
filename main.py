import time
import match
import visual


def puntoEnInterior(P, index_p1, index_p2):
    """Función que verifica si hay puntos al interior del rectángulo formado
    por los puntos p1 y p2.

    :param P: Puntos ordenados según su coordenada x de forma creciente.
    :param index_p1: Index punto p1 en P.
    :param index_p2: Index punto p2 en P.
    :returns:  True si es que hay puntos dentro, False si no.
    :rtype: Bool.

    """
    for i in range(index_p1 + 1, index_p2):
        if ((P[index_p1].y < P[i].y and P[i].y < P[index_p2].y)
                or (P[index_p2].y < P[i].y and P[i].y < P[index_p1].y)):
            return True
    return False


def superposicionRectangulos(R, p1, p2):
    """Función que verifica si el rectángulo formado por los puntos p1 y p2 no
    superpone rectángulos previamente creados.

    *Es más probable que el rectángulo formado entre p1 y p2 superponga rectán
    -gulos creados recientemente(más cercanos), por lo tanto, la iteración se
    realiza desde el final al inicio de la lista.

    :param R: Lista de rectángulos.
    :param p1: Punto de menor componente x(p1.x < p2.x).
    :param p2: Punto.
    :returns: True si hay superposición de rectángulos, False si no.
    :rtype: Bool.

    """
    largoR = len(R)
    if largoR == 0:
        return False
    for i in range(-1, -largoR - 1, -1):
        r = R[i]
        if p1.x < r.right:
            if not ((p1.y < r.bottom and p2.y < r.bottom) or
                    (p1.y > r.top and p2.y > r.top)):
                return True
    return False


def heuristica(P, largoP):
    """Busca en un tiempo de cómputo razonable, la mayor cantidad de duplas que
    pueda de manera tal que estas puedan ser simultáneamente apareadas.

    *El algoritmo barre el eje x de izquierda a derecha con el iterador i. Por
    cada P[i] se busca en los puntos posteriores el primer P[j] que sea un
    apareamiento válido de acuerdo a criterios definidos y lo aparea.

    :param P: Lista de puntos.
    :param largoP: Cantidad de puntos.
    :returns: Lista R de objetos match.Rectangle, correspondientes a cada una
    de las duplas.
    :rtype: Lista.

    """
    P.sort(key=lambda x: x.x)
    boolIndexPuntosApareados = [False] * largoP
    R = []
    for i in range(largoP):
        if (not boolIndexPuntosApareados[i]):
            p1 = P[i]
            for j in range(i + 1, largoP):
                p2 = P[j]
                if (p1.color == p2.color) and (
                        not boolIndexPuntosApareados[j]) and (
                            not puntoEnInterior(P, i, j)) and (
                                not superposicionRectangulos(R, p1, p2)):
                    R.append(
                        match.Rectangle(p1.x, p2.x, min(p1.y, p2.y),
                                        max(p1.y, p2.y)))
                    boolIndexPuntosApareados[j] = True
                    break
    return R


def aparear(n):
    P = match.create_random_points(n)
    start = time.time()
    R = heuristica(P, n)
    end = time.time()
    tiempo = " Tiempo: " + str(end - start) + " segundos"
    windowTitle = str(n) + " puntos:  " + (str(len(R) * 2 / n * 100) + "%" +
                                           tiempo)
    visual.Window(P, R, windowTitle)
    return
