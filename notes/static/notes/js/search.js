document.addEventListener('DOMContentLoaded', function () {
    const searchInput = document.getElementById('search-input');
    const notesGrid = document.getElementById('notes-grid');

    searchInput.addEventListener('input', function () {
        const query = searchInput.value;

        fetch('/api/notes/?query=' + encodeURIComponent(query))
            .then(response => response.json())
            .then(data => {
                showNotes(data);
            })
            .catch(error => {
                console.log('Greška kod pretrage:', error);
            });
    });

    function showNotes(notes) {
        notesGrid.innerHTML = '';

        if (notes.length === 0) {
            notesGrid.innerHTML = '<p>Nema rezultata.</p>';
            return;
        }

        notes.forEach(function (note) {
            const card = document.createElement('div');
            card.className = 'note-card';

            let ratingText = 'Još nema ocjena.';
            if (note.average_rating !== null) {
                ratingText = 'Ocjena: ' + note.average_rating + ' / 5';
            }

            card.innerHTML = `
                <h3>${note.course_name}</h3>
                <p>${note.title}</p>
                <p>Fakultet: ${note.faculty}</p>
                <p>Autor: ${note.author}</p>
                <p>${ratingText}</p>
                <div class="card-actions">
                    <a href="/note/${note.id}/">Detalji</a>
                </div>
            `;

            notesGrid.appendChild(card);
        });
    }
});