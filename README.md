# RxR Multilingual VLN Agent — Custom Map & Room Studio

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![WebGL](https://img.shields.io/badge/Three.js-r128-cyan.svg)](https://threejs.org/)
[![TailwindCSS](https://img.shields.io/badge/TailwindCSS-v3-38bdf8.svg)](https://tailwindcss.com/)
[![Node.js](https://img.shields.io/badge/Node.js-24+-339933.svg)](https://nodejs.org/)
[![Python](https://img.shields.io/badge/Python-3.8+-3776ab.svg)](https://python.org/)

An interactive **Room-Across-Room (RxR) Multilingual Vision-and-Language Navigation (VLN) Studio and Topological Map Builder**. This system enables research into embodied AI navigation across English, Hindi (हिंदी), and Telugu (తెలుగు), featuring a unified 3D Matterport viewport (360° Panorama and 3D Dollhouse), interactive 2D floorplan editor, token attention heatmap visualization, and shortest-path planning policies.

---

## ✨ Features

- **Multilingual Instruction Engine**:
  - Full support for **English**, **Hindi (हिंदी)**, and **Telugu (తెలుగు)** commands.
  - Interactive **Cross-Modal Token Attention Heatmap** tracking natural language focus at each navigation hop.
  - Preloaded with realistic navigation episodes for residential and robotics campus environments.

- **Unified Interactive Viewport**:
  - **360° First-Person Panorama**: Look around in realistic indoor rooms, click glowing floor waypoint rings or 3D doors to travel room-to-room.
  - **3D Dollhouse Orbit**: Free 3D orbital inspection of room geometry, wireframe perimeter cages, and transparent walls with configurable opacity.
  - **2D Topological Floorplan**: Interactive blueprint view showing viewpoint nodes, navigation graph edges, room boundaries, and agent field-of-view cone.

- **Interactive Room & Map Builder**:
  - Add custom rooms with parametric dimensions, theme colors, and landmark objects (Sofa, TV, Appliances, Desks).
  - Add viewpoint nodes and connect topological navigation graph edges with point-and-click tools.
  - Auto-link nearby viewpoint pairs using spatial proximity graph heuristics.
  - Export and import full topological maps in JSON schema.

- **Standard VLN Evaluation Metrics**:
  - **Path Length (PL)** in meters.
  - **Navigation Error (NE)** to destination viewpoint.
  - **Success weighted by Path Length (SPL)**.
  - Step-by-step action policy trace logging with adjustable walking pace (0.4x - 3.0x).

---

## 🏗️ Architecture: Separated Frontend & Backend

The project is structured with a decoupled frontend and backend that communicate via standard REST APIs while also supporting standalone zero-dependency execution.

```
rxr-multilingual-vln-studio/
├── frontend/                     # Client application
│   ├── index.html                # Semantic HTML layout
│   ├── css/
│   │   └── style.css             # Glassmorphism & UI styles
│   └── js/
│       └── app.js                # Three.js 3D engine, 2D canvas, & state
├── backend/                      # Server and REST API services
│   ├── server.py                 # Python backend server
│   ├── server.js                 # Node.js backend server
│   └── data/
│       └── maps.json             # Persistent indoor map configurations
├── main.py                       # Python root runner
├── server.js                     # Node.js root runner
├── start.bat                     # Windows one-click start script
├── package.json                  # NPM metadata & start scripts
└── README.md                     # Documentation
```

---

## 🚀 Running on Localhost

You can run the platform using **Node.js** OR **Python** (both use standard libraries with zero required external dependencies):

### Option A: Using Node.js
```bash
# Run using node directly
node server.js

# Or using npm
npm start
```

### Option B: Using Python
```bash
# Run using python directly
python main.py

# Or specify a custom port
python main.py 8080
```

### Option C: Windows Batch Launcher
Double click `start.bat` or run:
```cmd
start.bat
```

Open your browser and visit:
👉 **[http://localhost:8000](http://localhost:8000)** (or the configured port)

---

## 🔌 Backend REST API Reference

The backend exposes the following endpoints:

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/api/health` | Service health status and version info |
| `GET` | `/api/maps` | Retrieve all available topological indoor maps |
| `GET` | `/api/maps/:id` | Retrieve a specific map configuration |
| `POST` | `/api/maps` | Save a new custom map to persistent storage |
| `PUT` | `/api/maps/:id` | Update an existing map layout and graph |
| `DELETE` | `/api/maps/:id` | Delete a map from storage |
| `POST` | `/api/plan-path` | Compute optimal Dijkstra graph path between viewpoints |

---

## 📜 License

MIT License. Designed for Embodied AI and Multilingual VLN Research.
