import pyautogui
import time
import keyboard

intervalo = 0.1  # segundos entre clics
activo = False

print("F6 = iniciar/detener")
print("F7 = salir")

while True:
    if keyboard.is_pressed("f6"):
        activo = not activo
        print("Autoclicker:", "ACTIVADO" if activo else "DETENIDO")
        time.sleep(1)

    if keyboard.is_pressed("f7"):
        break

    if activo:
        pyautogui.click()
        time.sleep(intervalo)
