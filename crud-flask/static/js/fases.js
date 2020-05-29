function mostrar(id) {
    if (id == "decorado") {
        $("#decorado").show();
        $("#horneado").hide();
    }

    if (id == "horneado") {
        $("#horneado").show();
        $("#decorado").hide();

    }

}