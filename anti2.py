DECISION_TREE = {
  "start": {
    "question": "Sizning davlat xizmatidagi holatingingiz qanday?",
    "options": ["Hozirda davlat xizmatchisiman", "Kelajakda davlat xizmatchisi bo'lmoqchiman", "Oldin davlat xizmatchisi bo'lganman"],
    "next": {
      "Hozirda davlat xizmatchisiman": "1",
      "Kelajakda davlat xizmatchisi bo'lmoqchiman": "2",
      "Oldin davlat xizmatchisi bo'lganman": "3"
    }
  },
  
  "1": {
    "question": "Qanday holatni tekshirmoqchisiz?",
    "options": ["Qo'shimcha faoliyat olib boryapman", "Kompaniya sherigiman", "Oldin faoliyat olib borganman", "Qo'shimcha faoliyat rejalashtiryapman", "Kompaniya sherigi bo'lishni rejalashtiryapman"],
    "next": {
      "Qo'shimcha faoliyat olib boryapman": "1.1",
      "Kompaniya sherigiman": "1.2",
      "Oldin faoliyat olib borganman": "1.3",
      "Qo'shimcha faoliyat rejalashtiryapman": "1.4",
      "Kompaniya sherigi bo'lishni rejalashtiryapman": "1.5"
    }
  },
  
  "1.1": {
    "question": "Qo'shimcha faoliyatingiz qaysi sektorda?",
    "options": ["Xususiy sektorda", "Davlat sektorda"],
    "next": {
      "Xususiy sektorda": "1.1.1",
      "Davlat sektorda": {
        "title": "⚠️ Qonuniy maslahat kerak",
        "steps": ["Davlat xizmati boshqarmasiga murojaat qiling"],
        "analysis": "Davlat xizmatchisi sifatida davlat sektorida qo'shimcha faoliyat olib borish murakkab huquqiy vaziyatni keltirib chiqarishi mumkin. Bunday holatlar maxsus tartibga solinadi va har bir holat alohida ko'rib chiqilishi kerak.",
        "recommendations": [
          "15 kun ichida Davlat xizmati boshqarmasiga yozma ravishda murojaat qiling",
          "Manfaatlar to'qnashuvi ehtimolini aniqlash uchun tegishli hujjatlarni tayyorlang",
          "Qo'shimcha faoliyat uchun kerakli ruxsatnomalarni olish tartibini o'rganing"
        ],
        "legal_basis": [
          "O'zbekiston Respublikasi Adliya vazirligi tomonidan 2024-yil 5-noyabrda ro'yxatdan o'tkazilgan ro'yxat raqami 3569",
          "O'zbekiston Respublikasining 05.06.2024 yildagi O'RQ-931-son qonuni",
          "O'zbekiston Respublikasining 'Korrupsiyaga qarshi kurashish to'g'risida'gi qonuni"
        ]
      }
    }
  },
  
  "1.1.1": {
    "question": "Xususiy sektordagi faoliyatingiz turi?",
    "options": ["Xususiy kompaniyada", "Shaxsiy sifatda (tadbirkorlik)"],
    "next": {
      "Xususiy kompaniyada": "1.1.1.1",
      "Shaxsiy sifatda (tadbirkorlik)": "1.1.1.2"
    }
  },
  
  "1.1.1.1": {
    "question": "Faoliyat uchun ruxsatnoma oldingizmi?",
    "options": ["Ha", "Yo'q"],
    "next": {
      "Ha": "1.1.1.1.2",
      "Yo'q": {
        "title": "⚠️ Qonuniy maslahat kerak",
        "steps": ["Korrupsiyaga qarshi kurashish agentligiga murojaat qiling"],
        "analysis": "Davlat xizmatchisi sifatida xususiy kompaniyada qo'shimcha faoliyat olib borish uchun ruxsatnoma olish qonun bilan belgilangan majburiyatdir. Ruxsatnomasiz faoliyat olib borish manfaatlar to'qnashuviga olib kelishi mumkin.",
        "recommendations": [
          "Zudlik bilan faoliyatni to'xtatish yoki vaqtincha to'xtatib turish",
          "15 kun ichida Korrupsiyaga qarshi kurashish agentligiga murojaat qilib, vaziyatni tushuntirish",
          "Ruxsatnoma olish tartibini o'rganish va tegishli hujjatlarni topshirish"
        ],
        "legal_basis": [
          "O'zbekiston Respublikasi Adliya vazirligi tomonidan 2024-yil 5-noyabrda ro'yxatdan o'tkazilgan ro'yxat raqami 3569",
          "O'zbekiston Respublikasining 05.06.2024 yildagi O'RQ-931-son qonuni",
          "O'zbekiston Respublikasining 'Korrupsiyaga qarshi kurashish to'g'risida'gi qonuni"
        ]
      }
    }
  },
  
  "1.1.1.1.2": {
    "question": "Faoliyatingiz davlat xizmatiga bog'liqmi?",
    "options": ["Ha", "Yo'q"],
    "next": {
      "Ha": {
        "title": "⚠️ Potentsial manfaatlar to'qnashuvi",
        "steps": ["Axloq komissiyasidan maslahat olish kerak"],
        "analysis": "Davlat xizmatiga bog'liq bo'lgan qo'shimcha faoliyat manfaatlar to'qnashuviga olib kelishi mumkin. Davlat xizmatchisining davlat vazifalari va xususiy faoliyati o'rtasida bog'liqlik bo'lsa, bu qarorlar qabul qilishda xolislikka putur yetkazishi mumkin.",
        "recommendations": [
          "30 kun ichida axloq komissiyasiga yozma ravishda murojaat qiling",
          "O'zingizning davlat xizmatidagi funksiyalaringiz va xususiy faoliyatingiz o'rtasidagi bog'liqlikni aniq ko'rsating",
          "Qo'shimcha faoliyat davom ettirilsa, manfaatlar to'qnashuvini oldini olish uchun aniq chora-tadbirlarni taklif eting",
          "Davlat xizmati bilan bog'liq qarorlarda o'zingizni chetga olish tartibini o'rganing"
        ],
        "legal_basis": [
          "O'zbekiston Respublikasi Adliya vazirligi tomonidan 2024-yil 5-noyabrda ro'yxatdan o'tkazilgan ro'yxat raqami 3569",
          "O'zbekiston Respublikasining 05.06.2024 yildagi O'RQ-931-son qonuni",
          "O'zbekiston Respublikasining 'Korrupsiyaga qarshi kurashish to'g'risida'gi qonuni"
        ]
      },
      "Yo'q": "1.1.1.1.3"
    }
  },
  
  "1.1.1.1.3": {
    "question": "Kompaniya davlat bilan shartnomaviy aloqadami?",
    "options": ["Ha", "Yo'q"],
    "next": {
      "Ha": {
        "title": "⚠️ Potentsial manfaatlar to'qnashuvi",
        "steps": ["Tekshiruv kerak (Prokuratura yoki antikorrupsiya bo'linmasi)"],
        "analysis": "Davlat bilan shartnomaviy aloqada bo'lgan kompaniyada faoliyat yuritish manfaatlar to'qnashuviga olib kelishi mumkin. Davlat xizmatchisi sifatida siz o'z vazifalaringizni bajarishda xolislikni saqlashingiz kerak, ammo davlat bilan aloqadagi kompaniyada ishlash bu xolislikka putur yetkazishi mumkin.",
        "recommendations": [
          "30 kun ichida Prokuratura yoki antikorrupsiya bo'linmasiga murojaat qiling",
          "Davlat xizmatingiz va xususiy kompaniyadagi faoliyatingiz o'rtasida aniq chegaralar o'rnating",
          "Kompaniyaning davlat bilan shartnomaviy aloqalari to'g'risida ma'lumot to'plang",
          "Ruxsatnoma berilganligiga qaramasdan, bu holatda tegishli tekshiruv o'tkazilishi kerakligini esda tuting"
        ],
        "legal_basis": [
          "O'zbekiston Respublikasi Adliya vazirligi tomonidan 2024-yil 5-noyabrda ro'yxatdan o'tkazilgan ro'yxat raqami 3569",
          "O'zbekiston Respublikasining 05.06.2024 yildagi O'RQ-931-son qonuni",
          "O'zbekiston Respublikasining 'Korrupsiyaga qarshi kurashish to'g'risida'gi qonuni"
        ]
      },
      "Yo'q": "1.1.1.1.4"
    }
  },
  
  "1.1.1.1.4": {
    "question": "Yaqin qarindoshingiz ushbu kompaniyada ishlaydimi yoki sherikmi?",
    "options": ["Ha", "Yo'q"],
    "next": {
      "Ha": {
        "title": "⚠️ Potentsial manfaatlar to'qnashuvi",
        "steps": ["Korrupsiyaga qarshi kurashish agentligidan maslahat olish kerak"],
        "analysis": "Yaqin qarindoshingiz ishlayotgan yoki sherik bo'lgan kompaniyada faoliyat yuritish manfaatlar to'qnashuviga olib kelishi mumkin. Bu holat oilaviy aloqalar orqali davlat xizmatidagi qarorlaringizga ta'sir etishi mumkin bo'lgan vaziyatni keltirib chiqaradi.",
        "recommendations": [
          "30 kun ichida Korrupsiyaga qarshi kurashish agentligiga yozma ravishda murojaat qiling",
          "Yaqin qarindoshingiz bilan ishlaydigan kompaniyadagi o'zaro munosabatlaringizni aniq ko'rsating",
          "Davlat xizmatidagi vazifalaringizni bajarishda qarindoshlik aloqalari ta'sir qilmasligini ta'minlash uchun choralar taklif eting",
          "Qarindoshlaringiz bilan bog'liq qarorlar qabul qilishda o'zingizni chetga olish tartibini o'rganing"
        ],
        "legal_basis": [
          "O'zbekiston Respublikasi Adliya vazirligi tomonidan 2024-yil 5-noyabrda ro'yxatdan o'tkazilgan ro'yxat raqami 3569",
          "O'zbekiston Respublikasining 05.06.2024 yildagi O'RQ-931-son qonuni",
          "O'zbekiston Respublikasining 'Korrupsiyaga qarshi kurashish to'g'risida'gi qonuni"
        ]
      },
      "Yo'q": {
        "title": "✅ Manfaatlar to'qnashuvi yo'q",
        "steps": ["Sizning holatda manfaatlar to'qnashuvi aniqlanmadi"],
        "analysis": "Sizning vaziyatingiz manfaatlar to'qnashuviga olib kelmasligini ko'rsatmoqda. Siz xususiy kompaniyada qo'shimcha faoliyat olib borish uchun ruxsatnoma olgansiz, bu faoliyat davlat xizmatiga bog'liq emas, kompaniya davlat bilan shartnomaviy aloqada emas va yaqin qarindoshlaringiz bu kompaniyada ishlamaydi yoki sherik emas.",
        "recommendations": [
          "Vaziyatingizda o'zgarishlar bo'lsa, qaytadan tekshiruv o'tkazing",
          "Har yilgi daromad va mulk deklaratsiyasida bu qo'shimcha faoliyatni ko'rsating",
          "Kompaniyaning kelajakda davlat bilan aloqalari paydo bo'lsa, bu haqda xabar bering",
          "Davlat xizmati va qo'shimcha faoliyat o'rtasida aniq chegaralar saqlang"
        ],
        "legal_basis": [
          "O'zbekiston Respublikasi Adliya vazirligi tomonidan 2024-yil 5-noyabrda ro'yxatdan o'tkazilgan ro'yxat raqami 3569",
          "O'zbekiston Respublikasining 05.06.2024 yildagi O'RQ-931-son qonuni",
          "O'zbekiston Respublikasining 'Korrupsiyaga qarshi kurashish to'g'risida'gi qonuni"
        ]
      }
    }
  },
  
  "1.1.1.2": {
    "question": "Faoliyat uchun ruxsatnoma oldingizmi?",
    "options": ["Ha", "Yo'q"],
    "next": {
      "Ha": "1.1.1.2.2",
      "Yo'q": {
        "title": "⚠️ Qonuniy maslahat kerak",
        "steps": ["Korrupsiyaga qarshi kurashish agentligiga murojaat qiling"],
        "analysis": "Davlat xizmatchisi sifatida shaxsiy tadbirkorlik faoliyatini olib borish uchun ruxsatnoma olish qonun bilan belgilangan majburiyatdir. Ruxsatnomasiz faoliyat olib borish manfaatlar to'qnashuviga va ma'muriy javobgarlikka olib kelishi mumkin.",
        "recommendations": [
          "Zudlik bilan tadbirkorlik faoliyatini to'xtatish yoki vaqtincha to'xtatib turish",
          "15 kun ichida Korrupsiyaga qarshi kurashish agentligiga murojaat qilib, vaziyatni tushuntirish",
          "Tadbirkorlik faoliyati uchun ruxsatnoma olish tartibini o'rganish va hujjatlarni topshirish"
        ],
        "legal_basis": [
          "O'zbekiston Respublikasi Adliya vazirligi tomonidan 2024-yil 5-noyabrda ro'yxatdan o'tkazilgan ro'yxat raqami 3569",
          "O'zbekiston Respublikasining 05.06.2024 yildagi O'RQ-931-son qonuni",
          "O'zbekiston Respublikasining 'Korrupsiyaga qarshi kurashish to'g'risida'gi qonuni"
        ]
      }
    }
  },
  
  "1.1.1.2.2": {
    "question": "Faoliyatingiz davlat xizmatiga bog'liqmi?",
    "options": ["Ha", "Yo'q"],
    "next": {
      "Ha": {
        "title": "⚠️ Potentsial manfaatlar to'qnashuvi",
        "steps": ["Axloq komissiyasidan maslahat olish kerak"],
        "analysis": "Davlat xizmatiga bog'liq bo'lgan tadbirkorlik faoliyati manfaatlar to'qnashuviga olib kelishi mumkin. Davlat xizmatchisining davlat vazifalari va shaxsiy tadbirkorlik faoliyati o'rtasida bog'liqlik bo'lsa, bu qarorlar qabul qilishda xolislikka putur yetkazishi mumkin.",
        "recommendations": [
          "30 kun ichida axloq komissiyasiga yozma ravishda murojaat qiling",
          "O'zingizning davlat xizmatidagi funksiyalaringiz va tadbirkorlik faoliyatingiz o'rtasidagi bog'liqlikni aniq ko'rsating",
          "Tadbirkorlik faoliyati davom ettirilsa, manfaatlar to'qnashuvini oldini olish uchun aniq chora-tadbirlarni taklif eting",
          "Davlat xizmati bilan bog'liq qarorlarda o'zingizni chetga olish tartibini o'rganing"
        ],
        "legal_basis": [
          "O'zbekiston Respublikasi Adliya vazirligi tomonidan 2024-yil 5-noyabrda ro'yxatdan o'tkazilgan ro'yxat raqami 3569",
          "O'zbekiston Respublikasining 05.06.2024 yildagi O'RQ-931-son qonuni",
          "O'zbekiston Respublikasining 'Korrupsiyaga qarshi kurashish to'g'risida'gi qonuni"
        ]
      },
      "Yo'q": "1.1.1.2.3"
    }
  },
  
  "1.1.1.2.3": {
    "question": "Faoliyatingiz davlat bilan aloqadami?",
    "options": ["Ha", "Yo'q"],
    "next": {
      "Ha": {
        "title": "⚠️ Potentsial manfaatlar to'qnashuvi",
        "steps": ["Tekshiruv kerak (Prokuratura yoki antikorrupsiya bo'linmasi)"],
        "analysis": "Davlat bilan aloqada bo'lgan tadbirkorlik faoliyatini yuritish manfaatlar to'qnashuviga olib kelishi mumkin. Davlat xizmatchisi sifatida siz o'z vazifalaringizni bajarishda xolislikni saqlashingiz kerak, ammo davlat bilan aloqadagi tadbirkorlik bu xolislikka putur yetkazishi mumkin.",
        "recommendations": [
          "30 kun ichida Prokuratura yoki antikorrupsiya bo'linmasiga murojaat qiling",
          "Davlat xizmatingiz va tadbirkorlik faoliyatingiz o'rtasida aniq chegaralar o'rnating",
          "Tadbirkorlik faoliyatingizning davlat bilan aloqalari to'g'risida ma'lumot to'plang",
          "Ruxsatnoma berilganligiga qaramasdan, bu holatda tegishli tekshiruv o'tkazilishi kerakligini esda tuting"
        ],
        "legal_basis": [
          "O'zbekiston Respublikasi Adliya vazirligi tomonidan 2024-yil 5-noyabrda ro'yxatdan o'tkazilgan ro'yxat raqami 3569",
          "O'zbekiston Respublikasining 05.06.2024 yildagi O'RQ-931-son qonuni",
          "O'zbekiston Respublikasining 'Korrupsiyaga qarshi kurashish to'g'risida'gi qonuni"
        ]
      },
      "Yo'q": "1.1.1.2.4"
    }
  },
  
  "1.1.1.2.4": {
    "question": "Yaqin qarindoshingiz ushbu faoliyat bilan bog'liqmi?",
    "options": ["Ha", "Yo'q"],
    "next": {
      "Ha": {
        "title": "⚠️ Potentsial manfaatlar to'qnashuvi",
        "steps": ["Korrupsiyaga qarshi kurashish agentligidan maslahat olish kerak"],
        "analysis": "Yaqin qarindoshingiz bog'liq bo'lgan tadbirkorlik faoliyatini yuritish manfaatlar to'qnashuviga olib kelishi mumkin. Bu holat oilaviy aloqalar orqali davlat xizmatidagi qarorlaringizga ta'sir etishi mumkin bo'lgan vaziyatni keltirib chiqaradi.",
        "recommendations": [
          "30 kun ichida Korrupsiyaga qarshi kurashish agentligiga yozma ravishda murojaat qiling",
          "Yaqin qarindoshingiz bilan tadbirkorlikdagi o'zaro munosabatlaringizni aniq ko'rsating",
          "Davlat xizmatidagi vazifalaringizni bajarishda qarindoshlik aloqalari ta'sir qilmasligini ta'minlash uchun choralar taklif eting",
          "Qarindoshlaringiz bilan bog'liq qarorlar qabul qilishda o'zingizni chetga olish tartibini o'rganing"
        ],
        "legal_basis": [
          "O'zbekiston Respublikasi Adliya vazirligi tomonidan 2024-yil 5-noyabrda ro'yxatdan o'tkazilgan ro'yxat raqami 3569",
          "O'zbekiston Respublikasining 05.06.2024 yildagi O'RQ-931-son qonuni",
          "O'zbekiston Respublikasining 'Korrupsiyaga qarshi kurashish to'g'risida'gi qonuni"
        ]
      },
      "Yo'q": {
        "title": "✅ Manfaatlar to'qnashuvi yo'q",
        "steps": ["Sizning holatda manfaatlar to'qnashuvi aniqlanmadi"],
        "analysis": "Sizning vaziyatingiz manfaatlar to'qnashuviga olib kelmasligini ko'rsatmoqda. Siz tadbirkorlik faoliyati uchun ruxsatnoma olgansiz, bu faoliyat davlat xizmatiga bog'liq emas, davlat bilan aloqada emas va yaqin qarindoshlaringiz bu faoliyat bilan bog'liq emas.",
        "recommendations": [
          "Vaziyatingizda o'zgarishlar bo'lsa, qaytadan tekshiruv o'tkazing",
          "Har yilgi daromad va mulk deklaratsiyasida bu tadbirkorlik faoliyatini ko'rsating",
          "Tadbirkorlik faoliyatingizning kelajakda davlat bilan aloqalari paydo bo'lsa, bu haqda xabar bering",
          "Davlat xizmati va tadbirkorlik faoliyati o'rtasida aniq chegaralar saqlang"
        ],
        "legal_basis": [
          "O'zbekiston Respublikasi Adliya vazirligi tomonidan 2024-yil 5-noyabrda ro'yxatdan o'tkazilgan ro'yxat raqami 3569",
          "O'zbekiston Respublikasining 05.06.2024 yildagi O'RQ-931-son qonuni",
          "O'zbekiston Respublikasining 'Korrupsiyaga qarshi kurashish to'g'risida'gi qonuni"
        ]
      }
    }
  },
  
  "1.2": {
    "question": "Kompaniya davlat bilan shartnomaviy aloqadami?",
    "options": ["Ha", "Yo'q"],
    "next": {
      "Ha": {
        "title": "⚠️ Potentsial manfaatlar to'qnashuvi",
        "steps": ["Tekshiruv kerak (Prokuratura yoki antikorrupsiya bo'linmasi)"],
        "analysis": "Davlat bilan shartnomaviy aloqada bo'lgan kompaniyada sherik bo'lish manfaatlar to'qnashuviga olib kelishi mumkin. Davlat xizmatchisi sifatida siz o'z vazifalaringizni bajarishda xolislikni saqlashingiz kerak, ammo davlat bilan aloqadagi kompaniyada sheriklik bu xolislikka putur yetkazishi mumkin.",
        "recommendations": [
          "30 kun ichida Prokuratura yoki antikorrupsiya bo'linmasiga murojaat qiling",
          "Davlat xizmatingiz va kompaniyadagi sherikligingiz o'rtasida aniq chegaralar o'rnating",
          "Kompaniyaning davlat bilan shartnomaviy aloqalari to'g'risida ma'lumot to'plang",
          "Tekshiruv natijalariga ko'ra manfaatlar to'qnashuvini hal qilish choralarini ko'ring"
        ],
        "legal_basis": [
          "O'zbekiston Respublikasi Adliya vazirligi tomonidan 2024-yil 5-noyabrda ro'yxatdan o'tkazilgan ro'yxat raqami 3569",
          "O'zbekiston Respublikasining 05.06.2024 yildagi O'RQ-931-son qonuni",
          "O'zbekiston Respublikasining 'Korrupsiyaga qarshi kurashish to'g'risida'gi qonuni"
        ]
      },
      "Yo'q": "1.2.2"
    }
  },
  
  "1.2.2": {
    "question": "Sherikligingiz davlat xizmatiga bog'liqmi?",
    "options": ["Ha", "Yo'q"],
    "next": {
      "Ha": {
        "title": "⚠️ Potentsial manfaatlar to'qnashuvi",
        "steps": ["Axloq komissiyasidan maslahat olish kerak"],
        "analysis": "Davlat xizmatiga bog'liq bo'lgan kompaniyada sheriklik manfaatlar to'qnashuviga olib kelishi mumkin. Davlat xizmatchisining davlat vazifalari va shaxsiy biznes manfaatlari o'rtasida bog'liqlik bo'lsa, bu qarorlar qabul qilishda xolislikka putur yetkazishi mumkin.",
        "recommendations": [
          "30 kun ichida axloq komissiyasiga yozma ravishda murojaat qiling",
          "O'zingizning davlat xizmatidagi funksiyalaringiz va sheriklikdagi manfaatlaringiz o'rtasidagi bog'liqlikni aniq ko'rsating",
          "Sheriklik davom ettirilsa, manfaatlar to'qnashuvini oldini olish uchun aniq chora-tadbirlarni taklif eting",
          "Davlat xizmati bilan bog'liq qarorlarda o'zingizni chetga olish tartibini o'rganing"
        ],
        "legal_basis": [
          "O'zbekiston Respublikasi Adliya vazirligi tomonidan 2024-yil 5-noyabrda ro'yxatdan o'tkazilgan ro'yxat raqami 3569",
          "O'zbekiston Respublikasining 05.06.2024 yildagi O'RQ-931-son qonuni",
          "O'zbekiston Respublikasining 'Korrupsiyaga qarshi kurashish to'g'risida'gi qonuni"
        ]
      },
      "Yo'q": "1.2.3"
    }
  },
  
  "1.2.3": {
    "question": "Yaqin qarindoshingiz ushbu kompaniyada ishlaydimi yoki sherikmi?",
    "options": ["Ha", "Yo'q"],
    "next": {
      "Ha": {
        "title": "⚠️ Potentsial manfaatlar to'qnashuvi",
        "steps": ["Korrupsiyaga qarshi kurashish agentligidan maslahat olish kerak"],
        "analysis": "Yaqin qarindoshingiz ishlayotgan yoki sherik bo'lgan kompaniyada sheriklik qilish manfaatlar to'qnashuviga olib kelishi mumkin. Bu holat oilaviy aloqalar orqali davlat xizmatidagi qarorlaringizga ta'sir etishi mumkin bo'lgan vaziyatni keltirib chiqaradi.",
        "recommendations": [
          "30 kun ichida Korrupsiyaga qarshi kurashish agentligiga yozma ravishda murojaat qiling",
          "Yaqin qarindoshingiz bilan kompaniyadagi sheriklikdagi o'zaro munosabatlaringizni aniq ko'rsating",
          "Davlat xizmatidagi vazifalaringizni bajarishda qarindoshlik aloqalari ta'sir qilmasligini ta'minlash uchun choralar taklif eting",
          "Qarindoshlaringiz bilan bog'liq qarorlar qabul qilishda o'zingizni chetga olish tartibini o'rganing"
        ],
        "legal_basis": [
          "O'zbekiston Respublikasi Adliya vazirligi tomonidan 2024-yil 5-noyabrda ro'yxatdan o'tkazilgan ro'yxat raqami 3569",
          "O'zbekiston Respublikasining 05.06.2024 yildagi O'RQ-931-son qonuni",
          "O'zbekiston Respublikasining 'Korrupsiyaga qarshi kurashish to'g'risida'gi qonuni"
        ]
      },
      "Yo'q": {
        "title": "✅ Manfaatlar to'qnashuvi yo'q",
        "steps": ["Sizning holatda manfaatlar to'qnashuvi aniqlanmadi"],
        "analysis": "Sizning vaziyatingiz manfaatlar to'qnashuviga olib kelmasligini ko'rsatmoqda. Siz sherik bo'lgan kompaniya davlat bilan shartnomaviy aloqada emas, sheriklik davlat xizmatiga bog'liq emas va yaqin qarindoshlaringiz bu kompaniyada ishlamaydi yoki sherik emas.",
        "recommendations": [
          "Vaziyatingizda o'zgarishlar bo'lsa, qaytadan tekshiruv o'tkazing",
          "Har yilgi daromad va mulk deklaratsiyasida bu sheriklikni ko'rsating",
          "Kompaniyaning kelajakda davlat bilan aloqalari paydo bo'lsa, bu haqda xabar bering",
          "Davlat xizmati va sheriklik o'rtasida aniq chegaralar saqlang"
        ],
        "legal_basis": [
          "O'zbekiston Respublikasi Adliya vazirligi tomonidan 2024-yil 5-noyabrda ro'yxatdan o'tkazilgan ro'yxat raqami 3569",
          "O'zbekiston Respublikasining 05.06.2024 yildagi O'RQ-931-son qonuni",
          "O'zbekiston Respublikasining 'Korrupsiyaga qarshi kurashish to'g'risida'gi qonuni"
        ]
      }
    }
  },
  
  "1.3": {
    "question": "Oldingi faoliyatingiz hozirgi xizmatga bog'liqmi?",
    "options": ["Ha", "Yo'q"],
    "next": {
      "Ha": {
        "title": "⚠️ Potentsial manfaatlar to'qnashuvi",
        "steps": ["Axloq komissiyasidan maslahat olish kerak"],
        "analysis": "Oldingi faoliyatingiz hozirgi davlat xizmatiga bog'liq bo'lsa, bu manfaatlar to'qnashuviga olib kelishi mumkin. Oldingi faoliyatdagi aloqalaringiz va manfaatlaringiz hozirgi davlat xizmatidagi qarorlaringizga ta'sir etishi mumkin.",
        "recommendations": [
          "30 kun ichida axloq komissiyasiga yozma ravishda murojaat qiling",
          "Oldingi faoliyatingiz va hozirgi davlat xizmatidagi vazifalaringiz o'rtasidagi bog'liqlikni aniq ko'rsating",
          "Manfaatlar to'qnashuvini oldini olish uchun aniq chora-tadbirlarni taklif eting",
          "Oldingi faoliyatingiz bilan bog'liq qarorlar qabul qilishda o'zingizni chetga olish tartibini o'rganing"
        ],
        "legal_basis": [
          "O'zbekiston Respublikasi Adliya vazirligi tomonidan 2024-yil 5-noyabrda ro'yxatdan o'tkazilgan ro'yxat raqami 3569",
          "O'zbekiston Respublikasining 05.06.2024 yildagi O'RQ-931-son qonuni",
          "O'zbekiston Respublikasining 'Korrupsiyaga qarshi kurashish to'g'risida'gi qonuni"
        ]
      },
      "Yo'q": "1.3.2"
    }
  },
  
  "1.3.2": {
    "question": "Oldingi faoliyatingiz davlat bilan aloqadami?",
    "options": ["Ha", "Yo'q"],
    "next": {
      "Ha": {
        "title": "⚠️ Potentsial manfaatlar to'qnashuvi",
        "steps": ["Tekshiruv kerak (Prokuratura yoki antikorrupsiya bo'linmasi)"],
        "analysis": "Oldingi faoliyatingiz davlat bilan aloqada bo'lgan bo'lsa, bu manfaatlar to'qnashuviga olib kelishi mumkin. Oldingi faoliyatingizdagi davlat bilan bog'liq aloqalaringiz hozirgi davlat xizmatidagi qarorlaringizga ta'sir etishi mumkin.",
        "recommendations": [
          "30 kun ichida Prokuratura yoki antikorrupsiya bo'linmasiga murojaat qiling",
          "Oldingi faoliyatingizning davlat bilan aloqalari to'g'risida ma'lumot to'plang",
          "Davlat xizmati vazifalaringizni bajarishda oldingi faoliyatingiz ta'sir qilmasligini ta'minlash uchun choralar taklif eting",
          "Oldingi faoliyatingiz bilan bog'liq qarorlar qabul qilishda o'zingizni chetga olish tartibini o'rganing"
        ],
        "legal_basis": [
          "O'zbekiston Respublikasi Adliya vazirligi tomonidan 2024-yil 5-noyabrda ro'yxatdan o'tkazilgan ro'yxat raqami 3569",
          "O'zbekiston Respublikasining 05.06.2024 yildagi O'RQ-931-son qonuni",
          "O'zbekiston Respublikasining 'Korrupsiyaga qarshi kurashish to'g'risida'gi qonuni"
        ]
      },
      "Yo'q": "1.3.3"
    }
  },
  
  "1.3.3": {
    "question": "Yaqin qarindoshingiz ushbu faoliyat bilan bog'liqmi?",
    "options": ["Ha", "Yo'q"],
    "next": {
      "Ha": {
        "title": "⚠️ Potentsial manfaatlar to'qnashuvi",
        "steps": ["Korrupsiyaga qarshi kurashish agentligidan maslahat olish kerak"],
        "analysis": "Yaqin qarindoshingiz bog'liq bo'lgan oldingi faoliyatingiz manfaatlar to'qnashuviga olib kelishi mumkin. Bu holat oilaviy aloqalar orqali davlat xizmatidagi qarorlaringizga ta'sir etishi mumkin bo'lgan vaziyatni keltirib chiqaradi.",
        "recommendations": [
          "30 kun ichida Korrupsiyaga qarshi kurashish agentligiga yozma ravishda murojaat qiling",
          "Oldingi faoliyatingizdagi yaqin qarindoshingiz bilan o'zaro munosabatlaringizni aniq ko'rsating",
          "Davlat xizmatidagi vazifalaringizni bajarishda qarindoshlik aloqalari ta'sir qilmasligini ta'minlash uchun choralar taklif eting",
          "Qarindoshlaringiz bilan bog'liq qarorlar qabul qilishda o'zingizni chetga olish tartibini o'rganing"
        ],
        "legal_basis": [
          "O'zbekiston Respublikasi Adliya vazirligi tomonidan 2024-yil 5-noyabrda ro'yxatdan o'tkazilgan ro'yxat raqami 3569",
          "O'zbekiston Respublikasining 05.06.2024 yildagi O'RQ-931-son qonuni",
          "O'zbekiston Respublikasining 'Korrupsiyaga qarshi kurashish to'g'risida'gi qonuni"
        ]
      },
      "Yo'q": {
        "title": "✅ Manfaatlar to'qnashuvi yo'q",
        "steps": ["Sizning holatda manfaatlar to'qnashuvi aniqlanmadi"],
        "analysis": "Sizning vaziyatingiz manfaatlar to'qnashuviga olib kelmasligini ko'rsatmoqda. Oldingi faoliyatingiz hozirgi davlat xizmatiga bog'liq emas, davlat bilan aloqada emas va yaqin qarindoshlaringiz bu faoliyat bilan bog'liq emas.",
        "recommendations": [
          "Vaziyatingizda o'zgarishlar bo'lsa, qaytadan tekshiruv o'tkazing",
          "Har yilgi daromad va mulk deklaratsiyasida kerakli ma'lumotlarni ko'rsating",
          "Oldingi faoliyatingiz hozirgi xizmatingizga ta'sir qilishi mumkin bo'lgan o'zgarishlar yuzaga kelsa, bu haqda xabar bering",
          "Davlat xizmati va oldingi faoliyatingiz o'rtasida aniq chegaralar saqlang"
        ],
        "legal_basis": [
          "O'zbekiston Respublikasi Adliya vazirligi tomonidan 2024-yil 5-noyabrda ro'yxatdan o'tkazilgan ro'yxat raqami 3569",
          "O'zbekiston Respublikasining 05.06.2024 yildagi O'RQ-931-son qonuni",
          "O'zbekiston Respublikasining 'Korrupsiyaga qarshi kurashish to'g'risida'gi qonuni"
        ]
      }
    }
  },
  
  "1.4": {
    "question": "Qo'shimcha faoliyatingiz qaysi sektorda bo'ladi?",
    "options": ["Xususiy sektorda", "Davlat sektorda"],
    "next": {
      "Xususiy sektorda": "1.4.1",
      "Davlat sektorda": {
        "title": "⚠️ Qonuniy maslahat kerak",
        "steps": ["Davlat xizmati boshqarmasiga murojaat qiling"],
        "analysis": "Davlat xizmatchisi sifatida davlat sektorida qo'shimcha faoliyat rejalashtirish murakkab huquqiy vaziyatni keltirib chiqarishi mumkin. Bunday holatlar maxsus tartibga solinadi va har bir holat alohida ko'rib chiqilishi kerak.",
        "recommendations": [
          "15 kun ichida Davlat xizmati boshqarmasiga yozma ravishda murojaat qiling",
          "Manfaatlar to'qnashuvi ehtimolini aniqlash uchun tegishli hujjatlarni tayyorlang",
          "Qo'shimcha faoliyat uchun kerakli ruxsatnomalarni olish tartibini o'rganing"
        ],
        "legal_basis": [
          "O'zbekiston Respublikasi Adliya vazirligi tomonidan 2024-yil 5-noyabrda ro'yxatdan o'tkazilgan ro'yxat raqami 3569",
          "O'zbekiston Respublikasining 05.06.2024 yildagi O'RQ-931-son qonuni",
          "O'zbekiston Respublikasining 'Korrupsiyaga qarshi kurashish to'g'risida'gi qonuni"
        ]
      }
    }
  },
  
  "1.4.1": {
    "question": "Xususiy sektordagi faoliyatingiz turi qanday bo'ladi?",
    "options": ["Xususiy kompaniyada", "Shaxsiy sifatda"],
    "next": {
      "Xususiy kompaniyada": "1.4.1.1",
      "Shaxsiy sifatda": "1.4.1.2"
    }
  },
  
  "1.4.1.1": {
    "question": "Faoliyatingiz davlat xizmatiga bog'liq bo'ladimi?",
    "options": ["Ha", "Yo'q"],
    "next": {
      "Ha": {
        "title": "⚠️ Potentsial manfaatlar to'qnashuvi",
        "steps": ["Axloq komissiyasidan maslahat olish kerak"],
        "analysis": "Rejalashtirilayotgan qo'shimcha faoliyatingiz davlat xizmatiga bog'liq bo'lsa, bu manfaatlar to'qnashuviga olib kelishi mumkin. Davlat xizmatchisining davlat vazifalari va xususiy faoliyati o'rtasida bog'liqlik bo'lsa, bu qarorlar qabul qilishda xolislikka putur yetkazishi mumkin.",
        "recommendations": [
          "30 kun ichida axloq komissiyasiga yozma ravishda murojaat qiling",
          "Rejalashtirilayotgan faoliyatingiz va davlat xizmatidagi vazifalaringiz o'rtasidagi bog'liqlikni aniq ko'rsating",
          "Qo'shimcha faoliyatni boshlashdan oldin manfaatlar to'qnashuvini oldini olish uchun aniq chora-tadbirlarni taklif eting",
          "Davlat xizmati bilan bog'liq qarorlarda o'zingizni chetga olish tartibini o'rganing"
        ],
        "legal_basis": [
          "O'zbekiston Respublikasi Adliya vazirligi tomonidan 2024-yil 5-noyabrda ro'yxatdan o'tkazilgan ro'yxat raqami 3569",
          "O'zbekiston Respublikasining 05.06.2024 yildagi O'RQ-931-son qonuni",
          "O'zbekiston Respublikasining 'Korrupsiyaga qarshi kurashish to'g'risida'gi qonuni"
        ]
      },
      "Yo'q": "1.4.1.1.2"
    }
  },
  
  "1.4.1.1.2": {
    "question": "Kompaniya davlat bilan aloqada bo'ladimi?",
    "options": ["Ha", "Yo'q"],
    "next": {
      "Ha": {
        "title": "⚠️ Potentsial manfaatlar to'qnashuvi",
        "steps": ["Tekshiruv kerak (Prokuratura yoki antikorrupsiya bo'linmasi)"],
        "analysis": "Davlat bilan aloqada bo'lgan kompaniyada faoliyat yuritishni rejalashtirish manfaatlar to'qnashuviga olib kelishi mumkin. Davlat xizmatchisi sifatida siz o'z vazifalaringizni bajarishda xolislikni saqlashingiz kerak, ammo davlat bilan aloqadagi kompaniyada ishlash bu xolislikka putur yetkazishi mumkin.",
        "recommendations": [
          "30 kun ichida Prokuratura yoki antikorrupsiya bo'linmasiga murojaat qiling",
          "Davlat xizmatingiz va rejalashtirilayotgan faoliyatingiz o'rtasida aniq chegaralar o'rnating",
          "Kompaniyaning davlat bilan aloqalari to'g'risida ma'lumot to'plang",
          "Faoliyatni boshlashdan oldin tegishli tekshiruv o'tkazilishini ta'minlang"
        ],
        "legal_basis": [
          "O'zbekiston Respublikasi Adliya vazirligi tomonidan 2024-yil 5-noyabrda ro'yxatdan o'tkazilgan ro'yxat raqami 3569",
          "O'zbekiston Respublikasining 05.06.2024 yildagi O'RQ-931-son qonuni",
          "O'zbekiston Respublikasining 'Korrupsiyaga qarshi kurashish to'g'risida'gi qonuni"
        ]
      },
      "Yo'q": "1.4.1.1.3"
    }
  },
  
  "1.4.1.1.3": {
    "question": "Yaqin qarindoshingiz ushbu kompaniyada ishlaydimi yoki sherik bo'ladimi?",
    "options": ["Ha", "Yo'q"],
    "next": {
      "Ha": {
        "title": "⚠️ Potentsial manfaatlar to'qnashuvi",
        "steps": ["Korrupsiyaga qarshi kurashish agentligidan maslahat olish kerak"],
        "analysis": "Yaqin qarindoshingiz ishlayotgan yoki sherik bo'lgan kompaniyada faoliyat yuritishni rejalashtirish manfaatlar to'qnashuviga olib kelishi mumkin. Bu holat oilaviy aloqalar orqali davlat xizmatidagi qarorlaringizga ta'sir etishi mumkin bo'lgan vaziyatni keltirib chiqaradi.",
        "recommendations": [
          "30 kun ichida Korrupsiyaga qarshi kurashish agentligiga yozma ravishda murojaat qiling",
          "Rejalashtirilayotgan faoliyatingizda yaqin qarindoshingiz bilan o'zaro munosabatlaringizni aniq ko'rsating",
          "Davlat xizmatidagi vazifalaringizni bajarishda qarindoshlik aloqalari ta'sir qilmasligini ta'minlash uchun choralar taklif eting",
          "Qarindoshlaringiz bilan bog'liq qarorlar qabul qilishda o'zingizni chetga olish tartibini o'rganing"
        ],
        "legal_basis": [
          "O'zbekiston Respublikasi Adliya vazirligi tomonidan 2024-yil 5-noyabrda ro'yxatdan o'tkazilgan ro'yxat raqami 3569",
          "O'zbekiston Respublikasining 05.06.2024 yildagi O'RQ-931-son qonuni",
          "O'zbekiston Respublikasining 'Korrupsiyaga qarshi kurashish to'g'risida'gi qonuni"
        ]
      },
      "Yo'q": {
        "title": "✅ Manfaatlar to'qnashuvi yo'q",
        "steps": ["Sizning holatda manfaatlar to'qnashuvi aniqlanmadi"],
        "analysis": "Rejalashtirilayotgan faoliyatingiz manfaatlar to'qnashuviga olib kelmasligini ko'rsatmoqda. Siz rejalashtirayotgan xususiy kompaniyadagi faoliyat davlat xizmatiga bog'liq emas, kompaniya davlat bilan aloqada emas va yaqin qarindoshlaringiz bu kompaniyada ishlamaydi yoki sherik emas.",
        "recommendations": [
          "Faoliyatni boshlashdan oldin ruxsatnoma olishni unutmang",
          "Vaziyatingizda o'zgarishlar bo'lsa, qaytadan tekshiruv o'tkazing",
          "Har yilgi daromad va mulk deklaratsiyasida bu qo'shimcha faoliyatni ko'rsating",
          "Kompaniyaning kelajakda davlat bilan aloqalari paydo bo'lsa, bu haqda xabar bering"
        ],
        "legal_basis": [
          "O'zbekiston Respublikasi Adliya vazirligi tomonidan 2024-yil 5-noyabrda ro'yxatdan o'tkazilgan ro'yxat raqami 3569",
          "O'zbekiston Respublikasining 05.06.2024 yildagi O'RQ-931-son qonuni",
          "O'zbekiston Respublikasining 'Korrupsiyaga qarshi kurashish to'g'risida'gi qonuni"
        ]
      }
    }
  },
  
  "1.4.1.2": {
    "question": "Faoliyatingiz davlat xizmatiga bog'liq bo'ladimi?",
    "options": ["Ha", "Yo'q"],
    "next": {
      "Ha": {
        "title": "⚠️ Potentsial manfaatlar to'qnashuvi",
        "steps": ["Axloq komissiyasidan maslahat olish kerak"],
        "analysis": "Rejalashtirilayotgan shaxsiy tadbirkorlik faoliyatingiz davlat xizmatiga bog'liq bo'lsa, bu manfaatlar to'qnashuviga olib kelishi mumkin. Davlat xizmatchisining davlat vazifalari va shaxsiy tadbirkorlik faoliyati o'rtasida bog'liqlik bo'lsa, bu qarorlar qabul qilishda xolislikka putur yetkazishi mumkin.",
        "recommendations": [
          "30 kun ichida axloq komissiyasiga yozma ravishda murojaat qiling",
          "Rejalashtirilayotgan tadbirkorlik faoliyatingiz va davlat xizmatidagi vazifalaringiz o'rtasidagi bog'liqlikni aniq ko'rsating",
          "Tadbirkorlik faoliyatini boshlashdan oldin manfaatlar to'qnashuvini oldini olish uchun aniq chora-tadbirlarni taklif eting",
          "Davlat xizmati bilan bog'liq qarorlarda o'zingizni chetga olish tartibini o'rganing"
        ],
        "legal_basis": [
          "O'zbekiston Respublikasi Adliya vazirligi tomonidan 2024-yil 5-noyabrda ro'yxatdan o'tkazilgan ro'yxat raqami 3569",
          "O'zbekiston Respublikasining 05.06.2024 yildagi O'RQ-931-son qonuni",
          "O'zbekiston Respublikasining 'Korrupsiyaga qarshi kurashish to'g'risida'gi qonuni"
        ]
      },
      "Yo'q": "1.4.1.2.2"
    }
  },
  
  "1.4.1.2.2": {
    "question": "Faoliyatingiz davlat bilan aloqada bo'ladimi?",
    "options": ["Ha", "Yo'q"],
    "next": {
      "Ha": {
        "title": "⚠️ Potentsial manfaatlar to'qnashuvi",
        "steps": ["Tekshiruv kerak (Prokuratura yoki antikorrupsiya bo'linmasi)"],
        "analysis": "Davlat bilan aloqada bo'lgan tadbirkorlik faoliyatini yuritishni rejalashtirish manfaatlar to'qnashuviga olib kelishi mumkin. Davlat xizmatchisi sifatida siz o'z vazifalaringizni bajarishda xolislikni saqlashingiz kerak, ammo davlat bilan aloqadagi tadbirkorlik bu xolislikka putur yetkazishi mumkin.",
        "recommendations": [
          "30 kun ichida Prokuratura yoki antikorrupsiya bo'linmasiga murojaat qiling",
          "Davlat xizmatingiz va rejalashtirilayotgan tadbirkorlik faoliyatingiz o'rtasida aniq chegaralar o'rnating",
          "Tadbirkorlik faoliyatingizning davlat bilan aloqalari to'g'risida ma'lumot to'plang",
          "Faoliyatni boshlashdan oldin tegishli tekshiruv o'tkazilishini ta'minlang"
        ],
        "legal_basis": [
          "O'zbekiston Respublikasi Adliya vazirligi tomonidan 2024-yil 5-noyabrda ro'yxatdan o'tkazilgan ro'yxat raqami 3569",
          "O'zbekiston Respublikasining 05.06.2024 yildagi O'RQ-931-son qonuni",
          "O'zbekiston Respublikasining 'Korrupsiyaga qarshi kurashish to'g'risida'gi qonuni"
        ]
      },
      "Yo'q": "1.4.1.2.3"
    }
  },
  
  "1.4.1.2.3": {
    "question": "Yaqin qarindoshingiz ushbu faoliyat bilan bog'liq bo'ladimi?",
    "options": ["Ha", "Yo'q"],
    "next": {
      "Ha": {
        "title": "⚠️ Potentsial manfaatlar to'qnashuvi",
        "steps": ["Korrupsiyaga qarshi kurashish agentligidan maslahat olish kerak"],
        "analysis": "Yaqin qarindoshingiz bog'liq bo'lgan tadbirkorlik faoliyatini yuritishni rejalashtirish manfaatlar to'qnashuviga olib kelishi mumkin. Bu holat oilaviy aloqalar orqali davlat xizmatidagi qarorlaringizga ta'sir etishi mumkin bo'lgan vaziyatni keltirib chiqaradi.",
        "recommendations": [
          "30 kun ichida Korrupsiyaga qarshi kurashish agentligiga yozma ravishda murojaat qiling",
          "Rejalashtirilayotgan tadbirkorlikda yaqin qarindoshingiz bilan o'zaro munosabatlaringizni aniq ko'rsating",
          "Davlat xizmatidagi vazifalaringizni bajarishda qarindoshlik aloqalari ta'sir qilmasligini ta'minlash uchun choralar taklif eting",
          "Qarindoshlaringiz bilan bog'liq qarorlar qabul qilishda o'zingizni chetga olish tartibini o'rganing"
        ],
        "legal_basis": [
          "O'zbekiston Respublikasi Adliya vazirligi tomonidan 2024-yil 5-noyabrda ro'yxatdan o'tkazilgan ro'yxat raqami 3569",
          "O'zbekiston Respublikasining 05.06.2024 yildagi O'RQ-931-son qonuni",
          "O'zbekiston Respublikasining 'Korrupsiyaga qarshi kurashish to'g'risida'gi qonuni"
        ]
      },
      "Yo'q": {
        "title": "✅ Manfaatlar to'qnashuvi yo'q",
        "steps": ["Sizning holatda manfaatlar to'qnashuvi aniqlanmadi"],
        "analysis": "Rejalashtirilayotgan tadbirkorlik faoliyatingiz manfaatlar to'qnashuviga olib kelmasligini ko'rsatmoqda. Siz rejalashtirayotgan tadbirkorlik faoliyati davlat xizmatiga bog'liq emas, davlat bilan aloqada emas va yaqin qarindoshlaringiz bu faoliyat bilan bog'liq emas.",
        "recommendations": [
          "Faoliyatni boshlashdan oldin ruxsatnoma olishni unutmang",
          "Vaziyatingizda o'zgarishlar bo'lsa, qaytadan tekshiruv o'tkazing",
          "Har yilgi daromad va mulk deklaratsiyasida bu tadbirkorlik faoliyatini ko'rsating",
          "Tadbirkorlik faoliyatingizning kelajakda davlat bilan aloqalari paydo bo'lsa, bu haqda xabar bering"
        ],
        "legal_basis": [
          "O'zbekiston Respublikasi Adliya vazirligi tomonidan 2024-yil 5-noyabrda ro'yxatdan o'tkazilgan ro'yxat raqami 3569",
          "O'zbekiston Respublikasining 05.06.2024 yildagi O'RQ-931-son qonuni",
          "O'zbekiston Respublikasining 'Korrupsiyaga qarshi kurashish to'g'risida'gi qonuni"
        ]
      }
    }
  },
  
  "1.5": {
    "question": "Kompaniya davlat bilan aloqada bo'ladimi?",
    "options": ["Ha", "Yo'q"],
    "next": {
      "Ha": {
        "title": "⚠️ Potentsial manfaatlar to'qnashuvi",
        "steps": ["Tekshiruv kerak (Prokuratura yoki antikorrupsiya bo'linmasi)"],
        "analysis": "Davlat bilan aloqada bo'lgan kompaniyada sherik bo'lishni rejalashtirish manfaatlar to'qnashuviga olib kelishi mumkin. Davlat xizmatchisi sifatida siz o'z vazifalaringizni bajarishda xolislikni saqlashingiz kerak, ammo davlat bilan aloqadagi kompaniyada sheriklik bu xolislikka putur yetkazishi mumkin.",
        "recommendations": [
          "30 kun ichida Prokuratura yoki antikorrupsiya bo'linmasiga murojaat qiling",
          "Davlat xizmatingiz va rejalashtirilayotgan sherikligingiz o'rtasida aniq chegaralar o'rnating",
          "Kompaniyaning davlat bilan aloqalari to'g'risida ma'lumot to'plang",
          "Sheriklikni boshlashdan oldin tegishli tekshiruv o'tkazilishini ta'minlang"
        ],
        "legal_basis": [
          "O'zbekiston Respublikasi Adliya vazirligi tomonidan 2024-yil 5-noyabrda ro'yxatdan o'tkazilgan ro'yxat raqami 3569",
          "O'zbekiston Respublikasining 05.06.2024 yildagi O'RQ-931-son qonuni",
          "O'zbekiston Respublikasining 'Korrupsiyaga qarshi kurashish to'g'risida'gi qonuni"
        ]
      },
      "Yo'q": "1.5.2"
    }
  },
  
  "1.5.2": {
    "question": "Sherikligingiz davlat xizmatiga bog'liq bo'ladimi?",
    "options": ["Ha", "Yo'q"],
    "next": {
      "Ha": {
        "title": "⚠️ Potentsial manfaatlar to'qnashuvi",
        "steps": ["Axloq komissiyasidan maslahat olish kerak"],
        "analysis": "Davlat xizmatiga bog'liq bo'lgan kompaniyada sherik bo'lishni rejalashtirish manfaatlar to'qnashuviga olib kelishi mumkin. Davlat xizmatchisining davlat vazifalari va shaxsiy biznes manfaatlari o'rtasida bog'liqlik bo'lsa, bu qarorlar qabul qilishda xolislikka putur yetkazishi mumkin.",
        "recommendations": [
          "30 kun ichida axloq komissiyasiga yozma ravishda murojaat qiling",
          "Rejalashtirilayotgan sherikligingiz va davlat xizmatidagi vazifalaringiz o'rtasidagi bog'liqlikni aniq ko'rsating",
          "Sheriklikni boshlashdan oldin manfaatlar to'qnashuvini oldini olish uchun aniq chora-tadbirlarni taklif eting",
          "Davlat xizmati bilan bog'liq qarorlarda o'zingizni chetga olish tartibini o'rganing"
        ],
        "legal_basis": [
          "O'zbekiston Respublikasi Adliya vazirligi tomonidan 2024-yil 5-noyabrda ro'yxatdan o'tkazilgan ro'yxat raqami 3569",
          "O'zbekiston Respublikasining 05.06.2024 yildagi O'RQ-931-son qonuni",
          "O'zbekiston Respublikasining 'Korrupsiyaga qarshi kurashish to'g'risida'gi qonuni"
        ]
      },
      "Yo'q": "1.5.3"
    }
  },
  
  "1.5.3": {
    "question": "Yaqin qarindoshingiz ushbu kompaniyada ishlaydimi yoki sherik bo'ladimi?",
    "options": ["Ha", "Yo'q"],
    "next": {
      "Ha": {
        "title": "⚠️ Potentsial manfaatlar to'qnashuvi",
        "steps": ["Korrupsiyaga qarshi kurashish agentligidan maslahat olish kerak"],
        "analysis": "Yaqin qarindoshingiz ishlayotgan yoki sherik bo'lgan kompaniyada sherik bo'lishni rejalashtirish manfaatlar to'qnashuviga olib kelishi mumkin. Bu holat oilaviy aloqalar orqali davlat xizmatidagi qarorlaringizga ta'sir etishi mumkin bo'lgan vaziyatni keltirib chiqaradi.",
        "recommendations": [
          "30 kun ichida Korrupsiyaga qarshi kurashish agentligiga yozma ravishda murojaat qiling",
          "Rejalashtirilayotgan kompaniyadagi sheriklikda yaqin qarindoshingiz bilan o'zaro munosabatlaringizni aniq ko'rsating",
          "Davlat xizmatidagi vazifalaringizni bajarishda qarindoshlik aloqalari ta'sir qilmasligini ta'minlash uchun choralar taklif eting",
          "Qarindoshlaringiz bilan bog'liq qarorlar qabul qilishda o'zingizni chetga olish tartibini o'rganing"
        ],
        "legal_basis": [
          "O'zbekiston Respublikasi Adliya vazirligi tomonidan 2024-yil 5-noyabrda ro'yxatdan o'tkazilgan ro'yxat raqami 3569",
          "O'zbekiston Respublikasining 05.06.2024 yildagi O'RQ-931-son qonuni",
          "O'zbekiston Respublikasining 'Korrupsiyaga qarshi kurashish to'g'risida'gi qonuni"
        ]
      },
      "Yo'q": {
        "title": "✅ Manfaatlar to'qnashuvi yo'q",
        "steps": ["Sizning holatda manfaatlar to'qnashuvi aniqlanmadi"],
        "analysis": "Rejalashtirilayotgan kompaniyada sherikligingiz manfaatlar to'qnashuviga olib kelmasligini ko'rsatmoqda. Siz sherik bo'lishni rejalashtirayotgan kompaniya davlat bilan aloqada emas, sheriklik davlat xizmatiga bog'liq emas va yaqin qarindoshlaringiz bu kompaniyada ishlamaydi yoki sherik emas.",
        "recommendations": [
          "Sheriklikni boshlashdan oldin tegishli ruxsatnomalarni olishni unutmang",
          "Vaziyatingizda o'zgarishlar bo'lsa, qaytadan tekshiruv o'tkazing",
          "Har yilgi daromad va mulk deklaratsiyasida bu sheriklikni ko'rsating",
          "Kompaniyaning kelajakda davlat bilan aloqalari paydo bo'lsa, bu haqda xabar bering"
        ],
        "legal_basis": [
          "O'zbekiston Respublikasi Adliya vazirligi tomonidan 2024-yil 5-noyabrda ro'yxatdan o'tkazilgan ro'yxat raqami 3569",
          "O'zbekiston Respublikasining 05.06.2024 yildagi O'RQ-931-son qonuni",
          "O'zbekiston Respublikasining 'Korrupsiyaga qarshi kurashish to'g'risida'gi qonuni"
        ]
      }
    }
  },
  
  "2": {
    "question": "Kelajakda davlat xizmatchisi sifatida, qanday holatni tekshirmoqchisiz?",
    "options": ["Hozir faoliyat olib boryapman", "Kompaniya sherigiman", "Faoliyat olib borishni rejalashtiryapman"],
    "next": {
      "Hozir faoliyat olib boryapman": "2.1",
      "Kompaniya sherigiman": "2.2",
      "Faoliyat olib borishni rejalashtiryapman": "2.3"
    }
  },
  
  "2.1": {
    "question": "Faoliyatingiz qaysi sektorda?",
    "options": ["Xususiy sektorda", "Davlat sektorda"],
    "next": {
      "Xususiy sektorda": "2.1.1",
      "Davlat sektorda": {
        "title": "⚠️ Qonuniy maslahat kerak",
        "steps": ["Davlat xizmati boshqarmasiga murojaat qiling"],
        "analysis": "Kelajakda davlat xizmatchisi bo'lishni rejalashtirayotganingiz va hozir davlat sektorida faoliyat olib borayotganingiz murakkab huquqiy vaziyatni keltirib chiqarishi mumkin. Bunday holatlar maxsus tartibga solinadi va har bir holat alohida ko'rib chiqilishi kerak.",
        "recommendations": [
          "15 kun ichida Davlat xizmati boshqarmasiga yozma ravishda murojaat qiling",
          "Manfaatlar to'qnashuvi ehtimolini aniqlash uchun tegishli hujjatlarni tayyorlang",
          "Kelajakdagi davlat xizmatiga o'tish va hozirgi faoliyatingizni davom ettirish imkoniyatlarini o'rganing"
        ],
        "legal_basis": [
          "O'zbekiston Respublikasi Adliya vazirligi tomonidan 2024-yil 5-noyabrda ro'yxatdan o'tkazilgan ro'yxat raqami 3569",
          "O'zbekiston Respublikasining 05.06.2024 yildagi O'RQ-931-son qonuni",
          "O'zbekiston Respublikasining 'Korrupsiyaga qarshi kurashish to'g'risida'gi qonuni"
        ]
      }
    }
  },
  
  "2.1.1": {
    "question": "Xususiy sektordagi faoliyatingiz turi?",
    "options": ["Xususiy kompaniyada", "Shaxsiy sifatda"],
    "next": {
      "Xususiy kompaniyada": "2.1.1.1",
      "Shaxsiy sifatda": "2.1.1.2"
    }
  },
  
  "2.1.1.1": {
    "question": "Faoliyatingiz kelajakdagi xizmatga bog'liq bo'ladimi?",
    "options": ["Ha", "Yo'q"],
    "next": {
      "Ha": {
        "title": "⚠️ Potentsial manfaatlar to'qnashuvi",
        "steps": ["Axloq komissiyasidan maslahat olish kerak"],
        "analysis": "Hozirgi xususiy kompaniyadagi faoliyatingiz kelajakdagi davlat xizmatiga bog'liq bo'lsa, bu manfaatlar to'qnashuviga olib kelishi mumkin. Hozirgi faoliyatingizdagi manfaatlar kelajakdagi davlat xizmatidagi qarorlaringizga ta'sir etishi mumkin.",
        "recommendations": [
          "30 kun ichida axloq komissiyasiga yozma ravishda murojaat qiling",
          "Hozirgi faoliyatingiz va kelajakdagi davlat xizmatidagi vazifalaringiz o'rtasidagi bog'liqlikni aniq ko'rsating",
          "Davlat xizmatiga kirishdan oldin manfaatlar to'qnashuvini oldini olish uchun aniq chora-tadbirlarni taklif eting",
          "Davlat xizmatida oldingi faoliyatingiz bilan bog'liq qarorlar qabul qilishda o'zingizni chetga olish tartibini o'rganing"
        ],
        "legal_basis": [
          "O'zbekiston Respublikasi Adliya vazirligi tomonidan 2024-yil 5-noyabrda ro'yxatdan o'tkazilgan ro'yxat raqami 3569",
          "O'zbekiston Respublikasining 05.06.2024 yildagi O'RQ-931-son qonuni",
          "O'zbekiston Respublikasining 'Korrupsiyaga qarshi kurashish to'g'risida'gi qonuni"
        ]
      },
      "Yo'q": "2.1.1.1.2"
    }
  },
  
  "2.1.1.1.2": {
    "question": "Kompaniya davlat bilan aloqadami?",
    "options": ["Ha", "Yo'q"],
    "next": {
      "Ha": {
        "title": "⚠️ Potentsial manfaatlar to'qnashuvi",
        "steps": ["Tekshiruv kerak (Prokuratura yoki antikorrupsiya bo'linmasi)"],
        "analysis": "Davlat bilan aloqada bo'lgan kompaniyada hozir ishlashingiz va kelajakda davlat xizmatiga kirishingiz manfaatlar to'qnashuviga olib kelishi mumkin. Hozirgi kompaniyadagi aloqalaringiz kelajakdagi davlat xizmatidagi qarorlaringizga ta'sir etishi mumkin.",
        "recommendations": [
          "30 kun ichida Prokuratura yoki antikorrupsiya bo'linmasiga murojaat qiling",
          "Hozirgi kompaniyangizdagi faoliyatingiz va kelajakdagi davlat xizmati o'rtasida aniq chegaralar o'rnating",
          "Kompaniyaning davlat bilan aloqalari to'g'risida ma'lumot to'plang",
          "Davlat xizmatiga kirishdan oldin tegishli tekshiruv o'tkazilishini ta'minlang"
        ],
        "legal_basis": [
          "O'zbekiston Respublikasi Adliya vazirligi tomonidan 2024-yil 5-noyabrda ro'yxatdan o'tkazilgan ro'yxat raqami 3569",
          "O'zbekiston Respublikasining 05.06.2024 yildagi O'RQ-931-son qonuni",
          "O'zbekiston Respublikasining 'Korrupsiyaga qarshi kurashish to'g'risida'gi qonuni"
        ]
      },
      "Yo'q": "2.1.1.1.3"
    }
  },
  
  "2.1.1.1.3": {
    "question": "Yaqin qarindoshingiz ushbu kompaniyada ishlaydimi yoki sherikmi?",
    "options": ["Ha", "Yo'q"],
    "next": {
      "Ha": {
        "title": "⚠️ Potentsial manfaatlar to'qnashuvi",
        "steps": ["Korrupsiyaga qarshi kurashish agentligidan maslahat olish kerak"],
        "analysis": "Yaqin qarindoshingiz ishlayotgan yoki sherik bo'lgan kompaniyada ishlashingiz va kelajakda davlat xizmatiga kirishingiz manfaatlar to'qnashuviga olib kelishi mumkin. Bu holat oilaviy aloqalar orqali kelajakdagi davlat xizmatidagi qarorlaringizga ta'sir etishi mumkin.",
        "recommendations": [
          "30 kun ichida Korrupsiyaga qarshi kurashish agentligiga yozma ravishda murojaat qiling",
          "Kompaniyadagi yaqin qarindoshingiz bilan o'zaro munosabatlaringizni aniq ko'rsating",
          "Kelajakdagi davlat xizmatida qarindoshlik aloqalari ta'sir qilmasligini ta'minlash uchun choralar taklif eting",
          "Davlat xizmatida qarindoshlaringiz bilan bog'liq qarorlar qabul qilishda o'zingizni chetga olish tartibini o'rganing"
        ],
        "legal_basis": [
          "O'zbekiston Respublikasi Adliya vazirligi tomonidan 2024-yil 5-noyabrda ro'yxatdan o'tkazilgan ro'yxat raqami 3569",
          "O'zbekiston Respublikasining 05.06.2024 yildagi O'RQ-931-son qonuni",
          "O'zbekiston Respublikasining 'Korrupsiyaga qarshi kurashish to'g'risida'gi qonuni"
        ]
      },
      "Yo'q": {
        "title": "✅ Manfaatlar to'qnashuvi yo'q",
        "steps": ["Sizning holatda manfaatlar to'qnashuvi aniqlanmadi"],
        "analysis": "Hozirgi faoliyatingiz va kelajakdagi davlat xizmati o'rtasida manfaatlar to'qnashuviga olib keluvchi holatlar aniqlanmadi. Hozirgi xususiy kompaniyadagi faoliyatingiz kelajakdagi davlat xizmatiga bog'liq emas, kompaniya davlat bilan aloqada emas va yaqin qarindoshlaringiz bu kompaniyada ishlamaydi yoki sherik emas.",
        "recommendations": [
          "Davlat xizmatiga kirganingizdan so'ng qo'shimcha faoliyatni davom ettirish uchun ruxsatnoma olishni unutmang",
          "Vaziyatingizda o'zgarishlar bo'lsa, qaytadan tekshiruv o'tkazing",
          "Davlat xizmatiga kirganingizdan so'ng daromad va mulk deklaratsiyasida bu faoliyatni ko'rsating",
          "Davlat xizmati va qo'shimcha faoliyat o'rtasida aniq chegaralar saqlang"
        ],
        "legal_basis": [
          "O'zbekiston Respublikasi Adliya vazirligi tomonidan 2024-yil 5-noyabrda ro'yxatdan o'tkazilgan ro'yxat raqami 3569",
          "O'zbekiston Respublikasining 05.06.2024 yildagi O'RQ-931-son qonuni",
          "O'zbekiston Respublikasining 'Korrupsiyaga qarshi kurashish to'g'risida'gi qonuni"
        ]
      }
    }
  },
  
  "2.1.1.2": {
    "question": "Faoliyatingiz kelajakdagi xizmatga bog'liq bo'ladimi?",
    "options": ["Ha", "Yo'q"],
    "next": {
      "Ha": {
        "title": "⚠️ Potentsial manfaatlar to'qnashuvi",
        "steps": ["Axloq komissiyasidan maslahat olish kerak"],
        "analysis": "Hozirgi shaxsiy tadbirkorlik faoliyatingiz kelajakdagi davlat xizmatiga bog'liq bo'lsa, bu manfaatlar to'qnashuviga olib kelishi mumkin. Shaxsiy manfaatlaringiz kelajakdagi davlat xizmatidagi qarorlaringizga ta'sir etishi mumkin.",
        "recommendations": [
          "30 kun ichida axloq komissiyasiga yozma ravishda murojaat qiling",
          "Hozirgi tadbirkorlik faoliyatingiz va kelajakdagi davlat xizmatidagi vazifalaringiz o'rtasidagi bog'liqlikni aniq ko'rsating",
          "Davlat xizmatiga kirishdan oldin manfaatlar to'qnashuvini oldini olish uchun aniq chora-tadbirlarni taklif eting",
          "Davlat xizmatida oldingi faoliyatingiz bilan bog'liq qarorlar qabul qilishda o'zingizni chetga olish tartibini o'rganing"
        ],
        "legal_basis": [
          "O'zbekiston Respublikasi Adliya vazirligi tomonidan 2024-yil 5-noyabrda ro'yxatdan o'tkazilgan ro'yxat raqami 3569",
          "O'zbekiston Respublikasining 05.06.2024 yildagi O'RQ-931-son qonuni",
          "O'zbekiston Respublikasining 'Korrupsiyaga qarshi kurashish to'g'risida'gi qonuni"
        ]
      },
      "Yo'q": "2.1.1.2.2"
    }
  },
  
  "2.1.1.2.2": {
    "question": "Faoliyatingiz davlat bilan aloqadami?",
    "options": ["Ha", "Yo'q"],
    "next": {
      "Ha": {
        "title": "⚠️ Potentsial manfaatlar to'qnashuvi",
        "steps": ["Tekshiruv kerak (Prokuratura yoki antikorrupsiya bo'linmasi)"],
        "analysis": "Davlat bilan aloqada bo'lgan shaxsiy tadbirkorlik faoliyatingiz va kelajakda davlat xizmatiga kirishingiz manfaatlar to'qnashuviga olib kelishi mumkin. Hozirgi faoliyatingizdagi davlat bilan aloqalaringiz kelajakdagi davlat xizmatidagi qarorlaringizga ta'sir etishi mumkin.",
        "recommendations": [
          "30 kun ichida Prokuratura yoki antikorrupsiya bo'linmasiga murojaat qiling",
          "Hozirgi tadbirkorlik faoliyatingiz va kelajakdagi davlat xizmati o'rtasida aniq chegaralar o'rnating",
          "Tadbirkorlik faoliyatingizning davlat bilan aloqalari to'g'risida ma'lumot to'plang",
          "Davlat xizmatiga kirishdan oldin tegishli tekshiruv o'tkazilishini ta'minlang"
        ],
        "legal_basis": [
          "O'zbekiston Respublikasi Adliya vazirligi tomonidan 2024-yil 5-noyabrda ro'yxatdan o'tkazilgan ro'yxat raqami 3569",
          "O'zbekiston Respublikasining 05.06.2024 yildagi O'RQ-931-son qonuni",
          "O'zbekiston Respublikasining 'Korrupsiyaga qarshi kurashish to'g'risida'gi qonuni"
        ]
      },
      "Yo'q": "2.1.1.2.3"
    }
  },
  
  "2.1.1.2.3": {
    "question": "Yaqin qarindoshingiz ushbu faoliyat bilan bog'liqmi?",
    "options": ["Ha", "Yo'q"],
    "next": {
      "Ha": {
        "title": "⚠️ Potentsial manfaatlar to'qnashuvi",
        "steps": ["Korrupsiyaga qarshi kurashish agentligidan maslahat olish kerak"],
        "analysis": "Yaqin qarindoshingiz bog'liq bo'lgan shaxsiy tadbirkorlik faoliyatingiz va kelajakda davlat xizmatiga kirishingiz manfaatlar to'qnashuviga olib kelishi mumkin. Bu holat oilaviy aloqalar orqali kelajakdagi davlat xizmatidagi qarorlaringizga ta'sir etishi mumkin.",
        "recommendations": [
          "30 kun ichida Korrupsiyaga qarshi kurashish agentligiga yozma ravishda murojaat qiling",
          "Tadbirkorlikda yaqin qarindoshingiz bilan o'zaro munosabatlaringizni aniq ko'rsating",
          "Kelajakdagi davlat xizmatida qarindoshlik aloqalari ta'sir qilmasligini ta'minlash uchun choralar taklif eting",
          "Davlat xizmatida qarindoshlaringiz bilan bog'liq qarorlar qabul qilishda o'zingizni chetga olish tartibini o'rganing"
        ],
        "legal_basis": [
          "O'zbekiston Respublikasi Adliya vazirligi tomonidan 2024-yil 5-noyabrda ro'yxatdan o'tkazilgan ro'yxat raqami 3569",
          "O'zbekiston Respublikasining 05.06.2024 yildagi O'RQ-931-son qonuni",
          "O'zbekiston Respublikasining 'Korrupsiyaga qarshi kurashish to'g'risida'gi qonuni"
        ]
      },
      "Yo'q": {
        "title": "✅ Manfaatlar to'qnashuvi yo'q",
        "steps": ["Sizning holatda manfaatlar to'qnashuvi aniqlanmadi"],
        "analysis": "Hozirgi shaxsiy tadbirkorlik faoliyatingiz va kelajakdagi davlat xizmati o'rtasida manfaatlar to'qnashuviga olib keluvchi holatlar aniqlanmadi. Tadbirkorlik faoliyatingiz kelajakdagi davlat xizmatiga bog'liq emas, davlat bilan aloqada emas va yaqin qarindoshlaringiz bu faoliyat bilan bog'liq emas.",
        "recommendations": [
          "Davlat xizmatiga kirganingizdan so'ng tadbirkorlik faoliyatini davom ettirish uchun ruxsatnoma olishni unutmang",
          "Vaziyatingizda o'zgarishlar bo'lsa, qaytadan tekshiruv o'tkazing",
          "Davlat xizmatiga kirganingizdan so'ng daromad va mulk deklaratsiyasida bu faoliyatni ko'rsating",
          "Davlat xizmati va tadbirkorlik faoliyati o'rtasida aniq chegaralar saqlang"
        ],
        "legal_basis": [
          "O'zbekiston Respublikasi Adliya vazirligi tomonidan 2024-yil 5-noyabrda ro'yxatdan o'tkazilgan ro'yxat raqami 3569",
          "O'zbekiston Respublikasining 05.06.2024 yildagi O'RQ-931-son qonuni",
          "O'zbekiston Respublikasining 'Korrupsiyaga qarshi kurashish to'g'risida'gi qonuni"
        ]
      }
    }
  },
  
  "2.2": {
    "question": "Kompaniya davlat bilan aloqadami?",
    "options": ["Ha", "Yo'q"],
    "next": {
      "Ha": {
        "title": "⚠️ Potentsial manfaatlar to'qnashuvi",
        "steps": ["Tekshiruv kerak (Prokuratura yoki antikorrupsiya bo'linmasi)"],
        "analysis": "Davlat bilan aloqada bo'lgan kompaniyada sherik bo'lishingiz va kelajakda davlat xizmatiga kirishingiz manfaatlar to'qnashuviga olib kelishi mumkin. Sheriklikdagi manfaatlaringiz kelajakdagi davlat xizmatidagi qarorlaringizga ta'sir etishi mumkin.",
        "recommendations": [
          "30 kun ichida Prokuratura yoki antikorrupsiya bo'linmasiga murojaat qiling",
          "Hozirgi kompaniyadagi sherikligingiz va kelajakdagi davlat xizmati o'rtasida aniq chegaralar o'rnating",
          "Kompaniyaning davlat bilan aloqalari to'g'risida ma'lumot to'plang",
          "Davlat xizmatiga kirishdan oldin tegishli tekshiruv o'tkazilishini ta'minlang"
        ],
        "legal_basis": [
          "O'zbekiston Respublikasi Adliya vazirligi tomonidan 2024-yil 5-noyabrda ro'yxatdan o'tkazilgan ro'yxat raqami 3569",
          "O'zbekiston Respublikasining 05.06.2024 yildagi O'RQ-931-son qonuni",
          "O'zbekiston Respublikasining 'Korrupsiyaga qarshi kurashish to'g'risida'gi qonuni"
        ]
      },
      "Yo'q": "2.2.2"
    }
  },
  
  "2.2.2": {
    "question": "Sherikligingiz kelajakdagi xizmatga bog'liq bo'ladimi?",
    "options": ["Ha", "Yo'q"],
    "next": {
      "Ha": {
        "title": "⚠️ Potentsial manfaatlar to'qnashuvi",
        "steps": ["Axloq komissiyasidan maslahat olish kerak"],
        "analysis": "Hozirgi kompaniyadagi sherikligingiz kelajakdagi davlat xizmatiga bog'liq bo'lsa, bu manfaatlar to'qnashuviga olib kelishi mumkin. Kompaniyadagi manfaatlaringiz kelajakdagi davlat xizmatidagi qarorlaringizga ta'sir etishi mumkin.",
        "recommendations": [
          "30 kun ichida axloq komissiyasiga yozma ravishda murojaat qiling",
          "Hozirgi kompaniyadagi sherikligingiz va kelajakdagi davlat xizmatidagi vazifalaringiz o'rtasidagi bog'liqlikni aniq ko'rsating",
          "Davlat xizmatiga kirishdan oldin manfaatlar to'qnashuvini oldini olish uchun aniq chora-tadbirlarni taklif eting",
          "Davlat xizmatida sheriklikdagi kompaniya bilan bog'liq qarorlar qabul qilishda o'zingizni chetga olish tartibini o'rganing"
        ],
        "legal_basis": [
          "O'zbekiston Respublikasi Adliya vazirligi tomonidan 2024-yil 5-noyabrda ro'yxatdan o'tkazilgan ro'yxat raqami 3569",
          "O'zbekiston Respublikasining 05.06.2024 yildagi O'RQ-931-son qonuni",
          "O'zbekiston Respublikasining 'Korrupsiyaga qarshi kurashish to'g'risida'gi qonuni"
        ]
      },
      "Yo'q": "2.2.3"
    }
  },
  
  "2.2.3": {
    "question": "Yaqin qarindoshingiz ushbu kompaniyada ishlaydimi yoki sherikmi?",
    "options": ["Ha", "Yo'q"],
    "next": {
      "Ha": {
        "title": "⚠️ Potentsial manfaatlar to'qnashuvi",
        "steps": ["Korrupsiyaga qarshi kurashish agentligidan maslahat olish kerak"],
        "analysis": "Yaqin qarindoshingiz ishlayotgan yoki sherik bo'lgan kompaniyada sherikligingiz va kelajakda davlat xizmatiga kirishingiz manfaatlar to'qnashuviga olib kelishi mumkin. Bu holat oilaviy aloqalar orqali kelajakdagi davlat xizmatidagi qarorlaringizga ta'sir etishi mumkin.",
        "recommendations": [
          "30 kun ichida Korrupsiyaga qarshi kurashish agentligiga yozma ravishda murojaat qiling",
          "Kompaniyadagi yaqin qarindoshingiz bilan sheriklikdagi o'zaro munosabatlaringizni aniq ko'rsating",
          "Kelajakdagi davlat xizmatida qarindoshlik aloqalari ta'sir qilmasligini ta'minlash uchun choralar taklif eting",
          "Davlat xizmatida qarindoshlaringiz bilan bog'liq qarorlar qabul qilishda o'zingizni chetga olish tartibini o'rganing"
        ],
        "legal_basis": [
          "O'zbekiston Respublikasi Adliya vazirligi tomonidan 2024-yil 5-noyabrda ro'yxatdan o'tkazilgan ro'yxat raqami 3569",
          "O'zbekiston Respublikasining 05.06.2024 yildagi O'RQ-931-son qonuni",
          "O'zbekiston Respublikasining 'Korrupsiyaga qarshi kurashish to'g'risida'gi qonuni"
        ]
      },
      "Yo'q": {
        "title": "✅ Manfaatlar to'qnashuvi yo'q",
        "steps": ["Sizning holatda manfaatlar to'qnashuvi aniqlanmadi"],
        "analysis": "Hozirgi kompaniyadagi sherikligingiz va kelajakdagi davlat xizmati o'rtasida manfaatlar to'qnashuviga olib keluvchi holatlar aniqlanmadi. Sherik bo'lgan kompaniyangiz davlat bilan aloqada emas, sheriklik kelajakdagi davlat xizmatiga bog'liq emas va yaqin qarindoshlaringiz bu kompaniyada ishlamaydi yoki sherik emas.",
        "recommendations": [
          "Davlat xizmatiga kirganingizdan so'ng sheriklikni davom ettirish uchun ruxsatnoma olishni unutmang",
          "Vaziyatingizda o'zgarishlar bo'lsa, qaytadan tekshiruv o'tkazing",
          "Davlat xizmatiga kirganingizdan so'ng daromad va mulk deklaratsiyasida bu sheriklikni ko'rsating",
          "Davlat xizmati va sheriklik o'rtasida aniq chegaralar saqlang"
        ],
        "legal_basis": [
          "O'zbekiston Respublikasi Adliya vazirligi tomonidan 2024-yil 5-noyabrda ro'yxatdan o'tkazilgan ro'yxat raqami 3569",
          "O'zbekiston Respublikasining 05.06.2024 yildagi O'RQ-931-son qonuni",
          "O'zbekiston Respublikasining 'Korrupsiyaga qarshi kurashish to'g'risida'gi qonuni"
        ]
      }
    }
  },
  
  "2.3": {
    "question": "Faoliyatingiz qaysi sektorda bo'ladi?",
    "options": ["Xususiy sektorda", "Davlat sektorda"],
    "next": {
      "Xususiy sektorda": "2.3.1",
      "Davlat sektorda": {
        "title": "⚠️ Qonuniy maslahat kerak",
        "steps": ["Davlat xizmati boshqarmasiga murojaat qiling"],
        "analysis": "Kelajakda davlat xizmatchisi bo'lishni rejalashtirayotganingiz va davlat sektorida faoliyat olib borishni rejalashtirayotganingiz murakkab huquqiy vaziyatni keltirib chiqarishi mumkin. Bunday holatlar maxsus tartibga solinadi va har bir holat alohida ko'rib chiqilishi kerak.",
        "recommendations": [
          "15 kun ichida Davlat xizmati boshqarmasiga yozma ravishda murojaat qiling",
          "Manfaatlar to'qnashuvi ehtimolini aniqlash uchun tegishli hujjatlarni tayyorlang",
          "Kelajakdagi davlat xizmatiga o'tish va rejalashtirilayotgan faoliyatingizni boshlash imkoniyatlarini o'rganing"
        ],
        "legal_basis": [
          "O'zbekiston Respublikasi Adliya vazirligi tomonidan 2024-yil 5-noyabrda ro'yxatdan o'tkazilgan ro'yxat raqami 3569",
          "O'zbekiston Respublikasining 05.06.2024 yildagi O'RQ-931-son qonuni",
          "O'zbekiston Respublikasining 'Korrupsiyaga qarshi kurashish to'g'risida'gi qonuni"
        ]
      }
    }
  },
  
  "2.3.1": {
    "question": "Xususiy sektordagi faoliyatingiz turi qanday bo'ladi?",
    "options": ["Xususiy kompaniyada", "Shaxsiy sifatda"],
    "next": {
      "Xususiy kompaniyada": "2.3.1.1",
      "Shaxsiy sifatda": "2.3.1.2"
    }
  },
  
  "2.3.1.1": {
    "question": "Faoliyatingiz kelajakdagi xizmatga bog'liq bo'ladimi?",
    "options": ["Ha", "Yo'q"],
    "next": {
      "Ha": {
        "title": "⚠️ Potentsial manfaatlar to'qnashuvi",
        "steps": ["Axloq komissiyasidan maslahat olish kerak"],
        "analysis": "Rejalashtirilayotgan xususiy kompaniyadagi faoliyatingiz kelajakdagi davlat xizmatiga bog'liq bo'lsa, bu manfaatlar to'qnashuviga olib kelishi mumkin. Rejalashtirilayotgan faoliyatingizdagi manfaatlar kelajakdagi davlat xizmatidagi qarorlaringizga ta'sir etishi mumkin.",
        "recommendations": [
          "30 kun ichida axloq komissiyasiga yozma ravishda murojaat qiling",
          "Rejalashtirilayotgan faoliyatingiz va kelajakdagi davlat xizmatidagi vazifalaringiz o'rtasidagi bog'liqlikni aniq ko'rsating",
          "Davlat xizmatiga kirishdan oldin manfaatlar to'qnashuvini oldini olish uchun aniq chora-tadbirlarni taklif eting",
          "Davlat xizmatida oldingi faoliyatingiz bilan bog'liq qarorlar qabul qilishda o'zingizni chetga olish tartibini o'rganing"
        ],
        "legal_basis": [
          "O'zbekiston Respublikasi Adliya vazirligi tomonidan 2024-yil 5-noyabrda ro'yxatdan o'tkazilgan ro'yxat raqami 3569",
          "O'zbekiston Respublikasining 05.06.2024 yildagi O'RQ-931-son qonuni",
          "O'zbekiston Respublikasining 'Korrupsiyaga qarshi kurashish to'g'risida'gi qonuni"
        ]
      },
      "Yo'q": "2.3.1.1.2"
    }
  },
  
  "2.3.1.1.2": {
    "question": "Kompaniya davlat bilan aloqada bo'ladimi?",
    "options": ["Ha", "Yo'q"],
    "next": {
      "Ha": {
        "title": "⚠️ Potentsial manfaatlar to'qnashuvi",
        "steps": ["Tekshiruv kerak (Prokuratura yoki antikorrupsiya bo'linmasi)"],
        "analysis": "Davlat bilan aloqada bo'lgan kompaniyada faoliyat yuritishni rejalashtirish va kelajakda davlat xizmatiga kirish manfaatlar to'qnashuviga olib kelishi mumkin. Rejalashtirilayotgan faoliyatingizdagi davlat bilan aloqalaringiz kelajakdagi davlat xizmatidagi qarorlaringizga ta'sir etishi mumkin.",
        "recommendations": [
          "30 kun ichida Prokuratura yoki antikorrupsiya bo'linmasiga murojaat qiling",
          "Rejalashtirilayotgan faoliyatingiz va kelajakdagi davlat xizmati o'rtasida aniq chegaralar o'rnating",
          "Kompaniyaning davlat bilan aloqalari to'g'risida ma'lumot to'plang",
          "Davlat xizmatiga kirishdan oldin tegishli tekshiruv o'tkazilishini ta'minlang"
        ],
        "legal_basis": [
          "O'zbekiston Respublikasi Adliya vazirligi tomonidan 2024-yil 5-noyabrda ro'yxatdan o'tkazilgan ro'yxat raqami 3569",
          "O'zbekiston Respublikasining 05.06.2024 yildagi O'RQ-931-son qonuni",
          "O'zbekiston Respublikasining 'Korrupsiyaga qarshi kurashish to'g'risida'gi qonuni"
        ]
      },
      "Yo'q": "2.3.1.1.3"
    }
  },
  
  "2.3.1.1.3": {
    "question": "Yaqin qarindoshingiz ushbu kompaniyada ishlaydimi yoki sherik bo'ladimi?",
    "options": ["Ha", "Yo'q"],
    "next": {
      "Ha": {
        "title": "⚠️ Potentsial manfaatlar to'qnashuvi",
        "steps": ["Korrupsiyaga qarshi kurashish agentligidan maslahat olish kerak"],
        "analysis": "Yaqin qarindoshingiz ishlayotgan yoki sherik bo'lgan kompaniyada faoliyat yuritishni rejalashtirish va kelajakda davlat xizmatiga kirish manfaatlar to'qnashuviga olib kelishi mumkin. Bu holat oilaviy aloqalar orqali kelajakdagi davlat xizmatidagi qarorlaringizga ta'sir etishi mumkin.",
        "recommendations": [
          "30 kun ichida Korrupsiyaga qarshi kurashish agentligiga yozma ravishda murojaat qiling",
          "Rejalashtirilayotgan faoliyatingizda yaqin qarindoshingiz bilan o'zaro munosabatlaringizni aniq ko'rsating",
          "Kelajakdagi davlat xizmatida qarindoshlik aloqalari ta'sir qilmasligini ta'minlash uchun choralar taklif eting",
          "Davlat xizmatida qarindoshlaringiz bilan bog'liq qarorlar qabul qilishda o'zingizni chetga olish tartibini o'rganing"
        ],
        "legal_basis": [
          "O'zbekiston Respublikasi Adliya vazirligi tomonidan 2024-yil 5-noyabrda ro'yxatdan o'tkazilgan ro'yxat raqami 3569",
          "O'zbekiston Respublikasining 05.06.2024 yildagi O'RQ-931-son qonuni",
          "O'zbekiston Respublikasining 'Korrupsiyaga qarshi kurashish to'g'risida'gi qonuni"
        ]
      },
      "Yo'q": {
        "title": "✅ Manfaatlar to'qnashuvi yo'q",
        "steps": ["Sizning holatda manfaatlar to'qnashuvi aniqlanmadi"],
        "analysis": "Rejalashtirilayotgan xususiy kompaniyadagi faoliyatingiz va kelajakdagi davlat xizmati o'rtasida manfaatlar to'qnashuviga olib keluvchi holatlar aniqlanmadi. Rejalashtirilayotgan faoliyatingiz kelajakdagi davlat xizmatiga bog'liq emas, kompaniya davlat bilan aloqada emas va yaqin qarindoshlaringiz bu kompaniyada ishlamaydi yoki sherik emas.",
        "recommendations": [
          "Davlat xizmatiga kirganingizdan so'ng qo'shimcha faoliyatni boshlash uchun ruxsatnoma olishni unutmang",
          "Vaziyatingizda o'zgarishlar bo'lsa, qaytadan tekshiruv o'tkazing",
          "Davlat xizmatiga kirganingizdan so'ng daromad va mulk deklaratsiyasida bu faoliyatni ko'rsating",
          "Davlat xizmati va qo'shimcha faoliyat o'rtasida aniq chegaralar saqlang"
        ],
        "legal_basis": [
          "O'zbekiston Respublikasi Adliya vazirligi tomonidan 2024-yil 5-noyabrda ro'yxatdan o'tkazilgan ro'yxat raqami 3569",
          "O'zbekiston Respublikasining 05.06.2024 yildagi O'RQ-931-son qonuni",
          "O'zbekiston Respublikasining 'Korrupsiyaga qarshi kurashish to'g'risida'gi qonuni"
        ]
      }
    }
  },
  
  "2.3.1.2": {
    "question": "Faoliyatingiz kelajakdagi xizmatga bog'liq bo'ladimi?",
    "options": ["Ha", "Yo'q"],
    "next": {
      "Ha": {
        "title": "⚠️ Potentsial manfaatlar to'qnashuvi",
        "steps": ["Axloq komissiyasidan maslahat olish kerak"],
        "analysis": "Rejalashtirilayotgan shaxsiy tadbirkorlik faoliyatingiz kelajakdagi davlat xizmatiga bog'liq bo'lsa, bu manfaatlar to'qnashuviga olib kelishi mumkin. Rejalashtirilayotgan faoliyatingizdagi manfaatlar kelajakdagi davlat xizmatidagi qarorlaringizga ta'sir etishi mumkin.",
        "recommendations": [
          "30 kun ichida axloq komissiyasiga yozma ravishda murojaat qiling",
          "Rejalashtirilayotgan tadbirkorlik faoliyatingiz va kelajakdagi davlat xizmatidagi vazifalaringiz o'rtasidagi bog'liqlikni aniq ko'rsating",
          "Davlat xizmatiga kirishdan oldin manfaatlar to'qnashuvini oldini olish uchun aniq chora-tadbirlarni taklif eting",
          "Davlat xizmatida oldingi faoliyatingiz bilan bog'liq qarorlar qabul qilishda o'zingizni chetga olish tartibini o'rganing"
        ],
        "legal_basis": [
          "O'zbekiston Respublikasi Adliya vazirligi tomonidan 2024-yil 5-noyabrda ro'yxatdan o'tkazilgan ro'yxat raqami 3569",
          "O'zbekiston Respublikasining 05.06.2024 yildagi O'RQ-931-son qonuni",
          "O'zbekiston Respublikasining 'Korrupsiyaga qarshi kurashish to'g'risida'gi qonuni"
        ]
      },
      "Yo'q": "2.3.1.2.2"
    }
  },
  
  "2.3.1.2.2": {
    "question": "Faoliyatingiz davlat bilan aloqada bo'ladimi?",
    "options": ["Ha", "Yo'q"],
    "next": {
      "Ha": {
        "title": "⚠️ Potentsial manfaatlar to'qnashuvi",
        "steps": ["Tekshiruv kerak (Prokuratura yoki antikorrupsiya bo'linmasi)"],
        "analysis": "Davlat bilan aloqada bo'lgan tadbirkorlik faoliyatini yuritishni rejalashtirish va kelajakda davlat xizmatiga kirish manfaatlar to'qnashuviga olib kelishi mumkin. Rejalashtirilayotgan faoliyatingizdagi davlat bilan aloqalaringiz kelajakdagi davlat xizmatidagi qarorlaringizga ta'sir etishi mumkin.",
        "recommendations": [
          "30 kun ichida Prokuratura yoki antikorrupsiya bo'linmasiga murojaat qiling",
          "Rejalashtirilayotgan tadbirkorlik faoliyatingiz va kelajakdagi davlat xizmati o'rtasida aniq chegaralar o'rnating",
          "Tadbirkorlik faoliyatingizning davlat bilan aloqalari to'g'risida ma'lumot to'plang",
          "Davlat xizmatiga kirishdan oldin tegishli tekshiruv o'tkazilishini ta'minlang"
        ],
        "legal_basis": [
          "O'zbekiston Respublikasi Adliya vazirligi tomonidan 2024-yil 5-noyabrda ro'yxatdan o'tkazilgan ro'yxat raqami 3569",
          "O'zbekiston Respublikasining 05.06.2024 yildagi O'RQ-931-son qonuni",
          "O'zbekiston Respublikasining 'Korrupsiyaga qarshi kurashish to'g'risida'gi qonuni"
        ]
      },
      "Yo'q": "2.3.1.2.3"
    }
  },
  
  "2.3.1.2.3": {
    "question": "Yaqin qarindoshingiz ushbu faoliyat bilan bog'liq bo'ladimi?",
    "options": ["Ha", "Yo'q"],
    "next": {
      "Ha": {
        "title": "⚠️ Potentsial manfaatlar to'qnashuvi",
        "steps": ["Korrupsiyaga qarshi kurashish agentligidan maslahat olish kerak"],
        "analysis": "Yaqin qarindoshingiz bog'liq bo'lgan tadbirkorlik faoliyatini yuritishni rejalashtirish va kelajakda davlat xizmatiga kirish manfaatlar to'qnashuviga olib kelishi mumkin. Bu holat oilaviy aloqalar orqali kelajakdagi davlat xizmatidagi qarorlaringizga ta'sir etishi mumkin.",
        "recommendations": [
          "30 kun ichida Korrupsiyaga qarshi kurashish agentligiga yozma ravishda murojaat qiling",
          "Rejalashtirilayotgan tadbirkorlikda yaqin qarindoshingiz bilan o'zaro munosabatlaringizni aniq ko'rsating",
          "Kelajakdagi davlat xizmatida qarindoshlik aloqalari ta'sir qilmasligini ta'minlash uchun choralar taklif eting",
          "Davlat xizmatida qarindoshlaringiz bilan bog'liq qarorlar qabul qilishda o'zingizni chetga olish tartibini o'rganing"
        ],
        "legal_basis": [
          "O'zbekiston Respublikasi Adliya vazirligi tomonidan 2024-yil 5-noyabrda ro'yxatdan o'tkazilgan ro'yxat raqami 3569",
          "O'zbekiston Respublikasining 05.06.2024 yildagi O'RQ-931-son qonuni",
          "O'zbekiston Respublikasining 'Korrupsiyaga qarshi kurashish to'g'risida'gi qonuni"
        ]
      },
      "Yo'q": {
        "title": "✅ Manfaatlar to'qnashuvi yo'q",
        "steps": ["Sizning holatda manfaatlar to'qnashuvi aniqlanmadi"],
        "analysis": "Rejalashtirilayotgan shaxsiy tadbirkorlik faoliyatingiz va kelajakdagi davlat xizmati o'rtasida manfaatlar to'qnashuviga olib keluvchi holatlar aniqlanmadi. Rejalashtirilayotgan faoliyatingiz kelajakdagi davlat xizmatiga bog'liq emas, davlat bilan aloqada emas va yaqin qarindoshlaringiz bu faoliyat bilan bog'liq emas.",
        "recommendations": [
          "Davlat xizmatiga kirganingizdan so'ng tadbirkorlik faoliyatini boshlash uchun ruxsatnoma olishni unutmang",
          "Vaziyatingizda o'zgarishlar bo'lsa, qaytadan tekshiruv o'tkazing",
          "Davlat xizmatiga kirganingizdan so'ng daromad va mulk deklaratsiyasida bu faoliyatni ko'rsating",
          "Davlat xizmati va tadbirkorlik faoliyati o'rtasida aniq chegaralar saqlang"
        ],
        "legal_basis": [
          "O'zbekiston Respublikasi Adliya vazirligi tomonidan 2024-yil 5-noyabrda ro'yxatdan o'tkazilgan ro'yxat raqami 3569",
          "O'zbekiston Respublikasining 05.06.2024 yildagi O'RQ-931-son qonuni",
          "O'zbekiston Respublikasining 'Korrupsiyaga qarshi kurashish to'g'risida'gi qonuni"
        ]
      }
    }
  },
  
  "3": {
    "question": "Oldin davlat xizmatchisi sifatida, qanday holatni tekshirmoqchisiz?",
    "options": ["Hozir faoliyat olib boryapman", "Kompaniya sherigiman", "Faoliyat olib borishni rejalashtiryapman"],
    "next": {
      "Hozir faoliyat olib boryapman": "3.1",
      "Kompaniya sherigiman": "3.2",
      "Faoliyat olib borishni rejalashtiryapman": "3.3"
    }
  },
  
  "3.1": {
    "question": "Faoliyatingiz qaysi sektorda?",
    "options": ["Xususiy sektorda", "Davlat sektorda"],
    "next": {
      "Xususiy sektorda": "3.1.1",
      "Davlat sektorda": {
        "title": "⚠️ Qonuniy maslahat kerak",
        "steps": ["Davlat xizmati boshqarmasiga murojaat qiling"],
        "analysis": "Oldin davlat xizmatchisi bo'lib, hozir davlat sektorida faoliyat olib borish murakkab huquqiy vaziyatni keltirib chiqarishi mumkin. Bunday holatlar maxsus tartibga solinadi va har bir holat alohida ko'rib chiqilishi kerak.",
        "recommendations": [
          "15 kun ichida Davlat xizmati boshqarmasiga yozma ravishda murojaat qiling",
          "Manfaatlar to'qnashuvi ehtimolini aniqlash uchun tegishli hujjatlarni tayyorlang",
          "Oldingi davlat xizmatingiz va hozirgi faoliyatingiz o'rtasidagi bog'liqlikni aniq ko'rsating"
        ],
        "legal_basis": [
          "O'zbekiston Respublikasi Adliya vazirligi tomonidan 2024-yil 5-noyabrda ro'yxatdan o'tkazilgan ro'yxat raqami 3569",
          "O'zbekiston Respublikasining 05.06.2024 yildagi O'RQ-931-son qonuni",
          "O'zbekiston Respublikasining 'Korrupsiyaga qarshi kurashish to'g'risida'gi qonuni"
        ]
      }
    }
  },
  
  "3.1.1": {
    "question": "Xususiy sektordagi faoliyatingiz turi?",
    "options": ["Xususiy kompaniyada", "Shaxsiy sifatda"],
    "next": {
      "Xususiy kompaniyada": "3.1.1.1",
      "Shaxsiy sifatda": "3.1.1.2"
    }
  },
  
  "3.1.1.1": {
    "question": "Faoliyatingiz \"sovutish davri\" (2 yil) muddatlariga rioya qiladimi?",
    "options": ["Ha", "Yo'q"],
    "next": {
      "Ha": "3.1.1.1.2",
      "Yo'q": {
        "title": "⚠️ Potentsial qonunbuzarlik",
        "steps": ["Korrupsiyaga qarshi kurashish agentligiga murojaat qiling"],
        "analysis": "Davlat xizmatidan keyin 'sovutish davri' (2 yil) mobaynida oldingi xizmat vazifalaringizga bog'liq bo'lgan xususiy faoliyat bilan shug'ullanish qonun bilan cheklangan. Bu manfaatlar to'qnashuviga olib kelishi mumkin va potentsial qonunbuzarlik hisoblanishi mumkin.",
        "recommendations": [
          "30 kun ichida Korrupsiyaga qarshi kurashish agentligiga murojaat qiling",
          "Faoliyatni to'xtatish yoki vaqtincha to'xtatib turish masalasini ko'rib chiqing",
          "Sovutish davri muhlatini o'tib bo'lishini kutish imkoniyatlarini o'rganing",
          "Faoliyatni qonuniy ravishda davom ettirish uchun zarur chora-tadbirlarni aniqlash"
        ],
        "legal_basis": [
          "O'zbekiston Respublikasi Adliya vazirligi tomonidan 2024-yil 5-noyabrda ro'yxatdan o'tkazilgan ro'yxat raqami 3569",
          "O'zbekiston Respublikasining 05.06.2024 yildagi O'RQ-931-son qonuni",
          "O'zbekiston Respublikasining 'Korrupsiyaga qarshi kurashish to'g'risida'gi qonuni"
        ]
      }
    }
  },
  
  "3.1.1.1.2": {
    "question": "Faoliyatingiz oldingi xizmatga bog'liqmi?",
    "options": ["Ha", "Yo'q"],
    "next": {
      "Ha": {
        "title": "⚠️ Potentsial manfaatlar to'qnashuvi",
        "steps": ["Axloq komissiyasidan maslahat olish kerak"],
        "analysis": "Oldingi davlat xizmatiga bog'liq bo'lgan faoliyat bilan shug'ullanish, hatto sovutish davri o'tgan bo'lsa ham, potentsial manfaatlar to'qnashuviga olib kelishi mumkin. Oldingi xizmatdagi aloqalaringiz va tajribangiz hozirgi faoliyatingizga qonunga zid ta'sir ko'rsatishi mumkin.",
        "recommendations": [
          "30 kun ichida axloq komissiyasiga yozma ravishda murojaat qiling",
          "Oldingi davlat xizmatidagi funksiyalaringiz va hozirgi faoliyatingiz o'rtasidagi bog'liqlikni aniq ko'rsating",
          "Manfaatlar to'qnashuvini oldini olish uchun aniq chora-tadbirlarni taklif eting",
          "Davlat bilan aloqadagi shaxslar bilan munosabatda tegishli masofani saqlang"
        ],
        "legal_basis": [
          "O'zbekiston Respublikasi Adliya vazirligi tomonidan 2024-yil 5-noyabrda ro'yxatdan o'tkazilgan ro'yxat raqami 3569",
          "O'zbekiston Respublikasining 05.06.2024 yildagi O'RQ-931-son qonuni",
          "O'zbekiston Respublikasining 'Korrupsiyaga qarshi kurashish to'g'risida'gi qonuni"
        ]
      },
      "Yo'q": "3.1.1.1.3"
    }
  },
  
  "3.1.1.1.3": {
    "question": "Kompaniya davlat bilan aloqadami?",
    "options": ["Ha", "Yo'q"],
    "next": {
      "Ha": {
        "title": "⚠️ Potentsial manfaatlar to'qnashuvi",
        "steps": ["Tekshiruv kerak (Prokuratura yoki antikorrupsiya bo'linmasi)"],
        "analysis": "Davlat bilan aloqada bo'lgan kompaniyada ishlash, oldin davlat xizmatchisi bo'lgan shaxs uchun manfaatlar to'qnashuviga olib kelishi mumkin. Davlat bilan aloqada bo'lgan kompaniyada ishlash oldingidagi davlat xizmatida orttirgan aloqalaringizdan noqonuniy foydalanish imkoniyatini yaratishi mumkin.",
        "recommendations": [
          "30 kun ichida Prokuratura yoki antikorrupsiya bo'linmasiga murojaat qiling",
          "Kompaniyadagi faoliyatingiz va oldingi davlat xizmati o'rtasida aniq chegaralar o'rnating",
          "Kompaniyaning davlat bilan aloqalari to'g'risida to'liq ma'lumot to'plang va taqdim eting",
          "Tegishli tekshiruv o'tkazilishini ta'minlang"
        ],
        "legal_basis": [
          "O'zbekiston Respublikasi Adliya vazirligi tomonidan 2024-yil 5-noyabrda ro'yxatdan o'tkazilgan ro'yxat raqami 3569",
          "O'zbekiston Respublikasining 05.06.2024 yildagi O'RQ-931-son qonuni",
          "O'zbekiston Respublikasining 'Korrupsiyaga qarshi kurashish to'g'risida'gi qonuni"
        ]
      },
      "Yo'q": "3.1.1.1.4"
    }
  },

  
  "3.1.1.1.4": {
    "question": "Yaqin qarindoshingiz ushbu kompaniyada ishlaydimi yoki sherikmi?",
    "options": ["Ha", "Yo'q"],
    "next": {
      "Ha": {
        "title": "⚠️ Potentsial manfaatlar to'qnashuvi",
        "steps": ["Korrupsiyaga qarshi kurashish agentligidan maslahat olish kerak"],
        "analysis": "Yaqin qarindoshingiz ishlayotgan yoki sherik bo'lgan kompaniyada ishlash, oldin davlat xizmatchisi bo'lgan shaxs uchun manfaatlar to'qnashuviga olib kelishi mumkin. Bu holat oilaviy aloqalar orqali oldingidagi davlat xizmatida orttirgan aloqalaringizdan noqonuniy foydalanish imkoniyatini yaratishi mumkin.",
        "recommendations": [
          "30 kun ichida Korrupsiyaga qarshi kurashish agentligiga yozma ravishda murojaat qiling",
          "Kompaniyadagi yaqin qarindoshingiz bilan o'zaro munosabatlaringizni aniq ko'rsating",
          "Qarindoshlik aloqalari orqali davlat xizmatida orttirgan aloqalaringizdan foydalanmaslikni ta'minlash uchun choralar taklif eting",
          "Ushbu vaziyatda qo'shimcha huquqiy maslahat olishni ko'rib chiqing"
        ],
        "legal_basis": [
          "O'zbekiston Respublikasi Adliya vazirligi tomonidan 2024-yil 5-noyabrda ro'yxatdan o'tkazilgan ro'yxat raqami 3569",
          "O'zbekiston Respublikasining 05.06.2024 yildagi O'RQ-931-son qonuni",
          "O'zbekiston Respublikasining 'Korrupsiyaga qarshi kurashish to'g'risida'gi qonuni"
        ]
      },
      "Yo'q": {
        "title": "✅ Manfaatlar to'qnashuvi yo'q",
        "steps": ["Sizning holatda manfaatlar to'qnashuvi aniqlanmadi"],
        "analysis": "Hozirgi xususiy kompaniyadagi faoliyatingiz va oldingi davlat xizmati o'rtasida manfaatlar to'qnashuviga olib keluvchi holatlar aniqlanmadi. Faoliyatingiz sovutish davri muddatlariga rioya qiladi, oldingi xizmatga bog'liq emas, kompaniya davlat bilan aloqada emas va yaqin qarindoshlaringiz bu kompaniyada ishlamaydi yoki sherik emas.",
        "recommendations": [
          "Vaziyatingizda o'zgarishlar bo'lsa, qaytadan tekshiruv o'tkazing",
          "Oldingi davlat xizmatingiz bilan bog'liq aloqalardan foydalanmaslikni ta'minlang",
          "Kompaniyaning kelajakda davlat bilan aloqalari paydo bo'lsa, tegishli idoralarni xabardor qiling",
          "Davlat xizmati ma'muriyati bilan aloqada bo'lishda shaffoflikni saqlang"
        ],
        "legal_basis": [
          "O'zbekiston Respublikasi Adliya vazirligi tomonidan 2024-yil 5-noyabrda ro'yxatdan o'tkazilgan ro'yxat raqami 3569",
          "O'zbekiston Respublikasining 05.06.2024 yildagi O'RQ-931-son qonuni",
          "O'zbekiston Respublikasining 'Korrupsiyaga qarshi kurashish to'g'risida'gi qonuni"
        ]
      }
    }
  },
  
  "3.1.1.2": {
    "question": "Faoliyatingiz \"sovutish davri\" (2 yil) muddatlariga rioya qiladimi?",
    "options": ["Ha", "Yo'q"],
    "next": {
      "Ha": "3.1.1.2.2",
      "Yo'q": {
        "title": "⚠️ Potentsial qonunbuzarlik",
        "steps": ["Korrupsiyaga qarshi kurashish agentligiga murojaat qiling"],
        "analysis": "Davlat xizmatidan keyin 'sovutish davri' (2 yil) mobaynida oldingi xizmat vazifalaringizga bog'liq bo'lgan shaxsiy tadbirkorlik faoliyati bilan shug'ullanish qonun bilan cheklangan. Bu manfaatlar to'qnashuviga olib kelishi mumkin va potentsial qonunbuzarlik hisoblanishi mumkin.",
        "recommendations": [
          "30 kun ichida Korrupsiyaga qarshi kurashish agentligiga murojaat qiling",
          "Tadbirkorlik faoliyatini to'xtatish yoki vaqtincha to'xtatib turish masalasini ko'rib chiqing",
          "Sovutish davri muhlatini o'tib bo'lishini kutish imkoniyatlarini o'rganing",
          "Faoliyatni qonuniy ravishda davom ettirish uchun zarur chora-tadbirlarni aniqlash"
        ],
        "legal_basis": [
          "O'zbekiston Respublikasi Adliya vazirligi tomonidan 2024-yil 5-noyabrda ro'yxatdan o'tkazilgan ro'yxat raqami 3569",
          "O'zbekiston Respublikasining 05.06.2024 yildagi O'RQ-931-son qonuni",
          "O'zbekiston Respublikasining 'Korrupsiyaga qarshi kurashish to'g'risida'gi qonuni"
        ]
      }
    }
  },
  
  "3.1.1.2.2": {
    "question": "Faoliyatingiz oldingi xizmatga bog'liqmi?",
    "options": ["Ha", "Yo'q"],
    "next": {
      "Ha": {
        "title": "⚠️ Potentsial manfaatlar to'qnashuvi",
        "steps": ["Axloq komissiyasidan maslahat olish kerak"],
        "analysis": "Oldingi davlat xizmatiga bog'liq bo'lgan tadbirkorlik faoliyati bilan shug'ullanish, hatto sovutish davri o'tgan bo'lsa ham, potentsial manfaatlar to'qnashuviga olib kelishi mumkin. Oldingi xizmatdagi aloqalaringiz va tajribangiz hozirgi faoliyatingizga qonunga zid ta'sir ko'rsatishi mumkin.",
        "recommendations": [
          "30 kun ichida axloq komissiyasiga yozma ravishda murojaat qiling",
          "Oldingi davlat xizmatidagi funksiyalaringiz va hozirgi tadbirkorlik faoliyatingiz o'rtasidagi bog'liqlikni aniq ko'rsating",
          "Manfaatlar to'qnashuvini oldini olish uchun aniq chora-tadbirlarni taklif eting",
          "Davlat bilan aloqadagi shaxslar bilan munosabatda tegishli masofani saqlang"
        ],
        "legal_basis": [
          "O'zbekiston Respublikasi Adliya vazirligi tomonidan 2024-yil 5-noyabrda ro'yxatdan o'tkazilgan ro'yxat raqami 3569",
          "O'zbekiston Respublikasining 05.06.2024 yildagi O'RQ-931-son qonuni",
          "O'zbekiston Respublikasining 'Korrupsiyaga qarshi kurashish to'g'risida'gi qonuni"
        ]
      },
      "Yo'q": "3.1.1.2.3"
    }
  },
  
  "3.1.1.2.3": {
    "question": "Faoliyatingiz davlat bilan aloqadami?",
    "options": ["Ha", "Yo'q"],
    "next": {
      "Ha": {
        "title": "⚠️ Potentsial manfaatlar to'qnashuvi",
        "steps": ["Tekshiruv kerak (Prokuratura yoki antikorrupsiya bo'linmasi)"],
        "analysis": "Davlat bilan aloqada bo'lgan tadbirkorlik faoliyati bilan shug'ullanish, oldin davlat xizmatchisi bo'lgan shaxs uchun manfaatlar to'qnashuviga olib kelishi mumkin. Davlat bilan aloqada bo'lgan tadbirkorlik oldingidagi davlat xizmatida orttirgan aloqalaringizdan noqonuniy foydalanish imkoniyatini yaratishi mumkin.",
        "recommendations": [
          "30 kun ichida Prokuratura yoki antikorrupsiya bo'linmasiga murojaat qiling",
          "Tadbirkorlik faoliyatingiz va oldingi davlat xizmati o'rtasida aniq chegaralar o'rnating",
          "Tadbirkorlik faoliyatingizning davlat bilan aloqalari to'g'risida to'liq ma'lumot to'plang va taqdim eting",
          "Tegishli tekshiruv o'tkazilishini ta'minlang"
        ],
        "legal_basis": [
          "O'zbekiston Respublikasi Adliya vazirligi tomonidan 2024-yil 5-noyabrda ro'yxatdan o'tkazilgan ro'yxat raqami 3569",
          "O'zbekiston Respublikasining 05.06.2024 yildagi O'RQ-931-son qonuni",
          "O'zbekiston Respublikasining 'Korrupsiyaga qarshi kurashish to'g'risida'gi qonuni"
        ]
      },
      "Yo'q": "3.1.1.2.4"
    }
  },
  
  "3.1.1.2.4": {
    "question": "Yaqin qarindoshingiz ushbu faoliyat bilan bog'liqmi?",
    "options": ["Ha", "Yo'q"],
    "next": {
      "Ha": {
        "title": "⚠️ Potentsial manfaatlar to'qnashuvi",
        "steps": ["Korrupsiyaga qarshi kurashish agentligidan maslahat olish kerak"],
        "analysis": "Yaqin qarindoshingiz bog'liq bo'lgan tadbirkorlik faoliyati bilan shug'ullanish, oldin davlat xizmatchisi bo'lgan shaxs uchun manfaatlar to'qnashuviga olib kelishi mumkin. Bu holat oilaviy aloqalar orqali oldingidagi davlat xizmatida orttirgan aloqalaringizdan noqonuniy foydalanish imkoniyatini yaratishi mumkin.",
        "recommendations": [
          "30 kun ichida Korrupsiyaga qarshi kurashish agentligiga yozma ravishda murojaat qiling",
          "Tadbirkorlikda yaqin qarindoshingiz bilan o'zaro munosabatlaringizni aniq ko'rsating",
          "Qarindoshlik aloqalari orqali davlat xizmatida orttirgan aloqalaringizdan foydalanmaslikni ta'minlash uchun choralar taklif eting",
          "Ushbu vaziyatda qo'shimcha huquqiy maslahat olishni ko'rib chiqing"
        ],
        "legal_basis": [
          "O'zbekiston Respublikasi Adliya vazirligi tomonidan 2024-yil 5-noyabrda ro'yxatdan o'tkazilgan ro'yxat raqami 3569",
          "O'zbekiston Respublikasining 05.06.2024 yildagi O'RQ-931-son qonuni",
          "O'zbekiston Respublikasining 'Korrupsiyaga qarshi kurashish to'g'risida'gi qonuni"
        ]
      },
      "Yo'q": {
        "title": "✅ Manfaatlar to'qnashuvi yo'q",
        "steps": ["Sizning holatda manfaatlar to'qnashuvi aniqlanmadi"],
        "analysis": "Hozirgi shaxsiy tadbirkorlik faoliyatingiz va oldingi davlat xizmati o'rtasida manfaatlar to'qnashuviga olib keluvchi holatlar aniqlanmadi. Faoliyatingiz sovutish davri muddatlariga rioya qiladi, oldingi xizmatga bog'liq emas, davlat bilan aloqada emas va yaqin qarindoshlaringiz bu faoliyat bilan bog'liq emas.",
        "recommendations": [
          "Vaziyatingizda o'zgarishlar bo'lsa, qaytadan tekshiruv o'tkazing",
          "Oldingi davlat xizmatingiz bilan bog'liq aloqalardan foydalanmaslikni ta'minlang",
          "Tadbirkorlik faoliyatingizning kelajakda davlat bilan aloqalari paydo bo'lsa, tegishli idoralarni xabardor qiling",
          "Davlat xizmati ma'muriyati bilan aloqada bo'lishda shaffoflikni saqlang"
        ],
        "legal_basis": [
          "O'zbekiston Respublikasi Adliya vazirligi tomonidan 2024-yil 5-noyabrda ro'yxatdan o'tkazilgan ro'yxat raqami 3569",
          "O'zbekiston Respublikasining 05.06.2024 yildagi O'RQ-931-son qonuni",
          "O'zbekiston Respublikasining 'Korrupsiyaga qarshi kurashish to'g'risida'gi qonuni"
        ]
      }
    }
  },
  
  "3.2": {
    "question": "Faoliyatingiz \"sovutish davri\" (2 yil) muddatlariga rioya qiladimi?",
    "options": ["Ha", "Yo'q"],
    "next": {
      "Ha": "3.2.2",
      "Yo'q": {
        "title": "⚠️ Potentsial qonunbuzarlik",
        "steps": ["Korrupsiyaga qarshi kurashish agentligiga murojaat qiling"],
        "analysis": "Davlat xizmatidan keyin 'sovutish davri' (2 yil) mobaynida oldingi xizmat vazifalaringizga bog'liq bo'lgan kompaniyada sherik bo'lish qonun bilan cheklangan. Bu manfaatlar to'qnashuviga olib kelishi mumkin va potentsial qonunbuzarlik hisoblanishi mumkin.",
        "recommendations": [
          "30 kun ichida Korrupsiyaga qarshi kurashish agentligiga murojaat qiling",
          "Kompaniyadagi sheriklikni to'xtatish yoki vaqtincha to'xtatib turish masalasini ko'rib chiqing",
          "Sovutish davri muhlatini o'tib bo'lishini kutish imkoniyatlarini o'rganing",
          "Sheriklikni qonuniy ravishda davom ettirish uchun zarur chora-tadbirlarni aniqlash"
        ],
        "legal_basis": [
          "O'zbekiston Respublikasi Adliya vazirligi tomonidan 2024-yil 5-noyabrda ro'yxatdan o'tkazilgan ro'yxat raqami 3569",
          "O'zbekiston Respublikasining 05.06.2024 yildagi O'RQ-931-son qonuni",
          "O'zbekiston Respublikasining 'Korrupsiyaga qarshi kurashish to'g'risida'gi qonuni"
        ]
      }
    }
  },
  
  "3.2.2": {
    "question": "Kompaniya davlat bilan aloqadami?",
    "options": ["Ha", "Yo'q"],
    "next": {
      "Ha": {
        "title": "⚠️ Potentsial manfaatlar to'qnashuvi",
        "steps": ["Tekshiruv kerak (Prokuratura yoki antikorrupsiya bo'linmasi)"],
        "analysis": "Davlat bilan aloqada bo'lgan kompaniyada sherik bo'lish, oldin davlat xizmatchisi bo'lgan shaxs uchun manfaatlar to'qnashuviga olib kelishi mumkin. Davlat bilan aloqada bo'lgan kompaniyada sheriklik oldingidagi davlat xizmatida orttirgan aloqalaringizdan noqonuniy foydalanish imkoniyatini yaratishi mumkin.",
        "recommendations": [
          "30 kun ichida Prokuratura yoki antikorrupsiya bo'linmasiga murojaat qiling",
          "Kompaniyadagi sherikligingiz va oldingi davlat xizmati o'rtasida aniq chegaralar o'rnating",
          "Kompaniyaning davlat bilan aloqalari to'g'risida to'liq ma'lumot to'plang va taqdim eting",
          "Tegishli tekshiruv o'tkazilishini ta'minlang"
        ],
        "legal_basis": [
          "O'zbekiston Respublikasi Adliya vazirligi tomonidan 2024-yil 5-noyabrda ro'yxatdan o'tkazilgan ro'yxat raqami 3569",
          "O'zbekiston Respublikasining 05.06.2024 yildagi O'RQ-931-son qonuni",
          "O'zbekiston Respublikasining 'Korrupsiyaga qarshi kurashish to'g'risida'gi qonuni"
        ]
      },
      "Yo'q": "3.2.3"
    }
  },
  
  "3.2.3": {
    "question": "Sherikligingiz oldingi xizmatga bog'liqmi?",
    "options": ["Ha", "Yo'q"],
    "next": {
      "Ha": {
        "title": "⚠️ Potentsial manfaatlar to'qnashuvi",
        "steps": ["Axloq komissiyasidan maslahat olish kerak"],
        "analysis": "Oldingi davlat xizmatiga bog'liq bo'lgan kompaniyada sherik bo'lish, hatto sovutish davri o'tgan bo'lsa ham, potentsial manfaatlar to'qnashuviga olib kelishi mumkin. Oldingi xizmatdagi aloqalaringiz va tajribangiz hozirgi sheriklikda qonunga zid ta'sir ko'rsatishi mumkin.",
        "recommendations": [
          "30 kun ichida axloq komissiyasiga yozma ravishda murojaat qiling",
          "Oldingi davlat xizmatidagi funksiyalaringiz va hozirgi kompaniyadagi sherikligingiz o'rtasidagi bog'liqlikni aniq ko'rsating",
          "Manfaatlar to'qnashuvini oldini olish uchun aniq chora-tadbirlarni taklif eting",
          "Davlat bilan aloqadagi shaxslar bilan munosabatda tegishli masofani saqlang"
        ],
        "legal_basis": [
          "O'zbekiston Respublikasi Adliya vazirligi tomonidan 2024-yil 5-noyabrda ro'yxatdan o'tkazilgan ro'yxat raqami 3569",
          "O'zbekiston Respublikasining 05.06.2024 yildagi O'RQ-931-son qonuni",
          "O'zbekiston Respublikasining 'Korrupsiyaga qarshi kurashish to'g'risida'gi qonuni"
        ]
      },
      "Yo'q": "3.2.4"
    }
  },
  
  "3.2.4": {
    "question": "Yaqin qarindoshingiz ushbu kompaniyada ishlaydimi yoki sherikmi?",
    "options": ["Ha", "Yo'q"],
    "next": {
      "Ha": {
        "title": "⚠️ Potentsial manfaatlar to'qnashuvi",
        "steps": ["Korrupsiyaga qarshi kurashish agentligidan maslahat olish kerak"],
        "analysis": "Yaqin qarindoshingiz ishlayotgan yoki sherik bo'lgan kompaniyada sherik bo'lish, oldin davlat xizmatchisi bo'lgan shaxs uchun manfaatlar to'qnashuviga olib kelishi mumkin. Bu holat oilaviy aloqalar orqali oldingidagi davlat xizmatida orttirgan aloqalaringizdan noqonuniy foydalanish imkoniyatini yaratishi mumkin.",
        "recommendations": [
          "30 kun ichida Korrupsiyaga qarshi kurashish agentligiga yozma ravishda murojaat qiling",
          "Kompaniyadagi yaqin qarindoshingiz bilan sheriklikdagi o'zaro munosabatlaringizni aniq ko'rsating",
          "Qarindoshlik aloqalari orqali davlat xizmatida orttirgan aloqalaringizdan foydalanmaslikni ta'minlash uchun choralar taklif eting",
          "Ushbu vaziyatda qo'shimcha huquqiy maslahat olishni ko'rib chiqing"
        ],
        "legal_basis": [
          "O'zbekiston Respublikasi Adliya vazirligi tomonidan 2024-yil 5-noyabrda ro'yxatdan o'tkazilgan ro'yxat raqami 3569",
          "O'zbekiston Respublikasining 05.06.2024 yildagi O'RQ-931-son qonuni",
          "O'zbekiston Respublikasining 'Korrupsiyaga qarshi kurashish to'g'risida'gi qonuni"
        ]
      },
      "Yo'q": {
        "title": "✅ Manfaatlar to'qnashuvi yo'q",
        "steps": ["Sizning holatda manfaatlar to'qnashuvi aniqlanmadi"],
        "analysis": "Hozirgi kompaniyadagi sherikligingiz va oldingi davlat xizmati o'rtasida manfaatlar to'qnashuviga olib keluvchi holatlar aniqlanmadi. Sherikligingiz sovutish davri muddatlariga rioya qiladi, oldingi xizmatga bog'liq emas, kompaniya davlat bilan aloqada emas va yaqin qarindoshlaringiz bu kompaniyada ishlamaydi yoki sherik emas.",
        "recommendations": [
          "Vaziyatingizda o'zgarishlar bo'lsa, qaytadan tekshiruv o'tkazing",
          "Oldingi davlat xizmatingiz bilan bog'liq aloqalardan foydalanmaslikni ta'minlang",
          "Kompaniyaning kelajakda davlat bilan aloqalari paydo bo'lsa, tegishli idoralarni xabardor qiling",
          "Davlat xizmati ma'muriyati bilan aloqada bo'lishda shaffoflikni saqlang"
        ],
        "legal_basis": [
          "O'zbekiston Respublikasi Adliya vazirligi tomonidan 2024-yil 5-noyabrda ro'yxatdan o'tkazilgan ro'yxat raqami 3569",
          "O'zbekiston Respublikasining 05.06.2024 yildagi O'RQ-931-son qonuni",
          "O'zbekiston Respublikasining 'Korrupsiyaga qarshi kurashish to'g'risida'gi qonuni"
        ]
      }
    }
  },
  
  "3.3": {
    "question": "Faoliyatingiz qaysi sektorda bo'ladi?",
    "options": ["Xususiy sektorda", "Davlat sektorda"],
    "next": {
      "Xususiy sektorda": "3.3.1",
      "Davlat sektorda": {
        "title": "⚠️ Qonuniy maslahat kerak",
        "steps": ["Davlat xizmati boshqarmasiga murojaat qiling"],
        "analysis": "Oldin davlat xizmatchisi bo'lib, davlat sektorida faoliyat olib borishni rejalashtirish murakkab huquqiy vaziyatni keltirib chiqarishi mumkin. Bunday holatlar maxsus tartibga solinadi va har bir holat alohida ko'rib chiqilishi kerak.",
        "recommendations": [
          "15 kun ichida Davlat xizmati boshqarmasiga yozma ravishda murojaat qiling",
          "Manfaatlar to'qnashuvi ehtimolini aniqlash uchun tegishli hujjatlarni tayyorlang",
          "Oldingi davlat xizmatingiz va rejalashtirilayotgan faoliyatingiz o'rtasidagi bog'liqlikni aniq ko'rsating"
        ],
        "legal_basis": [
          "O'zbekiston Respublikasi Adliya vazirligi tomonidan 2024-yil 5-noyabrda ro'yxatdan o'tkazilgan ro'yxat raqami 3569",
          "O'zbekiston Respublikasining 05.06.2024 yildagi O'RQ-931-son qonuni",
          "O'zbekiston Respublikasining 'Korrupsiyaga qarshi kurashish to'g'risida'gi qonuni"
        ]
      }
    }
  },
  
  "3.3.1": {
    "question": "Xususiy sektordagi faoliyatingiz turi qanday bo'ladi?",
    "options": ["Xususiy kompaniyada", "Shaxsiy sifatda"],
    "next": {
      "Xususiy kompaniyada": "3.3.1.1",
      "Shaxsiy sifatda": "3.3.1.2"
    }
  },
  
  "3.3.1.1": {
    "question": "Faoliyatingiz \"sovutish davri\" (2 yil) muddatlariga rioya qiladimi?",
    "options": ["Ha", "Yo'q"],
    "next": {
      "Ha": "3.3.1.1.2",
      "Yo'q": {
        "title": "⚠️ Potentsial qonunbuzarlik",
        "steps": ["Korrupsiyaga qarshi kurashish agentligiga murojaat qiling"],
        "analysis": "Davlat xizmatidan keyin 'sovutish davri' (2 yil) mobaynida oldingi xizmat vazifalaringizga bog'liq bo'lgan xususiy kompaniyada faoliyat olib borishni rejalashtirish qonun bilan cheklangan. Bu manfaatlar to'qnashuviga olib kelishi mumkin va potentsial qonunbuzarlik hisoblanishi mumkin.",
        "recommendations": [
          "30 kun ichida Korrupsiyaga qarshi kurashish agentligiga murojaat qiling",
          "Faoliyatni boshlashdan voz kechish yoki kechiktirish masalasini ko'rib chiqing",
          "Sovutish davri muhlatini o'tib bo'lishini kutish imkoniyatlarini o'rganing",
          "Faoliyatni qonuniy ravishda boshlash uchun zarur chora-tadbirlarni aniqlash"
        ],
        "legal_basis": [
          "O'zbekiston Respublikasi Adliya vazirligi tomonidan 2024-yil 5-noyabrda ro'yxatdan o'tkazilgan ro'yxat raqami 3569",
          "O'zbekiston Respublikasining 05.06.2024 yildagi O'RQ-931-son qonuni",
          "O'zbekiston Respublikasining 'Korrupsiyaga qarshi kurashish to'g'risida'gi qonuni"
        ]
      }
    }
  },
  
  "3.3.1.1.2": {
    "question": "Faoliyatingiz oldingi xizmatga bog'liq bo'ladimi?",
    "options": ["Ha", "Yo'q"],
    "next": {
      "Ha": {
        "title": "⚠️ Potentsial manfaatlar to'qnashuvi",
        "steps": ["Axloq komissiyasidan maslahat olish kerak"],
        "analysis": "Oldingi davlat xizmatiga bog'liq bo'lgan xususiy kompaniyada faoliyat yuritishni rejalashtirish, hatto sovutish davri o'tgan bo'lsa ham, potentsial manfaatlar to'qnashuviga olib kelishi mumkin. Oldingi xizmatdagi aloqalaringiz va tajribangiz rejalashtirilayotgan faoliyatingizga qonunga zid ta'sir ko'rsatishi mumkin.",
        "recommendations": [
          "30 kun ichida axloq komissiyasiga yozma ravishda murojaat qiling",
          "Oldingi davlat xizmatidagi funksiyalaringiz va rejalashtirilayotgan faoliyatingiz o'rtasidagi bog'liqlikni aniq ko'rsating",
          "Manfaatlar to'qnashuvini oldini olish uchun aniq chora-tadbirlarni taklif eting",
          "Davlat bilan aloqadagi shaxslar bilan munosabatda tegishli masofani saqlash rejasini taqdim eting"
        ],
        "legal_basis": [
          "O'zbekiston Respublikasi Adliya vazirligi tomonidan 2024-yil 5-noyabrda ro'yxatdan o'tkazilgan ro'yxat raqami 3569",
          "O'zbekiston Respublikasining 05.06.2024 yildagi O'RQ-931-son qonuni",
          "O'zbekiston Respublikasining 'Korrupsiyaga qarshi kurashish to'g'risida'gi qonuni"
        ]
      },
      "Yo'q": "3.3.1.1.3"
    }
  },
  
  "3.3.1.1.3": {
    "question": "Kompaniya davlat bilan aloqada bo'ladimi?",
    "options": ["Ha", "Yo'q"],
    "next": {
      "Ha": {
        "title": "⚠️ Potentsial manfaatlar to'qnashuvi",
        "steps": ["Tekshiruv kerak (Prokuratura yoki antikorrupsiya bo'linmasi)"],
        "analysis": "Davlat bilan aloqada bo'lgan kompaniyada faoliyat yuritishni rejalashtirish, oldin davlat xizmatchisi bo'lgan shaxs uchun manfaatlar to'qnashuviga olib kelishi mumkin. Davlat bilan aloqada bo'lgan kompaniyada ishlash oldingidagi davlat xizmatida orttirgan aloqalaringizdan noqonuniy foydalanish imkoniyatini yaratishi mumkin.",
        "recommendations": [
          "30 kun ichida Prokuratura yoki antikorrupsiya bo'linmasiga murojaat qiling",
          "Rejalashtirilayotgan faoliyatingiz va oldingi davlat xizmati o'rtasida aniq chegaralar o'rnating",
          "Kompaniyaning davlat bilan aloqalari to'g'risida to'liq ma'lumot to'plang va taqdim eting",
          "Faoliyatni boshlashdan oldin tegishli tekshiruv o'tkazilishini ta'minlang"
        ],
        "legal_basis": [
          "O'zbekiston Respublikasi Adliya vazirligi tomonidan 2024-yil 5-noyabrda ro'yxatdan o'tkazilgan ro'yxat raqami 3569",
          "O'zbekiston Respublikasining 05.06.2024 yildagi O'RQ-931-son qonuni",
          "O'zbekiston Respublikasining 'Korrupsiyaga qarshi kurashish to'g'risida'gi qonuni"
        ]
      },
      "Yo'q": "3.3.1.1.4"
    }
  },
  
  "3.3.1.1.4": {
    "question": "Yaqin qarindoshingiz ushbu kompaniyada ishlaydimi yoki sherik bo'ladimi?",
    "options": ["Ha", "Yo'q"],
    "next": {
      "Ha": {
        "title": "⚠️ Potentsial manfaatlar to'qnashuvi",
        "steps": ["Korrupsiyaga qarshi kurashish agentligidan maslahat olish kerak"],
        "analysis": "Yaqin qarindoshingiz ishlayotgan yoki sherik bo'lgan kompaniyada faoliyat yuritishni rejalashtirish, oldin davlat xizmatchisi bo'lgan shaxs uchun manfaatlar to'qnashuviga olib kelishi mumkin. Bu holat oilaviy aloqalar orqali oldingidagi davlat xizmatida orttirgan aloqalaringizdan noqonuniy foydalanish imkoniyatini yaratishi mumkin.",
        "recommendations": [
          "30 kun ichida Korrupsiyaga qarshi kurashish agentligiga yozma ravishda murojaat qiling",
          "Rejalashtirilayotgan faoliyatingizda yaqin qarindoshingiz bilan o'zaro munosabatlaringizni aniq ko'rsating",
          "Qarindoshlik aloqalari orqali davlat xizmatida orttirgan aloqalaringizdan foydalanmaslikni ta'minlash uchun choralar taklif eting",
          "Ushbu vaziyatda qo'shimcha huquqiy maslahat olishni ko'rib chiqing"
        ],
        "legal_basis": [
          "O'zbekiston Respublikasi Adliya vazirligi tomonidan 2024-yil 5-noyabrda ro'yxatdan o'tkazilgan ro'yxat raqami 3569",
          "O'zbekiston Respublikasining 05.06.2024 yildagi O'RQ-931-son qonuni",
          "O'zbekiston Respublikasining 'Korrupsiyaga qarshi kurashish to'g'risida'gi qonuni"
        ]
      },
      "Yo'q": {
        "title": "✅ Manfaatlar to'qnashuvi yo'q",
        "steps": ["Sizning holatda manfaatlar to'qnashuvi aniqlanmadi"],
        "analysis": "Rejalashtirilayotgan xususiy kompaniyadagi faoliyatingiz va oldingi davlat xizmati o'rtasida manfaatlar to'qnashuviga olib keluvchi holatlar aniqlanmadi. Faoliyatingiz sovutish davri muddatlariga rioya qiladi, oldingi xizmatga bog'liq emas, kompaniya davlat bilan aloqada emas va yaqin qarindoshlaringiz bu kompaniyada ishlamaydi yoki sherik emas.",
        "recommendations": [
          "Vaziyatingizda o'zgarishlar bo'lsa, qaytadan tekshiruv o'tkazing",
          "Oldingi davlat xizmatingiz bilan bog'liq aloqalardan foydalanmaslikni ta'minlang",
          "Kompaniyaning kelajakda davlat bilan aloqalari paydo bo'lsa, tegishli idoralarni xabardor qiling",
          "Davlat xizmati ma'muriyati bilan aloqada bo'lishda shaffoflikni saqlang"
        ],
        "legal_basis": [
          "O'zbekiston Respublikasi Adliya vazirligi tomonidan 2024-yil 5-noyabrda ro'yxatdan o'tkazilgan ro'yxat raqami 3569",
          "O'zbekiston Respublikasining 05.06.2024 yildagi O'RQ-931-son qonuni",
          "O'zbekiston Respublikasining 'Korrupsiyaga qarshi kurashish to'g'risida'gi qonuni"
        ]
      }
    }
  },
  
  "3.3.1.2": {
    "question": "Faoliyatingiz \"sovutish davri\" (2 yil) muddatlariga rioya qiladimi?",
    "options": ["Ha", "Yo'q"],
    "next": {
      "Ha": "3.3.1.2.2",
      "Yo'q": {
        "title": "⚠️ Potentsial qonunbuzarlik",
        "steps": ["Korrupsiyaga qarshi kurashish agentligiga murojaat qiling"],
        "analysis": "Davlat xizmatidan keyin 'sovutish davri' (2 yil) mobaynida oldingi xizmat vazifalaringizga bog'liq bo'lgan shaxsiy tadbirkorlik faoliyatini rejalashtirish qonun bilan cheklangan. Bu manfaatlar to'qnashuviga olib kelishi mumkin va potentsial qonunbuzarlik hisoblanishi mumkin.",
        "recommendations": [
          "30 kun ichida Korrupsiyaga qarshi kurashish agentligiga murojaat qiling",
          "Tadbirkorlik faoliyatini boshlashdan voz kechish yoki kechiktirish masalasini ko'rib chiqing",
          "Sovutish davri muhlatini o'tib bo'lishini kutish imkoniyatlarini o'rganing",
          "Faoliyatni qonuniy ravishda boshlash uchun zarur chora-tadbirlarni aniqlash"
        ],
        "legal_basis": [
          "O'zbekiston Respublikasi Adliya vazirligi tomonidan 2024-yil 5-noyabrda ro'yxatdan o'tkazilgan ro'yxat raqami 3569",
          "O'zbekiston Respublikasining 05.06.2024 yildagi O'RQ-931-son qonuni",
          "O'zbekiston Respublikasining 'Korrupsiyaga qarshi kurashish to'g'risida'gi qonuni"
        ]
      }
    }
  },
  
  "3.3.1.2.2": {
    "question": "Faoliyatingiz oldingi xizmatga bog'liq bo'ladimi?",
    "options": ["Ha", "Yo'q"],
    "next": {
      "Ha": {
        "title": "⚠️ Potentsial manfaatlar to'qnashuvi",
        "steps": ["Axloq komissiyasidan maslahat olish kerak"],
        "analysis": "Oldingi davlat xizmatiga bog'liq bo'lgan shaxsiy tadbirkorlik faoliyatini rejalashtirish, hatto sovutish davri o'tgan bo'lsa ham, potentsial manfaatlar to'qnashuviga olib kelishi mumkin. Oldingi xizmatdagi aloqalaringiz va tajribangiz rejalashtirilayotgan tadbirkorlikka qonunga zid ta'sir ko'rsatishi mumkin.",
        "recommendations": [
          "30 kun ichida axloq komissiyasiga yozma ravishda murojaat qiling",
          "Oldingi davlat xizmatidagi funksiyalaringiz va rejalashtirilayotgan tadbirkorlik faoliyatingiz o'rtasidagi bog'liqlikni aniq ko'rsating",
          "Manfaatlar to'qnashuvini oldini olish uchun aniq chora-tadbirlarni taklif eting",
          "Davlat bilan aloqadagi shaxslar bilan munosabatda tegishli masofani saqlash rejasini taqdim eting"
        ],
        "legal_basis": [
          "O'zbekiston Respublikasi Adliya vazirligi tomonidan 2024-yil 5-noyabrda ro'yxatdan o'tkazilgan ro'yxat raqami 3569",
          "O'zbekiston Respublikasining 05.06.2024 yildagi O'RQ-931-son qonuni",
          "O'zbekiston Respublikasining 'Korrupsiyaga qarshi kurashish to'g'risida'gi qonuni"
        ]
      },
      "Yo'q": "3.3.1.2.3"
    }
  },
  
  "3.3.1.2.3": {
    "question": "Faoliyatingiz davlat bilan aloqada bo'ladimi?",
    "options": ["Ha", "Yo'q"],
    "next": {
      "Ha": {
        "title": "⚠️ Potentsial manfaatlar to'qnashuvi",
        "steps": ["Tekshiruv kerak (Prokuratura yoki antikorrupsiya bo'linmasi)"],
        "analysis": "Davlat bilan aloqada bo'lgan tadbirkorlik faoliyatini yuritishni rejalashtirish, oldin davlat xizmatchisi bo'lgan shaxs uchun manfaatlar to'qnashuviga olib kelishi mumkin. Davlat bilan aloqada bo'lgan tadbirkorlik oldingidagi davlat xizmatida orttirgan aloqalaringizdan noqonuniy foydalanish imkoniyatini yaratishi mumkin.",
        "recommendations": [
          "30 kun ichida Prokuratura yoki antikorrupsiya bo'linmasiga murojaat qiling",
          "Rejalashtirilayotgan tadbirkorlik faoliyatingiz va oldingi davlat xizmati o'rtasida aniq chegaralar o'rnating",
          "Tadbirkorlik faoliyatingizning davlat bilan aloqalari to'g'risida to'liq ma'lumot to'plang va taqdim eting",
          "Faoliyatni boshlashdan oldin tegishli tekshiruv o'tkazilishini ta'minlang"
        ],
        "legal_basis": [
          "O'zbekiston Respublikasi Adliya vazirligi tomonidan 2024-yil 5-noyabrda ro'yxatdan o'tkazilgan ro'yxat raqami 3569",
          "O'zbekiston Respublikasining 05.06.2024 yildagi O'RQ-931-son qonuni",
          "O'zbekiston Respublikasining 'Korrupsiyaga qarshi kurashish to'g'risida'gi qonuni"
        ]
      },
      "Yo'q": "3.3.1.2.4"
    }
  },
  
  "3.3.1.2.4": {
    "question": "Yaqin qarindoshingiz ushbu faoliyat bilan bog'liq bo'ladimi?",
    "options": ["Ha", "Yo'q"],
    "next": {
      "Ha": {
        "title": "⚠️ Potentsial manfaatlar to'qnashuvi",
        "steps": ["Korrupsiyaga qarshi kurashish agentligidan maslahat olish kerak"],
        "analysis": "Yaqin qarindoshingiz bog'liq bo'lgan tadbirkorlik faoliyatini yuritishni rejalashtirish, oldin davlat xizmatchisi bo'lgan shaxs uchun manfaatlar to'qnashuviga olib kelishi mumkin. Bu holat oilaviy aloqalar orqali oldingidagi davlat xizmatida orttirgan aloqalaringizdan noqonuniy foydalanish imkoniyatini yaratishi mumkin.",
        "recommendations": [
          "30 kun ichida Korrupsiyaga qarshi kurashish agentligiga yozma ravishda murojaat qiling",
          "Rejalashtirilayotgan tadbirkorlikda yaqin qarindoshingiz bilan o'zaro munosabatlaringizni aniq ko'rsating",
          "Qarindoshlik aloqalari orqali davlat xizmatida orttirgan aloqalaringizdan foydalanmaslikni ta'minlash uchun choralar taklif eting",
          "Ushbu vaziyatda qo'shimcha huquqiy maslahat olishni ko'rib chiqing"
        ],
        "legal_basis": [
          "O'zbekiston Respublikasi Adliya vazirligi tomonidan 2024-yil 5-noyabrda ro'yxatdan o'tkazilgan ro'yxat raqami 3569",
          "O'zbekiston Respublikasining 05.06.2024 yildagi O'RQ-931-son qonuni",
          "O'zbekiston Respublikasining 'Korrupsiyaga qarshi kurashish to'g'risida'gi qonuni"
        ]
      },
      "Yo'q": {
        "title": "✅ Manfaatlar to'qnashuvi yo'q",
        "steps": ["Sizning holatda manfaatlar to'qnashuvi aniqlanmadi"],
        "analysis": "Rejalashtirilayotgan shaxsiy tadbirkorlik faoliyatingiz va oldingi davlat xizmati o'rtasida manfaatlar to'qnashuviga olib keluvchi holatlar aniqlanmadi. Faoliyatingiz sovutish davri muddatlariga rioya qiladi, oldingi xizmatga bog'liq emas, davlat bilan aloqada emas va yaqin qarindoshlaringiz bu faoliyat bilan bog'liq emas.",
        "recommendations": [
          "Vaziyatingizda o'zgarishlar bo'lsa, qaytadan tekshiruv o'tkazing",
          "Oldingi davlat xizmatingiz bilan bog'liq aloqalardan foydalanmaslikni ta'minlang",
          "Tadbirkorlik faoliyatingizning kelajakda davlat bilan aloqalari paydo bo'lsa, tegishli idoralarni xabardor qiling",
          "Davlat xizmati ma'muriyati bilan aloqada bo'lishda shaffoflikni saqlang"
        ],
        "legal_basis": [
          "O'zbekiston Respublikasi Adliya vazirligi tomonidan 2024-yil 5-noyabrda ro'yxatdan o'tkazilgan ro'yxat raqami 3569",
          "O'zbekiston Respublikasining 05.06.2024 yildagi O'RQ-931-son qonuni",
          "O'zbekiston Respublikasining 'Korrupsiyaga qarshi kurashish to'g'risida'gi qonuni"
        ]
      }
    }
  }
}