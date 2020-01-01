/** 
 * add animation after first animation end 
 **/
var minutes = document.querySelector('.clock');
var sun = document.querySelector('.sun');
var marker = document.querySelector('.marker');
var centerComposition = document.querySelector('.center-composition');

minutes.addEventListener('animationend', function () {
  minutes.classList.add('start');
});

sun.addEventListener('animationend', function () {
  sun.classList.add('start');
});

marker.addEventListener('animationend', function () {
  marker.classList.add('start');
});

centerComposition.addEventListener('animationend', function () {
  centerComposition.classList.add('start');
});

/**
 * 
 */
document.body.onscroll = function (event) {
  const html = document.documentElement;
  if (html.scrollTop > 1000 && html.scrollTop < 2000) {
    const sectionAnimate = document.getElementById("sectionAnimate");
    sectionAnimate.classList.remove("d-none");
  }else if(html.scrollTop > 2050){
    const sectionSource=document.getElementById("sectionSource");
    sectionSource.classList.remove("d-none");
  }
  console.log(html.scrollTop)
};


/** 
 * Main background digit particle effect 
 **/
const sectionParticle=document.getElementById("sectionParticle");
str='';
for(let i=1;i<=80;i++){
  str+=`<span class='particle'>${((i/i+Math.floor(Math.random() * 10))-1)}</span>`;
}
sectionParticle.innerHTML=str;