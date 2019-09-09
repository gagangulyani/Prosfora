var imgs = new Array("camera2.jpg","cinema.jpg","drums.jpg","guitar.jpg");

function changeBg() {
    var imgUrl = imgs[Math.floor(Math.random()*imgs.length)];
    $('.site-space-background').css('background-image', 'url("/static/images/' + imgUrl + '")');
    $('.site-space-background').fadeIn(1000); //this is new, will fade in smoothly
}

function changeBackgroundSmoothly() {
    $('.site-space-background').fadeOut(1000, changeBg); //this is new, will fade out smoothly
}

setInterval(changeBackgroundSmoothly,10000);