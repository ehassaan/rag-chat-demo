<template>
  <div class="chat-input">
    <v-text-field :loading="loadingSend" :disabled="loadingSend" hide-details="auto" v-model="model"
      label="Type your message" @keyup.enter="() => emit('send', model)" outlined>
      <template #append-inner>
        <v-btn size="x-small" icon="$mdiAttachment" :loading="loadingAttach" @click="open_file_picker"></v-btn>
      </template>
    </v-text-field>
    <v-btn :loading="loadingSend" size="small" @click="() => model.length > 0 ? emit('send', model) : null"
      color="primary" icon="$mdiSend"></v-btn>

    <input ref="fileInput" type="file" style="display: none" @change="handle_file_change" />
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue';


const props = defineProps({
  loadingSend: {
    type: Boolean,
    default: false
  },
  loadingAttach: {
    type: Boolean,
    default: false
  },
  attachment: {
    type: String,
    default: null
  }
});
const model = defineModel<string>({ default: '' });

const emit = defineEmits(['send', 'document-opened']);
const fileInput = ref<HTMLInputElement | null>(null);

function open_file_picker() {
  if (fileInput.value) {
    fileInput.value.click();
  }
}

async function handle_file_change(event: Event) {
  const file = (event.target as HTMLInputElement).files?.[0];
  if (file) {
    const text = await file.text();
    console.log("Document: ", file, text);
    emit('document-opened', { name: file.name, content: text });
  }
}

</script>

<style scoped>
.chat-input {
  display: flex;
  align-items: center;
  gap: 6px;
}
</style>