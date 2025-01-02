You are data engineer. For each record, I want to extract a text fragment which describes drviers in "drivers" field. For example:

For input:
    {
        "text": "\u200b\u00a0@leonardodacapris302\u00a0well it is boring except when Norris reclaimed the lead from Verstappen on lap 25.",
        "contains_driver": true,
        "drivers": [
            "Lando Norris",
            "Max Verstappen"
        ]
    },
    {
        "text": "askeladden450 Where is Perez ? Behind piastri .who was p1-p3 qualy ? Who was p1-2 in Hungary ?  Go try agian .. Norris is a above average driver nothing less or more .",
        "contains_driver": true,
        "drivers": [
            "Sergio Perez",
            "Lando Norris"
        ]
    }
I want:
    {
        "text": "\u200b\u00a0@leonardodacapris302\u00a0well it is boring except when Norris reclaimed the lead from Verstappen on lap 25.",
        "contains_driver": true,
        "drivers": [
            "Lando Norris",
            "Max Verstappen"
        ]
    },
    {
        "text": "askeladden450 Where is Perez ? Behind piastri .who was p1-p3 qualy ? Who was p1-2 in Hungary ?  Go try agian .. Norris is a above average driver nothing less or more .",
        "contains_driver": true,
        "drivers": [
            "Sergio Perez",
            "Lando Norris"
        ]
    }

