# Expense Tracker (Beginner -> Intermediate Python Project)

A CLI-based expense tracker that helps you practice:

- Variables, loops, conditionals
- Functions and modular code
- Lists and dictionaries
- Dataclasses and type hints
- Error handling (`try/except`)
- File handling with JSON and CSV
- Basic reporting with comprehensions

## Features

- Add expense
- View all expenses
- Update expense
- Delete expense
- Filter by category
- Monthly summary
- Category summary
- Save and load data from JSON
- Export to CSV

## Project Structure

```text
expense_tracker/
  app.py
  tracker.py
  storage.py
  models.py
  data/
    expenses.json
```

## Run

From the parent directory:

```bash
python expense_tracker/app.py
```

## Suggested Learning Steps

1. Run the app and add 10-15 expenses.
2. Add a new field (like `payment_method`) to `Expense`.
3. Add a date-range report feature.
4. Add input validation for categories.
5. Write 3-5 tests for `tracker.py`.
