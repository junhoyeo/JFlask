import Vue from 'vue'
import App from './App.vue'
import router from './router'
import axios from 'axios'

Vue.config.productionTip = false
Vue.prototype.$api = axios.create({
  baseURL: 'http://localhost:5000/'
})

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
