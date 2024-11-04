export PATH="/opt/homebrew/opt/opencv@3/bin:$PATH"
export PATH="$PATH:$HOME/bin"

# >>> conda initialize >>>
# !! Contents within this block are managed by 'conda init' !!
__conda_setup="$('/Users/angelacassanelli/miniforge3/bin/conda' 'shell.zsh' 'hook' 2> /dev/null)"
if [ $? -eq 0 ]; then
    eval "$__conda_setup"
else
    if [ -f "/Users/angelacassanelli/miniforge3/etc/profile.d/conda.sh" ]; then
        . "/Users/angelacassanelli/miniforge3/etc/profile.d/conda.sh"
    else
        export PATH="/Users/angelacassanelli/miniforge3/bin:$PATH"
    fi
fi
unset __conda_setup
# <<< conda initialize <<<

export ANDROID_HOME="/Users/angelacassanelli/Android/Sdk"
export ANDROID_NDK_HOME="/Users/angelacassanelli/Android/Sdk/ndk-bundle/android-ndk-r18b"

export PATH="/opt/homebrew/opt/opencv@3/bin:$PATH"
export LDFLAGS="-L/opt/homebrew/opt/opencv@3/lib"
export CPPFLAGS="-I/opt/homebrew/opt/opencv@3/include"
export PKG_CONFIG_PATH="/opt/homebrew/opt/opencv@3/lib/pkgconfig"
export PATH="/opt/homebrew/opt/opencv@3/bin:$PATH"
export PATH="/opt/homebrew/opt/opencv@3/bin:$PATH"

export JAVA_HOME="/usr/libexec/java_home -v 17.0"

export PYTHONPATH="$PYTHONPATH:/Users/angelacassanelli/Documents/poliba/Kotlin2SwiftTranspiler/generated"

