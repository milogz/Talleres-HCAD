# 📊 HCAD - Herramientas Computacionales para Análisis de Datos

**Código del curso:** MIIA-4101  
**Universidad de los Andes**  
*Maestría en Inteligencia Analítica (MIIA)*

¡Bienvenido/a! Este es el repositorio de talleres autocalificables del curso HCAD. Aquí encontrarás los ejercicios prácticos semanales que te ayudarán a afianzar tus conocimientos en Python.

---

## 🛠️ Requisitos previos

Antes de comenzar, asegúrate de tener lo siguiente instalado en tu computador (ya deberías tenerlo listo tras la configuración inicial del curso):

*   **Python 3.8 o superior**
*   **Jupyter Notebook** o **JupyterLab**
*   **otter-grader**: Esta es la librería que evalúa tus respuestas. Si aún no la tienes, puedes instalarla abriendo tu terminal (o Anaconda Prompt) y ejecutando:
    ```bash
    pip install otter-grader
    ```

---

## 📥 Cómo descargar los talleres

Tienes dos opciones para descargar los talleres a tu computador:

**Opción A: Descargar como ZIP (Recomendada si no conoces Git)**
1. Haz clic en el botón verde **"<> Code"** arriba a la derecha en esta página.
2. Selecciona **"Download ZIP"**.
3. Extrae la carpeta en un lugar seguro de tu computador (por ejemplo, en tus Documentos).

*Nota: A medida que se publiquen nuevos talleres, tendrás que volver a descargar el repositorio en formato ZIP.*

**Opción B: Clonar con Git (Si ya sabes usar Git)**
Abre tu terminal y ejecuta:
```bash
git clone https://github.com/TU_ORGANIZACION/HCAD-Talleres.git
```
*Nota: Solo necesitas clonar el repositorio **una vez**. Para obtener los nuevos talleres, simplemente ejecuta `git pull` dentro de la carpeta.*

---

## 💻 Cómo trabajar en un taller

Sigue estos pasos para resolver cada taller:

1. Abre la carpeta del taller correspondiente (ejemplo: `Taller01`).
2. Abre el archivo `.ipynb` usando Jupyter Notebook o JupyterLab.
3. **Ejecuta la primera celda** del notebook (contiene `import otter`). Esto activa el sistema de verificación.
4. Lee cuidadosamente las instrucciones de cada ejercicio.
5. Escribe tu código únicamente en las celdas marcadas con `# Escribe tu codigo aqui` o donde veas `...`.
6. Para verificar si tu respuesta es correcta, ejecuta la celda que contiene `grader.check('qX')` (donde X es el número de la pregunta).
7. Si ves el mensaje **"All test cases passed!"**, ¡excelente! Tu respuesta es correcta. ✅
8. Si ves un mensaje de error, no te preocupes. Lee el mensaje, corrige tu código y vuelve a ejecutar. ❌ → 🔄
9. Puedes ejecutar `grader.check()` **cuantas veces quieras**. ¡La idea es aprender!

> **⚠️ Importante:** Pasar las pruebas de `grader.check()` significa que superaste las pruebas **públicas**. Durante la calificación final se ejecutan pruebas adicionales ocultas. Asegúrate de que tu solución sea **general** y no esté codificada a la fuerza (hardcoded) solo para pasar el caso visible.

---

## 📤 Cómo entregar tu taller

Una vez hayas completado todos los ejercicios:

1. Ejecuta **todas las celdas** del notebook en orden. Puedes hacerlo desde el menú: `Cell > Run All` o `Kernel > Restart & Run All`.
2. Ve al final del notebook y ejecuta la celda que contiene `grader.export()`. Esto generará un archivo `.zip` en la misma carpeta.
3. **Renombra** el archivo `.zip` con esta convención: **`TallerX_tucodigo.zip`**  
   Ejemplo: `Taller1_j.gomez123.zip`
4. Sube este archivo `.zip` a **Bloque Neón** (o a la plataforma indicada por tu profesor) antes de la fecha límite.

---

## 📅 Calendario de talleres

| Taller | Semana | Tema | Fecha límite |
|--------|--------|------|--------------|
| Taller 1 | S1 | Estructuras de datos: listas, tuplas, diccionarios | Por confirmar |
| Taller 2 | S1 | Estructuras de control | Por confirmar |
| Taller 3 | S2 | Funciones | Por confirmar |
| Taller 4 | S2 | Manejo de archivos y visualización | Por confirmar |
| Taller 5 | S3 | Librerías para manejo de datos | Por confirmar |
| Taller 6 | S4 | Explorar y modificar bases de datos | Por confirmar |
| Taller 7 | S5 | Limpiar y unir bases de datos | Por confirmar |
| Taller 8 | S6 | Visualización | Por confirmar |
| Taller 9 | S6 | Interactividad | Por confirmar |
| Taller 10 | S7 | Herramientas para análisis estadístico | Por confirmar |

---

## ❓ Preguntas frecuentes

**"¿Qué hago si `grader.check()` no funciona?"**  
Asegúrate de haber instalado `otter-grader` (ver Requisitos previos) y de haber ejecutado la primera celda del notebook que contiene `import otter`.

**"¿Puedo modificar las celdas que dicen 'No modifiques esta celda'?"**  
No. Si modificas estas celdas, los tests automáticos pueden fallar.

**"¿Qué significa el `...` en las celdas de código?"**  
Es un placeholder. Reemplázalo con tu solución.

**"¿Puedo verificar mis respuestas varias veces antes de entregar?"**  
¡Sí! Puedes ejecutar `grader.check()` tantas veces como necesites antes de hacer tu entrega oficial.

**"El notebook no encuentra el archivo al hacer `import otter`"**  
Asegúrate de haber instalado otter-grader con `pip install otter-grader` y reinicia el kernel de Jupyter.

---

## 🤝 Soporte

*   **Dudas sobre los ejercicios:** Escribe al foro del curso en Bloque Neón.
*   **Problemas técnicos con otter-grader:** Escribe al asistente del curso.

¡Mucho éxito en tu aprendizaje! 🚀
