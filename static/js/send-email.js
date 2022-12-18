function sendMail(contactUs) {
    emailjs.send('service_4i9pqi7', 'template_svkipe7', {
            "name": contactUs.name.value,
            "email": contactUs.email.value,
            "message": contactUs.commentbox.value
        })
        .then(
            function (response) {
                if (response.status == 200) {
                   $(".my-modal").modal('toggle', response)
                   $('.modal-title').html('Thank you for your email!')
                   $('.modal-body').html('<p>A member of staff would be in contact with you shortly. Your email/feedbacks mean alot to us here at active-spring.</p>')


                }
            },
            function (error) {
                console.log('Unsuccessful', error)
            });
            return false
}