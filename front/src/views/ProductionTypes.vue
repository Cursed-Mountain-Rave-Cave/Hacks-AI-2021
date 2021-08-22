<template>
  <v-container fluid>
    <h2></h2>
    <v-card class="pa-2" rounded="lg"> </v-card>
  </v-container>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';

@Component
export default class ProductionTypes extends Vue {
  desserts = [
    {
      name: 'Frozen Yogurt',
      calories: 159
    },
    {
      name: 'Ice cream sandwich',
      calories: 237
    },
    {
      name: 'Eclair',
      calories: 262
    },
    {
      name: 'Cupcake',
      calories: 305
    },
    {
      name: 'Gingerbread',
      calories: 356
    },
    {
      name: 'Jelly bean',
      calories: 375
    },
    {
      name: 'Lollipop',
      calories: 392
    },
    {
      name: 'Honeycomb',
      calories: 408
    },
    {
      name: 'Donut',
      calories: 452
    },
    {
      name: 'KitKat',
      calories: 518
    }
  ];
}
</script>
