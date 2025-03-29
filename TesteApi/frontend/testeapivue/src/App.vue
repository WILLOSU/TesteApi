<template>
  <div id="app">
    <HomePage />
  </div>
</template>

<script>
import HomePage from './views/HomePage.vue';

export default {
  name: 'App',
  components: {
    HomePage
  }
};
</script>

<style>
/* Estilos gerais do aplicativo */
#app {
  font-family: Arial, sans-serif;
  background-color: #fafafa;
  padding: 20px;
}
</style>
