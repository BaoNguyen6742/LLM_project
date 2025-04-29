# Omni Chat

Omni Chat is a powerful and versatile chat application that allows users to communicate seamlessly across multiple platforms. With its advanced features and user-friendly interface, Omni Chat is designed to enhance your chatting experience.

## Usage

To use Omni Chat, you need to set up the environment and install the required dependencies. Follow the instructions below to get started.

### Prerequisites

- Python 3.12 or higher
- API keys for the platforms you want to connect to (Google AI Studio, OpenRouter and Groq)
- uv from Astral

### Installation

1. Clone the repository:

2. Run the following command to install the required dependencies:

    ```bash
    uv sync
    ```

3. Set up your environment variables for the API keys. You need create a `.env` file in the `.env` directory of the project and add the following lines:

    ```bash
    GROQ_API_KEY=your-api-key-here
    GG_API_KEY=your-api-key-here
    OPENROUTER_API_KEY=your-api-key-here
    ```

4. Run the application:

    ```bash
    cd src
    uv run main.py
    ```
