$(document).ready(function () {
  function translate () {
    const lang = $('#language_code').val();
    $.get(`https://www.fourtonfish.com/hellosalut/hello/?lang=${lang}`, function (data) {
      $('#hello').text(data.hello);
    });
  }

  $('#btn_translate').click(translate);

  $('#language_code').keypress(function (e) {
    if (e.which === 13) { // Enter key pressed
      translate();
    }
  });
});
