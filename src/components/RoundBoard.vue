<template>
  <div
    style="display: none; height: 100px; width: 200px; border: solid 1px"
    @drop="(ev) => console.log(ev.dataTransfer)"
    @dragover="(ev) => ev.preventDefault()"
  ></div>
  <div class="row m-0" style="">
    <div class="p-0">
      <div class="form-group">
        <div
          class="row"
          style="display: none; background-color: rgba(255, 50, 0, 0.2)"
        >
          <div
            class="col-12"
            @click="hideclicked = !hideclicked"
            style="cursor: pointer"
          >
            <div class="hide" :class="{ hideclicked: hideclicked }">
              {{ hideclicked ? ">" : "<" }}
            </div>
          </div>
        </div>
        <div class="d-flex justify-content-around">
          <div
            @click="
              () => {
                this.performance = !this.performance;
                this.refreshGame();
              }
            "
            class="btn-container flex-grow-1"
          >
            <img
              class="btn-img"
              v-bind:src="
                require('../assets/cards/SVG-cards-1.3/SVG-cards-1.3/Card_back_01.svg') +
                '#svgView(preserveAspectRatio(none))'
              "
            />
            <span class="img-txt"> teswira kamla wella la </span>
          </div>

          <div @click="getCard" class="btn-container flex-grow-1">
            <img
              class="btn-img"
              v-bind:src="
                require('../assets/cards/SVG-cards-1.3/SVG-cards-1.3/Card_back_01.svg') +
                '#svgView(preserveAspectRatio(none))'
              "
            />
            <span class="img-txt"> echri </span>
          </div>
          <div @click="getCardDown" class="btn-container flex-grow-1">
            <img
              class="btn-img"
              v-bind:src="
                require('../assets/cards/SVG-cards-1.3/SVG-cards-1.3/Card_back_01.svg') +
                '#svgView(preserveAspectRatio(none))'
              "
            />
            <span class="img-txt"> rakked </span>
          </div>

          <div @click="getthrown" class="btn-container flex-grow-1">
            <img
              class="btn-img"
              v-bind:src="
                require('../assets/cards/SVG-cards-1.3/SVG-cards-1.3/Card_back_01.svg') +
                '#svgView(preserveAspectRatio(none))'
              "
            />
            <span class="img-txt"> faskel </span>
          </div>
          <div @click="throwCard" class="btn-container flex-grow-1">
            <img
              class="btn-img"
              v-bind:src="
                require('../assets/cards/SVG-cards-1.3/SVG-cards-1.3/Card_back_01.svg') +
                '#svgView(preserveAspectRatio(none))'
              "
            />
            <span class="img-txt"> tayech </span>
          </div>
          <!--+ '#svgView(preserveAspectRatio(none))'-->
          <div @click="getDown" class="btn-container flex-grow-1">
            <img
              class="btn-img"
              v-bind:src="
                require('../assets/cards/SVG-cards-1.3/SVG-cards-1.3/Card_back_01.svg') +
                '#svgView(preserveAspectRatio(none))'
              "
            />
            <span class="img-txt"> ahbet </span>
          </div>
          <div @click="revertGame" class="btn-container flex-grow-1">
            <img
              class="btn-img"
              v-bind:src="
                require('../assets/cards/SVG-cards-1.3/SVG-cards-1.3/Card_back_01.svg') +
                '#svgView(preserveAspectRatio(none))'
              "
            />
            <span class="img-txt"> arje3 </span>
          </div>
          <div @click="refreshGame" class="btn-container flex-grow-1">
            <img
              class="btn-img"
              v-bind:src="
                require('../assets/cards/SVG-cards-1.3/SVG-cards-1.3/Card_back_01.svg') +
                '#svgView(preserveAspectRatio(none))'
              "
            />
            <span class="img-txt"> refresh </span>
          </div>
        </div>
      </div>
    </div>
  </div>
  <div>
    <div class="row m-0">
      <div class="col-12 col-md-10">
        <!--h3>Draggable {{ draggingInfo }}</h3-->

        <div class="d-flex justify-content-around">
          <div class="d-flex">
            <div class="ncards">{{ nremaining }}</div>
            <img
              @click="getCard"
              style="cursor: pointer; height: 15vh"
              v-bind:src="
                require('../assets/cards/SVG-cards-1.3/SVG-cards-1.3/' +
                  'Card_back_01.svg') + '#svgView(preserveAspectRatio(none))'
              "
            />
          </div>
          <draggable
            :list="thrown"
            :disabled="false"
            item-key="name"
            class="list-group2 d-flex"
            ghost-class="ghost"
            :move="checkMove(thrown.length)"
            @start="dragging = true"
            @end="dragging = false"
          >
            <template #item="{ element, index }">
              <div
                :style="{
                  /*'transform-origin':'right bottom',
            transform: `translate(${index*0+80}%, 0)`
      + ` rotate(${(index)*0.21/14-0.02}turn)`
      ,*/
                  width: '2vh',
                  overflow: index >= thrown.length - 1 ? 'hidden2' : 'hidden2',
                  top: element.selected ? 0 : 0,
                }"
                class="list-group-item"
                :class="{ 'not-draggable': !enabled }"
              >
                <div
                  style="display: "
                  v-on:dblclick="element.selected = !element.selected"
                >
                  <img
                    @click="throwCard2"
                    style="height: 15vh; cursor: pointer"
                    v-bind:src="
                      require('../assets/cards/SVG-cards-1.3/SVG-cards-1.3/' +
                        getNumber2(element.number, element.color) +
                        '.svg')
                    "
                  />
                </div>
              </div>
            </template>
          </draggable>
        </div>

        <div>
          <div
            :class="{ fullscreen: fullscreen }"
            class="d-flex justify-content-around m-0"
          >
            <!--h3>Draggable {{ draggingInfo }}</h3-->

            <draggable
              :list="myCards"
              :disabled="!enabled"
              item-key="name"
              class="list-group2 d-flex"
              ghost-class="ghost"
              :move="checkMove(myCards.length)"
              @start="dragging = true"
              @end="onDrageEnd(100)"
            >
              <template #item="{ element, index }">
                <div
                  :style="{
                    /*'transform-origin':'right bottom',
            transform: `translate(${index*0+80}%, 0)`
      + ` rotate(${(index)*0.21/14-0.02}turn)`
      ,*/
                    width:
                      index >= myCards.length - 1
                        ? '3vh'
                        : fullscreen
                        ? '6vh'
                        : '3vh',
                    overflow:
                      (index >= myCards.length - 1 && !lastdragging) ||
                      (index == myCards.length - 2 && lastdragging)
                        ? 'hidden'
                        : 'hidden',
                    top:
                      (element.selected ? -5 : 0 + fullscreen ? 20 : 0) + 'vh',
                  }"
                  class="list-group-item"
                  :class="{ 'not-draggable': !enabled }"
                >
                  <div
                    style="display: "
                    v-on:dblclick="element.selected = !element.selected"
                  >
                    <img
                      :style="{ height: fullscreen ? '50vh' : '15vh' }"
                      v-bind:src="
                        require('../assets/cards/SVG-cards-1.3/SVG-cards-1.3/' +
                          getNumber2(element.number, element.color) +
                          '.svg')
                      "
                    />
                  </div>
                </div>
              </template>
            </draggable>
            <div
              class="m-2 p-1"
              v-bind:title="fullscreen ? 'close' : 'go fullscreen'"
              style="
                display: none;
                z-index: 100;
                background-color: white;
                cursor: pointer;
                height: 35px;
                border: solid 1px;

                width: 20px;
              "
              @click="fullscreen = !fullscreen"
            >
              {{ fullscreen ? "x" : "f" }}
            </div>
          </div>
        </div>

        <div v-for="player in players" v-bind:key="player.order">
          <div class="d-flex p-1">
            <div class="m-2" style="width: 10vw; overflow: hidden">
              <input
                v-if="player.uid.length > 15"
                class=""
                style="
                  border: solid 1px rgba(0, 0, 0, 0.1);
                  text-align: center;
                  width: 10vw;
                "
                title="user_name"
                v-model="user_name"
                v-bind:placeholder="player.order"
                @change="usernameChange"
              />
              <span v-else>{{ player.name || player.order }}</span>
            </div>

            <div
              class="d-flex"
              :style="{ width: player.cards.length * 0.5 + 15 + 'vh' }"
            >
              <div class="ncards">{{ player.cards.length }}</div>
              <div style="width: 0.5vw">
                <img
                  :style="{
                    height: player.cardsDown.length > 0 ? '15vh' : '8vh',
                  }"
                  v-bind:src="
                    require('../assets/cards/SVG-cards-1.3/SVG-cards-1.3/' +
                      'Card_back_01.svg') +
                    '#svgView(preserveAspectRatio(none))'
                  "
                />
              </div>
              <!--div v-for="card in player.cards" v-bind:key="card.id">
                <div style="width: 0.5vw">
                  <img
                    :style="{
                      height: player.cardsDown.length > 0 ? '15vh' : '8vh',
                    }"
                    v-bind:src="
                      require('../assets/cards/SVG-cards-1.3/SVG-cards-1.3/' +
                        'Card_back_01.svg') +
                      '#svgView(preserveAspectRatio(none))'
                    "
                  />
                </div>
              </div-->
            </div>
            <div
              v-for="(down, index2) in player.cardsDown"
              v-bind:key="down.ib"
            >
              <div class="px-3">
                <draggable
                  :list="makeReactive(down)"
                  :disabled="false"
                  item-key="id"
                  class="list-group2 d-flex"
                  ghost-class="ghost"
                  :move="checkMove(down.length)"
                  @start="dragging = true"
                  @end="onDrageEnd(index2)"
                >
                  <template #item="{ element, index }">
                    <div
                      :style="{
                        /*'transform-origin':'right bottom',
            transform: `translate(${index*0+80}%, 0)`
      + ` rotate(${(index)*0.21/14-0.02}turn)`
      ,*/
                        width: '2vh',
                        overflow:
                          index >= down.length - 1 ? 'hidden' : 'hidden',
                        top: element.selected ? '-2vh' : 0,
                      }"
                      class="list-group-item"
                      :class="{ 'not-draggable': !enabled }"
                    >
                      <div
                        style="display: "
                        v-on:dblclick="element.selected = !element.selected"
                      >
                        <img
                          style="height: 15vh"
                          v-bind:src="
                            require('../assets/cards/SVG-cards-1.3/SVG-cards-1.3/' +
                              getNumber2(element.number, element.color) +
                              '.svg')
                          "
                        />
                      </div>
                    </div>
                  </template>
                </draggable>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="col-12 col-md-2">
        <div v-for="notif in shownalert" v-bind:key="notif[1]">
          <div class="alert alert-success" v-html="notif[0]" role="alert"></div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import draggable from "vuedraggable";
import { reactive } from "vue";
import { ax, socket, context, saveContext } from "./api.js";

/*export const state = reactive({
  connected: false,
  fooEvents: [],
  barEvents: [],
});*/

let cardsBase = Array.from(Array(26))
  .flatMap((v, i) => [
    { number: Math.floor(i / 2) + 1, color: "clubs" },
    { number: Math.floor(i / 2) + 1, color: "spades" },
    { number: Math.floor(i / 2) + 1, color: "hearts" },
    { number: Math.floor(i / 2) + 1, color: "diamonds" },
  ])
  .concat(
    Array.from(Array(4)).map((v, i) => {
      return { number: 0, color: "hearts" };
    })
  );

function shuffle(array) {
  let currentIndex = array.length,
    randomIndex;

  // While there remain elements to shuffle.
  while (currentIndex > 0) {
    // Pick a remaining element.
    randomIndex = Math.floor(Math.random() * currentIndex);
    currentIndex--;

    // And swap it with the current element.
    [array[currentIndex], array[randomIndex]] = [
      array[randomIndex],
      array[currentIndex],
    ];
  }

  return array;
}

let id = 1;
export default {
  props: ["user_uid", "game_uid", "round_uid"],
  name: "RoundBoard",
  display: "Simple",
  components: {
    draggable,
  },
  setup() {},
  data() {
    return {
      enabled: true,
      myCards: [],
      dragging: false,
      lastdragging: reactive(false),
      user_name: "",
      np_players: 4,
      hideclicked: true,
      hideresumeclicked: true,
      alert: [],
      performance: false,
      api_url: localStorage.getItem("api_url"),
      shownalert: [],
      players: [],
      fullscreen: false,
      shownotif: true,
      thrown: [],
      porder: 0,
      nremaining: 0,
    };
  },
  computed: {
    draggingInfo() {
      return this.dragging ? "under drag" : "";
    },
  },
  beforeCreate: function () {
    socket.on("update", (args) => {
      //state.barEvents.push(args);
      this.refreshGame();
    });
    socket.on("notif", (...args) => {
      //state.barEvents.push(args);
      this.alert.push(args[0]);
      this.shownalert = this.alert
        .map((v, index) => {
          v = v.replace("origin", document.location.origin);
          v = v.replace("[puid]", this.user_uid);

          return [v, index];
        })
        .slice(this.alert.length >= 4 ? this.alert.length - 4 : 0)
        .reverse();

      this.shownotif = true;
    });
  },
  beforeMount: function () {
    this.refreshGame();
  },
  methods: {
    makeReactive: function (o) {
      return reactive(o);
    },
    joinRound: function (ev, round_uid) {
      ax.get(
        `/game/${this.game_uid}/${round_uid || this.round_uid}/${
          this.user_uid
        }/join`
      ).then((g) => {
        let p = JSON.parse(g.data);
        context["porder"] = p.order;
        context["user_name"] = p.user_name;
        context["round_uid"] = this.round_uid;
        console.log("join round", this.game_uid, this.round_uid, this.user_uid);
        saveContext("context_change");
        /*let npath = `?game_uid=${this.game_uid}&round_uid=${this.round_uid}&user_uid=${this.user_uid}`;
        if (window.location.search != npath) window.location.search = npath;*/

        //this.childComponentRef.refreshGame();
      });
    },

    initRound: function () {
      ax.get(`/game/${this.game_uid}/${this.round_uid}/init`).then((g) => {
        //this.childComponentRef.refreshGame();
      });
    },

    endRound: function () {
      ax.get(
        `/game/${this.game_uid}/${this.round_uid}/${this.user_uid}/end`
      ).then((g) => {
        //this.childComponentRef.refreshGame();
      });
    },

    refreshGame: function () {
      if (!this.user_uid) return;

      ax.get(`/game/${this.game_uid}/${this.round_uid}/${this.user_uid}`)
        .then((g) => {
          let round = JSON.parse(g.data);
          //this.game_uid = game.uid;
          let me = round.players.find((v) => v.uid == this.user_uid);
          if (me) {
            this.porder = me.order;
            this.myCards = me.cards;
            this.user_name = me.name;
          } else {
            this.myCards = [];
            this.user_name = [];
          }
          this.np_players = round.players.length;

          this.players = round.players;
          this.thrown = round.thrownCards;
          this.nremaining = round.nremaining;
        })
        .catch((v) => {});
    },
    throwCard2: function () {
      this.throwCard();
      /*let l = this.myCards.length + this.thrown[this.porder].map(v=> v.length).sum();
      if (l == 15) this.throwCard();

      let elm = this.myCards.filter((v) => v.selected);
      if (elm.length == 1)
        ax.get(
          `/game/${this.game_uid}/${this.round_uid}/${this.user_uid}/${elm[0].id}`
        ).then((g) => {});*/
    },

    throwCard: function () {
      let elm = this.myCards.filter((v) => v.selected);
      if (elm.length == 1)
        ax.get(
          `/game/${this.game_uid}/${this.round_uid}/${this.user_uid}/${elm[0].id}`
        ).then((g) => {});
    },
    getCard: function () {
      ax.get(
        `/game/${this.game_uid}/${this.round_uid}/${this.user_uid}/get`
      ).then((g) => {});
    },
    getDown: function () {
      let sel = this.myCards.filter((v) => v.selected).length;
      let sel2 = this.players
        .flatMap((p) => p.cardsDown.flatMap((gc) => gc))
        .filter((v) => v.selected);

      console.log(sel2);
      if (sel > 0 && sel2.length <= 1)
        ax.get(
          `/game/${this.game_uid}/${this.round_uid}/${
            this.user_uid
          }/down?target=${
            sel2.length == 1 ? sel2[0].id : -1
          }&cards=${this.myCards
            .filter((v) => v.selected)
            .map((v) => v.id)
            .join(",")}`
        ).then((g) => {});
    },
    getthrown: function () {
      ax.get(
        `/game/${this.game_uid}/${this.round_uid}/${this.user_uid}/getthrown`
      ).then((g) => {});
    },

    revertGame: function () {
      ax.get(
        `/game/${this.game_uid}/${this.round_uid}/${this.user_uid}/revert`
      );
    },

    getCardDown: function () {
      let mycard = this.myCards.find((v) => v.selected);
      let possible = this.players.flatMap((player) => {
        var cards = player.cardsDown.flatMap((down, index) =>
          down
            .filter((v) => v.selected)
            .map((card) => {
              return { order: player.order, cardid: card.id, downi: index };
            })
        );
        return cards;
      });

      var ps = possible
        .map((v) => `${mycard.id},${v.order},${v.downi},${v.cardid}`)
        .join(";");

      ax.get(
        `/game/${this.game_uid}/${this.round_uid}/${this.user_uid}/downcard?possible=${ps}`
      );
    },
    urlchange: function () {
      localStorage.setItem("api_url", this.api_url);
    },

    getNumber2: function (number, color) {
      switch (number) {
        case 0:
          return "red_joker";
        case 1:
          return "ace_of_" + color;
        case 11:
          return "jack_of_" + color + (this.performance ? "2" : "");
        case 12:
          return "queen_of_" + color + (this.performance ? "2" : "");
        case 13:
          return "king_of_" + color + (this.performance ? "2" : "");
        default:
          return number + "_of_" + color;
      }
    },
    add: function () {
      this.list.push({ name: "Juan " + id, id: id++ });
    },
    replace: function () {
      this.list = [{ name: "Edgard", id: id++ }];
    },
    checkMove: function (n = 1) {
      return (e) => {
        this.lastdragging = e.draggedContext.index == n - 1;
        /*window.console.log(
          "Future index: " +
            e.draggedContext.element +
            "  " +
            this.lastdragging +
            " " +
            e.draggedContext.futureIndex +
            "  " +
            e.draggedContext.index
        );*/
        //e.draggedContext.element.style.overflow = "hidden";
      };
    },
    onDrageEnd: function (tp = 0) {
      this.dragging = false;

      ax.get(
        `/game/${this.game_uid}/${this.round_uid}/${
          this.user_uid
        }/sort/${tp}?cards=${(tp == 100
          ? this.myCards
          : this.players[this.porder].cardsDown[tp]
        )
          .map((v) => v.id)
          .join(",")}`
      );
    },
  },
};
</script>
<style scoped>
.buttons {
  margin-top: 35px;
}

.ncards {
  color: rgba(100, 30, 100, 0.5);
}

.ghost {
  opacity: 0.5;
  background: #c8ebfb;
}

.fullscreen {
  position: fixed;
  top: 0;
  left: 0;
  min-width: 100vw;
  min-height: 100vh;
  background-color: wheat;
  z-index: 1000;
  overflow: auto;
}

.impn {
  display: none;
}

.wrap {
  z-index: 1000;
  width: 100vw;
  height: 100vh;
  position: absolute;
  top: 0;
  left: 0;
  background-color: white;
}
.hidawrap {
  width: 5vw;
  height: 100vh;
  background-color: rgba(255, 30, 0, 0.3);
}
</style>
