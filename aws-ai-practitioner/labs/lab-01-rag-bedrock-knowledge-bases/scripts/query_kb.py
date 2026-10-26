"""Consulta una Knowledge Base de Amazon Bedrock y muestra la respuesta con sus citas.

Uso:
    python query_kb.py --kb-id ABCDEFGHIJ --model-arn <arn> "¿Cuántos días de vacaciones tengo?"
    python query_kb.py --kb-id ABCDEFGHIJ --retrieve-only "política de teletrabajo"
"""

import argparse
import sys

import boto3


def retrieve_only(client, kb_id: str, question: str, top_k: int) -> None:
    response = client.retrieve(
        knowledgeBaseId=kb_id,
        retrievalQuery={"text": question},
        retrievalConfiguration={"vectorSearchConfiguration": {"numberOfResults": top_k}},
    )
    for i, result in enumerate(response["retrievalResults"], start=1):
        uri = result["location"].get("s3Location", {}).get("uri", "n/d")
        print(f"--- Chunk {i} | score={result.get('score', 0):.4f} | {uri}")
        print(result["content"]["text"][:500], "\n")


def retrieve_and_generate(client, kb_id: str, model_arn: str, question: str, top_k: int) -> None:
    response = client.retrieve_and_generate(
        input={"text": question},
        retrieveAndGenerateConfiguration={
            "type": "KNOWLEDGE_BASE",
            "knowledgeBaseConfiguration": {
                "knowledgeBaseId": kb_id,
                "modelArn": model_arn,
                "retrievalConfiguration": {"vectorSearchConfiguration": {"numberOfResults": top_k}},
            },
        },
    )
    print("Respuesta:\n" + response["output"]["text"] + "\n")

    sources = {
        ref["location"].get("s3Location", {}).get("uri", "n/d")
        for citation in response.get("citations", [])
        for ref in citation.get("retrievedReferences", [])
    }
    print("Fuentes citadas:")
    for uri in sorted(sources) or ["(ninguna: la respuesta no se apoyó en documentos recuperados)"]:
        print(f"  - {uri}")
    # sessionId permite continuar la conversación manteniendo el contexto.
    print(f"\nsessionId: {response['sessionId']}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("question")
    parser.add_argument("--kb-id", required=True)
    parser.add_argument("--model-arn", help="ARN del modelo o inference profile generador")
    parser.add_argument("--region", default=None)
    parser.add_argument("--top-k", type=int, default=4)
    parser.add_argument("--retrieve-only", action="store_true")
    args = parser.parse_args()

    client = boto3.client("bedrock-agent-runtime", region_name=args.region)

    if args.retrieve_only:
        retrieve_only(client, args.kb_id, args.question, args.top_k)
    elif args.model_arn:
        retrieve_and_generate(client, args.kb_id, args.model_arn, args.question, args.top_k)
    else:
        parser.error("--model-arn es obligatorio salvo con --retrieve-only")
    return 0


if __name__ == "__main__":
    sys.exit(main())
