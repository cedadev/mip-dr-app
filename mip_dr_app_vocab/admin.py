"""
This admin.py file was generated by the script generate_models_from_xml.py

"""
from django.contrib import admin
from import_export.admin import ImportExportActionModelAdmin

from mip_dr_app_vocab import models
from mip_dr_app_vocab import resources


@admin.register(models.Units)
class UnitsAdmin(ImportExportActionModelAdmin):
    list_display = ('label', 'title')
    resource_classes = [resources.UnitsResource]


@admin.register(models.Miptable)
class MiptableAdmin(ImportExportActionModelAdmin):
    list_display = ('label', 'title')
    resource_classes = [resources.MiptableResource]


@admin.register(models.Mip)
class MipAdmin(ImportExportActionModelAdmin):
    list_display = ('label', 'title')
    resource_classes = [resources.MipResource]


@admin.register(models.RequestVarGroup)
class RequestVarGroupAdmin(ImportExportActionModelAdmin):
    list_display = ('label', 'title')
    resource_classes = [resources.RequestVarGroupResource]


@admin.register(models.Exptgroup)
class ExptgroupAdmin(ImportExportActionModelAdmin):
    list_display = ('label', 'title')
    resource_classes = [resources.ExptgroupResource]


@admin.register(models.RequestLink)
class RequestLinkAdmin(ImportExportActionModelAdmin):
    list_display = ('label', 'title')
    resource_classes = [resources.RequestLinkResource]


@admin.register(models.Experiment)
class ExperimentAdmin(ImportExportActionModelAdmin):
    list_display = ('label', 'title')
    resource_classes = [resources.ExperimentResource]


@admin.register(models.Grids)
class GridsAdmin(ImportExportActionModelAdmin):
    list_display = ('label', 'title')
    resource_classes = [resources.GridsResource]


@admin.register(models.RequestItem)
class RequestItemAdmin(ImportExportActionModelAdmin):
    list_display = ('label', 'title')
    resource_classes = [resources.RequestItemResource]


@admin.register(models.Objective)
class ObjectiveAdmin(ImportExportActionModelAdmin):
    list_display = ('label', 'title')
    resource_classes = [resources.ObjectiveResource]


@admin.register(models.SpatialShape)
class SpatialShapeAdmin(ImportExportActionModelAdmin):
    list_display = ('label', 'title')
    resource_classes = [resources.SpatialShapeResource]


@admin.register(models.ModelConfig)
class ModelConfigAdmin(ImportExportActionModelAdmin):
    list_display = ('label', 'title')
    resource_classes = [resources.ModelConfigResource]


@admin.register(models.ObjectiveLink)
class ObjectiveLinkAdmin(ImportExportActionModelAdmin):
    list_display = ('label', 'title')
    resource_classes = [resources.ObjectiveLinkResource]


@admin.register(models.Remarks)
class RemarksAdmin(ImportExportActionModelAdmin):
    list_display = ('label', 'title')
    resource_classes = [resources.RemarksResource]


@admin.register(models.Standardname)
class StandardnameAdmin(ImportExportActionModelAdmin):
    list_display = ('label', 'title')
    resource_classes = [resources.StandardnameResource]


@admin.register(models.Var)
class VarAdmin(ImportExportActionModelAdmin):
    list_display = ('label', 'title')
    resource_classes = [resources.VarResource]


@admin.register(models.VarChoice)
class VarChoiceAdmin(ImportExportActionModelAdmin):
    list_display = ('label', 'title')
    resource_classes = [resources.VarChoiceResource]


@admin.register(models.TemporalShape)
class TemporalShapeAdmin(ImportExportActionModelAdmin):
    list_display = ('label', 'title')
    resource_classes = [resources.TemporalShapeResource]


@admin.register(models.TimeSlice)
class TimeSliceAdmin(ImportExportActionModelAdmin):
    list_display = ('label', 'title')
    resource_classes = [resources.TimeSliceResource]


@admin.register(models.CellMethods)
class CellMethodsAdmin(ImportExportActionModelAdmin):
    list_display = ('label', 'title')
    resource_classes = [resources.CellMethodsResource]


@admin.register(models.Structure)
class StructureAdmin(ImportExportActionModelAdmin):
    list_display = ('label', 'title')
    resource_classes = [resources.StructureResource]


@admin.register(models.CMORvar)
class CMORvarAdmin(ImportExportActionModelAdmin):
    list_display = ('label', 'title')
    resource_classes = [resources.CMORvarResource]


@admin.register(models.VarChoiceLinkC)
class VarChoiceLinkCAdmin(ImportExportActionModelAdmin):
    list_display = ('label', 'title')
    resource_classes = [resources.VarChoiceLinkCResource]


@admin.register(models.RequestVar)
class RequestVarAdmin(ImportExportActionModelAdmin):
    list_display = ('label', 'title')
    resource_classes = [resources.RequestVarResource]


@admin.register(models.VarChoiceLinkR)
class VarChoiceLinkRAdmin(ImportExportActionModelAdmin):
    list_display = ('label', 'title')
    resource_classes = [resources.VarChoiceLinkRResource]


@admin.register(models.TableSection)
class TableSectionAdmin(ImportExportActionModelAdmin):
    list_display = ('label', 'title')
    resource_classes = [resources.TableSectionResource]


@admin.register(models.Qcranges)
class QcrangesAdmin(ImportExportActionModelAdmin):
    list_display = ('label', 'title')
    resource_classes = [resources.QcrangesResource]


@admin.register(models.Places)
class PlacesAdmin(ImportExportActionModelAdmin):
    list_display = ('label', 'title')
    resource_classes = [resources.PlacesResource]


@admin.register(models.Transfers)
class TransfersAdmin(ImportExportActionModelAdmin):
    list_display = ('label', 'title')
    resource_classes = [resources.TransfersResource]
