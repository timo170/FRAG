'''n='d'
m='+'
for x in "QWERTYUIOPASDFGHJKLZXCVBNM":
    print("n\u207B")  # x² + y² = 2 '''
import pynliner

'''
html = "<h1>Hello World!</h1>"
css = "ch1 { color:#ffcc00; }"
p = pynliner.Pynliner()
p.from_string(html).with_cssString(css)
p=str(p)
print(p)
print(type(p))'''

html = "<style>h5 { color:#ffcc00; }</style><h1>Hello World!</h1>"
p=pynliner.Pynliner().from_string(html).run()
print(p)

'''
            <b><h5 style="margin-bottom: 0;margin-top: 0;">Reprezentarea prin matricea de adiacenţă:</h5></b>
            <p style="margin-bottom: 0;margin-top: 0;">Matricea de adiacenţă al unui graf de ordin n este o matrice pătratică de ordin n,</p>
            <img src="910839_orig.png">
            <ul>
                <li><a href='https://www.geeksforgeeks.org/python-programming-language/'>Python</a></li>
                <li><a href='https://www.geeksforgeeks.org/c-plus-plus/'>C++</a></li>
                <li><a href='https://www.geeksforgeeks.org/java/'>Java</a></li>
            </ul>
        '''

