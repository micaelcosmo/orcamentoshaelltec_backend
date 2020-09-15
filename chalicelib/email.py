import boto3
from botocore.exceptions import ClientError


class EmailSender:

    def enviar_email(self, orcamento):

        sender = "HaellTec <haelltec@gmail.com>"

        recipient = orcamento.email

        aws_region = "sa-east-1"

        subject = "Resposta de orçamento HaellTec."

        # The email body for recipients with non-HTML email clients.
        body_text = "orcamento. \nitem 1 \t {{orcamento.}}"

        body_html = self.ler_template(orcamento)

        # The character encoding for the email.
        charset = "UTF-8"

        # Create a new SES resource and specify a region.
        client = boto3.client('ses', region_name=aws_region)

        # Try to send the email.
        try:
            # Provide the contents of the email.
            response = client.send_email(
                Destination={
                    'ToAddresses': [
                        recipient,
                        # TODO adicionar atendentes
                    ],
                },
                Message={
                    'Body': {
                        'Html': {
                            'Charset': charset,
                            'Data': body_html,
                        },
                        'Text': {
                            'Charset': charset,
                            'Data': body_text,
                        },
                    },
                    'Subject': {
                        'Charset': charset,
                        'Data': subject,
                    },
                },
                Source=sender,
            )
        # Display an error if something goes wrong.
        except ClientError as e:
            print(e.response['Error']['Message'])
        else:
            print("Email sent! Message ID:"),
            print(response['MessageId'])

    def ler_template(self, orcamento: object) -> str:
        # implementa logica de leitura do template
        # substituir valores pelos reais (replace)
        pass
