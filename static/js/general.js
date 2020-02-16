
// Открытие и закрытие бокового меню

$("#show_menu").click(function() {
  $("#main_menu").addClass("show");
  $(".navbar_title").css({"display": "none"});
  $(".backdrop").css({"left": "0", "opacity": "1"});
});

$(document).on("click", function(event){
    if(!$(event.target).closest("#show_menu").length && !$(event.target).closest("#main_menu").length){
        $("#main_menu").removeClass("show");
        $(".navbar_title").css({"display": "block"});
        $(".backdrop").css({"left": "-100%", "opacity": "0"});
    }
});

// Вкладки

$('.tabs_caption li').on('click', function() {
  //console.log($(this).parent().parent().attr('id'));
  parentId = $(this).parent().parent().attr('id');
  $(this).addClass('active');
  $(this).siblings().removeClass('active');
  $( "#" + parentId + " .tabs_content").find("textarea").val("");
  $( "#" + parentId + " .tabs_content").find("input").val("");
  $( "#" + parentId + " .tabs_content").removeClass('active').eq($(this).index()).addClass('active');
});
