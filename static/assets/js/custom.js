 $( document ).ready(function() {
    //add number in cart
    $(document).on('click', '.add-to-cart', function() {
        var getId = $(this).attr('id');
        // var quantit = $('.total_quantity').val();
        // console.log(quantit);
        var dish_quantity = $(this).parent().find('.dish_quantity').val();
        var dish_id = $(this).parent().find('.dish_id').val();
        var dish_name = $(this).parent().find('.dish_name').val();
        var dish_price = $(this).parent().find('.dish_price').val();

        var cartCount = $('.cart-count').text();
        
        console.log(cartCount);

        $.post('/add-number-in-bag/', {
            dish_id: dish_id,
            quantity:dish_quantity,
            dishFrom: 'cart'
        }, function(success) {
            console.log("s========<>>> ");
            console.log(success.status );
            if (success.status == 1) {
                // var object = '';
                cartCount = parseInt(cartCount) + parseInt(1);
                console.log(cartCount);
                alert(success.msg);
                // var tpl = headerCart(object);
                // $('.topHeaderCartTbl').append(tpl);
                $('.header-cart-empty').hide();
                $('.cart-count').html(cartCount);
                // window.location.href = 'cart/'
            } else if(success.status == 0){
                alert(success.msg);
                // window.location.href = 'cart/'
            }

        });
    });

    //add number in cart
    $(document).on('click', '.add-to-cart-home', function() {
        var getId = $(this).attr('data-id');
        // var quantit = $('.total_quantity').val();
        // console.log(quantit);
        var dish_id = $(this).parent().parent().find('.dish_id').val();
        var dish_name = $(this).parent().parent().find('.dish_name').val();
        var dish_price = $(this).parent().parent().find('.dish_price').val();

        console.log(dish_id);
        console.log(dish_name);
        console.log(dish_price);
        var cartCount = $('.cart-count').text();
        
        // console.log(cartCount);

        $.post('/add-number-in-bag/', {
            dish_id: dish_id,
            quantity:1,
            dishFrom: 'cart'
        }, function(success) {
            console.log("s========<>>> ");
            console.log(success.status );
            if (success.status == 1) {
                // var object = '';
                cartCount = parseInt(cartCount) + parseInt(1);
                console.log(cartCount);
                alert(success.msg);
                // var tpl = headerCart(object);
                // $('.topHeaderCartTbl').append(tpl);
                $('.header-cart-empty').hide();
                $('.cart-count').html(cartCount);
                window.location.href = 'cart/'
            } else if(success.status == 0){
                alert(success.msg);
                window.location.href = 'cart/'
            }

        });
    });


     $(document).on('click', '.remove-art', function() {
        var getId = $(this).attr('data-val');
        // alert(getId);
        // getId = getId.split('_')[1];
        var cartCount = $('.cart-count').text();
        // alert(cartCount);
        $.post('/update-dish-in-bag/', {
            dishId: getId,
            dishFrom: 'updateCart'
        }, function(success) {
            window.location.href = 'cart/'
            if (success.status == 1) {
                // var object = '';
                // object = {
                //     "number": success.data[0].display_number,
                //     "price": 'Rs. ' + success.data[0].purchase_price,
                //     "number_id": success.data[0].number_id
                // };
                // cartCount = parseInt(cartCount) + parseInt(1);
                // var tpl = headerCart(object);
                // $('.topHeaderCartTbl').html('').append(tpl);
                // $('.header-cart-empty').hide();
                // $('.cart-count').html('1');
                // $('#directPayment').modal('show');
                // $('.btnVipCMBMdl').hide();
            } else if(success.status == 0){
                alert(success.msg);
            }

        });
    });

    // Home Page Spices of Life   
    $(document).on('click', '.show-hide-spicies', function() {
        var desc = $(this).parent().find('.descriptn').val();
        var spice_image = $(this).parent().find('.spice-image').val();
        console.log("spice_image");
        console.log(spice_image);
        $(".detail-des").text(desc);
        $("#my_image").attr("src",spice_image);
    });


    //add number in cart
    $(document).on('click', '.cart-minus', function() {
        var quant  = $(this).siblings('.cart-quantity').val();
        var price  = $(this).siblings('.cart-price').val();
        var rate  = $(this).parent().parent().siblings('.rate').text();
        console.log(rate);
        quant = parseInt(quant,10);
        price = parseFloat(price).toFixed(2);


        if (quant == 1){
          $(this).siblings('.cart-quantity').val(1);
          final_price = quant * price;
          // var frate = £ + final_price; 
          $(this).parent().parent().siblings('.rate').text(frate);
        }else{
          var value=quant-1;
          $(this).siblings('.cart-quantity').val(value);
          final_price = value * price;
          console.log(price);
          console.log(final_price);
          var frate = '£  ' + final_price; 
          $(this).parent().parent().siblings('.rate').text(frate);

        }
    });
    
    // add value in cart
    $(document).on('click', '.cart-plus', function() {
        var quant  = $(this).siblings('.cart-quantity').val();
        var price  = $(this).siblings('.cart-price').val();
        var rate  = $(this).parent().parent().siblings('.rate').text();

        quant = parseInt(quant,10);
        price = parseFloat(price).toFixed(2);
        console.log(quant);
        var value=quant+1;
        $(this).siblings('.cart-quantity').val(value);
        final_price = value * price;
        console.log(price);
        console.log(final_price);
        // var frate = £ + final_price; 
         var frate = '£  ' + final_price; 
        $(this).parent().parent().siblings('.rate').text(frate);
    });
});
