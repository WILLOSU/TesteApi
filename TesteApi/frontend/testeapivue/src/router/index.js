import { createRouter, createWebHistory } from 'vue-router'; // Importando as funções corretas
import HomePage from '@/views/HomePage.vue';

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomePage
  }
];

const router = createRouter({
  history: createWebHistory(), // Usando o createWebHistory para o modo de navegação com URLs "limpas"
  routes // A lista de rotas
});

export default router;
