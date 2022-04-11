<template>
    <div class="text-center">
        <div class="display-5">
            Update Service
        </div>
        <br />
        <div class="container bg-light">
            <div class="form-group text-start">
                <div class="row">
                    <div class="col">
                        <label class="col-form-label mt-4" for="inputDefault">Customer ID</label>
                        <input type="text" class="form-control" placeholder="Customer ID" id="inputDefault" v-model='service.Cust_ID' required>
                    </div>
                    <div class="col">
                        <label class="col-form-label mt-4" for="inputDefault">Service Name</label>
                        <input type="text" class="form-control" placeholder="Service Name" id="inputDefault" v-model='service.service_name' required>
                    </div>
                    <div class="col">
                        <label class="col-form-label mt-4" for="inputDefault">Amount</label>
                        <input type="text" class="form-control" placeholder="Amount" id="inputDefault" v-model='service.service_amount' required>
                    </div>
                </div>
                <div class="row">
                    <div class="col">
                        <label class="col-form-label mt-4" for="inputDefault">Description</label>
                        <input type="text" class="form-control" placeholder="Description" id="inputDefault" v-model='service.service_description'>
                    </div>
                    <div class="col">
                        <label class="col-form-label mt-4" for="inputDefault">Date Initiated</label>
                        <input type="text" class="form-control" placeholder="Date Initiated" id="inputDefault" v-model='service.service_date_init'>
                    </div>
                    <div class="col">
                        <label class="col-form-label mt-4" for="inputDefault">Date Completed</label>
                        <input type="text" class="form-control" placeholder="Date Completed" id="inputDefault" v-model='service.service_date_completed'>
                    </div>
                </div>
            </div>
            <div class="text-end mt-4">
                <button class="btn btn-primary" v-on:click="submitForm()">Add</button> <!-- Creating a button for the function of adding the service profile created -->
            </div>
        </div>
    </div>
</template>

<script>
    import axios from "axios";
	import config from '../config.js';

    export default {
        data() {
            return {
                // Setting the default values to nothing for a clear user entry, when it occurs
				
                service: {
                    Cust_ID: 0,
					service_name: '',
					service_amount: 0,
					service_description: '',
					service_date_init: '',
					service_date_completed: ''
                }
            }
        },
		created() {
		
			let apiURL = config.APIURL + 'service/' + this.$route.query.id;
			console.log(this.$route.query.id);
            axios.get(apiURL).then(res => {
                this.service = res.data[0];
            }).catch(error => {
                console.log(error)
            });
		
        },
        methods: {
            submitForm() {
                let apiURL = 'http://172.26.54.26:5000/service';

                axios.post(apiURL, this.service).then(() => {
				
                    //changing the view to the list, calling from the user entries
                    this.$router.push('/view/services')
                }).catch(error => { // If an error shall occur, this catches the error and logs it to the console for later reference, if needed
                    console.log(error)
                });
            }
        }

    }
</script>