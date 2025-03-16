# Tahák v Markdownu: Základy Programování
## Autoři: Rudolf Borovka, Tomáš Korolus, Jiří Fejtek
### Proměnné

* **Proměnné** slouží k ukládání dat.
* Deklarace: `jméno_proměnné = hodnota`
* **Typy dat:**
    * **Čísla:** Celá čísla (`int`), desetinná čísla (`float`)
    * **Text:** Řetězce (`str`)
    * **Logické hodnoty:** Pravda (`True`) nebo Nepravda (`False`)
* **Příklad:**
    ```python
    age = 25  # Celé číslo
    name = "Jan"  # Text
    is_student = True  # Logická hodnota
    ```

### Aritmetické Operace

* **Sčítání:** `+`
* **Odečítání:** `-`
* **Násobení:** `*`
* **Dělení:** `/`
* **Modulo (zbytek po dělení):** `%`
* **Umocňování:** `**`
* **Příklad:**
    ```python
    result = 10 + 5  # 15
    remainder = 10 % 3  # 1
    ```

### Podmínky a Logické Operace

* **Podmínky:** Používají se k provádění různých akcí na základě splnění podmínky.
* **Operátory srovnání:**
    * `==` Rovná se
    * `!=` Nerovná se
    * `>` Víc než
    * `<` Méně než
    * `>=` Víc než nebo rovno
    * `<=` Méně než nebo rovno
* **Logické operátory:**
    * `and` A
    * `or` Nebo
    * `not` Ne
* **Příklad:**
    ```python
    age = 20
    if age >= 18:
        print("Jsi plnoletý")
    else:
        print("Nejsi plnoletý")
    ```

### Cykly

* **Cykly:** Opakují kód, dokud není splněna podmínka.
* **Typy cyklů:**
    * **`for` cyklus:** Prochází sekvenci hodnot.
    * **`while` cyklus:** Opakuje kód, dokud je splněna podmínka.
* **Příklad:**
    ```python
    for i in range(5):
        print(i)

    i = 0
    while i < 5:
        print(i)
        i += 1
    ```

### Funkce

* **Funkce:** Bloky kódu, které provádějí specifické úkoly.
* **Definice:** `def jméno_funkce(parametry):`
* **Volání:** `jméno_funkce(argumenty)`
* **Příklad:**
    ```python
    def pozdrav(jméno):
        print("Ahoj", jméno)

    pozdrav("Jan")
    ```

### Texty

* **Řetězce:** Posloupnost znaků.
* **Operace s texty:**
    * **Sloučení:** `+`
    * **Délka:** `len()`
    * **Indexování:** `text[index]`
    * **Řezání:** `text[start:end]`
* **Příklad:**
    ```python
    jméno = "Jan"
    příjmení = "Novák"
    celé_jméno = jméno + " " + příjmení  # "Jan Novák"
    ```

### Výstupy

* **Tisk:** `print()`
* **Příklad:**
    ```python
    print("Ahoj světe!")
    ```

### Vstupy

* **Získání vstupu od uživatele:** `input()`
* **Příklad:**
    ```python
    jméno = input("Zadej své jméno: ")
    print("Ahoj", jméno)
    ```
    