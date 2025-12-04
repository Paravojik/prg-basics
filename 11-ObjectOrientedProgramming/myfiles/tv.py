class TV:
    def __init__(self):
        self.is_on = False
        self.channel_no=1
        self.channels=[]
        self.volume=0
    def turn_off(self):
        if self.is_on==True:
            self.is_on=False
    def turn_on(self):
        if self.is_on==False:
            self.is_on=True
    
    def set_channel(self,new_channel_no):
        if self.is_on:
            self.channel_no=new_channel_no
        else:
            print("The TV is off")
    def set_channels(self, channels_lists):
        for i in channels_lists:
            self.channels.append(i)
    
    def show_channels(self):
        print("Channels list: ")
        for i in range(len(self.channels)):
            print(f'{i+1}. {self.channels[i]}')
        print()
    def increase_volume(self):
        if self.volume<10:
            self.volume+=1
    def decrease_volume(self):
        if self.volume>0:
            self.volume-=1

    


    def show_status(self):
        if self.is_on:
            statusOn="on" if self.is_on else "off"
            statusChannel=self.channels[self.channel_no] if self.channel_no<len(self.channels) else "It exceeds the list of available channels"
            print(f'The TV is {statusOn}, channel {self.channel_no} {statusChannel}, volume:{self.volume}')
        else:
            print(f'The TV is {"on" if self.is_on else "off"}')