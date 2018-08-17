from django.test import TestCase

from .models import Mineral


class MineralModelTests(TestCase):
    def setUp(self):
        self.test_mineral_data = {
            'name': "Test Mineral",
            'image_filename': "Test Filename",
            'image_caption': "Test Caption",
            'category': "Test Category",
            'formula': "Test Formula",
            'strunz_classification': "Test Strunz Classification",
            'crystal_system': "Test Crystal System",
            'unit_cell': "Test Unit Cell",
            'color': "Test Color",
            'crystal_symmetry': "Test Crystal Symmetry",
            'cleavage': "Test Cleavage",
            'mohs_scale_hardness': "Test Mohs Scale Hardness",
            'luster': "Test Luster",
            'streak': "Test Streak",
            'diaphaneity': "Test Diaphaneity",
            'optical_properties': "Test Optical Properties",
            'group': "Test Group",
            'refractive_index': "Test Refractive Index",
            'crystal_habit': "Test Crystal Habit",
            'specific_gravity': "Test Specific Gravity"
        }

        self.test_mineral = Mineral.objects.create(**self.test_mineral_data)

    def test_create_saves_valid_model_to_db(self):
        db_mineral = Mineral.objects.get(
            name=self.test_mineral.name
        )

        self.assertEqual(
            db_mineral,
            self.test_mineral
        )

    def test_fieldnames_and_values_returns_valid_data(self):
        pass
