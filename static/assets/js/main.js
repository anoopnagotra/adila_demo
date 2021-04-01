$( document ).ready(function() {
    $(document).on("click",".parentButton", function () {
        var clickedBtnID = $(this).attr('id'); 
        $('.'+clickedBtnID).toggleClass("show").siblings().removeClass('show');
    });
});