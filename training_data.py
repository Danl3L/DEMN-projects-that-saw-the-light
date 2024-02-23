# Fake data for training courses
courses_data = {
    'finance': {
        'financial analysis': {'benefit': 'Enhance analytical skills', 'duration': '3 months', 'url': 'https://www.coursera.org/financial-analysis'},
        'risk management': {'benefit': 'Improve risk assessment abilities', 'duration': '6 months', 'url': 'https://www.coursera.org/risk-management'},
        'investment banking': {'benefit': 'Learn financial modeling and analysis', 'duration': '5 months', 'url': 'https://www.coursera.org/investment-banking'},
        'corporate finance': {'benefit': 'Understand financial strategies for corporations', 'duration': '4 months', 'url': 'https://www.coursera.org/corporate-finance'},
        'portfolio management': {'benefit': 'Manage investment portfolios effectively', 'duration': '4 months', 'url': 'https://www.coursera.org/portfolio-management'}
    },
    'manufacturing': {
        'lean manufacturing': {'benefit': 'Streamline production processes', 'duration': '4 months', 'url': 'https://www.coursera.org/lean-manufacturing'},
        'quality management': {'benefit': 'Ensure product quality standards', 'duration': '5 months', 'url': 'https://www.coursera.org/quality-management'},
        'supply chain optimization': {'benefit': 'Optimize logistics and distribution', 'duration': '6 months', 'url': 'https://www.coursera.org/supply-chain-optimization'},
        'six sigma': {'benefit': 'Implement quality improvement methodologies', 'duration': '3 months', 'url': 'https://www.coursera.org/six-sigma'},
        'production planning': {'benefit': 'Plan and schedule manufacturing processes', 'duration': '4 months', 'url': 'https://www.coursera.org/production-planning'}
    },
    'marketing': {
        'digital marketing': {'benefit': 'Learn modern marketing techniques', 'duration': '3 months', 'url': 'https://www.coursera.org/digital-marketing'},
        'brand management': {'benefit': 'Develop branding strategies', 'duration': '4 months', 'url': 'https://www.coursera.org/brand-management'},
        'social media marketing': {'benefit': 'Harness social platforms for promotion', 'duration': '3 months', 'url': 'https://www.coursera.org/social-media-marketing'},
        'market research': {'benefit': 'Conduct effective market analysis', 'duration': '5 months', 'url': 'https://www.coursera.org/market-research'},
        'marketing analytics': {'benefit': 'Utilize data analytics for marketing insights', 'duration': '4 months', 'url': 'https://www.coursera.org/marketing-analytics'}
    },
    'technology': {
        'data science fundamentals': {'benefit': 'Gain insights from data', 'duration': '6 months', 'url': 'https://www.coursera.org/data-science-fundamentals'},
        'software development': {'benefit': 'Learn coding and software design', 'duration': '8 months', 'url': 'https://www.coursera.org/software-development'},
        'cloud computing': {'benefit': 'Understand distributed computing', 'duration': '5 months', 'url': 'https://www.coursera.org/cloud-computing'},
        'cybersecurity': {'benefit': 'Protect systems from cyber threats', 'duration': '4 months', 'url': 'https://www.coursera.org/cybersecurity'},
        'blockchain technology': {'benefit': 'Explore decentralized digital ledgers', 'duration': '4 months', 'url': 'https://www.coursera.org/blockchain-technology'}
    }
}
roles = list(courses_data.keys())