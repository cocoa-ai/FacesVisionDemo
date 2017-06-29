import UIKit

@UIApplicationMain
final class AppDelegate: UIResponder, UIApplicationDelegate {
  var window: UIWindow?
  private lazy var controller: UIViewController = ViewController()

  func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplicationLaunchOptionsKey: Any]?) -> Bool {
    window = UIWindow()
    window?.rootViewController = controller
    window?.makeKeyAndVisible()

    return true
  }
}
