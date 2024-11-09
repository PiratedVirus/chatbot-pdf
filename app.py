import PyPDF2
from transformers import pipeline

# Load the open-source LLM (e.g., GPT-Neo)
generator = pipeline('text-generation', model='EleutherAI/gpt-neo-2.7B')

# Step 1: Upload the PDF File via Terminal
def upload_document():
    file_path = input("Enter the path to your PDF file: ")
    try:
        with open(file_path, "rb") as file:
            pdf_reader = PyPDF2.PdfReader(file)
            document_text = ""
            for page in pdf_reader.pages:
                document_text += page.extract_text()
            print("PDF uploaded and processed successfully.")
            return document_text
    except Exception as e:
        print(f"Error reading the PDF file: {e}")
        return ""

# Step 2: Ask Questions About the Uploaded Document
def query_document(document_text):
    while True:
        question = input("\nEnter your question (or type 'exit' to quit): ").strip()
        if question.lower() == "exit":
            print("Goodbye!")
            break

        if not document_text:
            print("No document uploaded. Please upload a document first.")
            break

        # Split the document into chunks
        chunks = [document_text[i:i+1000] for i in range(0, len(document_text), 1000)]

        # Perform semantic search to retrieve the top 3 relevant chunks
        relevant_chunks = []
        for chunk in chunks:
            if question.lower() in chunk.lower():
                relevant_chunks.append(chunk)
            if len(relevant_chunks) >= 3:
                break

        if not relevant_chunks:
            print("Answer: I don't know the answer.")
            continue

        # Generate a response using the open-source LLM
        prompt = f"Context: {' '.join(relevant_chunks)}\n\nQuestion: {question}\nAnswer:"
        response = generator(prompt, max_length=50, num_return_sequences=1)
        print(f"Answer: {response[0]['generated_text']}")

# Main Script
if __name__ == "__main__":
    print("Welcome to the PDF Question-Answering Chatbot!")
    document_text = upload_document()
    if document_text:
        query_document(document_text)