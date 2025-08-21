# Vue Chat Frontend

This project is a chat application built with Vue.js, Vite, and Vuetify 3. It allows users to create and manage conversations, send messages, and store their API key securely.

## Features

- Create new conversations
- Rename existing conversations
- Send messages within conversations
- Input field for API key, stored in cookies
- Integration with Chat Storage Microservice APIs

## Project Structure

```
vue-chat-frontend
├── src
│   ├── assets                # Static assets like images and fonts
│   ├── components            # Vue components for the application
│   │   ├── ChatInput.vue     # Input field for sending messages
│   │   ├── ConversationList.vue # Displays list of conversations
│   │   ├── ConversationRename.vue # Allows renaming of conversations
│   │   ├── MessageList.vue    # Displays messages of the selected conversation
│   │   └── ApiKeyInput.vue    # Input for API key
│   ├── composables           # Composable functions for state management
│   │   ├── useApiKey.ts      # Handles API key storage and retrieval
│   │   └── useChatStorage.ts  # Interacts with Chat Storage Microservice APIs
│   ├── views                 # View components for the application
│   │   └── ChatView.vue      # Main interface for the chat application
│   ├── router                # Routing configuration
│   │   └── index.ts          # Defines routes and components
│   ├── store                 # Vuex store for state management
│   │   └── index.ts          # Manages chat sessions and messages
│   ├── App.vue               # Root component of the application
│   └── main.ts               # Entry point of the application
├── public
│   └── favicon.ico           # Favicon for the application
├── index.html                # Main HTML file
├── package.json              # npm configuration file
├── tsconfig.json             # TypeScript configuration file
└── vite.config.ts            # Vite configuration file
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   ```

2. Navigate to the project directory:
   ```
   cd vue-chat-frontend
   ```

3. Install dependencies:
   ```
   npm install
   ```

4. Run the development server:
   ```
   npm run dev
   ```

## Usage

- Open your browser and navigate to `http://localhost:3000` (or the port specified in your terminal).
- Enter your API key in the provided input field.
- Create or select a conversation to start chatting.

## License

This project is licensed under the MIT License.