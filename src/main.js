import { createApp } from 'vue'
import App from './App.vue'
import RamiVue from "./components/RamiVue.vue"
import simpleList from "./components/simpleList.vue"
import { createRouter, createWebHashHistory } from 'vue-router'

const router = createRouter({
    history: createWebHashHistory(),
    routes: [
      // Les segments dynamiques commencent avec la ponctuation deux-points
      { path: "/game/:uid", component: simpleList },
      { path: "/simple", component: simpleList },
      { path: "/", component: simpleList },
    ],
  });
  

createApp(App)
//.use(router)
.mount('#app')
