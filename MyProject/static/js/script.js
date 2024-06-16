const Navbar=document.getElementById("Navbar")
const NavbarFake=document.getElementById("NavbarFake")

window.addEventListener('scroll',()=>{
    if (window.scrollY>=500){
        Navbar.style.position="fixed";
    }else if(window.scrollY<500){
        Navbar.style.position="sticky"
    }


    if (window.scrollY>=500){
        NavbarFake.style.position="sticky"
    }else if(window.scrollY<500){
        NavbarFake.style.position="fixed"
    }
    
})

window.onload=()=>{
    window.scrollTo(0, 0);
}


const allSection=document.querySelectorAll('section');
const allNavlink=document.querySelectorAll('header a');



allNavlink.forEach((e) => {
    e.addEventListener('click', (f) => {
       
        allNavlink.forEach(link => link.classList.remove('active'));
        
       
        e.classList.add('active');
        
    });
});