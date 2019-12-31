/**
 * initial target number
 */
const targetNumber=document.getElementById("targetNumber");
let target=Math.floor(Math.random() * 10); 

targetNumber.innerText=target;

/** 
 * reflash target number
 */
const reflash=()=>{
  target=Math.floor(Math.random() * 10); 
  targetNumber.innerText=target;
  clearCanvas(canvas,ctx);
  document.body.style.backgroundImage ="linear-gradient(rgba(25, 181, 254, 0.6),rgba(166, 219, 255, 0.822)),linear-gradient(rgba(0, 0, 0, 0.6),rgba(0, 0, 0, 0.6))";
}

/** 
 * check predict number is same with ground true and change background style(green/red) 
 */
const checkCorrect=(index)=>{
  if(target==index){
    document.body.style.backgroundImage = "linear-gradient(rgba(25, 254, 178, 0.6),rgba(202, 255, 166, 0.822)),linear-gradient(rgba(0, 0, 0, 0.6),rgba(0, 0, 0, 0.6))";
  }else{
    document.body.style.backgroundImage = "linear-gradient(rgba(254, 25, 75, 0.6),rgba(255, 179, 166, 0.822)),linear-gradient(rgba(0, 0, 0, 0.6),rgba(0, 0, 0, 0.6))"
  }
}