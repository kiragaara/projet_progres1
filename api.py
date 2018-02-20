import bottle
import datetime


@bottle.error(404)
def error_404(error):
    print("az")
    print(error)
    print("az")
    return "<h1> no found 404 </h1>" 



@bottle.route("/qui")
def qui() :
    stri = """
    <form method='post' action='bonjour'>
    <input type='text' name='nom' placeholder='Votre nom ?'/>
    <input type='submit' value='Validez !'/>
    </form>
    """
    return stri


@bottle.route("/bonjour", method='POST')
def bonjour() :
    nom = bottle.request.forms.get('nom')
    return "Bonjour " + format(nom)

@bottle.route("authors/<name>")
def authores(name):
    test = " co auteurs chkoupi"
    return name+test 


bottle.run(bottle.app(), host='localhost', port=8080, debug= True, reloader=True)
