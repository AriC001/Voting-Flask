// import "https://cdn.socket.io/3.0.0/socket.io.js"
import "./socket.io.js"
window.onload = function () {
    let location = window.location.host
    let socket = io("ws://localhost:5000", {transports: ['websocket']});
    const boca = document.getElementById('Boca')
    const river = document.getElementById('River')
    const indep = document.getElementById('Independiente')
    const tomba = document.getElementById('Tomba')
    socket.on('votos',function(votos){
        updatVotes(votos)
    });

    function updatVotes (votes){
        boca.value = votes[0]
        river.value = votes[1]
        indep.value = votes[2]
        tomba.value = votes[2] 
    }
}
