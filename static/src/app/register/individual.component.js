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
var register_service_1 = require("../services/register.service");
var ng2_toastr_1 = require("ng2-toastr/ng2-toastr");
var alert_service_1 = require("../services/alert.service");
var router_1 = require("@angular/router");
var IndividualComponent = (function () {
    function IndividualComponent(registerService, toastr, vRef, alert, _router) {
        this.registerService = registerService;
        this.toastr = toastr;
        this.vRef = vRef;
        this.alert = alert;
        this._router = _router;
        this.validate_password = true;
        this.meesage_password = 'here';
        this.toastr.setRootViewContainerRef(vRef);
    }
    IndividualComponent.prototype.registerForm = function (f) {
        var _this = this;
        var self = this;
        this.registerService.registerIndividual(f).subscribe(function (data) {
            _this.alert.success("Register Individual success.", true);
            _this._router.navigate(['login']);
        }, function (error) {
            var errors = error.json();
            var error_msg = '';
            if (errors.email) {
                for (var i = 0; i < errors.email.length; i++) {
                    if (error_msg == '') {
                        error_msg = errors.email[i];
                    }
                    else {
                        error_msg += "</br>" + errors.email[i];
                    }
                }
            }
            if (errors.username) {
                for (var i = 0; i < errors.username.length; i++) {
                    if (error_msg == '') {
                        error_msg = errors.username[i];
                    }
                    else {
                        error_msg += "</br>" + errors.username[i];
                    }
                }
            }
            if (errors.password) {
                for (var i = 0; i < errors.password.length; i++) {
                    if (error_msg == '') {
                        error_msg = errors.password[i];
                    }
                    else {
                        error_msg += "</br>" + errors.password[i];
                    }
                }
            }
            self.toastr.error(error_msg, "Error", { enableHTML: true });
        });
    };
    IndividualComponent.prototype.changepassword = function (f, password) {
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
    return IndividualComponent;
}());
IndividualComponent = __decorate([
    core_1.Component({
        selector: "individual-component",
        templateUrl: "individual.component.html",
        styleUrls: ['../login/login.component.css'],
        providers: [register_service_1.RegisterService]
    }),
    __metadata("design:paramtypes", [register_service_1.RegisterService,
        ng2_toastr_1.ToastsManager,
        core_1.ViewContainerRef,
        alert_service_1.AlertService,
        router_1.Router])
], IndividualComponent);
exports.IndividualComponent = IndividualComponent;
//# sourceMappingURL=individual.component.js.map