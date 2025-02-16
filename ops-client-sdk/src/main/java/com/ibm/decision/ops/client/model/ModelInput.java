/*
 * Copyright 2020 IBM
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 * <p>
 * http://www.apache.org/licenses/LICENSE-2.0
 * <p>
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.IBM Confidential
 */

package com.ibm.decision.ops.client.model;

import com.google.gson.TypeAdapter;
import com.google.gson.annotations.JsonAdapter;
import com.google.gson.stream.JsonReader;
import com.google.gson.stream.JsonWriter;

import java.io.IOException;

/**
 * Supported model input formats.
 */
@JsonAdapter(ModelInput.Adapter.class)
public enum ModelInput {

  AUTO("auto"),

  DATAFRAME("DataFrame"),

  NDARRAY("ndarray"),

  DMATRIX("DMatrix"),

  LIST("list");

  private final String value;

  ModelInput(String value) {
    this.value = value;
  }

  public String getValue() {
    return value;
  }

  @Override
  public String toString() {
    return String.valueOf(value);
  }

  public static ModelInput fromValue(String value) {
    for (ModelInput b : ModelInput.values()) {
      if (b.value.equals(value)) {
        return b;
      }
    }
    throw new IllegalArgumentException("Unexpected value '" + value + "'");
  }

  public static class Adapter extends TypeAdapter<ModelInput> {
    @Override
    public void write(final JsonWriter jsonWriter, final ModelInput enumeration) throws IOException {
      jsonWriter.value(enumeration.getValue());
    }

    @Override
    public ModelInput read(final JsonReader jsonReader) throws IOException {
      String value = jsonReader.nextString();
      return ModelInput.fromValue(value);
    }
  }
}
