import { createRouter, createWebHistory } from "vue-router";

import DatabasePage from "../views/DatabasePage.vue";
import HomePage from "../views/HomePage.vue";
import AnalysisPage from "../views/AnalysisPage.vue";
import StatisticsPage from '../views/StatisticsPage.vue'

const routes = [
    {
        path:'/',
        name: 'Home',
        component:HomePage
    },
    {
        path:'/statistics',
        name: 'Statistics',
        component:StatisticsPage
    },
    {
        path:'/database',
        name: 'Database',
        component:DatabasePage
    },
    {
        path:'/analysis',
        name: 'Analysis',
        component:AnalysisPage
    }
];

const router = createRouter({
    history:createWebHistory(process.env.BASE_URL),
    routes
})

export default router
