import * as axios from "axios";
import { io } from "socket.io-client";

// "undefined" means the URL will be computed from the `window.location` object
//process.env.NODE_ENV = "production";
let api_url = localStorage.getItem("api_url") || undefined;
const burl =
  process.env.NODE_ENV === "production" ? api_url : "http://192.168.1.188:8086";


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

  
  export {ax}