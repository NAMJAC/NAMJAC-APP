<template>
    <div class="text-center">
        <div class="display-5">
            Add a New Customer
        </div>
        <br />
        <div class="container bg-light">
            <div class="form-group text-start">
                <div class="row">
                    <div class="col">
                        <label class="col-form-label mt-4" for="inputDefault">First Name</label>
                        <input type="text" class="form-control" placeholder="First Name" id="inputDefault" v-model='customer.First_Name' required>
                    </div>
                    <div class="col">
                        <label class="col-form-label mt-4" for="inputDefault">Last Name</label>
                        <input type="text" class="form-control" placeholder="Last Name" id="inputDefault" v-model='customer.Last_Name' required>
                    </div>
                    <div class="col">
                        <label class="col-form-label mt-4" for="inputDefault">Address</label>
                        <input type="text" class="form-control" placeholder="Address" id="inputDefault" v-model='customer.Address' required>
                    </div>
                </div>
                <div class="row">
                    <div class="col">
                        <label class="col-form-label mt-4" for="inputDefault">City</label>
                        <input type="text" class="form-control" placeholder="City" id="inputDefault" v-model='customer.City'>
                    </div>
                    <div class="col">
                        <label class="col-form-label mt-4" for="inputDefault">State</label>
                        <input type="text" class="form-control" placeholder="State" id="inputDefault" v-model='customer.State'>
                    </div>

                    <div class="col">
                        <label class="col-form-label mt-4" for="inputDefault">Zip Code</label>
                        <input type="text" class="form-control" placeholder="Zip Code" id="inputDefault" v-model='customer.zipcode'>
                    </div>
                </div>
				<div class="row">
                    <div class="col">
                        <label class="col-form-label mt-4" for="inputDefault">Phone Number</label>
                        <input type="text" class="form-control" placeholder="Phone Number" id="inputDefault" v-model='customer.Phone_number'>
                    </div>
                    <div class="col">
                        <label class="col-form-label mt-4" for="inputDefault">Email Address</label>
                        <input type="text" class="form-control" placeholder="Email Address" id="inputDefault" v-model='customer.Email'>
                    </div>
                </div>
                <div class="row text-center">
                    <div class="col">
                        <label class="col-form-label mt-4" for="inputDefault">Contact Preference</label><br />
                        <button type="button" class="btn btn-outline-success" v-if="!formvals.conpref" v-on:click="formvals.conpref = true">Phone</button>
                        <button type="button" class="btn btn-outline-success" v-if="formvals.conpref" v-on:click="formvals.conpref = false">Email</button>
                    </div>
                </div>
            </div>
            <div class="text-end mt-4">
                <button class="btn btn-primary" v-on:click="submitForm()">Add</button> <!-- Creating a button for the function of adding the customer profile created -->
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
                customer: {
                    First_Name: '',
                    Last_Name: '',
                    City: '',
                    State: '',
                    Address: '',
					zipcode: 0,
					Phone_number: '',
					Email: '',
					conpref: '',
					creation_date: ''
                },
				
				formvals: {
					conpref: false
				}
            }
        },
        methods: {
            submitForm() {
                let apiURL = config.APIURL + 'customer';
				
				if(this.formvals.conpref) {
					this.customer.conpref = 'Email';
				}
				else {
					this.customer.conpref = 'Phone';
				}
				
				let date = new Date();
				this.customer.creation_date = date.toISOString().split('T')[0];

                axios.post(apiURL, this.customer).then(() => {
				
                    //changing the view to the list, calling from the user entries
                    this.$router.push('/view/customers')
                }).catch(error => { // If an error shall occur, this catches the error and logs it to the console for later reference, if needed
                    console.log(error)
                });
            }
        }

    }
</script>