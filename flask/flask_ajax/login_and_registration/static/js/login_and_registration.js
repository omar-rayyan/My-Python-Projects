$(document).ready(function(){
    $('#inputEmailR').keyup(function(){
        var data = $("#registration-form").serialize()
        console.log("Test1")
        $.ajax({
            method: "POST",
            url: "/email_validation",
            data: data
        })
        .done(function(res){
            $('#emailMsg').html(res)
        })
    })
})