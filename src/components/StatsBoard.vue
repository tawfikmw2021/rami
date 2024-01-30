<template>
  <div>
    <button @click="getGames">get games</button>
    <div class="border" v-for="game in games" :key="game.uid">
      <div>{{ game.uid }}</div>
      <div class="row">
        <div class="col-2" v-for="player in game.players" :key="player.uid">
          {{ player.name || player.uid }}
        </div>
      </div>
      <div class="border" v-for="round in game.rounds" :key="round.uid">
        <div>{{ game.uid }}</div>
        <div class="row">
          <div class="col-2" v-for="player in game.players" :key="player.uid">
            {{ getScore(player, round.players, round.scores) }}
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { ax } from "./api";

export default {
  name: "StatsBoard",
  components: {},
  data: function () {
    return {
      games: [],
    };
  },
  methods: {
    getScore: function (player, players, scores) {
      let index = players.findIndex((v) => v.uid == player.uid);
      if (index > -1) return scores[index];
      else return 0;
    },
    getGames: function () {
      this.games = [];
      ax.get("/api/games").then((res) => {
        this.games = JSON.parse(res.data);
      });
    },
  },
};
</script>

<style scoped></style>
