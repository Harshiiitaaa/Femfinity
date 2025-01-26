import { createRouter, createWebHistory } from 'vue-router';
import HomePage from './../views/HomePage.vue';
import AboutUs from './../views/AboutUs.vue';
import ContactUs from './../views/ContactUs.vue';
import LoginPage from './../views/LoginPage.vue';
import Community from './../views/Community.vue'

const routes = [
    {
        path: '/',
        name: 'home',
        component: HomePage

    },
    {
        path: '/about',
        name: 'about',
        component: AboutUs
    },
    {
        path: '/contact',
        name: 'contact',
        component: ContactUs
    },
    {
        path: '/login',
        name: 'login',
        component: LoginPage
    },
    {
        path: '/community',
        name: 'community',
        component: Community
    }
]

const router = createRouter({
    history: createWebHistory(),
    routes,
});

export default router;