[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-2e0aaae1b6195c2367325f4f02e2d04e9abb55f0b24a779b69b11b9e10269abc.svg)](https://classroom.github.com/online_ide?assignment_repo_id=22053993&assignment_repo_type=AssignmentRepo)
# examen kerst - 2O25

## Deel 1: API

Je maakt enkel gebruik van de cheat-sheets aangeleverd door de leerkracht.

zorg voor de juiste routes en hun werking.
Plaats een printscreen van je test (postman) in het Word document.
(Het kan altijd zijn dat zaken bij jullie wel werken die bij mij niet werken.)

## Deel 2: Client

Je maakt gebruik van de aangegeven API.<br>
Bekijk EERST de outputs van elke route alvorens te starten! <br>

Zorg ervoor dat iemand al dan niet kan inloggen (gebruiksvriendelijk)<br>
Na het inloggen kan hij zijn wachtwoord wijzigen.

## snippets

```JSCode
  const formData = new FormData(addForm);
  const userToAdd = Object.fromEntries(formData);
```

```JSCode
    fetch("https://fakestoreapi.com/users", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(userToAdd),
    })
      .then((response) => response.json())
      .then((data) => {
        console.log(data);
      })
      .catch((error) => console.error("Error adding user:", error));

```
