# MOON AIM - ABMODEL
# 🌕 Lunar Landing Site Navigator

![NASA Space Apps 2026](https://img.shields.io/badge/NASA_Space_Apps-2026-1c64f2?style=for-the-badge)
![Sede CUGDL](https://img.shields.io/badge/Sede-Guadalajara-0ea5e9?style=for-the-badge)
![License: MIT](https://img.shields.io/badge/License-MIT-f59e0b?style=for-the-badge)

Interactive navigation, topographic evaluation, and decision-making tool for the safe landing of spacecraft modules in the Lunar South Pole (70°S – 90°S), developed for the **Lunar Landing Site Navigator** challenge of the **NASA Space Apps Challenge 2026**.

Unlike a conventional cartographic viewer, this browser conditions terrain viability on the **actual physical, mechanical, thermal, and communications limits of the landing module (*lander*)**, integrating electromechanical engineering criteria with 100% autonomous vector cartographic processing (offline) or directly with the JPL Horizons System API.

---

## 🚀 Main Features

* **Autonomous Orthographic Polar Cartography:** Clean mosaic of the lunar South Pole (70°S–90°S) from the *Clementine* mission, locally embedded with **continuous vector zoom (1.0x to 18.0x)**, free dragging, and a selenographic grid of parallels and meridians.
* **Exclusive Layer Control:** Alternation between the **Lunar South Pole Base Map** and the **Viability Thermal Layer** with opacity adjustment and mutual locking to guarantee permanent visibility.

* **- **LSI (Landing Safety Index) Calculation:** Cell-by-cell multi-criteria scoring based on 5 adjustable physical constraints:
  1. **Maximum Stable Slope ($\theta_{\max}$):** Static limit against rollover based on the center of gravity ($CG$) and foot-pad footprint. ($CG$).
  2. **Nozzle Clearance ($h_{\text{clear}}$):** Maximum tolerable height of rocks/roughness beneath the main engine.
  3. **Minimum Solar Illumination (`%`):** Photovoltaic energy requirement and thermal survival against Permanently Shadowed Regions (PSRs).
  4. **Minimum Earth Visibility (`%`):** Direct-to-Earth (DTE) link towards the $0^\circ\text{E}$ pmeridian for telemetry and communications.
  5. **Lateral Deviation Budget ($\Delta v$):** Terminal maneuvering radius of the Guidance, Navigation, and Control (GNC) system.
* **Landing Date and Time Simulator (`UTC`):** Calculates the solar azimuth ($\lambda_{\odot}$), subsolar latitude (polar seasonality), and Earth optical libration ($\Delta\theta_{\text{Tierra}}$), recalibrating shadows and the communication window according to the exact mission timing.
* **Multi-Zone Stochastic Search (`OPT-1` a `OPT-5`):** Stochastic algorithm for detecting multiple well-separated optimal zones that simultaneously meet all lander parameters.
* **GNC (Guidance, Navigation, and Control) Diagnostics and Plain Language Explanation:** Translates the *Landing Safety Index (LSI)* nto a clear viability diagnosis and automatically plots an alternative evasion trajectory within the $\Delta v$ radius when the selected target presents a risk.
* **Manual Coordinate Input and Bilingual Support (`ES | EN`):** Direct navigation by selenographic latitude/longitude, quick access to 8 **Artemis III** andidate sites (Shackleton Rim, Connecting Ridge, Faustini Rim A, Haworth, Malapert, Mons Mouton, Nobile, and Schrödinger), and an interchangeable interface between Spanish and English.
* **Resilient Hybrid Mode:** Compatible with local analytical telemetry and live synchronization with the NASA JPL Horizons API.

---

## 📐 Physical Criteria and Evaluation Model (`LSI`)

Each cell of the polar disc is evaluated starting from a base score of `100` points, applying proportional penalties when the terrain exceeds the physical limits of the hardware:

| Lander Parameter | Standard Value | Evaluated Engineering Criterion |
| :--- | :---: | :--- |
| **Max. Stable Slope ($\theta_{\max}$)** | `12.0°` | Rollover safety factor ($\text{FS} = \theta_{\max} / \theta_{\text{local}} \ge 1.25$). |
| **Nozzle Free Clearance ($h_{\text{clear}}$)** | `0.55 m` | Mechanical clearance between the engine nozzle and regolith blocks. |
| **Minimum Solar Illumination** | `65%` | Nominal electrical generation (`~1,680 W` peak) and battery thermal control. |
| **Min. Earth Visibility (Comms)** | `60%` | Direct line of sight to Earth ($0^\circ\text{E}$) considering relief and libration. |
| **Deviation Budget ($\Delta v$)** | `45 m/s` | Available lateral range for terminal reorientation of the GNC system. |

---

### *Landing Safety Index (LSI)* Classification

* 🟢 **Optimal ($\text{LSI} \ge 75$):** Flat terrain, free of critical obstacles, with solar illumination and DTE link within specification.
* 🟡 **Marginal ($45 \le \text{LSI} < 75$):** Partially complies or with narrow margins; requires caution and active monitoring of the GNC system.
* 🔴 **Peligro / PSR ($\text{LSI} < 45$):** Risk of rollover, nozzle impact, permanent darkness, or communication loss; the system triggers automatic diversion to the nearest safe site.

---

## 🔄 GNC Workflow

1. **Phase 01 — Cartographic Ingestion & Ephemerides:** Loading of the clean South Pole orthographic mosaic (`70°S–90°S`), topographic gradient extraction, and real-time Sun–Earth relative position calculation (`UTC`).
2. **Phase 02 — Hardware Constraints:** Dynamic reading of the mechanical, energy, and telecommunication limits of the lunar module.
3. **Phase 03 — Scoring Engine (`LSI`):** Cell-by-cell multi-criteria evaluation to render the thermal risk layer over the lunar disk.
4. **Phase 04 — GNC Terminal Evasion:** If the target site violates any critical threshold, the algorithm scans the neighborhood within the $\Delta v$ budget and plots the route to an alternative safe zone.
5. **Phase 05 — Actuation and Telemetry:** Validation of the rollover Safety Factor, estimated surface photovoltaic power, and availability of the Earth link.

---

## 🔗 Links of Interest

- **Live Demo:** [https://ElAngelZ.github.io/MOON-AIM/](https://ElAngelZ.github.io/MOON-AIM/)

---

## 💻 Local Execution Instructions (Optional and Recommended)

If you want to run the application locally with the direct connection gateway to the NASA JPL Horizons API:

1. Clone the repository:
   ```bash
   git clone https://github.com/ElAngelZ/MOON-AIM

2. Run the local Python forwarding server:
   ```bash
    python server.py

3. Open your browser at: http://localhost:8000
