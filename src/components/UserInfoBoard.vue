<script>
import { context, ax, subscribeToEvent, saveContext } from "./api";

export default {
  name: "userInfo",
  data: function () {
    return {
      np_players: 4,
      game_uid: context["game_uid"],
      user_uid: context["user_uid"],
      order: context["porder"],
      user_name: context["user_name"],
      currentround: context["round_uid"],
    };
  },
  created: function () {
    console.log("click_game_join3");
    this.getUser();

    subscribeToEvent("context_change", "uirefresh", () => {
      this.refresh();
    });
  },
  methods: {
    usernameChange: function () {
      context["user_name"] = this.user_name;
      saveContext("context_change");
      ax.get(
        `/game/${this.game_uid}/${this.user_uid}/name?name=${this.user_name}`
      );
    },

    refresh: function () {
      this.user_uid = context["user_uid"];
      this.game_uid = context["game_uid"];
      this.currentround = context["round_uid"];
      console.log("refresh", this.game_uid, this.currentround, this.user_uid);
    },

    getUser: function () {
      ax.get(`/game/${this.game_uid}/${this.user_uid}`).then((v) => {
        this.user_name = this.user_name || v.data;
        context["user_name"] = this.user_name;
        saveContext("context_change");
      });
    },
  },
};
</script>

<template>
  <button @click="refresh">refresh</button>
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
