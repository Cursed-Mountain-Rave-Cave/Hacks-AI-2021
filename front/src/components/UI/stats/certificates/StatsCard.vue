<template>
  <v-card class="pa-2" rounded="lg">
    <v-card-text>
      <div>{{ title }}</div>
      <div class="text-h4 text-right text--primary">
        <strong class="text--lighten-1" :class="[stat > 0 ? problemColor : goodColor]">
          <template v-if="isPercent">{{ (stat * 100).toFixed(3) }}%</template>
          <template v-else>{{ stat }}</template>
        </strong>
      </div>
    </v-card-text>
  </v-card>
</template>

<script lang="ts">
import { Component, Prop, Vue } from 'vue-property-decorator';

@Component
export default class StatsCard extends Vue {
  @Prop(String) title!: string;
  @Prop({ type: String, default: 'orange--text' }) problemColor!: string;
  @Prop({ type: String, default: 'green--text' }) goodColor!: string;
  @Prop(Number) stat!: number;
  @Prop({ type: Boolean, default: false }) isPercent!: boolean;
}
</script>
