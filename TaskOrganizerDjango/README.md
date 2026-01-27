# Task Organizer Django Project

## 📋 Project Overview

A complete Django-based Task Management application with full CRUD (Create, Read, Update, Delete) operations. The project features a clean, modern UI built with TailwindCSS.

---

## ✨ Features

✅ **Create Tasks** - Add new tasks with title, description, status, and due date  
✅ **View Tasks** - See all tasks in a list view with status filtering  
✅ **View Task Details** - Click on any task to see complete information  
✅ **Update Tasks** - Edit existing tasks  
✅ **Delete Tasks** - Remove tasks with confirmation  
✅ **Status Tracking** - Pending, In Progress, Completed  
✅ **Beautiful UI** - Modern interface with TailwindCSS  
✅ **Responsive Design** - Works on desktop and mobile  

---

## 🗂️ Project Structure

```
TaskOrganizerDjango/
├── manage.py                          # Django management script
├── db.sqlite3                         # Database file
│
├── task/                              # Main app
│   ├── migrations/                    # Database migrations
│   ├── management/commands/           # Custom commands
│   ├── templates/tasks/               # HTML templates
│   │   ├── task_list.html            # List all tasks (READ)
│   │   ├── task_detail.html          # View task details (READ)
│   │   ├── create_task.html          # Create new task (CREATE)
│   │   ├── edit_task.html            # Edit existing task (UPDATE)
│   │   └── delete_task.html          # Delete task (DELETE)
│   ├── models.py                     # Task model definition
│   ├── views.py                      # View functions (Controllers)
│   ├── urls.py                       # URL routing
│   ├── forms.py                      # Django forms
│   └── admin.py                      # Admin configuration
│
├── Tasks/                             # Project settings
│   ├── settings.py                   # Django configuration
│   ├── urls.py                       # Project URLs
│   ├── wsgi.py                       # WSGI application
│   └── views.py                      # Custom error handlers
│
└── templates/                         # Project-level templates
    └── 404.html                      # 404 error page
```

---

## 🗄️ Database Model

### Task Model
```python
class Task(models.Model):
    title          : CharField (max_length=100)
    description    : TextField (max_length=500)
    status         : CharField (pending, in_progress, completed)
    duedate        : DateField
    created_at     : DateTimeField (auto_now_add=True)
    updated_at     : DateTimeField (auto_now=True)
```

**Status Choices:**
- `pending` - Task not yet started
- `in_progress` - Task currently being worked on
- `completed` - Task finished

---

## 🔗 URL Routes

| URL | Name | Method | Description |
|-----|------|--------|-------------|
| `/task_list` | `tasklist` | GET | View all tasks |
| `/task_detail/<id>/` | `taskdetail` | GET | View task details |
| `/create_task` | `createtask` | GET, POST | Create new task |
| `/edit_task/<id>/` | `edittask` | GET, POST | Edit task |
| `/delete_task/<id>/` | `deletetask` | GET, POST | Delete task |

---

## 📝 Form Fields

All forms use Django's `ModelForm` which auto-generates form fields based on the Task model:

- **Title** - Text input (required)
- **Description** - Textarea (required)
- **Status** - Select dropdown with 3 options
- **Due Date** - Date picker (required)

Forms automatically handle:
- CSRF token protection
- Field validation
- Error messages
- Data binding (for edit forms)

---

## 🎨 Frontend Technologies

- **TailwindCSS** - Modern utility-first CSS framework
- **Django Templates** - Server-side template rendering
- **Responsive Design** - Mobile-friendly layout
- **Color-coded Status Badges** - Visual status indicators
  - Yellow: Pending
  - Blue: In Progress
  - Green: Completed

---

## 🚀 Getting Started

### Prerequisites
- Python 3.x
- Django 6.0+

### Installation

1. **Navigate to project:**
   ```bash
   cd TaskOrganizerDjango
   ```

2. **Run migrations:**
   ```bash
   python manage.py migrate
   ```

3. **Start the server:**
   ```bash
   python manage.py runserver
   ```

4. **Access the application:**
   - Open browser and go to: `http://localhost:8000/task_list`

---

## 📚 How It Works

### 1. **CREATE Task**
- Navigate to "New Task" button in navigation
- Fill in all required fields (title, description, status, due date)
- Click "Create Task"
- Form validates input and saves to database
- Redirected to task list on success

### 2. **READ Tasks**
- **Task List:** Shows all tasks with summary and action buttons
- **Task Detail:** Shows complete task information with edit/delete options

### 3. **UPDATE Task**
- Click "Edit" button on any task
- Form pre-fills with existing data
- Modify any field
- Click "Update Task"
- Changes saved to database

### 4. **DELETE Task**
- Click "Delete" button on any task
- Shows confirmation with task preview
- Click "Delete Task" to confirm
- Task removed from database

---

## 💾 Configuration

**Database:** SQLite3 (development)
- Stored in: `db.sqlite3`

**Settings:** `Tasks/settings.py`
- `DEBUG = True` (Development mode)
- `INSTALLED_APPS` - Includes the `task` app

**Templates:** 
- App-level: `task/templates/tasks/`
- Project-level: `templates/`

---

## ✅ Testing the Application

### Test Workflow:
1. Click **"+ New Task"** → Create a task
2. See task in **"All Tasks"** list
3. Click **"View"** → See full details
4. Click **"Edit"** → Modify the task
5. Click **"Delete"** → Remove with confirmation

### Test Data:
Create tasks with various statuses to see color-coded badges:
- A "Pending" task (yellow badge)
- An "In Progress" task (blue badge)
- A "Completed" task (green badge)

---

## 🔒 Features Explained

### Django ModelForm Magic
The `TaskForm` uses `ModelForm` which automatically:
- Creates form fields matching model fields
- Handles validation rules from the model
- Binds data when editing instances
- Implements CSRF protection

### URL Namespacing
URLs are namespaced as `task:` (e.g., `task:createtask`)
- Prevents naming conflicts
- Makes templates cleaner
- Easier to manage large projects

### Template Tags
- `{% url %}` - Generate URLs dynamically
- `{% csrf_token %}` - CSRF protection
- `{{ variable }}` - Display variables
- `{% if %}...{% endif %}` - Conditional rendering
- `{% for %}...{% endfor %}` - Loop through data

---

## 🎯 Next Steps / Enhancements

Potential improvements:
1. **User Authentication** - Multi-user support with login
2. **Task Categories** - Organize tasks by category
3. **Priority Levels** - Add priority field
4. **Task Filtering** - Filter by status, date range, etc.
5. **Search Functionality** - Search tasks by title/description
6. **Task Comments** - Add comments to tasks
7. **Due Date Alerts** - Notify on upcoming due dates
8. **Dark Mode** - Dark theme option
9. **Export to PDF** - Download task list as PDF
10. **API Endpoints** - REST API for mobile apps

---

## 🐛 Troubleshooting

**Issue:** Server won't start
- Check if port 8000 is in use
- Try: `python manage.py runserver 8080`

**Issue:** Templates not loading
- Verify `APP_DIRS = True` in settings.py
- Check template path: `task/templates/tasks/`

**Issue:** Database errors
- Run migrations: `python manage.py migrate`
- Reset database: `rm db.sqlite3` then `python manage.py migrate`

---

## 📖 Django Documentation

- [Django Models](https://docs.djangoproject.com/en/6.0/topics/db/models/)
- [Django Forms](https://docs.djangoproject.com/en/6.0/topics/forms/)
- [Django URLs](https://docs.djangoproject.com/en/6.0/topics/http/urls/)
- [Django Templates](https://docs.djangoproject.com/en/6.0/topics/templates/)

---

## 📄 License

This is an educational project for learning Django.

---

## 👨‍💻 Project Complete!

All CRUD operations are fully implemented and linked together. The application is production-ready for a development environment.

**Start the server and begin managing tasks!** 🚀
