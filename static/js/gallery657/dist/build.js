/******/ (function(modules) { // webpackBootstrap
/******/ 	// The module cache
/******/ 	var installedModules = {};
/******/
/******/ 	// The require function
/******/ 	function __webpack_require__(moduleId) {
/******/
/******/ 		// Check if module is in cache
/******/ 		if(installedModules[moduleId]) {
/******/ 			return installedModules[moduleId].exports;
/******/ 		}
/******/ 		// Create a new module (and put it into the cache)
/******/ 		var module = installedModules[moduleId] = {
/******/ 			i: moduleId,
/******/ 			l: false,
/******/ 			exports: {}
/******/ 		};
/******/
/******/ 		// Execute the module function
/******/ 		modules[moduleId].call(module.exports, module, module.exports, __webpack_require__);
/******/
/******/ 		// Flag the module as loaded
/******/ 		module.l = true;
/******/
/******/ 		// Return the exports of the module
/******/ 		return module.exports;
/******/ 	}
/******/
/******/
/******/ 	// expose the modules object (__webpack_modules__)
/******/ 	__webpack_require__.m = modules;
/******/
/******/ 	// expose the module cache
/******/ 	__webpack_require__.c = installedModules;
/******/
/******/ 	// identity function for calling harmony imports with the correct context
/******/ 	__webpack_require__.i = function(value) { return value; };
/******/
/******/ 	// define getter function for harmony exports
/******/ 	__webpack_require__.d = function(exports, name, getter) {
/******/ 		if(!__webpack_require__.o(exports, name)) {
/******/ 			Object.defineProperty(exports, name, {
/******/ 				configurable: false,
/******/ 				enumerable: true,
/******/ 				get: getter
/******/ 			});
/******/ 		}
/******/ 	};
/******/
/******/ 	// getDefaultExport function for compatibility with non-harmony modules
/******/ 	__webpack_require__.n = function(module) {
/******/ 		var getter = module && module.__esModule ?
/******/ 			function getDefault() { return module['default']; } :
/******/ 			function getModuleExports() { return module; };
/******/ 		__webpack_require__.d(getter, 'a', getter);
/******/ 		return getter;
/******/ 	};
/******/
/******/ 	// Object.prototype.hasOwnProperty.call
/******/ 	__webpack_require__.o = function(object, property) { return Object.prototype.hasOwnProperty.call(object, property); };
/******/
/******/ 	// __webpack_public_path__
/******/ 	__webpack_require__.p = "/dist/";
/******/
/******/ 	// Load entry module and return exports
/******/ 	return __webpack_require__(__webpack_require__.s = 4);
/******/ })
/************************************************************************/
/******/ ([
/* 0 */
/***/ (function(module, exports) {

// this module is a runtime utility for cleaner component module output and will
// be included in the final webpack user bundle

module.exports = function normalizeComponent (
  rawScriptExports,
  compiledTemplate,
  scopeId,
  cssModules
) {
  var esModule
  var scriptExports = rawScriptExports = rawScriptExports || {}

  // ES6 modules interop
  var type = typeof rawScriptExports.default
  if (type === 'object' || type === 'function') {
    esModule = rawScriptExports
    scriptExports = rawScriptExports.default
  }

  // Vue.extend constructor export interop
  var options = typeof scriptExports === 'function'
    ? scriptExports.options
    : scriptExports

  // render functions
  if (compiledTemplate) {
    options.render = compiledTemplate.render
    options.staticRenderFns = compiledTemplate.staticRenderFns
  }

  // scopedId
  if (scopeId) {
    options._scopeId = scopeId
  }

  // inject cssModules
  if (cssModules) {
    var computed = Object.create(options.computed || null)
    Object.keys(cssModules).forEach(function (key) {
      var module = cssModules[key]
      computed[key] = function () { return module }
    })
    options.computed = computed
  }

  return {
    esModule: esModule,
    exports: scriptExports,
    options: options
  }
}


/***/ }),
/* 1 */
/***/ (function(module, exports, __webpack_require__) {

var Component = __webpack_require__(0)(
  /* script */
  __webpack_require__(3),
  /* template */
  null,
  /* scopeId */
  null,
  /* cssModules */
  null
)

module.exports = Component.exports


/***/ }),
/* 2 */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
Object.defineProperty(__webpack_exports__, "__esModule", { value: true });
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//


/* harmony default export */ __webpack_exports__["default"] = ({
  name: 'art',
  data() {
    return {
      prev: null,
      art: null,
      next: null
    };
  },
  created() {
    this.fetchData();
  },
  watch: {
    '$route': 'fetchData'
  },
  methods: {
    fetchData() {
      this.art = null;
      var image_id = 1;
      if (this.$route.params.id) {
        image_id = this.$route.params.id;
      }
      this.$http.get('/gallery/api/mediafiles/').then(response => {
        var count = response.body.count;
        this.art = response.body.results[image_id - 1];
        if (this.art.pk > 1) {
          this.prev = this.art.pk - 1;
        } else {
          this.prev = false;
        }
        if (this.art.pk < count) {
          this.next = this.art.pk + 1;
        } else {
          this.next = false;
        }
      }, response => {
        console.log('error');
      });
    }
  }
});

/***/ }),
/* 3 */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
Object.defineProperty(__webpack_exports__, "__esModule", { value: true });
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0__Art_vue__ = __webpack_require__(5);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0__Art_vue___default = __webpack_require__.n(__WEBPACK_IMPORTED_MODULE_0__Art_vue__);
//



/* harmony default export */ __webpack_exports__["default"] = ({
  routes: [{ path: '/', component: __WEBPACK_IMPORTED_MODULE_0__Art_vue___default.a }, { path: '/:id', name: 'art_id', component: __WEBPACK_IMPORTED_MODULE_0__Art_vue___default.a }]
});

/***/ }),
/* 4 */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
Object.defineProperty(__webpack_exports__, "__esModule", { value: true });
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0__components_Router_vue__ = __webpack_require__(1);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0__components_Router_vue___default = __webpack_require__.n(__WEBPACK_IMPORTED_MODULE_0__components_Router_vue__);



const router = new VueRouter({
    //mode: 'history',
    base: '/gallery',
    routes: __WEBPACK_IMPORTED_MODULE_0__components_Router_vue__["routes"]
});

new Vue({
    el: '#gallery',
    router
});

/***/ }),
/* 5 */
/***/ (function(module, exports, __webpack_require__) {

var Component = __webpack_require__(0)(
  /* script */
  __webpack_require__(2),
  /* template */
  __webpack_require__(6),
  /* scopeId */
  null,
  /* cssModules */
  null
)

module.exports = Component.exports


/***/ }),
/* 6 */
/***/ (function(module, exports) {

module.exports={render:function (){var _vm=this;var _h=_vm.$createElement;var _c=_vm._self._c||_h;
  return _c('div', [_c('h3', [_vm._v(_vm._s(_vm.art.title))]), _vm._v(" "), _c('table', {
    staticStyle: {
      "width": "100%"
    }
  }, [_c('tr', [_c('td', {
    staticClass: "edge"
  }, [(_vm.prev) ? _c('router-link', {
    attrs: {
      "to": {
        name: 'art_id',
        params: {
          id: _vm.prev
        }
      }
    }
  }, [_c('span', [_vm._v("<")])]) : _c('span', {
    staticClass: "toinfinity"
  }, [_vm._v("<")])], 1), _vm._v(" "), _c('td', [(_vm.art) ? _c('img', {
    attrs: {
      "src": _vm.art.media_file,
      "alt": _vm.art.title
    }
  }) : _vm._e()]), _vm._v(" "), _c('td', {
    staticClass: "edge"
  }, [(_vm.next) ? _c('router-link', {
    attrs: {
      "to": {
        name: 'art_id',
        params: {
          id: _vm.next
        }
      }
    }
  }, [_c('span', [_vm._v(">")])]) : _c('span', {
    staticClass: "toinfinity"
  }, [_vm._v(">")])], 1)])])])
},staticRenderFns: []}

/***/ })
/******/ ]);
//# sourceMappingURL=build.js.map