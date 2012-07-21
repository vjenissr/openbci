#!/usr/bin/env python
# -*- coding: utf-8 -*-


from multiplexer.multiplexer_constants import peers, types
from obci_control.peer.configured_multiplexer_server import ConfiguredMultiplexerServer
from obci_configs import settings, variables_pb2
import random, time, sys

from interfaces.etr import etr_ugm_manager
from gui.ugm import ugm_helper
from interfaces import interfaces_logging as logger

import numpy as np

LOGGER = logger.get_logger("etr_analysis", "debug")


class EtrAnalysis(ConfiguredMultiplexerServer):
    def __init__(self, addresses):
        super(EtrAnalysis, self).__init__(addresses=addresses,
                                     type=peers.ETR_P300_ANALYSIS)


        self.initConstants()
        self.ready()

    def initConstants(self):
        """
        Initiates constants values.
        """
        self.areaCount = int(self.get_param('speller_area_count'))
        print "self.areaCount: ", self.areaCount

        self.nCount = 0
        self.nRefresh = 10
        
        bufforLen = 30
        self.buffor = np.zeros((2,bufforLen))
        self.metricBuffor = np.zeros((self.areaCount, bufforLen))
        
        self.feeds = [0]*self.areaCount

        start_id = self.get_param('ugm_field_ids').split(';')[0]
        self.ugm_mgr = etr_ugm_manager.EtrUgmManager(
            self.get_param('ugm_config'),
            self.get_param('speller_area_count'),
            start_id,
            self.get_param('fix_id')
            )
        
        cX, cY = self.ugm_mgr.get_area_centres()
        self.cX = np.array(cX)
        self.cY = np.array(cY)

    def _update_heatmap(self, m):
        """
        Updates values of heatmap and creates probabilty 
        density for each epoch.
        """
        m = np.array(m)
        m = np.exp(-m)
        self.metricBuffor = np.hstack((self.metricBuffor[:,1:],m[np.newaxis].T))
    
    def _calc_pdf(self):
        self.pdf = np.sum(self.metricBuffor, axis=1)
        #~ self.pdf = self.pdf/np.sum(self.pdf)
        
        return self.pdf

    def _getPdf(self):
        """
        Returns Probability Density Function based on heatmap
        made of last nLast distances.
        """
        return self.pdf

    
    def _update_buffor(self, xy):
        """
        Updates buffor of gaze values.
        """
        self.buffor = np.concatenate( (self.buffor, xy), axis=1)[:,1:]
    
    def _calc_metric(self, x, y):
        return np.sqrt((self.cX-x)**4 + (self.cY-y)**4)
        
    def handle_message(self, mxmsg):
        LOGGER.info("EtrAnalysis\n")
        if mxmsg.type == types.ETR_CALIBRATION_RESULTS:
        #### What to do when receive ETR_MATRIX information
            res = variables_pb2.Sample()
            res.ParseFromString(mxmsg.message)
            LOGGER.debug("GOT ETR CALIBRATION RESULTS: "+str(res.channels))


        elif mxmsg.type == types.ETR_SIGNAL_MESSAGE:
        #### What to do when receive ETR_SIGNAL information
            msg = variables_pb2.Sample2D()
            msg.ParseFromString(mxmsg.message)
            LOGGER.debug("GOT MESSAGE: "+str(msg))

            # Save positions
            x, y = msg.x, msg.y            
            self._update_buffor(np.array([[x],[y]]))

            # Turn position into heatmap
            m = self._calc_metric(x,y)
            self._update_heatmap(m)
            
            # Calc heatmap as probabilty density
            pdf = self._calc_pdf()
            
            ugm = self.ugm_mgr.get_ugm_updates(self.feeds, msg)
            ugm_helper.send_config(self.conn, ugm, 1)
            
            self.nCount += 1
            
            if self.nCount & self.nRefresh == 0:
                self._send_results()
            
        #~ elif mxmsg.type == types.BLINK_MESSAGE:
        #### What to do when receive BLINK_NO information
            #~ blink = variables_pb2.Blink()
            #~ blink.ParseFromString(mxmsg.message)
            #~ LOGGER.debug("GOT BLINK: "+str(blink.index)+" / "+str(blink.timestamp))
            

        self.no_response()

    def _send_results(self):
        """
        Sends results do decision making module.
        """
        pdf = self._getPdf()
        
        r = variables_pb2.Sample()
        r.timestamp = time.time()
        for i in range(self.areaCount):
            r.channels.append(pdf[i])
        self.conn.send_message(message = r.SerializeToString(), type = types.ETR_ANALYSIS_RESULTS, flush=True)
        
        # Zastanowic sie, czy nie bedzie lekkiej desynchronizacji miedzy probkami


if __name__ == "__main__":
    EtrAnalysis(settings.MULTIPLEXER_ADDRESSES).loop()
