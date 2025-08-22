import 'vuetify/styles';
import { createApp } from 'vue';
import App from './App.vue';
import router from './router';

// Vuetify
import { createVuetify } from 'vuetify';
import * as components from 'vuetify/components';
import * as directives from 'vuetify/directives';
import { mdi } from 'vuetify/iconsets/mdi-svg';
import { mdiMessageOutline, mdiPencil, mdiDelete, mdiAccount, mdiRobot, mdiPlus, mdiSend,
  mdiDotsVertical, mdiStar, mdiFloppy, mdiLogout, mdiAttachment } from '@mdi/js';


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
      mdiSave: mdiFloppy,
      mdiLogout: mdiLogout,
      mdiDotsVertical: mdiDotsVertical,
      mdiRobot,
      mdiAccount,
      mdiAttachment
    },
    sets: {
      mdi
    },
  },
  theme: {
    defaultTheme: 'theme1',
    themes: {
      theme1: {
        dark: false,
        colors: {
          primary: '#1e1e1e',
          secondary: '#d5c8be',
          accent: '#d5c8be',
          error: '#E53935',
          info: '#d5c8be',
          success: '#43A047',
          warning: '#FDD835',
        }
      }
    }
  }
});

createApp(App)
  .use(router)
  .use(vuetify)
  .mount('#app');