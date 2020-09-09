import Vue from 'vue'
import Vuex from 'vuex'
import authenticationMod from "./authentication";

Vue.use(Vuex)

export default new Vuex.Store({
  state: {

  },
  mutations: {

  },
  actions: {

  },
  modules: {
    auth: authenticationMod,
  },
  getters: {

  }
})
