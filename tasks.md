# 🔧 Phase 1: Project Scaffolding

---

### ✅ **Task 1**: Initialize Extension Project

* **Start**: You have an empty project folder.
* **End**: You have a folder with `extension/`, `backend/`, `shared/`, and `scripts/`.

---

### ✅ **Task 2**: Set up Vite + React + Tailwind

* **Start**: Inside `extension/` folder.
* **End**: React + Tailwind configured; `popup/` renders "Hello World" in Chrome extension.

---

### ✅ **Task 3**: Create `manifest.json` (v3)

* **Start**: Inside `public/`
* **End**: Basic manifest with permissions for tabs, storage, scripting, and popup setup.

---

### ✅ **Task 4**: Hook up `chrome.runtime` to open popup

* **Start**: Extension loads in Chrome.
* **End**: Clicking the extension icon shows your popup UI.

---

# 🧠 Phase 2: Backend Setup

---

### ✅ **Task 5**: Initialize FastAPI app

* **Start**: You have a `backend/` folder.
* **End**: Running `uvicorn main:app` returns "Hello, world!" from `/ping`.

---

### ✅ **Task 6**: Add POST `/classify` endpoint

* **Start**: Text payload is accepted at `/classify`.
* **End**: It returns a dummy list of topics like `["technology", "psychology"]`.

---

### ✅ **Task 7**: Add GET `/recommend` endpoint

* **Start**: Takes `topics=["technology"]`.
* **End**: Returns static book recommendations.

---

# 🧪 Phase 3: Browser Content Tracking

---

### ✅ **Task 8**: Inject content script into pages

* **Start**: You have `content/content.js` listed in manifest.
* **End**: It logs the current page’s `<title>` to console.

---

### ✅ **Task 9**: Extract readable text from page

* **Start**: `content.js` running on an article.
* **End**: Grabs title + readable body text; sends message to background script.

---

### ✅ **Task 10**: Background script receives and logs content

* **Start**: `background.js` listens for messages.
* **End**: Logs `{ title, body }` received from `content.js`.

---

# 🌐 Phase 4: Backend Integration

---

### ✅ **Task 11**: POST page text to `/classify`

* **Start**: `background.js` has text.
* **End**: It sends the text to backend and logs received topics.

---

### ✅ **Task 12**: GET book recs from `/recommend`

* **Start**: You have topics from `/classify`.
* **End**: Send to `/recommend`, receive and log list of book titles.

---

### ✅ **Task 13**: Store recommendations in `chrome.storage`

* **Start**: Background receives book list.
* **End**: Saves books to `chrome.storage.local`.

---

# 📤 Phase 5: UI – Popup

---

### ✅ **Task 14**: Fetch book list in `popup.jsx`

* **Start**: React popup loads.
* **End**: Pulls recs from `chrome.storage.local` and logs to console.

---

### ✅ **Task 15**: Display list of books

* **Start**: You have list of titles.
* **End**: Rendered in Tailwind-styled list with title + author.

---

### ✅ **Task 16**: Add "Mark as Read" button

* **Start**: Each book in UI has a button.
* **End**: Clicking it updates local storage to remove book.

---

# ⚙️ Phase 6: UX & Preferences

---

### ✅ **Task 17**: Add options page

* **Start**: New React app in `options/`.
* **End**: User can set preferred genres and blocked sites.

---

### ✅ **Task 18**: Sync preferences using `chrome.storage`

* **Start**: Preferences entered in options page.
* **End**: Saved and retrievable in background script.

---

### ✅ **Task 19**: Filter requests based on blocklist

* **Start**: Background script receives content.
* **End**: Ignores blocked domains.

---

# 🧪 Phase 7: Testing & Finalization

---

### ✅ **Task 20**: Add dev build script

* **Start**: You have `scripts/build-extension.sh`.
* **End**: Runs Vite build + copies manifest/assets to `dist/`.

---

### ✅ **Task 21**: Manual test on 3 types of sites

* **Start**: Load unpacked extension.
* **End**: Visit sites, verify popup gives relevant book recs.

---

### ✅ **Task 22**: Deploy FastAPI to Render/Fly.io

* **Start**: Local server running.
* **End**: Backend hosted with live API for extension to call.

