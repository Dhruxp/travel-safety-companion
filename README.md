# 🚦 Travel Safety Companion

**Smarter routes. Safer cities.**

An **AI-powered navigation system** that recommends routes based not just on speed, but on **real-world safety, context, and urgency**.

Built for **Microsoft Imagine Cup ’26**.

---

##  Problem

Traditional navigation apps optimize for distance or time, ignoring critical safety factors such as:

* Poor lighting
* Isolated roads
* Crime-prone areas
* Emergency vehicle accessibility

This forces users to choose between *reaching fast* and *feeling safe*.

---

##  Solution

**Travel Safety Companion** is a context-aware routing platform that:

* Evaluates **multiple real-world routes**
* Scores them using **AI-driven safety intelligence**
* Recommends the **safest route for the situation**
* Clearly explains *why* a route was chosen

It adapts to different use cases:

*  Night-time travel
*  Women’s safety
*  Ambulance / emergency routing

---

##  System Architecture (High Level)

```
User (Web / App)
      ↓
Frontend (Maps + UI)
      ↓
Backend API
      ↓
AI & Risk Engine
      ↓
Ranked Routes + Explanations
```

---

##  Core Components

###  Frontend

* Interactive map-based UI
* Displays multiple routes
* Highlights safest option
* Shows human-readable safety explanations

**Tech**: React, Mapbox, TailwindCSS

---

###  Backend

* Exposes routing and safety APIs
* Connects frontend with AI engine
* Handles user context (night, women, ambulance)

**Tech**: FastAPI (Python), REST APIs

---

###  AI & Risk Engine

* Loads real road networks (OpenStreetMap)
* Generates alternative routes
* Extracts safety features per route
* Applies context-aware risk scoring
* Produces explainable decisions

**Tech**: Python, OSMnx, GeoPandas, NetworkX

 Located in: `risk_engine/`

---

##  Safety Intelligence (Examples)

| Context   | Prioritized Factors          |
| --------- | ---------------------------- |
| Night     | Lighting, isolation, crime   |
| Women     | Isolation, crime, visibility |
| Ambulance | Road width, accessibility    |

Lower risk score = **safer route**

---

##  Explainability

Every recommendation includes clear reasoning, such as:

* “Route is well-lit and passes through populated areas”
* “Avoided due to high isolation and crime exposure”
* “Favors wide roads suitable for emergency vehicles”

No black boxes.

---

##  Quick Start (Demo)

From project root:

```
python demo_test.py
```

This runs an **end-to-end demo**:

* Generates routes
* Scores them
* Prints ranked results with explanations

---

##  Repository Structure

```text
IMAGINE CUP '26/
├── frontend/        # UI and maps
├── backend/         # API layer
├── risk_engine/     # AI & risk intelligence
├── demo_test.py     # End-to-end demo
└── README.md
```

---

##  Why This Matters

* **Human-centric AI**: Safety over pure optimization
* **Explainable decisions**: Trust and transparency
* **Scalable impact**: Individuals, emergency services, cities
* **Real-world relevance**: Uses real map and geographic data

---

##  Future Scope

* Real-time traffic & alerts
* Crime severity weighting
* Predictive risk by time-of-day
* Crowd-sourced safety feedback
* Azure deployment & OpenAI-powered explanations

---


