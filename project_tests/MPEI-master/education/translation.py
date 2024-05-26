from modeltranslation import translator
from . import models

@translator.register(models.Faculty)
class FacultyTranslation(translator.TranslationOptions):
    fields = ('name',)

@translator.register(models.Group)
class GroupTranslation(translator.TranslationOptions):
    fields = ('name',)

@translator.register(models.EduProgram)
class EduProgramTranslation(translator.TranslationOptions):
    fields = ('text',)

@translator.register(models.TreResults)
class TreResultsTranslation(translator.TranslationOptions):
    fields = ('text',)

@translator.register(models.AdditionalEdu)
class AdditionalEduTranslation(translator.TranslationOptions):
    fields = ('text',)

@translator.register(models.DistanceEdu)
class DistanceEduTranslation(translator.TranslationOptions):
    fields = ('text',)

@translator.register(models.EmpAndInternship)
class EmpAndInternshipTranslation(translator.TranslationOptions):
    fields = ('text',)

@translator.register(models.FinalQua)
class FinalQuaTranslation(translator.TranslationOptions):
    fields = ('text',)

@translator.register(models.OfficialDocs)
class OfficialDocsTranslation(translator.TranslationOptions):
    fields = ('text',)

