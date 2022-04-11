<template>
	<div class="text-end">
	<button @click="this.$router.push('/create/service')" class="btn btn-primary ms-auto">New Service</button>
	</div>
	<br />
    <div class="row text-center">
        <div class="col-md-12">
            <table class="table table-striped">
                <thead class="table-dark">
                    <tr> <!-- Headers -->
                        <th>Service ID</th>
                        <th>Customer ID</th>
                        <th>Service Name</th>
                        <th>Amount</th>
                        <th>Description</th>
                        <th>Date Initialized</th>
                        <th>Date Completed</th>
						<th></th>
						<th></th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="_service in serviceList" :key="_service.Service_ID">  <!-- Calls the information from the API and puts them as data in the table -->
                        <td>{{ _service.Service_ID }}</td>
                        <td>{{ _service.Cust_ID }}</td>
                        <td>{{ _service.service_name }}</td>
                        <td>{{ _service.service_amount }}</td>
                        <td>{{ _service.service_description }}</td>
                        <td>{{ _service.service_date_init }}</td>
                        <td>{{ _service.service_date_completed }}</td>
						<td>
							<button @click="this.$router.push('/edit/service?id=' + _service.Service_ID)" class="btn btn-warning ms-auto">Edit</button>
						</td>
                        <td>
                            <button @click="delserv(_service.Service_ID)" class="btn btn-danger ms-auto">Delete</button>
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
                serviceList: [],
				contactList: []
            }
        },
        created() {
            axios.get(config.APIURL + 'service').then(res => {
                this.serviceList = res.data;
				this.serviceList.shift();
            }).catch(error => {
                console.log(error)
            });
        },
        methods: {
            delserv(id) {
                console.log(id)
                let apiURL= config.APIURL + 'service/' + id;               

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