<template>
  <simpleList v-if="true" />
</template>
//
<jeuRami v-if="false" />
<script>
import simpleList from "./simpleList.vue";
import jeuRami from "./jeuRami.vue";
export default {
  name: "RamiVue",
  components: {
    //RamiVue,
    simpleList,
    //jeuRami,
  },
  data: function () {},
  methods: {},
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped></style>
