class Television:
    MIN_VOLUME = 0
    MIN_CHANNEL = 0
    MAX_VOLUME = 2
    MAX_CHANNEL = 3
   
    def __init__(self):
        self.status = False
        self.muted = False
        self.__volume = Television.MIN_VOLUME 
        self.__channel = Television.MIN_CHANNEL

    def power(self):
        '''
        turns the television on or off
        :return: None
        '''
        
        if self.status:
            self.status = False
        else:
            self.status = True

    def mute(self):
        '''
        mutes and unmutes the television
        :return: None
        '''
        if self.status:
            if self.muted:
                self.muted = False
            else:
                self.muted = True

    def channel_up(self):
        '''
        Method that raises the channel,
        goes to the lowest channel if the
        TV is already on the highest channel
        :return: None
        '''
        if self.status:
            if self.__channel < Television.MAX_CHANNEL:
                self.__channel += 1
            else:
                self.__channel = Television.MIN_CHANNEL

    def channel_down(self):
        '''
        Method that lowers the channel,
        goes to the highest channel if the
        TV is already on the lowest channel
        :return: None
        '''
        if self.status:
            self.muted = False
            if self.__channel > Television.MIN_CHANNEL:
                self.__channel -= 1
            else:
                self.__channel = Television.MAX_CHANNEL

        
    def volume_up(self):
        '''
        method raises the volume one,
        it won't do anything if the TV is at
        max volume
        :return: None
        '''
        if self.status:
            self.muted = False
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self):
         '''
        method lowers the volume one,
        it won't do anything if the TV is at
        lowest volume
        :return: None
        '''
         if self.status:
            self.muted = False
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self):
        '''
        This prints the power status, channel, and volume
        to the console, used to test if the methods are
        working correctly
        :return: None
        '''
        self.show_volume = self.__volume
        if self.muted:
            self.show_volume = 0
        return f'Power = {self.status}, Channel = {self.__channel}, Volume = {self.show_volume}'
        



