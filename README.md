# Yandex Backend Course

Exercise solutions from the Yandex Backend Developer course — Python fundamentals through Django, ~120 files across 4 lessons.

---

## Course Structure

### Lesson 1 — Python Fundamentals (55 exercises)
- Functions, arguments, return values
- Conditionals and loops
- Strings, lists, dicts, sets — operations and methods
- `datetime`, `Decimal`, working with dates and numbers
- Final project: grocery inventory manager (`add`, `find`, `amount` with batch tracking and expiry dates)

### Lesson 2 — Testing (3 exercises)
- Writing and running tests with `pytest`
- Test structure: `assert`, custom error messages
- Testing function existence and correct execution

### Lesson 3 — OOP (26 exercises)
- Classes, `__init__`, instance and class attributes
- Inheritance, `super()`, method overriding
- Encapsulation and attribute access
- Generators and generator expressions
- Projects: `Employee` hierarchy, Tic-Tac-Toe `Board` class

### Lesson 4 — Web & Django (35 exercises)
- URL building, query strings
- HTTP requests with `requests`
- Django project setup: apps, views, URLs, templates
- Multi-app project: `anfisa_for_friends` (homepage + about + ice_cream apps)

---

## Tech Stack

| | |
|---|---|
| Language | Python 3 |
| Testing | pytest |
| Web | Django 3.x |
| HTTP | requests |

---

## Structure

```
Yandex_backend_course/
├── Lesson_1/          # Python fundamentals (7 topics, 55 exercises)
├── Lesson_2/          # pytest basics (3 exercises)
├── Lesson_3/          # OOP (4 topics, 26 exercises)
└── Lesson_4/          # Web & Django (3 topics, 35 exercises)
    └── 3/project/     # anfisa_for_friends Django project
```

---

## Running Tests

`Lesson_2/1` contains a `pytest` example (`test_program.py` + `pytest.ini`).
To run it:

```bash
cd Lesson_2/1
pip install pytest
pytest -vv
```

Note: this particular test targets a `practicum` module (the course
platform's expected solution filename), which isn't part of this repo, so
running it standalone will fail at collection with
`ModuleNotFoundError: No module named 'practicum'`. This is a limitation of
how the exercise was submitted originally, not a regression.

Most other exercises are standalone scripts — run them directly, e.g.:

```bash
python3 Lesson_1/6/1.py
```

## Running the Django Project

`Lesson_4/3/project` is a small multi-app Django project
(`anfisa_for_friends`, with `homepage`, `about`, and `ice_cream` apps).

```bash
cd Lesson_4/3/project
pip install django
python3 manage.py migrate
python3 manage.py runserver
```

`python3 manage.py check` passes cleanly with no issues.

---

## Author

- GitHub: [Shipovmax](https://github.com/Shipovmax)
- Email: shipov.max@icloud.com
