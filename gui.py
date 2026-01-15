import customtkinter as ctk
import random
import time

# Alapbeállítások: Sötét mód és kék téma
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class STPJatek(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("STP Root Bridge Választó Gyakorló")
        self.geometry("600x500")

        # Játék változók
        self.helyes_valasz = ""
        self.pontszam = 0
        self.hatralevo_ido = 10
        self.időzítő_fut = False

        # UI elemek létrehozása
        self.label_pont = ctk.CTkLabel(self, text="Pontszám: 0", font=("Arial", 16))
        self.label_pont.pack(pady=10)

        self.label_ido = ctk.CTkLabel(self, text="Idő: 10s", font=("Arial", 24, "bold"), text_color="orange")
        self.label_ido.pack(pady=10)

        self.label_kerdes = ctk.CTkLabel(self, text="Melyik a Root Bridge (legkisebb BID)?", font=("Arial", 18))
        self.label_kerdes.pack(pady=20)

        # Gombok tárolója
        self.gomb_keret = ctk.CTkFrame(self)
        self.gomb_keret.pack(pady=10, padx=20, fill="both", expand=True)

        self.gombok = []
        for i in range(3):
            gomb = ctk.CTkButton(self.gomb_keret, text="", font=("Courier", 14), 
                                 command=lambda x=i: self.ellenorzes(x))
            gomb.pack(pady=10, padx=20, fill="x")
            self.gombok.append(gomb)

        self.label_visszajelzes = ctk.CTkLabel(self, text="", font=("Arial", 14))
        self.label_visszajelzes.pack(pady=20)

        # Első kör indítása
        self.uj_kor()

    def general_mac(self):
        """Véletlenszerű MAC címet generál."""
        return ":".join(["{:02x}".format(random.randint(0, 255)) for _ in range(6)])

    def uj_kor(self):
        """Új feladványt generál és indítja az órát."""
        switchek = []
        prioritasok = [4096, 8192, 20480, 32768, 61440]
        
        for i in range(3):
            prio = random.choice(prioritasok)
            mac = self.general_mac()
            switchek.append({"id": i, "prio": prio, "mac": mac, "szoveg": f"Switch {chr(65+i)} -> Prio: {prio}, MAC: {mac}"})

        # Meghatározzuk a győztest (legkisebb prio, majd legkisebb MAC)
        gyoztes = min(switchek, key=lambda s: (s["prio"], s["mac"]))
        self.helyes_valasz = gyoztes["id"]

        # Gombok frissítése
        for i in range(3):
            self.gombok[i].configure(text=switchek[i]["szoveg"], fg_color=["#3B8ED0", "#1F6AA5"]) # Alap szín visszaállítása

        self.hatralevo_ido = 10
        self.label_visszajelzes.configure(text="")
        
        if not self.időzítő_fut:
            self.időzítő_fut = True
            self.visszaszamlalas()

    def visszaszamlalas(self):
        """Az időzítő logikája."""
        if self.időzítő_fut:
            if self.hatralevo_ido > 0:
                self.label_ido.configure(text=f"Idő: {self.hatralevo_ido}s")
                self.hatralevo_ido -= 1
                self.after(1000, self.visszaszamlalas)
            else:
                self.időzítő_fut = False
                self.label_visszajelzes.configure(text="LEJÁRT AZ IDŐ!", text_color="red")
                self.after(2000, self.uj_kor)

    def ellenorzes(self, gomb_id):
        """Ellenőrzi, hogy a jó gombra kattintott-e a felhasználó."""
        if not self.időzítő_fut: return # Ha lejárt az idő, ne lehessen kattintani

        if gomb_id == self.helyes_valasz:
            self.pontszam += 1
            self.label_pont.configure(text=f"Pontszám: {self.pontszam}")
            self.label_visszajelzes.configure(text="HELYES! Jön a következő...", text_color="green")
            self.gombok[gomb_id].configure(fg_color="green")
            self.időzítő_fut = False # Megállítjuk az órát a következő körig
            self.after(1000, self.uj_kor)
        else:
            self.label_visszajelzes.configure(text="ROSSZ VÁLASZ! Próbáld újra!", text_color="red")
            self.gombok[gomb_id].configure(fg_color="red")
            self.pontszam = max(0, self.pontszam - 1)
            self.label_pont.configure(text=f"Pontszám: {self.pontszam}")

# Program indítása
if __name__ == "__main__":
    app = STPJatek()
    app.mainloop()