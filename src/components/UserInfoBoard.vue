<script>
import { context, ax } from "./api";
export default {
  name: "userInfo",
  data: function () {
    return {
      np_players: 4,
      game_uid: context["game_uid"],
      user_uid: context["user_uid"],
      order: context["porder"],
      currentround: context["round_uid"],
    };
  },
  methods: {
    usernameChange: function () {
      ax.get(
        `/game/${this.game_uid}/${this.user_uid}/name?name=${this.user_name}`
      );
    },
  },
};
</script>

<template>
  <div class="d-flex flex-column">
    <div class="d-flex border-top border-bottom">
      <div class="imp col-md-6 col-6 px-1">api url</div>
      <input
        class="imp col-md-6 col-6 px-1"
        title="api url"
        v-model="api_url"
        @change="urlchange"
      />
    </div>

    <div class="d-flex border-bottom">
      <div class="imp col-md-6 col-6 px-1">game uid</div>
      <input
        class="imp col-md-6 col-6 px-1"
        title="game_uid"
        v-model="game_uid"
      />
    </div>

    <div class="d-flex border-bottom">
      <div class="imp col-md-6 col-6 px-1">round uid</div>
      <input
        class="imp col-md-6 col-6 px-1"
        title="user_uid"
        v-model="currentround"
      />
    </div>

    <div class="d-flex border-bottom">
      <div class="imp col-md-6 col-6 px-1">user uid</div>
      <input
        class="imp col-md-6 col-6 px-1"
        title="user_uid"
        v-model="user_uid"
      />
    </div>

    <div class="d-flex border-bottom">
      <div class="imp col-md-6 col-6 px-1">name</div>

      <input
        class="imp col-md-6 col-6 px-1"
        title="user_name"
        v-model="user_name"
        @change="usernameChange"
      />
    </div>

    <div class="d-flex border-bottom">
      <div class="imp col-md-6 col-6 px-1">order</div>
      <input
        class="imp col-md-6 col-6 px-1"
        title="porder"
        v-model="order"
        @change="orderChange"
      />
    </div>

    <div class="d-flex border-bottom">
      <div class="imp col-md-6 col-6 px-1">nb playeres</div>
      <input
        class="imp col-md-6 col-6 px-1"
        title="nb players"
        v-model="np_players"
      />
    </div>
  </div>
</template>

<style scoped>
.imp {
  border-left: solid 1px;
}
</style>
