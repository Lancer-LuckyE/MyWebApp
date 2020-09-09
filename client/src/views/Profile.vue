<template>
    <div>
        <p>Email: {{this.email}}</p>
        <p>User name: {{this.first_name}} {{this.last_name}}</p>
    </div>
</template>

<script>
    export default {
        name: "Profile",
        data() {
            return {
                email : '',
                first_name: '',
                last_name: '',
            }
        },
        mounted() {
            this.readUserInfo();
        },
        methods: {
            readUserInfo() {
                const user = JSON.parse(localStorage.getItem('user'));
                this.email = user['Email'];
                this.first_name = user['First_Name'];
                this.last_name = user['Last_Name'];
            }
        }
    }
</script>

<style scoped>

</style>
