from django.utils import timezone
from django.contrib.auth import get_user_model
from blog.models import Post

# Lấy người dùng 'lamtd'
User = get_user_model()
me = User.objects.get(username='lamtd')

# Query 1: Tạo bài viết về công nghệ
Post.objects.create(
    author=me,
    title='Lập trình Python với Django: Hành trình bắt đầu',
    text='Hôm nay, tôi bắt đầu học Django và thấy nó rất thú vị. Framework này cung cấp nhiều công cụ mạnh mẽ để xây dựng ứng dụng web nhanh chóng và an toàn.',
    created_date=timezone.now(),
    published_date=timezone.now()
)

# Query 2: Tạo bài viết về du lịch
Post.objects.create(
    author=me,
    title='Khám phá Đà Lạt mùa hoa mai anh đào',
    text='Đà Lạt vào mùa hoa mai anh đào thật đẹp. Những con đường rợp hoa và không khí se lạnh làm tôi nhớ mãi chuyến đi này.',
    created_date=timezone.now() - timezone.timedelta(days=5),
    published_date=timezone.now() - timezone.timedelta(days=2)
)

# Query 3: Tạo bài viết chưa xuất bản
Post.objects.create(
    author=me,
    title='Học máy tính và những thử thách đầu tiên',
    text='Tôi đang tìm hiểu về máy học và gặp một số khó khăn trong việc hiểu các thuật toán cơ bản. Nhưng tôi sẽ không bỏ cuộc!',
    created_date=timezone.now() - timezone.timedelta(days=10),
    published_date=None
)

# Query 4: Tạo bài viết về ẩm thực
Post.objects.create(
    author=me,
    title='Cách làm bánh mì pate chuẩn vị Việt Nam',
    text='Bánh mì pate là món ăn sáng yêu thích của tôi. Công thức đơn giản nhưng cần chú ý đến cách chọn nguyên liệu tươi ngon.',
    created_date=timezone.now() - timezone.timedelta(days=3),
    published_date=timezone.now()
)

# Query 5: Tạo bài viết về sách
Post.objects.create(
    author=me,
    title='Đọc "Nhà giả kim" và bài học cuộc sống',
    text='Cuốn sách "Nhà giả kim" của Paulo Coelho đã truyền cảm hứng cho tôi theo đuổi ước mơ và tin vào định mệnh.',
    created_date=timezone.now() - timezone.timedelta(days=7),
    published_date=timezone.now() - timezone.timedelta(days=4)
)