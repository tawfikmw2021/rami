<script>
import GameBoard from "./GameBoard.vue";
import StatsBoard from "./StatsBoard.vue";
import UserInfoBoard from "./UserInfoBoard.vue";
import { context, saveContext } from "./api";

export default {
  name: "mainBoard",
  data: function () {
    return {
      focus: localStorage.getItem("selectedtab") || "stats",
    };
  },
  methods: {
    focusChanged: function (n) {
      this.focus = n;
      localStorage.setItem("selectedtab", n);
    },
  },
  components: { StatsBoard, GameBoard, UserInfoBoard },
};
</script>

<template>
  <div class="d-flex header m-0">
    <div
      class="entry border col-2"
      :class="{ focus: focus == 'stats' }"
      @click="focusChanged('stats')"
    >
      stats
    </div>

    <div
      class="entry border col-2"
      :class="{ focus: focus == 'info' }"
      @click="focusChanged('info')"
    >
      info
    </div>

    <div
      class="entry border col-2"
      :class="{ focus: focus == 'game' }"
      @click="focusChanged('game')"
    >
      game
    </div>

    <div class="entry border last flex-grow-1"></div>
  </div>
  <div class="content" :class="{ focus: focus == 'stats' }">
    <StatsBoard @join="focus = 'game'" />
  </div>
  <div class="content" :class="{ focus: focus == 'info' }">
    <UserInfoBoard />
  </div>
  <div class="content" :class="{ focus: focus == 'game' }">
    <GameBoard />
  </div>
</template>

<style scoped>
.header {
  height: 30px;
}

.header .entry {
  text-align: center;
  /*z-index: 10;*/
  border-right: none !important;
  /*background-color: white;*/
  cursor: pointer;
}

.header .entry.last {
  z-index: 10;
  border-top: none !important;
}

.header .entry.focus {
  border-bottom: none !important;
  /*border: antiquewhite;*/
  color: blue;
}
.content {
  /*height: calc(100vh - 20px);*/
  display: none;
}

.content.focus {
  display: initial;
}
</style>
