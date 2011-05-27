(function($) {

  var _pics, populatePictures, removeItem;
  var pictures = [];

  populatePictures = function() {
    _pics = $('.image img');
    if (_pics.length > 0) {
      _pics.each(function(i, item) {
        pictures.push($(item).attr('id'));
      });
    }
  };

  removeItem = function(arr, item) {
    return $.grep(arr, function(value) {
      return value != item;
    });
  };

  $(function () {

    populatePictures();

    $('.discard').click(function () {
      var box = $(this).parent().parent();
      var id = box.find('.image img').attr('id');
      if (box.hasClass('keeper')) {
        box.removeClass('keeper');
      } else {
        box.fadeOut();
        pictures = removeItem(pictures, id);
      }
      return false;
    });

    $('.keep').click(function () {
      var box = $(this).parent().parent();
      var id = box.find('.image img').attr('id');
      box.addClass('keeper');
      return false;
    });

    $('#process-btn').click(function() {
      var place = prompt("Place?");
      $.post('/create-final', {pictures: pictures.join(), place: place}, function() {
        alert('Success!');
      });
      return false;
    });

    $('#proceed').click(function() {

      $.get('/process', null, function(r) {
        console.log(r);
        window.location = '/sort/';
      }); // get
      return false;
    });

  });

})(jQuery);
