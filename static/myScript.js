//A function to show or hide the Complementary files input group in index.html
function showHide(){
    var checkbox = document.getElementById("chk")
    var hiddeninputs = document.getElementsByClassName("hidden")


    for (var i = 0; i != hiddeninputs.length; i++ ) {
        if(checkbox.checked){
            hiddeninputs[i].style.display = "block"
        }
        else {
            hiddeninputs[i].style.display = "none"
        }
    }
}

//A function to show or hide the Track(s) TextArea upon selecting "Defined By Rule" in Select.
function showDiv(divId, element)
{
    document.getElementById(divId).style.display = element.value == 1 ? 'block' : 'none';
}



function addRow(divId) {
    //Find a <table> element with divId"

    console.log("ADD ROW!!")

    var table = document.getElementById(divId);

    //Create an empty <tr> element and add it to the last position of the table:
    row = table.insertRow(-1);

    //Count the number of columns

    length = document.getElementById(divId).rows[0].cells.length

    //Insert new cells (<td> elements) at the nth position of the table. Make the new cells as an input group (text). Add a "form-control" class. Append the newly created cells at the bottom. 
    for (i = 0; i < length; i++ ) {
        row.insertCell(i).appendChild(document.createElement('input')).classList.add("form-control");
    }

}


function deleteRow (divId) {
    var table = document.getElementById(divId);

    //Prevent the header not be removed    
    if (table.rows.length != 1) {
        table.deleteRow(-1);
    }
    
    
}

//Obsolete function. Needs to be refactored like toggleSelect4
function toggleSelect()
{
    var isChecked = document.getElementById("track1_check").checked
    document.getElementById("track1_select").disabled = !isChecked;

}
function toggleSelect1()
{
    var isChecked = document.getElementById("track2_check").checked
    document.getElementById("track2_select").disabled = !isChecked;
    
} 

function toggleSelect2()
{
    var isChecked = document.getElementById("track3_check").checked
    document.getElementById("track3_select").disabled = !isChecked;
} 

//Obsolete function. Needs to be refactored to toggleSelect4
function toggleSelect3()
{
    var hiddenEmv = document.getElementById("hiddenEmv")
    var isChecked = document.getElementById("deskeys_check").checked
    document.getElementById("deskeys_select").disabled = !isChecked;

    if (isChecked){
        hiddenEmv.style.display = "block"
    }
    else {
        hiddenEmv.style.display = "none"
    } 
    
} 

// A function to show/hide contents of a div when the checkbox is checked.
function toggleSelect4(divId_hidden, divId_check, divId_select, element)
{
    var element = document.getElementById(divId_hidden)
    var isChecked = document.getElementById(divId_check).checked
    document.getElementById(divId_select).disabled = !isChecked;

    if (isChecked){
        element.style.display = "block"
    }
    else {
        element.style.display = "none"
    } 
    
}





//JavaScript Client Validation
/*
window.addEventListener('load', 
  function() { 
    var nodes = document.querySelectorAll("input[type=text]");
        for (var i=0; i<nodes.length; i++)
    {
        console.log(nodes[i].value);
    }
  }, false);
*/