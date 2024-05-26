from modeltranslation import translator
from . import models

@translator.register(models.ScientificCouncil)
class ScientificCouncilTranslation(translator.TranslationOptions):
    fields = ('name', 'academic_degree', 'about')

@translator.register(models.UniversityManagement)
class UniversityManagementTranslation(translator.TranslationOptions):
    fields = ('text',)

@translator.register(models.MPEIuzLeaders)
class MPEIuzLeadersTranslation(translator.TranslationOptions):
    fields = ('name', 'academic_degree', 'some_text')

@translator.register(models.MPEIuzLeaderDetail)
class MPEIuzLeaderDetailTranslation(translator.TranslationOptions):
    fields = ('text',)

@translator.register(models.TheBoardOfDirectors)
class TheBoardOfDirectorsTranslation(translator.TranslationOptions):
    fields = ('name', 'academic_degree', 'position')

@translator.register(models.DepartmentsAndCenters)
class DepartmentsAndCentersTranslation(translator.TranslationOptions):
    fields = ('text',)

@translator.register(models.OfficesAndDepartments)
class OfficesAndDepartmentsTranslation(translator.TranslationOptions):
    fields = ('text',)

@translator.register(models.PublicOrganizations)
class PublicOrganizationsTranslation(translator.TranslationOptions):
    fields = ('text',)
    