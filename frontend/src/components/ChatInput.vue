<template>
  <div class="chat-input">
    <v-text-field :loading="loading" v-model="model" label="Type your message" @keyup.enter="() => emit('send', model)"
      outlined></v-text-field>
    <v-btn :loading="loading" :disabled="model.length === 0" size="small" @click="() => emit('send', model)"
      color="primary" icon="$mdiSend"></v-btn>
  </div>
</template>

<script setup lang="ts">

const props = defineProps({
  loading: {
    type: Boolean,
    default: false
  }
});
const model = defineModel<string>({ default: '' });

const emit = defineEmits(['send']);

</script>

<style scoped>
.chat-input {
  display: flex;
  align-items: center;
  gap: 10px;
}
</style>