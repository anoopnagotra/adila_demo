
$(document).ready(function(){
		if( typeof(CKEDITOR) !== "undefined" ) {
	CKEDITOR.on('instanceReady',function(){
		for (var i in CKEDITOR.instances) {
		(function(i){
    	   CKEDITOR.instances[i].on('change', function() { 
			   // move ckeditor value to real textarea
			   CKEDITOR.instances[i].updateElement();
			   // recheck validations
			   if(jQuery().validate){
					$(CKEDITOR.instances[i].element.$).valid();
				}
			});
		})(i);
		}
	});
}

	
 /* Validations other rules start*/
     	$.validator.addMethod("alphawithspace", function(value,element) {
		   return this.optional(element) || value == value.match(/^[-a-zA-Z ]+$/); 
		}, "Alphabets only");
		$.validator.addMethod("alpha", function(value,element) {
		   return this.optional(element) || value == value.match(/^[a-zA-Z]+$/); 
		}, "Alphabets only");
		$.validator.addMethod("alphanumericspecial", function(value, element) {
			return this.optional(element) || value == value.match(/^[a-z0-9A-Z#@$%^&*()!]+$/);
		},"Only Characters, Numbers & Special Chars Allowed.");
		$.validator.addMethod("phonenumberhy", function(value, element) {
			return this.optional(element) || value == value.match(/^[0-9-]+$/);
		},"Valid Phone Number");
                jQuery.validator.addMethod("scriptTags", function(value,element) {
		   return this.optional(element) || value == value.match(/^[a-zA-Z0-9?-_ .,'"'@#=$%^&*(){}\n]+$/); 
		}, "Alphabets only"); 
                $.validator.addMethod("scriptTagsAlow", function(value,element) {
		   return this.optional(element) || value == value.match(/^[a-zA-Z0-9-_ .,'"#$@%^&*(){=}\n\s]+$/); 
		}, "Alphabets only");
	 /* Validations other rules end*/
	 
	 // For Name only letters
    jQuery(function() {
        jQuery.validator.addMethod("loginRegex", function(value, element) {
            return this.optional(element) || /^[a-zA-Z]+$/i.test(value);
        }, 'Please enter valid name');
    });

    // For Password only letters,numbers   and @,_ as the special characters
    jQuery(function() {
        jQuery.validator.addMethod("passwordRegex", function(value, element) {
            return this.optional(element) || /^[0-9a-zA-Z@_]+$/.test(value);
        }, 'Please enter valid password');
    });

    // For Titles only letters , . and spaces
    jQuery(function() {
        jQuery.validator.addMethod("titleRegex", function(value, element) {
            //return this.optional(element) || /^[a-zA-Z0-9 .,]+$/i.test(value);
            return this.optional(element) || /^[a-zA-Z0-9 .,_-]+$/i.test(value);
        }, 'Please enter valid content');
    });

    // Custom validation for phone
    jQuery(function() {
        jQuery.validator.addMethod("phoneRegex", function(value, element) {
            return this.optional(element) || /^([\+][0-9]{1,3}[\ \.\-])?([\(]{1}[0-9]{2,6}[\)])?([0-9\ \.\-\/]{3,20})((x|ext|extension)[\ ]?[0-9]{1,4})?$/.test(value);
        }, 'Please enter valid phone no');
    });

    // Custom validation for description to validate against html tags
    jQuery(function() {
        jQuery.validator.addMethod("descRegex", function(value, element) {
            return this.optional(element) || /^[a-zA-Z0-9!%@$&*#()-.,:;?\/'_\n ]+$/i.test(value);
        }, 'please enter valid description');
    });

    // Custom validation for email
    jQuery(function() {
        jQuery.validator.addMethod("emailRegex", function(value, element) {
            value = $.trim(value);
            jQuery('#UserEmail').val(value);
            return this.optional(element) || /^((([a-z]|\d|[!#\$%&'\*\+\-\/=\?\^_`{\|}~]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])+(\.([a-z]|\d|[!#\$%&'\*\+\-\/=\?\^_`{\|}~]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])+)*)|((\x22)((((\x20|\x09)*(\x0d\x0a))?(\x20|\x09)+)?(([\x01-\x08\x0b\x0c\x0e-\x1f\x7f]|\x21|[\x23-\x5b]|[\x5d-\x7e]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(\\([\x01-\x09\x0b\x0c\x0d-\x7f]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF]))))*(((\x20|\x09)*(\x0d\x0a))?(\x20|\x09)+)?(\x22)))@((([a-z]|\d|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(([a-z]|\d|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])([a-z]|\d|-|\.|_|~|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])*([a-z]|\d|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])))\.)+(([a-z]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(([a-z]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])([a-z]|\d|-|\.|_|~|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])*([a-z]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])))\.?$/i.test(value);
        }, 'Please enter valid email');
    });	



});
