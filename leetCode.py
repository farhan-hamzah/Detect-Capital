class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return (
            word.isupper() or     # Semua huruf kapital
            word.islower() or     # Semua huruf kecil
            word.istitle()        # Hanya huruf pertama kapital
        )

# Contoh penggunaan dari terminal
if __name__ == "__main__":
    word = input("Masukkan sebuah kata: ")
    sol = Solution()
    if sol.detectCapitalUse(word):
        print("Penggunaan kapital BENAR.")
    else:
        print("Penggunaan kapital SALAH.")
