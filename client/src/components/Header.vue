<template>
  <nav class="nav-bar navbar-expand-lg navbar-dark">
    <div class="container-sm py-3">
      <router-link class="navbar-brand" to="/home">
        <img alt="EraO Logo" height="26.2" src="../assets/logo/erao-brand-white.png" width="102.8">
      </router-link>
      <button class="navbar-toggler border-white float-right" type="button" data-toggle="collapse" data-target="#navbarSupportedContent"
              aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <div class="nav-item d-block" v-if="!$store.getters['auth/isAuthenticated']">
          <router-link to="/user/register"><small class="login__register_link mr-3">Sign up</small></router-link>
          <router-link class="btn btn-outline-light " to="/user/login">Login</router-link>
        </div>

        <div class="nav-item btn-group" v-if="$store.getters['auth/isAuthenticated']">
          <router-link to="/user/profile">
            <button type="button" class="btn btn-outline-light rounded-left border-right-0">
              Profile
            </button>
          </router-link>
          <button type="button" class="btn btn-outline-light border-left-0 dropdown-toggle dropdown-toggle-split" data-toggle="dropdown"
                  aria-haspopup="true" aria-expanded="false">
            <span class="sr-only">Toggle Dropdown</span>
          </button>
          <div class="dropdown-menu dropdown-menu-right">
            <!-- Dropdown menu links -->
            <button class="dropdown-item" type="button">Action</button>
            <button class="dropdown-item" type="button">Another action</button>
            <div class="dropdown-divider"></div>
            <button @click="logout" class="dropdown-item" type="button">Log Out</button>
          </div>
        </div>
      </div>

    </div>
  </nav>
</template>

<script>
  import router from '../router'

  export default {
    name: "Header",
    mounted() {
      window.addEventListener("load", this.loadAnimation);
    },
    methods: {
      loadAnimation() {
        // TODO: loadAnimation
        console.log('Animation loaded');
      },
      logout() {
        localStorage.removeItem('user');
        localStorage.removeItem('access_token');
        this.$store.dispatch('auth/auth_logout')
        router.push('/home');
      }
    }
  }
</script>

<style scoped>
  nav {
    background-color: rgba(0, 0, 0, 0.75);
  }

  .login__register_link {
    color: white;
  }

  .rounded-left {
    border-top-left-radius: .25rem !important;
    border-bottom-left-radius: .25rem !important;
    border-top-right-radius: 0rem !important;
    border-bottom-right-radius: 0rem !important;
  }

  #navbarSupportedContent {
    float: right;
  }
</style>
