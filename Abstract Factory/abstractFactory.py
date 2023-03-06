from __future__ import annotations
from abc import ABC, abstractmethod


class VideoAbstract(ABC):
    def assistir(self):
        """iniciar video"""

    def enviar_email(self, text):
        """enviar o arquivo por email com o texto"""

    def salvar(self):
        """salvar video no sistema arquivo"""


class VideoAndroid(VideoAbstract):
    """compartilhar video por sistema android"""

    def assistir(self):
        print("\n---Iniciado video no android---\n")

    def enviar_email(self, text):
        print(f"\n(Android)Video enviado por email com texto: \n{text}.\n")

    def salvar(self):
        print("Video salvo no Android.")


class VideoIos(VideoAbstract):
    """Compartilhar video por IOS"""

    def assistir(self):
        print("\n---Iniciado video no ios---\n")

    def enviar_email(self, text):
        print(f"\n(IOS)Video enviado por email como texto: \n{text}.\n")

    def salvar(self):
        print("Video salvo no IOS.")


class AudioAbstract(ABC):
    def ouvir(selft):
        """Iniciar audio."""

    def salvar(self):
        """Salvar audio no sistema arquivo."""


class AudioAndroid(VideoAbstract):
    """Compartilhar audio por sistema android."""

    def ouvir(selft):
        print("\n--Iniciado audio no android--\n")

    def salvar(self):
        print("\nAudio salvo no android.\n")


class AudioIos(VideoAbstract):
    """Compartilhar audio por IOS."""

    def ouvir(selft):
        print("\n--Iniciado audio no ios--\n")

    def salvar(self):
        print("\nAudio salvo no IOS.\n")


class ExporterFactory(ABC):
    @abstractmethod
    def pegar_video(self) -> VideoAbstract:
        """pegar video"""

    def pegar_audio(self) -> AudioAbstract:
        """pegar audio"""


class MidiaAndroid(ExporterFactory):
    def pegar_video(self) -> VideoAbstract:
        return VideoAndroid()

    def pegar_audio(self) -> AudioAbstract:
        return AudioAndroid()


class MidiaIos(ExporterFactory):
    def pegar_video(self) -> VideoAbstract:
        return VideoIos()

    def pegar_audio(self) -> AudioAbstract:
        return AudioIos()


def iniciar() -> ExporterFactory:
    factories = {
        "android": MidiaAndroid(),
        "ios": MidiaIos(),
    }
    while True:
        export_quality = input("Qual sistema: (android, ios): ")
        if export_quality in factories:
            return factories[export_quality]
        print(f"Opcao desconhecida: {export_quality}.")


if __name__ == "__main__":
    factory = iniciar()

    video = factory.pegar_video()
    audio = factory.pegar_audio()

    video.assistir()
    video.enviar_email("OI")

    audio.ouvir()
