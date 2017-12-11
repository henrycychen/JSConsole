from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time

class ChromeConsoleLogging(object):

    def __init__(self, ):
        self.driver = None

    def setUp(self, ):
        desired = DesiredCapabilities.CHROME
        desired ['loggingPrefs'] = { 'browser':'ALL' }
        self.driver = webdriver.Chrome(desired_capabilities=desired)

    def analyzeLog(self, ):
        time.sleep(10)
        data = self.driver.get_log('browser')
        analytics_issues = 0
        json_issues = 0
        amp_tracking = 0
        for entry in data:
            print entry
            if str(entry).find("Analytics") >= 0:
                analytics_issues += 1
            if str(entry).find("JSON") >= 0:
                json_issues += 1
            if str(entry).find("AMP") >= 0:
                amp_tracking += 1
        if analytics_issues > 0:
            print "Possible Analytics issue"
        if json_issues > 0:
            print "Possible JSON issue"
        if amp_tracking == 0:
            print "Possible amp validator not working"

    def tearDown(self, ):
        self.driver.quit()

    def testMethod(self, x):
        self.setUp()
        self.driver.get(x)
        self.analyzeLog()
        self.tearDown()

ampPages = [
    "https://popsugar.dev4.onsugar.com/test/resources/amp/amp-slide.html",
    "https://popsugar.dev4.onsugar.com/food/Olive-Garden-Lasagna-Recipe-30741106/amp",
    "https://popsugar.dev4.onsugar.com/home/Pinterest-Perfect-House-Real-Life-43251872/amp",
    "https://popsugar.dev4.onsugar.com/Hair-Color-Trends-Spring-2017-43133201/amp",
    "https://popsugar.dev4.onsugar.com/Bone-Broth-Dogs-40872442/amp",
    "https://popsugar.dev4.onsugar.com/home/Best-Ikea-Kitchen-Products-42696278/amp",
    "https://popsugar.dev4.onsugar.com/entertainment/Milo-Ventimiglia-Talks-About-Us-Season-1-Finale-43261334/amp",
    "https://popsugar.dev4.onsugar.com/fitness/Gluten-Free-Chickpea-Cookie-Dough-Recipe-43219630/amp",
    "https://popsugar.dev4.onsugar.com/moms/Little-Boy-Autism-I-Am-New-Poem-40918118/amp",
    "https://popsugar.dev4.onsugar.com/beauty/Eva-Gutowski-Bullying-43237758/amp",
    "https://popsugar.dev4.onsugar.com/fitness/30-Minute-Zumba-Workout-43144255/amp",
    "https://popsugar.dev4.onsugar.com/entertainment/Emma-Watson-Talks-About-Harry-Potter-Cast-March-2017-43278785/amp",
    "https://popsugar.dev4.onsugar.com/fitness/Sweet-Potato-Tofu-Avocado-Breakfast-43269919/amp",
    "https://popsugar.dev4.onsugar.com/tech/Microsoft-Girls-STEM-Video-2017-43279050/amp",
    "https://popsugar.dev4.onsugar.com/celebrity/Chloe-Grace-Moretz-Brooklyn-Beckham-Back-Together-2017-43276244/amp",
    "https://popsugar.dev4.onsugar.com/food/Olive-Garden-Deep-Fried-Ravioli-Recipe-39772700/amp",
    "https://popsugar.dev4.onsugar.com/food/Gastro-Garage-Toasted-Doughnuts-43209870/amp",
    "https://popsugar.dev4.onsugar.com/beauty/One-Two-Cosmetics-Magnetic-Lashes-Review-43251418/amp",
    "https://popsugar.dev4.onsugar.com/fashion/Hailey-Baldwin-Green-Cutout-Swimsuit-August-2016-42211346/amp",
    "https://popsugar.dev4.onsugar.com/love/Bachelor-Fantasy-Suite-Secrets-43279076/amp",
    "https://popsugar.dev4.onsugar.com/love/Love-Sex-News-March-7-2017-43278461/amp",
    "https://popsugar.dev4.onsugar.com/home/photo-gallery/42357029/image/42357061/Texture-More-Merrier/amp",
    "https://popsugar.dev4.onsugar.com/home/photo-gallery/43012327/embed/43012338/When-Emmie-Perfected-Floral-Display/amp",
    "https://popsugar.dev4.onsugar.com/moms/Best-Bottles-Breastfed-Babies-16069693/amp",
    "https://popsugar.dev4.onsugar.com/smart-living/photo-gallery/43588487/video/43589238/Watch-ride-action/amp"
]
for x in range(len(ampPages)):
    print ampPages[x]
    logResult = ChromeConsoleLogging().testMethod(ampPages[x])
    print '\n'