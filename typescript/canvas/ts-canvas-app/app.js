"use strict";
// app.ts
const canvas = document.getElementById("myCanvas");
const ctx = canvas.getContext("2d");
// تنظیمات اولیه
let x = canvas.width / 2;
let y = canvas.height / 2;
const radius = 30;
let dx = 2; // سرعت حرکت در جهت X
let dy = 2; // سرعت حرکت در جهت Y
// تابع برای رسم دایره
function drawCircle() {
    ctx.beginPath();
    ctx.arc(x, y, radius, 0, Math.PI * 2);
    ctx.fillStyle = "blue";
    ctx.fill();
    ctx.closePath();
}
// تابع برای پاک کردن Canvas
function clearCanvas() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
}
// تابع برای به‌روزرسانی موقعیت دایره
function update() {
    // تغییر موقعیت دایره
    x += dx;
    y += dy;
    // برخورد با لبه‌های Canvas
    if (x + radius > canvas.width || x - radius < 0) {
        dx = -dx;
    }
    if (y + radius > canvas.height || y - radius < 0) {
        dy = -dy;
    }
}
// تابع اصلی انیمیشن
function animate() {
    clearCanvas();
    drawCircle();
    update();
    requestAnimationFrame(animate);
}
// شروع انیمیشن
animate();
