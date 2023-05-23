window.onload = function () {
    const email = document.getElementById('username');
    const spanEmail= document.getElementById('invalidEmail')
    let valid2 = false

    function ValidateEmail(mail)
    {
    if (/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/.test(mail.value))
    {
        return (true)
    }
        return (false)
    }

    email.addEventListener('blur',(event)=>{
        let valid = ValidateEmail(email)
        if (valid != true){
            spanEmail.style.display= "block"
        }else{
            spanEmail.style.display= "none"
        }
    })

}
