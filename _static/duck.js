$(document).ready(function(){
    $(".logo").hover(
        function() {$(this).attr("src","_static/duck_book.png");},
        function() {$(this).attr("src","_static/qa_of_code_favicon.png");
    });
});