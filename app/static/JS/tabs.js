document.addEventListener('DOMContentLoaded', function() {
   var el = document.querySelectorAll('.tabs');
   var options = {swipeable: true};
   var instances = M.Tabs.init(el, options);
});