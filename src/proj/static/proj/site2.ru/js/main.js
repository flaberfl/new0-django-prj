$(function () {

    $('.header-slider').slick({
        vertical: true,
        slidesToShow: 1,
        slidesToScroll: 1,
        autoplay: true,
        autoplaySpeed: 2000,
        arrows: false,
        lazyLoad: 'progressive',
        // adaptiveHeight: true,
        // variableWidth: true,
        adaptiveHeight: false,
        infinite: true,
        responsive: [{
                breakpoint: 992,
                settings: {
                    slidesToShow: 1,
                    slidesToScroll: 1,
                    infinite: true,
                }
            },
            {
                breakpoint: 480,
                settings: {
                    slidesToShow: 1,
                    slidesToScroll: 1
                }
            }
            // You can unslick at a given breakpoint now by adding:
            // settings: "unslick"
            // instead of a settings object
        ]
    });

    $('.info__content-description--text').readmore({
        maxHeight: 240,
        moreLink: '<a class="read-more" href="#">Читать полностью</a>',
        lessLink: '<a class="read-more" href="#">Свернуть текст</a>'
    });


});

// jQuery(document).ready(function () {
//     jQuery(".photo-list").unitegallery({
//         gallery_theme: "tiles",
//         tiles_type: "justified"
//     });
// });