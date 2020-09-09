import axios from 'axios';

export default {
  namespaced: true,
  state: {
    token: localStorage.getItem('access_token') || '',
    auth_status: '',
    auth_err: ''
  },
  mutations: {
    'AUTH_REQUEST': (state) => {
      state.status = 'loading'
    },
    'AUTH_SUCCESS': (state, token) => {
      state.status = 'success';
      state.token = token
    },
    'AUTH_ERROR': (state, err) => {
      state.status = 'error';
      state.auth_err = err
    },
    'AUTH_LOGOUT': (state) => {
      state.status = '';
      state.token = '';
    }
  },
  actions: {
    auth_post({commit, dispatch}, [path, postData]) {
      let pormise = new Promise((resolve, reject) => {
        axios.post(path, postData).then((res) => {
          if (res.data.token) {
            axios.defaults.headers.common['Authorization'] = res.data.token;
          }
          resolve(res);
        }).catch((err) => {
          if (err.response) {
            reject(err);
          } else if (err.request) {
            console.log('Request is made but no response from the server');
          } else {
            console.log('Error: ', err.message);
          }
        });
      });
      return pormise;
    },
    auth_success({commit}) {
      commit('AUTH_SUCCESS', localStorage.getItem('access_token'));
    },
    auth_error({commit}, err) {
      commit('AUTH_ERROR', err);
    },
    auth_logout({commit}) {
      delete axios.defaults.headers.common['Authorization']
      commit('AUTH_LOGOUT');
    }
  },
  modules: {},
  getters: {
    isAuthenticated: state => !!state.token,
    getStatus: state => state.status,
    getAuthErr: state => state.auth_err,
  }
}
