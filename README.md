# NoteFellas

NoteFellas is a simple web application where students can upload, browse, and download study materials (notes or scripts) for their courses. Users can leave reviews and save favorite notes.

## User types

- **Guest** - can browse all notes, view details, and download files
- **Registered user** - can do everything a guest can, plus upload their own notes, edit/delete their own notes, add reviews, and save notes to favorites
- **Admin (staff)** - has access to the admin panel, where they can manage users, notes, and reviews

## Technologies used

- **Backend**: Django, Django REST Framework
- **Frontend**: HTML, CSS, JavaScript
- **Database**: SQLite 
- **Other**: Google Fonts 

## Features

- User registration and login
- Upload, edit, delete notes (with file upload)
- Reviews/ratings on notes
- Favorite notes (AJAX)
- Live search by course name (AJAX, using own REST API)
- Client-side form validation
- Responsive design (CSS Grid/Flexbox + media queries)

## How to run the project

1. Clone the repository
```bash
git clone https://github.com/Lucija611/WebProgramiranje-projekt.git
cd NoteFellas
```

2. Create and activate a virtual environment
```bash
python -m venv venv
```
Windows:
```bash
venv/Scripts/activate
```

3. Install requirements
```bash
pip install -r requirements.txt
```

4. Migrations
```bash
python manage.py migrate
```

5. Run the server
```bash
python manage.py runserver
```

6. Open the app in your browser
```
http://127.0.0.1:8000/
```
