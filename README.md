# AI-Based Career Recommendation System and Skill Gap Analysis

## Stack
React/Vite frontend, Django REST Framework backend, SQLite, PyMuPDF/Python-docx resume parsing. Career matching uses explainable weighted skill overlap from `dataset/careers.json`; scores are compatibility indicators, not job probabilities. No paid APIs or API keys.

## Windows / VS Code setup
Install Python 3.11/3.12 and Node.js 20+. Open this folder in VS Code.

### Terminal 1 — backend
```powershell
cd backend
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```
If activation is blocked: `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass`, then activate again. If `py -3.12` is unavailable, use `python -m venv .venv`.

### Terminal 2 — frontend
```powershell
cd frontend
npm install
npm run dev
```
Open http://localhost:5173. Backend API: http://127.0.0.1:8000/api/health/

## Demo
Click **Use demo profile**, then **Analyze career fit**. Or upload a PDF/DOCX resume (maximum 5 MB), review detected skills, and analyze. Select a career to see skill gaps and learning links.

## API
- `GET /api/health/`
- `GET /api/careers/`
- `POST /api/resume/parse/` multipart field `resume`
- `POST /api/recommend/` JSON `{"skills":["Python","SQL"]}`
- `POST /api/skill-gap/` JSON `{"skills":["Python"],"career":"Data Scientist"}`
- `GET/POST /api/history/`; `DELETE /api/history/<id>/`

## Tests
From `backend/` with venv active: `python manage.py test`

## Notes
Resume text is processed locally and uploaded files are not persisted. Scanned PDFs need OCR, which this starter does not include. Review detected skills before analysis. This is an educational demo, not professional career advice.
