import csv
import random
import re
import uuid

# ===== FILE INPUT & OUTPUT =====
INPUT_FILE = 'alumni.csv'
OUTPUT_KONTAK = 'kontak_alumni.csv'
OUTPUT_PEKERJAAN = 'pekerjaan_alumni.csv'

# ===== HELPER FUNCTIONS =====
def clean_name(name):
    name = name.lower()
    name = re.sub(r'[^a-z0-9 ]', '', name)
    name = name.replace(" ", "")
    return name

def random_phone():
    return "08" + str(random.randint(1000000000, 9999999999))

def random_job():
    jobs = [
        "Staff IT", "Manager", "Admin", "Software Engineer",
        "Data Analyst", "HRD", "Marketing", "Finance"
    ]
    return random.choice(jobs)

def random_company():
    companies = [
        "PT Maju Jaya", "CV Sejahtera", "Startup Nusantara",
        "Tech Indo", "Global Corp", "Digital Solusi"
    ]
    return random.choice(companies)

def random_city():
    return random.choice(["Jakarta", "Surabaya", "Bandung", "Yogyakarta", "Semarang"])

def random_job_type():
    return random.choice(["PNS", "Swasta", "Wirausaha"])

# ===== MAIN PROCESS =====
def generate_data():
    with open(INPUT_FILE, newline='', encoding='utf-8') as infile:
        reader = csv.DictReader(infile)

        with open(OUTPUT_KONTAK, 'w', newline='', encoding='utf-8') as kontak_file, \
             open(OUTPUT_PEKERJAAN, 'w', newline='', encoding='utf-8') as kerja_file:

            kontak_writer = csv.writer(kontak_file)
            kerja_writer = csv.writer(kerja_file)

            # HEADER SESUAI SUPABASE
            kontak_writer.writerow([
                'id', 'nim', 'email', 'no_hp',
                'linkedin', 'instagram', 'facebook', 'tiktok'
            ])

            kerja_writer.writerow([
                'id', 'nim', 'tempat_kerja', 'alamat_kerja',
                'posisi', 'jenis_pekerjaan', 'sosial_media_perusahaan'
            ])

            count = 0

            for row in reader:
                nama = row['nama']
                nim = row['nim']

                clean = clean_name(nama)

                # ===== KONTAK =====
                kontak_writer.writerow([
                    str(uuid.uuid4()),  # generate UUID
                    nim,
                    f"{clean}@gmail.com",
                    random_phone(),
                    f"https://linkedin.com/in/{clean}",
                    f"https://instagram.com/{clean}",
                    f"https://facebook.com/{clean}",
                    f"https://tiktok.com/@{clean}"
                ])

                # ===== PEKERJAAN =====
                kerja_writer.writerow([
                    str(uuid.uuid4()),  # UUID juga
                    nim,
                    random_company(),
                    random_city(),
                    random_job(),
                    random_job_type(),
                    f"https://instagram.com/{clean}_company"
                ])

                count += 1

                if count % 10000 == 0:
                    print(f"{count} data processed...")

            print(f"\nDONE. Total data: {count}")

# ===== RUN =====
if __name__ == "__main__":
    generate_data()