function create_ticket() {
    data = $("#ticket_form").serialize();
    $.post('/new/create',data,function(data){
        if (data.res == "err") {
            if ("error" in data) {
               error_data = JSON.parse(data.error);
               //window.error = error_data;
               for (key in error_data) {
                   alert("**Invalid Data:**\nFor Field: '"+key+"':\nError in Input: '"+error_data[key][0].message+"'.\n");
               };
            };
        } else if (data.res == "ok") {
           alert("Success!! Ticket created successfully.");
        }
    });
    return false;
};


