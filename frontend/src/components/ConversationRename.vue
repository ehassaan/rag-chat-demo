<template>
  <v-dialog v-model="dialog" max-width="290">
    <v-card>
      <v-card-title>
        <span class="headline">Rename Conversation</span>
      </v-card-title>
      <v-card-text>
        <v-text-field
          v-model="newName"
          label="New Conversation Name"
          outlined
        ></v-text-field>
      </v-card-text>
      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn color="primary" @click="renameConversation">Rename</v-btn>
        <v-btn @click="closeDialog">Cancel</v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import { useChat } from '../composables/useChat';

const props = defineProps({
  conversationId: {
    type: String,
    required: true,
  },
  currentName: {
    type: String,
    required: true,
  },
});

const { patchSession: renameConversation } = useChat();
const dialog = ref(false);
const newName = ref(props.currentName);

const closeDialog = () => {
  dialog.value = false;
};

const openDialog = () => {
  newName.value = props.currentName;
  dialog.value = true;
};

const handleRename = () => {
  renameConversation(props.conversationId, newName.value).then(() => {
    closeDialog();
  });
};

</script>

<style scoped>
</style>