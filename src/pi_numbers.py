from auklet.monitoring import Monitoring
from pidigits import piGenerator


def generator():
    pi_generator = piGenerator()
    for digits in range(250):
        if digits == (250-1):
            print(9 / 0)
        else:
            pi_digits = [next(pi_generator) for i in range(digits)]
            print(pi_digits)


def main():
    auklet_monitoring = Monitoring("api_key", "app_id", base_url="api-staging.auklet.io")

    auklet_monitoring.start()
    generator()
    auklet_monitoring.stop()


if __name__ == "__main__":
    main()
