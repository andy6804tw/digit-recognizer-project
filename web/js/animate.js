// add animation after first animation end
var minutes = document.querySelector('.clock');
var sun = document.querySelector('.sun');
var marker = document.querySelector('.marker');
var centerComposition = document.querySelector('.center-composition');

minutes.addEventListener('animationend', function(){
  minutes.classList.add('start');
});

sun.addEventListener('animationend', function(){
  sun.classList.add('start');
});

marker.addEventListener('animationend', function(){
  marker.classList.add('start');
});

centerComposition.addEventListener('animationend', function(){
  centerComposition.classList.add('start');
});

const start=()=>{
  const sectionAnimate=document.getElementById("sectionAnimate");
  sectionAnimate.classList.remove('d-none');
  
  const itemClock=document.getElementById("itemClock");
  const pinkBall=document.getElementById("pinkBall");
  const pinkArrow=document.getElementById("pinkArrow");
  const dashPink=document.getElementById("dashedPink");

  itemClock.classList.add("scale-animation","delay-730");
  pinkBall.classList.add("scale-animation","delay-830");
  pinkArrow.classList.add("scale-animation","delay-1030");
  dashPink.classList.add("dashed-pink");
}