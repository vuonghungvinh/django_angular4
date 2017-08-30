"use strict";
var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var __metadata = (this && this.__metadata) || function (k, v) {
    if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
};
Object.defineProperty(exports, "__esModule", { value: true });
var core_1 = require("@angular/core");
var common_service_1 = require("./services/common.service");
var authentication_service_1 = require("./services/authentication.service");
var router_1 = require("@angular/router");
var AppComponent = (function () {
    function AppComponent(commonService, authencativeService, router) {
        this.commonService = commonService;
        this.authencativeService = authencativeService;
        this.router = router;
    }
    AppComponent.prototype.onActivate = function (e, outlet) {
        document.body.scrollTop = 0;
    };
    AppComponent.prototype.logout = function () {
        this.authencativeService.logout();
        this.router.navigate(['/login']);
    };
    return AppComponent;
}());
AppComponent = __decorate([
    core_1.Component({
        selector: 'app-root',
        templateUrl: './app.component.html',
        styleUrls: ['./app.component.css'],
        providers: [common_service_1.CommonService]
    }),
    __metadata("design:paramtypes", [common_service_1.CommonService,
        authentication_service_1.AuthenticationService,
        router_1.Router])
], AppComponent);
exports.AppComponent = AppComponent;
//# sourceMappingURL=app.component.js.map