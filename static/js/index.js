const navbtn = document.querySelector('.nav-btn');
const navlinks = document.querySelectorAll('.mynav_link');
window.onscroll = function() {myFunction()};

var header = document.querySelector("header");
var sticky = header.offsetTop;

function myFunction() {
  if (window.pageYOffset > sticky) {
    header.classList.add("sticky");
  } else {
    header.classList.remove("sticky");
  }
}
navbtn.addEventListener('click',() =>{
    document.body.classList.toggle('open-nav');
});
var el = document.querySelectorAll(".mynav_item");
//var one = el.previousSibling();
el.forEach(list => {
    list.addEventListener('click',function(){
//       list.children[0].style.color='red';
//        alert(list.getAttribute('class'));
        el.forEach(navlist => {
            navlist.classList.remove('active');
        });
        list.classList.add('active');
    });
});
navlinks.forEach(link => {
    link.addEventListener('click', () => {
        document.body.classList.remove('open-nav');
    });
});


var appendStyle = function(selector, prop, val) {
  var style = document.createElement("style");
  document.head.appendChild(style);
  
  style.sheet.addRule(selector, prop +": "+ val);
};
var footer = document.querySelector('.footer');
var footerAfter = ".footer::after";

footer.addEventListener('dblclick',()=>{
    footer.style.bottom = "-7em";
    appendStyle(footerAfter, "top", "-1.30em");
    appendStyle(footerAfter, "border-width", "0 25px 25px");
    appendStyle(footerAfter, "border-color", "#150907 transparent");
});
footer.addEventListener('click',()=>{
    footer.style.bottom = "-.99em";
    footer.classList.add('footerTrans');
//    window.getComputedStyle(footer,":after").getPropertyValue("left");
    appendStyle(footerAfter, "top", "-.01em");
    appendStyle(footerAfter, "border-width", "25px 25px 0");
    appendStyle(footerAfter, "border-color", "#FCECE1 transparent");
});
//const activate= this.getAttribute("href");
//        alert(activate);