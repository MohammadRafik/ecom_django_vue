// i should turn this into a compoenent so that it only loads when its being used instead of being loaded on every page
const axios = require('axios').default;
axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.xsrfHeaderName = "X-CSRFTOKEN"

export const vue_slides = {
    data: function () {
      return {
        slides: []
      }
    },
    created: function() {
        // all this function does it fetch the needed data using the api to update slides with the featured products
        // the proper way to do this would be to set up filters on the django rest framework views so that i can just specify what i want in the url request
        self = this
        axios.get('/api/products')
        .then(function(response_products){
          var featured_results = []
          response_products.data.results.forEach(element =>{
            if (element.featured == true){
              featured_results.push(element)
            }
          });
          response_products.data.results = featured_results

            axios.get('/api/productimages')
            .then(function(response_images){
              // relate each product to its image
              response_products.data.results.forEach(element_prod => {
                response_images.data.results.forEach(element_img => {
                  if (element_prod.id == Number(element_img.product.match(/\/[0-9]{1,4}\//g)[0].match(/[0-9]{1,4}/g)[0])){
                    element_prod.img_url = element_img.image_url
                  }
                });
              });
              // now we find the products with featured=true and make an api request to get their url's from django
              response_products.data.results.forEach(element => {
                if (element.featured == true){
                  // so here each element is one of the featured items we need to load into slides, before doing anything we need to get the image urls


                  
                  axios.get('/api/get_url',{
                    params: {
                      app_and_url_name: 'products:product_page',
                      url_arg: element.id
                    }
                  })
                  .then(function(response_url){
                    // now we have url in response_url.data, and everything else in element, so time to fill slides
                    self.slides.push({
                      title: element.title,
                      content: element.description,
                      id: element.id,
                      image: element.img_url,
                      link: response_url.data
                    })
                  })

                }
              });
            })
        })
        .catch(function (error){
            console.log('error with TEH product get request')
            console.log(error)
        })
        .finally(function(){
            
        })

    },
    methods: {

    }
  }



