import os,shutil
path_videos="/media/fmiled/LaCie/out"
output_path="/media/fmiled/LaCie/owncloud"
for video in os.listdir(path_videos):
    info=video.split('_')
    annee=info[0]
    type_compet=info[1]
    lieu=info[2]
    exo=info[3]
    sexe=info[4]
    distance=info[5]
    epreuve=info[6]
    type_video=info[7]
    if not os.path.exists(os.path.join(output_path,annee+'_'+type_compet+'_'+lieu)):
        os.makedirs(os.path.join(output_path,annee+'_'+type_compet+'_'+lieu))
    if  not os.path.exists(os.path.join(output_path,annee+'_'+type_compet+'_'+lieu,annee+'_'+type_compet+'_'+lieu+'_'+exo+'_'+sexe+'_'+distance+'_'+epreuve)):
        os.makedirs(os.path.join(output_path,annee+'_'+type_compet+'_'+lieu,annee+'_'+type_compet+'_'+lieu+'_'+exo+'_'+sexe+'_'+distance+'_'+epreuve))
    if video not in os.listdir(os.path.join(output_path,annee+'_'+type_compet+'_'+lieu,annee+'_'+type_compet+'_'+lieu+'_'+exo+'_'+sexe+'_'+distance+'_'+epreuve)):

        src=os.path.join(path_videos,video)
        dst=os.path.join(os.path.join(os.path.join(output_path,annee+'_'+type_compet+'_'+lieu,annee+'_'+type_compet+'_'+lieu+'_'+exo+'_'+sexe+'_'+distance+'_'+epreuve),video))
        shutil.copy(src,dst)
    
    


