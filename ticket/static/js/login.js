function go_login() {
    data = $("#loginForm").serialize();
    $.post('/login/action',data,function(data){
        if (data.res == "err") {
            alert("Invalid Credentials");
        } else {
           location.href="/";
        }
    });
    return false;
};
