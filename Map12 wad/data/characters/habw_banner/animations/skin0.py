#PROP_text
type: string = "PROP"
version: u32 = 3
linked: list[string] = {}
entries: map[hash,embed] = {
    "Characters/HABW_banner/Animations/Skin0" = animationGraphData {
        mCascadeBlendValue: f32 = 0
        mClipDataMap: map[hash,pointer] = {
            0x8d3a9de7 = SelectorClipData {
                mSelectorPairDataList: list[embed] = {
                    SelectorPairData {
                        mClipName: hash = "Runup1"
                        mProbability: f32 = 0.300000012
                    }
                    SelectorPairData {
                        mClipName: hash = "Runup2"
                        mProbability: f32 = 0.300000012
                    }
                    SelectorPairData {
                        mClipName: hash = "Runup3"
                        mProbability: f32 = 0.400000006
                    }
                }
                mFlags: u32 = 8
            }
            "Runup1" = AtomicClipData {
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/HABW_banner/Skins/Base/Animations/HABW_banner_runup1.anm"
                }
                mTrackDataName: hash = "Default"
                mFlags: u32 = 12
            }
            "Runup2" = AtomicClipData {
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/HABW_banner/Skins/Base/Animations/HABW_Banner_runup2.anm"
                }
                mTrackDataName: hash = "Default"
                mFlags: u32 = 12
            }
            0xb445ed49 = AtomicClipData {
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/HABW_banner/Skins/Base/Animations/HABW_banner_Idle1.anm"
                }
                mTrackDataName: hash = "Default"
                mFlags: u32 = 6
            }
            "Idle1" = SequencerClipData {
                mClipNameList: list[hash] = {
                    0x8d3a9de7
                    0xb445ed49
                }
            }
            "Runup3" = AtomicClipData {
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/HABW_banner/Skins/Base/Animations/HABW_banner_Idle1.anm"
                }
                mTrackDataName: hash = "Default"
            }
        }
        mTrackDataMap: map[hash,embed] = {
            "Default" = TrackData {}
        }
    }
}
