def filtre_rouge(img):
  for i in range(img[0][1]):
    for j in range(img[0][2]):
      r,v,b=img[1][i][j]
      img[1][i][j]=(r,0,0)
  return img

def filtre_vert(img):
  for i in range(img[0][1]):
    for j in range(img[0][2]):
      r,v,b=img[1][i][j]
      img[1][i][j]=(0,v,0)
  return img

def filtre_bleu(img):
  for i in range(img[0][1]):
    for j in range(img[0][2]):
      r,v,b=img[1][i][j]
      img[1][i][j]=(0,0,b)
  return img

def filtre_gris(img):
  for i in range(img[0][1]):
    for j in range(img[0][2]):
      r,v,b=img[1][i][j]
      img[1][i][j]=(r,r,r)
  return img

def filtre_binarisation(img):
  for i in range(img[0][1]):
    for j in range(img[0][2]):
      r,v,b=img[1][i][j]
      if r<=128:
        r=255
      else:r=0
      img[1][i][j]=(r,r,r)
  return img


def filtre_monochrome(img):
  for i in range(img[0][1]):
    for j in range(img[0][2]):
      r,v,b=img[1][i][j]
      img[1][i][j]=r*0.299+v*0.587+b*0.114
  return img

def filtre_monochrome2(img):
  for i in range(img[0][1]):
    for j in range(img[0][2]):
      r,v,b=img[1][i][j]
      img[1][i][j]=r*0.2125+v*0.7154+b*0.0721
  return img

def filtre_negatif(img):
  for i in range(img[0][1]):
    for j in range(img[0][2]):
      r,v,b=img[1][i][j]
      img[1][i][j]=(255-r,255-v,255-b)
  return img
