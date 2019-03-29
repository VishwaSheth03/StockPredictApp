//Sticky Menu Background 
window.addEventListener('scroll', function (){
  if (window.scrollY > 150) {
    document.querySelector('#navbar, #clients').style.opacity = 0.9;
  } else {
    document.querySelector('#navbar, #clients').style.opacity = 1;
  }
});

//Smooth Scrolling
$('#navbar a, .btn, #clients a, .items').on('click', function(event) {
  if (this.hash !== '') {
    event.preventDefault();

    const hash = this.hash;

    $('html, body').animate(
      {
        scrollTop: $(hash).offset().top - 64
      },
      800
    );
  }
});