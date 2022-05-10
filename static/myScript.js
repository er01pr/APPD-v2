var rowLength = 0;


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

    var table = document.getElementById(divId);

    rowLength = table.tBodies[0].rows.length -1;

    if (table.id != 'myTable')
    {
    
            //Find a <table> element with id="myTable"
            var table = document.getElementById(divId);
    
            //Create an empty <tr> element and add it to the last position of the table:
            row = table.insertRow(-1);
    
            //Insert new cells (<td elements) at the 1st and 2nd position of the "new" <tr> element:
            var element1 = document.createElement('input');
            var element2 = document.createElement('input');
            element1.type = "text";
            element2.type = "text";
    
            element1.setAttribute("name", "app1")
            element2.setAttribute("name", "row1")
            console.log("Create Element Input!")
    
            //Add class in the elements
            element1.classList.add("form-control");
            element2.classList.add("form-control");
            console.log("Add class form-control!")
    
            cell1 = row.insertCell(0);
            cell2 = row.insertCell(1);
            console.log("Insert Cell index 1 and 2!")
    
            
            //Append the newly created cells in the table.
            cell1.appendChild(element1)
            cell2.appendChild(element2)
            console.log("Append!")
    
            //Length of Table (Columns and rows)
            rowLength = table.tBodies[0].rows.length -1;
            
            for (i=0; i<rowLength;i++)
            {
                console.log("Column" + [i]);
                element1.setAttribute("name", "app" + [i])
                element2.setAttribute("name", "applet" + [i])
            }
    }

    if (table.id == 'myTable' && rowLength < 3)
    {
        //Find a <table> element with id="myTable"
        var table = document.getElementById(divId);

        //Create an empty <tr> element and add it to the last position of the table:
        row = table.insertRow(-1);

        //Insert new cells (<td elements) at the 1st and 2nd position of the "new" <tr> element:
        var element1 = document.createElement('input');
        var element2 = document.createElement('input');
        element1.type = "text";
        element2.type = "text";

        element1.setAttribute("name", "app1")
        element2.setAttribute("name", "row1")


        //Add class in the elements
        element1.classList.add("form-control");
        element2.classList.add("form-control");


        cell1 = row.insertCell(0);
        cell2 = row.insertCell(1);


        
        //Append the newly created cells in the table.
        cell1.appendChild(element1)
        cell2.appendChild(element2)


        
        for (i=0; i<rowLength;i++)
        {
            element1.setAttribute("name", "app" + [i])
            element2.setAttribute("name", "applet" + [i])
        }

    }

    else {
        return;
    }

}

function addRow1 (divId) {

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

    console.log("Table rows length in Delete is" + table.rows.length)
    //Prevent the header not be removed    
    if (table.rows.length != 1) {
        table.deleteRow(-1);
        console.log("Delete Row!")
        console.log("The number of rows after deletion is " + table.tBodies[0].rows.length)
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