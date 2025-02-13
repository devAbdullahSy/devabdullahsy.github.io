# المتغيرات variables
"""
- المتغير هو مكان في الذاكرة يخزن قيمة يمكن استخدامها وتغييرها لاحقًا.
- في بايثون لا تحتاج إلى تحديد نوع المتغير، لإن بايثون يحدد النوع تلقائيًا عند تخزين القيمة في المتغير.
- في بايثون في حاجة اسمها إسناد وهي تكون باستخدام العلامة يساوي = مثل هذا:
- x = ?
- الـ x هو المتغير والـ ؟ هو قيمة المتغير والـ = هو الإسناد.

"""
name = "Abdullah"
age= 30
country = "Egypt"

print("Hi, My name is", name, "and i'm", age, "years old and i'm from", country)

# العمليات الحسابية arithmetic operators
"""
- بايثون تدعم العمليات الحسابية الأساسية زي الجمع والطرح والضرب والقسمة ..إلخ.
"""

n1 = 10
n2 = 3

print(f"الجمع: {n1 + n2}")
print(f"الطرح: {n1 - n2}")
print(f"الضرب: {n1 * n2}")
print(f"القسمة: {n1 / n2}")
print(f"القسمة الصحيحة: {n1 // n2}")
print(f"باقي القسمة: {n1 % n2}")
print(f"الأس: {n1 ** n2}")

# العمليات المنطقية comparison & logical operators
"""
- هذه العمليات تستخدم للمقارنة بين القيم وتعيد إما True او False.
"""

# عمليات المقارنة

a = 7
b = 5

print(a > b)
print(a < b)
print(a == 7)
print(a != b)

# العمليات المنطقية and or not
"""
- هذه العمليات تستخدم لربط أكثر من شرط معًا.
"""

age1 = 20
is_student = True

print(age1 > 18 and is_student)
print(age1 < 18 or is_student)
print(not is_student)