<template>
  <v-navigation-drawer app permanent expand-on-hover :mini-variant.sync="isMini" elevation="8">
    <v-list>
      <v-list-item class="px-2">
        <v-list-item-avatar>
          <v-img src="@/assets/img/logo.png" />
        </v-list-item-avatar>
      </v-list-item>

      <v-list-item link to="/">
        <v-list-item-content>
          <v-list-item-title class="text-h6" :class="{ 'text-center': isMini }">{{ name }}</v-list-item-title>
        </v-list-item-content>
      </v-list-item>
    </v-list>

    <v-divider></v-divider>

    <v-list nav dense>
      <v-list-item link v-for="(link, key) in links" :key="key" v-model="selectedItem" :to="link.to">
        <v-list-item-icon>
          <v-icon>{{ link.icon }}</v-icon>
        </v-list-item-icon>
        <v-list-item-title>{{ link.title }}</v-list-item-title>
      </v-list-item>
    </v-list>
  </v-navigation-drawer>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';

import ILink from '@/interfaces/ILink';

@Component
export default class AiwcNavigation extends Vue {
  selectedItem = 0;
  links: ILink[] = [
    {
      title: 'Актуальные проблемы',
      to: 'actual_problems',
      icon: 'mdi-alert'
    },
    {
      title: 'Типы продукции',
      to: 'production_types',
      icon: 'mdi-food-variant'
    },
    {
      title: 'Сертификаты',
      to: 'certificates',
      icon: 'mdi-certificate'
    }
  ];
  isMini = true;
  teamName = 'Ai we can';

  get name(): string {
    return this.isMini ? this.teamName[0] : this.teamName;
  }
}
</script>
