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