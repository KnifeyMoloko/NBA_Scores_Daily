document.addEventListener('DOMContentLoaded',
    function () {
        const elems = document.querySelectorAll(".game-card");
        //elems.forEach((x) => console.log(x.parentElement.clientHeight));
        var elemArray = Array.from(elems);
        var heights = elemArray.map((e) => {return e.clientHeight});
        //console.log(heights);
        var maxCardHeight = Math.max(...heights);
        console.log(maxCardHeight);


        let slider = document.querySelector(".tabs-content.carousel.carousel-slider");
        let sliderHeight = slider.clientHeight;
        console.log(sliderHeight);
    });
