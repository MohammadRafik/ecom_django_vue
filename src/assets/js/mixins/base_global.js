const axios = require('axios').default;
axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.xsrfHeaderName = "X-CSRFTOKEN"

export const base_global = {
    data: function () {
      return {
        category: '',
        product_description: '',
        added_to_cart_successfully: false
      }
    },
    created: function() {
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
            self.category = response
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
            self.category = category
        },

        update_cart: function(cart_url, product_url, quantity = 1, updated_by = 'anonymous'){
            console.log('making an axios post request')
            let self= this;
            axios.post('/api/cartitem/', {

                cart: cart_url,
                product: product_url,
                quantity: quantity,
                updated_by: updated_by,
                created_by: updated_by
            })
            .then(function(response){
                console.log('axios post request succesful')
                self.added_to_cart_successfully = true
            })
            .catch(function (error){

            })
            .finally(function(){
                
            })
        },
    }
  }