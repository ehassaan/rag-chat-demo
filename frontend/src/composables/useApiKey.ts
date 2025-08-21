import { ref } from 'vue';
import Cookies from 'js-cookie';

export function useApiKey() {
  const apiKey = ref<string>(Cookies.get('apiKey') || '');

  const setApiKey = (key: string) => {
    apiKey.value = key;
    Cookies.set('apiKey', key, { expires: 7 }); // Store for 7 days
  };

  const clearApiKey = () => {
    apiKey.value = '';
    Cookies.remove('apiKey');
  };

  return {
    apiKey,
    setApiKey,
    clearApiKey,
  };
}