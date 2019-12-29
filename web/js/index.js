const targetNumber=document.getElementById("targetNumber");
let target=Math.floor(Math.random() * 10); 

targetNumber.innerText=target;

/** Reflash target */
const reflash=()=>{
  target=Math.floor(Math.random() * 10); 
  targetNumber.innerText=target;
  clearCanvas(canvas,ctx);
}

const checkCorrect=(index)=>{
  if(target==index){
    document.body.style.backgroundImage = "linear-gradient(rgba(25, 254, 178, 0.6),rgba(202, 255, 166, 0.822)),linear-gradient(rgba(0, 0, 0, 0.6),rgba(0, 0, 0, 0.6))";
  }else{
    document.body.style.backgroundImage = "linear-gradient(rgba(254, 25, 75, 0.6),rgba(255, 179, 166, 0.822)),linear-gradient(rgba(0, 0, 0, 0.6),rgba(0, 0, 0, 0.6))"
  }
}