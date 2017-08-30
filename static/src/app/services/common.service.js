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
var CommonService = (function () {
    function CommonService(router) {
        this.router = router;
    }
    CommonService.prototype.getUrl = function () {
        return this.router.url;
    };
    CommonService.prototype.jwt = function () {
        var currentUser = JSON.parse(localStorage.getItem('currentUser'));
        if (currentUser && currentUser.api_token) {
            var headers = new http_1.Headers({ 'Authorization': 'Token ' + currentUser.api_token });
            return new http_1.RequestOptions({ headers: headers });
        }
    };
    CommonService.prototype.jwt_social = function (token) {
        if (token) {
            var headers = new http_1.Headers({ 'Authorization': 'Token ' + token });
            return new http_1.RequestOptions({ headers: headers });
        }
    };
    return CommonService;
}());
CommonService = __decorate([
    core_1.Injectable(),
    __metadata("design:paramtypes", [router_1.Router])
], CommonService);
exports.CommonService = CommonService;
//# sourceMappingURL=common.service.js.map