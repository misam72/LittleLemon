# LittleLemon

LittleLemon is a task management application that has been built using Python and React. The app provides a simple and intuitive interface for users to manage their tasks, set deadlines, and track their progress.

## Features

- Create, edit, and delete tasks
- Set deadlines and priorities for tasks
- Categorize tasks by project or tag
- Search and filter tasks by various criteria
- Mark tasks as completed and track progress
- Receive notifications for upcoming or overdue tasks
- Sync tasks across multiple devices

## Technologies Used

- Python for the backend server
- Flask for building the RESTful API
- MongoDB for the database
- React.js for the frontend user interface
- Bootstrap for styling and layout

## Installation

To install LittleLemon, follow these steps:

1. Clone the repository to your local machine.
2. Navigate to the project directory and run `pip install -r requirements.txt` to install the necessary Python packages.
3. Create a `.env` file in the project root and add the necessary environment variables (see `.env.example` for reference).
4. Start the Flask server by running `python app.py`.
5. In a separate terminal window, navigate to the `client` directory and run `npm install` to install the necessary frontend dependencies.
6. Start the React development server by running `npm start`.
7. Open `localhost:3000` in your web browser to access the application.

Note: LittleLemon requires a MongoDB instance for full functionality. Make sure to set up the database and add the necessary configuration details to your `.env` file.

## Contributing

Thank you for considering contributing to LittleLemon! To contribute, please follow these steps:

1. Fork the repository to your own GitHub account.
2. Create a new branch for your contribution.
3. Make your changes and commit them with a descriptive commit message.
4. Push your changes to your branch on your forked repository.
5. Open a pull request to the original repository, detailing your changes and why they should be merged.

## License

LittleLemon is licensed under the MIT License. See `LICENSE` for more information.