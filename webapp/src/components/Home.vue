<template>
    <div class="text-center">
        <div class="display-1">
            Awesome Tires and Mechanic
        </div>
        <br />
        <br />
        <div class="row gx-5 gy-5">
            <div class="col text-end">
                <router-link class="display-6 text-decoration-none text-secondary p-3" to="/create/customer">Add a New Customer</router-link> <!-- Creates a routed link to Add a New Customer -->
            </div>
            <div class="col text-start">
                <router-link class="display-6 text-decoration-none text-secondary p-3" to="/create/service">Create a New Service</router-link> <!-- Creates a routed link to Create a New Event -->
            </div>
        </div>
        <!-- Breaks the div, to create another for visual appeal, as to not crowd all links onto one line. allowing easier UI usage -->
        <br />
        <div class="row gx-5 gy-5">
            <div class="col text-end">
                <router-link class="display-6 text-decoration-none text-secondary p-3" to="/view/customers">View All Customers</router-link> <!-- Creates a routed link to View All Customers -->
            </div>
            <div class="col text-start">
                <router-link class="display-6 text-decoration-none text-secondary p-3" to="/view/services">View All Services</router-link> <!-- Creates a routed link to View All Services -->
            </div>
        </div>
		<br />
		<router-link class="display-6 text-decoration-none text-secondary p-3" to="/email">Send Coupons</router-link>
    </div>
</template>

<script>
    export default {
        name: 'Home',
    }
</script>