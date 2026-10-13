# Frecuencia de palabras de un texto: normaliza, separa y cuenta; muestra el top 5.
texto = "a ,b c, e, 2, a, c, d, 3, a, 2,"
SIGNOS = ".,:;!?¡¿()\"'"
def contar_palabras(texto: str) -> dict[str, int]:    		        
    limpio = texto.lower()    
    for s in SIGNOS:        
        limpio = limpio.replace(s, "") # quitar puntuación                                          # antes de separar
    conteo: dict[str, int]={}
    lista = sorted(list(limpio.split(" ")))
    for palabra in lista:
        conteo[palabra] = int(lista.count(palabra))
    conteo_orde = dict(sorted(conteo.items(), key=lambda item: item[1], reverse=True))
    print(list(conteo_orde.items())[:3])
contar_palabras(texto=texto)
