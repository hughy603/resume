from django.apps import AppConfig


class ResumeConfig(AppConfig):
    name = 'resume.resume'
    verbose_name = "Resume"

    def ready(self):
        """Override this to put in:
            Users system checks
            Users signal registration
        """
        pass
