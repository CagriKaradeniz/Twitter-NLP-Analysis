import pandas as pd
import time
from wordcloud import WordCloud,STOPWORDS,ImageColorGenerator
import pandas as pd
import numpy as np
from os import path
from PIL import Image
import textblob
from textblob import TextBlob
from textblob import Word
import  seaborn as sns
import matplotlib.pyplot as plt

atık=["https","t","o","bir","ne","neden","ve", "bu", "bir", "ile", "as", "veya", "icin", "boyle", "ad", "soyad", "iliskin", "dosya", "esas",
                "adi", "soyadi", '', "muvekkilimin",
                "gore", "nedeniyle", "adres", "fazla", "az", "tc", "itibaren", "tckimlik", "olarak", "sonra", "no",
                "ne", "niye", "neden", "nicin", "dolayi","co","da","mi","togg https","co","a","b","c","d","w","x","e","f","g","h","ı",
      "i","o","j","k","l","m","n","u","bi","si","ha","o","ö","p","r","s","ş","t","u","ü","v","y","z","nasil","mu","ki","cok","https t","t co","RT","https  t"
      "değil","var","vardır","diğer","için","https://t.co/","t.co","https://t","t","t.co/","https   t","https  t", "teşekkür","teşekkürler","Çok teşekkür"
      ]
df=pd.DataFrame()

df_yorum=pd.read_csv("../input/twitter/trk_politika_yorumlar.csv")
df_dısPolitika=pd.read_csv("../input/twitter/D_politika.csv")
mask=np.array(Image.open("../input/twitter/Trk.png"))

df_dısPolitika['Text'] = df_dısPolitika['Text'].str.replace('[^\w\s]','')
df_dısPolitika['Text'] = df_dısPolitika['Text'].str.replace('\d','')
df_dısPolitika['Text'] = df_dısPolitika['Text'].apply(lambda x: str(x))
df_dısPolitika['Text']=df_dısPolitika['Text'].apply(lambda x: " ".join(x for x in x.split() if x not in atık))
at=df_dısPolitika['Text'].apply(lambda x: " ".join(x for x in x.split() if x not in atık))
at=pd.DataFrame(at,columns=['Text'])
df_dısPolitika['Text']=at['Text']
yorum = " ".join(i for i in df_dısPolitika.Text)
text1=WordCloud(background_color="white",mask=mask,contour_color="firebrick",contour_width=3,max_words=1000).generate(yorum)

df_yorum=df_yorum[df_yorum["User Name"]!='Türk Politika🎙️']
df_yorum['Text'] = df_yorum['Text'].str.replace('[^\w\s]','')
df_yorum['Text'] = df_yorum['Text'].str.replace('\d','')
df_yorum['Text'] = df_yorum['Text'].apply(lambda x: str(x))
df_yorum['Text'] = df_yorum['Text'].apply(lambda x: " ".join(x for x in x.split() if x not in atık))
df_yorum['Text'].apply(lambda x: " ".join(x for x in x.split() if x not in atık))
at=pd.DataFrame(at,columns=['Text'])
df_yorum['Text']=at['Text']
yorum = " ".join(i for i in df_dısPolitika.Text)
text2=WordCloud(background_color="white",mask=mask,contour_color="firebrick",contour_width=4,max_words=300).generate(yorum)

plt.figure(1)
plt.imshow(text1,interpolation="bilinear")
plt.axis("off")
plt.show()

plt.figure(1)
plt.imshow(text2,interpolation="bilinear")
plt.axis("off")
plt.show()

