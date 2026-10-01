; =====================================================================
;  Diablo 4 - Skill Rotation Helper (AutoHotkey v2)
; ---------------------------------------------------------------------
;  F1            : toggle ON / OFF   (hanya jalan di window Diablo IV)
;  F2            : reload script
;  Shift + Esc   : exit script
;
;  Behaviour saat ON:
;    - Skill 2 di-HOLD terus (channeling tidak putus)
;    - Skill 1, 3, 4 ditekan berulang tiap 100 ms (bergiliran)
;
;  Semua hotkey & timer dikunci ke window Diablo IV. Di luar game,
;  F1/F2 diteruskan ke aplikasi lain seperti tombol biasa.
; =====================================================================

#Requires AutoHotkey v2.0
#SingleInstance Force
SendMode "Event"          ; Event mode lebih mirip input fisik dibanding Input mode
SetKeyDelay 10, 25        ; delay antar key, durasi tekan (ms)
SetTitleMatchMode 3       ; judul harus sama persis, bukan sekadar mengandung

; --------------------------- Config ----------------------------------
; Window game diidentifikasi lewat nama proses (paling andal) DAN judul.
GAME_EXE    := "ahk_exe Diablo IV.exe"
GAME_TITLE  := "Diablo IV"
REPEAT_MS   := 100           ; interval spam skill 1/3/4
CHANNEL_KEY := "2"           ; skill channeling yang ditahan
SPAM_KEYS   := ["1", "3", "4"]
; ---------------------------------------------------------------------

active    := false
spamIndex := 1

; Watcher jalan terus (ringan): begitu fokus lepas dari game, rotation
; langsung dimatikan tanpa menunggu tick SpamSkills berikutnya.
SetTimer FocusWatchdog, 25

; #HotIf: hotkey di bawah ini HANYA terdaftar saat window game aktif.
; Di luar game, F1/F2/Shift+Esc berfungsi normal untuk aplikasi lain.
#HotIf GameActive()
F1:: ToggleRotation()
F2:: Reload
+Esc:: ExitApp
#HotIf

; Window game aktif? Cek proses dulu, fallback ke judul kalau nama exe berubah.
; `global` wajib: fungsi di AHK v2 tidak melihat variabel global kecuali
; dideklarasikan, dan #HotIf mengevaluasi fungsi ini terus-menerus.
GameActive() {
    global GAME_EXE, GAME_TITLE
    return WinActive(GAME_EXE) || WinActive(GAME_TITLE)
}

ToggleRotation() {
    global active, REPEAT_MS
    active := !active
    if (active) {
        StartChannel()
        SetTimer SpamSkills, REPEAT_MS
        ShowStatus("Rotation ON")
    } else {
        StopRotation()
        ShowStatus("Rotation OFF")
    }
}

; Matikan timer + lepas tombol. Dipakai saat toggle off maupun saat
; fokus keluar dari game.
StopRotation() {
    global active
    active := false
    SetTimer SpamSkills, 0
    StopChannel()
}

; Kirim key langsung ke handle window game, bukan ke "window yang sedang
; fokus". Kalau game tidak aktif, tidak ada yang dikirim sama sekali --
; ini jaring pengaman kalau fokus berubah persis saat Send berjalan.
SendToGame(keySpec) {
    global GAME_EXE, GAME_TITLE
    hwnd := WinActive(GAME_EXE)
    if (!hwnd)
        hwnd := WinActive(GAME_TITLE)
    if (!hwnd)
        return false
    ControlSend keySpec, , hwnd
    return true
}

; Tekan dan tahan skill channeling
StartChannel() {
    global CHANNEL_KEY
    SendToGame("{" CHANNEL_KEY " down}")
}

; Lepas tombol channeling. Dipanggil juga saat game sudah tidak aktif,
; jadi pakai WinExist (bukan WinActive) supaya key benar-benar dilepas
; di window game meski fokus sudah pindah.
StopChannel() {
    global CHANNEL_KEY, GAME_EXE, GAME_TITLE
    hwnd := WinExist(GAME_EXE)
    if (!hwnd)
        hwnd := WinExist(GAME_TITLE)
    if (hwnd)
        ControlSend "{" CHANNEL_KEY " up}", , hwnd
}

; Dipanggil timer tiap REPEAT_MS: kirim satu skill per tick secara bergiliran
SpamSkills() {
    global spamIndex, SPAM_KEYS, CHANNEL_KEY

    ; Fokus pindah dari game -> hentikan total, jangan kirim apa pun
    ; ke aplikasi lain. Harus di-toggle ulang dengan F1 di dalam game.
    if (!GameActive()) {
        StopRotation()
        return
    }

    ; pastikan channeling tetap ter-hold
    if (!GetKeyState(CHANNEL_KEY, "P"))
        SendToGame("{" CHANNEL_KEY " down}")

    key := SPAM_KEYS[spamIndex]
    SendToGame("{" key "}")

    spamIndex := Mod(spamIndex, SPAM_KEYS.Length) + 1
}

; Deteksi loss-focus lebih cepat daripada interval spam (100 ms).
FocusWatchdog() {
    global active
    if (active && !GameActive())
        StopRotation()
}

ShowStatus(text) {
    ToolTip text
    SetTimer () => ToolTip(), -1200
}

; Safety: lepas tombol saat reload / exit
OnExit((*) => StopChannel())
