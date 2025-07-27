# yt-dlp API

yt-dlp API is a FastAPI-based project that provides an interface for interacting with the [yt-dlp](https://github.com/yt-dlp/yt-dlp) library. It allows users to retrieve video information and download videos via HTTP endpoints.

## Features

- **Retrieve Video Information**: Get metadata and details about a video using its URL.
- **Download Videos**: Download videos in various formats and stream them as a response.

## Project Structure

```
ytdlpapi/
├── api.py                     # Entry point for the FastAPI application
├── controller/
│   ├── info_controller.py     # Controller for video information endpoints
│   ├── download_controller.py # Controller for video download endpoints
├── service/
│   ├── info_service.py        # Service for handling video information logic
│   ├── download_service.py    # Service for handling video download logic
├── client/
│   ├── yt_dlp_client.py       # Client wrapper for yt-dlp library
├── container/
│   ├── default_container.py   # Dependency injection container
```

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/yt-dlp-api.git
   cd yt-dlp-api
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Ensure `yt-dlp` is installed:
   ```bash
   pip install yt-dlp
   ```

## Usage

1. Start the FastAPI server:
   ```bash
   python ytdlpapi/api.py
   ```

2. Access the API documentation at [http://localhost:8000/docs](http://localhost:8000/docs).

3. Use the following endpoints:

   - **GET `/info`**: Retrieve video information.
     - Query Parameter: `url` (required) - The URL of the video.
     - Example:
       ```bash
       curl "http://localhost:8000/info?url=https://www.youtube.com/watch?v=example"
       ```

   - **GET `/download`**: Download a video.
     - Query Parameters:
       - `url` (required) - The URL of the video.
       - `format` (optional) - The desired format (e.g., `mp4`).
     - Example:
       ```bash
       curl "http://localhost:8000/download?url=https://www.youtube.com/watch?v=example&format=mp4" -o video.mp4
       ```

4. **Health Check**:
   - **GET `/health`**: Check the health status of the API.
     - Example:
       ```bash
       curl http://localhost:8000/health
       ```

## Configuration

The application uses a dependency injection container (`DefaultContainer`) to manage configurations. Update the `api_host` and `api_port` variables in the container to change the server's host and port.

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [yt-dlp](https://github.com/yt-dlp/yt-dlp) for providing the core functionality for video downloading and information retrieval.
- [FastAPI](https://fastapi.tiangolo.com/) for the