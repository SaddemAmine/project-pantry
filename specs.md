# project-pantry: AHOY!

## 1. Overview
I’ve been struggling to keep track of what’s in my pantry, which inspired me to build a kitchen management app. The goal is to make it easier for people like me to stay organized and reduce food waste. What's very motivating and exciting is how there’s a lot of potential for growth within this idea.

This app could evolve to include features like smart inventory tracking, meal planning, shopping list integration, and even expiration date reminders.

## 2. Goals and Non-Goals
### Goals
- Manage inventory.
    - Track what's in the pantry, expiration dates and quantities.
- Meal planning.
- Suggest recipes based on available ingredients.
- Suggest recipes based on dietary preferences.
- Smart shopping list integration.
    - Could include product reviews and recommendations based on other users' experiences.

### Non-Goals
- No super fancy AI stuff for now. I want to focus on the features and refine them before including that.

## 3. Requirements
### Functional Requirements
- User authentication
- Managing pantry
    - CRUD operations for items.
    - Cooking a meal, i.e. deducting items from the pantry.
    - Meal planning
        - Suggest recipes based on available ingredients.
        - Calendar integration for the meal plan ?
    - Expiring item notifications.
        - "Use it or lose it" keep users aware of items that are going to expire soon.
        - Could immediately suggest recipes based on the expiring items.
- Shopping list management
    - Create shopping lists based on recipes or pantry needs.
    - Super long term but could include plugs for grocery delivery services.
- Recipe management
    - CRUD operations for recipes.
    - Suggest recipes based on dietary preferences. (not necessarily AI-driven, at least as a start)
        - Should include dietary tags.
        - Should give priority to recipes with ingredients that are expiring soon.
    - Scrape recipes from the web.

### Non-Functional Requirements
- Scalability, performance and availability

## 4. Architecture / Design
- Frontend
    - iOS app using SwiftUI.
    - Kotlin for Android.
    - Probably something React based or maybe trying out Vue for the web app.
- Backend
    - JS vs Python ?
        - Python could be better if we want to include AI features later on.
        - JS could be better for the web dev ecosystem. (although Python has Django and Flask) (Note to self: look into FastAPI)
    - Idk if REST or something GraphQL.
        - Probably REST for now, tried and tested.
    - PostgreSQL.
- Authentication
    - Auth.js ? Is there an alternative for Python ?
    - OAuth2 for social logins.
    - JWT for session management.

## 5. User Stories / Use Cases
TBD

## 6. Milestones & Timeline
For now as long as effort is put into the project, I’m happy. I’m not in a rush to finish it, but I do want to make progress.

### Phase 1: MVP
The bare minimum for me to actually be able to use this app in my daily life. This helps me stay motivated to keep working on it and also gives me a chance to become my own user and see what works and what doesn't.

This phase should include:
- Authentication
- Basic pantry management
    - CRUD operations for items.
    - Cooking a meal, i.e. deducting items from the pantry.
- Basic recipe management
- Basic meal planning
    - Suggest recipes based on available ingredients.

UI should be simple and functional, nothing fancy yet. I want the focus to be on the functionality and UX.

#### Phase N: TBD
TBD

## 7. Risks & Assumptions
### Risks
- Users might forget to update their pantry after using items... Maybe add a “cook meal” flow that updates it for them.

### Assumption
- Users will manually input items, at least at first, think about how tedious that might be and how you can ease it (barcode scan, photos, etc. later).
