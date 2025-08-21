<template>
  <v-list class="message-list">
    <v-list-item elevation="2" v-for="message in messages.toReversed()" :key="message.id"
      :class="message.sender === 'user' ? 'user-message' : 'assistant-message'" class="mb-2">      
      <template #prepend>
        <v-avatar size="32" :color="message.sender === 'user' ? 'secondary' : 'primary'">
          <v-icon>
            {{ message.sender === 'assistant' ? 'mdi-robot' : 'mdi-account' }}
          </v-icon>
        </v-avatar>
      </template>
      <v-list-item-content>
        <v-list-item-title class="font-weight-bold">
          {{ message.sender === 'assistant' ? 'Assistant' : 'You' }}
          <span class="message-time">{{ message.timestamp }}</span>
        </v-list-item-title>
        <v-list-item-subtitle class="message-content">
          {{ message.content }}
        </v-list-item-subtitle>
      </v-list-item-content>
    </v-list-item>
  </v-list>
</template>

<script setup lang="ts">
const props = defineProps({
  messages: {
    type: Array,
    default: () => []
  }
});
</script>

<style scoped>
.message-list {
  /* height: 560px; */
  /* border-radius: 12px; */
  /* overflow-y: auto; */
  /* color: #222; */
}

.user-message {
  border-radius: 8px;
  padding: 8px 16px;
}

.assistant-message {
  border-radius: 8px;
  padding: 8px 16px;
}

.message-content {
  font-size: 1.05rem;
  margin-top: 2px;
  white-space: pre-line;
}

.message-time {
  font-size: 0.8rem;
  color: #888;
  margin-left: 8px;
  font-weight: normal;
}
</style>