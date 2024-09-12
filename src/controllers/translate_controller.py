from flask import Blueprint, render_template, request
from deep_translator import GoogleTranslator
from models.language_model import LanguageModel
from models.history_model import HistoryModel

translate_controller = Blueprint("translate_controller", __name__)


@translate_controller.route("/", methods=["GET", "POST"])
def index(translate_from="pt", translate_to="en"):
    text_to_translate = "O que deseja traduzir?"
    translated = "What do you want to translate?"

    # Se o método for POST, realiza a tradução
    if request.method == "POST":
        text_to_translate = request.form["text-to-translate"]
        translate_from = request.form["translate-from"]
        translate_to = request.form["translate-to"]

        # Utiliza o GoogleTranslator para realizar a tradução
        translated = GoogleTranslator(
            source=translate_from, target=translate_to
        ).translate(text_to_translate)

        # Salva o histórico da tradução
        HistoryModel(
            {
                "text_to_translate": text_to_translate,
                "translate_from": translate_from,
                "translate_to": translate_to,
            }
        ).save()

    # Renderiza o template com as variáveis necessárias
    return render_template(
        "index.html",
        languages=LanguageModel.list_dicts(),  # Lista de idiomas
        text_to_translate=text_to_translate,  # Texto de origem
        translated_from=translate_from,  # Idioma de origem
        translated_to=translate_to,  # Idioma de destino
        translated=translated,  # Texto traduzido
    )
