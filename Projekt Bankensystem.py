##############################################
# imports
##############################################

import random
import getpass

##############################################
# Klassen
##############################################

class Konto():
    def __init__(self, kontonummer:int, PIN:int, kontostand:float, kontoinhaber:'Kunde'):
        self.kontonummer = kontonummer
        self.PIN = PIN
        self.kontostand = kontostand
        self.kontoinhaber = kontoinhaber

    def einzahlung(self, betrag:float):
        self.kontostand += betrag
        round(self.kontostand, 2)
        print("Ihr neuer Kontostand beträgt: " + str(self.kontostand) + "€")

    def abheben(self, betrag:float): 
        if betrag <= self.kontostand:
            self.kontostand -= betrag
            round(self.kontostand, 2)
            print("Ihr neuer Kontostand beträgt: " + str(self.kontostand) + "€")
        else:
            print("Kontostand zu niedrig. Abheben nicht möglich.")


class Kunde():
    def __init__(self, kundenID:int, name:str, adresse:str, gebdatum:str, passwort:str, login_name:str):
        self.kundenID = kundenID
        self.name = name
        self.adresse = adresse
        self.gebdatum = gebdatum
        self.passwort = passwort
        self.login_name = login_name
        self.konten = []

class Bank():
    def __init__(self, bank_name:str):
        self.bank_name = bank_name
        self.standorte = []
        self.konten = []
        self.kunden = []

    def kunde_neu(self, kunde:Kunde):
        self.kunden.append(kunde)

    def kunde_entf(self, kunde:Kunde):
        self.kunden.remove(kunde)

    def konto_neu(self, konto:Konto):
        self.konten.append(konto)

    def konto_entf(self, konto:Konto):
        self.konten.remove(konto)


class Userinterface():
    def __init__(self, bank:Bank, passwort:str):
        self.bank = bank
        self.passwort = passwort
        
    def hauptmenü(self):
        while True:
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n") # Erzeuge viele Leerzeilen, damit das hauptmenü "sauberer" aussieht
            print("###############################################################################################")
            print("###############################                               #################################")
            print("############################### Willkomen bei " + self.bank.bank_name + " #################################")
            print("###############################                               #################################")
            print("###############################################################################################\n")
            print("Welche der folgenden Aktionen wollen sie ausführen?")
            print("(1) Kundenkonto verwalten")
            print("(2) Bankkonten verwalten")
            print("(3) Admin")
            select_main = input("Geben sie die entsprechende Nummer ein um fortzufahren: ")
            print("")
            if select_main == "1":
                self.kundenkonto()
            if select_main == "2":
                self.bankkonto()
            if select_main == "3":
                self.admin()
            else:
                print("Eingabe unzulässig. Probieren sie es erneut.")
                self.hauptmenü()

    def kundenkonto(self):
        print("Welche der folgenden Aktionen wollen sie ausführen?")
        print("(1) Kundenkonto erstellen")
        print("(2) Kundeninformationen verwalten/ändern")
        print("(3) Kundenkonto löschen")
        print("(4) abbrechen")
        select_kunde = input("Geben sie die entsprechende Nummer ein um fortzufahren: ")
        print("")
        if select_kunde == "1":
            self.create_kundenkonto()
        if select_kunde == "2":
            self.manage_kundenkonto()
        if select_kunde == "3":
            self.del_kundenkonto()
        if select_kunde == "4":
            self.hauptmenü()
        else:
            print("Eingabe unzulässig. Probieren sie es erneut.\n")
            self.kundenkonto()

    def create_kundenkonto(self):
        print("Geben sie folgende Informationen ein:")
        name = input("Nachnamen: ")
        vorname = input("Vornamen: ")
        PLZ = input("Postleitzahl: ")
        wohnort = input("aktueller Wohnort: ")
        straße = input("Straße: ")
        hausnummer = input("Hausnummer: ")
        gebdatum = input("Geburtsdatum: ")
        login_name = input("Loginname: ")
        passwort = input("Passwort: ")
        print(passwort)
        print("")
        kundenID = len(self.bank.kunden) + 1
        fullname = name + ", " + vorname
        while len(fullname) < 16:
            fullname += " " # zur besseren Formatierung wird der Name auf 16 Zeichen aufgefüllt
        self.bank.kunde_neu(Kunde(kundenID, fullname, PLZ + " " + wohnort + ", " + straße + " " + hausnummer, gebdatum, passwort, login_name))
        input("Ihr Kundenkonto wurde erfolgreich erstellt. (Drücken sie Enter um fortzufahren)")
        self.hauptmenü()

    def manage_kundenkonto(self):
        print("Geben sie ihren Loginnamen ein.")
        name = input("(Zum Abbrechen drücken sie die (1)): ")
        if name == "1":
            self.hauptmenü()
        else:
            for i in self.bank.kunden:
                if i.login_name == name:
                    passwort = input("Geben sie ihr Passwort ein: ")
                    print("")
                    if i.passwort == passwort:
                        print("Ihre gespeicherten Informationen sind:")
                        print("1 - Name: " + i.name)
                        print("2 - Adresse: " + i.adresse)
                        print("3 - Geburtsdatum: " + i.gebdatum)
                        print("4 - Loginname: " + i.login_name)
                        print("5 - Passwort: " + i.passwort)
                        print("6 - abbrechen\n")
                        select_inform = input("Geben sie die Nummer der zu ändernden Information ein: ")
                        if select_inform == "1":
                            print("Geben sie ihre neuen Daten ein:")
                            name = input("Nachnamen: ")
                            vorname = input("Vornamen: ")
                            i.name = name + ", " + vorname
                            input("Ihr Name wurde erfolgreich geändert! (Drücken sie Enter um fortzufahren)")
                            self.hauptmenü()
                        elif select_inform == "2":
                            print("Geben sie ihre neuen Daten ein:")
                            PLZ = input("Postleitzahl: ")
                            wohnort = input("aktueller Wohnort: ")
                            straße = input("Straße: ")
                            hausnummer = input("Hausnummer: ")
                            i.adresse = PLZ + "" + wohnort + "" + straße + "" + hausnummer
                            input("Ihre Adresse wurde erfolgreich geändert! (Drücken sie Enter um fortzufahren)")
                            self.hauptmenü()
                        elif select_inform == "3":
                            gebdatum = input("Geben sie ihr neues Geburtsdatum ein: ")
                            i.gebdatum = gebdatum
                            input("Ihr Geburtsdatum wurde erfolgreich geändert! (Drücken sie Enter um fortzufahren)")
                            self.hauptmenü()
                        elif select_inform == "4":
                            login_name = input("Geben sie ihren neuen Loginnamen ein: ")
                            i.login_name = login_name
                            input("Ihr Loginname wurde erfolgreich geändert! (Drücken sie Enter um fortzufahren)")
                            self.hauptmenü()
                        elif select_inform == "5":
                            passwort = input("Geben sie ihr neues Passwort ein: ")
                            i.passwort = passwort
                            input("Ihr Passwort wurde erfolgreich geändert! (Drücken sie Enter um fortzufahren)")
                            self.hauptmenü()
                        elif select_inform == "6":
                            self.hauptmenü()
                        else:
                            print("Eingabe unzulässig. Probieren sie es erneut.\n")
                            self.manage_kundenkonto()
                    else:
                        print("Das Passwort ist inkorrekt!\n")
                        self.manage_kundenkonto()
            else:
                print("Es existiert kein Konto mit diesem Namen. Versuchen sie es erneut!\n")
                self.manage_kundenkonto()


    def del_kundenkonto(self):
        print("Geben sie ihren Loginnamen ein.")
        name = input("(Zum Abbrechen drücken sie die (1)): ")
        if name == "1":
            self.hauptmenü()
        else:
            for i in self.bank.kunden:
                if i.login_name == name:
                    passwort = input("Geben sie ihr Passwort ein: ")
                    print("")
                    if i.passwort == passwort:
                        print("Wollen sie dieses Konto löschen? Dieser Vorgang ist unwiderruflich und endgültig!")
                        passwort2 = input("Zur Bestätigung geben sie ihr Passwort erneut ein: ")
                        if i.passwort == passwort2:
                            input("\nIhr Konto wurde erfolgreich gelöscht! (Drücken sie Enter um fortzufahren)")
                            self.hauptmenü()
                        else:
                            print("Passwort inkorrekt! Versuchen sie es erneut.\n")
                            self.del_kundenkonto()
                    else:
                        print("Passwort inkorrekt! Versuchen sie es erneut.\n")
                        self.del_kundenkonto()
            else:
                print("Dieses Konto existiert nicht! Vergewissern sie sich, dass sie den Namen richtig geschrieben haben und probieren sie es erneut.\n")
                self.del_kundenkonto() 

    def bankkonto(self):
        print("Welche der folgenden Aktionen wollen sie ausführen?")
        print("(1) Bankkonto erstellen")
        print("(2) Konten anzeigen")
        print("(3) Geld einzahlen")
        print("(4) Geld abheben")
        print("(5) Bankkonto löschen")
        print("(6) abbrechen")
        select_konto = input("Geben sie die entsprechende Nummer ein um fortzufahren: ")
        print("")
        if select_konto == "1":
            self.create_bankkonto()
        if select_konto == "2":
            self.show_konto()
        if select_konto == "3":
            self.einzahlung()
        if select_konto == "4":
            self.abheben()
        if select_konto == "5":
            self.del_konto()
        if select_konto == "6":
            self.hauptmenü()
        else:
            print("Eingabe unzulässig. Probieren sie es erneut.\n")
            self.bankkonto()

    def create_bankkonto(self):
        print("Geben sie ihren Loginnamen ein.")
        name = input("(Zum Abbrechen drücken sie die (1)): ")
        if name == "1":
            self.hauptmenü()
        else:
            for i in self.bank.kunden:
                if i.login_name == name:
                    passwort = input("Geben sie ihr Passwort ein: ")
                    if i.passwort == passwort:
                        kontonummer = random.randint(1000000000, 9999999999) # generiere Kontonummer
                        PIN = random.randint(1000, 9999) # generiere PIN
                        if len(i.konten) >= 1:
                            for j in self.bank.konten:
                                if j.kontonummer == kontonummer:
                                    kontonummer = random.randint(1000000000, 9999999999) # generiere Kontonummer neu, wenn es bereits ein Konto mit dieser PIN gibt
                        print("\nDie Daten ihres erstellten Kontos: ")
                        print("1 - Kontonummer: " + str(kontonummer))
                        print("2 - PIN: " + str(PIN))
                        konto = Konto(kontonummer, PIN, 0.00, i)
                        i.konten.append(konto)
                        self.bank.konten.append(konto)
                        input("(Drücken sie Enter um fortzufahren)")
                        self.hauptmenü()
                    else:
                        print("\nDas Passwort ist inkorrekt!\n")
                        self.create_bankkonto()
            else:
                print("Es existiert kein Konto mit diesem Namen. Versuchen sie es erneut!\n")
                self.create_bankkonto()

    def show_konto(self):
        print("Geben sie ihren Loginnamen ein.")
        name = input("(Zum Abbrechen drücken sie die (1)): ")
        if name == "1":
            self.hauptmenü()
        else:
            for i in self.bank.kunden:
                if i.login_name == name:
                    passwort = input("Geben sie ihr Passwort ein: ")
                    if i.passwort == passwort:
                        if len(i.konten) == 0:
                            print("\nEs existieren keine Konten!")
                        else:
                            print("\n############################################################################################################################################")
                            print("########################################################## Ihre Konten #####################################################################")
                            print("############################################################################################################################################")
                            print("####################### Kontonummer ########################### PIN ################################# Kontostand ###########################")
                            for j in i.konten:
                                print("\t\t\t" + str(j.kontonummer) + "\t\t\t\t" + str(j.PIN) + "\t\t\t\t\t" + str(j.kontostand) + "\t€")
                        input("(Drücken sie Enter um fortzufahren)")
                        self.hauptmenü()
                    else:
                        print("\nDas Passwort ist inkorrekt!\n")
                        self.show_konto()
            else:
                print("Es existiert kein Konto mit diesem Namen. Versuchen sie es erneut!\n")
                self.show_konto()

    def einzahlung(self):
        print("Geben sie ihre Kontonummer ein.")
        kontonummer = input("(Zum Abbrechen drücken sie die (1)): ")
        if kontonummer == "1":
            self.hauptmenü()
        else:
            for i in self.bank.konten:
                if str(i.kontonummer) == kontonummer:
                    PIN = input("Geben sie ihre PIN ein: ")
                    if str(i.PIN) == PIN:
                        betrag = input("\nGeben sie den Betrag ein, den sie einzahlen wollen: ")
                        i.einzahlung(float(betrag))
                        input("(Drücken sie Enter um fortzufahren)")
                        self.hauptmenü()
                    else:
                        print("Die PIN ist inkorrekt!\n")
                        self.einzahlung()
            else:
                print("Es existiert kein Konto mit dieser Kontonummer. Versuchen sie es erneut!\n")
                self.einzahlung()

    def abheben(self):
        print("Geben sie ihre Kontonummer ein.")
        kontonummer = input("(Zum Abbrechen drücken sie die (1)): ")
        if kontonummer == "1":
            self.hauptmenü()
        else:
            for i in self.bank.konten:
                if str(i.kontonummer) == kontonummer:
                    PIN = input("Geben sie ihre PIN ein: ")
                    if str(i.PIN) == PIN:
                        betrag = input("\nGeben sie den Betrag ein, den sie abheben wollen: ")
                        i.abheben(float(betrag))
                        input("(Drücken sie Enter um fortzufahren)")
                        self.hauptmenü()
                    else:
                        print("Die PIN ist inkorrekt!\n")
                        self.abheben()
            else:
                print("Es existiert kein Konto mit dieser Kontonummer. Versuchen sie es erneut!\n")
                self.abheben()

    def del_konto(self):
        print("Geben sie ihre Kontonummer ein.")
        kontonummer = input("(Zum Abbrechen drücken sie die (1)): ")
        if kontonummer == "1":
            self.hauptmenü()
        else:
            for i in self.bank.konten:
                if str(i.kontonummer) == kontonummer:
                    PIN = input("Geben sie ihre PIN ein: ")
                    if str(i.PIN) == PIN:
                        i.kontoinhaber.konten.remove(i)
                        self.bank.konten.remove(i)
                        print("Das Konto wurde erfolgreich gelöscht!")
                        input("(Drücken sie Enter um fortzufahren)")
                        self.hauptmenü()
                    else:
                        print("Die PIN ist inkorrekt!\n")
                        self.del_konto()
            else:
                print("Es existiert kein Konto mit dieser Kontonummer. Versuchen sie es erneut!\n")
                self.del_konto()

    def admin(self):
        print("Geben sie das Adminpasswort ein.")
        passwort = input("(Zum Abbrechen drücken sie die (1)): ")
        if passwort == "1":
            self.hauptmenü()
        elif passwort == self.passwort:
            print("\nWelche der folgenden Aktionen wollen sie ausführen?")
            print("(1) Kundenkonten anzeigen")
            print("(2) Kundenkonten erstellen / bearbeiten")
            print("(3) Bankkonten anzeigen")
            print("(4) Bankkonten erstellen / bearbeiten")
            print("(5) Standorte verwalten")
            print("(6) abbrechen")
            select_konto = input("Geben sie die entsprechende Nummer ein um fortzufahren: ")
            print("")
            if select_konto == "1":
                self.show_kundenkonten()
            if select_konto == "2":
                self.manage_kundenkonten()
            if select_konto == "3":
                self.show_bankkonten()
            if select_konto == "4":
                self.manage_bankkonten()
            if select_konto == "5":
                self.manage_locations()
            if select_konto == "6":
                self.hauptmenü()
            else:
                print("Eingabe unzulässig. Probieren sie es erneut.\n")
                self.admin()
        else:
            print("\nPasswort inkorrekt! Versuchen sie es erneut!\n")
            self.admin()

    def show_kundenkonten(self):
        if len(self.bank.kunden) == 0:
            print("\nEs existieren keine Kundenkonten!")
            input("(Drücken sie Enter um fortzufahren)")
            self.hauptmenü()
        else:
            print("\n###########################################################################################################################################################")
            print("#################################################################### Kundenkonten #########################################################################")
            print("###########################################################################################################################################################")
            print("####### ID ############ Name, Vorname ################# Adresse ###################### Geburtsdatum ######### Loginname ######## Anz. Bankkonten ##########")
            for i in self.bank.kunden:
                print("\t" + str(i.kundenID) + "\t\t" + i.name + "\t" + i.adresse + "\t\t" + i.gebdatum + "\t\t" + i.login_name + "\t\t\t" + str(len(i.konten)))
            input("(Drücken sie Enter um fortzufahren)")
            self.hauptmenü()

    def manage_kundenkonten(self):
        if len(self.bank.kunden) == 0:
            print("\nEs existieren keine Kundenkonten!")
            input("(Drücken sie Enter um fortzufahren)")
            self.hauptmenü()
        else:
            print("Geben sie die ID des zu ändernden Kontos ein.")
            print("(Zum Abbrechen drücken sie die (1)).")
            ID = input("(Zum erstellen eines neuen Kontos drücken sie die (2)): ")
            if ID == "1":
                self.hauptmenü()
            elif ID == "2":
                self.create_kundenkonto()
            else:
                for i in self.bank.kunden:
                    if ID == i.kundenID:
                        print("\nWelche der folgenden Aktionen wollen sie ausführen?")
                        print("(1) gespeicherte Daten bearbeiten")
                        print("(2) Konto löschen")
                        print("(3) abbrechen")
                        select_konto = input("Geben sie die entsprechende Nummer ein um fortzufahren: ")
                        print("")
                        if select_konto == "1":
                            self.admin_edit_kundenkonto(i)
                        if select_konto == "2":
                            self.admin_del_kundenkonto(i)
                        if select_konto == "3":
                            self.hauptmenü()
                        else:
                            print("Eingabe unzulässig. Probieren sie es erneut.\n")
                            self.manage_kundenkonten()
                else:
                    print("Es existiert kein Konto mit diesem Loginname. Versuchen sie es erneut!\n")
                    self.manage_kundenkonten()

    def admin_edit_kundenkonto(self, kunde:Kunde):
        print("\nWelche der folgenden Daten wollen sie ändern?")
        print("(1) Name")
        print("(2) Adresse")
        print("(3) Geburtsdatum")
        print("(4) Loginname")
        print("(5) abbrechen")
        select_konto = input("Geben sie die entsprechende Nummer ein um fortzufahren: ")
        print("")
        if select_konto == "1":
            print("Geben sie die neuen Daten ein:")
            name = input("Nachnamen: ")
            vorname = input("Vornamen: ")
            kunde.name = name + ", " + vorname
            input("Der Name wurde erfolgreich geändert! (Drücken sie Enter um fortzufahren)")
            self.hauptmenü()
        if select_konto == "2":
            print("Geben die neuen Daten ein:")
            PLZ = input("Postleitzahl: ")
            wohnort = input("aktueller Wohnort: ")
            straße = input("Straße: ")
            hausnummer = input("Hausnummer: ")
            kunde.adresse = PLZ + "" + wohnort + "" + straße + "" + hausnummer
            input("Die Adresse wurde erfolgreich geändert! (Drücken sie Enter um fortzufahren)")
            self.hauptmenü()
        if select_konto == "3":
            kunde.gebdatum = input("Geben sie das neue Geburtsdatum ein: ")
            print("Das Geburtsdatum wurde erfolgreich geändert!")
            input("(Drücken sie Enter um fortzufahren)")
            self.hauptmenü()
        if select_konto == "4":
            kunde.login_name = input("Geben sie den neuen Loginnamen ein: ")
            print("Der Loginname wurde erfolgreich geändert!")
            input("(Drücken sie Enter um fortzufahren)")
            self.hauptmenü()
        if select_konto == "5":
            self.hauptmenü()
        else:
            print("Eingabe unzulässig. Probieren sie es erneut.\n")
            self.admin_edit_kundenkonto(Kunde)

    def admin_del_kundenkonto(self, kunde:Kunde):
        print("Sind sie sicher, dass sie das Konto löschen wollen?")
        print("(1) Ja")
        print("(2) Nein")
        select_konto = input("Geben sie die entsprechende Nummer ein um fortzufahren: ")
        print("")
        if select_konto == "1":
            passwort = input("Geben sie das Adminpasswort ein um fortzufahren: ")
            if passwort == self.passwort:
                self.bank.kunden.remove(kunde)
                print("Das Konto wurde erfolgreich gelöscht!")
                input("(Drücken sie Enter um fortzufahren)")
                self.hauptmenü()
            else:
                print("Das Passwort ist falsch. Versuchen sie es erneut!")
                self.admin_del_kundenkonto(kunde)
        if select_konto == "2":
            self.hauptmenü()
        else:
            print("Eingabe unzulässig. Probieren sie es erneut.\n")
            self.admin_del_kundenkonto(kunde)

    def show_bankkonten(self):
        if len(self.bank.konten) == 0:
            print("\nEs existieren keine Bankkonten!")
            input("(Drücken sie Enter um fortzufahren)")
            self.hauptmenü()
        else:
            print("\n#######################################################################################################")
            print("############################################# Bankkonten ##############################################")
            print("#######################################################################################################")
            print("####### Kontonummer ########## Kontoinhaber ############### Kontostand ################# PIN ##########")
            for i in self.bank.konten:
                print("\t" + str(i.kontonummer) + "\t\t" + i.kontoinhaber.name + "\t\t" + str(i.kontostand) + "\t\t\t" + str(i.PIN))
            input("(Drücken sie Enter um fortzufahren)")
            self.hauptmenü()

    def manage_bankkonten(self):
        if len(self.bank.konten) == 0:
            print("\nEs existieren keine Bankkonten!")
            input("(Drücken sie Enter um fortzufahren)")
            self.hauptmenü()
        else:
            print("Geben sie die Kontonummer des zu ändernden Kontos ein.")
            print("(Zum Abbrechen drücken sie die (1)).")
            kontonummer = input("(Zum erstellen eines neuen Kontos drücken sie die (2)): ")
            if kontonummer == "1":
                self.hauptmenü()
            elif kontonummer == "2":
                self.create_bankkonto()
            else:
                for i in self.bank.konten:
                    if kontonummer == i.kontonummer:
                        print("\nWelche der folgenden Aktionen wollen sie ausführen?")
                        print("(1) gespeicherte Daten bearbeiten")
                        print("(2) Konto löschen")
                        print("(3) abbrechen")
                        select_konto = input("Geben sie die entsprechende Nummer ein um fortzufahren: ")
                        print("")
                        if select_konto == "1":
                            self.admin_edit_bankkonto(i)
                        if select_konto == "2":
                            self.admin_del_bankkonto(i)
                        if select_konto == "3":
                            self.hauptmenü()
                        else:
                            print("Eingabe unzulässig. Probieren sie es erneut.\n")
                            self.manage_bankkonten()
                else:
                    print("Es existiert kein Konto mit dieser Kontonummer. Versuchen sie es erneut!\n")
                    self.manage_bankkonten()

    def admin_edit_bankkonto(self, konto:Konto):
        print("\nWelche der folgenden Daten wollen sie ändern?")
        print("(1) Kontoinhaber")
        print("(2) Kontostand")
        print("(3) PIN")
        print("(4) abbrechen")
        select_konto = input("Geben sie die entsprechende Nummer ein um fortzufahren: ")
        print("")
        if select_konto == "1":
            print("Zum Ändern des Kontoinhabers geben sie das Adminpasswort ein.")
            passwort = input("(Zum Abbrechen drücken sie die (1)): ")
            if passwort == "1":
                self.hauptmenü()
            elif passwort == self.passwort:
                print("Geben sie die ID des neuen Kontoinhabers ein.")
                ID = input("(Zum Abbrechen drücken sie die (1)): ")
                if ID == "1":
                    self.hauptmenü()
                else:
                    for i in self.bank.kunden:
                        if ID == i.kundenID:
                            konto.kontoinhaber = i
                            print("Der Kontoinhaber wurde erfolgreich geändert!")
                            input("(Drücken sie Enter um fortzufahren)")
                            self.hauptmenü()
                    else:
                        print("Es existiert kein Kunde mit dieser ID. Versuchen sie es erneut!\n")
                        self.admin_edit_bankkonto(konto)
            else:
                print("Das Passwort ist falsch. Versuchen sie es erneut!")
                self.admin_edit_bankkonto(konto)
        if select_konto == "2":
            print("Wollen sie Geld einzahlen oder abheben?")
            print("(1) einzahlen")
            print("(2) abheben")
            print("(3) abbrechen")
            select_money = input("Geben sie die entsprechende Nummer ein um fortzufahren: ")
            print("")
            if select_money == "1":
                self.konto.einzahlen(float(input("Geben sie den einzuzahlenden Betrag ein: ")))
                self.hauptmenü()
            if select_money == "2":
                self.konto.abheben(float(input("Geben sie den abzuhebenden Betrag ein: ")))
                self.hauptmenü()
        if select_konto == "3":
            konto.PIN = input("Geben sie die neue PIN ein: ")
            print("Die PIN wurde erfolgreich geändert!")
            input("(Drücken sie Enter um fortzufahren)")
            self.hauptmenü()
        if select_konto == "4":
            self.hauptmenü()
        else:
            print("Eingabe unzulässig. Probieren sie es erneut.\n")
            self.admin_edit_bankkonto(konto)

    def admin_del_bankkonto(self, konto:Konto):
        print("Zum Löschen des Kontos geben sie das Adminpasswort ein.")
        passwort = input("(Zum Abbrechen drücken sie die (1)): ")
        if passwort == "1":
            self.hauptmenü()
        elif passwort == self.passwort:
            self.bank.konten.remove(konto)
            print("Das Konto wurde erfolgreich gelöscht!")
            input("(Drücken sie Enter um fortzufahren)")
            self.hauptmenü()
        else:
            print("Das Passwort ist falsch. Versuchen sie es erneut!")
            self.admin_del_bankkonto(konto)

    def standort(self):
        if len(self.bank.standorte) == 0:
            print("Die Bank hat noch keine festen Standorte!")
        else:
            print("\n#######################################################################################################")
            print("############################################ Standort ##################################################")
            print("#######################################################################################################")
            for i in self.bank.standorte:
                print("\t\t" + i + "\t\t")
        print("\nWelche der folgenden Aktionen wollen sie ausführen?")
        print("(1) Standort hinzufügen")
        print("(2) Standort bearbeiten")
        print("(3) Standort löschen")
        print("(4) abbrechen")
        select_location = input("Geben sie die entsprechende Nummer ein um fortzufahren: ")
        if select_location == "1":
            self.create_standort()
        if select_location == "2":
            self.edit_standort()
        if select_location == "3":
            self.del_standort()
        if select_location == "4":
            self.hauptmenü()
        else:
            print("Eingabe unzulässig. Probieren sie es erneut.\n")
            self.standort()

    def create_standort(self):
        print("Um einen neuen Standort anzulegen geben sie die folgenden Daten ein:")
        PLZ = input("Postleitzahl: ")
        stadt = input("Stadt: ")
        straße = input("Straße: ")
        hausnummer = input("Hausnummer: ")
        ID = str(len(self.bank.standorte) + 1)
        standort = PLZ + " " + stadt + ", " + straße + " " + hausnummer
        self.bank.standorte.append([ID, standort])
        print("Der Standort wurde erfolgreich hinzugefügt!")
        input("(Drücken sie Enter um fortzufahren)")
        self.hauptmenü()
    
    def edit_standort(self):
        print("Geben sie den Index des zu bearbeitenden Standorts ein.")
        ID = input("(Zum Abbrechen drücken sie die (1)): ")
        if ID == "1":
            self.hauptmenü()
        else:
            for i in self.bank.standorte:
                if ID == i[0]:
                    print("Geben sie die neuen Daten ein:")
                    PLZ = input("Postleitzahl: ")
                    stadt = input("Stadt: ")
                    straße = input("Straße: ")
                    hausnummer = input("Hausnummer: ")
                    standort = PLZ + " " + stadt + ", " + straße + " " + hausnummer
                    index = self.bank.standorte.index(i)
                    self.bank.standorte.remove(i)
                    self.bank.standorte.insert(index, [index + 1, standort])
                    print("Der Standort wurde erfolgreich geändert!")
                    input("(Drücken sie Enter um fortzufahren)")
                    self.hauptmenü()
            else:
                print("Es existiert kein Standort mit dieser ID. Versuchen sie es erneut!\n")
                self.edit_standort()
    
    def del_standort(self):
        print("Zum Löschen des Standorts geben sie das Adminpasswort ein.")
        passwort = input("(Zum Abbrechen drücken sie die (1)): ")
        if passwort == "1":
            self.hauptmenü()
        elif passwort == self.passwort:
            removed = False
            print("Geben sie den Index des zu löschenden Standorts ein.")
            ID = input("(Zum Abbrechen drücken sie die (1)): ")
            if ID == "1":
                self.hauptmenü()
            else:
                for i in self.bank.standorte:
                    if removed == False:
                        if ID == i[0]:
                            self.bank.standorte.remove(i)
                            removed = True
                    elif removed == True:
                        i[0] = str(self.bank.standorte.index(i) + 1) # ID neu setzen, da sich die Liste verändert hat
                if removed == True:
                    print("Der Standort wurde erfolgreich gelöscht!")
                    input("(Drücken sie Enter um fortzufahren)")
                    self.hauptmenü()
                else:
                    print("Es existiert kein Standort mit dieser ID. Versuchen sie es erneut!\n")
                    self.del_standort()
        else:
            print("Das Passwort ist falsch. Versuchen sie es erneut!")
            self.del_standort()


##############################################
# Hauptprogramm
##############################################

mainbank = Bank("Roffmann Trusts")

user = Userinterface(mainbank, "a")

user.hauptmenü()