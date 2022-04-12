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

function addRow() { //Not working properly
    
    //Find a <table> element with id="myTable"
    var table = document.getElementById("myTable")

    //Create an empty <tr> element and add it to the last position of the table:
    var row = table.insertRow(0);

    //Insert new cells (<td elements) at the 1st and 2nd position of the "new" <tr> element:
    var cell1 = row.inserCell(0)
    var cell2 = row.inserCell(1)

    cell1.innerHTML = "NEW CELL1";
    cell2.innerHTML = "NEW CELL2";
}


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


