<template>
    <nav class="nav-bar navbar-light">
        <div class="container-sm py-3">
            <router-link to="/home" class="navbar-brand">
                <img alt="EraO Logo" height="26.2" src="../assets/logo/erao-brand-white.png" width="102.8">
            </router-link>
            <div v-if="!$store.getters['auth/isAuthenticated']" class="float-right">
                <router-link to="/user/register"><small class="login__register_link mr-3">Sign up</small></router-link>
                <router-link to="/user/login" class="btn btn-outline-light ">Login</router-link>
            </div>
            <div v-if="$store.getters['auth/isAuthenticated']" class="float-right">
                <button class="btn btn-outline-light" type="button" @click="logout">Log Out</button>
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
</style>
