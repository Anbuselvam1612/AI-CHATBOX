# AI-CHATBOX

## Description

**AI Chatbox** is an interactive web application built using Django and integrated with advanced conversational AI models from the Hugging Face Transformers library. This project serves as a practical example of how to deploy a machine learning model in a web application to create a chatbot capable of engaging in dynamic and coherent conversations with users.

The chatbot leverages the power of state-of-the-art language models to provide intelligent and contextually relevant responses. The project includes a simple and user-friendly web interface that allows users to interact with the chatbot, making it easy to integrate conversational AI into various applications.

## Features

- **Conversational AI Integration**: Utilizes pre-trained language models to understand and generate responses to user inputs.
- **Django Framework**: A powerful web framework used for rapid development and clean architecture.
- **User Interface**: A straightforward web interface for engaging with the chatbot.
- **Admin Panel**: Django's built-in admin interface for managing application data and settings.

## Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

### Steps

1. **Clone the Repository**

   ```bash
   git clone https://github.com/Anbuselvam1612/AI-CHATBOX.git
   cd AI-CHATBOX
   ```

2. **Set Up Virtual Environment**

   Create and activate a virtual environment:

   ```bash
   python -m venv env
   ```

   - **On Windows**:
     ```bash
     .\env\Scripts\activate
     ```

   - **On macOS/Linux**:
     ```bash
     source env/bin/activate
     ```

3. **Install Dependencies**

   Install the required packages from `requirements.txt`:

   ```bash
   pip install -r requirements.txt
   ```

4. **Apply Database Migrations**

   Set up the database schema:

   ```bash
   python manage.py migrate
   ```

5. **Create a Superuser**

   Create a Django superuser to access the admin interface:

   ```bash
   python manage.py createsuperuser
   ```

   Follow the prompts to create the superuser account.

6. **Run the Development Server**

   Start the Django development server:

   ```bash
   python manage.py runserver
   ```

   Open your browser and navigate to `http://127.0.0.1:8000/` to see the application in action.

## Usage

1. **Interact with the Chatbot**

   - Navigate to the home page of the application.
   - Enter your message in the input field and click "Send" to receive a response from the chatbot.

2. **Access the Admin Interface**

   - Go to `http://127.0.0.1:8000/admin/` in your web browser.
   - Log in using the superuser credentials created earlier to manage the application.

## Project Structure

- **`chatbot/`**: Contains the core Django app files.
  - **`views.py`**: Contains the logic for generating chatbot responses.
  - **`models.py`**: Defines the data models (if applicable).
  - **`templates/`**: HTML templates for the chatbot's web interface.
- **`chatbot_project/`**: Contains project-wide settings and configuration.
  - **`settings.py`**: Configuration settings for the Django project.
  - **`urls.py`**: URL routing for the project.
  - **`wsgi.py`**: WSGI configuration for deploying the project.
- **`manage.py`**: Django's command-line tool for administrative tasks.
- **`requirements.txt`**: Lists the Python packages required for the project.
- **`.gitignore`**: Specifies files and directories to ignore in version control.
- **`README.md`**: This documentation file.

## Contributing

Contributions are welcome! If you have ideas for improvements or new features, please fork the repository and submit a pull request.

### How to Contribute

1. **Fork the Repository**: Click "Fork" on GitHub to create your own copy.
2. **Clone Your Fork**: 
   ```bash
   git clone https://github.com/your-username/AI-CHATBOX.git
   ```
3. **Create a Branch**: 
   ```bash
   git checkout -b your-feature-branch
   ```
4. **Make Changes**: Modify or add files as needed.
5. **Commit Changes**: 
   ```bash
   git add .
   git commit -m "Describe your changes"
   ```
6. **Push Changes**: 
   ```bash
   git push origin your-feature-branch
   ```
7. **Submit a Pull Request**: Open a pull request on GitHub.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- **Hugging Face**: For their powerful pre-trained language models.
- **Django**: For providing the web framework.
- **Open Source Community**: For their contributions and support.
