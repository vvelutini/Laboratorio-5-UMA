from paquete_academico.operaciones import calcular_promedio, encontrar_maximo


def generar_resumen(lista_notas):
    print("Promedio:", calcular_promedio(lista_notas))
    print("Nota máxima:", encontrar_maximo(lista_notas))
