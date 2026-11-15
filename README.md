# ABMODEL-Lunar-Landing-Site-Navigator
# 🌑 Lunar Landing Site Navigator — South Polar Orthographic Edition

![NASA Space Apps 2026](https://img.shields.io/badge/NASA_Space_Apps-2026-1c64f2?style=for-the-badge)
![Sede CUGDL](https://img.shields.io/badge/Sede-CUGDL_Guadalajara-0ea5e9?style=for-the-badge)
![Perfil](https://img.shields.io/badge/CETI_Colomos-Electromecánica_%26_Software-10b981?style=for-the-badge)
![License: MIT](https://img.shields.io/badge/License-MIT-f59e0b?style=for-the-badge)

Herramienta interactiva de navegación, evaluación topográfica y toma de decisiones para el alunizaje seguro de módulos espaciales en el **Polo Sur Lunar (`70°S – 90°S`)**, desarrollada para el reto **Lunar Landing Site Navigator** del **NASA Space Apps Challenge 2026**.

A diferencia de un visor cartográfico convencional, este navegador condiciona la viabilidad del terreno a los **límites físicos, mecánicos, térmicos y de comunicaciones reales del módulo de aterrizaje (*lander*)**, integrando criterios de ingeniería electromecánica con procesamiento cartográfico vectorial 100% autónomo (*offline*).

---

## 🚀 Características Principales

* **Cartografía Polar Ortográfica Autónoma (`100% Offline`):** Mosaico limpio del Polo Sur lunar (`70°S–90°S`) basado en la misión *Clementine*, embebido localmente con **zoom vectorial continuo (`1.0x` a `18.0x`)**, arrastre libre y retícula selenográfica de paralelos y meridianos.
* **Control Exclusivo de Capas:** Alternancia entre el **Mapa Base Polo Sur Lunar** y la **Capa Térmica de Seguridad (LSI)** con ajuste de opacidad y bloqueo mutuo para garantizar visibilidad permanente.
* **Parametrización Electromecánica del Lander:** Evaluación en tiempo real frente a 5 restricciones físicas ajustables:
  1. **Pendiente Máxima Estable ($\theta_{\max}$):** Límite estático contra volcadura según el centro de gravedad ($CG$) y huella de patas.
  2. **Despeje Libre de Tobera ($h_{\text{clear}}$):** Altura máxima de rocas/rugosidad tolerable bajo el motor principal.
  3. **Iluminación Solar Mínima (`%`):** Requerimiento energético fotovoltaico y supervivencia térmica frente a Regiones Permanentemente Sombreadas (PSR).
  4. **Visibilidad Tierra Mínima (`%`):** Enlace directo *Direct-to-Earth* (DTE) hacia el meridiano $0^\circ\text{E}$ para telemetría y comunicaciones.
  5. **Presupuesto de Desvío Lateral ($\Delta v$):** Radio de maniobra terminal del sistema de Guiado, Navegación y Control (GNC).
* **Simulador de Fecha y Hora de Alunizaje (`UTC`):** Calcula el azimut solar ($\lambda_{\odot}$), la latitud subsolar (estacionalidad polar) y la libración óptica de la Tierra ($\Delta\theta_{\text{Tierra}}$), recalibrando las sombras y la ventana de comunicación según el momento exacto de la misión.
* **Búsqueda Estocástica Multi-Zona (`OPT-1` a `OPT-5`):** Detecta y sortea múltiples sitios óptimos espacialmente distribuidos en todo el Polo Sur que cumplen simultáneamente con todos los parámetros del lander.
* **Diagnóstico GNC y Explicación en Lenguaje Sencillo:** Traduce el *Landing Safety Index (LSI)* en un diagnóstico claro de viabilidad y traza automáticamente una trayectoria alterna de evasión dentro del radio $\Delta v$ cuando el objetivo seleccionado presenta riesgo.
* **Ingreso Manual de Coordenadas y Soporte Bilingüe (`ES | EN`):** Navegación directa por latitud/longitud selenográfica, accesos rápidos a 8 sitios candidatos de **Artemis III** (*Shackleton Rim, Connecting Ridge, Faustini Rim A, Haworth, Malapert, Mons Mouton, Nobile* y *Schrödinger*) e interfaz intercambiable entre español e inglés.

---

## 📐 Criterios Físicos y Modelo de Evaluación (`LSI`)

Cada celda del disco polar se evalúa partiendo de una puntuación base de `100` puntos, aplicando penalizaciones proporcionales cuando el terreno excede los límites físicos del hardware:

| Parámetro del Lander | Valor Estándar | Criterio de Ingeniería Evaluado |
| :--- | :---: | :--- |
| **Pendiente Máx. Estable ($\theta_{\max}$)** | `12.0°` | Factor de seguridad contra volcadura ($\text{FS} = \theta_{\max} / \theta_{\text{local}} \ge 1.25$). |
| **Despeje Libre Tobera ($h_{\text{clear}}$)** | `0.55 m` | Holgura mecánica entre la tobera del motor y bloques de regolito. |
| **Iluminación Solar Mínima** | `65%` | Generación eléctrica nominal (`~1,680 W` pico) y control térmico de baterías. |
| **Visibilidad Tierra Mín. (Comms)** | `60%` | Línea de vista directa hacia la Tierra ($0^\circ\text{E}$) considerando relieve y libración. |
| **Presupuesto Desvío ($\Delta v$)** | `45 m/s` | Alcance lateral disponible para reorientación terminal del sistema GNC. |

### Clasificación del *Landing Safety Index (LSI)*
* 🟢 **Óptimo ($\text{LSI} \ge 75$):** Terreno plano, libre de obstáculos críticos, con iluminación solar y enlace DTE dentro de especificación.
* 🟡 **Marginal ($45 \le \text{LSI} < 75$):** Cumple parcialmente o con márgenes estrechos; requiere precaución y monitoreo activo del sistema GNC.
* 🔴 **Peligro / PSR ($\text{LSI} < 45$):** Riesgo de volcadura, impacto en tobera, oscuridad permanente o pérdida de comunicación; el sistema activa el desvío automático hacia el sitio seguro más cercano.

---

## 🔄 Arquitectura y Línea de Flujo GNC

1. **Fase 01 — Ingesta Cartográfica & Efemérides:** Carga del mosaico ortográfico limpio del Polo Sur (`70°S–90°S`), extracción de gradientes topográficos y cálculo de posición relativa Sol–Tierra en tiempo real (`UTC`).
2. **Fase 02 — Restricciones de Hardware:** Lectura dinámica de los límites mecánicos, energéticos y de telecomunicaciones del módulo lunar.
3. **Fase 03 — Motor de Scoring (`LSI`):** Evaluación multicriterio celda por celda para renderizar la capa térmica de riesgo sobre el disco lunar.
4. **Fase 04 — Evasión Terminal GNC:** Si el sitio objetivo viola algún umbral crítico, el algoritmo escanea el vecindario dentro del presupuesto $\Delta v$ y traza la ruta hacia una zona segura alternativa.
5. **Fase 05 — Actuación y Telemetría:** Validación del Factor de Seguridad contra volcadura, potencia fotovoltaica estimada en superficie y disponibilidad de enlace con la Tierra.

---

## 💻 Instalación y Ejecución

El proyecto está empaquetado como una aplicación web autocontenida sin dependencias externas ni necesidad de conexión a internet durante la demostración:

1. Clona este repositorio:
   ```bash
   git clone [https://github.com/tu-usuario/lunar-landing-site-navigator.git](https://github.com/tu-usuario/lunar-landing-site-navigator.git)
