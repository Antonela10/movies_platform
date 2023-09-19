import os
from core.wsgi import application

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))
    import bjoern

    print(f"Starting Bjoern server on 0.0.0.0:{port}")
    bjoern.run(application, "0.0.0.0", port, reuse_port=True)
