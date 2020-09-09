<template>
  <div>
    <div class="row justify-content-center">
      <form @submit="login"
            class="border border-primary rounded col-xl-5 col-lg-6 col-md-8 col-11 my-3 p-4 needs-validation" novalidate>
        <h1>Login</h1>
        <div v-if="this.error !== ''">
          <p style="color: red">
            <span><i class="fas fa-exclamation-triangle" style="color: red"></i></span>
            {{this.error}}
          </p>
        </div>
        <div class="form-group text-left">
          <label for="LoginEmailInput">Email address</label>
          <input class="form-control" id="LoginEmailInput" placeholder="Enter email"
                 required type="email" v-model="email">
          <div class="invalid-feedback">Invalid Email</div>
        </div>
        <div class="form-group text-left">
          <label for="LoginPWInput">Password</label>
          <!--TODO: href="/#"-->
          <div class="d-inline-block float-right"><a href="/#"><small>Forget Password</small></a></div>
          <input class="form-control" id="LoginPWInput" placeholder="Password" required type="password"
                 v-model="password">
          <div class="invalid-feedback">Empty Password</div>
        </div>
        <button class="btn btn-primary col-4" type="submit">Login</button>
      </form>
      <div class="col-8">
        <router-link to="/user/register">Don't have an account yet? Sign Up here!</router-link>
      </div>
    </div>
  </div>
</template>

<script>
  import VueJwtDecode from 'vue-jwt-decode';

  export default {
    name: "Login",
    data() {
      return {
        email: '',
        password: '',
        error: '',
      };
    },
    methods: {
      login(event) {
        event.preventDefault();
        const form = event.currentTarget;
        form.classList.add('was-validated');
        if (form.checkValidity() === false) {
          event.stopPropagation();
          // console.log('form invalid');
        } else {
          // console.log('form validated');
          // TODO: use https in production
          const path = '/api/user/login';
          // console.log(path);
          const postData = {
            'email': this.email,
            'password': this.password,
          };
          this.$store.dispatch('auth/auth_post', [path, postData]).then((res) => {
            localStorage.setItem('user', JSON.stringify(VueJwtDecode.decode(res.data.token)['identity']));
            localStorage.setItem('access_token', res.data.token);
            this.$store.dispatch('auth/auth_success');
            console.log(res.data.msg);
            this.error = '';
            this.$router.push({name: 'Profile'});
          }).catch((err) => {
            this.error = err.response.data.msg;
          });
        }
      },


    }
  }
</script>

<style scoped>

</style>
