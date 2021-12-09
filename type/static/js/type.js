function create_type() {
    data = $("#type_form").serialize();
    $.post('/type/new/create',data,function(data){
        if (data.res == "err") {
            alert("Invalid Data");
        } else if (data.res == "ok") {
           alert("Success!! Type created successfully.");
        }
    });
    return false;
};

