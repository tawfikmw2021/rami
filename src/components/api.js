import * as axios from "axios";
import { io } from "socket.io-client";

// "undefined" means the URL will be computed from the `window.location` object
//process.env.NODE_ENV = "production";
let api_url = localStorage.getItem("api_url") || undefined;
const burl =
  process.env.NODE_ENV === "production" ? api_url : "http://192.168.1.188:8086";


  let query = document.location.search;
const urlParams = new URLSearchParams(query);

let state = localStorage.getItem("game_state")
export const context = (function() { 
  let result = {}
  try {result = JSON.parse(state)} catch (error) {console.log(error)}
  return result || {}
})()

console.log(context)
let game_uid = urlParams.get("game_uid");
let round_uid = urlParams.get("round_uid");
let user_uid = urlParams.get("user_uid");
context["game_uid"] = game_uid || context["game_uid"] ;
context["round_uid"] = round_uid || context["round_uid"] ;
context["user_uid"] =user_uid || context["user_uid"];

localStorage.setItem("game_state",JSON.stringify(context))

let ax = new axios.Axios({
    baseURL:burl
  });

  export const socket = io(burl);

  /*socket.on("connect", () => {
    state.connected = true;
  });
  
  socket.on();
  
  socket.on("disconnect", () => {
    state.connected = false;
  });
  
  socket.on("foo", (...args) => {
    state.fooEvents.push(args);
  });
  
  socket.emit("join", { room: "someroom", username: "someuser" });*/

  export function saveContext(){
    localStorage.setItem("game_state", JSON.stringify(context))
  }
  
  export {ax}