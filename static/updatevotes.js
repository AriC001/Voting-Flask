const boca = document.querySelector('#Boca')
const river = document.querySelector('#River')
const indep = document.querySelector('#Independiente')
const tomba = document.querySelector('#Tomba')
let socket = io.connect("hhtp://votting-flask-production.up.railway.app/connect:");
socket.on("votos",function (votes){
    boca.value = votes[0]
    river.value = votes[1]
    indep.value = votes[2]
    tomba.value = votes[2] 
})