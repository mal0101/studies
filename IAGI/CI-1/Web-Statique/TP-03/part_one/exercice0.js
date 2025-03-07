//accès par id
function ChangeColor(newColor){
    var elem = document.getElementById('para');
    elem.innerHTML = "Bravo ! ";
    elem.style.color = newColor;
}
//accés par tagname
var Bout = document.getElementsByTagName('button');
alert('Nb Bouton: ' + Bout.length);
// retour sous forme des tableaux
var par = document.getElementsByTagName('p');
alert('Premier par: ' + par[0].innerHTML);
//query selector
el = document.querySelector(".maclasse");