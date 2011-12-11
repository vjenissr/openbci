#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author:
#     Mateusz Kruszyński <mateusz.kruszynski@gmail.com>


from multiplexer.multiplexer_constants import peers, types
from multiplexer.clients import connect_client
import configurer
import variables_pb2
import time

from openbci.ugm import ugm_logging as logger
LOGGER = logger.get_logger("ugm_blinking_connection", "debug")

class UgmBlinkingConnection(object):
    """Provides connection for engine to 'external' wold - other MX modules."""
    def __init__(self, addresses):
        self.connection = connect_client(type = peers.UGM_ENGINE, addresses=addresses)
        self.configurer = configurer.Configurer(addresses)
        self.blink_msg = variables_pb2.Blink()

    def get_configs(self, configs):
        return self.configurer.get_configs(configs)

    def send_blink(self, blink_id, blink_time):
        self.blink_msg.index = blink_id
        self.blink_msg.timestamp = blink_time
        self.connection.send_message(message = self.blink_msg.SerializeToString(), type = types.BLINK_MESSAGE, flush=True)

    def send_blinking_started(self):
        LOGGER.debug("Send blink started")
        msg = variables_pb2.Variable()
        msg.key = "blinking_started"
        msg.value = str(time.time())
        self.connection.send_message(message = msg.SerializeToString(), type = types.UGM_ENGINE_MESSAGE, flush=True)

    def send_blinking_stopped(self):
        LOGGER.debug("Send blinking stopped")
        msg = variables_pb2.Variable()
        msg.key = "blinking_stopped"
        msg.value = str(time.time())
        self.connection.send_message(message = msg.SerializeToString(), type = types.UGM_ENGINE_MESSAGE, flush=True)

    def send_mouse_event(self, button_nr):
        msg = variables_pb2.Variable()
        msg.key = "mouse_event"
        msg.value = str(button_nr)
        self.connection.send_message(message = msg.SerializeToString(), type = types.UGM_ENGINE_MESSAGE, flush=True)

    def send_keyboard_event(self, key):
        msg = variables_pb2.Variable()
        msg.key = "keybord_event"
        msg.value = str(key)
        self.connection.send_message(message = msg.SerializeToString(), type = types.UGM_ENGINE_MESSAGE, flush=True)

        


