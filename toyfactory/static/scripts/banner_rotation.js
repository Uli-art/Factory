let banners = document.querySelectorAll(".slider_item");
let interval = 4000;
let rotationTimer;
let currentImage = 0;

function startRotation() {
    rotationTimer = setInterval(rotateBanners, interval);
}

function stopRotation() {
    clearInterval(rotationTimer);
}

function rotateBanners() {
    currentImage = (currentImage + 1) % banners.length;
    console.log(banners)
    banners.forEach((element, index) => {
        banners[index].style.transform = `translateX(${-100 * currentImage}%)`;
    });
}

function changeSpeed() {
    const newInterval = parseInt(document.getElementById('rotationSpeed').value, 10) * 1000;
    if (!isNaN(newInterval)) {
        interval = newInterval;
        stopRotation();
        startRotation();
    }
}

document.addEventListener('visibilitychange', function () {
    if (document.visibilityState === 'visible') {
        startRotation();
    } else {
        stopRotation();
    }
});

startRotation();