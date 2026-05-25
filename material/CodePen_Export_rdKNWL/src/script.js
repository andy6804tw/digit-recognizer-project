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