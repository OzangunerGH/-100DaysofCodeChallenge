/**
  We're defining the event on the `body` element,
  because we know the `body` is not going away.
  Second argument makes sure the callback only fires when
  the `click` event happens only on elements marked as `data-editable`
*/



$('body').on('click', '[data-editable]', function(){

  var $el = $(this);

  var $input = $('<input name="lname" maxlength="50"/>').val( $el.text() );
  $el.replaceWith( $input );

  var save = function(){
    var $p = $('<h2 data-editable />').text( $input.val() );
    $input.replaceWith( $p );
  };

  /**
    We're defining the callback with `one`, because we know that
    the element will be gone just after that, and we don't want
    any callbacks leftovers take memory.
    Next time `p` turns into `input` this single callback
    will be applied again.
  */
  $input.one('blur', save).focus();

});

