import json
import sqlite3

bibles = [
    ["Afrikaans", "Afrikaans 1933/1953", "af_afr53"],
    ["Akan", "Akuapem Twi Contemporary Bible", "ak_wakna"],
    ["Albanian", "Bibla Shqip 1994", "sq_albb"],
    ["Ancient Greek", "Textus Receptus (Η Καινή Διαθήκη)", "grc_grctr"],
    [
        "Ancient Greek",
        "Septuagint, Brenton (μετάφραση των εβδομήκοντα)",
        "grc_grcbrent",
    ],
    ["Arabic", "Ketab El Hayat Majani", "ar_kehm"],
    ["Armenian", "Նոր Էջմիածին Աստվածաշունչ (New Etchmiadzin Bible)", "hy_neb"],
    ["Assamese", "Indian Revised Version (IRV) Assamese 2019", "as_irvasm"],
    ["Basque", "Navarro-Labourdin Basque Bible", "eu_bhnt"],
    ["Belarusian", "Bíblia (tradução de V. Semukha)", "be_bbl"],
    ["Bengali", "Indian Revised Version (IRV) Bengali", "bn_irvben"],
    ["Bislama", "Open Bislama Bible Revised", "bi_obbr"],
    ["Brazilian Portuguese", "Almeida Revisada Imprensa Bíblica", "pt_aa"],
    ["Brazilian Portuguese", "Almeida Corrigida e Revisada Fiel", "pt_acf"],
    ["Brazilian Portuguese", "Almeida Revista e Atualizada", "pt_ara"],
    ["Brazilian Portuguese", "Almeida Revista e Corrigida", "pt_arc"],
    ["Brazilian Portuguese", "Almeida Revista e Corrigida 1969", "pt_rc69"],
    ["Brazilian Portuguese", "Almeida Século 21", "pt_a21"],
    ["Brazilian Portuguese", "Bíblia para Todos", "pt_bpt09"],
    ["Brazilian Portuguese", "Bíblia Sagrada Ave-Maria", "pt_avm"],
    ["Brazilian Portuguese", "Bíblia Sagrada: Versão Fácil de Ler", "pt_vfl"],
    ["Brazilian Portuguese", "Edição Pastoral", "pt_pastoral"],
    ["Brazilian Portuguese", "King James Atualizada", "pt_kja"],
    ["Brazilian Portuguese", "King James Fiel", "pt_bkj"],
    ["Brazilian Portuguese", "Nova Almeida Atualizada", "pt_naa"],
    ["Brazilian Portuguese", "Nova Bíblia Viva 2007", "pt_nbv"],
    ["Brazilian Portuguese", "Nova Tradução na Linguagem de Hoje", "pt_ntlh"],
    ["Brazilian Portuguese", "Nova Versão Internacional", "pt_nvi"],
    ["Brazilian Portuguese", "Nova Versão Internacional 2011", "pt_nvi2011"],
    ["Brazilian Portuguese", "Nova Versão Transformadora", "pt_nvt"],
    ["Brazilian Portuguese", "O Livro", "pt_ol"],
    ["Brazilian Portuguese", "Tradução Brasileira", "pt_tb"],
    ["Brazilian Portuguese", "Tradução do Pe. Matos Soares", "pt_matos"],
    ["Bulgarian", "Veren", "bg_vbg"],
    ["Burmese", "Judson Bible", "my_jbmle"],
    ["Catalan", "Bíblia Catalana Interconfessional", "ca_bci"],
    ["Cebuano", "Ang Pulong sa Dios", "ceb_oapd"],
    ["Central Kurdish", "Kurdi Sorani Standard Version", "ckb_okss"],
    [
        "Chinese",
        "Chinese Union Version (New Punctuation, Shen Edition)",
        "zh_cunpss-shen",
    ],
    ["Chinese", "New Chinese Version", "zh_cnvs"],
    ["Croatian", "Knjiga o Kristu", "hr_okok"],
    ["Czech", "Bible Kralická 1613", "cs_bkr"],
    ["Dutch", "De Heilige Schrift, Petrus Canisiusvertaling, 1939", "nl_nld1939"],
    ["English", "American Standard Version 1901", "en_asv"],
    ["English", "Amplified Bible", "en_amp"],
    ["English", "Basic English", "en_bbe"],
    ["English", "Berean Standard Bible", "en_bsb"],
    ["English", "Christian Standard Bible", "en_csb"],
    ["English", "Contemporary English Version", "en_cev"],
    ["English", "Darby's Translation 1890", "en_darby"],
    ["English", "Douay-Rheims American 1899", "en_dra"],
    ["English", "English Standard Version", "en_esv"],
    ["English", "Free Bible Version", "en_fbv"],
    ["English", "Geneva Bible", "en_gnv"],
    ["English", "Good News Translation", "en_gnt"],
    ["English", "Jubilee Bible", "en_jub"],
    ["English", "King James Version", "en_kjv"],
    ["English", "King James Version with Apocrypha", "en_kjva"],
    ["English", "Lexham English Bible", "en_leb"],
    ["English", "Literal Standard Version", "en_lsv"],
    ["English", "Majority Standard Bible", "en_mbsb"],
    ["English", "New American Standard Bible 2020", "en_nasb"],
    ["English", "New International Version", "en_niv"],
    ["English", "New King James Version", "en_nkjv"],
    ["English", "New Living Translation", "en_nlt"],
    ["English", "New Messianic Version Bible", "en_nmv"],
    ["English", "Revised Version 1885", "en_engrv"],
    [
        "English",
        "The Cambridge Paragraph Bible of the Authorized English Version",
        "en_kjvcpb",
    ],
    ["English", "The Orthodox Jewish Bible", "en_tojb2011"],
    ["English", "A Translation for Translators", "en_t4t"],
    ["English", "World English Bible (American Edition)", "en_web"],
    ["English", "World English Bible Updated", "en_webu"],
    ["English", "World English Bible (British Edition)", "en_webbe"],
    [
        "English",
        "World English Bible, American English Edition, without Strong's numbers",
        "en_webus",
    ],
    ["English", "World Messianic Bible (American English)", "en_wmb"],
    ["English", "World Messianic Bible (British English)", "en_wmbbe"],
    ["English", "Wycliffe's Bible with Modern Spelling", "en_wbms"],
    ["English", "Young's Literal Translation 1898", "en_ylt98"],
    ["Esperanto", "La Sankta Biblio 1926", "eo_esp"],
    [
        "Estonian",
        "Vaba kasutusega Uus Testament, Pühakiri kaasaegses eesti keeles",
        "et_opkek",
    ],
    ["Ewe", "Ewe Contemporary Scriptures", "ee_oal"],
    ["Filipino", "Ang Biblia 1905", "tl_abtag"],
    ["Finnish", "Kirkkoraamattu 1933/38", "fi_fb38"],
    ["French", "Le Bible de I'Épée", "fr_apee"],
    ["German", "Schlachter 1951", "de_sch1951"],
    ["Greek", "Modern Greek (Demotic)", "el_fpb"],
    ["Gujarati", "Indian Revised Version (IRV) Gujarati 2019", "gu_irvguj"],
    ["Haitian Creole", "Bib Sen An: Kreyòl Ayisyen", "ht_bsa"],
    ["Hausa", "Hausa Contemporary Bible", "ha_bsrk"],
    ["Hebrew", "Westminster Leningrad Codex (WLC)", "he_wlc"],
    ["Hindi", "Indian Revised Version (IRV) Hindi 2019", "hi_irvhin"],
    ["Hungarian", "Károli 1908", "hu_hunk"],
    ["Icelandic", "Opna Lifandi Orð: Nýja testamentið og Sálmarnir", "is_olo"],
    ["Igbo", "Igbo Contemporary Bible", "ig_biuo"],
    [
        "Indonesian",
        "Alkitab Terjemahan Sederhana Indonesia, Edisi Ketiga (TSI)",
        "id_tsi",
    ],
    ["Italian", "Sacra Bibbia Versione Riveduta 2020", "it_irb20"],
    ["Japanese", "聖書 新共同訳 (Shinkyodoyaku)", "ja_jniv"],
    ["Kannada", "Indian Revised Version (IRV) Kannada 2019", "kn_irvkan"],
    ["Kazakh", "Киелі кітап", "kk_qazbi"],
    ["Kikuyu", "Kiugo Gĩtheru Kĩa Ngai Kĩhingũre", "ki_kgnk"],
    ["Kinyarwanda", "Rufumbira New Testament", "rw_ruf"],
    ["Kirundi", "Kirundi Contemporary Bible", "rn_obkc"],
    ["Korean", "Korean Revised", "ko_krv"],
    ["Latin", "Vulgata Latina", "la_vulg"],
    ["Latvian", "Glika Bībele", "lv_lg8"],
    ["Lingala", "Lingala Contemporary Bible", "ln_smnb"],
    ["Luganda", "Bayibuli Entukuvu", "lg_olcb"],
    ["Malay", "Alkitab Berita Baik", "ms_tmvr"],
    ["Malayalam", "Indian Revised Version (IRV) Malayalam", "ml_irvmal"],
    ["Maori", "Paipera Tapu 2012", "mi_mri2012"],
    ["Marathi", "Indian Revised Version (IRV) Marathi", "mr_irvmar"],
    ["Nepali", "Open Nepali Contemporary Version", "ne_oncv"],
    ["Northern Ndebele", "Ndebele Contemporary Bible", "nd_oben"],
    ["Norwegian (Bokmål)", "Bibel 2011", "nb_bibel2011"],
    ["Nyanja", "Chichewa Contemporary Version", "ny_tccl"],
    ["Odia", "Indian Revised Version (IRV) Odia", "or_irvory"],
    ["Oromo", "New Oromo Contemporary Version", "om_onocv"],
    ["Persian", "Persian Contemporary Bible 2022", "fa_opcb"],
    ["Polish", "Uwspółcześniona Biblia Gdańska", "pl_ubg"],
    ["Punjabi", "Indian Revised Version (IRV) Punjabi", "pa_irvpun"],
    ["Romanian", "Versiunea Dumitru Cornilescu", "ro_vdc"],
    ["Russian", "Синодальный перевод (Synodal Translation)", "ru_synod"],
    ["Sanskrit", "Sanskrit Bible (सत्यवेदः)", "sa_san-dn"],
    ["Scottish Gaelic", "Am Bìoball Gàidhlig 1992", "gd_abg1992"],
    ["Serbian", "Daničić-Karadžić", "sr_dk"],
    ["Shona", "Shona Contemporary Bible 2017", "sn_bdrsc"],
    ["Slovak", "Nádej pre každého", "sk_onpk"],
    ["Spanish", "Reina Valera 1960", "es_rvr1960"],
    ["Swahili", "Swahili Revised Union Version", "sw_sruv"],
    ["Swedish", "Svenska Folkbibeln 2015", "sv_sfb15"],
    ["Tamil", "Indian Revised Version (IRV) Tamil", "ta_irvtam"],
    ["Telugu", "Indian Revised Version (IRV) Telugu 2019", "te_irvtel"],
    ["Thai", "Thai KJV", "th_kjvthai"],
    ["Tongan", "Ko e Tohi Tapu Kātoa", "to_rwv"],
    ["Tswana", "Lefoko: La Botshelo Kgolagano e Ntsha", "tn_olef"],
    ["Turkish", "Yorumsuz Türkçe Çeviri", "tr_ytc"],
    [
        "Ukrainian",
        "Бібліка Відкрита Новий Переклад Українською (Biblica Open New Ukrainian Translation)",
        "uk_vnpu",
    ],
    ["Urdu", "Indian Revised Version (IRV) Urdu 2019", "ur_irvurd"],
    ["Vietnamese", "Tiếng Việt", "vi_vie"],
    ["Yiddish", "Orthodox Yiddish Tanakh (ארטאדאקסישע תּנ״ך)", "yi_oytanakh"],
    ["Yoruba", "Yoruba Contemporary Bible", "yo_oycb"],
]


def parse_file(name):
    with open(name, "rb") as source:
        bible = json.load(source)

    for book in bible:
        book_name = book["name"]
        book_abbrev = book["abbrev"]
        for chapter, verses in enumerate(book["chapters"], start=1):
            for verse, quote in enumerate(verses, start=1):
                yield (book_name, book_abbrev, chapter, verse, quote)


def parse_all():
    con = sqlite3.connect("bibles.db")
    cur = con.cursor()
    for language, version, code in bibles:
        file = f"json/{code}.json"
        for book, book_abbrev, chapter, verse, quote in parse_file(file):
            cur.execute(
                f"INSERT INTO bibles VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                [language, version, code, book, book_abbrev, chapter, verse, quote],
            )
        con.commit()
    con.close()


def create_db():
    con = sqlite3.connect("bibles.db")
    cur = con.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS bibles(
            language TEXT,
            version TEXT,
            version_code TEXT,
            book TEXT,
            book_abbrev TEXT,
            chapter INTEGER,
            verse INTEGER,
            quote TEXT);
        """)

    cur.execute("""CREATE INDEX IF NOT EXISTS language_index ON bibles(language);""")
    cur.execute("""CREATE INDEX IF NOT EXISTS version_index ON bibles(version);""")
    cur.execute(
        """CREATE INDEX IF NOT EXISTS version_code_index ON bibles(version_code);"""
    )
    cur.execute("""CREATE INDEX IF NOT EXISTS quote_index ON bibles(quote);""")
    con.close()


create_db()
parse_all()
