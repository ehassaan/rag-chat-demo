<template>
  <div>
    <v-text-field v-model="apiKey" label="Enter your API Key" outlined v-if="!isSaved"
      type="password" />
    <v-btn @click="saveApiKey" color="primary">{{ isSaved ? 'Clear API Key' : 'Save' }}</v-btn>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import { useApiKey } from '../composables/useApiKey';

const key = useApiKey();
const apiKey = ref<string>(key.apiKey.value);
const isSaved = ref(apiKey.value !== '' && apiKey.value);

function saveApiKey() {
  if (isSaved.value) {
    key.clearApiKey();
    isSaved.value = false;
    apiKey.value = '';
  }
  else {
    key.setApiKey(apiKey.value);
    isSaved.value = true;
  }
};
</script>

<style scoped></style>