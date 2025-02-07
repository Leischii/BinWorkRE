#PROP_text
type: string = "PROP"
version: u32 = 3
linked: list[string] = {}
entries: map[hash,embed] = {
    0x202b438c = ContextualActionData {
        mCooldown: f32 = 1
        mSituations: map[hash,embed] = {
            "Ambient" = ContextualSituation {
                mRules: list[embed] = {
                    ContextualRule {
                        mRuleName: string = "Ambient - 25s"
                        mConditions: list[pointer] = {
                            ContextualConditionCustomTimer {
                                mCustomTimer: f32 = 25
                            }
                        }
                        mAudioAction: pointer = ContextualActionPlayVO {
                            mAllyEventName: string = "Ambient3DGeneral"
                        }
                        0x98b66135: pointer = 0x15f6e07a {
                            0xc59f257e: bool = true
                        }
                    }
                }
            }
            "Browsing" = ContextualSituation {
                mRules: list[embed] = {
                    ContextualRule {
                        mRuleName: string = "Browsing - 22s"
                        mConditions: list[pointer] = {
                            ContextualConditionCustomTimer {
                                mCustomTimer: f32 = 22
                            }
                        }
                        mAudioAction: pointer = ContextualActionPlayVO {
                            mAllyEventName: string = "Browsing2DGeneral"
                        }
                        0x98b66135: pointer = 0x15f6e07a {
                            IgnoreTimer: bool = true
                            0xc59f257e: bool = true
                        }
                    }
                }
            }
            "ShopClose" = ContextualSituation {
                mRules: list[embed] = {
                    ContextualRule {
                        mRuleName: string = "Close"
                        mAudioAction: pointer = ContextualActionPlayVO {
                            mAllyEventName: string = "Close3DGeneral"
                        }
                        0x98b66135: pointer = 0x15f6e07a {
                            IgnoreTimer: bool = true
                            0xc59f257e: bool = true
                        }
                    }
                    ContextualRule {
                        mRuleName: string = "Game Timer"
                        mAudioAction: pointer = ContextualActionPlayVO {
                            mAllyEventName: string = "Close3DGameTimerTwentyFive"
                        }
                        0x98b66135: pointer = 0x15f6e07a {
                            IgnoreTimer: bool = true
                            0xc59f257e: bool = true
                        }
                    }
                    ContextualRule {
                        mRuleName: string = "General"
                        mAudioAction: pointer = ContextualActionPlayVO {
                            mAllyEventName: string = "Close3DGeneral"
                        }
                        0x98b66135: pointer = 0x15f6e07a {
                            IgnoreTimer: bool = true
                            0xc59f257e: bool = true
                        }
                    }
                }
            }
            "ShopOpen" = ContextualSituation {
                mRules: list[embed] = {
                    ContextualRule {
                        mRuleName: string = "Specific Faction/Race"
                        mConditions: list[pointer] = {
                            ContextualConditionCharacter {
                                mCharacterType: u8 = 1
                                mChildConditions: list[pointer] = {
                                    ContextualConditionCharacterMetadata {
                                        mCategory: string = "faction"
                                        mData: string = "piltover"
                                    }
                                }
                            }
                        }
                        mAudioAction: pointer = ContextualActionPlayVO {
                            mMaxOccurences: u32 = 1
                            mAllyEventName: string = "Open2DPiltover"
                        }
                        0x98b66135: pointer = 0x15f6e07a {
                            IgnoreTimer: bool = true
                            0xc59f257e: bool = true
                        }
                    }
                    ContextualRule {
                        mRuleName: string = "Specific Champion"
                        mConditions: list[pointer] = {
                            ContextualConditionCharacter {
                                mCharacterType: u8 = 1
                                mChildConditions: list[pointer] = {
                                    ContextualConditionCharacterName {
                                        mCharacters: list[hash] = {
                                            "Characters/Blitzcrank/CharacterRecords/Root"
                                        }
                                    }
                                }
                            }
                        }
                        mAudioAction: pointer = ContextualActionPlayVO {
                            mMaxOccurences: u32 = 1
                            mAllyEventName: string = "Open2DBlitzcrank"
                        }
                        0x98b66135: pointer = 0x15f6e07a {
                            IgnoreTimer: bool = true
                            0xc59f257e: bool = true
                        }
                    }
                    ContextualRule {
                        mRuleName: string = "Game Timer"
                        mConditions: list[pointer] = {
                            ContextualConditionGameTimer {
                                mGameTimeInMinutes: f32 = 25
                            }
                        }
                        mAudioAction: pointer = ContextualActionPlayVO {
                            mMaxOccurences: u32 = 3
                            mAllyEventName: string = "Open2DGameTimerTwentyFive"
                        }
                        0x98b66135: pointer = 0x15f6e07a {
                            IgnoreTimer: bool = true
                            0xc59f257e: bool = true
                        }
                    }
                    ContextualRule {
                        mRuleName: string = "Open Count"
                        mConditions: list[pointer] = {
                            ContextualConditionShopOpenCount {
                                mShopOpenCount: u32 = 10
                            }
                        }
                        mAudioAction: pointer = ContextualActionPlayVO {
                            mMaxOccurences: u32 = 3
                            mAllyEventName: string = "Open2DCount10"
                        }
                        0x98b66135: pointer = 0x15f6e07a {
                            IgnoreTimer: bool = true
                            0xc59f257e: bool = true
                        }
                    }
                    ContextualRule {
                        mRuleName: string = "Nearby Ally Count"
                        mConditions: list[pointer] = {
                            ContextualConditionNearbyChampionCount {
                                mCount: u32 = 2
                                mCompareOp: u8 = 3
                            }
                        }
                        mAudioAction: pointer = ContextualActionPlayVO {
                            mMaxOccurences: u32 = 3
                            mAllyEventName: string = "Open2DNearbyAllyCountTwo"
                        }
                        0x98b66135: pointer = 0x15f6e07a {
                            IgnoreTimer: bool = true
                            0xc59f257e: bool = true
                        }
                    }
                    ContextualRule {
                        mRuleName: string = "Nearby Enemy Count"
                        mConditions: list[pointer] = {
                            ContextualConditionNearbyChampionCount {
                                mTeamCompareOp: u8 = 1
                                mCount: u32 = 2
                                mCompareOp: u8 = 3
                            }
                        }
                        mAudioAction: pointer = ContextualActionPlayVO {
                            mMaxOccurences: u32 = 3
                            mAllyEventName: string = "Open2DNearbyEnemyCountTwo"
                        }
                        0x98b66135: pointer = 0x15f6e07a {
                            IgnoreTimer: bool = true
                            0xc59f257e: bool = true
                        }
                    }
                    ContextualRule {
                        mRuleName: string = "Gold"
                        mConditions: list[pointer] = {
                            ContextualConditionHasGold {
                                mGold: f32 = 3000
                            }
                        }
                        mAudioAction: pointer = ContextualActionPlayVO {
                            mMaxOccurences: u32 = 3
                            mAllyEventName: string = "Open2DGold3000"
                        }
                        0x98b66135: pointer = 0x15f6e07a {
                            IgnoreTimer: bool = true
                            0xc59f257e: bool = true
                        }
                    }
                    ContextualRule {
                        mRuleName: string = "General"
                        mAudioAction: pointer = ContextualActionPlayVO {
                            mAllyEventName: string = "Open2DGeneral"
                        }
                        0x98b66135: pointer = 0x15f6e07a {
                            0xc59f257e: bool = true
                        }
                    }
                }
            }
            "Purchase" = ContextualSituation {
                mRules: list[embed] = {
                    ContextualRule {
                        mRuleName: string = "MinimumPrice"
                        mConditions: list[pointer] = {
                            ContextualConditionItemPriceMinimum {
                                mItemPriceMinimum: u32 = 2900
                            }
                        }
                        mAudioAction: pointer = ContextualActionPlayVO {
                            mMaxOccurences: u32 = 3
                            mAllyEventName: string = "Purchase2DMinimumPrice2900"
                        }
                        0x98b66135: pointer = 0x15f6e07a {
                            IgnoreTimer: bool = true
                            0xc59f257e: bool = true
                        }
                    }
                    ContextualRule {
                        mRuleName: string = "Specific Item"
                        mConditions: list[pointer] = {
                            ContextualConditionItemID {
                                mItems: list[hash] = {
                                    "Items/6609"
                                    "Items/226609"
                                }
                            }
                        }
                        mAudioAction: pointer = ContextualActionPlayVO {
                            mMaxOccurences: u32 = 1
                            mAllyEventName: string = "Purchase2DChempunkChainsword"
                        }
                        0x98b66135: pointer = 0x15f6e07a {
                            IgnoreTimer: bool = true
                            0xc59f257e: bool = true
                        }
                    }
                    ContextualRule {
                        mRuleName: string = "General"
                        mAudioAction: pointer = ContextualActionPlayVO {
                            mAllyEventName: string = "Purchase2DGeneral"
                        }
                        0x98b66135: pointer = 0x15f6e07a {
                            IgnoreTimer: bool = true
                            0xc59f257e: bool = true
                        }
                    }
                }
            }
        }
        mObjectPath: string = "Characters/HA_AP_Viking/CAC/Shopkeeper_CAC_Template"
    }
    "Characters/HA_AP_Viking/CharacterRecords/Root" = CharacterRecord {
        mCharacterName: string = "HA_AP_Viking"
        primaryAbilityResource: embed = AbilityResourceSlotInfo {
            arType: u8 = 0
        }
        characterToolData: embed = characterToolData {
            mapAIPresence: map[u32,embed] = {
                0 = ToolAiPresence {}
                1 = ToolAiPresence {}
                2 = ToolAiPresence {}
            }
        }
        flags: u32 = 8398144
    }
    "Characters/HA_AP_Viking/Skins/Meta" = SkinCharacterMetaDataProperties {}
}
