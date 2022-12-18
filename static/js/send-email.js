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
                }
            },
            function (error) {
                console.log('Unsuccessful', error)
            });
            return false
}