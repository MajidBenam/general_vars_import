
################ Beginning of Serializers Imports (TODO: Make them automatic too)

from django.contrib.auth.models import User, Group
from rest_framework import serializers
from seshat.apps.general.models import Polity_research_assistant, Polity_utm_zone, Polity_original_name, Polity_alternative_name, Polity_peak_years, Polity_duration, Polity_degree_of_centralization, Polity_suprapolity_relations, Polity_capital, Polity_language, Polity_linguistic_family, Polity_language_genus, Polity_religion_genus, Polity_religion_family, Polity_religion, Polity_relationship_to_preceding_entity, Polity_preceding_entity, Polity_succeeding_entity, Polity_supracultural_entity, Polity_scale_of_supracultural_interaction, Polity_alternate_religion_genus, Polity_alternate_religion_family, Polity_alternate_religion, Polity_expert, Polity_editor, Polity_religious_tradition
from ..core.models import Polity, Reference, Section, Subsection, Variablehierarchy

################ End of Serializers Imports

################ Beginning of Base Serializers
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class ReferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reference
        fields = ['id', 'title', 'year', 'creator', 'zotero_link', 'long_name']
        
################ End of Base Serializers
################ Beginning of Serializers Imports

class Polity_research_assistantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Polity_research_assistant
        fields = ['year_from', 'year_to', 'polity_ra', 'tag']

class Polity_utm_zoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Polity_utm_zone
        fields = ['year_from', 'year_to', 'utm_zone', 'tag']

class Polity_original_nameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Polity_original_name
        fields = ['year_from', 'year_to', 'original_name', 'tag']

class Polity_alternative_nameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Polity_alternative_name
        fields = ['year_from', 'year_to', 'alternative_name', 'tag']

class Polity_peak_yearsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Polity_peak_years
        fields = ['year_from', 'year_to', 'peak_year_from', 'peak_year_to', 'tag']

class Polity_durationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Polity_duration
        fields = ['year_from', 'year_to', 'polity_year_from', 'polity_year_to', 'tag']

class Polity_degree_of_centralizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Polity_degree_of_centralization
        fields = ['year_from', 'year_to', 'degree_of_centralization', 'tag']

class Polity_suprapolity_relationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Polity_suprapolity_relations
        fields = ['year_from', 'year_to', 'supra_polity_relations', 'tag']

class Polity_capitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Polity_capital
        fields = ['year_from', 'year_to', 'capital', 'tag']

class Polity_languageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Polity_language
        fields = ['year_from', 'year_to', 'language', 'tag']

class Polity_linguistic_familySerializer(serializers.ModelSerializer):
    class Meta:
        model = Polity_linguistic_family
        fields = ['year_from', 'year_to', 'linguistic_family', 'tag']

class Polity_language_genusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Polity_language_genus
        fields = ['year_from', 'year_to', 'language_genus', 'tag']

class Polity_religion_genusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Polity_religion_genus
        fields = ['year_from', 'year_to', 'religion_genus', 'tag']

class Polity_religion_familySerializer(serializers.ModelSerializer):
    class Meta:
        model = Polity_religion_family
        fields = ['year_from', 'year_to', 'religion_family', 'tag']

class Polity_religionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Polity_religion
        fields = ['year_from', 'year_to', 'religion', 'tag']

class Polity_relationship_to_preceding_entitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Polity_relationship_to_preceding_entity
        fields = ['year_from', 'year_to', 'relationship_to_preceding_entity', 'tag']

class Polity_preceding_entitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Polity_preceding_entity
        fields = ['year_from', 'year_to', 'preceding_entity', 'tag']

class Polity_succeeding_entitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Polity_succeeding_entity
        fields = ['year_from', 'year_to', 'succeeding_entity', 'tag']

class Polity_supracultural_entitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Polity_supracultural_entity
        fields = ['year_from', 'year_to', 'supracultural_entity', 'tag']

class Polity_scale_of_supracultural_interactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Polity_scale_of_supracultural_interaction
        fields = ['year_from', 'year_to', 'scale_from', 'scale_to', 'tag']

class Polity_alternate_religion_genusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Polity_alternate_religion_genus
        fields = ['year_from', 'year_to', 'alternate_religion_genus', 'tag']

class Polity_alternate_religion_familySerializer(serializers.ModelSerializer):
    class Meta:
        model = Polity_alternate_religion_family
        fields = ['year_from', 'year_to', 'alternate_religion_family', 'tag']

class Polity_alternate_religionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Polity_alternate_religion
        fields = ['year_from', 'year_to', 'alternate_religion', 'tag']

class Polity_expertSerializer(serializers.ModelSerializer):
    class Meta:
        model = Polity_expert
        fields = ['year_from', 'year_to', 'expert', 'tag']

class Polity_editorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Polity_editor
        fields = ['year_from', 'year_to', 'editor', 'tag']

class Polity_religious_traditionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Polity_religious_tradition
        fields = ['year_from', 'year_to', 'religious_tradition', 'tag']
class PolitySerializer(serializers.ModelSerializer):
	general_polity_research_assistant_related = Polity_research_assistantSerializer(many=True, read_only=True)
	general_polity_utm_zone_related = Polity_utm_zoneSerializer(many=True, read_only=True)
	general_polity_original_name_related = Polity_original_nameSerializer(many=True, read_only=True)
	general_polity_alternative_name_related = Polity_alternative_nameSerializer(many=True, read_only=True)
	general_polity_peak_years_related = Polity_peak_yearsSerializer(many=True, read_only=True)
	general_polity_duration_related = Polity_durationSerializer(many=True, read_only=True)
	general_polity_degree_of_centralization_related = Polity_degree_of_centralizationSerializer(many=True, read_only=True)
	general_polity_suprapolity_relations_related = Polity_suprapolity_relationsSerializer(many=True, read_only=True)
	general_polity_capital_related = Polity_capitalSerializer(many=True, read_only=True)
	general_polity_language_related = Polity_languageSerializer(many=True, read_only=True)
	general_polity_linguistic_family_related = Polity_linguistic_familySerializer(many=True, read_only=True)
	general_polity_language_genus_related = Polity_language_genusSerializer(many=True, read_only=True)
	general_polity_religion_genus_related = Polity_religion_genusSerializer(many=True, read_only=True)
	general_polity_religion_family_related = Polity_religion_familySerializer(many=True, read_only=True)
	general_polity_religion_related = Polity_religionSerializer(many=True, read_only=True)
	general_polity_relationship_to_preceding_entity_related = Polity_relationship_to_preceding_entitySerializer(many=True, read_only=True)
	general_polity_preceding_entity_related = Polity_preceding_entitySerializer(many=True, read_only=True)
	general_polity_succeeding_entity_related = Polity_succeeding_entitySerializer(many=True, read_only=True)
	general_polity_supracultural_entity_related = Polity_supracultural_entitySerializer(many=True, read_only=True)
	general_polity_scale_of_supracultural_interaction_related = Polity_scale_of_supracultural_interactionSerializer(many=True, read_only=True)
	general_polity_alternate_religion_genus_related = Polity_alternate_religion_genusSerializer(many=True, read_only=True)
	general_polity_alternate_religion_family_related = Polity_alternate_religion_familySerializer(many=True, read_only=True)
	general_polity_alternate_religion_related = Polity_alternate_religionSerializer(many=True, read_only=True)
	general_polity_expert_related = Polity_expertSerializer(many=True, read_only=True)
	general_polity_editor_related = Polity_editorSerializer(many=True, read_only=True)
	general_polity_religious_tradition_related = Polity_religious_traditionSerializer(many=True, read_only=True)

	class Meta:
		model = Polity
		fields = ['id', 'name', 'start_year', 'end_year', 'general_polity_research_assistant_related', 'general_polity_utm_zone_related', 'general_polity_original_name_related', 'general_polity_alternative_name_related', 'general_polity_peak_years_related', 'general_polity_duration_related', 'general_polity_degree_of_centralization_related', 'general_polity_suprapolity_relations_related', 'general_polity_capital_related', 'general_polity_language_related', 'general_polity_linguistic_family_related', 'general_polity_language_genus_related', 'general_polity_religion_genus_related', 'general_polity_religion_family_related', 'general_polity_religion_related', 'general_polity_relationship_to_preceding_entity_related', 'general_polity_preceding_entity_related', 'general_polity_succeeding_entity_related', 'general_polity_supracultural_entity_related', 'general_polity_scale_of_supracultural_interaction_related', 'general_polity_alternate_religion_genus_related', 'general_polity_alternate_religion_family_related', 'general_polity_alternate_religion_related', 'general_polity_expert_related', 'general_polity_editor_related', 'general_polity_religious_tradition_related']
    
################ End of Serializers Imports
