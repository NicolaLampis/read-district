// Materialize CSS jQuery initialisation script

$(document).ready(function(){
    // Materialize plugins: mobile-side-navigation
    $('.sidenav').sidenav({edge: "right"});
    // Materialize form
    $('select').formSelect();
    // Materialize text form with character counter
    $('textarea#text_review').characterCounter();
    // Materialize Modal window    
    $('.modal').modal();
});
