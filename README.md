# Flask Phase
A self-directed learning phase focused on Flask web development. From learning the fundamentals to building a multi-page web application with a real database.

## Phase Goal
Learn how Python and HTML communicate through Flask. Understand routing, HTTP methods, the request-response cycle, database integration, and Jinja2 templating by building progressively more complex projects.

## Folders

### Topic 1 — Flask Fundamentals
A minimal two-template Flask app where a user enters their name and the next page displays a personalized welcome message. No database and no styling yet, it is just for learning the raw mechanics of how Flask maps URLs to Python functions and how Jinja2 renders dynamic content.

**Key concepts:** Routes, `render_template`, `request.form`, GET and POST basics

---

### Project 5 — Pando (Study Session Tracker)
A study session tracker with a home page displaying logged sessions and an add session form. I built it as a direct application of the fundamentals from topic 1. Same two-template structure but now with a real database, CRUD operations, and meaningful user data which are the logs of every session.

**Key concepts:** SQLite integration, `fetchone` vs `fetchall`, separation of route logic and database logic, the full request-response cycle

---

### Project 6 — Orchid (Personal Finance Tracker)
A personal finance tracker with four pages: Home, Accounts, Categories, and Transactions. Each page has complete CRUD via modals.

**Key concepts:** Jinja2 template inheritance, modals over page navigation, SQL JOINs, soft delete, Post/Redirect/Get pattern, CSS Grid, foreign key enforcement, filter handling with `or None`

---

## Growth Across the Phase
Each project was a deliberate upgrade of the last. A new project introduces more templates, more features, more complexity. Topic 1 established my foundation on the relationship of Flask and Web Development. In Project 5 I applied it with a real database where users can enter a study session. For Project 6, I pushed beyond my comfort zone into multi-table queries, template inheritance using jinja2, and patterns like PRAGMA and guard clauses that reflect how real web apps handle data integrity and safe data handling.

## How to Run Each Project
Navigate to the project folder and follow the README inside it.