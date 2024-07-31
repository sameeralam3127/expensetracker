# Expense Tracker

A simple web application to manage and track expenses. Built with Django and Tailwind CSS for a modern and responsive user interface.
<img width="924" alt="image" src="https://github.com/user-attachments/assets/874556cc-2d16-47d7-899e-147693aa6744">
<img width="901" alt="image" src="https://github.com/user-attachments/assets/e1dfc5a0-da96-4be6-90f6-21d814dbbc81">


## Features

- Add new expenses with name, amount, and category.
- View a list of all expenses,edit and delete in a table format.
- Responsive design with Tailwind CSS.

## Prerequisites

- Python 3.8 or higher
- Django 5.x
- Tailwind CSS

## Installation

Follow these steps to set up the project locally.

### 1. Clone the Repository

```bash
git clone https://github.com/sameer358/expensetracker.git
cd expensetracker
```

### 2. Create a Virtual Environment

```bash
python -m venv env
```

### 3. Activate the Virtual Environment

- **On Windows:**

```bash
env\Scripts\activate
```

- **On macOS/Linux:**

```bash
source env/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Apply Migrations

```bash
python manage.py migrate
```

### 6. Run the Development Server

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` in your web browser to see the application in action.

## Configuration

### Environment Variables

Create a `.env` file in the project root directory for environment variables (if needed). Example:

```
DEBUG=True
SECRET_KEY=your_secret_key
```

### Tailwind CSS

Ensure Tailwind CSS is properly configured in your Django settings. Refer to the [Tailwind CSS with Django documentation](https://tailwindcss.com/docs/guides/django) for detailed setup instructions.

## Usage

- **Adding Expenses**: Fill out the form with the expense details and click the "Add" button.
- **Viewing Expenses**: The table displays all the added expenses with their details.

## Contributing

1. **Fork the Repository**: Create your own fork of the repository.
2. **Create a Branch**: Create a new branch for your feature or bug fix.
3. **Commit Changes**: Make your changes and commit them with a clear message.
4. **Push to Your Fork**: Push your changes to your forked repository.
5. **Open a Pull Request**: Open a pull request to the main repository with a description of your changes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

