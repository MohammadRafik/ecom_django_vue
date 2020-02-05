const axios = require('axios').default;
axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.xsrfHeaderName = "X-CSRFTOKEN"

export const base_global = {
    data: function () {
      return {
        category: '',
        product_description: '',
        added_to_cart_successfully: false,
        cart_item_count: 0,
      }
    },
    created: function() {
        // check if there is a saved category in the session
        self = this
        axios.get('/api/session', {
            params: {
                index: 'category'
              }
        })
        .then(function (response){
            //runs when the http request is done successfully
            self.category = response
        })
        .catch(function (error){
            //runs when there is an error
            console.log(error)
        })
        .finally(function(){
            //this always runs
        })


        // update cart_item_count by getting the count from backend
        axios.get('/cart/get_cart_items_count')
        .then(function (response){
            self.cart_item_count = response.data
        })

    },
    methods: {
        update_category: function(category){
            self.category = category
        },
        update_cart_item_count: function(){
            self = this
            axios.get('/cart/get_cart_items_count')
            .then(function (response){
                self.cart_item_count = response.data
            })
        },

        update_cart: function(cart_url, product_url, quantity = 1, updated_by = 'anonymous'){
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
                self.update_cart_item_count()
            })
            .catch(function (error){

            })
            .finally(function(){
                
            })
        },
        delete_item_from_cart: function(cart_item_id){
            axios.delete('/api/cartitem/' + cart_item_id)
            .then(function(response){
                console.log('item deleted from cart')
                console.log(response)
                window.location.reload(true);
            })
            .catch(function (error){
                console.log('error with delete request')
                console.log(error)
            })
            .finally(function(){
                
            })
        },

      
        enter: function(el, done) {
    
            var self = this;
            setTimeout(function() {
                self.added_to_cart_successfully = false
            }, 1500); // hide the message after 1.5 seconds
        },
      

    }
  }



