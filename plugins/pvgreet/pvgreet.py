from errbot import BotPlugin, botcmd, arg_botcmd
# vim: nospell


greet_message = """**Te damos la bienvenida, {}!**
Este espacio está pensado para que podamos trabajar, compartir info útil, y ayudarnos

* Poné buena onda, conocé colegas, compartí ideas, material, ayuda para workshops y coworking :)
* Los canales públicos son los establecidos para el evento. Podés crear canales privados segun prefieras


# Canales publicos:
\#charlas - Info de charlas, anuncios, updates, preguntas
\#coworking - Colaborar en coworking, ayudar a otros colegas, compartí data
\#general - Información general, anuncios, preguntas, cosultas
\#lost_found - Si perdiste o encontraste algo, podés anunciarlo acá. Te pedimos también que se lo acerques a alguien de la organización
\#social - Socializar en general y conocer gente copada!
\#workshops - Ayuda y materiales de los workshops


# NO SE PERMITE:
* Insultos, lenguaje ofensivo u obsceno de ningun tipo. Nada, ni en chiste.
* Fotos, videos o cualquier tipo de material pornográfico, ofensivo, violento, racista, misógino, o que tenga como objetivo herir la sensibilida
* Flood, spam, publicidad, o cualquier tipo de contenido/molestia que no cuadre con el espíritu de nerdear.la
* Archivos aplicativos, ejecutables, scripts, etc. Si desean compartir software o archivos ejectuables les pedimos que utilicen Box, Dropbox, Dr
"""


class Pvgreet(BotPlugin):
    """
    Private Greet on user connect
    """
    def activate(self):
        super().activate()
        self._message = greet_message

    def callback_connect(self):
        """
        Triggers when bot is connected

        You should delete it if you're not using it to
        override any default behaviour
        """
        #self.warn_admins("Se reconecto @nerdobot!")
        self.send(self.build_identifier("@qlixed"), "Se reconecto @nerdobot!")

    def callback_presence(self, presence):
        the_who = presence.identifier.person
        if presence.status == 'online' and the_who == "@qlixed":
            identifier = self.build_identifier(the_who)
            self.log.debug(
                "Sending message to {}({})".format(the_who,
                      str(identifier)))
            self.send(identifier,
                      self._message.format(the_who))

    @botcmd(split_args_with=None)
    def greet_me(self, message, args):
        #yield str(dir(message))
        return  self._message.format(message.frm)

    
