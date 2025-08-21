<template>
  <v-navigation-drawer app permanent width="300" class="sidebar">
    <v-toolbar flat color="primary" class="sidebar-toolbar">
      <v-toolbar-title class="white--text">Conversations</v-toolbar-title>
    </v-toolbar>
    <v-divider></v-divider>
    <v-list nav dense>
      <v-list-item v-for="session in sessions" :key="session.session_id" :value="session.session_id"
        :active="currentSession === session.session_id" @click="onConversationChange(session.session_id)"
        class="sidebar-list-item">
        <template v-slot:prepend>
          <v-btn :loading="loading.favorite" :color="session.is_favorite ? 'primary' : 'backround'"
            @click="onFavorite(session.session_id, !session.is_favorite)" size="x-small" icon="$mdiFavorite"></v-btn>
        </template>
        <v-list-item-title class="ml-2">{{ session.session_name }}</v-list-item-title>
        <template v-slot:append>
          <!-- <v-list-item-action>
            <v-btn :loading="loading.rename" size="x-small" icon="$mdiEdit"
              @click.stop="() => onRename(session.session_id)">
            </v-btn>
          </v-list-item-action>
          <v-list-item-action>
            <v-btn size="x-small" :loading="loading.delete" icon="$mdiDelete"
              @click.stop="() => onDelete(session.session_id)">
            </v-btn>
          </v-list-item-action> -->
          <v-list-item-action>
            <v-btn :id="'menu-activator' + session.session_id" size="x-small" :loading="loading.menu" icon="$mdiDotsVertical"></v-btn>
          </v-list-item-action>

          <v-menu :activator="'#menu-activator' + session.session_id">
            <v-list>
              <v-list-item>
                <v-list-item-title @click="onRename(session.session_id)">Rename</v-list-item-title>
              </v-list-item>
              <v-list-item>
                <v-list-item-title @click="onDelete(session.session_id)">Delete</v-list-item-title>
              </v-list-item>
            </v-list>
          </v-menu>
        </template>

      </v-list-item>
    </v-list>
    <template #append>
      <v-btn :loading="loading.create" @click="onCreateSession" color="primary" class="btn-new-chat">
        <v-icon left>$mdiPlus</v-icon>
        New Conversation
      </v-btn>
    </template>
    <v-divider></v-divider>

  </v-navigation-drawer>

  <v-snackbar v-model="snackbar" multi-line>
    {{ message }}
    <template v-slot:actions>
      <v-btn color="red" variant="text" @click="snackbar = false">
        Close
      </v-btn>
    </template>
  </v-snackbar>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue';
import { useChat } from '../composables/useChat';

const emit = defineEmits(['selectionChanged']);
const { sessions, fetchSessions, patchSession, deleteSession, createSession } = useChat();

const currentSession = ref<string | null>(null);
const loading = ref({
  menu: false,
  create: false,
  favorite: false
});

const snackbar = ref(false);
const message = ref('');

const onConversationChange = (sessionId: string) => {
  currentSession.value = sessionId;
  emit('selectionChanged', sessionId);
};

const onRename = async (sessionId: string) => {
  try {
    loading.value.menu = true;
    const session = sessions.value.find(s => s.session_id === sessionId);
    if (session) {
      const newName = prompt('Enter new name for the conversation:', session.session_name);
      if (newName && newName.trim()) {
        await patchSession(sessionId, { session_name: newName.trim() });
        await fetchSessions();
      }
    }
  }
  catch (error) {
    console.error('Error renaming session:', error);
    message.value = 'Error renaming session: ' + error.message;
    snackbar.value = true;
  }
  finally {
    loading.value.menu = false;
  }
};

async function onDelete(sessionId: string) {
  try {
    loading.value.menu = true;
    await deleteSession(sessionId);
    if (currentSession.value === sessionId) {
      currentSession.value = sessions.value.length > 0 ? sessions.value[0].session_id : null;
      emit('selectionChanged', currentSession.value);
    }
    await fetchSessions();
  }
  catch (error) {
    console.error('Error deleting session:', error);
    message.value = 'Error deleting session: ' + error.message;
    snackbar.value = true;
  }
  finally {
    loading.value.menu = false;
  }
}

async function onFavorite(sessionId: string, isFavorite: boolean) {
  try {
    loading.value.favorite = true;
    const session = sessions.value.find(s => s.session_id === sessionId);
    if (session) {
      await patchSession(sessionId, { is_favorite: isFavorite });
      await fetchSessions();
    }
  }
  catch (error) {
    console.error('Error updating favorite status:', error);
    message.value = 'Error updating favorite status: ' + error.message;
    snackbar.value = true;
  }
  finally {
    loading.value.favorite = false;
  }
}

async function onCreateSession() {
  try {
    loading.value.create = true;
    const sessionName = prompt('Enter a name for the new conversation:');
    if (sessionName && sessionName.trim()) {
      await createSession(sessionName.trim());
      await fetchSessions();
      currentSession.value = sessions.value[sessions.value.length - 1].session_id;
      emit('selectionChanged', currentSession.value);
    }
  }
  catch (error) {
    console.error('Error creating session:', error);
    message.value = 'Error creating session: ' + error.message;
    snackbar.value = true;
  }
  finally {
    loading.value.create = false;
  }

}

onMounted(async () => {
  try {
    await fetchSessions();
    if (sessions.value.length > 0) {
      currentSession.value = sessions.value[0].session_id;
      emit('selectionChanged', currentSession.value);
    }
  }
  catch (error) {
    console.error('Error fetching sessions:', error);
    message.value = 'Error fetching sessions: ' + error.message;
    snackbar.value = true;
  }
});
</script>

<style scoped>
.sidebar {
  min-height: 100vh;
  box-shadow: 2px 0 8px rgba(0, 0, 0, 0.08);
}

.sidebar-toolbar {
  padding-left: 16px;
}

.sidebar-list-item {
  cursor: pointer;
  transition: background 0.2s;
}

.sidebar-list-item.v-list-item--active {
  background: rgba(255, 255, 255, 0.08);
}

.btn-new-chat {
  width: 100%;
  margin: 10px;
  width: calc(100% - 20px);
}
</style>