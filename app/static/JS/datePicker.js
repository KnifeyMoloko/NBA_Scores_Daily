document.addEventListener('DOMContentLoaded', function() {
            let elems = document.querySelectorAll('.datepicker');
            let options = {
                            "onOpen": () => {console.log('open')},
                            "onClose": function()
                                        {window.location.href="/games/"
                                            .concat(Date.parse(this.el.value).toString())}
            };
            let instances = M.Datepicker.init(elems, options);
          });