# HCAD - Herramientas Computacionales para Analisis de Datos

**Codigo del curso:** MIIA-4101  
**Universidad de los Andes**  
*Maestria en Inteligencia Analitica (MIIA)*

Bienvenido/a. Este es el repositorio de talleres autocalificables del curso HCAD. Aqui encontraras los ejercicios practicos semanales que te ayudaran a afianzar tus conocimientos en Python.

---

## Requisitos previos

Antes de comenzar, asegurate de tener lo siguiente instalado en tu computador (ya deberias tenerlo listo tras la configuracion inicial del curso):

*   **Python 3.8 o superior**
*   **Jupyter Notebook** o **JupyterLab**
*   **otter-grader**: Esta es la libreria que evalua tus respuestas. Si aun no la tienes, puedes instalarla abriendo tu terminal (o Anaconda Prompt) y ejecutando:
    ```bash
    pip install otter-grader
    ```

---

## Como descargar los talleres

Tienes dos opciones para descargar los talleres a tu computador:

**Opcion A: Descargar como ZIP (Recomendada si no conoces Git)**
1. Haz clic en el boton verde **"<> Code"** arriba a la derecha en esta pagina.
2. Selecciona **"Download ZIP"**.
3. Extrae la carpeta en un lugar seguro de tu computador (por ejemplo, en tus Documentos).

*Nota: A medida que se publiquen nuevos talleres, tendras que volver a descargar el repositorio en formato ZIP.*

**Opcion B: Clonar con Git (Si ya sabes usar Git)**
Abre tu terminal y ejecuta:
```bash
git clone https://github.com/milogz/Talleres-HCAD.git
```
*Nota: Solo necesitas clonar el repositorio **una vez**. Para obtener los nuevos talleres, simplemente ejecuta `git pull` dentro de la carpeta.*

---

## Como trabajar en un taller

Sigue estos pasos para resolver cada taller:

1. Abre la carpeta del taller correspondiente (ejemplo: `Taller01`).
2. **Descarga la carpeta completa** del taller, incluyendo la subcarpeta `tests/` y `Archivos/` (si existe). Los tests son necesarios para que `grader.check()` funcione.
3. Abre el archivo `.ipynb` usando Jupyter Notebook o JupyterLab.
4. **Ejecuta la primera celda** del notebook (contiene `import otter`). Esto activa el sistema de verificacion.
5. Lee cuidadosamente las instrucciones de cada ejercicio.
6. Escribe tu codigo unicamente en las celdas marcadas con `# Escribe tu codigo aqui` o donde veas `...`.
7. Para verificar si tu respuesta es correcta, ejecuta la celda que contiene `grader.check('qX')` (donde X es el numero de la pregunta).
8. Si ves el mensaje **"All test cases passed!"**, tu respuesta es correcta.
9. Si ves un mensaje de error, no te preocupes. Lee el mensaje, corrige tu codigo y vuelve a ejecutar.
10. Puedes ejecutar `grader.check()` **cuantas veces quieras**. La idea es aprender.

> **Importante:** Pasar las pruebas de `grader.check()` significa que superaste las pruebas **publicas**. Durante la calificacion final se ejecutan pruebas adicionales ocultas. Asegurate de que tu solucion sea **general** y no este codificada a la fuerza (hardcoded) solo para pasar el caso visible.

---

## Como entregar tu taller

Una vez hayas completado todos los ejercicios:

1. Ejecuta **todas las celdas** del notebook en orden. Puedes hacerlo desde el menu: `Cell > Run All` o `Kernel > Restart & Run All`.
2. Ve al final del notebook y ejecuta la celda que contiene `grader.export()`. Esto generara un archivo `.zip` en la misma carpeta.
3. **Renombra** el archivo `.zip` con esta convencion: **`TallerX_tucodigo.zip`**  
   Ejemplo: `Taller1_j.gomez123.zip`
4. Sube este archivo `.zip` a **Bloque Neon** (o a la plataforma indicada por tu profesor) antes de la fecha limite.

---

## Calendario de talleres

| Taller | Semana | Tema | Fecha limite |
|--------|--------|------|--------------|
| Taller 1 | S1 | Estructuras de datos: listas, tuplas, diccionarios | Por confirmar |
| Taller 2 | S1 | Estructuras de control | Por confirmar |
| Taller 3 | S2 | Funciones | Por confirmar |
| Taller 4 | S2 | Manejo de archivos y visualizacion | Por confirmar |
| Taller 5 | S3 | Librerias para manejo de datos | Por confirmar |
| Taller 6 | S4 | Explorar y modificar bases de datos | Por confirmar |
| Taller 7 | S5 | Limpiar y unir bases de datos | Por confirmar |
| Taller 8 | S6 | Visualizacion | Por confirmar |
| Taller 9 | S6 | Interactividad | Por confirmar |
| Taller 10 | S7 | Herramientas para analisis estadistico | Por confirmar |

---

## Estructura de cada taller

Cada carpeta de taller contiene:

```
TallerXX/
  TallerX.ipynb     # El notebook con los ejercicios
  tests/             # Archivos de prueba para grader.check()
    q1.py
    q2.py
    ...
  Archivos/          # Datos e imagenes (si aplica)
```

> **Importante:** Debes descargar la carpeta completa (incluyendo `tests/`) para que el sistema de verificacion funcione correctamente.

---

## Preguntas frecuentes

**"Que hago si `grader.check()` no funciona?"**  
Asegurate de haber instalado `otter-grader` (ver Requisitos previos), de haber ejecutado la primera celda del notebook que contiene `import otter`, y de tener la carpeta `tests/` en el mismo directorio que el notebook.

**"Puedo modificar las celdas que dicen 'No modifiques esta celda'?"**  
No. Si modificas estas celdas, los tests automaticos pueden fallar.

**"Que significa el `...` en las celdas de codigo?"**  
Es un placeholder. Reemplazalo con tu solucion.

**"Puedo verificar mis respuestas varias veces antes de entregar?"**  
Si. Puedes ejecutar `grader.check()` tantas veces como necesites antes de hacer tu entrega oficial.

**"El notebook no encuentra el archivo al hacer `import otter`"**  
Asegurate de haber instalado otter-grader con `pip install otter-grader` y reinicia el kernel de Jupyter.

---

## Soporte

*   **Dudas sobre los ejercicios:** Escribe al foro del curso en Bloque Neon.
*   **Problemas tecnicos con otter-grader:** Escribe al asistente del curso.
