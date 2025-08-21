# Vue Chat Frontend

This project is a chat application built with Vue 3, Vite, and Vuetify 3. It allows users to create and manage conversations, send messages, and securely store their API key. The frontend integrates with the FastAPI Chat Storage Microservice backend.

## Features

- Create, rename, and delete conversations
- Mark conversations as favorite
- Send and view messages within conversations
- Date breaks and unread message indicators in message list
- Load more messages (pagination)
- Input field for API key, stored in cookies
- Context menu (three-dot menu) for conversation actions
- Integration with Chat Storage Microservice APIs
- Responsive and compact view support
- Snackbar notifications for actions and errors

## Project Structure

```
frontend/
├── src
│   ├── components            # Vue components for the application
│   │   ├── ChatInput.vue
│   │   ├── ConversationList.vue
│   │   ├── MessageList.vue
│   │   ├── ApiKeyInput.vue
│   ├── composables           # Composable functions for state management
│   │   ├── useApiKey.ts
│   │   ├── useChat.ts        # Handles chat session/message logic
│   ├── views
│   │   └── ChatView.vue
│   ├── router
│   │   └── index.ts
│   ├── store                 # Pinia stores for state management
│   │   └── index.ts
│   ├── App.vue
│   └── main.ts
├── public
│   └── favicon.ico
├── index.html
├── package.json
├── tsconfig.json
└── vite.config.ts
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   ```

2. Navigate to the frontend directory:
   ```
   cd frontend
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

- Open your browser and navigate to `http://localhost:3000` (or the port shown in your terminal).
- Enter your API key in the input field (stored in cookies).
- Create, select, rename, favorite, or delete conversations using the sidebar.
- Send and view messages in the selected conversation.
- Use the "Load More" button to fetch older messages.
- Unread messages and date breaks are visually indicated in the message list.

## License

This project is licensed