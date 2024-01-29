<template>
  <RamiVue msg="Welcome to Your Vue.js App" />
  <RouterView2 />
</template>

<script>
import { RouterLink } from "vue-router";

import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap/dist/js/bootstrap.min.js";
import "bootstrap";
import RamiVue from "./components/RamiVue.vue";

//<RamiVue style="display: none;" msg="Welcome to Your Vue.js App"/>
//import simpleList from './components/simpleList.vue'

export default {
  name: "App",
  components: {
    RamiVue,
    //RouterView,
    //,
    //simpleList
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 0px;
}
</style>
