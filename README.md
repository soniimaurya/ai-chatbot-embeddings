🌐 Website-Based AI Chatbot using Embeddings

📌 Project Overview
This project is an AI-powered chatbot that answers user questions only from the content of a given website.
The chatbot first crawls and indexes the website, converts the content into embeddings, stores them in a vector database, and then retrieves relevant information to answer user queries.
If the answer is not present on the provided website, the chatbot responds with:
"The answer is not available on the provided website."

🎯 Objectives
-Crawl and extract meaningful content from a website
-Convert website text into vector embeddings
-Store embeddings efficiently using a vector database
-Implement a Question-Answering system based on similarity search
-Build an interactive web interface using Streamlit

🏗️ System Architecture

-Website URL Input
-Web Crawling & Content Extraction
-Text Cleaning & Chunking
-Embedding Generation
-Vector Storage (FAISS)
-Query Processing
-Similarity Search
-Answer Generation
-Streamlit Web Interface

🛠️Technologies Used

🔹 Programming Language
-Python

🔹 Libraries & Frameworks
-Streamlit – Web interface
-LangChain – Text splitting & workflow
-SentenceTransformers – Embedding generation
-FAISS – Vector database for similarity search
-BeautifulSoup – Web scraping
-Requests – HTTP requests

🤖 Embedding Model Used

-Model: all-MiniLM-L6-v2
Why this model?
*Lightweight and fast
*Produces high-quality sentence embeddings
*Ideal for semantic similarity tasks
*Works well on CPU (no GPU required)

🗄️ Vector Database
FAISS (Facebook AI Similarity Search)
Why FAISS?
-Efficient similarity search
-Fast retrieval even with large text chunks
-Open-source and easy to integrate
-Suitable for local development

website-chatbot/
│
├── app.py                  # Streamlit user interface
├── crawler.py              # Website crawling logic
├── processor.py            # Text cleaning & chunking
├── embeddings.py           # Embedding creation & storage
├── chatbot.py              # Question-answering logic
├── requirements.txt        # Required libraries
├── README.md               # Project documentation
└── data/                   # Stored embeddings & metadata


⚙️ Installation & Setup (VS Code)
1️⃣ Clone or Download Project
git clone https://github.com/your-username/website-ai-chatbot.git
cd website-ai-chatbot

2️⃣ Install Dependencies
pip install requests beautifulsoup4 langchain langchain-community langchain-text-splitters sentence-transformers faiss-cpu streamlit

pip install requests beautifulsoup4 langchain langchain-community langchain-text-splitters sentence-transformers faiss-cpu streamlit
streamlit run app.py


3️⃣ Run the Application
streamlit run app.py


