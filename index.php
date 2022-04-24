<html>
 <head>
  <title>Wyszukaj Na Allegro</title>
 </head>
 <body>

<form action='wyszukaj.php' method='post' accept-charset='UTF-8'>
<fieldset >
<legend>Wyszukaj</legend>
<input type='hidden' name='submitted' id='submitted' value='1'/>

Czego szukasz: 
<label for='klucz' >Czego szukasz*:</label>
<input type='text' name='klucz' id='klucz'  maxlength="50" /></br>
Cena Od:
<label for='cenaOd' >Od*:</label>
<input type='value' name='cenaOd' id='cenaOd' maxlength="50" /></br>
Cena Do:
<label for='cenaDo' >Do*:</label>
<input type='value' name='cenaDo' id='cenaDo' maxlength="50" /></br>
Ile Stron:
<label for='ilestron' >Ile Stron*:</label>
<input type='value' name='ilestron' id='ilestron' maxlength="50" /></br>
Segregacja:
<label for='segregacja'>Segregacja*:</label>
<select name='segregacja' id='segregacja'>
<option value='p'>Cena</option>
<option value='n'>Najnowsze</option>
</select>

<input type='submit' name='Submit' value='Submit' />

</fieldset>
</form>


 </body>
</html>
