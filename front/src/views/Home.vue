<template>
  <v-container fluid>
    <v-row>
      <v-col cols="12">
        <v-card class="pa-2" rounded="lg">
          <v-card-text>
            <div> {{ main.additional }}</div>
            <p class="text-h5 text--primary"> {{ main.title }} </p>
            <div class="text--primary"> {{ main.description }} </div>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
    <v-row>
      <v-col v-for="(card, key) in cards" sm="12" md="6" lg="4" :key="key">
        <v-card class="pa-2" rounded="lg" :color="card.color" :class="card.class">
          <v-card-text>
            <p class="text-h5 text--primary"> {{ card.title }} </p>
            <div class="text--primary"> {{ card.description }} </div>
          </v-card-text>
          <v-card-actions>
            <v-btn class="ml-2 mt-3" text link :to="card.to"> Перейти </v-btn>
          </v-card-actions>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';
import { ICase, ICard } from '@/interfaces/IInfo';

@Component
export default class Home extends Vue {
  main: ICase = {
    additional: 'Ai we can',
    title: 'Кейс',
    description:
      'Выявление аномальных транзакций и нетипичного поведения хозяйствующего субъекта при осуществлении деятельности в сфере оборота продукции животного происхождения посредством анализа производственных, транспортных и технических транзакций с целью достижения взрывного роста производительности мониторинговых групп, выявления до 100% нарушений и поиска неучтенных сценариев и прихнаков нарушения'
  };
  cards: ICard[] = [
    {
      title: 'Актуальные проблемы',
      description: 'Распознанные проблемы с транзакциями и сертификатами',
      color: '#FFCC80',
      class: 'actual_problems',
      to: 'actual_problems'
    },
    {
      title: 'Инвентаризация',
      description: 'Информация по инвентаризации',
      color: '#A5D6A7',
      class: 'inventory',
      to: 'inventory'
    },
    {
      title: 'Транспортные транзакции',
      description: 'Информация по транспортным транзакциям',
      color: '#B39DDB',
      class: 'transport_transaction',
      to: 'transport_transaction'
    },
    {
      title: 'Производственные транзакции',
      description: 'Информация по производственным транзакциям',
      color: '#B39DDB',
      class: 'production_transaction',
      to: 'production_transaction'
    }
  ];
}
</script>
