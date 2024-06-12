// script that updates the contents of the <header> element
// to New Header!!! when the user clicks on DIV#update_header
const $ = window.$;
$('DIV#update_header').click(function () {
  $('header').text('New Header!!!');
});
