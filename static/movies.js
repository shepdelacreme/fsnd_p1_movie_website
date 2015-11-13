$(document).ready(function() {
    // Animate in the movies when the page loads
    $('.movie-tile').hide().first().show("fast", function showNext() {
        $(this).next("div").show("fast", showNext);
    });

    // Init popovers
    $(function () {
      $('[data-toggle="popover"]').popover();
    });

    // Pause/remove the video when the modal is closed
    $('#trailerModal').on('hidden.bs.modal', function(event) {
        $(this).find('.modal-body iframe').removeAttr('src');
    });

    // Start playing the video when the trailer modal is opened
    // Set the modal title to the movie title
    $('#trailerModal').on('show.bs.modal', function(event) {
        var trigger = $(event.relatedTarget);
        var sourceUrl = 'http://www.youtube.com/embed/' +  trigger.data('youtube-id') + '?autoplay=1&html5=1';
        $(this).find('#modal-movie-title').text(trigger.data('movie-title'));
        $(this).find('.modal-body iframe').attr('src', sourceUrl);
    });
});
