import {createRouter, createWebHistory } from 'vue-router'
import Home from '../components/Home.vue'

const routes = [ // Creating routes to the different pages
    {
        // Creates the Home path as default path
        path: '/',
        name: 'Home',
        component: Home
    },
    {
        // Creates the Create Customer path
        path: '/create/customer',
        name: 'CreateCustomer',
        component: () => import('../components/CreateCustomer')
    },
    {
        // Creates the Customer List path
        path: '/view/customers',
        name: 'ViewCustomers',
        component: () => import('../components/ViewCustomers')
    },
	{
        // Creates the Edit Customer path
        path: '/edit/customer',
        name: 'EditCustomer',
        component: () => import('../components/EditCustomer')
    },
    {
        // Creates the Create Service path
        path: '/create/service',
        name: 'CreateService',
        component: () => import('../components/CreateService')
    },
    {
        // Creates the Service List path
        path: '/view/services',
        name: 'ViewServices',
        component: () => import('../components/ViewServices')
    },
	{
        // Creates the Edit Customer path
        path: '/edit/service',
        name: 'EditService',
        component: () => import('../components/EditService')
    },
	{
        // Creates the About path
        path: '/about',
        name: 'About',
        component: () => import('../components/About')
    },
    {
        // Creates the Edit Event path
        path: '/about/manuals',
        name: 'Manuals',
        component: () => import('../components/Manual')
    },
    {
        // Creates the Edit Event path
        path: '/email',
        name: 'Email',
        component: () => import('../components/EmailPage')
    },
	{
		// Creates the Edit Event path
        path: '/reports',
        name: 'Reports',
        component: () => import('../components/Reports')
	}
]



const router = createRouter({
    history: createWebHistory(process.env.BASE_URL), routes
})

export default router