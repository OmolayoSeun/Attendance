from resources.Variables import Variables as v

# Clear the widgets of the frame content
def clear_content():
    try:
        v.holdFrameReference.destroy()
    except Exception as e:
        print("Null View error\n", e)
    pass
