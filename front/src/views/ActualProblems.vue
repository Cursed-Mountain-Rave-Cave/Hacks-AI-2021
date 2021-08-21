<template>
  <v-container fluid>
    <h2 class="mb-5">Актуальные проблемы</h2>
    <v-row>
      <v-col cols="12" sm="12" md="4">
        <v-card class="pa-2" rounded="lg">
          <v-card-text>
            <div>Всего проблем</div>
            <div class="text-h2 text-right text--primary">
              <strong
                class="text--lighten-1"
                :class="{ 'orange--text': problemsLength > 0, 'green--text': problemsLength === 0 }"
              >
                {{ problemsLength }}
              </strong>
            </div>
          </v-card-text>
          <v-card-actions>
            <v-btn text @click="search = ''"> Показать </v-btn>
          </v-card-actions>
        </v-card>
      </v-col>
      <v-col cols="12" sm="12" md="4">
        <v-card class="pa-2" rounded="lg">
          <v-card-text>
            <div>Проблем с сертификатами</div>
            <div class="text-h2 text-right text--primary">
              <strong
                class="text--lighten-1"
                :class="{ 'orange--text': certProblems > 0, 'green--text': certProblems === 0 }"
              >
                {{ certProblems }}
              </strong>
            </div>
          </v-card-text>
          <v-card-actions>
            <v-btn text @click="search = 'сертификат'"> Показать </v-btn>
          </v-card-actions>
        </v-card>
      </v-col>
      <v-col cols="12" sm="12" md="4">
        <v-card class="pa-2" rounded="lg">
          <v-card-text>
            <div>Проблем с транзакциями</div>
            <div class="text-h2 text-right text--primary">
              <strong
                class="text--lighten-1"
                :class="{ 'orange--text': transactionProblems > 0, 'green--text': transactionProblems === 0 }"
              >
                {{ problems.filter((problem) => problem.type === 'транзакция').length }}
              </strong>
            </div>
          </v-card-text>
          <v-card-actions>
            <v-btn text @click="search = 'транзакция'"> Показать </v-btn>
          </v-card-actions>
        </v-card>
      </v-col>
    </v-row>
    <v-row class="mb-5">
      <v-col>
        <v-card class="pa-2" rounded="lg">
          <v-data-table :headers="headers" :items="problems" :search="search">
            <template v-slot:top>
              <v-text-field v-model="search" label="Поиск" class="mx-4"></v-text-field>
            </template>
            <template v-slot:body="{ items }">
              <tbody>
                <tr v-for="item in items" :key="item.id">
                  <td>{{ item.id }}</td>
                  <td>{{ item.type }}</td>
                  <td>{{ item.reason }}</td>
                  <td>{{ item.kind }}</td>
                  <td>{{ item.company }}</td>
                  <td>{{ item.date }}</td>
                </tr>
              </tbody>
            </template>
          </v-data-table>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';
import { DataService } from '@/service/DataService';
import IHeader from '@/interfaces/IHeader';

@Component
export default class ActualProblems extends Vue {
  search = '';
  headers: IHeader[] = [
    { text: 'Идентификатор', value: 'id' },
    { text: 'Тип ошибки', value: 'type' },
    { text: 'Причина', value: 'reason' },
    { text: 'Вид нарушения', value: 'kind' },
    { text: 'Компания', value: 'company' },
    { text: 'Дата обнаружения', value: 'date' }
  ];
  problems = [
    {
      id: '0',
      type: 'сертификат',
      reason: 'Причина',
      kind: 'вид нарушения',
      company: 'компания',
      date: '2020-08-21'
    },
    {
      id: '1',
      type: 'сертификат',
      reason: 'Причина',
      kind: 'вид нарушения',
      company: 'компания',
      date: '2020-08-21'
    },
    {
      id: '2',
      type: 'транзакция',
      reason: 'Причина',
      kind: 'вид нарушения',
      company: 'компания',
      date: '2020-08-21'
    },
    {
      id: '3',
      type: 'транзакция',
      reason: 'Причина',
      kind: 'вид нарушения',
      company: 'компания',
      date: '2020-08-21'
    },
    {
      id: '4',
      type: 'сертификат',
      reason: 'Причина',
      kind: 'вид нарушения',
      company: 'компания',
      date: '2020-08-21'
    },
    {
      id: '5',
      type: 'транзакция',
      reason: 'Причина',
      kind: 'вид нарушения',
      company: 'компания',
      date: '2020-08-21'
    }
  ];

  dataService = new DataService();

  // async mounted(): Promise<void> {
  //   await this.dataService.get('/actual_problems').then((response) => {
  //     console.log(response);
  //   });
  // }

  get certProblems(): number {
    return this.problems.filter((problem) => problem.type === 'сертификат').length || 0;
  }

  get transactionProblems(): number {
    return this.problems.filter((problem) => problem.type === 'транзакция').length || 0;
  }

  get problemsLength(): number {
    return this.problems.length || 0;
  }
}
</script>
