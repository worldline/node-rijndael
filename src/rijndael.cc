#include <node.h>
#include <nan.h>
#include <v8.h>
#include <node_buffer.h>

// dependency
#include <string.h>
#include <stdlib.h>
#include <mcrypt.h>

using namespace v8;
using namespace node;

/* compatibilty for centos6 */
__asm__(".symver memcpy,memcpy@GLIBC_2.2.5");
NAN_METHOD(Rijndael) {
  Nan::HandleScope scope;

  MCRYPT rijndael_module;

  int err = 0;
  char* error_message;
  int data_size;
  void* data;
  char* text;
  char* key;
  char* iv = NULL;

  int text_len;
  int key_len;
  bool encrypt;
  char* mode;

  if (info.Length() < 1 || !Buffer::HasInstance(info[0])) {
    err = 1; error_message = (char*) "data must be a buffer";
  } else if (info.Length() < 2 || !Buffer::HasInstance(info[1])) {
    err = 1; error_message = (char*) "key must be a buffer";
  } else if (info.Length() < 3 || !info[2]->IsBoolean()) {
    err = 1; error_message = (char*) "encryption must be a boolean";
  } else if (info.Length() < 4) {
    err = 1; error_message = (char*) "block mode must be a string";
  } else if (info.Length() < 5) {
    err = 1; error_message = (char*) "iv must be a buffer or null";
  }

  if (err == 1) {
    Nan::ThrowTypeError(error_message);
    return;
  }

  if (Buffer::HasInstance(info[4])) {
    iv = Buffer::Data(info[4]);
  }

  String::Utf8Value modeStr(info[3]->ToString());

  text = Buffer::Data(info[0]);
  key = Buffer::Data(info[1]);
  encrypt = info[2]->BooleanValue();
  mode = *modeStr;

  text_len = Buffer::Length(info[0]);
  key_len = Buffer::Length(info[1]);

  if (key_len != 16 && key_len != 24 && key_len != 32) {
    Nan::ThrowError("key length does not match algorithm parameters");
    return;
  }

  rijndael_module = mcrypt_module_open((char*) "rijndael-256", NULL, mode, NULL);
  if (rijndael_module == MCRYPT_FAILED) {
    Nan::ThrowError("rijndael mcrypt module failed to load");
    return;
  }

  err = mcrypt_generic_init(rijndael_module, (void*) key, key_len, iv);
  if (err < 0) {
    mcrypt_module_close(rijndael_module);
    Nan::ThrowError(mcrypt_strerror(err));
    return;
  }

  data_size = (((text_len - 1) / 32) + 1) * 32;
  data = malloc(data_size);
  memset(data, 0, data_size);
  memcpy(data, text, text_len);

  if (encrypt)
    err = mcrypt_generic(rijndael_module, data, data_size);
  else
    err = mdecrypt_generic(rijndael_module, data, data_size);

  if (err < 0) {
    mcrypt_module_close(rijndael_module);
    free(data);
    Nan::ThrowError(mcrypt_strerror(err));
    return;
  }
  
  mcrypt_generic_deinit(rijndael_module);

  Local<Object> buffer = Nan::NewBuffer((char*) data, data_size).ToLocalChecked();
  mcrypt_module_close(rijndael_module);
  free(data);
  info.GetReturnValue().Set(buffer);
}

void init(Handle<Object> exports) {
  Nan::HandleScope scope;
  exports->Set(Nan::New<String>("rijndael").ToLocalChecked(),
    Nan::New<FunctionTemplate>(Rijndael)->GetFunction());
}

NODE_MODULE(rijndael, init)
