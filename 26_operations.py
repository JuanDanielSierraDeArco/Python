print("Operaciones Con Conjuntos")
print()

America_sur = {'Colombia', 'Venezuela', 'Guyana', 'Surinam', 'Ecuador', 'Peru', 'Brasil', 'Bolivia', 'Paraguay', 'Chile', 'Uruguay','Argentina' }

America_central = {'Belice', 'Costa Rica', 'El Salvador', 'Guatemala', 'Honduras', 'Nicaragua', 'Panama'}

print("Paises de america del sur\n", America_sur)
print()
print("Paises de ameerica central",America_central)
print()
#Podemos crear uniones entre conjunto por el metodo "union" o por el operador "|"
America_latina = America_sur.union(America_central)
print("Paises de america latina\n", America_latina)

#Interseccion de conjunto utilizando el metodo "intersection" o por el operador "&"
print()
Inter_Paises = America_latina.intersection(America_sur)
print("paises de america del sur presentes en america latina\n", Inter_Paises)

#diferencia de conjuntos utilizando el metodo "intersection" o por el operador "-"
print()
Dife_Paises = America_latina.difference(America_sur)
print("paises de america latina que no son de america del sur\n", Dife_Paises)

print()
Symmtric_dif_Paises = America_latina.symmetric_difference(America_sur)
print("paises de america ", Symmtric_dif_Paises)