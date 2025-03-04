# -*- coding: utf-8 -*-
"""yapilacakListesi.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1YZhOt8wB-yZHM0YT8f6uZdZ96I6dTfdT
"""

def main () :
  tasks = []
  while True :
    print( "\n===== Yapılacaklar Listesi =====" )
    print( "1. Görev Ekle" )
    print( "2. Görevleri Göster" )
    print( "3. Görevi Tamamlandı Olarak İşaretle" )
    print( "4. Çık" )

    secim = input ( "Seçiminizi Girin: " )
    if secim == '1' :
      print ()
      n_tasks = int ( input ( "Kaç Görev Eklemek İstiyorsunuz: " ))

      for i in range (n_tasks):
        task = input ( "Görevi girin: " )
        tasks.append({ "task" : task, "done" : False })
        print ( "Görev eklendi! ")

    elif secim == '2' :
      print ("\nGörevler:")
      for index, task in enumerate (tasks):
          status = "Tamamlandı" if task[ "done" ] else "Tamamlanmadı"
          print ( f" {index + 1 } . {task[ 'task']} - {status} " )

    elif secim == '3' :
      task_index = int ( input ( "Tamamlandı olarak işaretlenecek görev numarasını girin: ")) - 1
      if  0 <= task_index < len (tasks):
        tasks[task_index][ "done" ] = True
        print ( "Görev tamamlandı olarak işaretlendi!" )
      else :
        print ( "Geçersiz görev numarası" )

    elif secim == '4' :
      print ( "Yapılacaklar listesinden çıkılıyor" )
      break
    else :
      print ("Geçersiz seçim. Lütfen tekrar deneyin." )

if __name__ == "__main__" :
    main()