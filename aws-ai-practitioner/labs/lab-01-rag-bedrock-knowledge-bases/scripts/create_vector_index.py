"""Crea el índice vectorial que usará la Knowledge Base de Amazon Bedrock.

Uso:
    python create_vector_index.py --endpoint <id>.<region>.aoss.amazonaws.com \
        --region us-east-1 --index bedrock-kb-index

La identidad que ejecuta el script debe figurar en la data access policy de la
colección (aoss:CreateIndex) y tener aoss:APIAccessAll sobre la colección.
"""

import argparse
import sys
import time

import boto3
from opensearchpy import AWSV4SignerAuth, OpenSearch, RequestsHttpConnection
from opensearchpy.exceptions import AuthorizationException, RequestError

# Nombres de campo que se pasan después en --storage-configuration de la KB.
VECTOR_FIELD = "bedrock-knowledge-base-default-vector"
TEXT_FIELD = "AMAZON_BEDROCK_TEXT_CHUNK"
METADATA_FIELD = "AMAZON_BEDROCK_METADATA"

# Amazon Titan Text Embeddings V2 genera vectores de 1024 dimensiones por defecto.
EMBEDDING_DIMENSION = 1024


def build_client(endpoint: str, region: str) -> OpenSearch:
    credentials = boto3.Session().get_credentials()
    auth = AWSV4SignerAuth(credentials, region, "aoss")
    return OpenSearch(
        hosts=[{"host": endpoint.replace("https://", ""), "port": 443}],
        http_auth=auth,
        use_ssl=True,
        verify_certs=True,
        connection_class=RequestsHttpConnection,
        timeout=300,
    )


def index_body() -> dict:
    return {
        "settings": {"index": {"knn": True, "knn.algo_param.ef_search": 512}},
        "mappings": {
            "properties": {
                VECTOR_FIELD: {
                    "type": "knn_vector",
                    "dimension": EMBEDDING_DIMENSION,
                    "method": {
                        "name": "hnsw",
                        "engine": "faiss",
                        "space_type": "l2",
                        "parameters": {"ef_construction": 512, "m": 16},
                    },
                },
                TEXT_FIELD: {"type": "text"},
                METADATA_FIELD: {"type": "text", "index": False},
            }
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--endpoint", required=True, help="Endpoint de la colección, sin https://")
    parser.add_argument("--region", required=True)
    parser.add_argument("--index", default="bedrock-kb-index")
    parser.add_argument("--retries", type=int, default=6, help="Reintentos mientras se propaga la data access policy")
    args = parser.parse_args()

    client = build_client(args.endpoint, args.region)

    for attempt in range(1, args.retries + 1):
        try:
            if client.indices.exists(index=args.index):
                print(f"El índice '{args.index}' ya existe; no se realizan cambios.")
                return 0
            client.indices.create(index=args.index, body=index_body())
            print(f"Índice '{args.index}' creado correctamente.")
            # La KB valida el índice al crearse: damos margen a que quede disponible.
            time.sleep(30)
            return 0
        except AuthorizationException as exc:
            # Las data access policies de OpenSearch Serverless tardan en propagarse.
            print(f"[{attempt}/{args.retries}] 403 al crear el índice, reintentando en 20 s: {exc.error}")
            time.sleep(20)
        except RequestError as exc:
            print(f"Error en la petición: {exc.info}", file=sys.stderr)
            return 1

    print("No se pudo crear el índice: revisa la data access policy y el principal.", file=sys.stderr)
    return 1


if __name__ == "__main__":
    sys.exit(main())
