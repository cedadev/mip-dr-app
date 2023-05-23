from django.db.models import Q
from django.http import JsonResponse
from django.views.generic import TemplateView

from mip_dr_app_vocab import models


class SuggestionView(TemplateView):
    """
    The suggestion view provides search terms for the search functionality.

    The intention is that the terms are used in a type ahead search widget. As the
    search is based on the "title" and "label" fields of the model(s), the suggestions
    are also taken from those fields. By default terms from all tables are provided. If
    the name of a json file is also provided in the URL, e.g. mip.json, then only terms
    for the associated table are returned.

    """

    def render_to_response(self, context):
        return JsonResponse(
            context["suggestion"],
            safe=False,
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            vocab = context["vocab"]
        except KeyError:
            vocab = "*"
        table_name = vocab.split(".")[0]
        values = set()

        if table_name in ["*", "mip"]:
            values.update(
                _get_suggestions(models.Mip.objects.values_list("title", "label"))
            )

        if table_name in ["*", "var"]:
            values.update(
                _get_suggestions(models.Var.objects.values_list("title", "label"))
            )

        if table_name in ["*", "CMORvar"]:
            values.update(
                _get_suggestions(models.CMORvar.objects.values_list("title", "label"))
            )

        if table_name in ["*", "requestVar"]:
            values.update(
                _get_suggestions(
                    models.RequestVar.objects.values_list("title", "label")
                )
            )

        if table_name in ["*", "experiment"]:
            values.update(
                _get_suggestions(
                    models.Experiment.objects.values_list("title", "label")
                )
            )

        if table_name in ["*", "objective"]:
            values.update(
                _get_suggestions(models.Objective.objects.values_list("title", "label"))
            )

        if table_name in ["*", "grids"]:
            values.update(
                _get_suggestions(models.Grids.objects.values_list("title", "label"))
            )

        if table_name in ["*", "standardname"]:
            values.update(
                _get_suggestions(
                    models.Standardname.objects.values_list("title", "label")
                )
            )

        if table_name in ["*", "exptgroup"]:
            values.update(
                _get_suggestions(models.Exptgroup.objects.values_list("title", "label"))
            )

        if table_name in ["*", "spatialShape"]:
            values.update(
                _get_suggestions(
                    models.SpatialShape.objects.values_list("title", "label")
                )
            )

        if table_name in ["*", "temporalShape"]:
            values.update(
                _get_suggestions(
                    models.TemporalShape.objects.values_list("title", "label")
                )
            )

        if table_name in ["*", "structure"]:
            values.update(
                _get_suggestions(models.Structure.objects.values_list("title", "label"))
            )

        if table_name in ["*", "miptable"]:
            values.update(
                _get_suggestions(models.Miptable.objects.values_list("title", "label"))
            )

        if table_name in ["*", "requestVarGroup"]:
            values.update(
                _get_suggestions(
                    models.RequestVarGroup.objects.values_list("title", "label")
                )
            )

        if table_name in ["*", "requestItem"]:
            values.update(
                _get_suggestions(
                    models.RequestItem.objects.values_list("title", "label")
                )
            )

        if table_name in ["*", "requestLink"]:
            values.update(
                _get_suggestions(
                    models.RequestLink.objects.values_list("title", "label")
                )
            )

        if table_name in ["*", "tableSection"]:
            values.update(
                _get_suggestions(
                    models.TableSection.objects.values_list("title", "label")
                )
            )

        if table_name in ["*", "modelConfig"]:
            values.update(
                _get_suggestions(
                    models.ModelConfig.objects.values_list("title", "label")
                )
            )

        if table_name in ["*", "varChoiceLinkC"]:
            values.update(
                _get_suggestions(
                    models.VarChoiceLinkC.objects.values_list("title", "label")
                )
            )

        if table_name in ["*", "objectiveLink"]:
            values.update(
                _get_suggestions(
                    models.ObjectiveLink.objects.values_list("title", "label")
                )
            )

        if table_name in ["*", "remarks"]:
            values.update(
                _get_suggestions(models.Remarks.objects.values_list("title", "label"))
            )

        if table_name in ["*", "varChoiceLinkR"]:
            values.update(
                _get_suggestions(
                    models.VarChoiceLinkR.objects.values_list("title", "label")
                )
            )

        if table_name in ["*", "varChoice"]:
            values.update(
                _get_suggestions(models.VarChoice.objects.values_list("title", "label"))
            )

        if table_name in ["*", "timeSlice"]:
            values.update(
                _get_suggestions(models.TimeSlice.objects.values_list("title", "label"))
            )

        if table_name in ["*", "cellMethods"]:
            values.update(
                _get_suggestions(
                    models.CellMethods.objects.values_list("title", "label")
                )
            )

        if table_name in ["*", "places"]:
            values.update(
                _get_suggestions(models.Places.objects.values_list("title", "label"))
            )

        if table_name in ["*", "qcranges"]:
            values.update(
                _get_suggestions(models.Qcranges.objects.values_list("title", "label"))
            )

        if table_name in ["*", "transfers"]:
            values.update(
                _get_suggestions(models.Transfers.objects.values_list("title", "label"))
            )

        if table_name in ["*", "units"]:
            values.update(
                _get_suggestions(models.Units.objects.values_list("title", "label"))
            )

        context["suggestion"] = sorted(list(values))
        return context


def _get_suggestions(result_set):
    values = set()
    for result in result_set:
        for word in result[0].split(" "):
            word = _clean_word(word)
            if word in ["", "-", "--", "..", "..."]:
                continue
            values.add(word)
        for word in result[1].split(" "):
            word = _clean_word(word)
            if word in ["-", "--", "..", "..."]:
                continue
            values.add(word)
    return values


def _clean_word(word):
    for symbol in ["(", ")", '"', ","]:
        word = word.replace(symbol, "")
    return word


class SearchView(TemplateView):
    """
    The search view provides search functionality for the DRS.

    The search is based on the value of "q" in the GET request. A search is done for the
    value of "q" in the "title" and "label" fields of the model(s).
    The models searched is dependent on the value of "vocab" in the GET request. By
    default all models are searched.

    """

    template_name = "mip_dr_app_search/search_results.html"

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
