/* Vamos a dividir el trabajo en 3 tablas:
 * 1 - Obtenemos la información de los datos relacionesdos con las canciones
 */

WITH "Cancion" AS 
	(select "Track"."AlbumId", "Track"."MediaTypeId", "Track"."GenreId", "Track"."TrackId", "Track"."Name", "Track"."Composer", 
	"Track"."Milliseconds", "Track"."Bytes", "Track"."UnitPrice", "Playlist"."Name" AS "Estilo"
	FROM "Track"
	LEFT JOIN "PlaylistTrack"
	ON "Track"."TrackId" = "PlaylistTrack"."TrackId"
	LEFT JOIN "Playlist"
	ON "PlaylistTrack"."PlaylistId" = "Playlist"."PlaylistId")
SELECT c."TrackId", c."Name" AS "t_cancion", c."composer", c."Milliseconds", c."Bytes", c."UnitPrice", c."Estilo",
		a."Title", "Artist"."Name" AS "Grupo", g."Name" AS "Género", mt."Name" AS "Formato_Rep"
FROM "Cancion" AS c
RIGHT JOIN "Album" AS a
ON c."AlbumId" = a."AlbumId"
RIGHT JOIN "Artist"
ON a."ArtistId" = "Artist"."ArtistId"
RIGHT JOIN "genre" AS g
ON c."GenreId" = g."GenreId"
RIGHT JOIN MEDIATYPE AS mt
ON c."MediaTypeId" = mt."MediaTypeId";

/* 2- Obtenemos los datos de los empleados y de los clientes */

SELECT CONCAT(e."FirstName", " " , e."LastName") AS "Nombre_Empleado", e."title", e."ReportsTo", e."City" AS "Ciudad_Empleado",
	   e."Country", CONCAT(cu."FirstName", " ", cu."LastName") AS "Nombre_Cliente", cu."Company", cu."City" AS "Ciudad_Cliente",
	   cu."Country", cu."CustomerId"
FROM "Customer" AS cu
RIGHT JOIN "Employee" AS e
ON cu."SupportRepId" = e."EmployeeId";

/* 3- Obtenemos los datos de las facturas realizadas */

SELECT il."TrackId", i."CustomerId", i."InvoiceDate", i."BillingCity", i."BillingCountry", i."Total" AS "Total_Fra",
	   il. "Quantity", il."UnitPrice"
FROM "Invoice" AS i
LEFT JOIN "InvoiceLine" AS il
ON i."InvoiceId" = il."InvoiceId";











