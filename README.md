# Discord OpenAI Bot

This bot is an interface to the OpenAI Chat API.

The app provides a slash command `chatgpt` with a required arg `prompt` and 8 other optional args.

```py
prompt: str,
system_prompt: str = None,
model: str = 'gpt-3.5-turbo',
temperature: float = 1.0,
top_p: int = 1,
n: int = 1,
max_tokens: int = 64,
presence_penalty: float = 0.0,
frequency_penalty: float = 0.0,
```

Requires an OpenAI API Key and Discord Bot token.

## Running the app

1. Install Docker
2. Build the Docker image: `docker build -t openai_bot .`
3. Run a Docker container: `docker run openai_bot`