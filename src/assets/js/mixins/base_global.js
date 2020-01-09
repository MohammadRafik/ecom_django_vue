const axios = require('axios').default;

export const base_global = {
    data: function() {
      return {
        category: ''
      }
    },
    created: function(){
        console.log('this is mixin')
        // check if there is a saved category in the session
        axios.get('/api/session', {
            params: {
                index: 'category'
              }
        })
        .then(function (response){
            //runs when the http request is done successfully
            console.log(response)
            this.category = response
        })
        .catch(function (error){
            //runs when there is an error
            console.log(error)
        })
        .finally(function(){
            //this always runs
        })
    },
    methods: {
        update_category: function(category){
            this.category = category
        },

        update_cart: function(){
            axios.post('/?????????????')
            .then(function(response){

            })
            .catch(function (error){

            })
            .finally(function(){
                
            })
        }
    }
  }