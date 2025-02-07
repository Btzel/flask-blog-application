# Flask Blog Application
A dynamic blog platform built with Flask, featuring API integration for content management and responsive template rendering.

![Python](https://img.shields.io/badge/Python-3.8+-blue)
![Flask](https://img.shields.io/badge/Flask-Backend-red)
![API](https://img.shields.io/badge/JSON-API-green)
![HTML](https://img.shields.io/badge/HTML-Templates-orange)

## 🎯 Overview
This project creates a blog platform that:
1. Fetches articles from API
2. Renders dynamic content
3. Handles article routing
4. Displays full posts
5. Manages blog layout

## 🌐 Application Features
### Backend Components
- Flask routing system
- API integration
- Data handling
- URL management
- Error handling

### Frontend Elements
- Responsive templates
- Article previews
- Dynamic content
- Clean typography
- Custom styling

## 🔧 Technical Components
### Route Management System
```python
@app.route('/post/<int:article_id>')
def post(article_id):
    for article in response.json():
        if article_id == article['id']:
            return render_template(
                "post.html",
                article_json=article
            )
```

### Key Features
1. **Content Management**
   - API integration
   - JSON processing
   - Article routing
   - Content rendering

2. **Template System**
   - Dynamic rendering
   - Content mapping
   - Layout structure
   - Responsive design

3. **Data Processing**
   - JSON handling
   - Route parameters
   - Article filtering
   - Content display

## 💻 Implementation Details
### Project Structure
- Flask application core
- HTML templates
- Static assets
- Route handlers

### Data Flow
- API data fetching
- Content processing
- Template rendering
- User presentation

## 🚀 Usage
1. Install required packages:
```bash
pip install flask requests
```

2. Run the application:
```bash
python main.py
```

## 🎯 Application Rules
1. Configure Flask app
2. Set up API connection
3. Design templates
4. Handle routing
5. Manage content

## 🛠️ Project Structure
```
flask-blog/
├── main.py           # Flask application
├── post.py          # Post model
└── templates/
    ├── index.html    # Home page
    └── post.html     # Article page
```

## 📊 Features
### Route Handling
- Home page display
- Article routing
- Content mapping
- Dynamic URLs

### Content Display
- Article previews
- Full post views
- Responsive layout
- Clean typography

## 📝 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👥 Author
Burak TÜZEL