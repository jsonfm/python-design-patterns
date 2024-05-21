"""
Type: Creational Pattern
Description: It helps to hide the logic of creating objects
"""

from abc import ABC, abstractmethod
from enum import Enum


class Notification(ABC):
    @abstractmethod
    def notify(self, message: str):
        pass


class EmailNotification(Notification):
    def notify(self, message: str):
        print(f"Sending Email: {message}")


class SMSNotification(Notification):
    def notify(self, message: str):
        print(f"Sending SMS: {message}")


class NotificationTypeEnum(str, Enum):
    EMAIL = "EMAIL"
    SMS = "SMS"


class NotificationFactory:
    def create_notification(self, type: NotificationTypeEnum) -> Notification:
        if type == NotificationTypeEnum.EMAIL:
            return EmailNotification()
        elif type == NotificationTypeEnum.SMS:
            return SMSNotification()
        else:
            raise ValueError("invalid notification type")
