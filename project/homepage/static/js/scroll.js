document.addEventListener('DOMContentLoaded', function() {

  // Window function to lock time progress bar at the top when event happens
  window.addEventListener('scroll', myScroll);

  // Get the progress bar
  var head_progress = document.getElementById("myProgress");

  // Get the offset position of the progress bar
  var sticky = head_progress.offsetTop;

  // Add the sticky class to the navbar when you reach its scroll position.
  // Remove "sticky" when you leave the scroll position
  function myScroll()
  {
    if (window.pageYOffset > sticky)
    {
      head_progress.classList.add("sticky");
    } else
    {
      head_progress.classList.remove("sticky");
    }
  }

  // Reducing timer
  var timer,
      width;
  var time_left = 1200;
  var bar = document.getElementById("bar");

  function reduce(){
    var min = Math.floor(time_left / 60);
    var sec = time_left % 60;
    if (time_left >= 0)
    {
        if (min < 10)
        {
            min = "0" + min;
        }
        if (sec < 10)
        {
            sec = "0" + sec;
        }
        document.getElementById("countdown").innerHTML = min + ":" + sec;
        // Move progress bar width
        width = (time_left * 100) / 1200;
        bar.style.width = width + "%";
    }
    if (time_left <= 0)
    {
        clearTimeout(timer);
        document.getElementById("iqtest").submit();
        return;
    }
    time_left--;
    timer = setTimeout(reduce, 1000);
  }
  // Run function for countdown
  reduce();

})