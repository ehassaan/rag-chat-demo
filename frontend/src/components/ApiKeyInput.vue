<template>
  <div class="api-key-input">
    <v-text-field class="text-field" density="compact" hide-details="auto" v-model="apiKey" label="Enter your API Key" outlined v-if="!isSaved" type="password" />
    <v-btn @click="saveApiKey" variant="flat" color="contrast" size="small" :icon="isSaved ? '$mdiLogout' : '$mdiSave'"></v-btn>
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
  window.location.reload();
};
</script>

<style scoped>
.api-key-input {
  display: flex;
  align-items: center;
  /* justify-content: right; */
  flex-direction: row;
  margin-left: auto;
  padding: 5px;
}

.api-key-input .text-field {
  width: 300px;
  margin-right: 5px;
}
</style>