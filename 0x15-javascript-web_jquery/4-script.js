//  script that toggles the class of the <header> element when the user clicks on the tag DIV#toggle_header:
const $ = window.$;
if ($('DIV#toggle_header')) {
  $('DIV#toggle_header').click(function () {
    $('header').toggleClass('red green');
  });
}
