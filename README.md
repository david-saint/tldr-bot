# TL;DR Bot

A Twitter bot that summarizes tweet threads into concise TL;DR bullet points using OpenAI.

## Setup

1. **Clone the repository**:
    ```bash
    git clone https://github.com/david-saint/tldr_bot.git
    cd tldr_bot
    ```

2. **Create and activate a virtual environment**:
    ```bash
    python -m venv tldr_bot_env
    source tldr_bot_env/bin/activate  # On Windows: tldr_bot_env\Scripts\activate
    ```

3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up environment variables**:
    Create a `.env` file in the root directory and add your API keys:
    ```env
    TWITTER_API_KEY=your_twitter_api_key
    TWITTER_API_SECRET_KEY=your_twitter_api_secret_key
    TWITTER_ACCESS_TOKEN=your_twitter_access_token
    TWITTER_ACCESS_TOKEN_SECRET=your_twitter_access_token_secret
    OPENAI_API_KEY=your_openai_api_key
    ```

5. **Run the bot**:
    ```bash
    python bot.py
    ```

## Usage

Mention @tldr_app in a thread to get a summarized version of the thread in bullet points.
