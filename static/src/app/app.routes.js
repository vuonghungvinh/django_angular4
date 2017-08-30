"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
var router_1 = require("@angular/router");
var home_component_1 = require("./home/home.component");
var addetail_component_1 = require("./addetail/addetail.component");
var login_component_1 = require("./login/login.component");
var mainregister_component_1 = require("./register/mainregister.component");
var individual_component_1 = require("./register/individual.component");
var business_component_1 = require("./register/business.component");
var twitter_component_1 = require("./twitter/twitter.component");
var auth_guard_1 = require("./guards/auth.guard");
var routing = [
    // {path: "", component: HomeComponent, canActivate: [AuthGurad]},
    { path: "", component: home_component_1.HomeComponent },
    { path: "ad-detail/:slug", component: addetail_component_1.AdDetailComponent },
    { path: "twitter", component: twitter_component_1.TwitterComponent },
    { path: "login", component: login_component_1.LoginComponent, canActivate: [auth_guard_1.AuthGurad] },
    { path: "register", component: mainregister_component_1.MainRegisterComponent, canDeactivate: [auth_guard_1.AuthGurad] },
    { path: "register/individual", component: individual_component_1.IndividualComponent, canDeactivate: [auth_guard_1.AuthGurad] },
    { path: "register/business", component: business_component_1.BusinessComponent, canDeactivate: [auth_guard_1.AuthGurad] },
    // {path: "trains", component: TrainComponent, canActivate: [AuthGurad]},
    { path: '**', redirectTo: '' }
];
exports.appRoutes = router_1.RouterModule.forRoot(routing);
//# sourceMappingURL=app.routes.js.map