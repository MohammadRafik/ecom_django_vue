const axios = require('axios').default;
axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.xsrfHeaderName = "X-CSRFTOKEN"

export const vue_slides = {
    data: function () {
      return {
        pauseOnHover: true,
        autoPlaying: true,
        internalAutoPlaying: true,
        slides: []
      }
    },
    created: function() {
        console.log('hello this is the vue_slides_data_loader')
        // self = this
        // axios.get('/api/products/?featured=True')
        // .then(function(response){
        //     console.log('making get request to products that are featured')
        //     console.log(response)
        //     // now we get the image url's
        //     axios.get('/api/productimages')
        //     .then(function(response){
        //         console.log('got product image urls, ALL OF THEM D:')
        //         console.log(response)
        //     })
        //     // so i need title:title, content:description, image:, link:, 
        //     // well i just relized i need to get those links from the RENDERED DJANGO TEMPLAE!








        // })
        // .catch(function (error){
        //     console.log('error with product get request')
        //     console.log(error)
        // })
        // .finally(function(){
            
        // })

    },
    methods: {
        load_data_into_slides: function(link, url, title, id){
            console.log('running load_data_into_slides')
            this.slides.push({
                // title: title,
                // content: description,
                id: id,
                image: '/media/' + url,
                link: link
            })
        },
    }
  }



