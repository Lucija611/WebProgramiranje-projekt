document.addEventListener('DOMContentLoaded', function () {

    // za reg formu
    const registerForm = document.getElementById('register-form');

    if (registerForm) {
        registerForm.addEventListener('submit', function (event) {
            const username = registerForm.querySelector('[name="username"]');
            const email = registerForm.querySelector('[name="email"]');
            const password1 = registerForm.querySelector('[name="password1"]');
            const password2 = registerForm.querySelector('[name="password2"]');
            const faculty = registerForm.querySelector('[name="faculty"]');

            let errorMessage = '';

            if (username.value.trim() === '') {
                errorMessage = 'Korisničko ime je obavezno.';
            } else if (email.value.trim() === '') {
                errorMessage = 'Email je obavezan.';
            } else if (!email.value.includes('@')) {
                errorMessage = 'Email nije ispravan.';
            } else if (faculty.value.trim() === '') {
                errorMessage = 'Naziv fakulteta je obavezan.';
            } else if (password1.value.trim() === '') {
                errorMessage = 'Lozinka je obavezna.';
            } else if (password1.value !== password2.value) {
                errorMessage = 'Lozinke se ne poklapaju.';
            }

            if (errorMessage !== '') {
                event.preventDefault();
                alert(errorMessage);
            }
        });
    }

    // za upload formu
    const uploadForm = document.getElementById('upload-form');

    if (uploadForm) {
        uploadForm.addEventListener('submit', function (event) {
            const title = uploadForm.querySelector('[name="title"]');
            const courseName = uploadForm.querySelector('[name="course_name"]');
            const faculty = uploadForm.querySelector('[name="faculty"]');
            const description = uploadForm.querySelector('[name="description"]');
            const file = uploadForm.querySelector('[name="file"]');

            let errorMessage = '';

            if (title.value.trim() === '') {
                errorMessage = 'Naziv skripte je obavezan.';
            } else if (courseName.value.trim() === '') {
                errorMessage = 'Naziv kolegija je obavezan.';
            } else if (faculty.value.trim() === '') {
                errorMessage = 'Naziv fakulteta je obavezan.';
            } else if (description.value.trim() === '') {
                errorMessage = 'Opis je obavezan.';
            } else if (file.files.length === 0) {
                errorMessage = 'Datoteka je obavezna.';
            }

            if (errorMessage !== '') {
                event.preventDefault();
                alert(errorMessage);
            }
        });
    }

});