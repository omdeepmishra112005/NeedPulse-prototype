<!DOCTYPE html>
<!-- saved from url=(0073)https://69ea1254222984c0a3b13783-%2Dephemeral-centaur-462d97.netlify.app/ -->
<html lang="en"><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>NeedPulse - Smart Volunteer Coordination</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: system-ui, sans-serif;
            background: linear-gradient(135deg, #eef5fc 0%, #f5f7ff 50%, #f8f9fa 100%);
            color: #333;
            line-height: 1.6;
            min-height: 100vh;
        }

        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 16px;
        }

        /* Navbar */
        .navbar {
            background: rgba(255, 255, 255, 0.95);
            border-bottom: 1px solid rgba(255, 255, 255, 0.65);
            padding: 16px 0;
            position: sticky;
            top: 0;
            z-index: 100;
            box-shadow: 0 12px 30px rgba(0, 0, 0, 0.06);
        }

        .navbar .container {
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .logo {
            font-size: 24px;
            font-weight: bold;
        }

        .logo .pulse {
            color: #7F77DD;
            background: linear-gradient(45deg, #7F77DD, #378ADD);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }

        /* Enhanced Visual Appeal */
        body {
            background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
            min-height: 100vh;
        }

        .navbar {
            background: rgba(255, 255, 255, 0.95);
            backdrop-filter: blur(10px);
            border-bottom: 1px solid rgba(255, 255, 255, 0.2);
            box-shadow: 0 2px 20px rgba(0, 0, 0, 0.1);
        }

        .hero {
            background: linear-gradient(135deg, rgba(255, 255, 255, 0.1) 0%, rgba(255, 255, 255, 0.05) 100%);
            border-radius: 20px;
            padding: 80px 40px;
            margin: 40px 0;
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255, 255, 255, 0.2);
            position: relative;
            overflow: hidden;
        }

        .hero::before {
            content: '';
            position: absolute;
            top: -50%;
            left: -50%;
            width: 200%;
            height: 200%;
            background: radial-gradient(circle, rgba(127, 119, 221, 0.1) 0%, transparent 70%);
            animation: float 6s ease-in-out infinite;
        }

        @keyframes float {
            0%, 100% { transform: translate(-50%, -50%) rotate(0deg); }
            50% { transform: translate(-50%, -50%) rotate(180deg); }
        }

        .stat-card {
            background: linear-gradient(135deg, rgba(255, 255, 255, 0.9) 0%, rgba(255, 255, 255, 0.7) 100%);
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255, 255, 255, 0.3);
            position: relative;
            overflow: hidden;
        }

        .stat-card::before {
            content: '';
            position: absolute;
            top: 0;
            left: -100%;
            width: 100%;
            height: 100%;
            background: linear-gradient(90deg, transparent, rgba(55, 138, 221, 0.1), transparent);
            transition: left 0.5s;
        }

        .stat-card:hover::before {
            left: 100%;
        }

        .btn-primary {
            background: linear-gradient(135deg, #378ADD 0%, #7F77DD 100%);
            box-shadow: 0 4px 15px rgba(55, 138, 221, 0.3);
            transition: all 0.3s ease;
        }

        .btn-primary:hover {
            transform: translateY(-2px);
            box-shadow: 0 8px 25px rgba(55, 138, 221, 0.4);
        }

        .btn-outline {
            border: 2px solid;
            border-image: linear-gradient(135deg, #378ADD, #7F77DD) 1;
            background: transparent;
            color: #378ADD;
            position: relative;
            overflow: hidden;
        }

        .btn-outline::before {
            content: '';
            position: absolute;
            top: 0;
            left: -100%;
            width: 100%;
            height: 100%;
            background: linear-gradient(135deg, #378ADD, #7F77DD);
            transition: left 0.3s;
            z-index: -1;
        }

        .btn-outline:hover::before {
            left: 0;
        }

        .btn-outline:hover {
            color: white;
        }

        .language-toggle {
            display: flex;
            align-items: center;
            gap: 8px;
            margin-left: 24px;
        }

        .lang-btn {
            padding: 6px 12px;
            border: 1px solid #e0e0e0;
            border-radius: 16px;
            background: white;
            cursor: pointer;
            font-size: 12px;
            font-weight: 500;
            transition: all 0.15s;
        }

        .lang-btn.active {
            background: #378ADD;
            color: white;
            border-color: #378ADD;
        }

        .lang-btn:hover:not(.active) {
            background: #f0f0f0;
        }

        .auth-buttons {
            display: flex;
            align-items: center;
            margin-left: 24px;
        }

        /* Enhanced Interactions */
        .btn, .nav-link, .lang-btn, .urgency-btn, .login-btn {
            position: relative;
            overflow: hidden;
        }

        .btn::before, .nav-link::before, .lang-btn::before, .urgency-btn::before, .login-btn::before {
            content: '';
            position: absolute;
            top: 50%;
            left: 50%;
            width: 0;
            height: 0;
            background: rgba(255, 255, 255, 0.3);
            border-radius: 50%;
            transform: translate(-50%, -50%);
            transition: width 0.3s, height 0.3s;
        }

        .btn:active::before, .nav-link:active::before, .lang-btn:active::before, .urgency-btn:active::before, .login-btn:active::before {
            width: 300px;
            height: 300px;
        }

        .card-hover {
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        }

        .card-hover:hover {
            transform: translateY(-4px);
            box-shadow: 0 8px 25px rgba(0, 0, 0, 0.1);
        }

        .stat-card, .task-card, .match-card, .success-card, .login-card, .activity-feed {
            transition: all 0.3s ease;
        }

        .stat-card:hover, .task-card:hover, .match-card:hover, .success-card:hover, .login-card:hover, .activity-feed:hover {
            transform: translateY(-2px);
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.08);
        }

        .form-input:focus, .form-textarea:focus, .login-input:focus {
            outline: none;
            border-color: #378ADD;
            box-shadow: 0 0 0 3px rgba(55, 138, 221, 0.1);
            transform: scale(1.01);
        }

        .loading {
            position: relative;
            pointer-events: none;
        }

        .loading::after {
            content: '';
            position: absolute;
            top: 50%;
            left: 50%;
            width: 16px;
            height: 16px;
            margin: -8px 0 0 -8px;
            border: 2px solid rgba(255, 255, 255, 0.3);
            border-top: 2px solid white;
            border-radius: 50%;
            animation: spin 1s linear infinite;
        }

        @keyframes spin {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }

        .fade-in {
            animation: fadeIn 0.5s ease-in;
        }

        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(20px); }
            to { opacity: 1; transform: translateY(0); }
        }

        .nav-links {
            display: flex;
            gap: 24px;
            flex-wrap: wrap;
        }

        .nav-link {
            padding: 8px 16px;
            border-radius: 6px;
            cursor: pointer;
            transition: all 0.15s;
            color: #666;
        }

        .nav-link.active {
            background: #378ADD;
            color: white;
        }

        .nav-link:hover:not(.active) {
            background: #f0f0f0;
        }

        .auth-buttons {
            display: flex;
            align-items: center;
            gap: 8px;
        }

        .auth-buttons .btn {
            min-height: 42px;
        }

        .auth-buttons .btn.btn-outline {
            color: #378ADD;
            border-color: #378ADD;
        }

        .auth-buttons .btn.btn-outline:hover {
            color: white;
        }

        /* Pages */
        .page {
            display: none;
            padding: 32px 0;
        }

        .page.active {
            display: block;
        }

        /* Landing Page */
        .hero {
            text-align: center;
            padding: 80px 0;
            background: rgba(255, 255, 255, 0.75);
            border-radius: 28px;
            border: 1px solid rgba(255, 255, 255, 0.75);
            box-shadow: 0 24px 60px rgba(55, 138, 221, 0.08);
            position: relative;
            overflow: hidden;
            backdrop-filter: blur(10px);
            margin-top: 24px;
        }

        .hero::before {
            content: '';
            position: absolute;
            top: -20%;
            left: -10%;
            width: 200px;
            height: 200px;
            border-radius: 50%;
            background: rgba(127, 119, 221, 0.12);
            z-index: 0;
        }

        .hero h1 {
            background: linear-gradient(135deg, #378ADD 0%, #7F77DD 50%, #1D9E75 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            font-size: 56px;
            font-weight: 800;
            text-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
            animation: textGlow 3s ease-in-out infinite alternate;
            position: relative;
            z-index: 1;
        }

        @keyframes textGlow {
            from { filter: brightness(1); }
            to { filter: brightness(1.08); }
        }

        .hero p {
            font-size: 24px;
            color: #4b5563;
            margin-bottom: 32px;
            position: relative;
            z-index: 1;
        }

        .cta-buttons {
            display: flex;
            gap: 16px;
            justify-content: center;
            flex-wrap: wrap;
        }

        .btn {
            padding: 12px 24px;
            border-radius: 6px;
            font-weight: 500;
            cursor: pointer;
            transition: all 0.15s;
            border: none;
            font-size: 16px;
        }

        .btn-primary {
            background: linear-gradient(135deg, #378ADD 0%, #7F77DD 100%);
            color: white;
            box-shadow: 0 14px 28px rgba(55, 138, 221, 0.16);
        }

        .btn-primary:hover {
            transform: translateY(-2px);
            box-shadow: 0 18px 32px rgba(55, 138, 221, 0.22);
        }

        .btn-outline {
            background: transparent;
            color: #378ADD;
            border: 1px solid #378ADD;
        }

        .btn-outline:hover {
            background: #378ADD;
            color: white;
            transform: translateY(-2px);
        }

        .stats {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
            gap: 24px;
            margin: 80px 0;
        }

        .stat-card {
            background: white;
            border: 0.5px solid #e0e0e0;
            border-radius: 12px;
            padding: 24px;
            text-align: center;
        }

        .stat-number {
            font-size: 32px;
            font-weight: bold;
            color: #378ADD;
        }

        .stat-label {
            color: #666;
            margin-top: 8px;
        }

        .activity-feed {
            background: white;
            border: 0.5px solid #e0e0e0;
            border-radius: 12px;
            padding: 24px;
            max-width: 600px;
            margin: 0 auto;
        }

        .activity-item {
            display: flex;
            align-items: center;
            gap: 12px;
            padding: 12px 0;
            border-bottom: 1px solid #f0f0f0;
        }

        .activity-item:last-child {
            border-bottom: none;
        }

        .activity-dot {
            width: 8px;
            height: 8px;
            border-radius: 50%;
            background: #1D9E75;
        }

        .activity-dot.purple {
            background: #7F77DD;
        }

        .activity-dot.amber {
            background: #BA7517;
        }

        /* Dashboard */
        .tabs {
            display: flex;
            gap: 24px;
            margin-bottom: 32px;
            border-bottom: 1px solid #e0e0e0;
        }

        .tab {
            padding: 12px 0;
            cursor: pointer;
            border-bottom: 2px solid transparent;
            transition: all 0.15s;
        }

        .tab.active {
            border-bottom-color: #378ADD;
            color: #378ADD;
        }

        .metric-cards {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 24px;
            margin-bottom: 32px;
        }

        .metric-card {
            background: white;
            border: 0.5px solid #e0e0e0;
            border-radius: 12px;
            padding: 24px;
        }

        .metric-number {
            font-size: 24px;
            font-weight: bold;
            color: #378ADD;
        }

        .metric-label {
            color: #666;
            margin-top: 8px;
        }

        .map-placeholder {
            background: #E6F1FB;
            border: 0.5px solid #e0e0e0;
            border-radius: 12px;
            height: 300px;
            position: relative;
            margin-bottom: 32px;
        }

        .map-pin {
            position: absolute;
            font-size: 24px;
        }

        .map-label {
            position: absolute;
            bottom: 16px;
            left: 16px;
            background: white;
            padding: 8px 12px;
            border-radius: 6px;
            font-weight: 500;
        }

        /* Post Need */
        .form-card {
            background: white;
            border: 0.5px solid #e0e0e0;
            border-radius: 12px;
            padding: 32px;
            max-width: 600px;
            margin: 0 auto;
        }

        .form-group {
            margin-bottom: 24px;
        }

        .form-label {
            display: block;
            margin-bottom: 8px;
            font-weight: 500;
        }

        .form-input, .form-textarea, .form-select {
            width: 100%;
            padding: 12px;
            border: 1px solid #e0e0e0;
            border-radius: 6px;
            font-size: 16px;
        }

        .form-textarea {
            resize: vertical;
            min-height: 100px;
        }

        .urgency-buttons {
            display: flex;
            gap: 12px;
        }

        .urgency-btn {
            padding: 8px 16px;
            border: 1px solid #e0e0e0;
            border-radius: 20px;
            background: white;
            cursor: pointer;
            transition: all 0.15s;
        }

        .urgency-btn.active {
            background: #BA7517;
            color: white;
            border-color: #BA7517;
        }

        .success-state {
            display: none;
            text-align: center;
        }

        .ai-match {
            background: linear-gradient(135deg, #378ADD, #7F77DD);
            color: white;
            border-radius: 12px;
            padding: 24px;
            margin-bottom: 24px;
        }

        .match-cards {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 16px;
            margin-top: 16px;
        }

        .match-card {
            background: rgba(255, 255, 255, 0.1);
            border-radius: 8px;
            padding: 16px;
            text-align: center;
        }

        .avatar {
            width: 40px;
            height: 40px;
            border-radius: 50%;
            background: rgba(255, 255, 255, 0.2);
            display: flex;
            align-items: center;
            justify-content: center;
            font-weight: bold;
            margin: 0 auto 8px;
        }

        .success-card {
            background: white;
            border: 0.5px solid #e0e0e0;
            border-radius: 12px;
            padding: 24px;
            max-width: 400px;
            margin: 0 auto;
        }

        .checkmark {
            width: 48px;
            height: 48px;
            border-radius: 50%;
            background: #1D9E75;
            display: flex;
            align-items: center;
            justify-content: center;
            color: white;
            font-size: 24px;
            margin: 0 auto 16px;
        }

        /* Login Page */
        .login-container {
            max-width: 400px;
            margin: 0 auto;
        }

        .login-card {
            background: linear-gradient(180deg, #ffffff 0%, #f7fbff 100%);
            border: 1px solid rgba(55, 138, 221, 0.15);
            border-radius: 24px;
            padding: 36px;
            text-align: center;
            box-shadow: 0 16px 40px rgba(55, 138, 221, 0.08);
        }

        .login-card::before {
            content: '';
            position: absolute;
            top: -20px;
            right: -20px;
            width: 120px;
            height: 120px;
            border-radius: 50%;
            background: rgba(127, 119, 221, 0.12);
            z-index: 0;
        }

        .login-card > * {
            position: relative;
            z-index: 1;
        }

        .login-tabs {
            display: flex;
            margin-bottom: 24px;
            border-bottom: 1px solid rgba(55, 138, 221, 0.15);
            background: rgba(255, 255, 255, 0.85);
            border-radius: 16px;
            overflow: hidden;
        }

        .login-tab {
            flex: 1;
            padding: 12px;
            cursor: pointer;
            border-bottom: 2px solid transparent;
            transition: all 0.15s;
        }

        .login-tab.active {
            border-bottom-color: #378ADD;
            color: #378ADD;
            background: rgba(55, 138, 221, 0.08);
            font-weight: 700;
        }

        .login-form {
            display: none;
        }

        .login-form.active {
            display: block;
        }

        .login-input {
            width: 100%;
            padding: 12px;
            border: 1px solid #e0e0e0;
            border-radius: 6px;
            font-size: 16px;
            margin-bottom: 16px;
        }

        .login-btn {
            width: 100%;
            padding: 12px;
            background: linear-gradient(135deg, #378ADD 0%, #7F77DD 100%);
            color: white;
            border: none;
            border-radius: 10px;
            font-size: 16px;
            cursor: pointer;
            transition: all 0.2s ease;
            box-shadow: 0 12px 24px rgba(55, 138, 221, 0.16);
        }

        .login-btn:hover {
            transform: translateY(-2px);
            box-shadow: 0 16px 28px rgba(55, 138, 221, 0.24);
        }

        .login-footer {
            margin-top: 24px;
            font-size: 14px;
            color: #666;
        }

        .login-link {
            color: #378ADD;
            cursor: pointer;
            text-decoration: underline;
        }

        /* Volunteer Dashboard */
        .filter {
            margin-bottom: 32px;
        }

        .task-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
            gap: 24px;
        }

        .task-card {
            background: white;
            border: 0.5px solid #e0e0e0;
            border-radius: 12px;
            padding: 24px;
        }

        .task-title {
            font-size: 18px;
            font-weight: bold;
            margin-bottom: 12px;
        }

        .badge {
            display: inline-block;
            padding: 4px 8px;
            border-radius: 12px;
            font-size: 12px;
            font-weight: 500;
        }

        .badge.education {
            background: #EEEDFE;
            color: #3C3489;
        }

        .badge.medical {
            background: #FCEBEB;
            color: #791F1F;
        }

        .badge.delivery {
            background: #FAEEDA;
            color: #633806;
        }

        .badge.misc {
            background: #F1EFE8;
            color: #444441;
        }

        .badge.urgency-high {
            background: #FCEBEB;
            color: #791F1F;
        }

        .badge.urgency-medium {
            background: #FAEEDA;
            color: #BA7517;
        }

        .badge.urgency-low {
            background: #E1F5EE;
            color: #1D9E75;
        }

        .task-meta {
            display: flex;
            gap: 12px;
            margin: 12px 0;
            font-size: 14px;
            color: #666;
        }

        .task-desc {
            margin-bottom: 16px;
            color: #666;
        }

        .btn-accept {
            width: 100%;
            padding: 12px;
            background: #378ADD;
            color: white;
            border: none;
            border-radius: 6px;
            cursor: pointer;
            transition: all 0.15s;
        }

        .btn-accept:hover:not(:disabled) {
            background: #2c6cb8;
        }

        .btn-accept.accepted {
            background: #1D9E75;
            cursor: default;
        }

        /* Profile */
        .profile-header {
            text-align: center;
            margin-bottom: 32px;
        }

        .profile-avatar {
            width: 80px;
            height: 80px;
            border-radius: 50%;
            background: #378ADD;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 32px;
            font-weight: bold;
            color: white;
            margin: 0 auto 16px;
        }

        .profile-name {
            font-size: 24px;
            font-weight: bold;
            margin-bottom: 4px;
        }

        .profile-subtitle {
            color: #666;
        }

        .trust-badge {
            display: inline-block;
            padding: 4px 12px;
            background: #FAEEDA;
            color: #BA7517;
            border-radius: 12px;
            font-size: 14px;
            margin-top: 8px;
        }

        .skills-card {
            background: white;
            border: 0.5px solid #e0e0e0;
            border-radius: 12px;
            padding: 24px;
            margin-bottom: 24px;
        }

        .skills-tags {
            display: flex;
            gap: 8px;
            flex-wrap: wrap;
        }

        .skill-tag {
            padding: 6px 12px;
            background: #E6F1FB;
            color: #378ADD;
            border-radius: 16px;
            font-size: 14px;
        }

        .trust-journey {
            background: white;
            border: 0.5px solid #e0e0e0;
            border-radius: 12px;
            padding: 24px;
        }

        .progress-bar {
            display: flex;
            height: 8px;
            border-radius: 4px;
            overflow: hidden;
            margin-bottom: 16px;
        }

        .progress-segment {
            flex: 1;
            background: #e0e0e0;
        }

        .progress-segment.filled {
            background: #1D9E75;
        }

        .progress-segment.silver {
            background: #BA7517;
        }

        .progress-labels {
            display: flex;
            justify-content: space-between;
            font-size: 14px;
            color: #666;
        }

        /* Toast */
        .toast {
            position: fixed;
            bottom: 20px;
            right: 20px;
            background: rgba(0, 0, 0, 0.8);
            color: white;
            padding: 12px 16px;
            border-radius: 6px;
            opacity: 0;
            pointer-events: none;
            transition: opacity 0.3s;
            z-index: 1000;
        }

        .toast.show {
            opacity: 1;
        }

        /* Mobile */
        @media (max-width: 768px) {
            .hero h1 {
                font-size: 32px;
            }

            .hero p {
                font-size: 16px;
            }

            .cta-buttons {
                flex-direction: column;
                align-items: center;
            }

            .nav-links {
                gap: 8px;
                flex-wrap: wrap;
            }

            .auth-buttons {
                margin-left: 12px;
                flex-direction: column;
                gap: 4px;
            }

            .auth-buttons .btn {
                padding: 6px 12px;
                font-size: 12px;
            }

            .language-toggle {
                margin-left: 12px;
            }

            .lang-btn {
                padding: 4px 8px;
                font-size: 11px;
            }

            .task-grid {
                grid-template-columns: 1fr;
            }

            .match-cards {
                grid-template-columns: 1fr;
            }

            .navbar .container {
                padding: 0 12px;
            }

            .btn, .nav-link, .lang-btn {
                min-height: 44px; /* iOS touch target */
                min-width: 44px;
            }

            .toast {
                bottom: 10px;
                left: 10px;
                right: 10px;
                margin: 0 auto;
                max-width: 300px;
            }

            .form-input, .form-textarea, .login-input {
                font-size: 16px; /* Prevents zoom on iOS */
            }
        }

        /* Extra small phones */
        @media (max-width: 480px) {
            .hero h1 {
                font-size: 28px;
            }

            .hero p {
                font-size: 14px;
            }

            .navbar .container {
                flex-wrap: wrap;
                justify-content: space-between;
                padding: 8px 12px;
            }

            .nav-links {
                order: 3;
                width: 100%;
                justify-content: center;
                margin-top: 8px;
            }

            .auth-buttons {
                order: 2;
                margin-left: 0;
            }

            .language-toggle {
                order: 1;
            }

            .cta-buttons .btn {
                width: 100%;
                margin-bottom: 8px;
            }

            .stats {
                grid-template-columns: 1fr;
            }

            .task-card, .match-card {
                padding: 12px;
            }
        }
    </style>
</head>
<body>
    <nav class="navbar">
        <div class="container">
            <div class="logo">Need<span class="pulse">Pulse</span></div>
            <div class="nav-links">
                <div class="nav-link active" data-page="landing" data-translate="home">Home</div>
                <div class="nav-link" data-page="dashboard" data-translate="dashboard">Dashboard</div>
                <div class="nav-link" data-page="post" data-translate="postNeed">Post a Need</div>
                <div class="nav-link" data-page="volunteer" data-translate="volunteer">Volunteer</div>
                <div class="nav-link" id="profile-nav" style="display: none;" data-page="profile" data-translate="profile">Profile</div>
            </div>
            <div class="auth-buttons" id="auth-buttons">
                <button class="btn btn-outline" onclick="openSignup()" style="margin-right: 8px; padding: 8px 16px;" data-translate="signUpBtn">Sign Up</button>
                <button class="btn btn-primary" onclick="openSignin()" style="padding: 8px 16px;" data-translate="loginBtn">Login</button>
            </div>
            <div class="language-toggle">
                <button class="lang-btn active" data-lang="en">EN</button>
                <button class="lang-btn" data-lang="hi">हि</button>
            </div>
        </div>
    </nav>

    <div id="toast" class="toast"></div>

    <!-- Landing Page -->
    <div id="landing" class="page active">
        <div class="container">
            <div class="hero">
                <h1 data-translate="heroTitle">Connecting local help to the right people, instantly</h1>
                <p data-translate="heroSubtitle">Join our community of volunteers making a difference in everyday lives</p>
                <div class="cta-buttons">
                    <button class="btn btn-primary" onclick="navigateTo(&#39;post&#39;)" data-translate="postNeedBtn">Post a Need</button>
                    <button class="btn btn-outline" onclick="navigateTo(&#39;volunteer&#39;)" data-translate="becomeVolunteerBtn">Become a Volunteer</button>
                    <button class="btn btn-outline" onclick="navigateTo(&#39;login&#39;)" style="font-size: 14px; padding: 10px 16px;" data-translate="loginBtn">Login</button>
                </div>
            </div>

            <div class="stats">
                <div class="stat-card card-hover fade-in">
                    <div class="stat-number" id="volunteer-count" style="">248</div>
                    <div class="stat-label" data-translate="activeVolunteers">Active volunteers</div>
                </div>
                <div class="stat-card card-hover fade-in">
                    <div class="stat-number">1,430</div>
                    <div class="stat-label" data-translate="tasksCompleted">Tasks completed</div>
                </div>
                <div class="stat-card card-hover fade-in">
                    <div class="stat-number">34</div>
                    <div class="stat-label" data-translate="communitiesHelped">Communities helped</div>
                </div>
            </div>

            <div class="activity-feed card-hover fade-in">
                <h3 style="margin-bottom: 16px;" data-translate="liveActivity">Live Activity</h3>
                <div class="activity-item">
                    <div class="activity-dot"></div>
                    <div>Math tutoring request posted in Indore</div>
                </div>
                <div class="activity-item">
                    <div class="activity-dot purple"></div>
                    <div>Medicine delivery completed successfully</div>
                </div>
                <div class="activity-item">
                    <div class="activity-dot amber"></div>
                    <div>New volunteer joined the platform</div>
                </div>
            </div>
        </div>
    </div>

    <!-- Dashboard -->
    <div id="dashboard" class="page">
        <div class="container">
            <div class="tabs">
                <div class="tab active">Overview</div>
                <div class="tab">Nearby tasks</div>
                <div class="tab">My tasks</div>
            </div>

            <div class="metric-cards">
                <div class="metric-card">
                    <div class="metric-number">12</div>
                    <div class="metric-label">Tasks near you</div>
                </div>
                <div class="metric-card">
                    <div class="metric-number">3</div>
                    <div class="metric-label">You're helping with</div>
                </div>
            </div>

            <div class="map-placeholder">
                <div class="map-pin" style="top: 20%; left: 30%;">📍</div>
                <div class="map-pin" style="top: 40%; left: 60%;">📍</div>
                <div class="map-pin" style="top: 60%; left: 20%;">📍</div>
                <div class="map-pin" style="top: 70%; left: 70%;">📍</div>
                <div class="map-pin" style="top: 30%; left: 80%;">📍</div>
                <div class="map-label">Tasks near Indore</div>
            </div>

            <div class="activity-feed">
                <h3 style="margin-bottom: 16px;">Recent Activity</h3>
                <div class="activity-item">
                    <div class="activity-dot"></div>
                    <div>You accepted a tutoring task</div>
                </div>
                <div class="activity-item">
                    <div class="activity-dot purple"></div>
                    <div>Medicine delivery completed</div>
                </div>
                <div class="activity-item">
                    <div class="activity-dot amber"></div>
                    <div>New task posted nearby</div>
                </div>
            </div>
        </div>
    </div>

    <!-- Post a Need -->
    <div id="post" class="page">
        <div class="container">
            <div id="post-form" class="form-card">
                <h2 style="margin-bottom: 24px;">Post a Need</h2>
                <form id="need-form">
                    <div class="form-group">
                        <label class="form-label">Title</label>
                        <input type="text" class="form-input" id="title" required="">
                    </div>
                    <div class="form-group">
                        <label class="form-label">Category</label>
                        <select class="form-select" id="category">
                            <option value="education">Education</option>
                            <option value="delivery">Delivery</option>
                            <option value="medical">Medical</option>
                            <option value="misc">Miscellaneous</option>
                        </select>
                    </div>
                    <div class="form-group">
                        <label class="form-label">Location</label>
                        <input type="text" class="form-input" id="location">
                    </div>
                    <div class="form-group">
                        <label class="form-label">Description</label>
                        <textarea class="form-textarea" id="description"></textarea>
                    </div>
                    <div class="form-group">
                        <label class="form-label">Urgency</label>
                        <div class="urgency-buttons">
                            <button type="button" class="urgency-btn" data-urgency="low">Low</button>
                            <button type="button" class="urgency-btn active" data-urgency="medium">Medium</button>
                            <button type="button" class="urgency-btn" data-urgency="high">High</button>
                        </div>
                    </div>
                    <button type="submit" class="btn btn-primary" style="width: 100%;">Post Request</button>
                </form>
            </div>

            <div id="success-state" class="success-state">
                <div class="ai-match">
                    <h3>AI-Powered Matches</h3>
                    <p>Based on your request, we've found the best volunteers nearby</p>
                    <div class="match-cards">
                        <div class="match-card">
                            <div class="avatar">RK</div>
                            <div>Rahul Kumar</div>
                            <div>0.8km • Tutoring • 95% match</div>
                        </div>
                        <div class="match-card">
                            <div class="avatar">PK</div>
                            <div>Priya Kapoor</div>
                            <div>1.2km • Education • 88% match</div>
                        </div>
                        <div class="match-card">
                            <div class="avatar">AS</div>
                            <div>Amit Singh</div>
                            <div>1.5km • Teaching • 82% match</div>
                        </div>
                    </div>
                </div>

                <div class="success-card">
                    <div class="checkmark">✓</div>
                    <h3>Request posted successfully</h3>
                    <p>3 volunteers have been notified nearby</p>
                    <button class="btn btn-outline" onclick="resetForm()" style="margin-top: 16px;">Post another request</button>
                </div>
            </div>
        </div>
    </div>

    <!-- Volunteer Dashboard -->
    <div id="volunteer" class="page">
        <div class="container">
            <div class="filter">
                <select class="form-select" id="category-filter" style="max-width: 200px;">
                    <option value="all">All categories</option>
                    <option value="education">Education</option>
                    <option value="delivery">Delivery</option>
                    <option value="medical">Medical</option>
                </select>
            </div>

            <div class="task-grid">
                <div class="task-card" data-category="education">
                    <div class="task-title">Math tutoring help</div>
                    <div class="badge education">Education</div>
                    <div class="task-meta">
                        <span>0.8km</span>
                        <span>15 min ago</span>
                        <span class="badge urgency-medium">Medium</span>
                    </div>
                    <div class="task-desc">Need help with algebra and geometry for high school student</div>
                    <button class="btn-accept" onclick="acceptTask(this)">Accept task</button>
                </div>

                <div class="task-card" data-category="medical">
                    <div class="task-title">Medicine delivery</div>
                    <div class="badge medical">Medical</div>
                    <div class="task-meta">
                        <span>1.2km</span>
                        <span>32 min ago</span>
                        <span class="badge urgency-high">High</span>
                    </div>
                    <div class="task-desc">Urgent delivery of prescription medicines to elderly patient</div>
                    <button class="btn-accept" onclick="acceptTask(this)">Accept task</button>
                </div>

                <div class="task-card" data-category="delivery">
                    <div class="task-title">Grocery pickup</div>
                    <div class="badge delivery">Delivery</div>
                    <div class="task-meta">
                        <span>2.0km</span>
                        <span>1hr ago</span>
                        <span class="badge urgency-low">Low</span>
                    </div>
                    <div class="task-desc">Pick up groceries from local store and deliver to home</div>
                    <button class="btn-accept" onclick="acceptTask(this)">Accept task</button>
                </div>

                <div class="task-card" data-category="misc">
                    <div class="task-title">NGO pamphlet distribution</div>
                    <div class="badge misc">Misc</div>
                    <div class="task-meta">
                        <span>3.4km</span>
                        <span>2hrs ago</span>
                        <span class="badge urgency-low">Low</span>
                    </div>
                    <div class="task-desc">Help distribute awareness pamphlets in the neighborhood</div>
                    <button class="btn-accept" onclick="acceptTask(this)">Accept task</button>
                </div>
            </div>
        </div>
    </div>

    <!-- Profile -->
    <div id="profile" class="page">
        <div class="container">
            <div class="profile-header">
                <div class="profile-avatar">AK</div>
                <div class="profile-name">Arjun Khanna</div>
                <div class="profile-subtitle">Volunteer since Jan 2024</div>
                <div class="trust-badge">Silver</div>
            </div>

            <div class="metric-cards">
                <div class="metric-card">
                    <div class="metric-number">24</div>
                    <div class="metric-label">Tasks completed</div>
                </div>
                <div class="metric-card">
                    <div class="metric-number">38h</div>
                    <div class="metric-label">Hours contributed</div>
                </div>
            </div>

            <div class="skills-card">
                <h3 style="margin-bottom: 16px;">Skills</h3>
                <div class="skills-tags">
                    <div class="skill-tag">Tutoring</div>
                    <div class="skill-tag">Delivery</div>
                    <div class="skill-tag">Medical escort</div>
                    <div class="skill-tag">Translation</div>
                </div>
            </div>

            <div class="trust-journey">
                <h3 style="margin-bottom: 16px;">Trust Journey</h3>
                <div class="progress-bar">
                    <div class="progress-segment filled"></div>
                    <div class="progress-segment silver filled"></div>
                    <div class="progress-segment"></div>
                </div>
                <div class="progress-labels">
                    <span>Bronze ✓</span>
                    <span>Silver ✓</span>
                    <span>Gold (50 tasks)</span>
                </div>
            </div>

            <div style="text-align: center; margin-top: 32px;">
                <button class="btn btn-outline" onclick="logoutUser()" style="background: linear-gradient(135deg, #ff6b6b 0%, #ee5a52 100%); border: none; color: white;" data-translate="logoutBtn">Logout</button>
            </div>
        </div>
    </div>

    <!-- Login Page -->
    <div id="login" class="page">
        <div class="container">
            <div class="login-container">
                <div class="login-card">
                    <h2 style="margin-bottom: 24px;" data-translate="welcome">Welcome to NeedPulse</h2>

                    <div class="login-tabs">
                        <div class="login-tab active" data-form="signin" data-translate="signIn">Sign In</div>
                        <div class="login-tab" data-form="signup" data-translate="signUp">Sign Up</div>
                    </div>

                    <form id="signin-form" class="login-form active">
                        <input type="email" class="login-input" data-translate-placeholder="email" placeholder="Email address" required="">
                        <input type="password" class="login-input" data-translate-placeholder="password" placeholder="Password" required="">
                        <button type="submit" class="login-btn" data-translate="signIn">Sign In</button>
                    </form>

                    <form id="signup-form" class="login-form">
                        <input type="text" class="login-input" data-translate-placeholder="fullName" placeholder="Full name" required="">
                        <input type="email" class="login-input" data-translate-placeholder="email" placeholder="Email address" required="">
                        <input type="password" class="login-input" data-translate-placeholder="password" placeholder="Password" required="">
                        <input type="password" class="login-input" data-translate-placeholder="confirmPassword" placeholder="Confirm password" required="">
                        <button type="submit" class="login-btn" data-translate="createAccount">Create Account</button>
                    </form>

                    <div class="login-footer">
                        <div id="signin-footer">
                            <span data-translate="dontHaveAccount">Don't have an account?</span> <span class="login-link" onclick="switchToSignup()" data-translate="signUp">Sign up</span>
                        </div>
                        <div id="signup-footer" style="display: none;">
                            <span data-translate="alreadyHaveAccount">Already have an account?</span> <span class="login-link" onclick="switchToSignin()" data-translate="signIn">Sign in</span>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <script>
        // Translations
        const translations = {
            en: {
                // Navigation
                home: "Home",
                dashboard: "Dashboard",
                postNeed: "Post a Need",
                volunteer: "Volunteer",
                profile: "Profile",
                login: "Login",

                // Landing Page
                heroTitle: "Connecting local help to the right people, instantly",
                heroSubtitle: "Join our community of volunteers making a difference in everyday lives",
                postNeedBtn: "Post a Need",
                becomeVolunteerBtn: "Become a Volunteer",
                loginBtn: "Login",
                activeVolunteers: "Active volunteers",
                tasksCompleted: "Tasks completed",
                communitiesHelped: "Communities helped",
                liveActivity: "Live Activity",

                // Dashboard
                overview: "Overview",
                nearbyTasks: "Nearby tasks",
                myTasks: "My tasks",
                tasksNearYou: "Tasks near you",
                youreHelpingWith: "You're helping with",
                tasksNear: "Tasks near",
                recentActivity: "Recent Activity",
                youAcceptedTask: "You accepted a tutoring task",
                medicineDelivered: "Medicine delivery completed",
                newTaskNearby: "New task posted nearby",

                // Post Need
                postNeedTitle: "Post a Need",
                title: "Title",
                category: "Category",
                education: "Education",
                delivery: "Delivery",
                medical: "Medical",
                miscellaneous: "Miscellaneous",
                location: "Location",
                description: "Description",
                urgency: "Urgency",
                low: "Low",
                medium: "Medium",
                high: "High",
                postRequest: "Post Request",
                pleaseAddTitle: "Please add a title",
                requestPosted: "Request posted successfully",
                volunteersNotified: "3 volunteers have been notified nearby",
                postAnother: "Post another request",

                // AI Match
                aiMatch: "AI-Powered Matches",
                aiMatchDesc: "Based on your request, we've found the best volunteers nearby",
                match: "match",

                // Volunteer Dashboard
                allCategories: "All categories",
                mathTutoring: "Math tutoring help",
                medicineDelivery: "Medicine delivery",
                groceryPickup: "Grocery pickup",
                ngoDistribution: "NGO pamphlet distribution",
                km: "km",
                minAgo: "min ago",
                hrAgo: "hr ago",
                hrsAgo: "hrs ago",
                acceptTask: "Accept task",
                taskAccepted: "Task accepted — the requester has been notified",

                // Profile
                volunteerSince: "Volunteer since",
                tasksCompleted: "Tasks completed",
                hoursContributed: "Hours contributed",
                skills: "Skills",
                tutoring: "Tutoring",
                medicalEscort: "Medical escort",
                translation: "Translation",
                trustJourney: "Trust Journey",
                bronze: "Bronze",
                silver: "Silver",
                gold: "Gold",
                tasks: "tasks",

                // Login
                welcome: "Welcome to NeedPulse",
                signIn: "Sign In",
                signUp: "Sign Up",
                fullName: "Full name",
                email: "Email address",
                password: "Password",
                confirmPassword: "Confirm password",
                createAccount: "Create Account",
                dontHaveAccount: "Don't have an account?",
                alreadyHaveAccount: "Already have an account?",
                signUpBtn: "Sign Up",
                loginBtn: "Login",
                loginSuccess: "Successfully logged in! Welcome back.",
                logoutSuccess: "Successfully logged out.",
                logoutBtn: "Logout",
                loginFirst: "Please log in to view your profile.",
                signUpSuccess: "Account created successfully! Welcome to NeedPulse.",
                passwordsDontMatch: "Passwords do not match"
            },
            hi: {
                // Navigation
                home: "होम",
                dashboard: "डैशबोर्ड",
                postNeed: "ज़रूरत पोस्ट करें",
                volunteer: "स्वयंसेवक बनें",
                profile: "प्रोफ़ाइल",
                login: "लॉगिन",

                // Landing Page
                heroTitle: "स्थानीय मदद को सही लोगों से तुरंत जोड़ना",
                heroSubtitle: "हमारे समुदाय में शामिल हों जहां स्वयंसेवक रोजमर्रा की जिंदगी में बदलाव ला रहे हैं",
                postNeedBtn: "ज़रूरत पोस्ट करें",
                becomeVolunteerBtn: "स्वयंसेवक बनें",
                loginBtn: "लॉगिन",
                activeVolunteers: "सक्रिय स्वयंसेवक",
                tasksCompleted: "पूर्ण किए गए कार्य",
                communitiesHelped: "मदद किए गए समुदाय",
                liveActivity: "लाइव गतिविधि",

                // Dashboard
                overview: "अवलोकन",
                nearbyTasks: "आस-पास के कार्य",
                myTasks: "मेरे कार्य",
                tasksNearYou: "आपके आस-पास के कार्य",
                youreHelpingWith: "आप जिनकी मदद कर रहे हैं",
                tasksNear: "आस-पास के कार्य",
                recentActivity: "हाल की गतिविधि",
                youAcceptedTask: "आपने ट्यूशन कार्य स्वीकार किया",
                medicineDelivered: "दवा वितरण पूरा हुआ",
                newTaskNearby: "आस-पास नया कार्य पोस्ट हुआ",

                // Post Need
                postNeedTitle: "ज़रूरत पोस्ट करें",
                title: "शीर्षक",
                category: "श्रेणी",
                education: "शिक्षा",
                delivery: "वितरण",
                medical: "चिकित्सा",
                miscellaneous: "विविध",
                location: "स्थान",
                description: "विवरण",
                urgency: "तात्कालिकता",
                low: "कम",
                medium: "मध्यम",
                high: "उच्च",
                postRequest: "अनुरोध पोस्ट करें",
                pleaseAddTitle: "कृपया शीर्षक जोड़ें",
                requestPosted: "अनुरोध सफलतापूर्वक पोस्ट हुआ",
                volunteersNotified: "3 स्वयंसेवकों को आस-पास सूचित किया गया",
                postAnother: "एक और अनुरोध पोस्ट करें",

                // AI Match
                aiMatch: "AI-संचालित मिलान",
                aiMatchDesc: "आपके अनुरोध के आधार पर, हमने आस-पास के सर्वोत्तम स्वयंसेवकों को ढूंढा है",
                match: "मिलान",

                // Volunteer Dashboard
                allCategories: "सभी श्रेणियां",
                mathTutoring: "गणित ट्यूशन मदद",
                medicineDelivery: "दवा वितरण",
                groceryPickup: "किराने की उठान",
                ngoDistribution: "NGO पर्चा वितरण",
                km: "किमी",
                minAgo: "मिनट पहले",
                hrAgo: "घंटा पहले",
                hrsAgo: "घंटे पहले",
                acceptTask: "कार्य स्वीकार करें",
                taskAccepted: "कार्य स्वीकार किया गया — अनुरोधकर्ता को सूचित किया गया",

                // Profile
                volunteerSince: "स्वयंसेवक बनें",
                tasksCompleted: "पूर्ण किए गए कार्य",
                hoursContributed: "योगदान किए गए घंटे",
                skills: "कौशल",
                tutoring: "ट्यूशन",
                medicalEscort: "चिकित्सा सहायता",
                translation: "अनुवाद",
                trustJourney: "विश्वास यात्रा",
                bronze: "कांस्य",
                silver: "रजत",
                gold: "स्वर्ण",
                tasks: "कार्य",

                // Login
                welcome: "NeedPulse में आपका स्वागत है",
                signIn: "साइन इन",
                signUp: "साइन अप",
                fullName: "पूरा नाम",
                email: "ईमेल पता",
                password: "पासवर्ड",
                confirmPassword: "पासवर्ड की पुष्टि करें",
                createAccount: "खाता बनाएं",
                dontHaveAccount: "खाता नहीं है?",
                alreadyHaveAccount: "पहले से खाता है?",
                signUpBtn: "साइन अप",
                loginBtn: "लॉगिन",
                loginSuccess: "सफलतापूर्वक लॉग इन! वापस स्वागत है।",
                logoutSuccess: "सफलतापूर्वक लॉग आउट।",
                logoutBtn: "लॉग आउट",
                loginFirst: "कृपया अपनी प्रोफ़ाइल देखने के लिए लॉग इन करें।",
                signUpSuccess: "खाता सफलतापूर्वक बनाया गया! NeedPulse में आपका स्वागत है।",
                passwordsDontMatch: "पासवर्ड मेल नहीं खाते"
            }
        };

        let currentLang = 'en';
        let isLoggedIn = false;

        // Authentication functions
        function loginUser() {
            isLoggedIn = true;
            document.getElementById('auth-buttons').style.display = 'none';
            document.getElementById('profile-nav').style.display = 'block';
            showToast('loginSuccess');
        }

        function logoutUser() {
            isLoggedIn = false;
            document.getElementById('auth-buttons').style.display = 'flex';
            document.getElementById('profile-nav').style.display = 'none';
            navigateTo('landing');
            showToast('logoutSuccess');
        }

        function openSignin() {
            switchToSignin();
            navigateTo('login');
        }

        function openSignup() {
            switchToSignup();
            navigateTo('login');
        }

        // Language switching function
        function switchLanguage(lang) {
            currentLang = lang;
            document.querySelectorAll('.lang-btn').forEach(btn => {
                btn.classList.toggle('active', btn.dataset.lang === lang);
            });

            // Update all translatable elements
            document.querySelectorAll('[data-translate]').forEach(element => {
                const key = element.dataset.translate;
                if (translations[lang][key]) {
                    element.textContent = translations[lang][key];
                }
            });

            // Update placeholders
            document.querySelectorAll('[data-translate-placeholder]').forEach(element => {
                const key = element.dataset.translatePlaceholder;
                if (translations[lang][key]) {
                    element.placeholder = translations[lang][key];
                }
            });

            // Update form values and other attributes
            document.querySelectorAll('[data-translate-value]').forEach(element => {
                const key = element.dataset.translateValue;
                if (translations[lang][key]) {
                    element.value = translations[lang][key];
                }
            });

            showToast(`Language switched to ${lang === 'en' ? 'English' : 'हिंदी'}`);
        }

        // Navigation
        function navigateTo(page) {
            if (page === 'profile' && !isLoggedIn) {
                openSignin();
                showToast('loginFirst');
                return;
            }

            document.querySelectorAll('.page').forEach(p => p.classList.remove('active'));
            document.querySelectorAll('.nav-link').forEach(n => n.classList.remove('active'));
            document.getElementById(page).classList.add('active');
            const navLink = document.querySelector(`[data-page="${page}"]`);
            if (navLink) {
                navLink.classList.add('active');
            }
        }

        document.querySelectorAll('.nav-link').forEach(link => {
            link.addEventListener('click', () => {
                const page = link.dataset.page;
                navigateTo(page);
            });
        });

        // Language switching
        document.querySelectorAll('.lang-btn').forEach(btn => {
            btn.addEventListener('click', () => {
                const lang = btn.dataset.lang;
                switchLanguage(lang);
            });
        });

        // Enhanced interactions
        document.querySelectorAll('.stat-card').forEach(card => {
            card.addEventListener('click', () => {
                card.style.transform = 'scale(0.95)';
                setTimeout(() => {
                    card.style.transform = '';
                }, 150);
            });
        });

        // Add pulse animation to volunteer counter
        const volunteerCounter = document.getElementById('volunteer-count');
        let pulseInterval = setInterval(() => {
            volunteerCounter.style.transform = 'scale(1.05)';
            setTimeout(() => {
                volunteerCounter.style.transform = '';
            }, 200);
        }, 10000); // Pulse every 10 seconds

        // Form handling
        const form = document.getElementById('need-form');
        const postForm = document.getElementById('post-form');
        const successState = document.getElementById('success-state');

        form.addEventListener('submit', async (e) => {
            e.preventDefault();
            const submitBtn = form.querySelector('button[type="submit"]');
            const title = document.getElementById('title').value.trim();

            if (!title) {
                showToast(translations[currentLang].pleaseAddTitle || 'Please add a title');
                return;
            }

            // Show loading state
            submitBtn.classList.add('loading');
            submitBtn.disabled = true;

            // Simulate API call
            await new Promise(resolve => setTimeout(resolve, 1500));

            // Hide loading and show success
            submitBtn.classList.remove('loading');
            submitBtn.disabled = false;

            postForm.style.display = 'none';
            successState.style.display = 'block';
            successState.classList.add('fade-in');
        });

        function resetForm() {
            form.reset();
            document.querySelectorAll('.urgency-btn').forEach(btn => btn.classList.remove('active'));
            document.querySelector('[data-urgency="medium"]').classList.add('active');
            successState.style.display = 'none';
            postForm.style.display = 'block';
        }

        // Urgency buttons
        document.querySelectorAll('.urgency-btn').forEach(btn => {
            btn.addEventListener('click', () => {
                document.querySelectorAll('.urgency-btn').forEach(b => b.classList.remove('active'));
                btn.classList.add('active');
            });
        });

        // Accept task
        function acceptTask(button) {
            button.textContent = translations[currentLang].accepted || 'Accepted!';
            button.classList.add('accepted');
            button.disabled = true;
            showToast('taskAccepted');
        }

        // Filter tasks
        document.getElementById('category-filter').addEventListener('change', (e) => {
            const filter = e.target.value;
            document.querySelectorAll('.task-card').forEach(card => {
                if (filter === 'all' || card.dataset.category === filter) {
                    card.style.display = 'block';
                } else {
                    card.style.display = 'none';
                }
            });
        });

        // Toast
        function showToast(message) {
            const toast = document.getElementById('toast');
            const text = translations[currentLang][message] || message;
            toast.textContent = text;
            toast.classList.add('show');
            setTimeout(() => {
                toast.classList.remove('show');
            }, 3000);
        }

        // Login functionality
        function switchToSignup() {
            document.querySelectorAll('.login-tab').forEach(tab => tab.classList.remove('active'));
            document.querySelectorAll('.login-form').forEach(form => form.classList.remove('active'));
            document.querySelector('[data-form="signup"]').classList.add('active');
            document.getElementById('signup-form').classList.add('active');
            document.getElementById('signin-footer').style.display = 'none';
            document.getElementById('signup-footer').style.display = 'block';
        }

        function switchToSignin() {
            document.querySelectorAll('.login-tab').forEach(tab => tab.classList.remove('active'));
            document.querySelectorAll('.login-form').forEach(form => form.classList.remove('active'));
            document.querySelector('[data-form="signin"]').classList.add('active');
            document.getElementById('signin-form').classList.add('active');
            document.getElementById('signup-footer').style.display = 'none';
            document.getElementById('signin-footer').style.display = 'block';
        }

        // Login tab switching
        document.querySelectorAll('.login-tab').forEach(tab => {
            tab.addEventListener('click', () => {
                if (tab.dataset.form === 'signup') {
                    switchToSignup();
                } else {
                    switchToSignin();
                }
            });
        });

        // Login form handling
        document.getElementById('signin-form').addEventListener('submit', (e) => {
            e.preventDefault();
            showToast('signInSuccess');
            // In a real app, this would authenticate the user
            setTimeout(() => {
                loginUser();
                navigateTo('dashboard');
            }, 1000);
        });

        document.getElementById('signup-form').addEventListener('submit', (e) => {
            e.preventDefault();
            const password = e.target.querySelector('input[type="password"]').value;
            const confirmPassword = e.target.querySelectorAll('input[type="password"]')[1].value;

            if (password !== confirmPassword) {
                showToast('passwordsDontMatch');
                return;
            }

            showToast('signUpSuccess');
            // In a real app, this would create the user account
            setTimeout(() => {
                loginUser();
                navigateTo('dashboard');
            }, 1000);
        });
    </script>

</body></html>