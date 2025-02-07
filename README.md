# Blog Application
A dynamic blog platform built with Flask and Bootstrap, featuring clean design, modular templates, and content management through API integration.

![Python](https://img.shields.io/badge/Python-3.8+-blue)
![Flask](https://img.shields.io/badge/Flask-Backend-red)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5.2.3-purple)
![API](https://img.shields.io/badge/JSON-API-green)

## 🎯 Overview
This project creates a professional blog platform that:
1. Implements responsive design
2. Uses template inheritance
3. Integrates external API
4. Features modular components
5. Includes contact forms

## 🌐 Application Features
### Backend Components
- Flask routing system
- Template inheritance
- URL management
- Static asset handling
- API integration

### Frontend Elements
- Bootstrap integration
- Responsive design
- Navigation bar
- Contact form
- Social links

## 🔧 Technical Components
### Route Management System
```python
@app.route('/')
@app.route('/index.html')
def home():
    url_dict = get_url_dict()
    return render_template('index.html',
                           url=url_dict,
                           blog_posts=blog_data_json)

@app.route('/post/<int:blog_id>.html')
def post(blog_id):
    url_dict = get_url_dict()
    for blog in blog_data_json:
        if blog['id'] == blog_id:
            return render_template('post.html',
                                   url=url_dict,
                                   blog_post=blog)
```

### Key Features
1. **Content Management**
   - API integration
   - Dynamic routing
   - Template inheritance
   - Component reuse

2. **Page Structure**
   - Home page
   - Blog posts
   - About page
   - Contact form

3. **Asset Management**
   - Static files
   - Bootstrap CDN
   - Font Awesome
   - Google Fonts

## 💻 Implementation Details
### Project Structure
- Flask application core
- Modular templates
- Bootstrap integration
- Font Awesome icons

### Components
- Header template
- Navigation bar
- Footer template
- Contact form

## 🚀 Usage
1. Install required packages:
```bash
pip install flask requests
```

2. Run the application:
```bash
python main.py
```

## 🎯 Project Structure
```
flask-blog/
├── main.py          # Flask application
├── url.py           # URL management
├── static/
│   ├── assets/     # Images and assets
│   ├── css/        # Stylesheets
│   └── js/         # JavaScript files
└── templates/
    ├── index.html    # Home page
    ├── post.html     # Article page
    ├── about.html    # About page
    ├── contact.html  # Contact page
    ├── header.html   # Header component
    ├── footer.html   # Footer component
    └── navigation_bar.html # Navigation
```

## 📊 Features
### Page Components
- Dynamic blog posts
- Responsive navigation
- Contact form
- Social links
- About section

### Design Elements
- Bootstrap framework
- Google Fonts
- Font Awesome icons
- Responsive layout
- Clean typography

## 📝 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👥 Author
Burak TÜZEL