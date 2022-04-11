<template>
	<div class="display-5 text-center">
        Reports
    </div>
    <br />
	<div>
        <div class="container bg-light">
			<div class="row">
				<div class="col">
					<label class="col-form-label mt-4" for="inputDefault">Total Customers</label>
					<input type="text" class="form-control" id="inputDefault" v-model='report.Customers' readonly>
				</div>
				<div class="col">
					<label class="col-form-label mt-4" for="inputDefault">Total Services</label>
					<input type="text" class="form-control" id="inputDefault" v-model='report.Services' readonly>
				</div>
				<div class="col">
					<label class="col-form-label mt-4" for="inputDefault">Average Services Per Customer</label>
					<input type="text" class="form-control" id="inputDefault" v-model='report.avgSPC' readonly>
				</div>
			</div>
			<div class="row">
				<div class="col">
					<label class="col-form-label mt-4" for="inputDefault">New Customers Past Month</label>
					<input type="text" class="form-control" id="inputDefault" v-model='report.NewCust' readonly>
				</div>
				<div class="col">
					<label class="col-form-label mt-4" for="inputDefault">New Services Past Month</label>
					<input type="text" class="form-control" id="inputDefault" v-model='report.NewServ' readonly>
				</div>
				<div class="col">
					<label class="col-form-label mt-4" for="inputDefault">Coupons Sent</label>
					<input type="text" class="form-control" id="inputDefault" v-model='report.Coupons' readonly>
				</div>
			</div>
			<div class="row mt-4 text-end">
				<div class="col">
					<button class="btn btn-primary" v-on:click="SaveLog()">Save</button>
				</div>
			</div>
		</div>
	</div>
	<br />
	<br />
	<div class="row text-center">
        <div class="col-md-12">
            <table class="table table-striped">
                <thead class="table-dark">
                    <tr> <!-- Headers -->
                        <th>Report ID</th>
                        <th>Total Customers</th>
                        <th>Total Services</th>
                        <th>Average Services Per Customer</th>
                        <th>New Customers Past Month</th>
                        <th>New Services Past Month</th>
                        <th>Coupons Sent</th>
						<th>Date</th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="_report in reportlist" :key="_report.Report_ID">  <!-- Calls the information from the API and puts them as data in the table -->
                        <td>{{ _report.Report_ID }}</td>
                        <td>{{ _report.Customers }}</td>
                        <td>{{ _report.Services }}</td>
                        <td>{{ _report.avgSPC }}</td>
                        <td>{{ _report.NewCust }}</td>
                        <td>{{ _report.NewServ }}</td>
                        <td>{{ _report.Coupons }}</td>
						<td>{{ _report.date }}</td>
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
				report: {
					Customers: 0,
					Services: 0,
					avgSPC: 0,
					NewCust: 0,
					NewServ: 0,
					Coupons: 0,
					date: '',
				},
				reportlist: []
            }
        },
		created() {
			// Fetch Customer Count
            axios.get(config.APIURL + 'customer').then(res => {
                this.report.Customers = res.data[0].count;
				this.report.avgSPC = this.report.Services / this.report.Customers;
            }).catch(error => {
                console.log(error)
            });
			
			// Fetch Service Count
            axios.get(config.APIURL + 'service').then(res => {
                this.report.Services = res.data[0].count;
				this.report.avgSPC = this.report.Services / this.report.Customers;
            }).catch(error => {
                console.log(error)
            });
			
			// Fetch New Customers Past Month
			axios.get(config.APIURL + 'pastmonth/customers').then(res => {
                this.report.NewCust = res.data[0].NewCust
            }).catch(error => {
                console.log(error)
            });
			
			// Fetch New Services Past Month
			axios.get(config.APIURL + 'pastmonth/services').then(res => {
                this.report.NewServ = res.data[0].NewServ
            }).catch(error => {
                console.log(error)
            });
			
			// Fetch Coupons Count
			axios.get(config.APIURL + 'coupon').then(res => {
                this.report.Coupons = res.data[0].count;
            }).catch(error => {
                console.log(error)
            });
			
			// Fetch Past Reports
			axios.get(config.APIURL + 'reports').then(res => {
                this.reportlist = res.data;
				this.reportlist.shift();
            }).catch(error => {
                console.log(error)
            });
			
        },
		methods: {
			SaveLog() {
				
				// Get Current Date
				let date = new Date();
				this.report.date = date.toISOString().split('T')[0];
				console.log(this.report.date)
			
				// Send our report object to the API
                axios.post(config.APIURL + 'reports', this.report).then(() => {
				
                    // Reload the view
                    this.$router.go();
                }).catch(error => { // If an error shall occur, this catches the error and logs it to the console for later reference, if needed
                    console.log(error)
                });
			}
		}
	}
</script>