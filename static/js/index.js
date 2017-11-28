$(document).ready(function(){

    $('#outer_box').on('click', '#add_button', function() {

        var thedata = {},
        thekey = $('#input_key').val(),
        thevalue = $('#input_value').val();
        thedata[thekey] = thevalue;

        $.ajax({
            type: 'POST',
            contentType: 'application/json',
            data: JSON.stringify(thedata),  // data must be a dict style, even if its the same values
            url: '/add',
            success: function(response) {
                success_fn(response);
                $.getJSON({
                        url: "/show_table",
                        data: { get_param: 'list' },
                        dataType: 'json',
                        type: "GET",
                        success: function(data_in) { show_table (data_in) }
                });
            },
            error: function(error) { console.log("failure!! " + error); }
        });

        function success_fn(result){
            $("#add_success").html(result + ": " + thekey + " " + thevalue);
            $("#input_key").val('');
            $("#input_value").val('');
        }
    });

    $('#outer_box').on('click', '#download_button', function() {
        $.get({
                url: "/download_csv",
                //dataType: 'json',
                success: function(file_in) {
                    alert(file_in);
                }
        });
    });

    //$('a').click(function(e) {
        //e.preventDefault();  //stop the browser from following
        //window.location.href = 'outputs/test.csv';
    //});

    function show_table(data) {
        var new_table = '<h4>The Table</h4><table id="TheTable">';
        new_table += '<tr><th>Index</th><th>Key</th><th>Value</th></tr>';
        $(data.one).each(function(index, element){
            new_table += '<tr>';
            $(element).each(function(index, element){
                new_table += '<td>' + element + '</td>';
            })
            new_table += '</tr>';
        });
        new_table += '</table>';
        $("#show_table").html(new_table);
    }
});