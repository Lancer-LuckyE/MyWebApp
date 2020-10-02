<template>
  <div>
    <div class="row justify-content-center">
      <form @submit="register"
            class="border border-primary rounded col-xl-5 col-lg-6 col-md-8 col-11 my-3 p-4 needs-validation"
            novalidate>
        <h1>Sign Up</h1>
        <div v-if="this.error !== ''">
          <p style="color: red">
            <span><i class="fas fa-exclamation-triangle" style="color: red"></i></span>
            {{this.error}}
          </p>
        </div>
        <div class="form-group text-left">
          <label for="RegisterEmailInput">Email address</label>
          <input class="form-control" id="RegisterEmailInput" placeholder="Enter email"
                 required type="email" v-model="email">
          <div class="invalid-feedback">Invalid Email</div>
        </div>
        <div class="form-group text-left">
          <label for="RegisterPWInput">Password</label>
          <input class="form-control" id="RegisterPWInput" placeholder="Password" required type="password"
                 v-model="password">
          <div class="invalid-feedback">Empty Password</div>
        </div>
        <div class="form-group text-left">
          <label for="RegisterPWConfirm">Password Confirmation</label>
          <input class="form-control" id="RegisterPWConfirm" placeholder="Re-enter Password" required
                 type="password" v-model="pw_confirm">
          <!--                    TODO: v-if to switch-->
          <!--                    <div class="invalid-feedback">Password not matched</div>-->
          <div class="invalid-feedback">Not Matching Password</div>
        </div>
        <div class="form-group text-left">
          <label for="RegisterLastInput">Last Name</label>
          <input class="form-control" id="RegisterLastInput" placeholder="Enter last name"
                 required type="text" v-model="lastName">
          <div class="invalid-feedback">Empty Last Name</div>
        </div>
        <div class="form-group text-left">
          <label for="RegisterFirstInput">First Name</label>
          <input class="form-control" id="RegisterFirstInput" placeholder="Enter first name"
                 required type="text" v-model="firstName">
          <div class="invalid-feedback">Empty First Name</div>
        </div>
        <button class="btn btn-primary col-4" type="submit">Submit</button>
      </form>
      <router-link class="col-12" to="/user/login">Already have an account? Login here!</router-link>
    </div>
  </div>
</template>

<script>
  import VueJwtDecode from "vue-jwt-decode";

  export default {
    name: "Register",
    data() {
      return {
        email: '',
        password: '',
        pw_confirm: '',
        lastName: '',
        firstName: '',
        pw_matching: false,
        error: ''
      };
    },
    methods: {
      setStyle() {
        const input = document.getElementById('RegisterPWConfirm');
        if (this.pw_matching) {
          input.addEventListener('focus', (e) => {
            input.boxShadow = '0 0 0 0.2rem rgba(40,167,69,.25)';
            input.style.webkitBoxShadow = '0 0 0 0.2rem rgba(40,167,69,.25)';
          });
          input.style.borderColor = "#28a745";
          input.style.backgroundImage = 'url("data:image/svg+xml,%3csvg xmlns=\'http://www.w3.org/2000/svg\' ' +
            'width=\'8\' height=\'8\' viewBox=\'0 0 8 8\'%3e%3cpath fill=\'%2328a745\' ' +
            'd=\'M2.3 6.73L.6 4.53c-.4-1.04.46-1.4 1.1-.8l1.1 1.4 3.4-3.8c.6-.63 1.6-.27 1.2.7l-4 4.6c-.43.5-.8.4-1.1.1z\'' +
            '/%3e%3c/svg%3e")';
          input.classList.remove('is-invalid');
          input.classList.add('is-valid');
        } else {
          input.addEventListener('focus', (e) => {
            input.style.boxShadow = '0 0 0 0.2rem rgba(220,53,69,.25)';
            input.style.webkitBoxShadow = '0 0 0 0.2rem rgba(220,53,69,.25)';
          });
          input.style.borderColor = "#dc3545";
          input.style.backgroundImage = 'url("data:image/svg+xml,%3csvg xmlns=\'http://www.w3.org/2000/svg\' ' +
            'width=\'12\' height=\'12\' fill=\'none\' stroke=\'%23dc3545\' viewBox=\'0 0 12 12\'%3e%3ccircle ' +
            'cx=\'6\' cy=\'6\' r=\'4.5\'/%3e%3cpath stroke-linejoin=\'round\' d=\'M5.8 3.6h.4L6 6.5z\'/%3e%3ccircle ' +
            'cx=\'6\' cy=\'8.2\' r=\'.6\' fill=\'%23dc3545\' stroke=\'none\'/%3e%3c/svg%3e")';
          input.classList.remove('is-valid');
          input.classList.add('is-invalid');
        }
      },

      register(event) {
        event.preventDefault();
        const form = event.currentTarget;
        form.classList.add('was-validated');
        if (form.checkValidity() === false || this.password !== this.pw_confirm) {
          event.stopPropagation();
          // console.log('form invalid');
        } else {
          // From checked, process the registration
          // console.log('form validated');
          // TODO: use https in production
          const path = '/api/user/register';
          // console.log(path);
          const postData = {
            'email': this.email,
            'password': this.password,
            'last_name': this.lastName,
            'first_name': this.firstName
          };
          this.$store.dispatch('auth/auth_post', [path, postData]).then((res) => {
            console.log(res.data.msg);
            //this.$router.push('/user/login');
            const loginPath = '/api/user/login';
            const loginPostData = {
              'email': this.email,
              'password': this.password
            };
            this.$store.dispatch('auth/auth_post', [loginPath, loginPostData]).then((res) => {
              localStorage.setItem('user', JSON.stringify(VueJwtDecode.decode(res.data.token)['identity']));
              localStorage.setItem('access_token', res.data.token);
              this.$store.dispatch('auth/auth_success');
              console.log(res.data.msg);
              this.error = '';
              this.$router.push({name: 'Profile'});
            }).catch((err) => {
              this.error = err.response.data.msg;
            });
          }).catch((err) => {
            this.error = err.response.data.msg;
          });
        }
      },
    },
    watch: {
      pw_confirm: {
        handler: function () {
          let PWConfirm = document.getElementById('RegisterPWConfirm');
          if (this.pw_confirm === this.password && this.pw_confirm !== '' && this.password !== '') {
            //console.log('success')
            this.pw_matching = true;
            this.setStyle();
          } else {
            //console.log('failed')
            this.pw_matching = false;
            this.setStyle();
          }
        },
        deep: true
      },
    },
  }
</script>

<style scoped>

</style>
