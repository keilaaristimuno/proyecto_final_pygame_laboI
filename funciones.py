import pygame
import constantes.colores as colores
import fuentes.fuentes as fuentes

pygame.init()

def centrar_rect(centerx, centery, rect):
    """ 
    Centra un rectangulo en base a otro.
    
    Args: 
        centerx: Valor de la coordenada x del centro.
        centry: Valor de la coordenada y del centro.
        rect: Rectangula a centrar.
        
    Returns:
        pos_et: Coordenadas del texto centradas.
    
    """
    rect.centerx = centerx
    rect.centery = centery
    
    return(rect)

def ordenar_burbujeo(lista):

    for i in range(len(lista)):
        for j in range(i, len(lista)-1):
            # Comparamos el elemento actual con el siguiente
            if lista[i]["nombre"] > lista[j]["nombre"]:
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux 
    for jugador in lista:
        jugador["nombre"]

def listar_jugadores(ventana, jugadores: list, pagina: int, jugadores_por_pagina = 10):
    
    inicio = (pagina - 1) * jugadores_por_pagina
    fin = inicio + jugadores_por_pagina
    if inicio >= len(jugadores):
        fin = inicio
    if fin > len(jugadores):
        fin = len(jugadores)
    
    pos_y = ventana.get_rect().centery - 150
    for i in range(inicio, fin):
        nombre = fuentes.FUENTE_30.render(jugadores[i]["nombre"], True, colores.NEGRO)
        ventana.blit(nombre, centrar_txt(ventana.get_rect().centerx, pos_y, nombre))
        pos_y += 35
        
def centrar_txt(centerx, centery, txt):
    
    pos_txt = txt.get_rect()
    pos_txt = centrar_rect(centerx, centery, pos_txt)
    
    return(pos_txt)
   
def crear_dic_jugador(datos_jugador: list, cabecera: list) -> dict:
    #Creo el diccionario del jugador
    jugador  = {}
    
    #Recorro la cabecera y completo el diccionario
    for i in range(len(cabecera)):
        jugador[cabecera[i]] = datos_jugador[i]
    
    #Normalizo los datos del diccionario
    normalizar_datos_jugador(jugador)
    return jugador

def normalizar_datos_jugador(diccionario: dict) -> None:
    
    diccionario["monedas"] = int(diccionario["monedas"])
    diccionario["gemas"] = int(diccionario["gemas"])
    diccionario["nivel_exp"] = int(diccionario["nivel_exp"])
    diccionario["puntaje_exp"] = diccionario["puntaje_exp"].split("/")
    diccionario["record_monedas"] = int(diccionario["record_monedas"])
    parsear_lista(diccionario["puntaje_exp"], "int")
    
def parsear_lista(lista:list, tipo_dato: str):
    
    match tipo_dato:
        case "int":
            for i in range(len(lista)):
                lista[i] = int(lista[i])
        case "str":
            for i in range(len(lista)):
                lista[i] = str(lista[i])
        
def crear_lista_jugadores(datos: list, cabecera: list) -> list:
    """Crea una lista

    Args:
        datos (list): lista 
        cabecera (list): _description_

    Returns:
        list: _description_
    """
    #Creo la lista de jugadores
    lista_jugadores = []
    
    #Recorro la lista de los datos
    for elemento in datos:
        datos_jugador = elemento.split(",")
        lista_jugadores.append(crear_dic_jugador(datos_jugador,cabecera))  
        
    return lista_jugadores

def pintar_btn(rect_btn, pos_mouse, color_n, color_h):
    
    #Valido si el mouse esta sobre el boton
    if rect_btn.collidepoint(pos_mouse):
        #El mouse esta sobre el boton entonces retorno el color hover
        return color_h
    else:
        #El mouse no esta sobre el boton entonces retorno el color normal
        return color_n
 
def validar_click_en_boton(lista_eventos, pos_mouse, boton):
    
    for evento in lista_eventos:
        #Valido que el evento sea un click y este dentro del cuadro de texto
        if evento.type == pygame.MOUSEBUTTONDOWN and boton.collidepoint(pos_mouse) and evento.button == 1:   
            return True
        elif evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
            return False

def crear_jugador(jugadores, juego):
    # Si el jugador no está en la lista, agrégalo
    nuevo_jugador = {
        "nombre": juego.nombre_jugador.strip(),
        "monedas": juego.monedas,
        "gemas": juego.gemas,
        "nivel_exp": juego.nivel_jugador,
        "puntaje_exp": [0,10],
        "record_monedas": juego.record_monedas
    }
    jugadores.append(nuevo_jugador)
    juego.logear(nuevo_jugador)

def obtener_categoria(juego):
    
    match juego.categoria:
        
        case "b":
            categoria = "Banderas"
        case "c":
            categoria = "Comidas"
        case "e":
            categoria = "Equipos"
        case "a":
            categoria = "Autos"
        case "t":
            categoria = "Tecnologia"
    
    return categoria

def obtener_archivo_categoria(juego):
    
    match juego.categoria:
        case "b":
            categoria = "datos_banderas.json"
        case "c":
            categoria = "datos_comidas.json"
        case "e":
            categoria = "datos_equipos.json"
            
    return categoria

def obtener_dificultad(juego):

    match juego.dificultad:
        case "f":
            dificultad = "Facil"
        case "n":
            dificultad = "Normal"
        case "d":
            dificultad = "Dificil"
    
    return dificultad

def validar_dificultad_seleccionada(juego, btn_dif_f, btn_dif_n, btn_dif_d):
    match juego.dificultad:
        case "f":
            btn_dif_f.color = colores.VERDE_C
            btn_dif_n.color = colores.OCRE
            btn_dif_d.color = colores.ROJO_O
        case "n":
            btn_dif_f.color = colores.VERDE
            btn_dif_n.color = colores.AMARILLO
            btn_dif_d.color = colores.ROJO_O
        case "d":
            btn_dif_f.color = colores.VERDE
            btn_dif_n.color = colores.OCRE
            btn_dif_d.color = colores.ROJO_C
            
def validar_categoria_seleccionada(juego, btn_cat_banderas, btn_cat_comidas, btn_cat_equipos, btn_cat_autos, 
                                   btn_cat_tecno):
    match juego.categoria:
        case "b":
            btn_cat_banderas.color = colores.VERDE
            btn_cat_banderas.hover = colores.VERDE
            btn_cat_comidas.color = colores.GRIS
            btn_cat_comidas.hover = colores.GRIS_C
            btn_cat_equipos.color = colores.GRIS
            btn_cat_equipos.hover = colores.GRIS_C
            btn_cat_autos.color  = colores.GRIS
            btn_cat_autos.hover = colores.GRIS_C
            btn_cat_tecno.color = colores.GRIS
            btn_cat_tecno.hover = colores.GRIS_C
        case "c":
            btn_cat_banderas.color = colores.GRIS
            btn_cat_banderas.hover = colores.GRIS_C
            btn_cat_comidas.color = colores.VERDE
            btn_cat_comidas.hover = colores.VERDE
            btn_cat_equipos.color = colores.GRIS
            btn_cat_equipos.hover = colores.GRIS_C
            btn_cat_autos.color  = colores.GRIS
            btn_cat_autos.hover = colores.GRIS_C
            btn_cat_tecno.color = colores.GRIS
            btn_cat_tecno.hover = colores.GRIS_C
        case "e":
            btn_cat_banderas.color = colores.GRIS
            btn_cat_banderas.hover = colores.GRIS_C
            btn_cat_comidas.color = colores.GRIS
            btn_cat_comidas.hover = colores.GRIS_C
            btn_cat_equipos.color = colores.VERDE
            btn_cat_equipos.hover = colores.VERDE
            btn_cat_autos.color  = colores.GRIS
            btn_cat_autos.hover = colores.GRIS_C
            btn_cat_tecno.color = colores.GRIS
            btn_cat_tecno.hover = colores.GRIS_C
        case "a":
            btn_cat_banderas.color = colores.GRIS
            btn_cat_banderas.hover = colores.GRIS_C
            btn_cat_comidas.color = colores.GRIS
            btn_cat_comidas.hover = colores.GRIS_C
            btn_cat_equipos.color = colores.GRIS
            btn_cat_equipos.hover = colores.GRIS_C
            btn_cat_autos.color  = colores.GRIS_C
            btn_cat_autos.hover = colores.GRIS_C
            btn_cat_tecno.color = colores.GRIS
            btn_cat_tecno.hover = colores.GRIS_C
        case "t":
            btn_cat_banderas.color = colores.GRIS
            btn_cat_banderas.hover = colores.GRIS_C
            btn_cat_comidas.color = colores.GRIS
            btn_cat_comidas.hover = colores.GRIS_C
            btn_cat_equipos.color = colores.GRIS
            btn_cat_equipos.hover = colores.GRIS_C
            btn_cat_autos.color  = colores.GRIS
            btn_cat_autos.hover = colores.GRIS_C
            btn_cat_tecno.color = colores.GRIS_C
            btn_cat_tecno.hover = colores.GRIS_C

def validar_enter(lista_eventos):
    for evento in lista_eventos:
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_RETURN:
                return True
            
def resetear_btns_rtas(btns:  list):
    
    for btn in btns:
        btn.color = colores.AZUL_O
        btn.hover = colores.CELESTE
        
def set_cabecera_csv(cabecera: list, csv_txt):
    
    for i in range(len(cabecera)):
        if i < len(cabecera) -1:
            csv_txt += cabecera[i] + ","
        else:
            csv_txt += cabecera[i] 
    return csv_txt

def set_data_csv(data: list, csv_txt: str, juego) -> str:

    set_datos_jugador_csv(data, juego)
    
    for i in range(len(data)):
        parsear_lista(data[i]["puntaje_exp"], "str")
        data[i]["puntaje_exp"] = "/".join(data[i]["puntaje_exp"])
        data_linea = list(data[i].values())
        for j in range(len(data_linea)):
            if j < len(data_linea)-1:
                if j == 0:
                    csv_txt += "\n"
                csv_txt += str(data_linea[j]) + ","
            else:
                csv_txt += str(data_linea[j])
    return csv_txt

def set_datos_jugador_csv(data, juego):
    # Verifica si el jugador ya está en la lista y actualiza sus datos
    for jugador in data:
        if jugador["nombre"] == juego.nombre_jugador:
            jugador["monedas"] = juego.monedas
            jugador["gemas"] = juego.gemas
            jugador["nivel_exp"] = juego.nivel_jugador
            jugador["record_monedas"] = juego.record_monedas
            break 
        # Si se encuentra el jugador, se actualizan los datos y se retorna la lista

def mostrar_cartel_record(ventana,juego):
    
    titulo_record = fuentes.FUENTE_30.render("NUEVO RECORD DE MONEDAS ", True, colores.VIOLETA_O, colores.CREMA)
    record_viejo = fuentes.FUENTE_25.render(f" Su record anterior: {juego.record_monedas}", True, colores.VIOLETA, colores.CREMA)
    record_nuevo = fuentes.FUENTE_25.render(f" Su record nuevo: {juego.monedas}", True, colores.VIOLETA, colores.CREMA)
    ventana.blit(titulo_record,centrar_txt(ventana.get_rect().centerx, ventana.get_rect().centery - 50 , titulo_record) )
    ventana.blit(record_viejo,centrar_txt(ventana.get_rect().centerx, ventana.get_rect().centery + 50 , record_viejo) )
    ventana.blit(record_nuevo,centrar_txt(ventana.get_rect().centerx, ventana.get_rect().centery , record_nuevo) )
    pygame.display.update()  #actualizar la pantalla para mostrar el cambio
    
def mostrar_mensaje(ventana, mensaje):
    
    ventana.blit(mensaje,centrar_txt(ventana.get_rect().centerx, ventana.get_rect().centery, mensaje) )
    pygame.display.update()  #actualizar la pantalla para mostrar el cambio