import Vue from 'vue';
import VueRouter, { RouteConfig } from 'vue-router';
import Home from '@/views/Home.vue';
import ActualProblems from '@/views/ActualProblems.vue';
import Certificates from '@/views/Certificates.vue';
import ProductionTypes from '@/views/ProductionTypes.vue';

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
    path: '/certificates',
    name: 'Certidicates',
    component: Certificates,
    meta: {
      class: 'certificates'
    }
  },
  {
    path: '/production_types',
    name: 'ProductionTypes',
    component: ProductionTypes,
    meta: {
      class: 'production_types'
    }
  }
];

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
});

export default router;
