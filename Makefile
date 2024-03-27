build:
	python3 ./platforms/js/build_js.py build_wasm --build_wasm --emscripten_dir ${HOME}/repos/emsdk/upstream/emscripten && \
	cp build_wasm/bin/opencv.js ${DEV_APTUS_CORRECTOR}/static/js/opencv-custom-build.js && \
	sed -i 's/cv\./window\.cv\./g' ${DEV_APTUS_CORRECTOR}/static/js/opencv-custom-build.js && \
	sed -i 's/var wasmMemory/wasmMemory/g' ${DEV_APTUS_CORRECTOR}/static/js/opencv-custom-build.js && \
	sed -i 's/wasmMemory/window.wasmMemory/g' ${DEV_APTUS_CORRECTOR}/static/js/opencv-custom-build.js && \
	ls -lh ${DEV_APTUS_CORRECTOR}/static/js/
