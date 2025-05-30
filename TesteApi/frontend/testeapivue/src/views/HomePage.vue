<template>
  <div class="home-page">
    <h1>Intuitive Care</h1>
    
    <!-- Campo de pesquisa com ícone -->
    <div class="input-container">
      <i class="fa fa-search"></i>
      <input v-model="termoBusca" @input="buscar" placeholder="Digite um termo" />
    </div>
    
    <!-- Indicador de carregamento -->
    <div v-if="carregando">Carregando...</div>

    <!-- Exibição de erro -->
    <div v-if="erroMensagem" class="erro">{{ erroMensagem }}</div>
    
    <!-- Exibição dos resultados -->
    <ul v-if="resultados.length">
      <li v-for="item in resultados" :key="item.CNPJ">
        <strong>{{ item.Nome_Fantasia }}</strong>
        <br />
        CNPJ: {{ item.CNPJ }}
      </li>
    </ul>

    <!-- Caso não haja resultados ou erro -->
    <div v-if="!carregando && !erroMensagem && !resultados.length">
      Nenhum resultado encontrado.
    </div>
  </div>
</template>


<script>
export default {
  name: 'HomePage',
  data() {
    return {
      termoBusca: '',
      resultados: [],
      carregando: false,  // Estado de carregamento
      erroMensagem: '',   // Mensagem de erro
    };
  },
  methods: {
    async buscar() {
      // Verifica se o termo é muito curto ou vazio
      if (this.termoBusca.trim() === '' || this.termoBusca.length < 3) {
        this.resultados = [];
        return;
      }

      // Inicia o carregamento e limpa erro
      this.carregando = true;
      this.erroMensagem = '';  // Limpa a mensagem de erro

      try {
        // Requisição para a API usando a URL configurada na variável de ambiente
        const resposta = await fetch(`http://127.0.0.1:5000/buscar?termo=${this.termoBusca}`);
        const data = await resposta.json();

        console.log('Resposta da API:', data);  // Verifique os dados retornados pela API

        // Verifique se os dados são um array não vazio
        if (Array.isArray(data) && data.length > 0) {
          // Limita a 10 itens
          this.resultados = data.slice(0, 10);
        } else {
          // Caso não haja dados
          this.resultados = [];
        }
      } catch (erro) {
        console.error('Erro ao buscar:', erro);
        this.erroMensagem = 'Ocorreu um erro. Tente novamente mais tarde.'; // Exibe mensagem de erro
      } finally {
        // Finaliza o carregamento
        this.carregando = false;
      }
    }
  }
};
</script>


<style scoped>
.home-page {
  text-align: center;
}

.input-container {
  position: relative;
  display: inline-block;
}

input {
  padding: 10px 10px 10px 30px; /* Adiciona espaçamento à esquerda para a lupa */
  font-size: 16px;
  margin: 10px;
  width: 100%;  /* Faz o campo de entrada ocupar 100% do espaço disponível */
  max-width: 300px;  /* Limita a largura máxima do input para 300px */
  border-radius: 5px;
  border: 1px solid #ccc;
}

input:focus {
  outline: none;
  border-color: #cba4ef;
}

i.fa-search {
  position: absolute;
  left: 10px; /* Posiciona a lupa à esquerda */
  top: 50%;
  transform: translateY(-50%); /* Alinha verticalmente ao centro */
  color: #cba4ef;
  font-size: 18px;
}

ul {
  list-style-type: none;
  padding: 0;
  margin-top: 20px; /* Espaçamento acima da lista */
}

li {
  background-color: #f0f0f0;
  margin: 5px 0;
  padding: 10px;
  border-radius: 5px;
}

.erro {
  color: red;
  font-weight: bold;
}

div {
  margin-top: 10px;
}

/* Responsividade */
@media (max-width: 600px) {
  .input-container {
    width: 100%;
  }

  input {
    width: 100%;  /* Faz o campo de entrada ocupar 100% do espaço disponível */
    max-width: none;  /* Remove a limitação da largura máxima */
  }
}
</style>