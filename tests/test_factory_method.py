from patterns.factory_method import NotificationFactory, NotificationTypeEnum


def test_factory_method():
    factory = NotificationFactory()

    email_notification = factory.create_notification(NotificationTypeEnum.EMAIL)
    email_notification.notify("Hello via Email!")

    sms_notification = factory.create_notification(NotificationTypeEnum.SMS)
    sms_notification.notify("Hello via SMS!")
