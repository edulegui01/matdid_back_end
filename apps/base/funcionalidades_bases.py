from asyncio.windows_events import NULL


def cargar_datos(claves,valores):
    datos={}
    for i in range(len(claves)):
        datos[claves[i]] = valores[i]
    
    return datos


def carga_detalle(claves,valores,detalle):
    index_detalle = claves.index(detalle)
    detalle_compra = valores[index_detalle]

    return detalle_compra

def carga_detalle_compra(claves,valores,modelo,detalle,id_valor,id_update=NULL):
    detalles_g = carga_detalle(claves,valores,detalle)
    print(id_update)
    for detalle in detalles_g:
        if id_update != NULL:
            detalle[id_valor]=id_update
        else:
            detalle[id_valor]=modelo.objects.values('id').latest('id')['id']
    
    return detalles_g


