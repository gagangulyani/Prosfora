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
    var imgUrl = imgs[Math.floor(Math.random() * imgs.length)];
    $('.site-space-background').css('background-image', 'url("/static/images/backgrounds/' + imgUrl + '")');
    $('.site-space-background').fadeIn(1000); //this is new, will fade in smoothly
}

function changeBackgroundSmoothly() {
    $('.site-space-background').fadeOut(1000, changeBg); //this is new, will fade out smoothly
}

setInterval(changeBackgroundSmoothly, 10000);

function play(card) {
    var myVideo = card.querySelector('video');
    // var card_ = $(card).children('.card-img-overlay-up');
    // var actions = $(card).children('.card-img-overlay-down');

    if (myVideo != undefined) {
        if (myVideo.paused) {
            myVideo.currentTime = 0;
            myVideo.play();
            // card_.fadeOut('slow/400/fast', function() {});
            // actions.fadeIn('slow/400/fast', function() {});
        }
    }
}

function pause(card) {
    var myVideo = card.querySelector('video');
    // var card_ = $(card).children('.card-img-overlay-up');
    // var actions = $(card).children('.card-img-overlay-down');

    if (myVideo == undefined) {
        // card_.fadeOut('slow/400/fast', function() {});
    } else {
        myVideo.currentTime = 0;
        myVideo.pause();
    }

    // actions.fadeOut('slow/400/fast', function() {});
    // card_.fadeIn('slow/400/fast', function() {});
}

if (Array(document.getElementById('wave-form-audio')).length) {
    var wavesurfer = WaveSurfer.create({
        container: '#waveform-audio',
        waveColor: 'white',
        progressColor: '#AA0000',
        barWidth: 3,
        responsive: true,
        hideScrollbar: true,
        cursorColor: 'white',
        height: 80,
    });

    wavesurfer.load('/static/audios/test/Never Leave Me (feat. Joe Janiak).mp3');
    wavesurfer.on('ready', updateTimer);
    wavesurfer.on('audioprocess', updateTimer);

    // Need to watch for seek in addition to audioprocess as audioprocess doesn't fire
    // if the audio is paused.
    wavesurfer.on('seek', updateTimer);

}


function updateTimer() {
    var formattedTime = secondsToTimestamp(wavesurfer.getCurrentTime());
    $('.duration').text(formattedTime + ' - ' + secondsToTimestamp(wavesurfer.getDuration()));
}

function secondsToTimestamp(seconds) {
    seconds = Math.floor(seconds);
    var h = Math.floor(seconds / 3600);
    var m = Math.floor((seconds - (h * 3600)) / 60);
    var s = seconds - (h * 3600) - (m * 60);

    h = h < 10 ? '0' + h : h;
    m = m < 10 ? '0' + m : m;
    s = s < 10 ? '0' + s : s;
    return h + ':' + m + ':' + s;
}

$('.playPause').click(function (event) {
    $('.playPause').toggleClass('fa-play-circle');
    $('.playPause').toggleClass('fa-pause-circle');
});
