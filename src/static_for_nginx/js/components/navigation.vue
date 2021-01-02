<template>
    <div>
        <a v-on:click="fetch_categories">click this to get navigation from the api</a>
    </div>
</template>

<script>
const axios = require('axios').default;
export default {
    name: 'navigation',
    data () {
        return {

        }
    },
    methods:{
        fetch_categories: function(){
            axios.get('/api/categories')
                .then(function (response){
                    //runs when the http request is done successfully
                    console.log(response)
                })
                .catch(function (error){
                    //runs when there is an error
                    console.log(error)
                })
                .finally(function(){
                    //this always runs
                })
        },
        
        

    }
}
</script>

<style scoped>

</style>