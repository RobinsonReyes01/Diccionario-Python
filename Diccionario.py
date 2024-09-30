# Diccionario con información fictivia
informacion_personal = {"Nombre": "Ana García", "Edad": 28, "Pais": "España",
                        "Ciudad": "Barcelona", "Profesion": "Enfermera" }

if "telefono" not in informacion_personal:
    informacion_personal["Telefono"] = "+34 123 456 789"

del informacion_personal["edad"]

print("Diccionario final:")
print(informacion_personal)