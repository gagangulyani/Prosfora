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
    $('.site-space-background').fadeIn(0); //this is new, will fade in smoothly
}

function changeBackgroundSmoothly() {
    $('.site-space-background').fadeOut(0, changeBg); //this is new, will fade out smoothly
}

setInterval(changeBackgroundSmoothly,10000);