# C3PI

Greetings, I am C3PI, an open-source AI assistant and chatbot powered by language models. I am fluent in over six million forms of communication, and I'm here to assist you.

## Installation

To install C3PI, clone the repository:
git clone https://github.com/shadowaxe99/C3PI.git

This will download the source code to your local machine. You will need Python 3.7 or later to run C3PI.

## Usage

C3PI can be run via Docker Compose. Start it with:
docker-compose up

This will start the backend API server and frontend UI. The backend API server handles the bot logic and accesses data, while the frontend UI allows you to configure conversation flows and test the bot.

The main components are:

- `Agent` - Core class that handles conversations. It uses language models to generate responses to user inputs.
- `DatabaseManager` - Manages access to SQLite database. It handles all database operations, including creating, reading, updating, and deleting data.
- `DataManager` - Retrieves data from database. It uses the DatabaseManager for its operations.
- `chains` - Modules that define conversation flows and logic. They determine how the bot responds to different user inputs.

## Architecture

C3PI is built using:

- Python, SQLite - For backend API and bot logic. Python is used for its powerful libraries and easy syntax, while SQLite is used for its simplicity and reliability.
- React, Node.js - For frontend UI. React is used for its component-based architecture and efficient updates, while Node.js is used for its event-driven architecture and non-blocking I/O model.
- Docker Compose - For running the app. Docker Compose is used for its service orchestration capabilities.

## Contributing

Contributions are most welcome! Open issues and PRs to improve C3PI. Please follow the contributing guidelines when making a contribution.

## License

C3PI is licensed under the MIT License. This means you are free to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the software, subject to the conditions stated in the license.

May the force be with you!