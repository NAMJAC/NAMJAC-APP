import emailjs from '@emailjs/browser'

const USER_ID = 'dBaFNl1ZAtGnN9X8n'
const SERVICE_ID = 'service_xz1l7el'
const TEMPLATE_ID = 'template_b66ecvp'
const FROM_NAME = 'Awesome Tire' // Can be any Name

emailjs.init(USER_ID)

export default async function sendEmail(recipients, message, img){
    recipients.forEach(async recipient => {
        await emailjs.send(
            SERVICE_ID,
            TEMPLATE_ID,
            {
                to_name: recipient,
                from_name: FROM_NAME,
                message: message,
                img: img
            },
            USER_ID
        )
        alert(recipient)
        
    })
}