import 'vuetify/styles';
import { createApp } from 'vue';
import App from './App.vue';
import router from './router';

// Vuetify
import { createVuetify } from 'vuetify';
import * as components from 'vuetify/components';
import * as directives from 'vuetify/directives';
import { mdi } from 'vuetify/iconsets/mdi-svg';
import { mdiMessageOutline, mdiPencil, mdiDelete, mdiPlus, mdiSend, mdiDotsVertical, mdiStar } from '@mdi/js';


const vuetify = createVuetify({
  components,
  directives,
  icons: {
    defaultSet: 'mdi',
    aliases: {
      mdiMessage: mdiMessageOutline,
      mdiEdit: mdiPencil,
      mdiDelete,
      mdiPlus,
      mdiSend,
      mdiFavorite: mdiStar,
      mdiDotsVertical: mdiDotsVertical,
    },
    sets: {
      mdi
    },
  },
  theme: {
    defaultTheme: 'light',
  }
});

createApp(App)
  .use(router)
  .use(vuetify)
  .mount('#app');