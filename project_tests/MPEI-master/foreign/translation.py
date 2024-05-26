from modeltranslation import translator
from . import models

@translator.register(models.PreparingForeigners)
class PreparingForeignersTranslation(translator.TranslationOptions):
    fields = ('text',)

@translator.register(models.ForeignPrograms)
class ForeignProgramsTranslation(translator.TranslationOptions):
    fields = ('name',)

@translator.register(models.ForeignProgramDetail)
class ForeignProgramDetailTranslation(translator.TranslationOptions):
    fields = ('text',)

@translator.register(models.OrganizationCIS)
class OrganizationCISTranslation(translator.TranslationOptions):
    fields = ('text',)

@translator.register(models.Cooperation)
class CooperationTranslation(translator.TranslationOptions):
    fields = ('text',)

@translator.register(models.Graduates)
class GraduatesTranslation(translator.TranslationOptions):
    fields = ('text',)

@translator.register(models.AboutMPEIStudentsForeignPrograms)
class AboutMPEIStudentsForeignProgramsTranslation(translator.TranslationOptions):
    fields = ('text',)

@translator.register(models.Information)
class InformationTranslation(translator.TranslationOptions):
    fields = ('text',)

@translator.register(models.GlobalEnergyAssociation)
class GlobalEnergyAssociationTranslation(translator.TranslationOptions):
    fields = ('text',)

@translator.register(models.RegistrationForAMO)
class RegistrationForAMOTranslation(translator.TranslationOptions):
    fields = ('text',)