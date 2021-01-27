import statistics


class EmailAlert:
    def __init__(self):
        self.emailSent = False

    def trigger(self):
        self.emailSent = True


class LEDAlert:
    def __init__(self):
        self.ledGlows = False

    def trigger(self):
        self.ledGlows = True


class StatsAlerter:
    def __init__(self, maxThreshold, alertObjects):
        self.maxThreshold = maxThreshold
        self.alertObjects = alertObjects

    def checkAndAlert(self, numbers):
        computedStats = statistics.calculateStats(numbers)
        if computedStats["max"] > self.maxThreshold:
            for obj in self.alertObjects:
                obj.trigger()
