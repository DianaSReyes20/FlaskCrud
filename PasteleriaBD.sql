create database pasteleria;
use pasteleria;

CREATE TABLE PERSONA_EXTERNA (
    cedula varchar(10) not null,
    nombre varchar(40) not null,
    direccion varchar(40) not null,
    primary key (cedula) 
    ) engine = InnoDB;
    
    CREATE TABLE EMPRESA (
    NIT varchar(10) not null,
    nombre varchar(40) not null,
    direccion varchar(40) not null,
    primary key (NIT) 
    ) engine = InnoDB;
    
    CREATE TABLE EMPLEADO (
    codigo varchar(10) not null,
    nombre varchar(40) not null,
    salario double not null,
    primary key (codigo) 
    ) engine = InnoDB;
    
    CREATE TABLE PASTELERO (
    codigo varchar(10) not null,
    numero_pasaporte int(20) not null,
    pais_origen varchar(20) not null,
    experiencia float(5) not null,
    recomendacion varchar(40),
    primary key (numero_pasaporte),
    FOREIGN KEY (codigo) REFERENCES EMPLEADO(codigo)
    ) engine = InnoDB;
    
    CREATE TABLE PASTEL (
    nombre_pastel varchar(20) not null,
    tipo_pastel varchar(20) not null,
    peso_minimo float(6) not null,
    primary key (nombre_pastel) 
    ) engine = InnoDB;
    
    CREATE TABLE INGREDIENTE (
    nombre varchar(30) not null,
    cantidad float(10) not null,
    unidad_medida varchar(20) not null,
    nombre_pastel varchar(20) not null,
    primary key (nombre),
	FOREIGN KEY (nombre_pastel) REFERENCES PASTEL(nombre_pastel)
    ) engine = InnoDB;
    
    CREATE TABLE ORDEN (
    codigo_orden varchar(10) not null,
    fecha_solicitud date not null,
    fecha_entrega date not null,
    especificaciones varchar(100),
    nombre_pastel varchar(20) not null,
	cedula varchar(10) not null,
    codigo varchar(10) not null,
    nombre varchar(30) not null,
    primary key (codigo_orden),
    FOREIGN KEY (cedula) REFERENCES PERSONA_EXTERNA(cedula),
    FOREIGN KEY (nombre_pastel) REFERENCES PASTEL(nombre_pastel),
    FOREIGN KEY (nombre) REFERENCES INGREDIENTE(nombre),
	FOREIGN KEY (codigo) REFERENCES EMPLEADO(codigo)
   ) engine = InnoDB;
    
    CREATE TABLE DECORADO (
    id_decorado varchar(10) not null,
    fecha_inicio date not null,
    fecha_fin date not null,
    peso_final float(10) not null,
    nombre_pastel varchar(10) not null,
    primary key (id_decorado),
    FOREIGN KEY (nombre_pastel) REFERENCES PASTEL(nombre_pastel)
    ) engine = InnoDB;
    
    CREATE TABLE HORNEADO (
    id_horneado varchar(10) not null,
    temperatura_coccion float(10) not null,
    fecha_inicio date not null,
    fecha_fin date not null,
    nombre_pastel varchar(20) not null,
    primary key (id_horneado),
    FOREIGN KEY (nombre_pastel) REFERENCES PASTEL(nombre_pastel)
    ) engine = InnoDB;
    
    CREATE TABLE HORNO (
    codigo varchar(10) not null,
    marca varchar(40) not null,
    valor_actual double not null,
    primary key (codigo) 
    ) engine = InnoDB;