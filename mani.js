document.getElementById('contactForm').addEventListener('submit', function(event) {
    event.preventDefault();
    
    var name = document.getElementById('name').value;
    var email = document.getElementById('email').value;
    var message = document.getElementById('message').value;

    var formResponse = document.getElementById('formResponse');
    formResponse.textContent = 'Thank you, ' + name + '! Your message has been sent.';

    document.getElementById('contactForm').reset();
});
