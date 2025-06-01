
Task Management API

A simple Django-based RESTful API for managing tasks. It allows users to create tasks, retrieve all tasks, and manage individual task details including updates and deletions.
Example task data is already preloaded into the database, and also available in example-data.json for reference or reuse.


Features

- Create new tasks
- Retrieve all tasks
- View, update, or delete individual tasks
- Status tracking (Pending, In Progress, Completed)
- Filtering and sorting by status, due date, and more
- Smart task suggestion for incomplete tasks


Tech Stack

- Python 3.x
- Django
- SQLite (default database)



Project Structure

api/
apps.py         # Django app configuration
models.py       # Task model definition
urls.py         # API route definitions
views.py        # Views to handle HTTP requests


Installation

1. Clone the repository
   git clone https://github.com/BalintKiss2001/django_crud.git
   cd crudproject

2. Create a virtual environment
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate

3. Install dependencies
   pip install -r requirements.txt

4. Run migrations
   python manage.py migrate

5. Start the development server
   python manage.py runserver

---

API Endpoints

 Method  Endpoint            Description              

 GET     api/tasks/             Retrieve all tasks       
 POST    api/tasks/create       Create a new task        
 GET     api/tasks/<int:pk>     Get task details         
 PUT     api/tasks/<int:pk>     Update a task            
 DELETE  api/tasks/<int:pk>     Delete a task
 GET     api/smart-suggestions  Smart task suggestion for pending tasks           



Query Parameters

The GET /tasks/ endpoint supports filtering and sorting through query parameters:

Filtering

You can filter tasks based on their status:

GET /tasks/?status=pending
GET /tasks/?status=in_progress
GET /tasks/?status=completed

You can also filter by a due date range:

GET /tasks/?due_after=2025-05-01&due_before=2025-06-01

Sorting

Sort tasks by any field, such as due date or creation date:

GET /tasks/?ordering=due_date
GET /tasks/?ordering=-creation_date

Prefix with '-' for descending order.

Combined Example

Get all "in progress" tasks sorted by due date ascending:

GET /tasks/?status=in_progress&ordering=due_date

Smart Task Suggestions

The system analyzes the title and description of incomplete tasks and suggests follow-up tasks using common keywords. Suggestions are derived from frequently observed patterns in completed tasks.

For example:
- A task titled "API Review" may suggest:
  - "Follow-up Meeting"
  - "Generate API Docs"
- A task titled "Client Feedback Analysis" may suggest:
  - "Revise Based on Feedback"

Endpoint

GET `api/smart-suggestions/`  
Returns a list of incomplete tasks with their recommended follow-up actions.

Response Example

json:
[
  {
    "task_id": 12,
    "task_title": "Client Feedback Analysis",
    "status": "in_progress",
    "suggestions": [
      "Revise Based on Feedback"
    ]
  },
  {
    "task_id": 13,
    "task_title": "API Review",
    "status": "pending",
    "suggestions": [
      "Follow-up Meeting",
      "Generate API Docs"
    ]
  }
]