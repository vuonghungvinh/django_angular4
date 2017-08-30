"use strict";
var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
Object.defineProperty(exports, "__esModule", { value: true });
var platform_browser_1 = require("@angular/platform-browser");
var core_1 = require("@angular/core");
var forms_1 = require("@angular/forms");
var app_routes_1 = require("./app.routes");
var http_1 = require("@angular/http");
var ng2_toastr_1 = require("ng2-toastr/ng2-toastr");
var animations_1 = require("@angular/platform-browser/animations");
var ngx_facebook_1 = require("ngx-facebook");
var app_component_1 = require("./app.component");
var home_component_1 = require("./home/home.component");
var addetail_component_1 = require("./addetail/addetail.component");
var slider_component_1 = require("./slider/slider.component");
var login_component_1 = require("./login/login.component");
var mainregister_component_1 = require("./register/mainregister.component");
var individual_component_1 = require("./register/individual.component");
var business_component_1 = require("./register/business.component");
var alert_component_1 = require("./alert/alert.component");
var alert_service_1 = require("./services/alert.service");
var authentication_service_1 = require("./services/authentication.service");
var common_service_1 = require("./services/common.service");
var twitter_component_1 = require("./twitter/twitter.component");
var sliderlocation_component_1 = require("./sliderlocation/sliderlocation.component");
var auth_guard_1 = require("./guards/auth.guard");
var logined_guard_1 = require("./guards/logined.guard");
var AppModule = (function () {
    function AppModule() {
    }
    return AppModule;
}());
AppModule = __decorate([
    core_1.NgModule({
        declarations: [
            app_component_1.AppComponent,
            home_component_1.HomeComponent,
            addetail_component_1.AdDetailComponent,
            slider_component_1.SliderComponent,
            login_component_1.LoginComponent,
            mainregister_component_1.MainRegisterComponent,
            individual_component_1.IndividualComponent,
            business_component_1.BusinessComponent,
            alert_component_1.AlertComponent,
            twitter_component_1.TwitterComponent,
            sliderlocation_component_1.SliderlocationComponent
        ],
        imports: [
            platform_browser_1.BrowserModule,
            animations_1.BrowserAnimationsModule,
            ng2_toastr_1.ToastModule.forRoot(),
            app_routes_1.appRoutes,
            forms_1.FormsModule,
            ngx_facebook_1.FacebookModule.forRoot(),
            http_1.HttpModule
        ],
        providers: [
            alert_service_1.AlertService,
            authentication_service_1.AuthenticationService,
            common_service_1.CommonService,
            auth_guard_1.AuthGurad,
            logined_guard_1.LoginGurad
        ],
        bootstrap: [app_component_1.AppComponent]
    })
], AppModule);
exports.AppModule = AppModule;
//# sourceMappingURL=app.module.js.map