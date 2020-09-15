import boto3
from botocore.exceptions import ClientError

class EmailSender:

    def enviar_email(self, orcamento):

        SENDER = "HaellTec <haelltec@gmail.com>"

        RECIPIENT = orcamento.email

        AWS_REGION = "sa-east-1"

        SUBJECT = "Resposta de orçamento HaellTec."

        # The email body for recipients with non-HTML email clients.
        BODY_TEXT = ("orcamento. \nitem 1 \t {{orcamento.}}")

        BODY_HTML = self.ler_template(orcamento)

        # The character encoding for the email.
        CHARSET = "UTF-8"

        # Create a new SES resource and specify a region.
        client = boto3.client('ses', region_name=AWS_REGION)

        # Try to send the email.
        try:
            # Provide the contents of the email.
            response = client.send_email(
                Destination={
                    'ToAddresses': [
                        RECIPIENT,
                        #TODO adicionar atendentes
                    ],
                },
                Message={
                    'Body': {
                        'Html': {
                            'Charset': CHARSET,
                            'Data': BODY_HTML,
                        },
                        'Text': {
                            'Charset': CHARSET,
                            'Data': BODY_TEXT,
                        },
                    },
                    'Subject': {
                        'Charset': CHARSET,
                        'Data': SUBJECT,
                    },
                },
                Source=SENDER,
            )
        # Display an error if something goes wrong.
        except ClientError as e:
            print(e.response['Error']['Message'])
        else:
            print("Email sent! Message ID:"),
            print(response['MessageId'])

    def ler_template(orcamento):
        #implementa logica de leitura do template
        #substituir valores pelos reais (replace)
        pass

