# NeilGPT

NeilGPT is a cosmic-themed chatbot that combines advanced conversational AI with real-time voice interactions. The application features a dynamic chat interface that supports both text and speech input, powered by speech-to-text (STT) and text-to-speech (TTS) functionalities.


https://github.com/user-attachments/assets/b6ecc74d-3cc9-4ead-9948-f2125a2e69fd


## Key Features

- **Conversational Chat Interface:**  
  Engage with NeilGPT via text. The chat interface is designed with a cosmic theme, complete with animated backgrounds and stars.

- **Speech-to-Text (STT):**  
  Convert spoken language to text using the Hugging Face Whisper Tiny API, enabling hands-free interaction.

- **Text-to-Speech (TTS):**  
  Hear responses read aloud via a TTS system that leverages OpenAI's TTS service via RapidAPI.

- **Responsive & Intuitive Design:**  
  A user-friendly interface that adapts to different screen sizes and provides animated visual cues during interactions.

- **Seamless Integration:**  
  Frontend built in React and backend powered by FastAPI ensure a smooth and interactive experience.

## Tech Stack

### Frontend
- **React:** For building dynamic user interfaces.
- **Tailwind CSS:** (or similar) for styling and responsive design.
- **Lucide-React:** Icon library for intuitive UI icons.
- **Axios:** For making HTTP requests to the backend.
- **Environment Variables:** Managed via `.env` files (using `REACT_APP_` prefix for Create React App or `VITE_` for Vite).

### Backend
- **FastAPI:** A modern, high-performance web framework for building APIs with Python.
- **Uvicorn:** ASGI server for serving FastAPI applications.
- **Pandas:** For data manipulation and processing.
- **LlamaIndex & ReActAgent:** For building and querying the conversational AI engine.
- **Python Dotenv:** For loading environment variables.
- **CORS Middleware:** Allows cross-origin requests from the frontend.

### External APIs
- **Hugging Face Whisper Tiny:** For converting speech to text.
- **OpenAI TTS via RapidAPI:** For converting text to speech.

### Deployment
- **Render:** Hosting backend (as a web service) on Render’s free tier.
