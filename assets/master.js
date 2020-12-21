$(document).ready(function(){
    $("#showSearchForm").click(function(){
      $("#searchfrom").slideToggle()
    });
  });

$(window).on("load",function(){
  $(".loader-wrapper").fadeOut("slow");
});