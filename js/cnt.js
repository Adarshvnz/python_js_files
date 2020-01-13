var c1=document.querySelectorAll("#a");
var c2=document.querySelectorAll("#b");
var c3=document.querySelectorAll("#c");
var c4=document.querySelectorAll("#d");
var c5=document.querySelectorAll("#e");
var c6=document.querySelectorAll("#f");
var c7=document.querySelectorAll("#g");
var c8=document.querySelectorAll("#h");

var rest=document.querySelector("h2");
var crcl=document.querySelectorAll("td");
var cnt=1;

function clear() {
  for (var i = 0; i < crcl.length; i++) {
       crcl[i].style.backgroundColor="white";
     }
j=7;
k=7;
l=7;
m=7;
n=7;
o=7;
p=7;
q=7;
}
rest.addEventListener("click",clear)


function color1() {
  if (cnt===1) {
    c1[j].style.backgroundColor="blue";
    cnt=2;
    j--;
  }
  else if (cnt===2) {
    c1[j].style.backgroundColor="red";
    cnt=1;
    j--;
  }
}
for (var i = 0; i < c1.length; i++) {
  c1[i].addEventListener("click",color1)
var j=7;
  }


  function color2() {
    if (cnt===1) {
      c2[k].style.backgroundColor="blue";
      cnt=2;
      k--;
    }
    else if (cnt===2) {
      c2[k].style.backgroundColor="red";
      cnt=1;
      k--;
    }
  }
  for (var i = 0; i < c2.length; i++) {
    c2[i].addEventListener("click",color2)
    var k=7;
  }


  function color3() {
    if (cnt===1) {
      c3[l].style.backgroundColor="blue";
      cnt=2;
      l--;
    }
    else if (cnt===2) {
      c3[l].style.backgroundColor="red";
      cnt=1;
      l--;
    }
  }
  for (var i = 0; i < c3.length; i++) {
    c3[i].addEventListener("click",color3)
    var l=7;
  }


  function color4() {
    if (cnt===1) {
      c4[m].style.backgroundColor="blue";
      cnt=2;
      m--;
    }
    else if (cnt===2) {
      c4[m].style.backgroundColor="red";
      cnt=1;
      m--;
    }
  }
  for (var i = 0; i < c4.length; i++) {
    c4[i].addEventListener("click",color4)
    var m=7;
  }


  function color5() {
    if (cnt===1) {
      c5[n].style.backgroundColor="blue";
      cnt=2;
      n--;
    }
    else if (cnt===2) {
      c5[n].style.backgroundColor="red";
      cnt=1;
      n--;
    }
  }
  for (var i = 0; i < c5.length; i++) {
    c5[i].addEventListener("click",color5)
    var n=7;
  }


  function color6() {
    if (cnt===1) {
      c6[o].style.backgroundColor="blue";
      cnt=2;
      o--;
    }
    else if (cnt===2) {
      c6[o].style.backgroundColor="red";
      cnt=1;
      o--;
    }
  }
  for (var i = 0; i < c6.length; i++) {
    c6[i].addEventListener("click",color6)
    var o=7;
  }


  function color7() {
    if (cnt===1) {
      c7[p].style.backgroundColor="blue";
      cnt=2;
      p--;
    }
    else if (cnt===2) {
      c7[p].style.backgroundColor="red";
      cnt=1;
      p--;
    }
  }
  for (var i = 0; i < c7.length; i++) {
    c7[i].addEventListener("click",color7)
    var p=7;
  }


  function color8() {
    if (cnt===1) {
      c8[q].style.backgroundColor="blue";
      cnt=2;
      q--;
    }
    else if (cnt===2) {
      c8[q].style.backgroundColor="red";
      cnt=1;
      q--;
    }
  }
  for (var i = 0; i < c8.length; i++) {
    c8[i].addEventListener("click",color8)
    var q=7;
  }
