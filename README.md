# 🤖 AI-Powered Chat & Vision Applications  

## 🚀 Overview  
This repository contains multiple AI-powered applications built using **Google Gemini AI** and **Streamlit**. These apps allow users to interact with AI for text-based Q&A, conversational chat, and image-based Q&A.  

## 📌 Applications Included  

### 1️⃣ **Simple Chatbot (`app.py`)**  
🔹 A basic Q&A chatbot that answers user queries using Google Gemini AI.  
🔹 Provides direct responses to user input.  

### 2️⃣ **AI Chatbot with Chat History (`chat.py`)**  
🔹 A conversational chatbot with **chat history** support.  
🔹 Stores past interactions to maintain context in conversations.  

### 3️⃣ **Multimodal Chatbot – Image & Text (`vision.py`)**  
🔹 Accepts both text and image inputs.  
🔹 Analyzes images and provides AI-generated insights.  

## 🛠️ Installation  

1. **Clone the repository**  
   ```bash
   git clone https://github.com/your-repo/ai-chat-vision.git
   cd ai-chat-vision
Create a virtual environment (optional but recommended)

bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

Install dependencies

bash
pip install -r requirements.txt


Set up the API key
Create a .env file in the project root and add your Google API Key:

ini
GOOGLE_API_KEY=your_google_api_key_here

▶️ Usage
Run the Simple Chatbot
bash
streamlit run app.py

Run the AI Chatbot with Chat History
bash
streamlit run chat.py

Run the Image & Text Chatbot
bash
streamlit run vision.py
📚 Dependencies
The project requires the following Python libraries (from requirements.txt):

streamlit – Web UI framework
google-generativeai – Gemini AI integration
python-dotenv – Environment variable management
PyPDF2 – PDF processing (for future enhancements)
faiss-cpu – Efficient vector search
langchain – AI model chaining
langchain_google_genai – Google AI integration with LangChain

🔥 Future Enhancements
✅ Integration with PDF and Document Parsing
✅ Enhanced OCR capabilities for invoice extraction
✅ Fine-tuned AI models for improved accuracy
✅ Memory-based chat responses for better context retention

🤝 Contribution
Feel free to fork, modify, and contribute to the project!
