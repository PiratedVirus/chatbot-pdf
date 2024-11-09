# chatbot-pdf

## Performance Evaluation

To evaluate the model performance in production, we propose the following method:

### Metrics

1. **Response Accuracy**: Measure the accuracy of the responses provided by the model. This can be done by comparing the model's responses to a set of predefined correct answers.

2. **Response Time**: Measure the time taken by the model to respond to a query. This can help in identifying any performance bottlenecks.

3. **User Feedback**: Collect feedback from users regarding the relevance and accuracy of the responses. This can be done through a feedback form or rating system.

### Evaluation Process

1. **Data Collection**: Collect a set of queries and their corresponding correct answers. This can be done by manually creating a dataset or using existing datasets.

2. **Model Testing**: Test the model using the collected dataset and measure the response accuracy and response time.

3. **User Feedback Collection**: Deploy the model in production and collect user feedback on the responses provided by the model.

4. **Performance Analysis**: Analyze the collected data to identify any performance issues and areas for improvement.

5. **Model Improvement**: Use the insights gained from the performance analysis to improve the model and repeat the evaluation process.

## How to Use

### Setup

1. **Install Dependencies**: Make sure you have Python installed. Then, install the required dependencies using pip:

    ```bash
    pip install fastapi pydantic PyPDF2 transformers
    ```

2. **Run the FastAPI Application**: Start the FastAPI application by running the following command:

    ```bash
    uvicorn app:app --reload
    ```

### Upload a PDF

1. **Upload Endpoint**: Use the `/upload` endpoint to upload a PDF document. You can use tools like `curl` or Postman to upload the file.

    ```bash
    curl -X POST "http://127.0.0.1:8000/upload" -F "file=@your_document.pdf"
    ```

2. **Response**: If the upload is successful, you will receive a message indicating that the PDF document was uploaded successfully.

### Ask a Question

1. **Query Endpoint**: Use the `/query` endpoint to ask a question based on the uploaded document. You can use tools like `curl` or Postman to send the query.

    ```bash
    curl -X POST "http://127.0.0.1:8000/query" -H "Content-Type: application/json" -d '{"question": "Your question here"}'
    ```

2. **Response**: The API will return an answer based on the document. If no relevant answer is found, it will respond with "I don't know the answer".
