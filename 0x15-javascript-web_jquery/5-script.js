// addind an item to the list
const $ = window.$;
$('DIV#add_item').click(function () {
  const item = '<li>Item</li>';
  $('UL.my_list').append(item);
});
