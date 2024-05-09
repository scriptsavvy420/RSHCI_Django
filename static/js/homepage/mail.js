$("#submit").click(function(e){
    e.preventDefault()

    $("input").each(function(){
        $(this).removeClass("input-error")
    })
    $("textarea").each(function(){
        $(this).removeClass("input-error")
    })
    $("._error").each(function(){
        $(this).removeClass("is-active")
    })
    var success = true;
    var testEmail = /^[A-Z0-9._%+-]+@([A-Z0-9-]+\.)+[A-Z]{2,4}$/i;
    var contact_name = $("#contact-name").val()
    var contact_email = $("#contact-email").val()
    var contact_phone = $("#contact-phone").val()
    var contact_type = $("#contact-disires").val()
    var contact_contents = $("#contact-text").val()
    var contact_check = $("#contact-check").prop('checked')
    if(contact_name == ""){
        $("#contact-name").addClass("input-error")
        $(".name__error").addClass("is-active")
        success = false
    }
    
    if (!testEmail.test(contact_email)){
        $("#contact-email").addClass("input-error")
        $(".email__error").addClass("is-active")
        success = false
    }
    if(contact_phone == ""){
        $("#contact-phone").addClass("input-error")
        $(".phone__error").addClass("is-active")
        success = false
    }
    if(contact_type == ""){
        $("#contact-disires").addClass("input-error")
        $(".disires__error").addClass("is-active")
        success = false
    }
    if(contact_contents == ""){
        $("#contact-text").addClass("input-error")
        $(".text__error").addClass("is-active")
        success = false
    }
    if(!contact_check){ // Corrected checkbox value check
        $(".agree__error").addClass("is-active");
        success = false;
    }

    if(success){
        

        const form = document.getElementById('p-contact__form');
        const formData = new FormData(form);
        console.log(form)

        fetch("/send_mail", {
            method: 'POST',
            body: formData
        })
        .then((response) => {
            
            
            if(response = true){
                
                $("#contact-name").val("")
                $("#contact-email").val("")
                $("#contact-phone").val("")
                $("#contact-disires").val("")
                $("#contact-text").val("")
                $("#contact-check").prop('checked',false)
                alert("The message has been successfully sent.")  
            }
            
        })
        .catch((error) => {
            alert("Failed to send message due to server error. Please try again later.")
            print(str(error))

        });
    }

    
})