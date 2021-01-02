<template>
<div id="stripe_checkout">

</div>
</template>

<script>
  export default {
      props: ['stripe_key', 'total_cost'],
    mounted() {
      let stripe_script = document.createElement('script')
      stripe_script.setAttribute('src', 'https://checkout.stripe.com/checkout.js')
      stripe_script.setAttribute('class', 'stripe-button')
      stripe_script.setAttribute('data-key', this.stripe_key)
      stripe_script.setAttribute('data-description', 'Electrone eCommerce store Charge')
      stripe_script.setAttribute('data-amount', this.total_cost)
      stripe_script.setAttribute('data-locale', 'auto')
      stripe_script.setAttribute('data-currency', 'CAD')
      document.getElementById("stripe_checkout").appendChild(stripe_script)
    },
    methods: {
      
    }
  }
</script>