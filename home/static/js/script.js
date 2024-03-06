// window.addEventListener('scroll',function(){
//                     let navbar=document.getElementById('nav-menu');
//                     if(window.scrollY>=400)
//                     {
//                                         navbar.classList.add("sticky");
//                     }
//                     else{
//                                         navbar.classList.remove("sticky");
//                     }
// });
/*Slider*/
let flag=0;
function controller(x){
                    flag=flag+x;
                    showSlider(flag);
}

function showSlider(num){
                    let slides=document.getElementsByClassName('slider');


                    if(num==slides.length){
                                        flag=0;
                                        num=0;
                    }
                    else if(num<0){
                                        flag=slides.length-1;
                                        num=slides.length-1;
                    }
                    /*hide all other images*/
                    for(let img of slides){
                                        img.style.display="none";
                    } 
                    //*Display a Single Image Initial */
                    slides[num].style.display="block"
} 

function print(){
                    window.print();
}