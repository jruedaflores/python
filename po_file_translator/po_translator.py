import polib
from deep_translator import GoogleTranslator
import logging
from .constant import LANGUAGES

log = logging.getLogger(__name__)


class po_file_translator:

    def translate(self, po_file_path, source_lang='auto', target_lang='en'):
        """
        :param po_file_path: Source PO file path
        :param source_lang: Language of the source text. The value should be one of the language codes listed in:
        'LANGUAGES'
        :param target_lang: Language to translate the source text into. The value should be one of the language codes
        listed in: 'LANGUAGES'
        :return: Save the document in the same path as the source file. '_target_lang' is added to the name.
        """
        try:
            LANGUAGES[source_lang]
        except:
            source_lang = 'auto'
        try:
            LANGUAGES[target_lang]
        except:
            source_lang = 'en'

        po = polib.pofile(po_file_path)
        for entry in po:
            if entry.msgstr or not entry.msgid:
                continue
            try:
                translation = GoogleTranslator(source=source_lang, target=target_lang).translate(entry.msgid)
                entry.msgstr = translation
            except Exception as e:
                log.error('%s %s. %s' % ("Error processing key:", entry.msgid, e))

        po_save_path = po_file_path.replace(".po", "_" + target_lang + ".po")
        po.save(po_save_path)
