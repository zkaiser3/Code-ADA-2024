CREATE TABLE IF NOT EXISTS "patients" (
    "availability" INTEGER PRIMARY KEY AUTOINCREMENT,
    "reason" TEXT NOT NULL,
    "insurance" TEXT NOT NULL,
    "price_range" TEXT NOT NULL,
    "gender_preference" TEXT NOT NULL
);
