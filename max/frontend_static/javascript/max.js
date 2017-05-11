/**
 * Created by sheshank.kodam on 4/15/17.
 */
$(document).ready(function () {
    console.log("Hello max");

    $(".default_image").click(function(){
        console.log("Clicked on image");
        $('#uploaded_file').trigger('click');
    });

    $("#uploaded_file").change(function(){
        console.log("File upload received");
        previewImage(this);
        saveImage(this);
    });

    function previewImage(input) {
        console.log("Previewing image");
        if (input.files && input.files[0]) {
            var reader = new FileReader();
            reader.onload = function (e) {
                $('.default_image').attr('src', e.target.result);
            };
            reader.readAsDataURL(input.files[0]);
        }
    }

    function saveImage(input) {
        console.log("Saving image");
        $.ajax({
            url: '/upload',
            type: 'POST',
            contentType: 'application/json',
            data: "steve",
            success: function (result) {
               console.log(result);
            },
            error: function (error) {
                console.log(error);
            }
        })
    }
});