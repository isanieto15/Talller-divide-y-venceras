#Isabella Nieto Cardona

import csv

def merge(izq, der):
    resultado = []
    i = j = 0
    while i < len(izq) and j < len(der):
        
        if (izq[i]["calificacion"] > der[j]["calificacion"]) or \
           (izq[i]["calificacion"] == der[j]["calificacion"] and izq[i]["precio"] < der[j]["precio"]):
            resultado.append(izq[i]); i += 1
        else:
            resultado.append(der[j]); j += 1
    resultado.extend(izq[i:])
    resultado.extend(der[j:])
    return resultado

def merge_sort(lista):
    if len(lista) <= 1:
        return lista
    mid = len(lista)//2
    izq = merge_sort(lista[:mid])
    der = merge_sort(lista[mid:])
    return merge(izq, der)



productos = []
with open("productos (1).csv", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        row["id"] = int(row["id"])
        row["precio"] = float(row["precio"])
        row["calificacion"] = int(row["calificacion"])
        row["stock"] = int(row["stock"])
        productos.append(row)


ordenados = merge_sort(productos)

print("Top 10 productos:\n")
for p in ordenados[:10]:
    print(f"ID:{p['id']} | {p['nombre']} | {p['calificacion']} | ${p['precio']} | Stock:{p['stock']}")

#nuevo archivo para guardar los productos ordenados

with open("productos_ordenados.csv", "w", newline="", encoding="utf-8") as f:
    fieldnames = ["id", "nombre", "precio", "calificacion", "stock"]
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(ordenados)

print("Archivo guardado como productos_ordenados.csv")
        
            