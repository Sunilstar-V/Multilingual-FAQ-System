# Django FAQ Management System

A Django application for managing Frequently Asked Questions (FAQs) with multi-language support and WYSIWYG editor integration. This project demonstrates the ability to create a RESTful API for managing FAQs, including translation features and caching mechanisms.

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Caching](#caching)
- [Unit Tests](#unit-tests)
- [Contributing](#contributing)
- [License](#license)

## Features

- **WYSIWYG Editor**: Integrated using `django-ckeditor` for rich text formatting of answers.
- **Multi-language Support**: Store translations for FAQs in multiple languages (e.g., Hindi, Bengali).
- **REST API**: Create, read, update, and delete FAQs via a RESTful API.
- **Caching**: Implemented caching using Redis to improve performance.
- **Automated Translations**: Use Google Translate API or `googletrans` to automate translations during FAQ creation.

## Technologies Used

- Django 5.x
- Django REST Framework
- django-ckeditor
- Redis (for caching)
- Google Translate API or googletrans
- PostgreSQL or SQLite (for database)

## Installation

1. Clone the repository:

git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
cd YOUR_REPO_NAME
text

2. Create a virtual environment:

python -m venv venv
text

3. Activate the virtual environment:

- On Windows:

  ```
  venv\Scripts\activate
  ```

- On macOS/Linux:

  ```
  source venv/bin/activate
  ```

4. Install the required packages:

pip install -r requirements.txt
text

5. Set up environment variables (if needed) in a `.env` file or directly in your environment.

6. Run database migrations:

python manage.py migrate
text

7. Create a superuser to access the admin panel:

python manage.py createsuperuser
text

8. Start the development server:

python manage.py runserver
text

## Usage

You can access the application at `http://127.0.0.1:8000/`. Use the admin panel to manage FAQs or interact with the API directly.

## API Endpoints

### Fetch FAQs

- **Fetch FAQs in English (default)**:
curl http://localhost:8000/api/faqs/
text

- **Fetch FAQs in Hindi**:
curl http://localhost:8000/api/faqs/?lang=hi
text

- **Fetch FAQs in Bengali**:
curl http://localhost:8000/api/faqs/?lang=bn
text

### Create FAQ

POST /api/faqs/
Content-Type: application/json
{
"question": "What is Django?",
"answer": "<p>Django is a web framework.</p>",
"question_hi": "डjango क्या है?",
"answer_hi": "<p>डjango एक वेब फ्रेमवर्क है।</p>",
"question_bn": "ডjango কি?",
"answer_bn": "<p>ডjango একটি ওয়েব ফ্রেমওয়ার্ক।</p>"
}
text

### Update FAQ

PUT /api/faqs/{id}/
Content-Type: application/json
{
"question": "Updated question?",
"answer": "<p>Updated answer.</p>"
}
text

### Delete FAQ

DELETE /api/faqs/{id}/
text

## Caching

This application uses Redis to cache translations for improved performance. Ensure that Redis is installed and running on your machine.

## Unit Tests

Unit tests are written using `pytest`. To run the tests, execute:

pytest
text

## Contributing

Contributions are welcome! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeature`).
3. Make your changes and commit them (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Open a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
