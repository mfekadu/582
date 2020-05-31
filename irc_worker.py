#! /usr/bin/env python
#
# Example program using irc.bot.
#
# Joel Rosdahl <joel@rosdahl.net>
# slight modifications by Foaad Khosmood
# futher modification by Michael Fekadu to chat with Rasa over REST webhook
#
# Original Source: https://github.com/jaraco/irc
#
# NOTE: The SimpleIRCClient._dispatcher will seek functions named "on_<event_type>"
#     * Event Types:
#         * https://github.com/jaraco/irc/blob/1331ba85b5d093f06304d316a03a832959eaf4da/irc/events.py#L1-L201
#     * Source:
#         * https://github.com/jaraco/irc/blob/1331ba85b5d093f06304d316a03a832959eaf4da/irc/client.py#L1119

"""A simple IRC bot.

# Michael:
# This bot/worker serves as Rasa's eyes and ears.
# It handles simple commands, and passes all else to Rasa via REST.

This is an example bot that uses the SingleServerIRCBot class from
irc.bot.  The bot enters a channel and listens for commands in
private messages and channel traffic.  Commands in channel messages
are given by prefixing the text by the bot name followed by a colon.
It also responds to DCC CHAT invitations and echos data sent in such
sessions.
The known commands are:
    stats -- Prints some channel information.
    disconnect -- Disconnect the bot.  The bot will try to reconnect
                  after 60 seconds.
    die -- Let the bot cease to exist.
    dcc -- Let the bot invite you to a DCC CHAT connection.
"""

import logging
import os
import sys

import irc.bot
import irc.strings
from irc.client import ip_numstr_to_quad, ip_quad_to_numstr

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
# create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
# create formatter
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
# add formatter to ch
ch.setFormatter(formatter)
# add ch to logger
logger.addHandler(ch)


try:
    from rasa.core.constants import DEFAULT_SERVER_URL
except ModuleNotFoundError:
    logging.warning("No rasa? Consider: `pip install rasa`")
    DEFAULT_SERVER_URL = "http://localhost:5005"


DEFAULT_SERVER_URL = os.environ.get("RASA_SERVER_URL", DEFAULT_SERVER_URL)
IRC_CHANNEL = os.environ.get("RASA_IRC_CHANNEL", "#CPE582")
IRC_SERVER = os.environ.get("RASA_IRC_SERVER", "irc.freenode.net")
IRC_PORT = os.environ.get("RASA_IRC_PORT", 6667)


class RasaIRCBot(irc.bot.SingleServerIRCBot):
    def __init__(self, channel, nickname, server, port=6667):
        irc.bot.SingleServerIRCBot.__init__(self, [(server, port)], nickname, nickname)
        self.channel = channel

    def get_version(self):
        """
        https://github.com/jaraco/irc/blob/1331ba85b5d093f06304d316a03a832959eaf4da/irc/bot.py#L310-L315
        """
        logger.debug("function called: get_version...")
        super(RasaIRCBot, self).get_version()
        logger.debug("completed: get_version...")

    def die(self, msg="Bye, cruel world!"):
        """
        https://github.com/jaraco/irc/blob/1331ba85b5d093f06304d316a03a832959eaf4da/irc/bot.py#L288-L297
        """
        logger.debug("function called: die...")
        super(RasaIRCBot, self).die(msg=msg)
        logger.debug("completed: die...")

    def disconnect(self, msg="I'll be back!"):
        """
        https://github.com/jaraco/irc/blob/1331ba85b5d093f06304d316a03a832959eaf4da/irc/bot.py#L299-L308
        """
        logger.debug("function called: disconnect...")
        super(RasaIRCBot, self).disconnect(msg=msg)
        logger.debug("completed: disconnect...")

    def jump_server(self, msg="Changing servers"):
        """
        https://github.com/jaraco/irc/blob/1331ba85b5d093f06304d316a03a832959eaf4da/irc/bot.py#L317-L327
        """
        logger.debug("function called: jump_server...")
        super(RasaIRCBot, self).jump_server(msg=msg)
        logger.debug("completed: jump_server...")

    def _connect(self):
        logger.debug("function called: _connect...")
        super(RasaIRCBot, self)._connect()
        logger.debug("completed: _connect...")

    def _on_disconnect(self, connection, event):
        logger.debug(
            (
                "function called: _on_disconnect...\n"
                f"connection: {connection}\n"
                f"event: {event}\n"
            )
        )
        super(RasaIRCBot, self)._on_disconnect(connection, event)
        logger.debug("completed: _on_disconnect...")

    def _on_join(self, connection, event):
        logger.debug(
            (
                "function called: _on_join...\n"
                f"connection: {connection}\n"
                f"event: {event}\n"
            )
        )
        super(RasaIRCBot, self)._on_join(connection, event)
        logger.debug("completed: _on_join...")

    def _on_kick(self, connection, event):
        logger.debug(
            (
                "function called: _on_kick...\n"
                f"connection: {connection}\n"
                f"event: {event}\n"
            )
        )
        super(RasaIRCBot, self)._on_kick(connection, event)
        logger.debug("completed: _on_kick...")

    def _on_mode(self, connection, event):
        logger.debug(
            (
                "function called: _on_mode...\n"
                f"connection: {connection}\n"
                f"event: {event}\n"
            )
        )
        super(RasaIRCBot, self)._on_mode(connection, event)
        logger.debug("completed: _on_mode...")

    def _on_namreply(self, connection, event):
        logger.debug(
            (
                "function called: _on_namreply...\n"
                f"connection: {connection}\n"
                f"event: {event}\n"
            )
        )
        super(RasaIRCBot, self)._on_namreply(connection, event)
        logger.debug("completed: _on_namreply...")

    def _on_nick(self, connection, event):
        logger.debug(
            (
                "function called: _on_nick...\n"
                f"connection: {connection}\n"
                f"event: {event}\n"
            )
        )
        super(RasaIRCBot, self)._on_nick(connection, event)
        logger.debug("completed: _on_nick...")

    def _on_part(self, connection, event):
        logger.debug(
            (
                "function called: _on_part...\n"
                f"connection: {connection}\n"
                f"event: {event}\n"
            )
        )
        super(RasaIRCBot, self)._on_part(connection, event)
        logger.debug("completed: _on_part...")

    def _on_quit(self, connection, event):
        logger.debug(
            (
                "function called: _on_quit...\n"
                f"connection: {connection}\n"
                f"event: {event}\n"
            )
        )
        super(RasaIRCBot, self)._on_quit(connection, event)
        logger.debug("completed: _on_quit...")

    def on_ctcp(self, connection, event):
        """
        https://github.com/jaraco/irc/blob/1331ba85b5d093f06304d316a03a832959eaf4da/irc/bot.py#L329-L345
        """
        logger.debug(
            (
                "handler called: on_ctcp...\n"
                f"connection: {connection}\n"
                f"event: {event}\n"
            )
        )
        super(RasaIRCBot, self).on_ctcp(connection, event)
        logger.debug("completed: on_ctcp...")

    def on_dccchat(self, connection, event):
        """
        https://github.com/jaraco/irc/blob/1331ba85b5d093f06304d316a03a832959eaf4da/irc/bot.py#L347-L348
        """
        logger.debug(
            (
                "handler called: on_dccchat...\n"
                f"connection: {connection}\n"
                f"event: {event}\n"
            )
        )
        super(RasaIRCBot, self).on_dccchat(connection, event)
        logger.debug("completed: super on_dccchat...")
        logger.debug("doing RasaIRCBot.on_dccchat...")
        if len(event.arguments) != 2:
            return
        args = event.arguments[1].split()
        if len(args) == 4:
            try:
                address = ip_numstr_to_quad(args[2])
                port = int(args[3])
            except ValueError:
                return
            self.dcc_connect(address, port)
        logger.debug("compelted on_dccchat...")

    def start(self):
        """
        https://github.com/jaraco/irc/blob/1331ba85b5d093f06304d316a03a832959eaf4da/irc/bot.py#L350-L353
        """
        logger.debug("starting bot...")
        super(RasaIRCBot, self).start()
        logger.debug("started bot!!!")

    def on_nicknameinuse(self, connection, event):
        logger.debug(
            (
                "handler called: on_nicknameinuse...\n"
                f"connection: {connection}\n"
                f"event: {event}\n"
            )
        )
        connection.nick(connection.get_nickname() + "_")

    def on_welcome(self, connection, event):
        logger.debug(
            (
                "handler called: on_welcome...\n"
                f"connection: {connection}\n"
                f"event: {event}\n"
            )
        )
        connection.join(self.channel)

    def on_privmsg(self, connection, event):
        logger.debug(
            (
                "handler called: on_privmsg...\n"
                f"connection: {connection}\n"
                f"event: {event}\n"
            )
        )
        self.do_command(event, event.arguments[0])

    def on_pubmsg(self, connection, event):
        logger.debug(
            (
                "handler called: on_pubmsg...\n"
                f"connection: {connection}\n"
                f"event: {event}\n"
            )
        )
        a = event.arguments[0].split(":", 1)
        if len(a) > 1 and irc.strings.lower(a[0]) == irc.strings.lower(
            self.connection.get_nickname()
        ):
            self.do_command(event, a[1].strip())
        return

    def on_dccmsg(self, connection, event):
        logger.debug(
            (
                "handler called: on_dccmsg...\n"
                f"connection: {connection}\n"
                f"event: {event}\n"
            )
        )
        # non-chat DCC messages are raw bytes; decode as text
        text = event.arguments[0].decode("utf-8")
        connection.privmsg("You said: " + text)

    def do_command(self, event, command):
        logger.debug(
            (
                "function called: do_command...\n"
                f"command: {command}\n"
                f"event: {event}\n"
            )
        )
        nick = event.source.nick
        c = self.connection

        if command == "disconnect":
            self.disconnect()
        elif command == "die":
            self.die()
        elif command == "stats":
            for chname, chobj in self.channels.items():
                c.notice(nick, "--- Channel statistics ---")
                c.notice(nick, "Channel: " + chname)
                users = sorted(chobj.users())
                c.notice(nick, "Users: " + ", ".join(users))
                opers = sorted(chobj.opers())
                c.notice(nick, "Opers: " + ", ".join(opers))
                voiced = sorted(chobj.voiced())
                c.notice(nick, "Voiced: " + ", ".join(voiced))
        elif command == "dcc":
            dcc = self.dcc_listen()
            c.ctcp(
                "DCC",
                nick,
                "CHAT chat %s %d"
                % (ip_quad_to_numstr(dcc.localaddress), dcc.localport),
            )
        elif command == "hello":  # Foaad: change this
            c.privmsg(self.channel, "well double hello to you too!")
        elif command == "about":  # Foaad: add your name
            c.privmsg(
                self.channel,
                "I was made by Dr. Foaad Khosmood for the CPE 466 class in Spring 2016. I was furthere modified by _____",
            )
        elif command == "usage":
            # Foaad: change this
            c.privmsg(self.channel, "I can answer questions like this: ....")
        else:
            c.notice(nick, "Not understood: " + command)


def ensure_hashtag_channel(ch_name):
    return f"#{ch_name}" if ch_name[0] != "#" else ch_name


def print_usage():
    print("Usage: irc_worker <server[:port]> <channel> <nickname>")
    print()
    print("Usage: irc_worker <nickname>")
    print()
    print(f"\tserver default: {IRC_SERVER}")
    print(f"\tport default: {IRC_PORT}")
    print(f"\tchannel default: {IRC_CHANNEL}")
    print()


def exit_usage():
    print_usage()
    sys.exit(1)


def main():
    logger.setLevel(10)

    if len(sys.argv) <= 1:
        exit_usage()
    elif len(sys.argv) == 2:
        print_usage()
        nickname = sys.argv[1]
        channel = IRC_CHANNEL
        server = IRC_SERVER
        port = int(IRC_PORT)
    elif len(sys.argv) == 4:
        url = sys.argv[1]
        server, port = url.split(":", 1) if ":" in url else (url, IRC_PORT)
        port = int(port)
        channel = sys.argv[2]
        nickname = sys.argv[3]
    else:
        exit_usage()

    channel = ensure_hashtag_channel(channel)
    logger.info(
        (
            "\n\tinitalizing with:\n"
            f"\t\tchannel = {channel}\n"
            f"\t\tnickname = {nickname}\n"
            f"\t\tserver = {server}\n"
            f"\t\tport = {port}\n"
        )
    )
    bot = RasaIRCBot(channel=channel, nickname=nickname, server=server, port=port)
    bot.start()


if __name__ == "__main__":
    main()
