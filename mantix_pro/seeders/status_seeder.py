from django.core.management.base import BaseCommand
from mantix_pro.models.status import Status

class Command(BaseCommand):
    help = "Seeder De Status"

    def handle(self, *args, **options):
        data_list = [
            {
                'status_name': 'Activo',
                'status_code': 'A',
                'active': 'S',
            },
            {
                'status_name': 'Inactivo',
                'status_code': 'I',
                'active': 'S',
            },
            {
                'status_name': 'Programado',
                'status_code': 'P',
                'active': 'S',
            },
            {
                'status_name': 'Reprogramado',
                'status_code': 'R',
                'active': 'S',
            },
            {
                'status_name': 'En ejecucion',
                'status_code': 'E',
                'active': 'S',
            },
            {
                'status_name': 'Completado',
                'status_code': 'C',
                'active': 'S',
            },
            {
                'status_name': 'Peticion de Reprogramar',
                'status_code': 'PR',
                'active': 'S',
            },
            # Agrega más registros según sea necesario
        ]

        for data in data_list:
            Status.objects.create(**data)

        self.stdout.write(self.style.SUCCESS('Se han creado los objetos de Status'))



