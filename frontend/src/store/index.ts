import { createStore } from 'vuex';

export default createStore({
  state: {
    conversations: [],
    selectedConversationId: null,
    apiKey: null,
  },
  mutations: {
    setConversations(state, conversations) {
      state.conversations = conversations;
    },
    addConversation(state, conversation) {
      state.conversations.push(conversation);
    },
    renameConversation(state, { id, newName }) {
      const conversation = state.conversations.find(conv => conv.id === id);
      if (conversation) {
        conversation.name = newName;
      }
    },
    selectConversation(state, id) {
      state.selectedConversationId = id;
    },
    setApiKey(state, apiKey) {
      state.apiKey = apiKey;
    },
  },
  actions: {
    fetchConversations({ commit }) {
      // Logic to fetch conversations from the API
    },
    createConversation({ commit }, conversation) {
      // Logic to create a new conversation via the API
      commit('addConversation', conversation);
    },
    updateConversationName({ commit }, payload) {
      commit('renameConversation', payload);
    },
    selectConversation({ commit }, id) {
      commit('selectConversation', id);
    },
    saveApiKey({ commit }, apiKey) {
      commit('setApiKey', apiKey);
      // Logic to store API key in cookies
    },
  },
  getters: {
    conversations: state => state.conversations,
    selectedConversation: state => state.conversations.find(conv => conv.id === state.selectedConversationId),
    apiKey: state => state.apiKey,
  },
});