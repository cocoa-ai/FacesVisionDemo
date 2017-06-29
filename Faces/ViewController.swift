import VisionLab

final class ViewController: ImageClassificationController<ClassificationService> {
  override func viewDidLoad() {
    super.viewDidLoad()
    classificationService.delegate = self
  }
}

// MARK: - ClassificationServiceDelegate

extension ViewController: ClassificationServiceDelegate {
  func classificationService(_ service: ClassificationService, didDetectGender gender: String) {
    append(to: mainView.label, title: "Gender", text: gender)
  }

  func classificationService(_ service: ClassificationService, didDetectAge age: String) {
    append(to: mainView.label, title: "Age", text: age)
  }

  func classificationService(_ service: ClassificationService, didDetectEmotion emotion: String) {
    append(to: mainView.label, title: "Emotions", text: emotion)
  }

  /// Set results of the classification request
  func append(to label: UILabel, title: String, text: String) {
    DispatchQueue.main.async { [weak label] in
      let attributedText = label?.attributedText ?? NSAttributedString(string: "")
      let string = NSMutableAttributedString(attributedString: attributedText)
      string.append(.init(string: "\(title): ", attributes: [.font: UIFont.boldSystemFont(ofSize: 18)]))
      string.append(.init(string: text, attributes: [.font: UIFont.systemFont(ofSize: 18)]))
      string.append(.init(string: "\n\n"))

      label?.attributedText = string
    }
  }
}
