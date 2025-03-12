#PROP_text
type: string = "PROP"
version: u32 = 3
linked: list[string] = {
    "DATA/Characters/HA_AP_Viking/Animations/Skin0.bin"
    "DATA/Characters/HA_AP_Viking/HA_AP_Viking.bin"
}
entries: map[hash,embed] = {
    "Characters/HA_AP_Viking/Skins/Skin0" = SkinCharacterDataProperties {
        championSkinName: string = "HA_AP_Viking"
        skinAnimationProperties: embed = skinAnimationProperties {
            animationGraphData: link = "Characters/HA_AP_Viking/Animations/Skin0"
        }
        skinMeshProperties: embed = SkinMeshDataProperties {
            skeleton: string = "ASSETS/Characters/HA_AP_Viking/Skins/Base/HA_AP_Viking.skl"
            simpleSkin: string = "ASSETS/Characters/HA_AP_Viking/Skins/Base/HA_AP_Viking.skn"
            texture: string = "ASSETS/Characters/HA_AP_Viking/Skins/Base/HA_AP_Viking.tex"
            skinScale: f32 = 1.35000002
            selfIllumination: f32 = 1
            castShadows: bool = false
            reflectionFresnelColor: rgba = { 0, 0, 0, 255 }
        }
        mContextualActionData: link = "Characters/HA_AP_Viking/CAC/HA_AP_Viking"
    }
    "Characters/HA_AP_Viking/CAC/HA_AP_Viking" = ContextualActionData {
        mCooldown: f32 = 1
        mSituations: map[hash,embed] = {
            "Purchase" = ContextualSituation {
                mRules: list[embed] = {
                    ContextualRule {
                        mRuleName: string = "Purchase"
                        mConditions: list[pointer] = {
                            ContextualConditionItemPriceMinimum {
                                mItemPriceMinimum: u32 = 300
                            }
                        }
                        mAudioAction: pointer = ContextualActionPlayVO {
                            mAllyEventName: string = "Purchase2DGeneral"
                        }
                    }
                }
            }
            "ShopOpen" = ContextualSituation {
                mRules: list[embed] = {
                    ContextualRule {
                        mRuleName: string = "OpenRich"
                        mConditions: list[pointer] = {
                            ContextualConditionHasGold {
                                mGold: f32 = 3000
                            }
                        }
                        mAudioAction: pointer = ContextualActionPlayVO {
                            mMaxOccurences: u32 = 1
                            mAllyEventName: string = "Open2DGold3000"
                        }
                    }
                    ContextualRule {
                        mRuleName: string = "OpenMulti"
                        mConditions: list[pointer] = {
                            ContextualConditionShopOpenCount {
                                mShopOpenCount: u32 = 7
                            }
                        }
                        mAudioAction: pointer = ContextualActionPlayVO {
                            mMaxOccurences: u32 = 1
                            mAllyEventName: string = "Open2DCountSeven"
                        }
                    }
                    ContextualRule {
                        mRuleName: string = "OpenYordle"
                        mConditions: list[pointer] = {
                            ContextualConditionCharacter {
                                mCharacterType: u8 = 1
                                mChildConditions: list[pointer] = {
                                    ContextualConditionCharacterMetadata {
                                        mCategory: string = "race"
                                        mData: string = "Yordle"
                                    }
                                }
                            }
                        }
                        mAudioAction: pointer = ContextualActionPlayVO {
                            mAllyEventName: string = "Open2DYordle"
                        }
                    }
                    ContextualRule {
                        mRuleName: string = "OpenUdyr"
                        mConditions: list[pointer] = {
                            ContextualConditionCharacter {
                                mCharacterType: u8 = 1
                                mChildConditions: list[pointer] = {
                                    ContextualConditionCharacterName {
                                        mCharacters: list[hash] = {
                                            "Characters/Udyr/CharacterRecords/Root"
                                        }
                                    }
                                }
                            }
                        }
                        mAudioAction: pointer = ContextualActionPlayVO {
                            mAllyEventName: string = "Open2DUdyr"
                        }
                    }
                    ContextualRule {
                        mRuleName: string = "OpenVolibear"
                        mConditions: list[pointer] = {
                            ContextualConditionCharacter {
                                mCharacterType: u8 = 1
                                mChildConditions: list[pointer] = {
                                    ContextualConditionCharacterName {
                                        mCharacters: list[hash] = {
                                            "Characters/Volibear/CharacterRecords/Root"
                                        }
                                    }
                                }
                            }
                        }
                        mAudioAction: pointer = ContextualActionPlayVO {
                            mAllyEventName: string = "Open2DVolibear"
                        }
                    }
                    ContextualRule {
                        mRuleName: string = "OpenOlaf"
                        mConditions: list[pointer] = {
                            ContextualConditionCharacter {
                                mCharacterType: u8 = 1
                                mChildConditions: list[pointer] = {
                                    ContextualConditionCharacterName {
                                        mCharacters: list[hash] = {
                                            "Characters/Olaf/CharacterRecords/Root"
                                        }
                                    }
                                }
                            }
                        }
                        mAudioAction: pointer = ContextualActionPlayVO {
                            mAllyEventName: string = "Open2DOlaf"
                        }
                    }
                    ContextualRule {
                        mRuleName: string = "OpenBroOlaf"
                        mConditions: list[pointer] = {
                            ContextualConditionCharacter {
                                mCharacterType: u8 = 1
                                mChildConditions: list[pointer] = {
                                    ContextualConditionCharacterSkinID {
                                        mSkinIDs: list[i32] = {
                                            3
                                        }
                                    }
                                }
                            }
                        }
                        mAudioAction: pointer = ContextualActionPlayVO {
                            mAllyEventName: string = "Open2DOlafSkin03"
                        }
                    }
                    ContextualRule {
                        mRuleName: string = "OpenGragas"
                        mConditions: list[pointer] = {
                            ContextualConditionCharacter {
                                mCharacterType: u8 = 1
                                mChildConditions: list[pointer] = {
                                    ContextualConditionCharacterName {
                                        mCharacters: list[hash] = {
                                            "Characters/Gragas/CharacterRecords/Root"
                                        }
                                    }
                                }
                            }
                        }
                        mAudioAction: pointer = ContextualActionPlayVO {
                            mAllyEventName: string = "Open2DGragas"
                        }
                    }
                    ContextualRule {
                        mRuleName: string = "OpenNunu"
                        mConditions: list[pointer] = {
                            ContextualConditionCharacter {
                                mCharacterType: u8 = 1
                                mChildConditions: list[pointer] = {
                                    ContextualConditionCharacterName {
                                        mCharacters: list[hash] = {
                                            "Characters/Nunu/CharacterRecords/Root"
                                        }
                                    }
                                }
                            }
                        }
                        mAudioAction: pointer = ContextualActionPlayVO {
                            mAllyEventName: string = "Open2DNunu"
                        }
                    }
                    ContextualRule {
                        mRuleName: string = "OpenSejuani"
                        mConditions: list[pointer] = {
                            ContextualConditionCharacter {
                                mCharacterType: u8 = 1
                                mChildConditions: list[pointer] = {
                                    ContextualConditionCharacterName {
                                        mCharacters: list[hash] = {
                                            "Characters/Sejuani/CharacterRecords/Root"
                                        }
                                    }
                                }
                            }
                        }
                        mAudioAction: pointer = ContextualActionPlayVO {
                            mAllyEventName: string = "Open2DSejuani"
                        }
                    }
                    ContextualRule {
                        mRuleName: string = "OpenLissandra"
                        mConditions: list[pointer] = {
                            ContextualConditionCharacter {
                                mCharacterType: u8 = 1
                                mChildConditions: list[pointer] = {
                                    ContextualConditionCharacterName {
                                        mCharacters: list[hash] = {
                                            "Characters/Lissandra/CharacterRecords/Root"
                                        }
                                    }
                                }
                            }
                        }
                        mAudioAction: pointer = ContextualActionPlayVO {
                            mAllyEventName: string = "Open2DLissandra"
                        }
                    }
                    ContextualRule {
                        mRuleName: string = "OpenTrundle"
                        mConditions: list[pointer] = {
                            ContextualConditionCharacter {
                                mCharacterType: u8 = 1
                                mChildConditions: list[pointer] = {
                                    ContextualConditionCharacterName {
                                        mCharacters: list[hash] = {
                                            "Characters/Trundle/CharacterRecords/Root"
                                        }
                                    }
                                }
                            }
                        }
                        mAudioAction: pointer = ContextualActionPlayVO {
                            mAllyEventName: string = "Open2DTrundle"
                        }
                    }
                    ContextualRule {
                        mRuleName: string = "OpenTryndamere"
                        mConditions: list[pointer] = {
                            ContextualConditionCharacter {
                                mCharacterType: u8 = 1
                                mChildConditions: list[pointer] = {
                                    ContextualConditionCharacterName {
                                        mCharacters: list[hash] = {
                                            "Characters/Tryndamere/CharacterRecords/Root"
                                        }
                                    }
                                }
                            }
                        }
                        mAudioAction: pointer = ContextualActionPlayVO {
                            mAllyEventName: string = "Open2DTryndamere"
                        }
                    }
                    ContextualRule {
                        mRuleName: string = "OpenAnivia"
                        mConditions: list[pointer] = {
                            ContextualConditionCharacter {
                                mCharacterType: u8 = 1
                                mChildConditions: list[pointer] = {
                                    ContextualConditionCharacterName {
                                        mCharacters: list[hash] = {
                                            "Characters/Anivia/CharacterRecords/Root"
                                        }
                                    }
                                }
                            }
                        }
                        mAudioAction: pointer = ContextualActionPlayVO {
                            mAllyEventName: string = "Open2DAnivia"
                        }
                    }
                    ContextualRule {
                        mRuleName: string = "OpenAshe"
                        mConditions: list[pointer] = {
                            ContextualConditionCharacter {
                                mCharacterType: u8 = 1
                                mChildConditions: list[pointer] = {
                                    ContextualConditionCharacterName {
                                        mCharacters: list[hash] = {
                                            "Characters/Ashe/CharacterRecords/Root"
                                        }
                                    }
                                }
                            }
                        }
                        mAudioAction: pointer = ContextualActionPlayVO {
                            mAllyEventName: string = "Open2DAshe"
                        }
                    }
                    ContextualRule {
                        mRuleName: string = "OpenBrand"
                        mConditions: list[pointer] = {
                            ContextualConditionCharacter {
                                mCharacterType: u8 = 1
                                mChildConditions: list[pointer] = {
                                    ContextualConditionCharacterName {
                                        mCharacters: list[hash] = {
                                            "Characters/Brand/CharacterRecords/Root"
                                        }
                                    }
                                }
                            }
                        }
                        mAudioAction: pointer = ContextualActionPlayVO {
                            mAllyEventName: string = "Open2DBrand"
                        }
                    }
                    ContextualRule {
                        mRuleName: string = "OpenNami"
                        mConditions: list[pointer] = {
                            ContextualConditionCharacter {
                                mCharacterType: u8 = 1
                                mChildConditions: list[pointer] = {
                                    ContextualConditionCharacterName {
                                        mCharacters: list[hash] = {
                                            "Characters/Nami/CharacterRecords/Root"
                                        }
                                    }
                                }
                            }
                        }
                        mAudioAction: pointer = ContextualActionPlayVO {
                            mAllyEventName: string = "Open2DNami"
                        }
                    }
                    ContextualRule {
                        mRuleName: string = "ShopOpen"
                        mAudioAction: pointer = ContextualActionPlayVO {
                            mAllyEventName: string = "Open2DGeneral"
                        }
                    }
                }
            }
            "ShopClose" = ContextualSituation {
                mRules: list[embed] = {
                    ContextualRule {
                        mRuleName: string = "CloseForgotItems"
                        mConditions: list[pointer] = {
                            ContextualConditionItemPurchased {}
                        }
                        mAudioAction: pointer = ContextualActionPlayVO {
                            mAllyEventName: string = "Close3DNoPurchase"
                        }
                    }
                    ContextualRule {
                        mRuleName: string = "ShopClose"
                        mAudioAction: pointer = ContextualActionPlayVO {
                            mAllyEventName: string = "Close3DGeneral"
                        }
                    }
                }
            }
            "Browsing" = ContextualSituation {
                mRules: list[embed] = {
                    ContextualRule {
                        mRuleName: string = "Browsing"
                        mConditions: list[pointer] = {
                            ContextualConditionCustomTimer {
                                mCustomTimer: f32 = 22
                            }
                        }
                        mAudioAction: pointer = ContextualActionPlayVO {
                            mAllyEventName: string = "Browsing2DGeneral"
                        }
                    }
                }
            }
            "Ambient" = ContextualSituation {
                mRules: list[embed] = {
                    ContextualRule {
                        mRuleName: string = "Ambient"
                        mConditions: list[pointer] = {
                            ContextualConditionCustomTimer {
                                mCustomTimer: f32 = 28
                            }
                        }
                        mAudioAction: pointer = ContextualActionPlayVO {
                            mAllyEventName: string = "Ambient3DGeneral"
                        }
                    }
                }
            }
        }
        mObjectPath: string = "Characters/HA_AP_Viking/CAC/HA_AP_Viking"
    }
}
