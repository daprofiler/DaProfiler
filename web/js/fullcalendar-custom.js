$(document).ready(function () {


    /* initialize the external events
     -----------------------------------------------------------------*/

    $('#external-events .fc-event').each(function () {

        // store data so the calendar knows to render an event upon drop
        $(this).data('event', {
            title: $.trim($(this).text()), // use the element's text as the event title
            stick: true // maintain when user navigates (see docs on the renderEvent method)
        });

        // make the event draggable using jQuery UI
        $(this).draggable({
            zIndex: 999,
            revert: true, // will cause the event to go back to its
            revertDuration: 0  //  original position after the drag
        });

    });


    /* initialize the calendar
     -----------------------------------------------------------------*/

    $('#calendar').fullCalendar({
         events: [
				{
					title: 'All Day Event',
					start: '2015-09-05'
                                },
                                {
					title: 'Meeting',
                                        start: '2015-09-14T10:30:00',
					end: '2015-02-12T12:30:00'

                                },
                                {
					title: 'Conference',
					start: '2015-09-19'
                                },
                                {
					title: 'Birthday party',
					start: '2015-09-20'
                                }
                            ],
        header: {
            left: 'prev,next today',
            center: 'title',
            right: 'month,agendaWeek,agendaDay'
        },
        editable: true,
        droppable: true, // this allows things to be dropped onto the calendar
        drop: function () {
            // is the "remove after drop" checkbox checked?
            if ($('#drop-remove').is(':checked')) {
                // if so, remove the element from the "Draggable Events" list
                $(this).remove();
            }
        }
       
    });


});




