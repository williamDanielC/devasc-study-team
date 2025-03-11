#\. C:\Base de Datos\copia d taller.sql
#autor: Wiliam Daniel Cruz Lopez
DROP DATABASE IF EXISTS dbtaller;

CREATE DATABASE dbtaller;

USE dbtaller;

CREATE TABLE lineainv (idlinea CHAR(10) PRIMARY KEY, nombreproy VARCHAR(250));

CREATE TABLE tipoproyecto (tipo CHAR(10) PRIMARY KEY);

CREATE TABLE profesor (idprofesor INT AUTO_INCREMENT PRIMARY KEY, nombreProf VARCHAR(200));

CREATE TABLE proyecto (clave CHAR(10) PRIMARY KEY, nombreproy VARCHAR(250), idlinea CHAR(10), tipo CHAR(10),              
CONSTRAINT asignada FOREIGN KEY (idlinea) REFERENCES lineainv(idlinea),
CONSTRAINT asignado FOREIGN KEY (tipo) REFERENCES tipoproyecto(tipo));

CREATE TABLE profesorproy (idprofesor INT, clave CHAR(10), calificacion FLOAT, rol VARCHAR(45),              
CONSTRAINT revisa FOREIGN KEY (idprofesor) REFERENCES profesor(idprofesor),
CONSTRAINT es_revisado FOREIGN KEY (clave) REFERENCES proyecto(clave));

CREATE TABLE alumno (nocontrol CHAR(10) PRIMARY KEY, nombre VARCHAR(150), clave CHAR(10),                 
CONSTRAINT participan FOREIGN KEY (clave) REFERENCES proyecto(clave));

LOAD DATA LOCAL INFILE 'C:/Base de Datos/cargar.csv'
INTO TABLE lineainv
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 ROWS
(@col1, @col2, idlinea, @col4, @col5, @col6, @col7)
SET nombreproy = @col2;

LOAD DATA LOCAL INFILE 'C:/Base de Datos/cargar.csv'
INTO TABLE tipoproyecto
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 ROWS
(@col1, @col2, @col3, tipo, @col5, @col6, @col7);

LOAD DATA LOCAL INFILE 'C:/Base de Datos/cargar.csv'
INTO TABLE profesor
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 ROWS
(@col1, @col2, @col3, @col4, @col5, @col6, nombreProf);

LOAD DATA LOCAL INFILE 'C:/Base de Datos/cargar.csv'
INTO TABLE proyecto
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 ROWS
(clave, nombreproy, idlinea, tipo, @col5, @col6, @col7);

LOAD DATA LOCAL INFILE 'C:/Base de Datos/cargar.csv'
INTO TABLE alumno
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 ROWS
(@col1, @col2, @col3, @col4, nocontrol, nombre, @col7)
SET clave = @col1;

LOAD DATA LOCAL INFILE 'C:/Base de Datos/cargar.csv'
INTO TABLE profesorproy
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(@col1, @col2, @col3, @col4, @col5, @col6, @col7, @col8, @col9)
SET idprofesor = (SELECT idprofesor FROM profesor WHERE nombreProf = @col7), clave = LEFT(@col1, 10), calificacion = NULL, rol = 'Asesor';

CREATE TABLE area ( idarea INT AUTO_INCREMENT PRIMARY KEY,nombre VARCHAR(150));

CREATE TABLE indicador (idindicador INT AUTO_INCREMENT PRIMARY KEY, nombre VARCHAR(150) NULL,descripcion MEDIUMTEXT NULL);

CREATE TABLE rubrica (idindicador INT NOT NULL,idarea INT NOT NULL, ponderacion FLOAT NULL, PRIMARY KEY (idindicador, idarea),  
    CONSTRAINT fk_indicador FOREIGN KEY (idindicador) REFERENCES indicador(idindicador),
    CONSTRAINT fk_area FOREIGN KEY (idarea) REFERENCES area(idarea));


INSERT INTO area(nombre) values
("Base de datos"),
("Ingenieria de software"),
("Redes de computadoras"),
("Tesis"),
("Arquitectura de computadoras");

INSERT INTO indicador(nombre, descripcion) VALUES 
("Descripción de Procesos", "Explicación del proceso general actual. Se refiere a la descripción detallada del proceso 
general actual, estableciendo entre otros, las actividades que se realizan, las entidades que participan en ese proceso 
general, indicando el rol que juegan, las relaciones y formas de comunicación que existen entre esas entidades, los insumos, 
así como la información resultante."),
("Especificación de Requisitos del Software", "Requisitos funcionales: a. Requisitos Funcionales: de información, de comportamiento, 
reglas del negocio. Cada requisito funcional contiene un código identificador y descripción clara, completa y sin ambigüedades."),
("Diseño preliminar del sistema"," Diseño Detallado
 Sepresentaladescripcióndecadacomponentedelsoftware,sucomportamiento
 específico y la documentación que se requiere para su construcción. Se consideran 
comoposiblesherramientas: Diagramasde secuencia,Diagrama deeventos,
 Tarjetas CRC, Diagrama de Despliegue, Diagrama de Componentes"),
("Modelo de Proceso de Software","Nombre y justificación del modelo
 Se especifica el nombre del modelo de proceso a utilizar  y se explican las razones 
por las cuales ha sido elegido. Toda la teoría acerca del modelo seleccionado va 
en la sección de marco teórico.");

INSERT INTO rubrica (idindicador, idarea, ponderacion) VALUES
(1, 2, 9),
(2, 2, 28),
(3, 3, 10),
(4, 3, 10);


