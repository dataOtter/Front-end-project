$(document).ready(function(){

    $('#add_button').click(function() {

        //alert("This");
        var thedata = {};
        var thekey = $('#input_key').val();
        var thevalue = $('#input_value').val();
        thedata[thekey] = thevalue;
        //alert(thedata);

        $.ajax({
            type: 'POST',
            contentType: 'application/json',
            data: JSON.stringify(thedata),  // data must be a dict style, even if its the same values
            url: '/add',
            success: function(response) {
                console.log("success!! " + response);

                $.getJSON({
                        url: "/add_success",
                        data: { get_param: 'msg' },
                        dataType: 'json',
                        type: "GET",
                        success: function(ddd){
                            $("#add_success").html(ddd.value + ": " + thekey + " " + thevalue);
                            $("#input_key").val('');
                            $("#input_value").val('');
                        },
                    });

                $.getJSON({
                        url: "/show_list",
                        data: { get_param: 'list' },
                        dataType: 'json',
                        type: "GET",
                        success: function(ddd){
                            //alert(ddd.one);
                            var new_table = '<h4>The Table</h4><table id="TheTable">';
                            new_table += '<tr><th>Index</th><th>Key</th><th>Value</th></tr>';
                            $(ddd.one).each(function(index, element){
                                new_table += '<tr>';
                                $(element).each(function(index, element){
                                    new_table += '<td>' + element + '</td>';
                                })
                                new_table += '</tr>';
                            });
                            //alert("HERE");
                            new_table += '</table>';
                            $("#show_table").html(new_table);
                        },
                    });
            },
            error: function(error) {
                console.log("failure!! " + error);
            }
        });

    });

});