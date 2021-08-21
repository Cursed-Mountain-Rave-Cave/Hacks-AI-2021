<template>
  <v-container fluid>
    <h2 class="mb-5">Сертификаты</h2>
    <v-card class="mb-5 pa-2" rounded="lg">
      <v-data-table
        :single-expand="true"
        :headers="headers"
        :items="certificates"
        :expanded.sync="expanded"
        show-expand
      >
        <template v-slot:expanded-item="{ headers, item }">
          <div :colspan="headers.length"> {{ item.product_name }} </div>
          <div :colspan="headers.length"> {{ item.product_type }} </div>
          <div :colspan="headers.length"> {{ item.base_unit }} </div>
          <div :colspan="headers.length"> {{ item.base_weight }} </div>
          <div :colspan="headers.length"> {{ item.canceled_cert_date }} </div>
          <div :colspan="headers.length"> {{ item.canceled_doctor }} </div>
          <div :colspan="headers.length"> {{ item.cert_nature_type }} </div>
          <div :colspan="headers.length"> {{ item.cert_protected }} </div>
          <div :colspan="headers.length"> {{ item.cert_reqsource_type }} </div>
          <div :colspan="headers.length"> {{ item.cert_request_type }} </div>
          <div :colspan="headers.length"> {{ item.cert_source }} </div>
          <div :colspan="headers.length"> {{ item.cert_status }} </div>
          <div :colspan="headers.length"> {{ item.cert_type }} </div>
          <div :colspan="headers.length"> {{ item.cert_vetform }} </div>
          <div :colspan="headers.length"> {{ item.consignee_be }} </div>
          <div :colspan="headers.length"> {{ item.consignee_be_region }} </div>
          <div :colspan="headers.length"> {{ item.consignee_be_sub_region }} </div>
          <div :colspan="headers.length"> {{ item.consignee_ent }} </div>
          <div :colspan="headers.length"> {{ item.consignee_ent_region }} </div>
          <div :colspan="headers.length"> {{ item.consignee_ent_sub_region }} </div>
          <div :colspan="headers.length"> {{ item.consignor_be }} </div>
          <div :colspan="headers.length"> {{ item.consignor_be_region }} </div>
          <div :colspan="headers.length"> {{ item.consignor_be_sub_region }} </div>
          <div :colspan="headers.length"> {{ item.consignor_ent }} </div>
          <div :colspan="headers.length"> {{ item.consignor_ent_region }} </div>
          <div :colspan="headers.length"> {{ item.consignor_ent_sub_region }} </div>
          <div :colspan="headers.length"> {{ item.milk_attr_density_max }} </div>
          <div :colspan="headers.length"> {{ item.milk_attr_density_min }} </div>
          <div :colspan="headers.length"> {{ item.milk_attr_density_type }} </div>
          <div :colspan="headers.length"> {{ item.milk_attr_fat_max }} </div>
          <div :colspan="headers.length"> {{ item.milk_attr_fat_min }} </div>
          <div :colspan="headers.length"> {{ item.milk_attr_fat_type }} </div>
          <div :colspan="headers.length"> {{ item.milk_attr_protein_max }} </div>
          <div :colspan="headers.length"> {{ item.milk_attr_protein_min }} </div>
          <div :colspan="headers.length"> {{ item.milk_attr_protein_type }} </div>
          <div :colspan="headers.length"> {{ item.product }} </div>
          <div :colspan="headers.length"> {{ item.protocol_version }} </div>
          <div :colspan="headers.length"> {{ item.repaid_cert_date }} </div>
          <div :colspan="headers.length"> {{ item.repaid_doctor }} </div>
          <div :colspan="headers.length"> {{ item.sub_product }} </div>
          <div :colspan="headers.length"> {{ item.transfer_type }} </div>
          <div :colspan="headers.length"> {{ item.transit_time_hour }} </div>
          <div :colspan="headers.length"> {{ item.unit }} </div>
          <div :colspan="headers.length"> {{ item.unit_guid }} </div>
          <div :colspan="headers.length"> {{ item.vetExpertise }} </div>
        </template>
      </v-data-table>
    </v-card>
  </v-container>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';
import { DataService } from '@/service/DataService';
import IHeader from '@/interfaces/IHeader';

@Component
export default class Certificates extends Vue {
  headers: IHeader[] = [
    {
      text: 'Пользователь, оформивший ВСД',
      value: 'doctor'
    },
    {
      text: 'Тип пользователя, оформившего ВСД',
      value: 'former_id'
    },
    {
      text: 'Источник сертификата',
      value: 'cert_source'
    },
    {
      text: 'Статус сертификата',
      value: 'cert_status'
    },
    {
      text: 'Тип сертификата',
      value: 'cert_type'
    },
    {
      text: 'Страна происхождения',
      value: 'OriginCountry'
    },
    {
      text: 'Страна назначения',
      value: 'RecipientCountry'
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
  expanded = [];
  dataService = new DataService();

  async mounted(): Promise<void> {
    await this.dataService.get('certificates').then((response) => {
      this.certificates = response;
    });
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
