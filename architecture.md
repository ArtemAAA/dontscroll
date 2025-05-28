# 🧱 Project Structure (React + FastAPI)

```
chrome-book-replacer/
│
├── extension/                    # Chrome Extension (frontend + logic)
│   ├── public/                  # Static files (manifest, icons)
│   │   ├── icons/
│   │   └── manifest.json
│   ├── src/
│   │   ├── popup/              # Popup UI React app
│   │   │   ├── Popup.jsx
│   │   │   ├── popup.css
│   │   │   └── index.tsx
│   │   ├── options/            # Settings page React app
│   │   ├── components/         # Shared React components
│   │   ├── content/            # Content script injected into pages
│   │   │   └── content.js
│   │   ├── background/         # Background service worker
│   │   │   └── background.js
│   │   ├── hooks/              # Custom hooks (e.g., useStorage, useRecommendations)
│   │   ├── state/              # Global state (Zustand or Context)
│   │   ├── utils/              # Utility functions
│   │   ├── styles/             # Tailwind setup + global styles
│   │   └── index.css
│   ├── tailwind.config.js
│   ├── postcss.config.js
│   ├── vite.config.js          # Vite bundler for React+extension
│   └── tsconfig.json
│
├── backend/                     # FastAPI backend
│   ├── app/
│   │   ├── api/                # API routes: classify, recommend
│   │   ├── core/               # NLP & topic extraction
│   │   ├── services/           # Recommendation engine
│   │   ├── models/             # Pydantic schemas
│   │   ├── db/                 # (Optional) persistence
│   │   └── main.py             # App entry point
│   └── requirements.txt
│
├── shared/                      # Shared static resources
│   └── book_metadata.json
│
├── scripts/                     # Build and tooling
│   └── build-extension.sh
│
├── README.md
└── .gitignore
```

---

# 🔍 Component Roles

## ✅ **Frontend (extension/)**

### **React App (popup & options)**

* **Popup**:
  Displays current book recommendations and a button to "pause" distractions.
* **Options Page**:
  UI for user to manage preferences, block domains, set frequency, etc.

### **Content Script (`content.js`)**

* Injected into web pages to:

  * Extract readable content (via DOM or libraries like `Readability`)
  * Send content to background script

### **Background Script (`background.js`)**

* Acts as the orchestrator:

  * Receives page content from content script
  * Filters and forwards it to the FastAPI backend
  * Stores recs in `chrome.storage` and pushes them to popup on demand

### **State Management**

* Use **Zustand** or **React Context** in `state/` for lightweight global state (e.g., current recs, UI state).
* Use `chrome.storage.sync` for persistent user data across browsers.

---

## ✅ **Backend (FastAPI)**

### **Routes (`api/`)**

* `POST /classify`: Accepts raw page text, returns topics.
* `GET /recommend`: Given topics or interests, returns book list.

### **Core NLP (`core/`)**

* Use **spaCy** or **transformers** to:

  * Extract main subjects from text
  * Classify interest areas

### **Recommender (`services/`)**

* Maps topics → genres → books using `book_metadata.json`
* Could evolve into vector similarity matching with `sentence-transformers`

---

# 🔄 Data Flow

```
User visits a webpage
    ↓
content.js scrapes text + sends → background.js
    ↓
background.js → POST /classify → FastAPI
    ↓
FastAPI → topics → /recommend → returns book recs
    ↓
background.js stores recs in chrome.storage
    ↓
popup.js retrieves and displays them in the UI
```

---

# 🧠 State Overview

| **Where**       | **Data**                       | **Storage Method**             |
| --------------- | ------------------------------ | ------------------------------ |
| Content Script  | Extracted content              | In-memory → background message |
| Background      | Book recs, tab info, settings  | `chrome.storage.local` or sync |
| Popup           | UI state (which book is shown) | React state or Zustand         |
| FastAPI backend | Book metadata, NLP models      | JSON file or DB                |

---

# 📦 Example Tooling

* **Bundler**: [Vite](https://vitejs.dev/) — fast, great with extensions
* **React framework**: Just React + Tailwind (no Next.js)
* **Testing**: Vitest or Jest for components and backend
* **Deployment**:

  * Backend can be hosted via Render, Railway, or Fly.io
  * Chrome extension is packaged via `build-extension.sh` using `vite build`

---

# 🧰 Permissions Example (`manifest.json`)

```json
{
  "manifest_version": 3,
  "name": "Read Instead",
  "version": "1.0",
  "permissions": [
    "storage",
    "tabs",
    "scripting"
  ],
  "host_permissions": ["<all_urls>"],
  "action": {
    "default_popup": "popup/index.html"
  },
  "background": {
    "service_worker": "background/background.js"
  },
  "content_scripts": [
    {
      "matches": ["<all_urls>"],
      "js": ["content/content.js"]
    }
  ]
}
```