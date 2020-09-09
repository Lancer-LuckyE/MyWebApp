// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import store from './store'
import axios from 'axios'
import 'bootstrap'
import 'bootstrap/dist/css/bootstrap.min.css'

Vue.config.productionTip = false;
const token = localStorage.getItem('access_token');
if (token) {
  axios.defaults.headers.common['Authorization'] = token;
}

new Vue({
  el: '#app',
  router,
  store,
  render: h => h(App)
}).$mount('#app');


