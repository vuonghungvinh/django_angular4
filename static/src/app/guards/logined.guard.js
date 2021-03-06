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
var router_1 = require("@angular/router");
var alert_service_1 = require("../services/alert.service");
var LoginGurad = (function () {
    function LoginGurad(router, alertService) {
        this.router = router;
        this.alertService = alertService;
    }
    LoginGurad.prototype.canActivate = function (route, state) {
        if (localStorage.getItem("currentUser")) {
            this.alertService.success("You are logined.", true);
            this.router.navigate(['login'], { queryParams: { returnUrl: state.url } });
            return false;
        }
        return true;
    };
    return LoginGurad;
}());
LoginGurad = __decorate([
    core_1.Injectable(),
    __metadata("design:paramtypes", [router_1.Router, alert_service_1.AlertService])
], LoginGurad);
exports.LoginGurad = LoginGurad;
//# sourceMappingURL=logined.guard.js.map