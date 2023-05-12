from django.db.models import Q
from django.views.generic import TemplateView
from django.http import JsonResponse

from mip_dr_app_api import models


class SearchView(TemplateView):
    """
    The search view provides search functionality for the DRS.

    The search is based on the value of "q" in the GET request. A search is done for the
    value of "q" in the "title" and "label" fields of the model(s).
    The models searched is dependent on the value of "vocab" in the GET request. By
    default all models are searched.

    """

    template_name = "search_results.html"

    def render_to_response(self, context):
        if (
            self.request.GET.get("format") == "json"
            or self.request.content_type == "application/json"
        ):
            data = {}
            for key in context.keys():
                if key in ["table", "q", "view"] or "_table_name" in key:
                    continue
                values = list(context[key].values())
                if len(values) > 0:
                    data[key] = values
            return JsonResponse(data, json_dumps_params={"indent": 2})
        return super().render_to_response(context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        query = self.request.GET.get("q")
        table_name = self.request.GET.get("vocab", "*")
        context["table"] = table_name
        context["q"] = query

        if query is not None:
            lookups = Q(title__icontains=query) | Q(label__icontains=query)

            if table_name in ["*", "mip"]:
                context["mip"] = models.Mip.objects.filter(lookups).distinct()
                context["mip_table_name"] = models.Mip._meta.verbose_name

            if table_name in ["*", "var"]:
                context["var"] = models.Var.objects.filter(lookups).distinct()
                context["var_table_name"] = models.Var._meta.verbose_name

            if table_name in ["*", "CMORvar"]:
                context["CMORvar"] = models.Mip.objects.filter(lookups).distinct()
                context["CMORvar_table_name"] = models.CMORvar._meta.verbose_name

            if table_name in ["*", "requestVar"]:
                context["requestVar"] = models.RequestVar.objects.filter(
                    lookups
                ).distinct()
                context["requestVar_table_name"] = models.RequestVar._meta.verbose_name

            if table_name in ["*", "experiment"]:
                context["experiment"] = models.Experiment.objects.filter(
                    lookups
                ).distinct()
                context["experiment_table_name"] = models.Experiment._meta.verbose_name

            if table_name in ["*", "objective"]:
                context["objective"] = models.Objective.objects.filter(
                    lookups
                ).distinct()
                context["objective_table_name"] = models.Objective._meta.verbose_name

            if table_name in ["*", "grids"]:
                context["grids"] = models.Grids.objects.filter(lookups).distinct()
                context["grids_table_name"] = models.Grids._meta.verbose_name

            if table_name in ["*", "standardname"]:
                context["standardname"] = models.Standardname.objects.filter(
                    lookups
                ).distinct()
                context[
                    "standardname_table_name"
                ] = models.Standardname._meta.verbose_name

            if table_name in ["*", "exptgroup"]:
                context["exptgroup"] = models.Exptgroup.objects.filter(
                    lookups
                ).distinct()
                context["exptgroup_table_name"] = models.Exptgroup._meta.verbose_name

            if table_name in ["*", "spatialShape"]:
                context["spatialShape"] = models.SpatialShape.objects.filter(
                    lookups
                ).distinct()
                context[
                    "spatialShape_table_name"
                ] = models.SpatialShape._meta.verbose_name

            if table_name in ["*", "temporalShape"]:
                context["temporalShape"] = models.TemporalShape.objects.filter(
                    lookups
                ).distinct()
                context[
                    "temporalShape_table_name"
                ] = models.TemporalShape._meta.verbose_name

            if table_name in ["*", "structure"]:
                context["structure"] = models.Structure.objects.filter(
                    lookups
                ).distinct()
                context["structure_table_name"] = models.Structure._meta.verbose_name

            if table_name in ["*", "miptable"]:
                context["miptable"] = models.Miptable.objects.filter(lookups).distinct()
                context["miptable_table_name"] = models.Miptable._meta.verbose_name

            if table_name in ["*", "requestVarGroup"]:
                context["requestVarGroup"] = models.RequestVarGroup.objects.filter(
                    lookups
                ).distinct()
                context[
                    "requestVarGroup_table_name"
                ] = models.RequestVarGroup._meta.verbose_name

            if table_name in ["*", "requestItem"]:
                context["requestItem"] = models.RequestItem.objects.filter(
                    lookups
                ).distinct()
                context[
                    "requestItem_table_name"
                ] = models.RequestItem._meta.verbose_name

            if table_name in ["*", "requestLink"]:
                context["requestLink"] = models.RequestLink.objects.filter(
                    lookups
                ).distinct()
                context[
                    "requestLink_table_name"
                ] = models.RequestLink._meta.verbose_name

            if table_name in ["*", "tableSection"]:
                context["tableSection"] = models.TableSection.objects.filter(
                    lookups
                ).distinct()
                context[
                    "tableSection_table_name"
                ] = models.TableSection._meta.verbose_name

            if table_name in ["*", "modelConfig"]:
                context["modelConfig"] = models.ModelConfig.objects.filter(
                    lookups
                ).distinct()
                context[
                    "modelConfig_table_name"
                ] = models.ModelConfig._meta.verbose_name

            if table_name in ["*", "varChoiceLinkC"]:
                context["varChoiceLinkC"] = models.VarChoiceLinkC.objects.filter(
                    lookups
                ).distinct()
                context[
                    "varChoiceLinkC_table_name"
                ] = models.VarChoiceLinkC._meta.verbose_name

            if table_name in ["*", "objectiveLink"]:
                context["objectiveLink"] = models.ObjectiveLink.objects.filter(
                    lookups
                ).distinct()
                context[
                    "objectiveLink_table_name"
                ] = models.ObjectiveLink._meta.verbose_name

            if table_name in ["*", "remarks"]:
                context["remarks"] = models.Remarks.objects.filter(lookups).distinct()
                context["remarks_table_name"] = models.Remarks._meta.verbose_name

            if table_name in ["*", "varChoiceLinkR"]:
                context["varChoiceLinkR"] = models.VarChoiceLinkR.objects.filter(
                    lookups
                ).distinct()
                context[
                    "varChoiceLinkR_table_name"
                ] = models.VarChoiceLinkR._meta.verbose_name

            if table_name in ["*", "varChoice"]:
                context["varChoice"] = models.VarChoice.objects.filter(
                    lookups
                ).distinct()
                context["varChoice_table_name"] = models.VarChoice._meta.verbose_name

            if table_name in ["*", "timeSlice"]:
                context["timeSlice"] = models.TimeSlice.objects.filter(
                    lookups
                ).distinct()
                context["timeSlice_table_name"] = models.TimeSlice._meta.verbose_name

            if table_name in ["*", "cellMethods"]:
                context["cellMethods"] = models.CellMethods.objects.filter(
                    lookups
                ).distinct()
                context[
                    "cellMethods_table_name"
                ] = models.CellMethods._meta.verbose_name

            if table_name in ["*", "places"]:
                context["places"] = models.Places.objects.filter(lookups).distinct()
                context["places_table_name"] = models.Places._meta.verbose_name

            if table_name in ["*", "qcranges"]:
                context["qcranges"] = models.Qcranges.objects.filter(lookups).distinct()
                context["qcranges_table_name"] = models.Qcranges._meta.verbose_name

            if table_name in ["*", "transfers"]:
                context["transfers"] = models.Transfers.objects.filter(
                    lookups
                ).distinct()
                context["transfers_table_name"] = models.Transfers._meta.verbose_name

            if table_name in ["*", "units"]:
                context["units"] = models.Units.objects.filter(lookups).distinct()
                context["units_table_name"] = models.Units._meta.verbose_name

        return context
