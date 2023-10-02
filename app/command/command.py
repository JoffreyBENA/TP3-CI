from app.machine.machine import Machine

machine = Machine()

var = ''

while var != 'quitter':
    var = input(str("'Machine' ou 'Application' ou 'Quitter' : "))
    if var == 'machine':
        action = input(str("'Liste', 'Afficher', 'Ajouter', Modifier ou 'Supprimer': "))
        if action == 'liste':
            print(machine.liste())
        else :
            name = input(str('Nom de la machine: '))
            if action =='afficher':
                print(machine.get(name))
            elif action == 'supprimer':
                machine.delete(name)
            elif action == 'ajouter':
                print ('on demande les données')
            elif action == 'modifier':
                print('on récupère les données avec le nom et on propose de les modifier')
            else:
                print('Merci de saisir un choix valide')
    elif var == 'application':
        print("L'entrée n'est pas un palindrome")
    else:
        print('Merci de saisir un choix valide')