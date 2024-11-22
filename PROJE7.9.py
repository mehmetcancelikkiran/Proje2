from abc import ABC, abstractmethod

class Controllable(ABC):
    
    def turn_on(self):
        pass

    
    def turn_off(self):
        pass

    
    def get_status(self):
        pass

class Appliance(Controllable):
    def __init__(self, name):
        self.name = name
        self.is_on = False

    def turn_on(self):
        self.is_on = True
        print(f"{self.name} açıldı.")

    def turn_off(self):
        self.is_on = False
        print(f"{self.name} kapatıldı.")

    def get_status(self):
        status = "açık" if self.is_on else "kapalı"
        print(f"{self.name} durumu: {status}")


class Fan(Appliance):
    def __init__(self, name):
        super().__init__(name)

class AirConditioner(Appliance):
    def __init__(self, name):
        super().__init__(name)
        self.temperature = 24  

    def set_temperature(self, temp):
        self.temperature = temp
        print(f"{self.name} sıcaklığı {self.temperature}°C olarak ayarlandı.")

class AlarmSystem(Appliance):
    def __init__(self, name):
        super().__init__(name)
        self.alarm_triggered = False

    def trigger_alarm(self):
        self.alarm_triggered = True
        print(f"{self.name} alarmı tetiklendi!")

    def reset_alarm(self):
        self.alarm_triggered = False
        print(f"{self.name} alarmı sıfırlandı.")


class SmartHome:
    def __init__(self):
        self.appliances = []

    def add_appliance(self, appliance):
        self.appliances.append(appliance)

    def control_appliances(self):
        while True:
            print("\nCihazlar:")
            for i, appliance in enumerate(self.appliances):
                print(f"{i + 1}. {appliance.name}")

            choice = input("Cihazı kontrol etmek için numarasını seçin (çıkmak için 'q'): ")
            if choice == 'q':
                break

            try:
                appliance = self.appliances[int(choice) - 1]
            except (IndexError, ValueError):
                print("Geçersiz seçim. Lütfen tekrar deneyin.")
                continue

            action = input("Yapmak istediğiniz işlemi seçin (aç/kapat/durum/sıcaklık/alarm): ").lower()
            if action == "aç":
                appliance.turn_on()
            elif action == "kapat":
                appliance.turn_off()
            elif action == "durum":
                appliance.get_status()
            elif isinstance(appliance, AirConditioner) and action == "sıcaklık":
                temp = int(input("Yeni sıcaklığı girin: "))
                appliance.set_temperature(temp)
            elif isinstance(appliance, AlarmSystem) and action == "alarm":
                alarm_action = input("Alarmı tetiklemek için 'tetik', sıfırlamak için 'sıfırla' yazın: ").lower()
                if alarm_action == "tetik":
                    appliance.trigger_alarm()
                elif alarm_action == "sıfırla":
                    appliance.reset_alarm()
            else:
                print("Bu işlem bu cihaz için geçerli değil.")


if __name__ == "__main__":
    smart_home = SmartHome()

    # Yeni cihazlar eklendi
    smart_home.add_appliance(Fan("Oda Fanı"))
    smart_home.add_appliance(AirConditioner("Oda Klimalı"))
    smart_home.add_appliance(AlarmSystem("Ev Alarm Sistemi"))

    # Cihazları kontrol etme
    smart_home.control_appliances()
