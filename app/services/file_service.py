from pathlib import Path

from PyPDF2 import PdfReader


class FileService:

    @staticmethod
    def extract_text(file_path: str):

        path = Path(file_path)

        extension = path.suffix.lower()

        if extension == ".pdf":

            reader = PdfReader(file_path)

            text = ""

            for page in reader.pages:
                text += page.extract_text() or ""

            return text

        elif extension in [
            ".txt",
            ".py",
            ".java",
            ".js",
            ".jsx",
            ".ts",
            ".tsx",
            ".json",
            ".yaml",
            ".yml"
        ]:

            return path.read_text(
                encoding="utf-8",
                errors="ignore"
            )

        return path.read_text(
            encoding="utf-8",
            errors="ignore"
        )