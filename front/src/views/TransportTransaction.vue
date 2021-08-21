<template>
  <v-container fluid>
    <h2 class="mb-5">Транспортные транзакции</h2>
    <v-row v-if="Object.keys(stats).length > 0">
      <v-col md="3" sm="6" xs="12">
        <stats-card
          title="Количество пользователей, оформивших ВСД"
          problem-color="purple--text"
          :stat="stats.doctors_count"
        />
      </v-col>
      <v-col md="3" sm="6" xs="12">
        <stats-card title="Количество сертификатов" problem-color="purple--text" :stat="stats.certificates_count" />
      </v-col>
      <v-col md="3" sm="6" xs="12">
        <stats-card title="Количество ошибок" problem-color="purple--text" :stat="stats.mistakes_count" />
      </v-col>
      <v-col md="3" sm="6" xs="12">
        <stats-card title="Процент ошибок" problem-color="purple--text" :stat="stats.mistakes_ratio" is-percent />
      </v-col>
    </v-row>
    <v-row>
      <v-col>
        <v-card class="mb-5 pa-2" rounded="lg">
          <v-data-table
            class="transport_transactions"
            :headers="headers"
            :items="certificates"
            @click:row="showDrawer"
          />
        </v-card>
      </v-col>
    </v-row>
    <v-navigation-drawer v-model="drawer" width="550" absolute temporary right>
      <v-row>
        <v-col>
          <v-card elevation="0" class="ma-3 text-center">
            <v-list-item three-line>
              <v-list-item-content>
                <div class="text-overline mb-4">
                  {{ drawerData.cert_request_type }} / {{ drawerData.cert_reqsource_type }} /
                  {{ drawerData.cert_nature_type }}
                </div>
                <v-list-item-title class="text-h5 mb-1"> {{ drawerData.product }} </v-list-item-title>
                <v-list-item-subtitle>{{ drawerData.sub_product }}</v-list-item-subtitle>
              </v-list-item-content>
            </v-list-item>
          </v-card>
        </v-col>
      </v-row>
      <v-divider />
      <v-row>
        <v-col :cols="12">
          <div class="text-center text-overline my-2"> Информация об отправителе и получателе</div>
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
          <div class="text-center text-overline my-2"> Информация об выдаче и погашении сертификата</div>
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
                    <template v-if="drawerData.repaid_cert_date">{{ drawerData.repaid_cert_date }}</template>
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
    </v-navigation-drawer>
  </v-container>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';
import StatsCard from '@/components/UI/stats/certificates/StatsCard.vue';
import { DataService } from '@/service/DataService';
import IHeader from '@/interfaces/IHeader';

@Component({
  components: {
    StatsCard
  }
})
export default class TransportTransaction extends Vue {
  headers: IHeader[] = [
    {
      text: 'Пользователь, оформивший ВСД',
      value: 'doctor'
    },
    {
      text: 'продукт',
      value: 'product'
    },
    {
      text: 'Тип сертификата',
      value: 'cert_type'
    },
    {
      text: 'Статус сертификата',
      value: 'cert_status'
    },
    {
      text: 'Источник сертификата',
      value: 'cert_source'
    },
    {
      text: 'Страна происхождения',
      value: 'origin_country'
    },
    {
      text: 'Страна назначения',
      value: 'recipient_country'
    },
    {
      text: 'Дата оформления ВСД',
      value: 'cert_date'
    },
    {
      text: 'Дата добавления записи в базу Меркурия',
      value: 'cert_insert_date'
    }
  ];
  certificates = [];
  stats = {};
  drawer = false;
  drawerData = {};
  dataService = new DataService();

  async mounted(): Promise<void> {
    await this.dataService.get('certificates', { limit: 2000 }).then((response) => {
      this.certificates = response;
    });

    await this.dataService.get('certificates/stats').then((response) => {
      this.stats = response;
    });
  }

  public showDrawer(data: any): void {
    if (this.drawer) {
      this.drawerData = {};
    } else {
      this.drawerData = data;
    }
    this.drawer = !this.drawer;
  }

  // async expandCertificate(payload: any): Promise<any> {
  //   if (payload.value) {
  //     await this.dataService.get('certificates', { id: payload.item.id }).then((response) => {
  //       this.expanded = response;
  //     });
  //   }
  // }
}
</script>

<style lang="scss" scoped>
.transport_transactions {
  cursor: pointer;
}
</style>
