from FSM import State


class ChatbotEngine:
    def __init__(self):
        self.state = State.START

    def process(self, user_input):
        user_input = user_input.lower()

        if self.state == State.START:
            self.state = State.MENU
            return (
                "Selamat datang di Chatbot Layanan Publik.\n"
                "Pilih layanan:\n"
                "1. Informasi KTP\n"
                "2. Informasi Kartu Keluarga (KK)\n"
                "3. Informasi Akta Kelahiran\n"
                "4. Pengaduan Masyarakat\n"
                "5. Keluar"
            )

        elif self.state == State.MENU:

            if user_input == "1":
                self.state = State.KTP
                return (
                    "Persyaratan pembuatan KTP:\n"
                    "- Berusia 17 tahun atau sudah menikah\n"
                    "- Membawa Kartu Keluarga\n"
                    "- Datang ke kantor Disdukcapil"
                )

            elif user_input == "2":
                self.state = State.KK
                return (
                    "Persyaratan pembuatan KK:\n"
                    "- Surat pengantar RT/RW\n"
                    "- Buku nikah/akta perkawinan\n"
                    "- Dokumen pendukung lainnya"
                )

            elif user_input == "3":
                self.state = State.AKTA
                return (
                    "Persyaratan Akta Kelahiran:\n"
                    "- Surat kelahiran dari rumah sakit\n"
                    "- KTP orang tua\n"
                    "- Kartu Keluarga"
                )

            elif user_input == "4":
                self.state = State.PENGADUAN
                return (
                    "Silakan tuliskan pengaduan Anda.\n"
                    "Contoh: Jalan rusak di Desa Sukamaju."
                )

            elif user_input == "5":
                self.state = State.EXIT
                return "Terima kasih telah menggunakan layanan kami."

            else:
                return "Pilihan tidak tersedia. Masukkan angka 1-5."

        elif self.state == State.KTP:
            self.state = State.MENU
            return (
                "Kembali ke menu utama.\n"
                "1. KTP\n"
                "2. KK\n"
                "3. Akta Kelahiran\n"
                "4. Pengaduan\n"
                "5. Keluar"
            )

        elif self.state == State.KK:
            self.state = State.MENU
            return (
                "Kembali ke menu utama.\n"
                "1. KTP\n"
                "2. KK\n"
                "3. Akta Kelahiran\n"
                "4. Pengaduan\n"
                "5. Keluar"
            )

        elif self.state == State.AKTA:
            self.state = State.MENU
            return (
                "Kembali ke menu utama.\n"
                "1. KTP\n"
                "2. KK\n"
                "3. Akta Kelahiran\n"
                "4. Pengaduan\n"
                "5. Keluar"
            )

        elif self.state == State.PENGADUAN:
            pengaduan = user_input
            self.state = State.MENU

            return (
                f"Pengaduan Anda telah diterima:\n'{pengaduan}'\n\n"
                "Terima kasih atas laporan Anda.\n"
                "Kembali ke menu utama.\n"
                "1. KTP\n"
                "2. KK\n"
                "3. Akta Kelahiran\n"
                "4. Pengaduan\n"
                "5. Keluar"
            )

        elif self.state == State.EXIT:
            return "Program selesai."