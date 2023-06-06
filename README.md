![image](https://mentalhealth.ie/wp-content/uploads/2021/02/scale-of-emotions-with-emojis.jpg)

# Text Classification API

This is a simple API for text classification tasks. It allows you to classify text into predefined categories or labels using machine learning models. The API is built using Python and Flask, and it can be easily deployed and used for various text classification applications.

## Getting Started

To get started with the Text Classification API, follow the instructions below.

### Prerequisites

- Python 3.x
- pip package manager

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Hoaper/text-classification-api.git
   ```

2. Navigate to the project directory:

   ```bash
   cd text-classification-api
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

### Usage

1. Start the API server:

   ```bash
   uvicorn main:app --reload
   ```

   The server will start running on `http://localhost:8000`.

2. Send a POST request to the API endpoint for text uploading:

   ```bash
   curl -X POST -H "Content-Type: application/json" -d '{"text": "your_text_here", "lang": "your_language"}' http://localhost:8000/upload
   ```

   Replace `"your_text_here"` with the text you want to classify. <br />
   Replace `"your_language""` lang with lang that you want 

3. The API will return a JSON response containing token, save him.

4. Send A GET request to the API endpoint for text classification

    ```bash
    curl -X GET -H "Content-Type: application/json" http://localhost:8000/result?token=<your_token>
    ```    
    
    Replace `"your_token"` with token, that you saved before

## Contributing

Contributions to this project are welcome. If you find any issues or have ideas for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.
