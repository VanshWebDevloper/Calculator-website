from django.shortcuts import render
 
def calculator(request):
     display = ""
     op = ""
     stored = ""
     result = None
 
     if request.method == "POST":
         action = request.POST.get("action", "")
         display = request.POST.get("display", "")
         op = request.POST.get("op", "")
         stored = request.POST.get("stored", "")
 
         if action and action.startswith("digit_"):
             display += action[-1]
 
         elif action in ("add", "subtract", "multiply", "divide"):
             stored, op, display = display, action, ""
 
         elif action == "equals":
             if stored and op:
                 try:
                     a = float(stored)
                     b = float(display)
                     if op == "add":
                         result = a + b
                     elif op == "subtract":
                         result = a - b
                     elif op == "multiply":
                         result = a * b
                     elif op == "divide":
                         if b == 0:
                             result = "can't divide by 0"
                         else:
                             result = a / b
                 except ValueError:
                     result = "error"
                 if result is not None:
                     display = str(result)
                 stored = ""
                 op = ""
 
         elif action == "clear":
             display = ""
             stored = ""
             op = ""
 
     return render(request, "calculator.html", {
         "display": display,
         "op": op,
         "stored": stored,
     })