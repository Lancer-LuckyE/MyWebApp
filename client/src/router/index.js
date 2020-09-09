import Vue from 'vue'
import Router from 'vue-router'
import store from '../store'
import Home from '../views/Home'
import Login from "../views/Login"
import Profile from "../views/Profile"
import Register from "../views/Register"

const needAuth = (to, from, next) => {
  if (!store.getters['auth/isAuthenticated']) {
    next('/user/login');
  } else {
    next()
  }
};

Vue.use(Router)
const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/home',
    name: 'Home',
    component: Home
  },
  {
    path: '/user/login',
    name: 'Login',
    component: Login
  },
  {
    path: '/user/register',
    name: 'Register',
    component: Register
  },
  {
    path: '/user/profile',
    name: 'Profile',
    component: Profile,
    beforeEnter: needAuth
  }
];

const router = new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
});

export default router;
