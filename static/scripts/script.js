if (loggedIn){
    $('.login').remove();
    $('.register').remove();
    $('.logout').toggleClass('d-none');
    $('.submit-a-photo').css('background', 'rgba(0,0,0,0.8)');
    $('.submit-a-photo').css("color", 'white');
    $('.joinNow').text('Now')
}
var imgs = new Array(
"avel-chuklanov-rWazZf6qDFM-unsplash.jpg",
"celine-druguet-ttzoSPBYdrI-unsplash.jpg",
"chris-bair-A10y2Eq7OHY-unsplash.jpg",
"clem-onojeghuo-xJXxMR5PXoY-unsplash.jpg",
"david-hurley-hjSt16JGyEE-unsplash.jpg",
"davisco-rhUU1pemhQ0-unsplash.jpg",
"jakob-owens-CiUR8zISX60-unsplash.jpg",
"keagan-henman-pPxJTtxfV1A-unsplash.jpg",
"allef-vinicius-P2BoE6tb8ig-unsplash.jpg");

function changeBg() {
    var imgUrl = imgs[Math.floor(Math.random()*imgs.length)];
    $('.site-space-background').css('background-image', 'url("/static/images/backgrounds/' + imgUrl + '")');
    $('.site-space-background').fadeIn(1000); //this is new, will fade in smoothly
}

function changeBackgroundSmoothly() {
    $('.site-space-background').fadeOut(1000, changeBg); //this is new, will fade out smoothly
}

setInterval(changeBackgroundSmoothly,10000);