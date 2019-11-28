<template>
    <div>
        <slot></slot>
    </div>
</template>

<script>
export default {
    name: 'tools',
    data () {
        return {
            filters:{
                category: '',
            }
        }
    },
    methods:{
        update_category: function(category){
            this.category = category
        }
    }
}
</script>