# Explanation
1) Navigate to Home page.
2) View product "striped-cotton-sweater".
3) Navigate to Cart page.
4) Navigate to Checkout page
5) Navigate to Home page.
6) Navigate to Login page.
7) Navigate to Home page.

# Raw Logs
🐛 debug:
[GET] /
-> Middleware context - 0.187208 ms
-> Middleware detectCurrentCart - 17.438375 ms
-> Middleware auth - 0.003667 ms
-> Middleware meta - 17.22775 ms
-> Middleware bodyParser - 0.033916 ms
-> Middleware addCustomerToCart - 0.001542 ms
-> Middleware buildQuery - 45.095333 ms
-> Middleware graphql - 70.315834 ms
-> Middleware notification - 0.001167 ms
-> Middleware notFound - 0.001666 ms
-> Middleware response

🐛 debug:
[GET] /homepage.js

99% done plugins webpack-hot-middlewarewebpack built cart a2fb415c243abed08390 in 968ms
99% done plugins webpack-hot-middlewarewebpack built productView 149be3e9c1a9fae16228 in 1019ms
🐛 debug:
[GET] /striped-cotton-sweater
-> Middleware context - 0.191625 ms
-> Middleware detectCurrentCart - 1.083584 ms
-> Middleware auth - 0.006375 ms
-> Middleware index - 1.113917 ms
-> Middleware bodyParser - 0.068292 ms
-> Middleware addCustomerToCart - 0.012833 ms
-> Middleware buildQuery - 84.307208 ms
-> Middleware graphql - 61.417584 ms
-> Middleware notification - 0.002375 ms
-> Middleware notFound - 0.001875 ms
-> Middleware response

🐛 debug:
[GET] /productView.js

🐛 debug:
[GET] /cart
-> Middleware context - 0.140833 ms
-> Middleware detectCurrentCart - 1.171125 ms
-> Middleware auth - 0.003666 ms
-> Middleware index - 0.073625 ms
-> Middleware bodyParser - 0.050208 ms
-> Middleware addCustomerToCart - 0.005916 ms
-> Middleware buildQuery - 78.168334 ms
-> Middleware graphql - 63.244625 ms
-> Middleware notification - 0.001 ms
-> Middleware notFound - 0.001208 ms
-> Middleware response

🐛 debug:
[GET] /cart.js

99% done plugins webpack-hot-middlewarewebpack built checkout 643d41df58e97b989ee8 in 607ms
🐛 debug:
[GET] /checkout
-> Middleware context - 0.107167 ms
-> Middleware detectCurrentCart - 17.844083 ms
-> Middleware auth - 0.002458 ms
-> Middleware index - 14.375667 ms
-> Middleware bodyParser - 0.029958 ms
-> Middleware addCustomerToCart - 0.002125 ms
-> Middleware buildQuery - 67.177042 ms
-> Middleware graphql - 156.1865 ms
-> Middleware notification - 0.000875 ms
-> Middleware notFound - 0.000791 ms
-> Middleware response

🐛 debug:
[GET] /checkout.js

🐛 debug:
[GET] /checkout?ajax=true
-> Middleware context - 0.17225 ms
-> Middleware detectCurrentCart - 0.636 ms
-> Middleware auth - 0.003416 ms
-> Middleware index - 2.880666 ms
-> Middleware bodyParser - 0.076125 ms
-> Middleware addCustomerToCart - 0.007625 ms
-> Middleware buildQuery - 98.495583 ms
-> Middleware graphql - 111.384625 ms
-> Middleware notification - 0.001625 ms
-> Middleware notFound - 0.001083 ms
-> Middleware response

(node:66698) MaxListenersExceededWarning: Possible EventEmitter memory leak detected. 11 uncaughtException listeners added to [process]. Use emitter.setMaxListeners() to increase limit
🐛 debug:
[POST] /api/graphql
-> Middleware context - 0.102958 ms
-> Middleware getCurrentUser - 0.365125 ms
-> Middleware demoAccountBlocking - 0.029708 ms
-> Middleware getCurrentCustomer - 0.747583 ms
-> Middleware bodyParser - 5.898083 ms
-> Middleware auth - 0.028584 ms
-> Middleware payloadValidate - 0.02475 ms
-> Middleware escapeHtml - 0.101 ms
-> Middleware removeUser - 0.012708 ms
-> Middleware graphql

🐛 debug:
[GET] /api/paymentMethods
-> Middleware context - 0.055458 ms
-> Middleware getCurrentUser - 0.430458 ms
-> Middleware demoAccountBlocking - 0.00125 ms
-> Middleware getCurrentCustomer - 1.444 ms
-> Middleware auth - 0.001625 ms
-> Middleware payloadValidate - 0.001042 ms
-> Middleware escapeHtml - 0.0005 ms
-> Middleware registerCod - 0.021375 ms
-> Middleware registerPaypal - 0.043208 ms
-> Middleware registerStripe - 0.040584 ms
-> Middleware sendMethods

🐛 debug:
[GET] /checkout?ajax=true
-> Middleware context - 0.049083 ms
-> Middleware detectCurrentCart - 0.338042 ms
-> Middleware auth - 0.001542 ms
-> Middleware index - 1.768416 ms
-> Middleware bodyParser - 0.022792 ms
-> Middleware addCustomerToCart - 0.0025 ms
-> Middleware buildQuery - 68.769583 ms
-> Middleware graphql - 14.597375 ms
-> Middleware notification - 0.000792 ms
-> Middleware notFound - 0.000666 ms
-> Middleware response

🐛 debug:
[GET] /api/shippingMethods/c3f61bd4-b6fc-4657-8e31-fa9bf08a98c5?country=null&province=
-> Middleware context - 0.241375 ms
-> Middleware getCurrentUser - 2.030542 ms
-> Middleware demoAccountBlocking - 0.005917 ms
-> Middleware getCurrentCustomer - 1.963875 ms
-> Middleware auth - 0.0085 ms
-> Middleware payloadValidate - 0.0035 ms
-> Middleware escapeHtml - 0.0025 ms
-> Middleware sendMethods

🐛 debug:
[GET] /
-> Middleware context - 0.101166 ms
-> Middleware detectCurrentCart - 2.713 ms
-> Middleware auth - 0.004 ms
-> Middleware meta - 0.044333 ms
-> Middleware bodyParser - 0.069917 ms
-> Middleware addCustomerToCart - 0.004375 ms
-> Middleware buildQuery - 52.939875 ms
-> Middleware graphql - 22.495583 ms
-> Middleware notification - 0.000917 ms
-> Middleware notFound - 0.000791 ms
-> Middleware response

🐛 debug:
[GET] /homepage.js

99% done plugins webpack-hot-middlewarewebpack built login 2722a503b9cb7f5f51b2 in 691ms
🐛 debug:
[GET] /account/login
-> Middleware context - 0.072625 ms
-> Middleware detectCurrentCart - 18.061375 ms
-> Middleware auth - 0.002917 ms
-> Middleware index - 0.034583 ms
-> Middleware bodyParser - 0.035583 ms
-> Middleware addCustomerToCart - 0.002041 ms
-> Middleware buildQuery - 47.876666 ms
-> Middleware graphql - 15.2905 ms
-> Middleware notification - 0.000792 ms
-> Middleware notFound - 0.000542 ms
-> Middleware response

🐛 debug:
[GET] /login.js

🐛 debug:
[GET] /
-> Middleware context - 0.175375 ms
-> Middleware detectCurrentCart - 0.784583 ms
-> Middleware auth - 0.004834 ms
-> Middleware meta - 0.06875 ms
-> Middleware bodyParser - 0.052958 ms
-> Middleware addCustomerToCart - 0.004583 ms
-> Middleware buildQuery - 80.407542 ms
-> Middleware graphql - 11.252125 ms
-> Middleware notification - 0.001042 ms
-> Middleware notFound - 0.000917 ms
-> Middleware response

🐛 debug:
[GET] /homepage.js

