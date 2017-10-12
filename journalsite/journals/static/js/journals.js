function hello() {
            var frm = document.getElementById("entry-select");
            frm.submit();
}

function entryChange() {
            var frm = document.getElementById("entry-select");
            frm.submit();
}

function setValue(id) {
    if (id ==1){
        document.getElementById("option_1").selected = 'selected';
    } else if(id ==2){
        document.getElementById("option_2").selected = 'selected';
    }
}

function myFunction() {
    document.getElementById("list_seletor").value = document.getElementById("id_entry_list").value;
    // alert(document.getElementById("list_seletor").value)

}
