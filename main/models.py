from django.db import models


class Author(models.Model):
    name = models.CharField(
        max_length=100, verbose_name='Name'
    )
    last_name = models.CharField(
        max_length=100, verbose_name='Last name'
    )
    date_birth = models.DateField(
        verbose_name='Date birth'
    )
    biography = models.TextField(
        max_length=500
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'


class Genre(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Book(models.Model):
    title = models.CharField(max_length=255, verbose_name='The title of the book'
    )
    published = models.DateField(verbose_name='The data of publishing')
    pages = models.PositiveIntegerField(verbose_name='The count of the pages')
    author = models.ForeignKey(
        Author, on_delete=models.CASCADE, related_name='books', verbose_name='Author'
    )
    genre = models.ManyToManyField(
        Genre
    )

    def __str__(self):
        return f"{self.author}---{self.title}"

    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'


class BookImage(models.Model):
    image = models.ImageField(upload_to='book_images')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='images')

    @property
    def get_absolute_image_url(self):
        image_url = ''
        if self.image:
            image_url = self.image.url
        return image_url
