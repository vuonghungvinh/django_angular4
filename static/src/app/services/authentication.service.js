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
var http_1 = require("@angular/http");
require("rxjs/add/operator/map");
var common_service_1 = require("./common.service");
var AuthenticationService = (function () {
    function AuthenticationService(_http, cmservice) {
        this._http = _http;
        this.cmservice = cmservice;
    }
    AuthenticationService.prototype.login = function (data) {
        return this._http.post('api/accounts/api-token-auth/', data).map(function (response) {
            var user = response.json();
            user['type'] = "normal";
            if (user && user.api_token) {
                localStorage.setItem('currentUser', JSON.stringify(user));
            }
        });
    };
    AuthenticationService.prototype.loginWithFacebook = function (access_token) {
        return this._http.post("api/accounts/rest-auth/facebook/", { 'access_token': access_token }).map(function (response) { return response.json(); });
    };
    AuthenticationService.prototype.loginWithGoogle = function (access_token) {
        return this._http.post("api/accounts/rest-auth/google/", { 'access_token': access_token }).map(function (response) { return response.json(); });
    };
    AuthenticationService.prototype.loginWithTwitter = function (access_token, token_secret) {
        return this._http.post("api/accounts/rest-auth/twitter/", { 'access_token': access_token, 'token_secret': token_secret }).map(function (responsive) { return responsive.json(); });
    };
    AuthenticationService.prototype.loginWithSocial = function (token, type) {
        return this._http.post('api/accounts/login-with-social/', {}, this.cmservice.jwt_social(token)).map(function (response) {
            var user = response.json();
            user['type'] = type;
            if (user.user && user.user.individual_user) {
                var avatar_url = user.user.individual_user.avatar.replace(/%3A/g, ":/").replace(/%3F/g, "?").replace(/%3D/g, "=").replace(/%26/g, '&');
                user.user.individual_user.avatar = avatar_url.substring(avatar_url.indexOf("http"), avatar_url.length);
            }
            if (user && user.api_token) {
                localStorage.setItem('currentUser', JSON.stringify(user));
            }
        });
    };
    AuthenticationService.prototype.logout = function () {
        localStorage.removeItem("currentUser");
    };
    AuthenticationService.prototype.checkLogin = function () {
        var currentUser = JSON.parse(localStorage.getItem('currentUser'));
        if (currentUser && currentUser.api_token) {
            return true;
        }
        else {
            return false;
        }
    };
    AuthenticationService.prototype.getUser = function () {
        var currentUser = JSON.parse(localStorage.getItem('currentUser'));
        if (currentUser && currentUser.api_token) {
            return currentUser;
        }
        else {
            return {};
        }
    };
    return AuthenticationService;
}());
AuthenticationService = __decorate([
    core_1.Injectable(),
    __metadata("design:paramtypes", [http_1.Http,
        common_service_1.CommonService])
], AuthenticationService);
exports.AuthenticationService = AuthenticationService;
//# sourceMappingURL=authentication.service.js.map