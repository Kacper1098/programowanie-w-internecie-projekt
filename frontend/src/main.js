import Vue from 'vue'
import App from './App.vue'
import vuetify from './plugins/vuetify';
import router from "./router";
import axios from 'axios';
import store from './plugins/vuex';

const token = store.state.token;
if (token) {
    axios.defaults.headers.common['Authorization'] = `JWT ${token}`;
}

axios.defaults.baseURL = 'http://localhost:8000/api';
Vue.prototype.$http = axios;

Vue.config.productionTip = false;

router.beforeEach((to, from, next) => {
    const loggedIn = store.state.isAuthenticated;
    if (to.matched.some(record => record.meta.requiresAuth)) {
        if (!loggedIn) {
            next({ path: '/login' });
        } else {
            next();
        }
    }
    if (to.matched.some(record => record.meta.hideForAuth)) {
        if (loggedIn) {
            next(from);
        } else {
            next();
        }
    }
});

const ignoreWarnMessage = 'The .native modifier for v-on is only valid on components but it was used on <div>.';
Vue.config.warnHandler = function (msg, vm, trace) {
  if (msg === ignoreWarnMessage) {
    msg = null;
    vm = null;
    trace = null;
  }
}

new Vue({
  vuetify,
  router,
    store,
  render: h => h(App)
}).$mount('#app')
