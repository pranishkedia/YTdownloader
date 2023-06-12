# YTdownloader
A command-line YouTube downloader script written in Python using the `pytube` library. This script allows you to download videos from YouTube and save them to your local machine.

## Prerequisites

Make sure you have the following installed on your system:

- Python 3.x
- `pytube` library

## Installation

1. Clone the repository:

   ```shell
   git clone https://github.com/your-username/youtube-downloader.git
   ```

2. Install the required dependencies:
   ```shell
   pytube
   ```
## Usage

1. Open a terminal and navigate to the project directory:
   ```shell
   cd youtube-downloader
   ```

2. Run the script with the following command:
   ```shell
   python youtube_downloader.py [YouTube video URL]
   ```

   Replace [YouTube video URL] with the URL of the YouTube video you want to download.  
   The script will fetch information about the video, such as title and view count.  
   It will then download the highest resolution version of the video and save it to the specified directory.  
   Note: Update the directory path in the download() function to the desired location on your system.

## Example

Here's an example of how to use the script:

   ```shell
   python youtube_downloader.py https://www.youtube.com/watch?v=dQw4w9WgXcQ
   ```


## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvement, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License.

Please make sure to update the README with any additional information or customization required for your specific use case.