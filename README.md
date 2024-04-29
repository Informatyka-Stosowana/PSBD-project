# PSBD (Podstawy Systemów Baz Danych) Project

## Project setup

Prerequisites:
- `node.js` LTS (20.11.1) and `npm` (https://nodejs.org/en/download/)
- `docker` and `docker-compose` (https://docs.docker.com/get-docker/)
- If using VSCode, install [EditorConfig plugin](https://marketplace.visualstudio.com/items?itemName=EditorConfig.EditorConfig).
- `python` (https://www.python.org/downloads/) 

To setup the project:

1. Clone the repository,
2. In ./client directory run `npm install` to install tooling,
3. In ./server-python directory install the required packages using `pip install`.

To run the project:

1. In ./dockerfiles directory run `docker-compose up`,
2. In ./python-server directory run `python app.py`,
3. In ./client directory run `npm run serve`.
