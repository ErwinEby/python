import pytest
from television import *

class Test:
    def setup_method(self):
        self.tverwin = Television()

    def teardown_method(self):
        del self.tverwin

    def test_init(self):
        assert self.tverwin.__str__() == 'Power = False, Channel = 0, Volume = 0'

    def testPower(self):
        assert self.tverwin.__str__() == 'Power = False, Channel = 0, Volume = 0'
        self.tverwin.power()
        assert self.tverwin.__str__() == 'Power = True, Channel = 0, Volume = 0'

    def testMute(self):
        self.tverwin.power()
        self.tverwin.volume_up()
        self.tverwin.mute()
        assert self.tverwin.__str__() == 'Power = True, Channel = 0, Volume = 0'
        self.tverwin.mute()
        assert self.tverwin.__str__() == 'Power = True, Channel = 0, Volume = 1'
        self.tverwin.mute()
        self.tverwin.power()
        assert self.tverwin.__str__() == 'Power = False, Channel = 0, Volume = 0'
        self.tverwin.mute()
        assert self.tverwin.__str__() == 'Power = False, Channel = 0, Volume = 0'

    def testChannelUp(self):
        self.tverwin.channel_up()
        assert self.tverwin.__str__() == 'Power = False, Channel = 0, Volume = 0'
        self.tverwin.power()
        self.tverwin.channel_up()
        assert self.tverwin.__str__() == 'Power = True, Channel = 1, Volume = 0'
        self.tverwin.channel_up()
        self.tverwin.channel_up()
        self.tverwin.channel_up()
        assert self.tverwin.__str__() == 'Power = True, Channel = 0, Volume = 0'

    def testChannelDown(self):
        self.tverwin.channel_down()
        assert self.tverwin.__str__() == 'Power = False, Channel = 0, Volume = 0'
        self.tverwin.power()
        self.tverwin.channel_down()
        assert self.tverwin.__str__() == 'Power = True, Channel = 3, Volume = 0'

    def testVolumeUp(self):
        self.tverwin.volume_up()
        assert self.tverwin.__str__() == 'Power = False, Channel = 0, Volume = 0'
        self.tverwin.power()
        self.tverwin.volume_up()
        assert self.tverwin.__str__() == 'Power = True, Channel = 0, Volume = 1'
        self.tverwin.mute()
        self.tverwin.volume_up()
        assert self.tverwin.__str__() == 'Power = True, Channel = 0, Volume = 2'
        self.tverwin.mute()
        self.tverwin.volume_up()
        self.tverwin.volume_up()
        assert self.tverwin.__str__() == 'Power = True, Channel = 0, Volume = 2'

    def testVolumeDown(self):
        self.tverwin.volume_down()
        assert self.tverwin.__str__() == 'Power = False, Channel = 0, Volume = 0'
        self.tverwin.power()
        self.tverwin.volume_up()
        self.tverwin.volume_up()
        self.tverwin.volume_up()
        self.tverwin.volume_up()
        self.tverwin.volume_down()
        assert self.tverwin.__str__() == 'Power = True, Channel = 0, Volume = 1'
        self.tverwin.mute()
        self.tverwin.volume_down()
        assert self.tverwin.__str__() == 'Power = True, Channel = 0, Volume = 0'
        self.tverwin.mute()
        self.tverwin.volume_down()
        self.tverwin.volume_down()
        self.tverwin.volume_down()
        assert self.tverwin.__str__() == 'Power = True, Channel = 0, Volume = 0'


