// CSRF token helper - iz Django dokumentacije
// https://docs.djangoproject.com/en/stable/howto/csrf/#using-csrf-protection-with-ajax
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

document.addEventListener('DOMContentLoaded', function () {
    const csrftoken = getCookie('csrftoken');
    const favoriteButtons = document.querySelectorAll('.favorite-btn');

    favoriteButtons.forEach(function (button) {
        button.addEventListener('click', function () {
            const noteId = button.getAttribute('data-note-id');

            fetch('/api/notes/' + noteId + '/favorite/', {
                method: 'POST',
                headers: {
                    'X-CSRFToken': csrftoken,
                },
            })
                .then(response => response.json())
                .then(data => {
                    if (data.is_fav) {
                        button.textContent = '❤️';
                    } else {
                        button.textContent = '🤍';
                    }
                })
                .catch(error => {
                    console.log('Greška kod favorita:', error);
                });
        });
    });
});