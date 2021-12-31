"use strict";
let pageTitle = "";

for (let index = document.location.href.length - 1; index >= 0; index--) {
    if (document.location.href[index] === "/") break;
    pageTitle += document.location.href[index];
}

pageTitle = pageTitle.split("").reverse().join("");
pageTitle = pageTitle.at(0).toUpperCase() + pageTitle.slice(1);
// console.log(pageTitle);

if (!pageTitle) document.title = "notLinkedin";
else document.title = `${pageTitle} | notLinkedin`;
