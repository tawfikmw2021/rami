<template>
  <div class="row m-0">
    <div class="p-0" v-if="!hideclicked">
      <div class="row m-0" style="">
        <div class="p-0">
          <div class="form-group">
            <div class="row" style="background-color: rgba(255, 50, 0, 0.2)">
              <div class="col-12" style="cursor: pointer">
                <div
                  class="hide"
                  :class="{ hideclicked: hideclickedimps }"
                ></div>
              </div>
            </div>
            <div class="d-flex justify-content-around">
              <!--div @click="newGame" class="btn-container flex-grow-1">
                <img
                  class="btn-img"
                  v-bind:src="
                    require('../assets/cards/SVG-cards-1.3/SVG-cards-1.3/Card_back_01.svg')
                  "
                />
                <span class="img-txt"> new game </span>
              </div>

              <div @click="joinGame" class="btn-container flex-grow-1">
                <img
                  class="btn-img"
                  v-bind:src="
                    require('../assets/cards/SVG-cards-1.3/SVG-cards-1.3/Card_back_01.svg')
                  "
                />
                <span class="img-txt"> join game </span>
              </div>

              <div @click="newRound" class="btn-container flex-grow-1">
                <img
                  class="btn-img"
                  v-bind:src="
                    require('../assets/cards/SVG-cards-1.3/SVG-cards-1.3/Card_back_01.svg')
                  "
                />
                <span class="img-txt"> new round </span>
              </div>
              <div @click="joinRound" class="btn-container flex-grow-1">
                <img
                  class="btn-img"
                  v-bind:src="
                    require('../assets/cards/SVG-cards-1.3/SVG-cards-1.3/Card_back_01.svg')
                  "
                />
                <span class="img-txt"> join round </span>
              </div!-->

              <div @click="initRound" class="btn-container flex-grow-1">
                <img
                  class="btn-img"
                  v-bind:src="
                    require('../assets/cards/SVG-cards-1.3/SVG-cards-1.3/Card_back_01.svg')
                  "
                />
                <span class="img-txt"> init round </span>
              </div>
              <div @click="endRound" class="btn-container flex-grow-1">
                <img
                  class="btn-img"
                  v-bind:src="
                    require('../assets/cards/SVG-cards-1.3/SVG-cards-1.3/Card_back_01.svg')
                  "
                />
                <span class="img-txt"> end round </span>
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
    :user_uid="user_uid"
    :game_uid="game_uid"
    :round_uid="currentround"
    ref="childComponentRef"
  />
</template>
<script>
import RoundBoard from "./RoundBoard.vue";
import { ax } from "./api.js";
import { ref } from "vue";
import { context, saveContext, subscribeToEvent } from "./api";

export default {
  name: "GameBoard",
  components: {
    RoundBoard,
  },
  data: function () {
    return {
      hideclicked: context["hide"],
      hideclickedimps: localStorage.getItem("hide2") == "true",
      hideclickeddash: localStorage.getItem("hidedash") == "true",
      np_players: 4,
      game_uid: context["game_uid"],
      user_uid: context["user_uid"],
      currentround: context["round_uid"],
    };
  },
  setup() {
    const childComponentRef = ref(null);
    return {
      childComponentRef,
    };
  },
  created() {
    subscribeToEvent("click_game_join", "game_b", (args) => {
      console.log("click_game_join");
      let joingame = this.game_uid != args[0];
      this.game_uid = args[0];
      if (joingame) this.joinGame();
    });

    subscribeToEvent("click_round_join", "game_b", (args) => {
      console.log("click_round_join");
      let joingame = this.game_uid != args[0];
      let joinround = this.currentround != args[1];

      this.game_uid = args[0];
      this.currentround = args[1];
      console.log("ev", args, joingame, joinround);
      if (joingame) this.joinGame().then(() => this.joinRound());
      else if (joinround) this.joinRound();
      else {
        context["round_uid"] = this.currentround;
        saveContext("context_change");
      }
    });
    subscribeToEvent("click_game_new", "game_b", () => {
      console.log("click_round_new");
      this.newGame();
    });

    subscribeToEvent("click_round_new", "game_b", () => {
      this.newRound();
    });
  },
  methods: {
    refreshGame: function () {
      ax.get(`/game/${this.game_uid}/join`).then((g) => {
        console.log();
        let game = JSON.parse(g.data);
        this.game_uid = game.uid;
        //this.childComponentRef.refreshGame();
      });
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
      return ax.get(`/game/${this.game_uid}/join`).then((g) => {
        if (g.data.length > 100) return;
        this.user_uid = g.data;
        console.log("join", this.game_uid, this.user_uid);
        //this.childComponentRef.refreshGame();
        context["user_uid"] = this.user_uid;
        context["game_uid"] = this.game_uid;
        saveContext("context_change");
        /*let npath = `?game_uid=${this.game_uid}&user_uid=${this.user_uid}`;
        if (window.location.search != npath) window.location.search = npath;*/
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
    endRound: function () {
      this.childComponentRef.endRound();
    },
    hideclickedimpsChange: function () {
      localStorage.setItem("hide2", !this.hideclickedimps);
      this.hideclickedimps = !this.hideclickedimps;
    },

    hideclickedChange: function () {
      context["hide"] = !this.hideclicked;
      saveContext(context);
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
  height: 5vh;
  /*transform: rotate(0.25turn);*/
  cursor: pointer;
  src: require(
    "../assets/cards/SVG-cards-1.3/SVG-cards-1.3/" + "Card_back_01.svg"
  );
  aspect-ratio: 4/1;

  display: none;
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
  font-size: x-small;
  cursor: pointer;
}

.img-txt2 {
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
  background-color: rgba(255, 30, 0, 0.1);
  cursor: pointer;
  border-left: solid 1px;
  text-align: center;
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
