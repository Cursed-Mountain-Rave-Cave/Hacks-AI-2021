<template>
  <v-container fluid>
    <h2 class="mb-4" v-if="doctorInfo.name">{{ doctorInfo.name }}</h2>
    <v-row>
      <v-col cols="12">
        <v-card class="pa-2" rounded="lg">
          <v-card-title>Количество выданных сертификатов</v-card-title>
          <v-card-text>
            <div id="chartdiv"></div>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
    {{ doctorInfo.mistakes_ratio }}
    {{ doctorInfo.product_mistakes_ratio }}
  </v-container>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';
import { DataService } from '@/service/DataService';
import * as am4core from '@amcharts/amcharts4/core';
import * as am4charts from '@amcharts/amcharts4/charts';
import am4themes_animated from '@amcharts/amcharts4/themes/animated';
import am4themes_material from '@amcharts/amcharts4/themes/material';

@Component
export default class Doctor extends Vue {
  dataService = new DataService();
  doctorInfo = {
    given_certificates: []
  };

  get doctorId(): string {
    return this.$route.params.id;
  }

  get doctorType(): string | null | undefined {
    return this.$route.name;
  }

  mounted(): void {
    this.$nextTick(() => {
      if (this.doctorType) {
        this.dataService
          .get(`certificates/${this.snakeCase(this.doctorType)}_info/${this.doctorId}`)
          .then((response) => {
            this.doctorInfo = response;
            this.renderChart();
          });
      }
    });
  }

  private renderChart() {
    if (this.doctorInfo && this.doctorInfo['given_certificates']) {
      am4core.useTheme(am4themes_animated);
      am4core.useTheme(am4themes_material);
      let chart = am4core.create('chartdiv', am4charts.XYChart);
      chart.logo.disabled = true;
      // Add data
      chart.data = this.doctorInfo['given_certificates'];
      chart.dateFormatter.inputDateFormat = 'yyyy-MM-dd';
      // Create axes
      let dateAxis = chart.xAxes.push(new am4charts.DateAxis());
      let valueAxis = chart.yAxes.push(new am4charts.ValueAxis());
      // Create series
      let series = chart.series.push(new am4charts.LineSeries());
      series.dataFields.valueY = 'count';
      series.dataFields.dateX = 'date';
      series.tooltipText = '{count}';
      series.strokeWidth = 2;
      series.minBulletDistance = 15;
      // Drop-shaped tooltips
      series.tooltip = new am4core.Tooltip();
      series.tooltip.background.cornerRadius = 20;
      series.tooltip.background.strokeOpacity = 0;
      series.tooltip.pointerOrientation = 'vertical';
      series.tooltip.label.minWidth = 40;
      series.tooltip.label.minHeight = 40;
      series.tooltip.label.textAlign = 'middle';
      series.tooltip.label.textValign = 'middle';
      // Make bullets grow on hover
      let bullet = series.bullets.push(new am4charts.CircleBullet());
      bullet.circle.strokeWidth = 2;
      bullet.circle.radius = 4;
      bullet.circle.fill = am4core.color('#fff');
      let bullethover = bullet.states.create('hover');
      bullethover.properties.scale = 1.3;
      // Make a panning cursor
      chart.cursor = new am4charts.XYCursor();
      chart.cursor.behavior = 'panXY';
      chart.cursor.xAxis = dateAxis;
      chart.cursor.snapToSeries = series;
    }
  }

  private snakeCase(text: string) {
    return text.replace(
      /[A-Z]|-./g,
      (char: string, index: number) =>
        `${index > 0 ? '_' : ''}${char.length > 1 ? char.toLowerCase()[1] : char.toLowerCase()}`
    );
  }
}
</script>

<style lang="scss" scoped>
#chartdiv {
  width: 100%;
  height: 300px;
}
</style>
