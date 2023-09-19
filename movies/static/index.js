document.addEventListener('DOMContentLoaded', function() {

    var scrollable_container_all = document.querySelectorAll('.scrollable-container');
    scrollable_container_all.forEach(function(container) {

        const movies_display = container.querySelector('.movies-display');
        const right_arrow = container.querySelector('.icon-right');
        const left_arrow = container.querySelector('.icon-left');

        console.log(movies_display.children.length);

        let scrolled = false; // Flag to track scrolling

        // When right arrow is clicked
        right_arrow.addEventListener('click', () => {

            left_arrow.style.display = 'block';
            
            movies_display.scrollBy({ left: 200, behavior: "smooth" });

            // Set the scrolled flag to true
            scrolled = true;
        })
        
        // On mouseover
        container.addEventListener('mouseover', () => {

            if (movies_display.children.length < 9 || movies_display.scrollLeft >= (movies_display.scrollWidth - movies_display.clientWidth)) {
                right_arrow.style.display = 'none';
            } else {
                right_arrow.style.display = 'block';
            }
             
            // Display left arrow only if scrolled and if there's content to the left
            if (scrolled && movies_display.scrollLeft > 0) {
                left_arrow.style.display = 'block';
            }                      
        })

        // On mouseout
        container.addEventListener('mouseout', (event) => {
            right_arrow.style.display = 'none';
            left_arrow.style.display = 'none';
        })
        
        // When left arrow is clicked
        left_arrow.addEventListener('click', () => {
            movies_display.scrollBy({ left: -200, behavior: "smooth" });
        })
        
    })

})