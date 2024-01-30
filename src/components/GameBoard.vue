<template>
  <div class="row m-0">
    <div v-if="!hideclickeddash">
      <StatsBoard />
    </div>
    <div class="col-12" style="background-color: rgba(255, 50, 0, 0.2)">
      <div
        class="col-12"
        @click="hideclickeddashChange"
        style="cursor: pointer"
      >
        <div class="hide" :class="{ hideclicked: hideclickeddash }">
          {{ hideclickeddash ? ">" : "<" }}
        </div>
      </div>
    </div>
  </div>
  <div class="row m-0">
    <div v-if="!hideclicked">
      <div class="row m-0" style="">
        <div class="p-0">
          <div class="form-group">
            <div v-if="!hideclickedimps" class="row inputs">
              <div class="imp col-md-6 col-6 px-1">api url</div>

              <input
                class="imp col-md-6 col-6 px-1"
                title="api url"
                v-model="api_url"
                @change="urlchange"
              />

              <div class="imp col-md-6 col-6 px-1">game uid</div>
              <input
                class="imp col-md-6 col-6 px-1"
                title="game_uid"
                v-model="game_uid"
              />

              <div class="imp col-md-6 col-6 px-1">round uid</div>
              <input
                class="imp col-md-6 col-6 px-1"
                title="user_uid"
                v-model="currentround"
              />

              <div class="imp col-md-6 col-6 px-1">user uid</div>
              <input
                class="imp col-md-6 col-6 px-1"
                title="user_uid"
                v-model="user_uid"
              />

              <div class="imp col-md-2 col-6 px-1">name</div>

              <input
                class="imp col-md-2 col-6 px-1"
                title="user_name"
                v-model="user_name"
                @change="usernameChange"
              />

              <div class="imp col-md-2 col-6 px-1">order</div>
              <input
                class="imp col-md-2 col-6 px-1"
                title="porder"
                v-model="currentporder"
                @change="orderChange"
              />

              <div class="imp col-md-2 col-6 px-1">nb playeres</div>
              <input
                class="imp col-md-2 col-6 px-1"
                title="nb players"
                v-model="np_players"
              />
            </div>
            <div class="row" style="background-color: rgba(255, 50, 0, 0.2)">
              <div
                class="col-12"
                @click="hideclickedimpsChange"
                style="cursor: pointer"
              >
                <div class="hide" :class="{ hideclicked: hideclickedimps }">
                  {{ hideclickedimps ? ">" : "<" }}
                </div>
              </div>
            </div>
            <div class="d-flex justify-content-around">
              <div @click="newGame" class="btn-container">
                <img
                  class="btn-img"
                  v-bind:src="
                    require('../assets/cards/SVG-cards-1.3/SVG-cards-1.3/Card_back_01.svg')
                  "
                />
                <span class="img-txt"> new game </span>
              </div>

              <div @click="joinGame" class="btn-container">
                <img
                  class="btn-img"
                  v-bind:src="
                    require('../assets/cards/SVG-cards-1.3/SVG-cards-1.3/Card_back_01.svg')
                  "
                />
                <span class="img-txt"> join game </span>
              </div>

              <div @click="newRound" class="btn-container">
                <img
                  class="btn-img"
                  v-bind:src="
                    require('../assets/cards/SVG-cards-1.3/SVG-cards-1.3/Card_back_01.svg')
                  "
                />
                <span class="img-txt"> new round </span>
              </div>
              <div @click="() => joinRound()" class="btn-container">
                <img
                  class="btn-img"
                  v-bind:src="
                    require('../assets/cards/SVG-cards-1.3/SVG-cards-1.3/Card_back_01.svg')
                  "
                />
                <span class="img-txt"> join round </span>
              </div>
              <div @click="initRound" class="btn-container">
                <img
                  class="btn-img"
                  v-bind:src="
                    require('../assets/cards/SVG-cards-1.3/SVG-cards-1.3/Card_back_01.svg')
                  "
                />
                <span class="img-txt"> init round </span>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div></div>
    </div>
    <div class="col-12" style="background-color: rgba(255, 50, 0, 0.2)">
      <div class="col-12" @click="hideclickedChange" style="cursor: pointer">
        <div class="hide" :class="{ hideclicked: hideclicked }">
          {{ hideclicked ? ">" : "<" }}
        </div>
      </div>
    </div>
  </div>
  <RoundBoard
    :porder="currentporder"
    :user_uid="user_uid"
    :game_uid="game_uid"
    :p_order="currentporder"
    :round_uid="currentround"
    ref="childComponentRef"
  />
</template>
<script>
import RoundBoard from "./RoundBoard.vue";
import StatsBoard from "./StatsBoard.vue";
import { ax } from ".//api.js";
import { ref } from "vue";

let query = document.location.search;
const urlParams = new URLSearchParams(query);

let round_uid = urlParams.get("round_uid");
let porder = urlParams.get("porder");
if (round_uid) localStorage.setItem("round_uid", round_uid);
if (porder) localStorage.setItem("porder", porder);

let game_uid = urlParams.get("game_uid");
let user_uid = urlParams.get("user_uid");
if (game_uid) localStorage.setItem("game_uid", game_uid);
if (user_uid) localStorage.setItem("user_uid", user_uid);

export default {
  name: "GameBoard",
  components: {
    RoundBoard,
    StatsBoard,
  },
  data: function () {
    return {
      hideclicked: localStorage.getItem("hide") == "true",
      hideclickedimps: localStorage.getItem("hide2") == "true",
      hideclickeddash: localStorage.getItem("hidedash") == "true",
      np_players: 4,
      game_uid: localStorage.getItem("game_uid") || "init",
      user_uid: localStorage.getItem("user_uid"),
      currentporder: localStorage.getItem("porder") || "0",
      currentround: localStorage.getItem("round_uid") || "0",
      //currentRound: localStorage.getItem("round_uid") || "0",
    };
  },
  setup() {
    const childComponentRef = ref(null);
    return {
      childComponentRef,
    };
  },
  methods: {
    beforeMount: function () {
      //this.refreshGame();
    },
    usernameChange: function () {
      ax.get(
        `/game/${this.game_uid}/${this.user_uid}/name?name=${this.user_name}`
      );
    },
    refreshGame: function () {
      ax.get(`/game/${this.game_uid}/join`).then((g) => {
        let game = JSON.parse(g.data);
        this.game_uid = game.uid;
        //this.childComponentRef.refreshGame();
      });
    },
    orderChange: function () {
      localStorage.setItem("porder", this.porder);
    },
    newGame: function () {
      ax.get(`/game/new?np=${this.np_players}`).then((g) => {
        let game = JSON.parse(g.data);
        this.game_uid = game.uid;
        this.joinGame();
        //this.childComponentRef.refreshGame();
      });
    },
    joinGame: function () {
      ax.get(`/game/${this.game_uid}/join`).then((g) => {
        this.user_uid = g.data;
        console.log(this.user_uid);
        //this.childComponentRef.refreshGame();
        localStorage.setItem("user_uid", this.user_uid);
        let npath = `?game_uid=${this.game_uid}&user_uid=${this.user_uid}`;
        if (window.location.search != npath) window.location.search = npath;
      });
    },
    newRound: function () {
      ax.get(`/game/${this.game_uid}/new`).then((g) => {
        let round = JSON.parse(g.data);
        this.currentround = round.uid;
        this.childComponentRef.joinRound(null, this.currentround);
      });
    },
    joinRound: function () {
      this.childComponentRef.joinRound(null, this.currentround);
    },
    initRound: function () {
      this.childComponentRef.initRound();
    },
    hideclickedimpsChange: function () {
      localStorage.setItem("hide2", !this.hideclickedimps);
      this.hideclickedimps = !this.hideclickedimps;
    },

    hideclickedChange: function () {
      localStorage.setItem("hide", !this.hideclicked);
      this.hideclicked = !this.hideclicked;
    },
    hideclickeddashChange: function () {
      localStorage.setItem("hidedash", !this.hideclickeddash);
      this.hideclickeddash = !this.hideclickeddash;
    },
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>
.btn-img {
  opacity: 0.4;
  width: 5vh;
  transform: rotate(0.25turn);
  cursor: pointer;
  src: require(
    "../assets/cards/SVG-cards-1.3/SVG-cards-1.3/" + "Card_back_01.svg"
  );
}

.btn-img:hover {
  opacity: 0.8;
}

.hide {
  width: fit-content !important;
  font-size: x-small;
  cursor: pointer;
  transform: rotate(0.25turn);
  position: relative;
  left: 50%;
  color: rgba(255, 30, 0, 0.3);
  font-weight: bold;
}

.img-txt {
  color: black;
  font-weight: bold;
  position: absolute;
  font-size: 1vh;
  left: 0.3vh;
  top: 2vh;
  cursor: pointer;
}

.btn-container {
  position: relative;
}

.imp {
  border: none;
  opacity: 0.5;
  font-size: small;
}

.imp {
  border: none;
  opacity: 0.5;
  font-size: small;
}
.inputs {
  /*display: none;*/
  background-color: rgba(255, 30, 0, 0.1);
}
</style>
