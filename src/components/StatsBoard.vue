<template>
  <div>
    <button @click="getGames">get games</button>
    <div class="border m-2 p-2" v-for="game in games" :key="game.uid">
      <div class="uid">{{ game.uid }}</div>
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
          :style="{
            'grid-row': 1,
            'grid-column': index + 2,
          }"
        >
          {{ player.name || player.uid }}
        </div>
        <template v-for="(round, index) in game.rounds" :key="round.uid">
          <div
            :style="{
              'grid-row': index + 2,
              'grid-column': 1,
            }"
            class="uid"
          >
            {{ round.uid }}
          </div>
          <div
            :style="{
              'grid-row': index + 2,
              'grid-column': pindex + 2,
            }"
            v-for="(player, pindex) in game.players"
            :key="player.uid"
          >
            {{ getScore(player, round.players, round.scores) }}
          </div>
        </template>
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
  created: function () {
    this.getGames();
  },
  methods: {
    getScore: function (player, players, scores) {
      let index = players.findIndex((v) => v.uid == player.uid);
      if (index > -1) return scores[index] || 0;
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

<style scoped>
.gameb {
  display: grid;
  grid-template-columns: repeat(8, 1fr);
}

.uid {
  overflow: hidden;
  height: 30px;
}
</style>
