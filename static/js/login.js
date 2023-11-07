$("#entrarbutton").click(function() {
    email = $("#email").val()
    senha = $("#senha").val()

    if ($("#email").val() == "" || $("#senha").val() == "") {
        $(".errortext").text('Você precisa preencher todos os campos para poder logar.')
        $(".errormessage").removeClass("hidden")
    }else {
        $.ajax({
            url: "/authenticate?email=" + email + "&senha=" + senha,
            type: "POST",
            success: function(result){
                if(result == '0') {
                    location.href = "/dashboard"
                }else if(result == '1') {
                    $(".errortext").text('Não foi possível logar, seus dados estão incorretos.')
                    $(".errormessage").removeClass("hidden")
                }else if(result == '2') {
                    $(".errortext").text('Não foi possível logar, seus dados estão incorretos.')
                    $(".errormessage").removeClass("hidden")
                }
            },
        });
    }


});

$("#showpassword").click(function() {
    if ($("#senha").attr('type') == "password") {
        $("#senha").attr('type', 'text');
    }else {
        $("#senha").attr('type', 'password');
    }
})