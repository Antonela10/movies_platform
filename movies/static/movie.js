document.addEventListener('DOMContentLoaded', function() {

    var movie_body = document.querySelector('.movie-body');
    var movie_id = document.querySelector('.movie-id');
    
    // Trailer pop-up box
    try {
        var trailer_pop_up_box = document.querySelector('.trailer-pop-up-box');
        var movie_trailer = document.querySelector('.movie-trailer');

        // Show trailer pop-up box
        movie_trailer.addEventListener('click', () => {
            movie_body.classList.add('blur');
            trailer_pop_up_box.classList.add('pop-up-show');
        })

        // Hide trailer pop-up box
        document.querySelector('.trailer-overlay').addEventListener('click', () => {
            movie_body.classList.remove('blur');
            trailer_pop_up_box.classList.remove('pop-up-show');
        })
    }
    catch (err) {
        console.log(err);
    }

    // Person pop-up box
    try {
        var person_pop_up_box = document.querySelector('.person-pop-up-box');
        var person_info_all = document.querySelectorAll('.person-info');
        var person_image = document.querySelector('.person-image')
        var person_name = document.querySelector('.person-name')
        var person_movies = document.querySelector('.person-movies')
        var person_role = document.querySelector('.person-role')

        person_info_all.forEach(function(person_info) {
            person_info.addEventListener('click', (event) => {
                person_pop_up_box.classList.add('pop-up-show');
                movie_body.classList.add('blur');
                const person_div = event.target;
                const person_id = person_div.dataset.personid;

                var url = '/person/?person_id=' + person_id;
                fetch(url)
                    .then(function(response) {
                        console.log('Response status:', response.status);
                        if (!response.ok) {
                            throw new Error('Network response was not ok');
                        }
                        return response.json();
                    })
                    .then(function(data) {
                        person_image.src = data.person_photo_file_name
                        person_name.textContent = data.name
                        person_movies.textContent = data.person_movies.join(', ')
                        person_role.textContent = data.person_roles
                    })
                    .catch(function(error) {
                        console.error('Error fetching information:', error);
                    });

            })
        })

        document.querySelector('.person-overlay').addEventListener('click', () => {
                person_pop_up_box.classList.remove('pop-up-show');
                movie_body.classList.remove('blur'); 
            })

    }
    catch (err) {
        console.log(err);
    }
})