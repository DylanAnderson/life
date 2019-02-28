CXX := clang++
CXXFLAGS := -Wall -g -std=c++17 -pedantic
LDFLAGS :=
BUILD := ./build
OBJ_DIR := $(BUILD)/objects
APP_DIR := $(BUILD)/apps
TARGET := life
INCLUDE := -Iinclude/

SOURCES := $(wildcard src/*.cpp)
OBJECTS := $(SOURCES:src/%.cpp=$(OBJ_DIR)/%.o)

all: build $(APP_DIR)/$(TARGET)

$(OBJ_DIR)/%.o: src/%.cpp
	$(CXX) $(CXXFLAGS) $(INCLUDE) -o $@ -c $<

$(APP_DIR)/$(TARGET): $(OBJECTS)
	$(CXX) $(CXXFLAGS) $(INCLUDE) $(LDFLAGS) -o $(APP_DIR)/$(TARGET) $(OBJECTS)

.PHONY: all build clean debug release

build:
	$(info SOURCES: $(SOURCES))
	$(info OBJECTS: $(OBJECTS))
	@mkdir -p $(APP_DIR)
	@mkdir -p $(OBJ_DIR)

debug: CXXFlags += -DDEBUG -g
debug: all

release: CXXFLAGS += -O2
relase: all

clean:
	@rm -rvf $(BUILD)
