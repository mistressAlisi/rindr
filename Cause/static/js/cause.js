function create_cause() {
    data = $("#cause_form").serialize();
    $.post('/cause/new/create',data,function(data){
        if (data.res == "err") {
            alert("Invalid Data");
        } else if (data.res == "ok") {
           alert("Success!! Cause created successfully.");
        }
    });
    return false;
};

