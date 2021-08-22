<template>
  <v-container fluid>
    <v-progress-linear :active="loading" indeterminate color="orange darken-2"></v-progress-linear>
    <h2 class="mb-5">Актуальные проблемы</h2>
    <!-- <v-row>
      <v-col cols="12" sm="12" md="4">
        <v-card class="pa-2" rounded="lg">
          <v-card-text>
            <div>Всего проблем</div>
            <div class="text-h4 text-right text--primary">
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
            <div class="text-h4 text-right text--primary">
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
            <div class="text-h4 text-right text--primary">
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
    </v-row> -->
    <v-row class="mb-5">
      <v-col>
        <v-card class="pa-2" rounded="lg">
          <v-data-table
            class="actual_problem"
            :headers="headers"
            :items="problems"
            :search="search"
            @click:row="showDrawer"
          >
            <template v-slot:top>
              <v-text-field v-model="search" label="Поиск" class="mx-4"></v-text-field>
            </template>
          </v-data-table>
        </v-card>
      </v-col>
    </v-row>
    <v-navigation-drawer v-model="drawer" width="550" absolute temporary right>
      <v-progress-linear :active="loading" indeterminate color="orange darken-2"></v-progress-linear>
      <v-row>
        <v-col>
          <v-card elevation="0" class="ma-1 text-center">
            <v-list-item three-line>
              <v-list-item-content>
                <div class="text-overline mb-4">
                  {{ drawerData.cert_request_type }} / {{ drawerData.cert_reqsource_type }} /
                  {{ drawerData.cert_nature_type }}
                </div>
                <v-list-item-title class="text-h5"> {{ drawerData.product }} </v-list-item-title>
                <v-list-item-subtitle>{{ drawerData.sub_product }}</v-list-item-subtitle>
              </v-list-item-content>
            </v-list-item>
          </v-card>
        </v-col>
      </v-row>
      <v-divider />
      <v-row>
        <v-col :cols="12">
          <div class="text-center text-overline"> Информация об отправителе и получателе</div>
        </v-col>
        <v-col :cols="6">
          <v-card class="mx-2 text-center" elevation="0">
            <v-list two-line>
              <v-list-item>
                <v-list-item-content>
                  <v-list-item-title>{{ drawerData.consignor_be_id }}</v-list-item-title>
                  <v-list-item-subtitle>ХС-отправитель</v-list-item-subtitle>
                </v-list-item-content>
              </v-list-item>
              <v-list-item>
                <v-list-item-content>
                  <v-list-item-title>{{ drawerData.consignor_ent_id }}</v-list-item-title>
                  <v-list-item-subtitle>Предприятие-отправитель</v-list-item-subtitle>
                </v-list-item-content>
              </v-list-item>
            </v-list>
          </v-card>
        </v-col>
        <v-col :cols="6">
          <v-card class="mx-2 text-center" elevation="0">
            <v-list two-line>
              <v-list-item>
                <v-list-item-content>
                  <v-list-item-title>{{ drawerData.consignee_be_id }}</v-list-item-title>
                  <v-list-item-subtitle>ХС-получатель</v-list-item-subtitle>
                </v-list-item-content>
              </v-list-item>
              <v-list-item>
                <v-list-item-content>
                  <v-list-item-title>{{ drawerData.consignee_ent_id }}</v-list-item-title>
                  <v-list-item-subtitle>Предприятие-получатель</v-list-item-subtitle>
                </v-list-item-content>
              </v-list-item>
            </v-list>
          </v-card>
        </v-col>
      </v-row>
      <v-divider />
      <v-row>
        <v-col :cols="12">
          <div class="text-center text-overline"> Информация об выдаче и погашении сертификата</div>
        </v-col>
        <v-col :cols="6">
          <v-card class="mx-4" elevation="0">
            <v-list two-line>
              <v-list-item>
                <v-list-item-content>
                  <v-list-item-title>{{ drawerData.doctor }}</v-list-item-title>
                  <v-list-item-subtitle>Выдал сертификат</v-list-item-subtitle>
                  <v-list-item-subtitle>{{ drawerData.former }}</v-list-item-subtitle>
                  <v-list-item-subtitle>Дата выдачи: {{ drawerData.cert_date }}</v-list-item-subtitle>
                </v-list-item-content>
              </v-list-item>
            </v-list>
            <v-card-actions>
              <v-btn link :to="{ name: 'Doctor', params: { id: drawerData.doctor_id } }"> Перейти </v-btn>
            </v-card-actions>
          </v-card>
        </v-col>
        <v-col :cols="6">
          <v-card class="mx-2" elevation="0">
            <v-list two-line>
              <v-list-item>
                <v-list-item-content>
                  <v-list-item-title>{{ drawerData.repaid_doctor }}</v-list-item-title>
                  <v-list-item-subtitle>Погасил сертификат</v-list-item-subtitle>
                  <v-list-item-subtitle>
                    Дата погашения:
                    <template v-if="drawerData.repaid_doctor_id > -1">{{ drawerData.repaid_cert_date }}</template>
                    <template v-else> Сертификат не погашен </template>
                  </v-list-item-subtitle>
                </v-list-item-content>
              </v-list-item>
            </v-list>
            <v-card-actions>
              <v-btn
                link
                :disabled="drawerData.repaid_doctor_id === -1"
                :to="{ name: 'RepaidDoctor', params: { id: drawerData.repaid_doctor_id } }"
              >
                Перейти
              </v-btn>
            </v-card-actions>
          </v-card>
        </v-col>
      </v-row>
      <v-divider />
      <v-row class="my-2 text-center">
        <v-col class="text-center" cols="12">
          <v-btn color="error mr-2"> Отказать </v-btn>
          <v-btn color="success"> Принять </v-btn>
        </v-col>
      </v-row>
    </v-navigation-drawer>
  </v-container>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';
import { DataService } from '@/service/DataService';
import IHeader from '@/interfaces/IHeader';

@Component
export default class ActualProblems extends Vue {
  search = '';
  drawer = false;
  drawerData = {};
  loading = true;
  headers: IHeader[] = [
    { text: 'Идентификатор', value: 'certificate_id' },
    { text: 'Score', value: 'score' },
    { text: 'Причина нарушения', value: 'score_violation_type' },
    { text: 'Дата обнаружения', value: 'score_date' }
  ];
  problems = [];

  dataService = new DataService();

  async mounted(): Promise<void> {
    this.loading = true;
    await this.dataService.get('scoring').then((response) => {
      this.problems = response;
    });
    this.loading = false;
  }

  public showDrawer(item: any): void {
    this.loading = true;
    this.drawerData = {};
    this.drawer = true;
    this.dataService.get(`certificates/${item.certificate_id}`).then((response) => {
      this.drawerData = response;
    });
    this.loading = false;
  }
}
</script>

<style lang="scss" scoped>
.actual_problem {
  cursor: pointer;
}
</style>
