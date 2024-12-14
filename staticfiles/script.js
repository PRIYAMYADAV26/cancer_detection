$(document).ready(function () {
  var scroll_start = 0;
  var startchange = $(".title");
  var offset = startchange.offset();



  if (startchange.length) {
      $(document).scroll(function () {
          scroll_start = $(this).scrollTop();
          if (scroll_start > offset.top) {
              $(".navbar").css('background-color', 'rgba(255,255,255,.9)');
              $(".menu").css('color', 'rgb(0,0,0)');
              $(".logo a").css('color', 'rgb(0,0,0)');
            
          } else {
              $('nav').css('background-color', 'transparent');
              $(".menu").css('color', 'rgb(255,255,255)');
              $(".logo a").css('color', 'rgb(255,255,255)');
          }
      });
  }
});

