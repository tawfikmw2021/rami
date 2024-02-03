<template>
  <div>
    <button @click="getGames">get games</button>
    <button v-if="key == 'enable'" @click="newGame">new game</button>
    <button v-if="key == 'enable'" @click="newRound">new Round</button>

    <input v-model="key" placeholder="key" />

    <div
      :class="{ focus: focus(game) }"
      class="border m-2 p-2"
      v-for="game in games"
      :key="game.uid"
    >
      <div class="uid">{{ game.time }}</div>
      <a href="javascript:void(0)" @click="joinGame(game.uid)">{{
        game.uid
      }}</a>
      <div
        class="gameb"
        :style="{
          'grid-template-columns':
            'repeat(' + (game.players.length + 1) + ',1fr)',
          'grid-template-rows': 'repeat(' + (game.rounds.length + 1) + ',1fr)',
        }"
      >
        <div
          v-for="(player, index) in game.players"
          :key="player.uid"
          :class="{ focusu: focusu(player) }"
          :style="{
            'grid-row': 1,
            'grid-column': index + 2,
          }"
        >
          {{ player.name || player.uid }}
        </div>
        <template v-for="(round, index) in game.rounds" :key="round.uid">
          <div
            :class="{ focusr: focusr(round) }"
            :style="{
              'grid-row': index + 2,
              'grid-column': 1,
            }"
            class="uid"
          >
            <a
              :title="round.uid"
              href="javascript:void(0)"
              @click="joinRound(game.uid, round.uid)"
              >{{ round.uid }}</a
            >
          </div>
          <div
            :style="{
              'grid-row': index + 2,
              'grid-column': pindex + 2,
            }"
            v-for="(player, pindex) in game.players"
            :key="player.uid"
            :class="{ focusu: focusu(player) }"
          >
            {{ getScore(player, round.players, round.scores) }}
          </div>
        </template>
      </div>
    </div>
  </div>
</template>

<script>
import { ax, fireEvent, saveContext, context, subscribeToEvent } from "./api";

export default {
  name: "StatsBoard",
  components: {},
  emits: ["join"],
  data: function () {
    return {
      games: [],
      key: "",
    };
  },
  created: function () {
    //this.getGames();
    subscribeToEvent("context_change", "stats", () => {
      this.getGames();
    });
  },
  methods: {
    focus(game) {
      return game.uid == context["game_uid"];
    },
    focusr(round) {
      return round.uid == context["round_uid"];
    },
    focusu(player) {
      return context["user_uid"] && context["user_uid"].startsWith(player.uid);
    },
    getScore: function (player, players, scores) {
      let index = players.findIndex((v) => v.uid == player.uid);
      if (index > -1) return scores[index] || 0;
      else return "none";
    },
    getGames: function () {
      this.games = [];
      ax.get("/api/games").then((res) => {
        this.games = JSON.parse(res.data);
      });
    },

    newGame() {
      fireEvent("click_game_new");
    },
    newRound() {
      fireEvent("click_round_new");
    },

    joinGame(game_uid) {
      /*context["game_uid"] = game_uid;
      context["user_uid"] = "";
      context["round_uid"] = "";
      console.log(game_uid);
      saveContext();
      fireEvent("click_game_join", [game_uid]);*/
      //this.$emit("join");
    },

    joinRound(game_uid, round_uid) {
      fireEvent("click_round_join", [game_uid, round_uid]);
      this.$emit("join");
    },
  },
};
</script>

<style scoped>
.focus {
  background-color: rgba(150, 50, 0, 0.1);
}

.gameb {
  display: grid;
  grid-template-columns: repeat(8, 1fr);
}

.focusr {
  background-color: rgba(150, 50, 0, 0.2);
}

.focusu {
  background-color: rgba(150, 50, 0, 0.2);
}
.uid {
  overflow: hidden;
  height: 30px;
}
</style>
