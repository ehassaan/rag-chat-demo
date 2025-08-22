<template>
  <v-list class="message-list">
    <v-list-item elevation="1" v-for="message in messages.toReversed()" :key="message.id"
      :class="message.role === 'user' ? 'message user-message' : 'message assistant-message'" class="mb-2">      
      <template #prepend>
        <v-avatar size="32" :color="message.role === 'user' ? 'secondary' : 'primary'">
          <v-icon>
            {{ message.role === 'assistant' ? '$mdiRobot' : '$mdiAccount' }}
          </v-icon>
        </v-avatar>
      </template>
      <div>
        <v-list-item-title class="font-weight-bold">
          {{ message.role === 'assistant' ? 'Assistant' : 'You' }}
          <span class="message-time">{{ message.created_at }}</span>
        </v-list-item-title>
        <v-list-item-subtitle class="message-content">
          {{ message.content }}
        </v-list-item-subtitle>
      </div>
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
  display: flex;
  flex-direction: column;
  justify-content: flex-end;
}

.message {
  border-radius: 8px;
  padding: 10px 10px !important;
  margin-top: 10px;
  width: 60%;
}

.user-message {
  background-color: rgb(var(--v-theme-secondary));
  align-self: flex-end;
}

.assistant-message {
  align-self: flex-start;
}

.message-content {
  font-size: 1.1rem;
  margin-top: 5px;
  white-space: pre-line;
}

.message-time {
  font-size: 0.8rem;
  margin-left: 8px;
  font-weight: 100;
}
</style>