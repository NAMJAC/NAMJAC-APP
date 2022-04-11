<template>
    <div>
        <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
            <div class="container-fluid">
                <div class="collapse navbar-collapse" id="navbarColor02">
                    <ul class="navbar-nav me-auto">
                        <li class="navbar-brand">
                            <router-link to="/">
								<img
									src="./assets/Awesome-transparent.png"
									style="
										object-fit:contain;
										width:128px;
										height:auto
									"
								/>
							</router-link>
                        </li>
                        <li class="nav-item">
                            <router-link class="nav-link" to="/view/customers">Customers</router-link>
                        </li>
                        <li class="nav-item">
                            <router-link class="nav-link" to="/view/services">Services</router-link>
                        </li>
						<li class="nav-item">
                            <router-link class="nav-link" to="/email">Email</router-link>
                        </li>
						<li class="nav-item">
                            <router-link class="nav-link" to="/reports">Reports</router-link>
                        </li>
                    </ul>
                    <div class="d-flex navbar-nav nav-item">
                        <router-link class=" nav-link" to="/about">About</router-link>
                    </div>
                </div>
            </div>
        </nav>

        <div class="container mt-5">
            <router-view></router-view>
        </div>

        <footer class="footer fixed-bottom bg-light">
                    <div class="text-muted text-center">Created by NAMJAC Development for Awesome Tires and Mechanic. Running Vue.js and Python</div>
        </footer>
    </div>

    
</template>

<script>
</script>

<style>
</style>