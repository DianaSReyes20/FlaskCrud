function mostrar(id) {
    if (id == "pastelero") {
        $("#pastelero").show();
        $("#empresa").hide();
        $("#persona_externa").hide();
        $("#decorador").hide();
    }

    if (id == "empresa") {
        $("#empresa").show();
        $("#pastelero").hide();
        $("#decorador").hide();
        $("#persona_externa").hide();

    }

    if (id == "persona_externa") {
        $("#persona_externa").show();
        $("#pastelero").hide();
        $("#empresa").hide();
        $("#decorador").hide();
    }

     if (id == "decorador") {
        $("#pastelero").hide();
        $("#empresa").hide();
        $("#persona_externa").hide();
        $("#decorador").show();
    }
}