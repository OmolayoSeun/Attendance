class Reader:

    @staticmethod
    def getFingerPrint(warmStart):
        # Boilerplate stuff to start the module
        # time.sleep(3)
        import jpype.imports

        # Launch the JVM
        if not warmStart:
            jpype.startJVM(classpath=['FReader.jar'])

        # import the Java modules
        from com.OmolayoSeun import Action
        from com.OmolayoSeun import SampleApp

        DPSdk = SampleApp()

        FPInfo = DPSdk.call(Action.REGISTER_USER)

        print(FPInfo)

        return FPInfo
    @staticmethod
    def verifyFingerPrint(fingerPrint):
        import jpype.imports

        # Launch the JVM
        jpype.startJVM(classpath=['FReader.jar'])

        # import the Java modules
        from com.OmolayoSeun import Action
        from com.OmolayoSeun import SampleApp

        DPSdk = SampleApp()

        byte_arr = bytearray(fingerPrint)

        FPInfo = DPSdk.call(Action.VERIFY_USER, byte_arr)

        print(FPInfo)


