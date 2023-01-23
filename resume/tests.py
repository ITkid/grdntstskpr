import json
from copy import deepcopy

from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.test import APIClient

from resume.models import Resume

resume_data = {
            'id': 1,
            'status': 'ready',
            'grade': 'one',
            'speciality': 'doctor',
            'salary': 123.00,
            'education': 'education',
            'experience': 'experience',
            'portfolio': 'portfolio',
            'title': 'title',
            'phone': '+71234567890',
            'email': 'email@mail.com',
}


class ResumeTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        user1 = User.objects.create(
            username='u1',
        )
        user1.set_password('tst')
        user1.save()
        user2 = User.objects.create(
            username='u2',
        )
        user2.set_password('tst')
        user2.save()

        resume = Resume.objects.create(
            **resume_data, owner=user1
        )
        resume.save()

        data2 = deepcopy(resume_data)
        data2['id'] = 2

        resume = Resume.objects.create(
            **data2, owner=user2
        )
        resume.save()

    def test_patch_resume_success(self):
        self.client.login(username='u1', password='tst')
        data_to_patch = json.dumps({
            'status': 'dead',
            'grade': 'something',
            'speciality': 'technical',
            'salary': 222.50,
            'email': 'email@email.com',
        })

        response = self.client.patch(
            reverse(
                'resume-detail',
                kwargs={'pk': 1, },
            ),
            data_to_patch,
            content_type='application/json'
        )

        self.assertContains(response, 'something')
        self.assertContains(response, 'technical')
        self.assertContains(response, 222.50)
        self.assertContains(response, 'dead')
        self.assertContains(response, 'mail@email.com')
        self.assertEqual(response.status_code, 200)

    def test_patch_resume_invalid_data(self):
        self.client.login(username='u1', password='tst')
        data_to_patch = json.dumps({
            'email': 'email',
            'phone': 'incorrect phone',
        })

        response = self.client.patch(
            reverse(
                'resume-detail',
                kwargs={'pk': 1, },
            ),
            data_to_patch,
            content_type='application/json'
        )
        self.assertEqual(str(response.data['email'][0]), 'Enter a valid email address.')
        self.assertEqual(
            str(response.data['phone'][0]),
            "The phone number entered is not valid."
        )
        self.assertEqual(response.status_code, 400)

    def test_patch_resume_without_login(self):
        response = self.client.patch(
            reverse(
                'resume-detail',
                kwargs={'pk': 1, },
            ),
        )
        self.assertEqual(response.status_code, 302)

    def test_patch_resume_other_owner(self):
        self.client.login(username='u2', password='tst')
        response = self.client.patch(
            reverse(
                'resume-detail',
                kwargs={'pk': 1, },
            ),
        )
        self.assertEqual(response.status_code, 403)

    def test_patch_not_found_resume(self):
        self.client.login(username='u2', password='tst')
        response = self.client.patch(
            reverse(
                'resume-detail',
                kwargs={'pk': 3, },
            ),
        )
        self.assertEqual(response.status_code, 404)

    def test_get_first_resume(self):
        response = self.client.get(
            reverse(
                'resume-detail',
                kwargs={'pk': 1, },
            ),
        )

        self.assertEqual(response.status_code, 200)
        for item in resume_data:
            self.assertContains(response, item)

    def test_get_not_found(self):
        response = self.client.get(
            reverse(
                'resume-detail',
                kwargs={'pk': 3, },
            ),
        )

        self.assertEqual(response.status_code, 404)
