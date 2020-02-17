document.addEventListener('DOMContentLoaded', function() {
            let elems = document.querySelectorAll('.datepicker');
            let options = {
                            onOpen: () => {console.log('open')},
                            onClose: function() {
                                    window.location.href="/games/"
                                        .concat((Date.parse(this.el.value)).toString());},
                            container: 'body'
                            };
            let instances = M.Datepicker.init(elems, options);
          });


document.addEventListener('DOMContentLoaded', function() {
    let elems = document.querySelectorAll('.sidenav');
    let options = {draggable: true,
                   preventScrolling: true};
    let instances = M.Sidenav.init(elems, options);
  });
