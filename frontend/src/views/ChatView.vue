<template>
  <div class="chat-view">
    <ConversationList @selectionChanged="onSessionChanged" />
    <v-main class="main">
      <ApiKeyInput />
      <MessageList class="message-list" :messages="messages" v-if="currentSessionId" />
      <ChatInput class="message-input" @send="sendMessage" v-model="vmMessage" :loading="loading.send" />
    </v-main>

    <!-- toast notification for error -->
    <v-snackbar v-model="snackbar" multi-line>
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
  fetch: false
});

const chat = useChat();
const vmMessage = ref('');
const message = ref<string | null>(null);
const snackbar = ref(false);


async function onSessionChanged(id: string) {
  console.log('Selected session ID:', id);
  currentSessionId.value = id;
  try {
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
  margin: 15px;
}

.message-list {
  flex: 1;
  overflow-y: auto;
  margin-bottom: 15px;
}

.message-input {
  margin-bottom: 15px;
}
</style>