from resources.Variables import Variables as v
class Reader:

    # Gets the fingerprint by called the jar sdk program for interfacing the fingerprint
    @staticmethod
    def getFingerPrint():
        # Boilerplate stuff to start the module
        # time.sleep(3)
        import jpype.imports

        # Launch the JVM
        if not v.initialiseJVM:
            jpype.startJVM(classpath=['FReader.jar'])
            v.initialiseJVM = True

        # import the Java modules
        from com.OmolayoSeun import Action
        from com.OmolayoSeun import SampleApp

        DPSdk = SampleApp()

        FPInfo = DPSdk.call(Action.REGISTER_USER)

        print(FPInfo)

        return FPInfo

    # This function checks the fingerprint if it matches
    @staticmethod
    def verifyFingerPrint(fingerPrints):
        import jpype.imports

        if not v.initialiseJVM:
            jpype.startJVM(classpath=['FReader.jar'])
            v.initialiseJVM = True
        # Launch the JVM

        # import the Java modules
        from com.OmolayoSeun import Action
        from com.OmolayoSeun import SampleApp

        DPSdk = SampleApp()

        FIndex = DPSdk.call(Action.VERIFY_USER, fingerPrints)

        # print("The index value is ",FIndex)
        return FIndex

# Error code ERR100 no fingerprint scanner
# Error code ERR200 failed operation
# Error code ERR300 no matching fingerprint
# Error code ERR400
#
#
