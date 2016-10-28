from pytocl.car import State, Command, MPS_PER_KMH
from pytocl.lane import Lane


class Dynamic:

    def __init__ (self):
        self.speed = 0

        # out
        self.accelerator = 0
        self.gear = 0
        self.brake = 0
        self.steering = 0

        self.steerCorrection = 0

    def correctGear(self, carstate):
        self.gear = carstate.gear or 1
        if carstate.rpm > 7000 and carstate.gear < 6:
            # _logger.info('switching up')
            self.gear = carstate.gear + 1
        elif carstate.rpm < 2000 and carstate.gear > 1:
            # _logger.info('switching down')
            self.gear = carstate.gear - 1

    def simple(self, carstate, mylane: Lane):

        # dummy steering control:
        #
        speed = mylane.velocity()

        angle = mylane.angle()

        dSpeed = speed - carstate.speed_x
        self.gear = carstate.gear

        if ((speed < 0) and (speed < carstate.speed_x)):
            self.accelerator = 1
            self.gear = -1
            print("REVERSE g %f  a%  s %f" % (self.gear,self.accelerator,carstate.speed_x))
        else:
            if (self.gear == -1): self.gear = 1
            #bremsen
            if (dSpeed < 0):
                dSpeedFactor = (100/carstate.speed_x) * speed
            # hart bremsen
                if (dSpeedFactor < 25):
                    self.brake = 1
                    print("BRAKE HARD")
            # mittel
                elif (dSpeedFactor >= 25) and (dSpeedFactor < 70):
                    self.brake = 0.8
                    print("BRAKE MID")
            # sanft bremsen
                elif (dSpeedFactor >=70) and (dSpeedFactor <94):
                    self.brake = 0.4
                    print("BRAKE LIGHT")
                else :
                    print("BRAKE NO")
            else :
                self.brake = 0
            self.accelerate(speed, carstate)


       # print ("%f -> x %f  y %f" % (speed, carstate.speed_x, carstate.speed_y))


        # if ((carstate.distance_from_center < -0.2) or (carstate.distance_from_center > 0.2)):
        #     self.steerCorrection = 1
        #
        # if (self.steerCorrection == 1) :
        #     self.steering = (carstate.angle - carstate.distance_from_center * 0.2)
        #
        # if (carstate.distance_from_center == 0):
        #         self.steerCorrection = 0

        if (angle == 500):
            self.steering = (carstate.angle - carstate.distance_from_center * 0.2)
        else:
            self.steering = (-1)*angle/77



       # self.accelerator = min(1, self.accelerator)
       # self.accelerator = max(-1, self.accelerator)

        # _logger.info('accelerator: {}'.format(command.accelerator))

        # gear shifting:
        #_logger.info('rpm, gear: {}, {}'.format(carstate.rpm, carstate.gear))


        if carstate.rpm > 8000 and carstate.gear < 6:
            # _logger.info('switching up')
            self.gear = carstate.gear + 1
        elif carstate.rpm < 2700 and carstate.gear > 1:
            #_logger.info('switching down')
            self.gear = carstate.gear -1

    def accelerate (self, speed, carstate : State):

        if (speed > carstate.speed_x):
            if abs(carstate.speed_y) >= 0:
                self.accelerator += 1
            else:
                self.accelerator -= 0.5
        else:
            self.accelerator -= 0.7
