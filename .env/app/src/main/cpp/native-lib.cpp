#include <jni.h>

extern "C"
JNIEXPORT jstring JNICALL
Java_com_js_brazil_MainActivity_stringFromJNI(JNIEnv *env, jobject /* this */) {
    return env->NewStringUTF("PixelArt Studio");
}