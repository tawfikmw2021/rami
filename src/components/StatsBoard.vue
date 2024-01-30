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
            {{ (round.players.find((v) => v.uid == player.uid) || {}).uid }}
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
