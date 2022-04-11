<template>
	<div class="text-end">
	<button @click="this.$router.push('/create/customer')" class="btn btn-primary ms-auto">New Customer</button>
	</div>
	<br />
    <div class="row text-center">
        <div class="col-md-12">
            <table class="table table-striped"> <!-- Creates a table to list the volunteers created -->
                <thead class="table-dark">
                    <tr> <!-- Headers -->
                        <th>Customer ID</th>
                        <th>First Name</th>
                        <th>Last Name</th>
                        <th>Address</th>
                        <th>City</th>
                        <th>State</th>
                        <th>Zip Code</th>
                        <th>Phone Number</th>
                        <th>E-Mail</th>
						<th>Preferred Contact Method</th>
						<th></th>
						<th></th>
						<th></th>
						<th></th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="_customer in customerList" :key="_customer.Cust_ID">  <!-- Calls the information from the API and puts them as data in the table -->
                        <td>{{ _customer.Cust_ID }}</td>
                        <td>{{ _customer.First_Name }}</td>
                        <td>{{ _customer.Last_Name }}</td>
                        <td>{{ _customer.Address }}</td>
                        <td>{{ _customer.City }}</td>
                        <td>{{ _customer.State }}</td>
                        <td>{{ _customer.zipcode }}</td>
                        <td>{{ _customer.Phone_number }}</td>
                        <td>{{ _customer.Email }}</td>
						<td>{{ _customer.conpref }}</td>
						<td>
							<button @click="this.$router.push('/create/service?id=' + _customer.Cust_ID)" class="btn btn-primary ms-auto">Service</button>
						</td>
						<td>
							<button @click="this.$router.push('/email?email=' + _customer.Email)" class="btn btn-success ms-auto">Coupon</button>
						</td>
						<td>
							<button @click="this.$router.push('/edit/customer?id=' + _customer.Cust_ID)" class="btn btn-warning ms-auto">Edit</button>
						</td>
                        <td>
                            <button @click="delcust(_customer.Cust_ID)" class="btn btn-danger ms-auto">Delete</button>
                        </td>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>
</template>

<script>
    import axios from "axios";
	import config from '../config.js';

    export default {
        data() {
            return {
                customerList: [],
				contactList: []
            }
        },
        created() {
            let apiURL = config.APIURL + 'customer';
            axios.get(apiURL).then(res => {
                this.customerList = res.data;
				this.customerList.shift();
            }).catch(error => {
                console.log(error)
            });
        },
        methods: {
            delcust(id) {
                console.log(id)
                let apiURL= config.APIURL + 'customer/' + id;               

                axios.delete(apiURL).then( () => {                    
                    this.$router.go();
                }).catch(error => {
                    console.log(error);
                })
            },
        }
    }
</script>



<style>
    .btn-success {
        margin-right: 10px;
    }
</style>