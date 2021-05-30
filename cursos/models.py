from django.db import models


class Curso(models.Model):
    titulo = models.CharField(max_length=225)
    url = models.URLField(unique=True)

    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'

    def __str__(self):
        return self.titulo


class Avaliacao(models.Model):
    curso = models.ForeignKey('Curso', related_name='avaliacoes', on_delete=models.CASCADE)
    nome = models.CharField(max_length=225)
    email = models.EmailField()
    comentario = models.TextField(blank=True, default='')
    avaliacao = models.DecimalField(max_digits=2, decimal_places=1)

    class Meta:
        verbose_name = 'Avaliacao'
        verbose_name_plural = 'Avaliacoes'
 #       unique_together=['email','cursos']

        def __str__(self):
            return f'{self.nome} avaliou o cursos {self.curso} com a nota {self.avaliacao}'


