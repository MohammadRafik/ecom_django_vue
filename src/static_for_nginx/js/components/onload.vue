<template>
    <span></span>
</template>

<script>
export default {
    props: [],
    created: function () {
        this.load();
    },
    methods: {
        load() {
            this.$emit('load')
        }
    }
}
</script>