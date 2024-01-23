>## สมาชิกในกลุ่ม 
>- นายวิชญ์ภาส โพธิ์พุ่มเย็น 6510450950<br>
>- นายอติราช แก้ววิเชียร 6510451051

>## ลิงค์ข้อมูลที่จะใช้ใน mini-project
>***Employee Turnover***<br>
>https://www.kaggle.com/datasets/marikastewart/employee-turnover

>## มีค่าที่หายไป (missing values) หรือไม่ อะไรบ้าง แบบใด มากน้อยแค่ไหน แก้ไขได้อย่างไร
> ใน data set นี้จากที่ได้รับมาไม่มี missing values ในรูปแบบไหนเลย แต่หากเกิด missing values ขึ้นจริงๆก็อาจจะเข้ารูปแบบ MCAR (Missing Compleltely at random) ซึ่งจะแก้ไขด้วยวิธี row deletion กับข้อมูลที่ไม่สมบูรณ์

>## แต่ละลักษณะ/feature ต้องมีการทำกระบวนการต่างๆ (operations) หรือไม่ อะไรบ้าง อย่างไร
>ใน data set นี้มี department feature ที่ถูก encoding โดยวิธี Encoding Categorical Features โดยเราใช้วิธี Label encoding ในการแยกความแตกต่างของแต่ละหมวดหมู่ ส่วนใน left feature จะไม่ถูกแปลง เพราะจะใช้เป็นผลเฉลย ส่วน review และ satisfactio feature เป็นค่าแบบต่อเนื่อง จึงใช้วิธี Discretization ในการปรับค่าเป็นช่วงๆแทน และส่วน number feature อื่นๆไม่ต้องทำ operation ใดๆ เพราะในแต่ละ feature มีความเป็นการแจกแจงแบบปกติอยู่แล้ว

>## สามารถป้องกันการเกิด data leakage ได้อย่างไรบ้าง (สำหรับ dataset นี้)
> ไม่ควรสร้าง feature ที่เยอะจนเกินไปหรือมีความละเอียดเยอะมากๆ จะทำให้เกิด overfitting ได้ และควรแบ่งข้อมูลให้มีการกระจายไปทั่ว ไม่ให้การเกิดการเกาะกลุ่มของข้อมูล

>## ประเด็นอื่น ๆ ที่เกี่ยวข้องกับข้อมูลของตัวเอง
>ไม่มี