from errbot import BotPlugin, botcmd, arg_botcmd

msg_gral = """@all
#YOUR ATTENTION PLEASE!: 
#{mensaje}
**LA GERENCIA**"""

msg_charla = """@all
#La charla: {mensaje} Esta por arrancar!!!
**LA GERENCIA**"""

class Announcer(BotPlugin):
    """
    Allow you to send messages to one or more channel
    """

    @botcmd
    def ann_gral(self, message, args):
        msg = msg_gral
        self.send(self.build_identifier('#general'),msg.format(args))
        return "Sent msg:\n{}\nTo #general".format(args)

    @arg_botcmd("--charla", dest='charla', type=str)
    def ann_charla(self, message, charla=None):
        msg = msg_charla
        self.send(self.build_identifier('#charlas'),msg.format(charla))
        return "Sent msg:\n"{}" \nTo #charlas".format(msg.format(charla))
