<template>
	<div class="display-5 text-center">
        Send an Email Coupon
    </div>
    <br />
    <div class="container bg-light">
		<div class="form-group text-start">
			<div class="row">
				<div class="col">
					<label class="col-form-label mt-4">Enter one or more recipients</label>
					<br />
					<textarea class="form-control" placeholder="Enter one or more recipients" v-model="recipients">
					</textarea>
				</div>
			</div>
			<div class="row">
				<div class="col">
					<label class="col-form-label mt-4">Enter Your Message</label>
					<br />
					<textarea class="form-control" placeholder="Enter Your Message" v-model="message"></textarea>
				</div>
			</div>
			<div class="row">
				<div class="col">
					<label class="col-form-label mt-4">Choose an image</label>
					<br />
					<input type="file" @change="handleImg" />
				</div>
			</div>
			<p>
				<canvas ref="imgCanvas"></canvas>
			</p>
			<div class="row">
				<div class="col text-center">
					<button class="btn btn-primary" type="submit" @click="handleSubmit">Submit</button>
				</div>
			</div>
		</div>
    </div>
</template>

<script>
import sendEmail from '@/utils/email'
import axios from "axios";
import config from '../config.js';

export default {
    data: () => ({
        img: null,
        imgCanvas: null,
        imgCtx: null,
        canvasSize: {
            width: 100,
            height: 100
        },
        recipients: '',
        message: '',
		couponlog: {
			recipient: '',
			message: '',
			date: ''
		}
    }),
    mounted(){
		this.recipients = this.$route.query.email;
	
        this.imgCanvas = this.$refs.imgCanvas
        this.imgCanvas.width = this.canvasSize.width
        this.imgCanvas.height = this.canvasSize.height

        this.imgCtx = this.imgCanvas.getContext('2d')
    },
    methods: {
        handleImg(e){
            const file = e.target.files[0]
            if(!file){
                this.imgCtx.clearRect(0, 0, this.canvasSize.width, this.canvasSize.height)
                this.canvasSize.width = 100
                this.canvasSize.height = 100
                this.imgCanvas.width = this.canvasSize.width
                this.imgCanvas.height = this.canvasSize.height
                return
            }
            const reader = new FileReader()

            reader.onload = (e) => {
                const img = new Image()
                img.onload = () => {
                    let imgWidth = img.width
                    let imgHeight = img.height
                    let ratio = imgWidth / imgHeight

                    const maxWidth = 300
                    const maxHeight = 300

                    if(imgWidth > maxWidth){
                        imgWidth = maxWidth
                        imgHeight = imgWidth / ratio
                    }
                    if(imgHeight > maxHeight){
                        imgHeight = maxHeight
                        imgWidth = imgHeight * ratio
                    }
                    this.canvasSize.width = imgWidth
                    this.canvasSize.height = imgHeight
                    this.imgCanvas.width = this.canvasSize.width
                    this.imgCanvas.height = this.canvasSize.height
                    this.imgCtx.drawImage(img, 0, 0, this.canvasSize.width, this.canvasSize.height)
                }
                img.src = e.target.result
            }

            reader.readAsDataURL(file)
        },
        async handleSubmit(){
            if(!this.recipients.trim() || !this.message.trim()){
                alert('Please fill out all fields')
                return
            }
            let recipients = this.recipients.split(',').map(e => e.trim())
            //Replace above line with a api call if needed
            //eg let recipients = await axios.get('/api/get-recipients')
            try{
                await sendEmail(recipients, this.message, this.imgCanvas.toDataURL())
                alert('Email sent successfully')
            }catch(e){
                console.log(e)
            }
			
			let date = new Date();
			this.couponlog.message = this.message
			this.couponlog.date = date.toISOString().split('T')[0];
			
			for (let i = 0; i < recipients.length; i++) {
				this.couponlog.recipient = recipients[i]
				try {
					await axios.post(config.APIURL + 'coupon', this.couponlog)
				} catch(e) {
					console.log(e)
				}
			}
        }
    }
}
</script>
