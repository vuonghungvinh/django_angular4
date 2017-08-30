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
var http_1 = require("@angular/http");
var authentication_service_1 = require("../services/authentication.service");
var alert_service_1 = require("../services/alert.service");
var TwitterComponent = (function () {
    function TwitterComponent(router, auth, alertService) {
        this.router = router;
        this.auth = auth;
        this.alertService = alertService;
    }
    TwitterComponent.prototype.ngAfterViewInit = function () {
        var _this = this;
        this.router.events.subscribe(function (s) {
            var params = new http_1.URLSearchParams(s['url'].split("?")[1]);
            var oauth_token = params.get('oauth_token');
            var oauth_token_secret = params.get('oauth_token_secret');
            if (oauth_token && oauth_token_secret) {
                _this.auth.loginWithTwitter(oauth_token, oauth_token_secret).subscribe(function (data) {
                    _this.auth.loginWithSocial(data.key, 'twitter').subscribe(function (data) {
                        _this.alertService.success("Login success.", true);
                        _this.router.navigate(['/']);
                    }, function (errors) {
                        // console.error(errors);
                        _this.alertService.error("Can not login with twitter. PLease try again!", true);
                        _this.router.navigate(['/login']);
                    });
                }, function (errors) {
                    // console.log(errors);
                    _this.alertService.error("Can not login with twitter. PLease try again!", true);
                    _this.router.navigate(['/login']);
                });
            }
        });
    };
    return TwitterComponent;
}());
TwitterComponent = __decorate([
    core_1.Component({
        selector: "twitter-component",
        template: "<h1>Proccessing...",
        providers: [authentication_service_1.AuthenticationService]
    }),
    __metadata("design:paramtypes", [router_1.Router,
        authentication_service_1.AuthenticationService,
        alert_service_1.AlertService])
], TwitterComponent);
exports.TwitterComponent = TwitterComponent;
//# sourceMappingURL=twitter.component.js.map