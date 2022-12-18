function sendMail(contactUs) {
    emailjs.send('service_4i9pqi7', 'template_svkipe7', {
            "name": contactUs.name.value,
            "email": contactUs.email.value,
            "message": contactUs.commentbox.value
        })
        .then(
            function (response) {
                if (response.status == 200) {
                   $(".my-modal").modal('toggle');
                   $('.modal-title').html(`Thank you for your email!`);
                   $('.modal-body').html('<p>A member of staff would be in contact with you shortly. Your email/feedbacks are important to us here at active-spring.</p>');
                   $("#change-color").addClass("bg-green");


                }
            },
            function (error) {
                $(".my-modal").modal('toggle');
                $('.modal-title').html(`Sorry but an ${error.error} has occured!`);
                $('.modal-body').html('<p>Please return back to the home page then try again. Alternatively you can contact us at (+0700800100).</p>');
                $(".modal-header").removeClass("grad");
                $(".modal-body").removeClass("grad");
                $("#change-color").addClass("red-btn");
            });
            return false
}