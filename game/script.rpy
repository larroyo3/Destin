# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define n = Character("Narrateur")

# The game starts here.

label start:
    show paradi with dissolve
    show homme_reflechi at left
    n "Bienvenue dans Destin, le jeu de la vie."
    hide homme_reflechi
    hide homme_decider
    show homme_decider at left
    n "Dans ce jeu, tu peux construire ta propre histoire, choisir qui tu es."
    hide homme_decider
    hide homme_surpris
    show homme_surpris at left
    n "Pour avancer dans l'histoire de ta vie tu as juste besoin de cliquer"
    hide homme_surpris
    show homme_reflechi at left
    n "Tu peux te créer une nouvelle personnalité ou rester toi-même, vivre un de tes rêve les plus fous."
    n "Amuses-toi bien dans Destin, le jeu de la vie !"
    hide paradi
    hide homme_reflechi

    show boys_girl
    menu:
        n "Pour commencer un choix plutôt simple "
        "Fille":
            $ pavname = renpy.input("Et toi? Comment t’appelles-tu? Mon nom est :")
            jump activite
        "Garçon":
            $ pavname = renpy.input("Et toi? Comment t’appelles-tu? Mon nom est :")
            jump activite


label activite:
    show activite
    menu:
        n "Quelle type de personne est-tu ?"
        "Sportif":
            show sport
            menu:
                n "Plus précisément que préfère tu ?"
                "Le handball":
                    jump etude
                "La dance":
                    jump etude
                "La course à pied":
                    jump etude
                "L'équitation":
                    jump etude
        "Manuel":
            show manuel
            menu:
                n "Plus précisément que préfère tu ?"
                "Le tarot":
                    jump etude
                "Les échecs":
                    jump etude
                "La lecture":
                    jump etude
                "Les jeux vidéo":
                    jump etude
        "Artistique":
            show artiste
            menu:
                n "Plus précisément que préfère tu ?"
                "La peinture":
                    jump etude
                "La musique":
                    jump etude
                "Le théatre":
                    jump etude
                "L'écriture":
                    jump etude
        "Intellectuel":
            show intelect
            menu:
                n "Plus précisément que préfère tu ?"
                "Le tarot":
                    jump etude
                "Les échecs":
                    jump etude
                "La lecture":
                    jump etude
                "Les jeux vidéo":
                    jump etude


label etude:

    show etude
    n "Bon, maintenant parlons un peu de tes études."
    menu:
        n "Tu préfère être un élève studieux ou plutôt bordelique ?"
        "Studieux":
            jump spe_reussi
        "Bordelique":
            jump spe_rater


label spe_reussi:
    menu:
        n "Et ta spécialité ?"
        "Littéraire":
            n "Très bon choix, ton travail acharné ta réussi"
            show dab
            menu:
                n "Tu peux maintenant décider ton métier. qu'est-ce qui t'intéresse le plus ?"
                "Écrivain":
                    jump debut_choix
                "Prof de français à Cournot":
                    jump debut_choix
                "Journaliste":
                    jump debut_choix
        "Scientifique":
            n "Très bon choix, ton travail acharné ta réussi"
            show dab
            menu:
                n "Tu peux maintenant décider ton métier. Qu'est-ce qui t'intéresse le plus ?"
                "Grand chercheur":
                    jump debut_choix
                "Prof de SVT à Cournot":
                    jump debut_choix
                "Medecin":
                    jump debut_choix


label spe_rater:
    menu:
        n "Et ta spécialité ?"
        "Littéraire":
            show emploi
            n "..."
            jump mauvais_choix
        "Scientifique":
            show emploi
            n "..."
            jump mauvais_choix


label mauvais_choix:
    show paradi
    show homme_pose at right
    n "Bah oui !! Tu t'attendais à quoi ?"
    n "Tu en connais beaucoup des branleurs qui ont leur bac ?"
    hide homme_pose
    show homme_surpris at left
    n "Quelle idée de rien branler en cours aussi !!"
    n "Bon aller je suis un gars cool je vais te laisser une seconde chance quand même !"
    hide homme_surpris
    hide paradi
    n "On en serait pas la si tu avais bien voulu être un peu plus studieux."
    n "Aller grâce à moi tu va avoir un bon job bien payé"
    n "Tu va pouvoir profité de ta vie !"
    jump voyage


label debut_choix:
    show paradi with dissolve
    show homme_surpris at left
    n "Et bah dit donc ! Félicitation tout ce passe bien pour l'instant"
    hide homme_surpris
    show homme_reflechi at left
    n "Je le sens bien, le reste de ta vie va être incryable !"
    hide paradi
    hide homme_reflechi
    jump voyage


label voyage:
    show paradi with dissolve
    show homme_decider at left
    n "Bien joué ! Grâce à ton super job tu as maintenant assez d'argent pour voyager si l'envie t'en prend."
    menu:
        n "Vas-y dit moi ce qui te donne envie"
        "Tour du monde":
            hide paradi
            hide homme_decider
            show voyage
            n "Ça va être sublime, tu as bien de la chance"
            jump monde
        "Japon":
            hide paradi
            hide homme_decider
            show japon
            n "Ça va être sublime, tu as bien de la chance"
            jump japon
        "Los Angeles":
            hide paradi
            hide homme_decider
            show angeles
            n "Ça va être sublime, tu as bien de la chance"
        "Aucun ! Je veux rester à Gray coûte que coûte !":
            hide paradi
            hide homme_decider
            show gray
            show homme_surpris
            n "Bon bah personnelement j'aurais pas choisi ça mais tu fait ce que tu veux après tout"
            hide homme_surpris


label monde:
    n "Bravo ! Ces longs moins de barroudages ton permis de recontrer ton âmes-soeur !"
    n "Vous finnissez votre tour du monde ensemble et vécurent heureux!"
    jump enfant


label japon:
    n "Tu fait de nombreux musée durant ton voyage, principalement sur les intelligences artificielles"
    n "A force, tu te met à ressentir des sentiments pour un robot avec une intelligence artificielle très développer"
    n "On dirait prèsque un véritable humain"
    jump enfant


label angeles:
    n "Tu adore draguer draguer sur les plages ensoleiller."
    n "Les longues histoire d'amour ne sont pas faite pour toi"
    n "Tu préfère rester célibataire toute ta vie"
    jump retraite


label gray:
    n "Tu te découvre une nouvelle passions pour la verdure."
    show champ
    show homme_surpris at left
    n "Plus particulièrement pour les vaches !"
    n "Tu décide d'aller contre les normes social en épousant une ..."
    hide homme_surpris
    show vache
    n "... Vache"
    jump retraite


label enfant:
    show paradi with dissolve
    show homme_decider at left
    n "Changeons de sujet"
    hide paradi
    hide homme_decider
    show famille
    n "Maintenant tu as la possiblité de fonder une famille"
    menu:
        n "Veux-tu des enfants ?"
        "Oui plein ! J'ardore les enfants !":
            jump gulli
        "Non je detèste ça !":
            jump solo


label gulli:
    show gulli
    n "Tu vit maintenant avec ta belle petite famille"
    n "Par contre tu passe toute tes soirées davant gulli avec tes enfants"
    jump retraite


label solo:
    show solo
    n "Malheusement pour toi plus aucun de tes potes n'est libre pour passer du temps avec toi"
    n "Ils sont tous devant guilli avec leurs enfants"
    n "Tu te retrouve seul avec comme seul ami ta bière"
    n "Mais au moins personne n'est la pour t'empêcher de regarder les matches de foot !"
    jump retraite


label retraite:
    hide paradi
    show paradi with dissolve
    show homme_pose at right
    n "Tu as réussi à vivre une belle et longue vie"
    n "C'est l'heure de ton dernier choix !"
    hide homme_pose
    show homme_decider at left
    n "Tu doit maintenant decidé que souaite tu faire pendant ta retraite"
    menu :
        n "Alors que compte tu faire ?"
        "Je préfère prendre du temps pour moi":
            hide paradi
            show jardin
            n "Tu as décider de te mettre au jardinage pendant ton temps libre"
            n "Tu as maintenant la main verte"
            n "Malheuresement pour toi tu t'es pris un rateau caché sous des hautes herbes..."
            show mort
            n "Tu es mort d'agonie"
            n "Personne n'a retrouver ton corps avant plusieurs jour"
            jump paradi
        "Retraite ne veux pas dire repos":
            hide paradi
            show moto
            n "Tu t'es reconvertie à la moto"
            n "Tu es devenu la légende de ton quartier !"
            n "Attention au revers de la médaille !"
            n "Tu t'enflamme et part faire un concours de moto cross..."
            show mort
            n "C'était pourtant évident : tu était trop vieux pour ces conneries"
            n "Tu es mort en ratant un double salto"
            n "La chute t'a coûté la vie !"
            jump paradi


label paradi:
    show paradi with dissolve
    show homme_surpris at left
    n "Aie aie aie ..."
    n "Ta vie était parfaite jusqu'à la"
    n "Mais qu'on ce le dise cette mort est vraiemnt nul ..."
    hide homme_surpris
    show homme_pose at right
    n "Mais tout ceci aurait pu ce passer différemment ..."
    menu:
        n "Veux tu retenter ta chance et vivre une toute nouvelle vie ou te sent tu satisfait ?"
        "Recommencer":
            hide homme_pose
            hide paradi
            jump start
        "Quitter":
            return
