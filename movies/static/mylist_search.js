document.addEventListener('DOMContentLoaded', function() {

    var movie_summary_all = document.querySelectorAll('.movie-summary');
    movie_summary_all.forEach(function(movie_summary) {
        var content = movie_summary.innerHTML;
        if (content.length > 200) {
            var truncated_content = content.substring(0, 200) + "...";
            movie_summary.innerHTML = truncated_content;
        }
    })

    // Convert minutes to hours and minutes
    var movie_duration_div = document.querySelectorAll('.movie-duration');
    movie_duration_div.forEach(function(movie) {
        var movie_duration = movie;
        var movie_duration_shown = movie_duration.querySelector('.movie-duration-shown');
        var movie_duration_hidden = movie_duration.querySelector('.movie-duration-hidden');
        var total_minutes = parseInt(movie_duration_hidden.innerHTML);
        const hours = Math.floor(total_minutes / 60);
        const minutes = total_minutes % 60;
        movie_duration_shown.innerHTML = `${hours}h ${minutes}min`;
    })
})