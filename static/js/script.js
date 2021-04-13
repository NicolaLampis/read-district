$(document).ready(function(){
    $('.sidenav').sidenav({edge: "right"});
    $('select').formSelect();
    $('textarea#text_review').characterCounter();

    $('.materialboxed').materialbox();

    $('.my-action-btn').floatingActionButton({
        hoverEnabled: false,
        direction: 'top',
        isOpen: true
    });

});

