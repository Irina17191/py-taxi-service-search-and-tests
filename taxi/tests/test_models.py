from django.contrib.auth import get_user_model
from django.test import TestCase

from taxi.models import Manufacturer, Car


class ModelsTests(TestCase):
    def test_manufacturer_str(self):
        manufacturer = Manufacturer(name="Audi", country="Germany")
        self.assertEqual(str(manufacturer), "Audi Germany")

    def test_driver_str(self):
        driver = get_user_model().objects.create(
            username="test",
            password = "test123",
            first_name = "test_first",
            last_name = "test_last",
        )
        self.assertEqual(
            str(driver),
            f"{driver.username} ({driver.first_name} {driver.last_name})"
        )

    def test_car_str(self):
        manufacturer = Manufacturer.objects.create(name="Audi", country="Germany") # ForeignKey relation
        driver = get_user_model().objects.create(
            username="test",
            password="test123",
            first_name="test_first",
            last_name="test_last",
        )
        car = Car.objects.create(model="AudiQ8", manufacturer=manufacturer)
        car.drivers.add(driver)        # ManyToMany relation
        self.assertEqual(str(car), car.model)

    def test_create_driver_with_license_number(self):
        username = "test"
        password = "test123"
        license_number = "12345678"
        driver = get_user_model().objects.create_user(
            username=username,
            password=password,
            license_number=license_number,
        )
        self.assertEqual(driver.username, username)
        self.assertEqual(driver.license_number, license_number)
        self.assertTrue(driver.check_password(password))