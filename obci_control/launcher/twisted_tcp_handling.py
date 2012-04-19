#!/usr/bin/python
# -*- coding: utf-8 -*-

from twisted.protocols.basic import NetstringReceiver
from twisted.internet.protocol import Factory
from twisted.internet import reactor

import zmq
import socket
import threading

from common.message import OBCIMessageTool, send_msg, recv_msg, PollingObject
from launcher.launcher_messages import message_templates, error_codes

from common.obci_control_settings import PORT_RANGE
import common.net_tools as net

class OBCIProxy(NetstringReceiver):

    def stringReceived(self, string):
        req_sock = self.factory.ctx.socket(zmq.REQ)
        req_sock.connect(self.factory.zmq_rep_addr)
        req = unicode(string, encoding='utf-8')
        print "twisted got:", req

        parsed = self.factory.mtool.unpack_msg(req)
        if parsed.type == 'find_eeg_experiments' or parsed.type == 'find_eeg_amplifiers'\
            or parsed.type == 'start_eeg_signal':
            pull_addr = 'tcp://' + socket.gethostname() + ':' + str(self.factory.pull_port)
            parsed.client_push_address = pull_addr

        send_msg(req_sock, parsed.SerializeToString())

        pl = PollingObject()
        msg, det = pl.poll_recv(req_sock, timeout=5000)
        if not msg:
            msg = self.factory.mtool.fill_msg("rq_error", details=det)

        if parsed.type == 'find_eeg_experiments' or parsed.type == 'find_eeg_amplifiers'\
            or parsed.type == 'start_eeg_signal':
            msg, det = pl.poll_recv(self.factory.pull_sock, timeout=20000)
            if not msg:
                msg = self.factory.mtool.fill_msg("rq_error", details=det)
                return

        encmsg = msg.encode('utf-8')
        self.sendString(encmsg)
        reactor.callFromThread(self.sendString, encmsg)



class OBCIProxyFactory(Factory):
    protocol = OBCIProxy

    def __init__(self, address, zmq_ctx, zmq_rep_addr):
        self.srv_address = address
        self.ctx = zmq_ctx
        self.zmq_rep_addr = zmq_rep_addr
        self.pull_sock = self.ctx.socket(zmq.PULL)
        self.pull_port = self.pull_sock.bind_to_random_port('tcp://*',
                                            min_port=PORT_RANGE[0],
                                            max_port=PORT_RANGE[1], max_tries=500)
        self.mtool = OBCIMessageTool(message_templates)


def run_twisted_server(address, zmq_ctx, zmq_rep_addr):
    fact = OBCIProxyFactory(address, zmq_ctx, zmq_rep_addr)
    port = reactor.listenTCP(address[1], fact)
    port = port.getHost().port
    fact.srv_address = (address[0], port)
    thr = threading.Thread(target=reactor.run, args=[False])
    thr.daemon = True
    thr.start()
    print "Twisted: listening on port", port
    return thr, port

if __name__ == '__main__':
    run_twisted_server(('0.0.0.0', 12013), zmq.Context(), 'tcp://127.0.0.1:54654')
    print "twisted: server started."
