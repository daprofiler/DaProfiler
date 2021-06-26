// ----------------------------------------------
// # Search
// ----------------------------------------------

(function () {

    $('.fa-search').on('click', function () {
        $('.search').fadeIn(500, function () {
            $(this).toggleClass('search-toggle');
        });
    });

    $('.search-close').on('click', function () {
        $('.search').fadeOut(500, function () {
            $(this).removeClass('search-toggle');
        });
    });

}());


$(document).ready(function () {

    // Add body-small class if window less than 768px
    if ($(this).width() < 769) {
        $('body').addClass('body-small');
    } else {
        $('body').removeClass('body-small');
    }

    // MetsiMenu
    $('#side-menu').metisMenu();

    // Minimalize menu
    $('.navbar-minimalize').click(function () {
        $("body").toggleClass("mini-navbar");


    });
              $(".nano").nanoScroller();
});

//------------- Last sales locations -------------//
$('#world-map').vectorMap({
    map: 'world_mill_en',
    scaleColors: ['#666', '#29b6d8'],
    normalizeFunction: 'polynomial',
    hoverOpacity: 0.7,
    hoverColor: false,
    focusOn: {
        x: 0.5,
        y: 0.5,
        scale: 1.0
    },
    zoomMin: 0.85,
    markerStyle: {
        initial: {
            fill: '#fff',
            stroke: '#fff',
            color: '#ffffff'
        }
    },
    backgroundColor: '#fff',
    regionStyle: {
        initial: {
            fill: '#e77b55',
            "fill-opacity": 1,
            stroke: '#87c2e0',
            "stroke-width": 0,
            "stroke-opacity": 0
        },
        hover: {
            "fill-opacity": 0.8
        },
        selected: {
            fill: 'yellow'
        }
    },
    markers: [
        //http://www.latlong.net/
        {latLng: [51.507351, -0.127758], name: 'London'},
        {latLng: [41.385064, 2.173403], name: 'Barcelona'},
        {latLng: [40.712784, -74.005941], name: 'New York'},
        {latLng: [-22.911632, -43.188286], name: 'Rio De Janeiro'},
        {latLng: [49.282729, -123.120738], name: 'Vancuver'},
        {latLng: [35.689487, 139.691706], name: 'Tokio'},
        {latLng: [55.755826, 37.617300], name: 'Moskva'},
        {latLng: [43.214050, 27.914733], name: 'Varna'},
        {latLng: [30.044420, 31.235712], name: 'Cairo'}
    ]
});

// Panels
(function ($) {

    $(function () {
        $('.panel')
                .on('panel:toggle', function () {
                    var $this,
                            direction;

                    $this = $(this);
                    direction = $this.hasClass('panel-collapsed') ? 'Down' : 'Up';

                    $this.find('.panel-body, .panel-footer')[ 'slide' + direction ](200, function () {
                        $this[ (direction === 'Up' ? 'add' : 'remove') + 'Class' ]('panel-collapsed')
                    });
                })
                .on('panel:dismiss', function () {
                    var $this = $(this);

                    if (!!($this.parent('div').attr('class') || '').match(/col-(xs|sm|md|lg)/g) && $this.siblings().length === 0) {
                        $row = $this.closest('.row');
                        $this.parent('div').remove();
                        if ($row.children().length === 0) {
                            $row.remove();
                        }
                    } else {
                        $this.remove();
                    }
                })
                .on('click', '[data-panel-toggle]', function (e) {
                    e.preventDefault();
                    $(this).closest('.panel').trigger('panel:toggle');
                })
                .on('click', '[data-panel-dismiss]', function (e) {
                    e.preventDefault();
                    $(this).closest('.panel').trigger('panel:dismiss');
                })
                /* Deprecated */
                .on('click', '.panel-actions a.fa-caret-up', function (e) {
                    e.preventDefault();
                    var $this = $(this);

                    $this
                            .removeClass('fa-caret-up')
                            .addClass('fa-caret-down');

                    $this.closest('.panel').trigger('panel:toggle');
                })
                .on('click', '.panel-actions a.fa-caret-down', function (e) {
                    e.preventDefault();
                    var $this = $(this);

                    $this
                            .removeClass('fa-caret-down')
                            .addClass('fa-caret-up');

                    $this.closest('.panel').trigger('panel:toggle');
                })
                .on('click', '.panel-actions a.fa-times', function (e) {
                    e.preventDefault();
                    var $this = $(this);

                    $this.closest('.panel').trigger('panel:dismiss');
                });
    });

})(jQuery);

//tooltips
$(function () {
    $('[data-toggle="tooltip"]').tooltip();
    $('[data-toggle="popover"]').popover()
});


//waves effects
  Waves.attach('.button-wave', ['waves-button', 'waves-light']);
            Waves.init();