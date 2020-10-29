$(function () {
  $('#senti-but').click(function () {
    let str = 'query='.concat($('#review').val())

    $.ajax({
      url: 'https://jack-sentiment-classifier.herokuapp.com/api/',
      data: str,
      type: 'GET',
      success: function (response) {
        if (response['prediction'] == 'Negative') {
          $('body').css('background-color', '#ffa8a8')
          $('textarea').css('background-color', '#ffa8a8')
        } else if (response['prediction'] == 'Positive') {
          $('body').css('background-color', '#b3ffa9')
          $('textarea').css('background-color', '#b3ffa9')
        }
      }
    });
  });
});

