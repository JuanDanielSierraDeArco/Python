import time

# Establecer el tiempo de espera en segundos
tiempo_espera = 5

# Mensaje a mostrar
mensaje = "¡Hola! Este es un mensaje programado."

# Mostrar un mensaje después del tiempo de espera
print(f"El programa se ejecutará en {tiempo_espera} segundos...")
time.sleep(tiempo_espera)
print(mensaje)