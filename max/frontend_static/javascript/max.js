/**
 * Created by sheshank.kodam on 4/15/17.
 */
$(document).ready(function () {
    // load default data on page load
    console.log("Hello max");

    $(".upload_image").click(function(){
        console.log("clicked on image")
        $('#imgupload').trigger('click');
    });

    $("#imgupload").change(function(){
        console.log("get image here")
        readURL(this);
    });

    function readURL(input) {
        console.log(input.files[0])
        if (input.files && input.files[0]) {
            var reader = new FileReader();
            reader.onload = function (e) {
                $('.upload_image').attr('src', e.target.result);
            };
            reader.readAsDataURL(input.files[0]);
        }
    }
});