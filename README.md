# Course Catalog API

A FastAPI backend for the course catalog that previously lived in `lib/courses.ts` of the Next.js project.

## How to run

Requires Python 3.10+.

```bash
# macOS / Linux
python3 -m venv .venv
source .venv/bin/activate

# Windows (PowerShell)
python -m venv .venv
.venv\Scripts\Activate.ps1

pip install -r requirements.txt
fastapi dev main.py
```

The server runs at http://127.0.0.1:8000, and the interactive documentation is at http://127.0.0.1:8000/docs.

## Routes

| Route | Description |
|---|---|
| `GET /` | Checks that the server is alive |
| `GET /courses` | Course list with filtering, sorting, search and pagination |
| `GET /courses/{course_id}` | A single course, or 404 |

Query parameters of `GET /courses`:

- `is_elective` (`true` / `false`): only elective or only required courses
- `sort` (`popular` by default, or `title`): by likes descending or alphabetically by title
- `q`: case-insensitive search by title
- `page` (≥ 1, default 1) and `page_size` (1–100, default 20): pagination via `Depends(pagination)`

## What was verified

| Request | Result |
|---|---|
| `GET /` | `{"message": "Course Catalog API is running"}` |
| `GET /courses` | 6 courses: ai-integration, modern-frontend, web-security, backend-fastapi, databases-postgresql, api-design |
| `GET /courses?is_elective=true` | 2 courses: ai-integration, api-design |
| `GET /courses?is_elective=false` | 4 courses: modern-frontend, web-security, backend-fastapi, databases-postgresql |
| `GET /courses?sort=title` | ai-integration, api-design, backend-fastapi, modern-frontend, databases-postgresql, web-security |
| `GET /courses?page=1&page_size=2` | ai-integration, modern-frontend |
| `GET /courses?page=2&page_size=2` | web-security, backend-fastapi |
| `GET /courses?page=3&page_size=2` | databases-postgresql, api-design |
| `GET /courses?page=4&page_size=2` | `[]` |
| `GET /courses/web-security` | The Web Security Essentials course |
| `GET /courses/nope` | 404, `{"detail": "Course not found"}` |
| `GET /courses?q=react` | modern-frontend |
| `GET /courses?q=api` | backend-fastapi, api-design |
| `GET /courses?sort=banana` | 422 |
| `GET /courses?page=0`, `GET /courses?page_size=1000` | 422 |
| `/docs` | Exactly three routes: `GET /`, `GET /courses`, `GET /courses/{course_id}`; the `Course` schema is listed under Schemas |
