# Mini RAG From A to Z

## Overview

Mini RAG From A to Z is a FastAPI-based project that processes and manages project data. It includes functionalities for uploading files, processing file content into chunks, and storing these chunks in a MongoDB database.

## Features

- Upload files to specific projects
- Validate file types and sizes
- Process file content into manageable chunks
- Store project and chunk data in MongoDB
- Retrieve and manage project data

## Project Structure

 file:

```markdown
## Project Structure
miniRag/
├── docker/
│   ├── .gitignore
│   └── docker-compose.yml
├── src/
│   ├── assets/
│   │   ├── .gitignore
│   │   ├── .gitkeep
│   │   └── adel.txt
│   ├── controllers/
│   │   ├── BaseController.py
│   │   ├── DataController.py
│   │   ├── PorcessController.py
│   │   ├── ProjectController.py
│   │   └── __init__.py
│   ├── helpers/
│   │   ├── __init__.py
│   │   └── config.py
│   ├── models/
│   │   ├── BaseDataModel.py
│   │   ├── ChunkModel.py
│   │   ├── ProjectModel.py
│   │   ├── __init__.py
│   │   ├── db_schemas/
│   │   │   ├── __init__.py
│   │   │   ├── data_chunk.py
│   │   │   └── project.py
│   │   ├── enums/
│   │   │   ├── DataBaseEnum.py
│   │   │   ├── PorcessingEnum.py
│   │   │   ├── ResponseEnum.py
│   │   │   └── __init__.py
│   ├── routes/
│   │   ├── base.py
│   │   ├── data.py
│   │   ├── schemas/
│   │   │   ├── __init__.py
│   │   │   └── data_schema.py
│   │   └── __init__.py
│   ├── .gitignore
│   ├── .gitkeep
│   ├── env.txt
│   ├── error.txt
│   ├── main.py
│   ├── requirements.txt
│   └── run.sh
├── LICENSE
└── 
README.md
```

This structure provides an overview of the project's organization, making it easier for contributors and users to navigate the codebase.
This structure provides an overview of the project's organization, making it easier for contributors and users to navigate the codebase.

## Getting Started

### Prerequisites

- Python 3.8+
- Docker
- MongoDB

### Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/miniRag.git
    cd miniRag
    ```

2. Create a virtual environment and activate it:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the dependencies:
    ```sh
    pip install -r src/requirements.txt
    ```

4. Set up environment variables:
    ```sh
    cp src/env.txt .env
    # Edit .env file with your configuration
    ```

5. Start the MongoDB service using Docker:
    ```sh
    cd docker
    docker-compose up -d
    ```

### Running the Application

1. Run the FastAPI application:
    ```sh
    cd src
    ./run.sh
    ```

2. Access the application at `http://localhost:5000`.

### API Endpoints

- **Home**: `GET /api/v1/`
- **Upload Data**: `POST /api/v1/data/upload/{project_id}`
- **Process Data**: `POST /api/v1/data/porcess/{project_id}`

### Configuration

The application configuration is managed via environment variables defined in the `.env` file. Key settings include:

- [APP_NAME](http://_vscodecontentref_/32)
- [APP_VERSION](http://_vscodecontentref_/33)
- [APP_PORT](http://_vscodecontentref_/34)
- [APP_HOST](http://_vscodecontentref_/35)
- [APP_URL](http://_vscodecontentref_/36)
- [OPENAI_API_KEY](http://_vscodecontentref_/37)
- [FILE_ALLOWED_TYPES](http://_vscodecontentref_/38)
- [FILE_MAX_SIZE](http://_vscodecontentref_/39)
- [FILE_DEFAULT_CHANK_SIZE](http://_vscodecontentref_/40)
- [MONGODB_URL](http://_vscodecontentref_/41)
- [MONGODB_DATABASE](http://_vscodecontentref_/42)

### Contributing

Contributions are welcome! Please open an issue or submit a pull request for any changes.

### License

This project is licensed under the terms specified in the [LICENSE](http://_vscodecontentref_/43) file.

### Acknowledgements

Special thanks to all contributors and open-source projects that made this project possible.
