from __future__ import with_statement

import boto3
from botocore.exceptions import ClientError

from datetime import datetime, timezone, timedelta


def ler_template(orcamento: dict) -> str:
    try:
        with open('chalicelib/orcamento_email_template.html') as template:
            result = template.read()
        return prencher_template(result, orcamento)
    except EnvironmentError as e:
        print('Erro ao abrir template de email')
        print(e)
        return {
            "ResponseMetadata": {
                "HTTPStatusCode": 500,
            }
        }


def prencher_template(template: str, orcamento: dict) -> str:
    return template \
        .replace("{{email}}", orcamento['email']) \
        .replace("{{data}}", agora()) \
        .replace("{{notebooks}}", str(orcamento['notebooks'])) \
        .replace("{{desktops}}", str(orcamento['desktops'])) \
        .replace("{{cobertura}}", str(orcamento['cobertura'])) \
        .replace("{{velocidade}}", str(orcamento['velocidade'])) \
        .replace("{{total}}", str(orcamento['total']))\
        .replace("{{consultor}}", orcamento['consultor'])


def now():
    return datetime.now().astimezone(timezone(timedelta(hours=-3)))


def agora() -> str:
    return now().strftime('%d/%m/%Y %H:%M')


class EmailSender:

    agora = agora()

    def enviar_email(self, orcamento: dict) -> dict:

        sender = "HaellTec Developer <micael.trabalho@hotmail.com>"

        recipient = orcamento['email']

        aws_region = "sa-east-1"

        subject = "Resposta de orçamento HaellTec."

        # The email body for recipients with non-HTML email clients.
        body_text = "orcamento"

        body_html = ler_template(orcamento)

        # The character encoding for the email.
        charset = "UTF-8"

        # Create a new SES resource and specify a region.
        client = boto3.client('ses', region_name=aws_region)

        # Try to send the email.
        try:
            # Provide the contents of the email.
            return client.send_email(
                Destination={
                    'ToAddresses': [
                        recipient,
                        # TODO adicionar atendentes
                    ],
                    'CcAddresses': [
                        sender,
                    ]
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
            return {
                "ResponseMetadata": {
                    "HTTPStatusCode": 500,
                }
            }
