import match, visual

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
    
P = match.create_random_points(1000)
R = []
sobras = []
indexPuntosApareados = []
i = 0
largoP = len(P)
while(i < largoP):
    p1 = P[i]
    j=i+1
    p2 = P[j]
    flag = True
    while flag:
        if p1.color == p2.color:
            R.append(match.Rectangle(p1,p2))
            flag = False
        else:
            sobras.append(p2)
            j = j+1
            p2 = P[j]

   

