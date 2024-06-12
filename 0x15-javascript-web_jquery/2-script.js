// Write a JavaScript script that updates the text color of the <header> element to red (#FF0000) when the user clicks on the tag DIV#red_header:
// You can’t use document.querySelector to select the HTML tag
// You must use the jQuery API
const $ = window.$;
const rHeader = $('DIV#red_header');
rHeader.click(function () {
  $('header').css('color', '#FF0000');
});
