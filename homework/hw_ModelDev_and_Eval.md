>## สมาชิกในกลุ่ม 
>- นายวิชญ์ภาส โพธิ์พุ่มเย็น 6510450950<br>
>- นายอติราช แก้ววิเชียร 6510451051

>## ลิงค์ข้อมูลที่จะใช้ใน mini-project
>***Employee Turnover***<br>
>https://www.kaggle.com/datasets/marikastewart/employee-turnover

>## mini-project ของตัวเองสามารถใช้ algorithm อะไรได้บ้าง
>SVC(SVM) เป็นตัวเริ่มต้นของการทดลอง และต่อมา KNeighbors Classifiers 

>## แต่ละ algorithm มี hyperparameter อะไรบ้าง ปรับเป็นอะไรได้บ้าง
>SVC(SVM) มี "gamma", "kernel"
>KNeighbors Classifiers มี "n_neighbors", "algorithm", "leaf_size", "p"

>## training score, test score, mean cross validation score ปัจจุบันมีค่าเท่าไหร่
> mean cross validation score โดยเฉลี่ยอยู่ที่ 0.83 - 0.85
> training score โดยเฉลี่ยอยู่ที่ 0.83-0.85
> test score โดยเฉลี่ยอยู่ที่ 0.80-0.84

>## ใช้ baseline และ วิธีการประเมินอะไรได้บ้าง อย่างไร
>เนื่องจาก project ของพวกเราเป็นแบบ classification จึงมีการใช้ baseline แบบ mostfrequent, prior, stratified, uniform

>## จากการทดลองเบื้องต้น สามารถนำโมเดลไปใช้งานจริงได้แล้วหรือไม่ เพราะเหตุใด
> คิดว่าจากการได้เห็นประสิทธิภาพของการ train model และนำไปทดสอบแล้วได้ค่าประสิทธิภาพ accuracy ประมาณ 0.83 ซึ่งถ้าเราเทียบกับ baseline แล้วที่ score อยู่ที่ประมาณ 0.5 - 0.7 ซึ่งจากผลลัพธ์ตรงนี้ก็คิดว่าสามารถนำไปใช้งานจริงได้แล้ว

>##  ทำอะไรได้บ้างเพื่อให้คะแนนต่าง ๆ มีค่าสูงขึ้น และ/หรือ โมเดลมีประโยชน์มากขึ้น
> มีการปรับ hyperparameters ของแต่ละ models โดยใช้ GridServeCV เพื่อหาค่า hyperparameters ที่ดีที่สุด แล้วอีกทั้งยังใช้วิธีแบบ Ensemble Classifier แบบ Voting และ Stacking ซึ่งมีประโยชน์ทั้งในเรื่องประสิทธิภาพแล้วระยะเวลาในการ train models อีกด้วย

>## ประเด็นอื่น ๆ ที่เกี่ยวข้องกับงานของตัวเอง
>ไม่มี