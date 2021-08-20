<template>
  <v-app>
    <aiwc-navigation />
    <v-main app :class="$route.meta.class">
      <router-view />
    </v-main>
  </v-app>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';
import AiwcNavigation from '@/components/UI/AiwcNavigation.vue';

@Component({
  components: {
    AiwcNavigation
  }
})
export default class App extends Vue {}
</script>

<style lang="scss">
@import '@/assets/sass/main.scss';
</style>
