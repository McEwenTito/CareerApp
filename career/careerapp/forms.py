from django import forms
from .models import *

class GradesForm(forms.Form):
    grade0 = forms.ModelChoiceField(queryset=Subject.objects.all(), label='Subject')
    grade1 = forms.ModelChoiceField(queryset=Subject.objects.all(), label='Subject')
    grade2 = forms.ModelChoiceField(queryset=Subject.objects.all(), label='Subject')
    grade3 = forms.ModelChoiceField(queryset=Subject.objects.all(), label='Subject')
    grade4 = forms.ModelChoiceField(queryset=Subject.objects.all(), label='Subject')
    grade5 = forms.ModelChoiceField(queryset=Subject.objects.all(), label='Subject')

class ClusterForm(forms.Form):
    cluster1 = forms.ModelMultipleChoiceField(
        queryset = ClusterActivity.objects.filter(cluster_id = 1),
        widget = forms.CheckboxSelectMultiple,
        label = '',
        required = False,
    )
    cluster2 = forms.ModelMultipleChoiceField(
        queryset = ClusterActivity.objects.filter(cluster_id = 2),
        widget = forms.CheckboxSelectMultiple,
        label = '',
        required = False,)
    cluster3 = forms.ModelMultipleChoiceField(
        queryset = ClusterActivity.objects.filter(cluster_id = 3),
        widget = forms.CheckboxSelectMultiple,
        label = '',
        required = False,    )
    cluster4 = forms.ModelMultipleChoiceField(
        queryset = ClusterActivity.objects.filter(cluster_id = 4),
        widget = forms.CheckboxSelectMultiple,
        label = '',
        required = False,    )
    cluster5 = forms.ModelMultipleChoiceField(
        queryset = ClusterActivity.objects.filter(cluster_id = 5),
        widget = forms.CheckboxSelectMultiple,
        label = '',
        required = False,    )
    cluster6 = forms.ModelMultipleChoiceField(
        queryset = ClusterActivity.objects.filter(cluster_id = 7),
        widget = forms.CheckboxSelectMultiple,
        label = '',
        required = False,    )
    cluster7 = forms.ModelMultipleChoiceField(
        queryset = ClusterActivity.objects.filter(cluster_id = 8),
        widget = forms.CheckboxSelectMultiple,
        label = '',
        required = False,    )
    cluster8 = forms.ModelMultipleChoiceField(
        queryset = ClusterActivity.objects.filter(cluster_id = 9),
        widget = forms.CheckboxSelectMultiple,
        label = '',
        required = False,    )
    cluster9 = forms.ModelMultipleChoiceField(
        queryset = ClusterActivity.objects.filter(cluster_id = 10),
        widget = forms.CheckboxSelectMultiple,
        label = '',
        required = False,    )
    cluster10 = forms.ModelMultipleChoiceField(
        queryset = ClusterActivity.objects.filter(cluster_id = 11),
        widget = forms.CheckboxSelectMultiple,
        label = '',
        required = False,    )
    cluster11 = forms.ModelMultipleChoiceField(
        queryset = ClusterActivity.objects.filter(cluster_id = 12),
        widget = forms.CheckboxSelectMultiple,
        label = '',
        required = False,    )
    cluster12 = forms.ModelMultipleChoiceField(
        queryset = ClusterActivity.objects.filter(cluster_id = 13),
        widget = forms.CheckboxSelectMultiple,
        label = '',
        required = False,    )
    cluster13 = forms.ModelMultipleChoiceField(
        queryset = ClusterActivity.objects.filter(cluster_id = 14),
        widget = forms.CheckboxSelectMultiple,
        label = '',
        required = False,    )
    cluster14 = forms.ModelMultipleChoiceField(
        queryset = ClusterActivity.objects.filter(cluster_id = 15),
        widget = forms.CheckboxSelectMultiple,
        label = '',
        required = False,    )
    cluster15 = forms.ModelMultipleChoiceField(
        queryset = ClusterActivity.objects.filter(cluster_id = 16),
        widget = forms.CheckboxSelectMultiple,
        label = '',
        required = False,    )
    cluster16 = forms.ModelMultipleChoiceField(
        queryset = ClusterActivity.objects.filter(cluster_id = 17),
        widget = forms.CheckboxSelectMultiple,
        label = '',
        required = False,    )
