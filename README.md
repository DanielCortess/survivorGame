# CompuGSurvivor (Pygame)

Videojuego 2D hecho con Pygame.

## Requisitos

- Windows
- Python 3.11 (recomendado)
- Pip

## Instalacion

1. Clona este repositorio o descargalo como ZIP.
2. Abre una terminal en la carpeta del proyecto.
3. Instala dependencias:

```powershell
py -m pip install -r requirements.txt
```

## Ejecucion

Desde la carpeta del proyecto, ejecuta:

```powershell
py Survivor.py
```

Si tienes varias versiones de Python y `py` no usa la correcta, prueba:

```powershell
py -3.11 Survivor.py
```

## Controles

- Flechas: mover personaje
- Espacio: disparar
- V: cambiar a arma secundaria
- B: volver a arma principal
- P: pausa
- Enter: avanzar en menus y escenas
- S: salir en pantalla de victoria/game over

## Estructura principal

- `Survivor.py`: punto de entrada del juego
- `ClaseJugador.py`: logica del jugador
- `ClaseEnemigo.py`: enemigos normales
- `ClaseBoss.py`: jefe final
- `ClaseSpawn.py`: generadores de enemigos
- `requirements.txt`: dependencias Python

## Solucion de problemas

- Error `No module named pygame`:

```powershell
py -m pip install -r requirements.txt
```

- El juego no abre al hacer doble clic:
  - Ejecutalo desde terminal con `py Survivor.py` para ver errores.

- No se escucha audio:
  - Verifica que el PC tenga dispositivo de salida activo.

## Notas

- El proyecto fue adaptado para ejecutarse en Python 3.
- Se recomienda mantener los archivos de imagen, audio y mapas en la misma carpeta que `Survivor.py`.

