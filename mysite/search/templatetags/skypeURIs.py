from django import template
from SkypeURI import SkypeURI

register = template.Library()

@register.assignment_tag
def skypeVoiceURI(patients):
    patientUUIDs = []
    for patient in patients:
        patientUUIDs.append(patient.uuid)

    return SkypeURI().getSkypeVoiceURI(patientUUIDs)

@register.assignment_tag
def skypeVideoURI(patients):
    patientUUIDs = []
    for patient in patients:
        patientUUIDs.append(patient.uuid)

    return SkypeURI().getSkypeVideoURI(patientUUIDs)

@register.assignment_tag
def skypeChatURI(patients):
    patientUUIDs = []
    for patient in patients:
        patientUUIDs.append(patient.uuid)

    return SkypeURI().getSkypeChatURI(patientUUIDs)