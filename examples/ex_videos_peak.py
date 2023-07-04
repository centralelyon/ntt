from ntt.videos.peak import detect_peak_video

if __name__ == "__main__":
    xa, xb, ya, yb = 750, 820, 3590, 3670
    # xa,xb,ya,yb = 500,580,3170,3230
    # xa,xb,ya,yb = 150,220,2550,2700
    # xa,xb,ya,yb = 10,100,2350,2400

    rep = detect_start_video(
        "./vidéos/2021_Montpellier_freestyle_hommes_50_FinaleC_fixeDroite.mp4",
        xa,
        xb,
        ya,
        yb,
        nb_frame=1300,
        afficher_anime=True,
        afficher_hist=True,
    )
    print(rep)
