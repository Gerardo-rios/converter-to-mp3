# YouTube to MP3 Converter API

This project is a YouTube to MP3 converter API built using FastAPI. It allows users to convert YouTube videos to MP3 format. The project uses Poetry for dependency management and Docker for containerization.

## Features

- Convert YouTube videos to MP3 format
- FastAPI for building the API
- Poetry for dependency management
- Docker for containerization

## Requirements

- Python 3.11+
- Poetry
- Docker

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/youtube_to_mp3_api.git
    cd youtube_to_mp3_api
    ```

2. Install dependencies using Poetry:
    ```sh
    poetry install
    ```

3. Run the FastAPI server:
    ```sh
    poetry run uvicorn app.main:app --reload
    ```

## Usage

To use the API, send a POST request to the `/convert` endpoint with the YouTube video URL. The API will respond with a link to download the MP3 file.

## Docker

To run the application using Docker:

1. Build the Docker image:
    ```sh
    docker build -t youtube_to_mp3_api .
    ```

2. Run the Docker container:
    ```sh
    docker run -p 8000:8000 youtube_to_mp3_api
    ```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## Acknowledgements

- [FastAPI](https://fastapi.tiangolo.com/)
- [Poetry](https://python-poetry.org/)
- [Docker](https://www.docker.com/)
