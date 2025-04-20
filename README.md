# BW Assistant – Chatbot with OpenAI and Yahoo Finance

This project is a personal assistant powered by **OpenAI** and **Yahoo Finance**, capable of retrieving historical stock prices and answering questions using **GPT-4o-mini**.

## 📌 Features

- Integration with OpenAI's API to generate intelligent responses.
- Fetch historical stock data using the `yfinance` library.
- Tool support for direct function calls.
- Simple terminal interface.

## 🛠️ Technologies Used

- Python
- OpenAI API
- Yahoo Finance (`yfinance`)
- `dotenv` for loading environment variables
- JSON for data handling

## 🚀 How to Run

1. **Clone this repository**  
   ```sh
   git clone https://github.com/your-username/your-repo.git
   cd your-repo
   ```

2. **Create and activate a virtual environment**  
   ```sh
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate   # Windows
   ```

3. **Install dependencies**  
   ```sh
   pip install -r requirements.txt
   ```

4. **Create a `.env` file and add your OpenAI key**  
   ```env
   OPENAI_API_KEY=your_api_key_here
   ```

5. **Run the chatbot**  
   ```sh
   python chatbot_finance.py
   ```
