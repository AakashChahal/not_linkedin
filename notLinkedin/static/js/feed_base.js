"use strict";
let pageTitle = "";

for (let index = document.location.href.length - 1; index >= 0; index--) {
    if (document.location.href[index] === "/") break;
    pageTitle += document.location.href[index];
}

pageTitle = pageTitle.split("").reverse().join("");
// console.log(pageTitle);

if (!pageTitle) document.title = "notLinkedin";
else
    document.title = `${
        pageTitle.at(0).toUpperCase() + pageTitle.slice(1)
    } | notLinkedin`;

const currPageIcon = document.querySelector(`.${pageTitle}`);
// currPageIcon.closest("li").style.borderBottom = "2px solid black";
currPageIcon.closest("li").style.boxShadow = "1px 1px 0 black";
