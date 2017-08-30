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
var home_service_1 = require("../services/home.service");
var register_service_1 = require("../services/register.service");
var ng2_toastr_1 = require("ng2-toastr/ng2-toastr");
var alert_service_1 = require("../services/alert.service");
var router_1 = require("@angular/router");
var BusinessComponent = (function () {
    function BusinessComponent(_homeservice, registerService, vRef, toast, alert, _router) {
        this._homeservice = _homeservice;
        this.registerService = registerService;
        this.vRef = vRef;
        this.toast = toast;
        this.alert = alert;
        this._router = _router;
        this.countries = [
            { code: "BH", value: "Bahrain" },
            { code: "EG", value: "Egypt" },
            { code: "KW", value: "Kuwait" },
            { code: "LB", value: "Lebanon" },
            { code: "OM", value: "Oman" },
            { code: "QA", value: "Qatar" },
            { code: "SA", value: "Saudi Arabia" },
            { code: "AE", value: "United Arab Emirates" }
        ];
        this.validate_password = true;
        this.meesage_password = 'here';
        this.toast.setRootViewContainerRef(vRef);
    }
    BusinessComponent.prototype.ngOnInit = function () {
        var _this = this;
        this._homeservice.BCategories().subscribe(function (data) {
            _this.bcategories = data;
        });
    };
    BusinessComponent.prototype.changeCountry = function (country) {
        var _this = this;
        this._homeservice.getCities(country).subscribe(function (data) {
            _this.cities = data;
        });
    };
    BusinessComponent.prototype.registerForm = function (f) {
        var _this = this;
        var self = this;
        this.registerService.registerBusiness(f).subscribe(function (data) {
            _this.alert.success("Register Business success.", true);
            _this._router.navigate(['login']);
        }, function (error) {
            var errors = error.json();
            var error_msg = '';
            for (var err in errors) {
                for (var i = 0; i < errors[err].length; i++) {
                    if (error_msg == '') {
                        error_msg = errors[err][i];
                    }
                    else {
                        error_msg += "</br>" + errors[err][i];
                    }
                }
            }
            self.toast.error(error_msg, "Error", { enableHTML: true });
        });
    };
    BusinessComponent.prototype.changepassword = function (f, password) {
        this.validate_password = true;
        this.meesage_password = '';
        if (f.username == password) {
            this.validate_password = false;
            this.meesage_password = 'Password must be different from Username! Try again.';
            return;
        }
        if (password.length < 8) {
            this.validate_password = false;
            this.meesage_password = '';
            return;
        }
        var re = /[0-9]/;
        if (!re.test(password)) {
            this.validate_password = false;
            this.meesage_password = 'Password must contain at least one number (0-9)!';
            return;
        }
        re = /[a-z]/;
        if (!re.test(password)) {
            this.validate_password = false;
            this.meesage_password = 'Password must contain at least one lowercase letter (a-z)!';
            return;
        }
        re = /[A-Z]/;
        if (!re.test(password)) {
            this.validate_password = false;
            this.meesage_password = 'Password must contain at least one uppercase letter (A-Z)!';
            return;
        }
    };
    return BusinessComponent;
}());
BusinessComponent = __decorate([
    core_1.Component({
        selector: "business-component",
        templateUrl: "business.component.html",
        styleUrls: ['../login/login.component.css'],
        providers: [home_service_1.HomeService, register_service_1.RegisterService]
    }),
    __metadata("design:paramtypes", [home_service_1.HomeService,
        register_service_1.RegisterService,
        core_1.ViewContainerRef,
        ng2_toastr_1.ToastsManager,
        alert_service_1.AlertService,
        router_1.Router])
], BusinessComponent);
exports.BusinessComponent = BusinessComponent;
//# sourceMappingURL=business.component.js.map