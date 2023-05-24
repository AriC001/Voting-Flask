import "https://cdn.socket.io/3.0.0/socket.io.js"
window.onload = function () {
    let socket = io("https://votting-flask-production.up.railway.app/");
    const boca = document.getElementById('Boca')
    const river = document.getElementById('River')
    const indep = document.getElementById('Independiente')
    const tomba = document.getElementById('Tomba')
    // const  socket = new WebSocket('ws://localhost:5000/echo')
    socket.on('votos',function(votos){
        updatVotes(votos)
        // updatVotes(ev.data)
    });
    // socket.send()

    function updatVotes (votes){
        boca.value = votes[0]
        river.value = votes[1]
        indep.value = votes[2]
        tomba.value = votes[2] 
    }
}
