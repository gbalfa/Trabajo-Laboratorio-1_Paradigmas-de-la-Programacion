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
    
# def usado(pos, PuntosApareados):
#     for i in PuntosApareados:
#         if 


P = match.create_random_points(10)
P.sort(key = lambda x: x.x)
R = []
sobras = []
indexPuntosApareados = []
i = 0
largoP = len(P)
while(i < largoP-1):
    p1 = P[i]
    j=i+1
    flag = True
    while flag and j < largoP:
        p2 = P[j]
        if p1.color == p2.color:
            if p1.y >p2.y:
                R.append(match.Rectangle(p1.x, p2.x, p1.y, p2.y))
            else:
                R.append(match.Rectangle(p1.x, p2.x, p2.y, p1.y))
            indexPuntosApareados.append((i,j))
            flag = False
        else:
            sobras.append(p2)
            j = j+1
    i+=1

visual.Window(P, R)
   

