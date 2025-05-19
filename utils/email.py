import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import os
import datetime


def generate_email_report(test_results, send_email=False, email_config=None, html_attachment_path=None):
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # HTML table rows for mail body
    html_rows = ""
    for result in test_results:
        color = "#28a745" if result["result"] == "PASS" else "#dc3545" if result["result"] == "FAIL" else "#ffc107"
        html_rows += f"""
        <tr>
            <td>{result['test_case']}</td>
            <td>{result['environment_url']}</td>
            <td>{result['status_code']}</td>
            <td style="color:{color}"><b>{result['result']}</b></td>
            <td>{result['error_message']}</td>
        </tr>
        """
    # HTML content for mail body
    html_body = f"""
    <html>
    <body>
        <h3>Datom API Test Suite Summary</h3>
        <p><b>Run Date:</b> {now}</p>
        <table border="1" cellpadding="5" cellspacing="0" style="border-collapse: collapse; font-family: Arial;">
            <thead style="background-color: #f2f2f2;">
                <tr>
                    <th>Test Case</th>
                    <th>Environment URL</th>
                    <th>Status Code</th>
                    <th>Result</th>
                    <th>Error Message</th>
                </tr>
            </thead>
            <tbody>
                {html_rows}
            </tbody>
        </table>
    </body>
    </html>
    """

    if send_email and email_config:
        msg = MIMEMultipart()
        msg["Subject"] = "API Test Report"
        msg["From"] = email_config["sender"]
        msg["To"] = ", ".join(email_config["recipient"])

        # Add HTML table as email body
        msg.attach(MIMEText(html_body, "html"))

        # Attach HTML report from pytest-html
        if html_attachment_path and os.path.exists(html_attachment_path):
            with open(html_attachment_path, "rb") as f:
                attachment = MIMEApplication(f.read(), _subtype="html")
                attachment.add_header("Content-Disposition", "attachment", filename=os.path.basename(html_attachment_path))
                msg.attach(attachment)

        try:
            with smtplib.SMTP(email_config["host"], email_config["port"]) as server:
                server.starttls()
                server.login(email_config["sender"], email_config["app_password"])
                server.sendmail(email_config["sender"], email_config["recipient"], msg.as_string())
                print("Email sent with HTML report attached.")
        except Exception as e:
            print("Email sending failed:", e)
