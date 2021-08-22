import Vue from 'vue';
import VueRouter, { RouteConfig } from 'vue-router';
import Home from '@/views/Home.vue';
import ActualProblems from '@/views/ActualProblems.vue';
import TransportTransaction from '@/views/TransportTransaction.vue';
import ProductionTransaction from '@/views/ProductionTransaction.vue';
import Inventory from '@/views/ProductionTypes.vue';
import Doctor from '@/views/Doctor.vue';

Vue.use(VueRouter);

const routes: Array<RouteConfig> = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/actual_problems',
    name: 'ActualProblems',
    component: ActualProblems,
    meta: {
      class: 'actual_problems'
    }
  },
  {
    path: '/inventory',
    name: 'Inventory',
    component: Inventory,
    meta: {
      class: 'inventory'
    }
  },
  {
    path: '/transport_transaction',
    name: 'TransportTransaction',
    component: TransportTransaction,
    meta: {
      class: 'transport_transaction'
    }
  },
  {
    path: '/production_transaction',
    name: 'ProductionTransaction',
    component: ProductionTransaction,
    meta: {
      class: 'production_transaction'
    }
  },
  {
    path: '/doctor/:id',
    name: 'Doctor',
    component: Doctor
  },
  {
    path: '/repaid_doctor/:id',
    name: 'RepaidDoctor',
    component: Doctor
  }
];

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
});

export default router;
