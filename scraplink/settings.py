from pathlib import Path

# المسار الأساسي للمشروع
BASE_DIR = Path(__file__).resolve().parent.parent

# إعدادات الأمان
SECRET_KEY = 'django-insecure-fh8g)xa7=f@!a&a731ase7ck@bgr*9=z(wj#&qva+!h=rfe-pm'
DEBUG = True
ALLOWED_HOSTS = []

# التطبيقات المثبتة
INSTALLED_APPS = [
    # تطبيقات Django الأساسية
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # تطبيقات المشروع
    'accounts',
    'listings',
    'core',
    'userproducts',  # ✅ تمت الإضافة هنا
]

# إعدادات الوسطاء (Middleware)
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',

    # تثبيت اللغة العربية افتراضياً عبر ميدل وير مخصص
    'listings.middleware.ForceArabicMiddleware',

    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# ملف URL الرئيسي
ROOT_URLCONF = 'scraplink.urls'

# إعدادات القوالب
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# إعدادات WSGI
WSGI_APPLICATION = 'scraplink.wsgi.application'

# إعدادات قاعدة البيانات
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# تحقق من كلمات المرور
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# إعدادات اللغة والتوقيت
LANGUAGE_CODE = 'ar'
TIME_ZONE = 'Asia/Riyadh'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# اللغات المتوفرة
LANGUAGES = [
    ('ar', 'Arabic'),
]

# مسار ملفات الترجمة
LOCALE_PATHS = [
    BASE_DIR / 'locale',
]

# ملفات الاستايل
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'

# ملفات الوسائط
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# الحقل الأساسي الافتراضي
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# نموذج المستخدم المخصص
AUTH_USER_MODEL = 'accounts.CustomUser'

# ✅ توجيه المستخدم بعد تسجيل الدخول إلى صفحة الخدمات
LOGIN_REDIRECT_URL = '/services/'

# (اختياري) توجيه المستخدم بعد تسجيل الخروج
LOGOUT_REDIRECT_URL = '/login/'
