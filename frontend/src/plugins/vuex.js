import Vue from 'vue'
import Vuex from 'vuex'
import createPersistedState from 'vuex-persistedstate'

Vue.use(Vuex)

export default new Vuex.Store({
  plugins: [createPersistedState({
        storage: window.sessionStorage,
    })],
  state: {
    isAuthenticated: false,
    token: null,
    firstName: '',
    lastName: '',
    doctorId: null,
    facilityName: '',
    alert: {
      color: 'green',
      text: '',
      display: false
    }
  },
  mutations: {
    setAuthenticated (state, payload) {
      state.isAuthenticated = payload.authenticated;
      if (!payload.authenticated) {
        state.token = null;
      } else if (payload.token) {
        state.token = payload.token;
      }
    },
    setFullName(state, payload) {
      state.firstName = payload.firstName;
      state.lastName = payload.lastName;
    },
    setDoctorId(state, payload) {
      state.doctorId = payload.doctorId;
    },
    setAlert(state, payload) {
      state.alert.color = payload.color;
      state.alert.text = payload.text;
      state.alert.display = true;
    },
    setFacilityName(state, payload) {
      state.facilityName = payload.facilityName;
    }
  },
  actions: {
    showAlert({commit}, payload) {
      commit('setAlert', payload);

    }
  }
})

