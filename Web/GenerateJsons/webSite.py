import random
import string
import web
from web import form

render = web.template.render('templates/')
urls = (
    '/', 'index'
)
app = web.application(urls, globals())
textArea = "TextAreaToGet"
myForm = form.Form(
    form.Textarea(name = textArea, id=textArea),
    form.Button("btn", id="Destroy all humans", value="deshum", html="Destroy all humans", class_="deshum"),
    form.Button("btn",type="submit", value= "Submit One"),
    form.Button("btn",type="submit", value= "Submit Two")
    )
#<input type="submit" value="Submit" name="Submit1" />
class index:

    def GET(self):
        form = myForm()
        return render.formtest(form)

    def POST(self):
        form = myForm()
        userData = web.input()
        if userData.btn == "Submit One":
            l =0
        mValue = form[textArea].value

        if not form.validates():
            return render.formtest(form)
        else:
            # form.d.boe and form['boe'].value are equivalent ways of
            # extracting the validated arguments from the form.

            #return u"Great success! boe: {0:s}, bax: {1:s}".format(form.d.TextAreaToGet) form['TextAreaToGet'].value
            return form[textArea].value


if __name__ == "__main__":
    web._InternalError = web.debugerror
    app.run()
