from datetime import datetime

def spocitej_dny_zivota():
    # Požádáme uživatele o zadání data
    datum_str = input("Zadej své datum narození (ve formátu DD.MM.RRRR, např. 25.04.1995): ")
    
    # Definujeme, jaký formát data očekáváme
    format_data = "%d.%m.%Y"
    
    try:
        # Převedeme zadaný text na reálný 'datumový' objekt
        datum_narozeni = datetime.strptime(datum_str, format_data).date()
        
        # Získáme aktuální dnešní datum
        dnesni_datum = datetime.now().date()
        
        # Odečteme data od sebe (Python zde automaticky řeší přestupné roky!)
        rozdil = dnesni_datum - datum_narozeni
        
        # Vypíšeme výsledek
        if rozdil.days < 0:
            print("Zadal jsi datum v budoucnosti! Cestování v čase zatím neumíme.")
        else:
            print(f"Od tvého narození do dnešního dne ({dnesni_datum.strftime('%d.%m.%Y')}) uběhlo přesně {rozdil.days} dní.")
            
    except ValueError:
        # Pokud uživatel zadá nesmysl nebo špatný formát
        print("Chyba: Zadal jsi špatný formát data. Zkus to znovu a použij formát DD.MM.RRRR.")

# Spuštění programu
if __name__ == "__main__":
    spocitej_dny_zivota()
