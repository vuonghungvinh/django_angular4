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
var authentication_service_1 = require("../services/authentication.service");
var ng2_toastr_1 = require("ng2-toastr/ng2-toastr");
var ngx_facebook_1 = require("ngx-facebook");
var LoginComponent = (function () {
    function LoginComponent(route, router, authenticate, alertService, toast, vRef, fb) {
        this.route = route;
        this.router = router;
        this.authenticate = authenticate;
        this.alertService = alertService;
        this.toast = toast;
        this.vRef = vRef;
        this.fb = fb;
        this.validate_password = true;
        this.meesage_password = '';
        this.toast.setRootViewContainerRef(vRef);
    }
    LoginComponent.prototype.ngAfterViewInit = function () {
        var that = this;
        setTimeout(function () {
            gapi.load('auth2', function () {
                that.auth2 = gapi.auth2.init({
                    client_id: '989166669078-3jetaeidl05o31hutbkalrvislqqt5ee.apps.googleusercontent.com',
                    cookiepolicy: 'single_host_origin',
                    scope: 'profile email'
                });
                that.attachSignin(document.getElementById('googleBtn'));
            });
            var initParams = {
                appId: '129381297646323',
                xfbml: true,
                version: 'v2.9'
            };
            that.fb.init(initParams);
        }, 1500);
    };
    LoginComponent.prototype.attachSignin = function (element) {
        var that = this;
        this.auth2.attachClickHandler(element, {}, function (googleUser) {
            // let profile = googleUser.getBasicProfile();
            // console.log('access_token || ' + googleUser.getAuthResponse().access_token);
            // console.log('Token || ' + googleUser.getAuthResponse().id_token);
            // console.log('ID: ' + profile.getId());
            // console.log('Name: ' + profile.getName());
            // console.log('Image URL: ' + profile.getImageUrl());
            // console.log('Email: ' + profile.getEmail());
            //YOUR CODE HERE
            that.authenticate.loginWithGoogle(googleUser.getAuthResponse().access_token).subscribe(function (data) {
                that.authenticate.loginWithSocial(data.key, 'google').subscribe(function (data) {
                    that.alertService.success("Login success.", true);
                    that.router.navigate([that.returnUrl]);
                }, function (errors) {
                    that.toast.error("Can not login with google. PLease try again!");
                });
            }, function (errors) {
                // console.log(errors);
                that.toast.error("Can not login with google. PLease try again!");
            });
        }, function (error) {
            // alert(JSON.stringify(error, undefined, 2));
        });
    };
    LoginComponent.prototype.loginTwitter = function () {
        window.location.href = 'accounts/twitter/login/';
    };
    LoginComponent.prototype.loginFB = function () {
        var _this = this;
        this.fb.login().then(function (response) {
            _this.authenticate.loginWithFacebook(response.authResponse.accessToken).subscribe(function (data) {
                _this.authenticate.loginWithSocial(data.key, 'facebook').subscribe(function (data) {
                    _this.alertService.success("Login success.", true);
                    _this.router.navigate([_this.returnUrl]);
                }, function (errors) {
                    console.error(errors);
                    _this.toast.error("Can not login with facebook. PLease try again!");
                });
            }, function (errors) {
                console.error(errors);
                _this.toast.error("Can not login with facebook. PLease try again!");
            });
        })
            .catch(function (error) {
            console.error(error);
            _this.toast.error("Can not login with facebook. PLease try again!");
        });
    };
    LoginComponent.prototype.ngOnInit = function () {
        this.authenticate.logout();
        this.returnUrl = this.route.snapshot.queryParams['returnUrl'] || '/';
    };
    LoginComponent.prototype.login = function (value) {
        var _this = this;
        this.authenticate.login(value).subscribe(function (data) {
            _this.alertService.success("Login success.", true);
            _this.router.navigate([_this.returnUrl]);
        }, function (error) {
            _this.toast.error("Username or password incorrect!", "Login fail!");
        });
    };
    LoginComponent.prototype.changepassword = function (f, password) {
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
    return LoginComponent;
}());
LoginComponent = __decorate([
    core_1.Component({
        selector: "login-component",
        templateUrl: "login.component.html",
        styleUrls: ['login.component.css'],
    }),
    __metadata("design:paramtypes", [router_1.ActivatedRoute,
        router_1.Router,
        authentication_service_1.AuthenticationService,
        alert_service_1.AlertService,
        ng2_toastr_1.ToastsManager,
        core_1.ViewContainerRef,
        ngx_facebook_1.FacebookService])
], LoginComponent);
exports.LoginComponent = LoginComponent;
//# sourceMappingURL=login.component.js.map