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
      <template v-for="(link, key) in links">
        <v-list-group v-if="link.child" :value="true" :prepend-icon="link.icon" :key="key">
          <template v-slot:activator>
            <v-list-item-title>{{ link.title }}</v-list-item-title>
          </template>
          <v-list-item
            v-for="(childLink, childKey) in link.child"
            link
            :key="`child-${childKey}`"
            v-model="selectedItem"
            :to="{ name: childLink.to }"
            :class="{ disabled: childLink.disable }"
          >
            <v-list-item-icon>
              <v-icon>{{ childLink.icon }}</v-icon>
            </v-list-item-icon>
            <v-list-item-title>{{ childLink.title }}</v-list-item-title>
          </v-list-item>
        </v-list-group>
        <v-list-item v-else link :key="key" v-model="selectedItem" :to="{ name: link.to }">
          <v-list-item-icon>
            <v-icon>{{ link.icon }}</v-icon>
          </v-list-item-icon>
          <v-list-item-title>{{ link.title }}</v-list-item-title>
        </v-list-item>
      </template>
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
      to: 'ActualProblems',
      icon: 'mdi-alert',
      disable: false
    },
    {
      title: 'Аналитика',
      icon: 'mdi-google-analytics',
      disable: false,
      child: [
        {
          title: 'Инвентаризация',
          to: 'Inventory',
          icon: 'mdi-warehouse',
          disable: true
        },
        {
          title: 'Транспортные транзакции',
          to: 'TransportTransaction',
          icon: 'mdi-truck',
          disable: false
        },
        {
          title: 'Производственные транзакции',
          to: 'ProductionTransaction',
          icon: 'mdi-factory',
          disable: true
        }
      ]
    }
  ];
  isMini = true;
  teamName = 'Ai we can';

  get name(): string {
    return this.isMini ? this.teamName[0] : this.teamName;
  }
}
</script>

<style lang="scss" scoped>
.disabled {
  cursor: auto !important;
}
</style>
