import { createApp } from 'vue'; // Importa createApp ao invés de Vue
import App from './App.vue';
import router from './router'; // Importa o roteador

// Cria o aplicativo e monta no #app
createApp(App)
  .use(router) // Usa o roteador
  .mount('#app'); // Monta no elemento com id "app"
