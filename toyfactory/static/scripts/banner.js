const mountainLeft = document.querySelector('#mountain_left');
const mountainRight = document.querySelector('#mountain_right');
const text = document.querySelector('#text');
const spin1 = document.querySelector('#spin1');
const spin2 = document.querySelector('#spin2');

window.addEventListener('scroll',()=>{
    let value = scrollY;
    mountainLeft.style.left = `-${value/0.7}px`
    mountainRight.style.left = `${value/0.7}px`
    text.style.bottom = `-${value}px`;
    spin1.style.transform = "rotate(" + window.pageYOffset + "deg)";
    spin2.style.transform = "rotate(" + window.pageYOffset + "deg)";
})