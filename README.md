# Course Catalog API

FastAPI backend for the Course Catalog frontend. It serves the six courses,
accepts likes and enrollments, and exposes an OpenAPI UI for testing.

## How to run

Requires Python 3.10 or newer.

```bash
# macOS / Linux
python3 -m venv .venv
source .venv/bin/activate

# Windows PowerShell
python -m venv .venv
.venv\Scripts\Activate.ps1

pip install -r requirements.txt
fastapi dev main.py
```

The API runs at <http://localhost:8000>. Interactive documentation is available
at <http://localhost:8000/docs>.

## What changed in Lab 5

The backend now uses `CORSMiddleware` to allow browser requests from the exact
frontend origin `http://localhost:3000`. CORS is needed for Client Component
requests because the frontend and backend have different origins.

`CamelModel` keeps Python field names in snake_case while exposing body and
response fields in camelCase. For example, `is_elective`, `course_id`, and
`student_name` become `isElective`, `courseId`, and `studentName` in JSON. Query
parameters such as `is_elective` keep their original names.

The server stores likes and enrollments in memory. They return to their initial
state whenever the backend restarts.

## Routes

| Method and route | Description |
|---|---|
| `GET /` | Checks that the API is running |
| `GET /courses` | Lists courses with filtering, sorting, search, and pagination |
| `GET /courses/{course_id}` | Returns one course or 404 |
| `POST /courses/{course_id}/like` | Adds one like and returns the updated course |
| `POST /enrollments` | Creates an enrollment and returns 201 |
| `GET /enrollments` | Lists the in-memory enrollments |

Example like response:

```json
{
  "id": "web-security",
  "title": "Web Security Essentials",
  "description": "JWT/OAuth2, defending against XSS, CSRF, SQL injection.",
  "credits": 4,
  "isElective": false,
  "likes": 22
}
```

Example enrollment request:

```json
{
  "courseId": "web-security",
  "studentName": "Aigerim"
}
```

Example 201 response:

```json
{
  "courseId": "web-security",
  "studentName": "Aigerim",
  "id": 1
}
```

A one-character `studentName` returns 422, and an unknown course returns 404
with `{"detail":"Course not found"}`.
