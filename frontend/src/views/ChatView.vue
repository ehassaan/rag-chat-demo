<template>
  <div class="chat-view">
    <v-app-bar color="primary">
      <v-app-bar-nav-icon variant="text"></v-app-bar-nav-icon>
      <v-toolbar-title>DGE RAG</v-toolbar-title>
      <template #append>
        <ApiKeyInput />
      </template>

      <v-btn icon="mdi-dots-vertical" variant="text"></v-btn>
    </v-app-bar>

    <ConversationList @selectionChanged="onSessionChanged" />
    <v-main class="main">
      <MessageList class="message-list" :messages="messages" />
      <ChatInput class="message-input" @send="sendMessage" @document-opened="onDocumentOpened" v-model="vmMessage"
        :loading-send="loading.send" :loading-attach="loading.attach" />
    </v-main>

    <!-- toast notification for error -->
    <v-snackbar v-model="snackbar" multi-line timeout="6000">
      {{ message }}
      <template v-slot:actions>
        <v-btn color="red" variant="text" @click="snackbar = false">
          Close
        </v-btn>
      </template>
    </v-snackbar>
  </div>
</template>

<script setup lang="ts">
import ApiKeyInput from '@/components/ApiKeyInput.vue';
import ConversationList from '@/components/ConversationList.vue';
import MessageList from '@/components/MessageList.vue';
import ChatInput from '@/components/ChatInput.vue';
import { ref, watch } from 'vue';
import { useChat } from '@/composables/useChat';

const currentSessionId = ref<string | null>(null);
const messages = ref([]);
const loading = ref({
  send: false,
  fetch: false,
  attach: false
});

const chat = useChat();
const vmMessage = ref('');
const message = ref<string | null>(null);
const snackbar = ref(false);


async function onSessionChanged(id: string) {
  console.log('Selected session ID:', id);
  currentSessionId.value = id;
  try {
    messages.value = [];
    messages.value = await chat.fetchMessages(id);
  }
  catch (error) {
    console.error('Error fetching messages:', error);
    message.value = 'Error fetching messages: ' + error.message;
    snackbar.value = true;
  }
}

const sendMessage = async (message: string) => {
  try {
    loading.value.send = true;
    if (message.trim() && currentSessionId.value) {
      console.log('Sending message:', message);
      await chat.sendMessage(currentSessionId.value, message);
      const chunks = await chat.getSimilarChunks(message, currentSessionId.value);
      console.log('Similar chunks:', chunks);
      const prompt = `
        Query: ${message}
        Context: ${chunks.map(c => c.chunk_text).join('\n')}
      `;
      console.log("Using Prompt: ", prompt);
      const res = await chat.generateResponse(prompt, currentSessionId.value);
      console.log("Generation Response: ", res);
      vmMessage.value = '';
      messages.value = await chat.fetchMessages(currentSessionId.value); // Refresh messages
    }
  }
  catch (error) {
    console.error('Error sending message:', error);
    message.value = 'Error: ' + error.message;
    snackbar.value = true;
  }
  finally {
    loading.value.send = false;
  }
};

async function onDocumentOpened(doc: any) {
  if (!currentSessionId.value) {
    return;
  }
  try {
    loading.value.attach = true;
    const res = await chat.indexDocument(doc.name, doc.content, currentSessionId.value);
  }
  catch (error: any) {
    console.error('Error sending message:', error);
    message.value = 'Error: ' + error.message;
    snackbar.value = true;
  }
  finally {
    loading.value.attach = false;
  }
}

</script>

<style scoped>
.chat-view {
  display: flex;
  flex-direction: column;
  height: 100vh;
}

.main {
  display: flex;
  flex-direction: column;
  /* margin: 15px 20%; */
}

.message-list {
  flex: 1;
  overflow-y: auto;
  margin: 15px 20px;
}

.message-input {
  margin: 15px 15px;
}
</style>