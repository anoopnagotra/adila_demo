// File:           customjs.js
// Developer       Anoop kumar.
// Purpose         Custome functions and code
// Created Date    12-06-2020
$(document).ready(function() {

    // // $( "#update_num_vip_admin" ).submit(function( event ) {
    // //   alert( "Handler for .submit() called." );
    // //   event.preventDefault();
    // // });
    
    $("#update_num_vip_admin").validate({
        rules: {
            "numbers": {
                required: true,
                // minlength: 5
            },
            "price_1": {
                required: true,
                number: 5
            },
            "rtp_date_1": {
                // required: true,
                // minlength: 5
            },
            "number_delete_date_1": {
                // required: true,
            }
        },
        messages: {
            // "signupCPassword": " Confirm password should be same as password"
        }
    });

});