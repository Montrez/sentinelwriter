import requests

def generate_threat_report(log_data: str) -> str:
    prompt = f"Generate a cybersecurity incident report from these logs:\n{log_data}"

    response = requests.post(
        "http://host.docker.internal:11434/api/generate",
        json={
            "model": "llama3",
            "prompt": prompt,
            "stream": False
        }
    )

    return response.json()["response"].strip()
