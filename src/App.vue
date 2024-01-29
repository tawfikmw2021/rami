<template>
  <GameBoard />
</template>

<script>
import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap/dist/js/bootstrap.min.js";
import "bootstrap";
import GameBoard from "./components/GameBoard.vue";

//<RamiVue style="display: none;" msg="Welcome to Your Vue.js App"/>
//import simpleList from './components/simpleList.vue'

export default {
  name: "App",
  components: {
    GameBoard,
  },
};
</script>

<style></style>
