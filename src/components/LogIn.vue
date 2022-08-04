<template>
    <div class="logIn_user">
        <div class="container_logIn_user">
            <h2>Iniciar Sesión</h2>
            <form v-on:submit.prevent="processlogInUser">
                <input type="text" v-model = "user.username" placeholdername="Username">
                <br>
                <input type="password" v-model = "user.password" placeholdername="Password">
                <br>
                <button type="submit">Iniciar Sesión</button>
            </form>
        </div>
    </div>
</template>

<script>
    import axios from 'axios'
    export default {
        name: "LogIn",

        data: function () {
            return {
                user: {
                    username: "",
                    password: ""
                }
            }
        },

        methods: {
            processlogInUser: function () {
                axios.post(
                    "https://misiontic-bank-db-c3g3p2.herokuapp.com/user/logIn/",
                    this.user,
                    {headers:{}}
                    ).then((result) => {
                    let dataLogin = {
                        username: this.user.username,
                        token_access: result.data.access,
                        token_refresh: result.data.refresh,
                    }
                    this.$emit('completedLogIn', dataLogin)
                    })
                    .catch((error)=>{
                    if(error.response.status == "401")
                        alert("ERROR 401: Credenciales Incorrectas.");
                })
        }
    }

    }

</script>

<style>
    .logIn_user{
        margin: 0px;
        padding: 0px;
        height: 100%;
        width: 100%;

        display: flex;
        justify-content: center;
        align-items: center;

    }

    .container_logIn_user{
        border: 3px solid #283747;
        border-radius: 10px;
        width: 25%;
        height: 60%;

        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
    }

    .logIn_user h2{
        color:#283747;
    }

    .logIn_user form{
        width:70%;
    }

    .logIn_user input{
        height: 40px;
        width: 100%;

        box-sizing: border-box;
        padding: 10px 20px;
        margin: 5px 0;

        border: 1px solid #283747;
    }

    .logIn_user button{
        width: 100%;
        height: 40px;
        color: #e5e7e9;
        background: #283747;
        border: 1px solid #e5e7e9;
        border-radius: 5px;
        padding: 10px 25px;
        margin: 5px 0;
    }
    .logIn_user button:hover{
        color: #e5e7e9;
        background: crimson;
        border: 1px solid crimson;
    }
</style>