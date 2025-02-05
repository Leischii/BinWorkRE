#PROP_text
type: string = "PROP"
version: u32 = 3
linked: list[string] = {}
entries: map[hash,embed] = {
    0x075d43f4 = CharacterRecord {
        mCharacterName: string = "Turret"
        mFallbackCharacterName: string = "SRUAP_Turret"
        targetLaserEffects: pointer = TargetLaserComponentEffects {
            beamEffectDefinition: embed = SkinCharacterDataProperties_CharacterIdleEffect {
                effectKey: hash = 0xb6e0e814
                boneName: string = "joint2"
            }
            towerTargetingEffectDefinition: embed = SkinCharacterDataProperties_CharacterIdleEffect {
                effectName: string = "Yikes-Tower.troy"
                boneName: string = "joint2"
            }
            champTargetingEffectDefinition: embed = SkinCharacterDataProperties_CharacterIdleEffect {
                effectName: string = "yikes-champ.troy"
                boneName: string = "C_Buffbone_Glb_Head_Loc"
            }
        }
        DisabledTargetLaserEffects: pointer = TargetLaserComponentEffects {
            beamEffectDefinition: embed = SkinCharacterDataProperties_CharacterIdleEffect {
                effectKey: hash = "LaserSight_Beam_Disabled"
                boneName: string = "joint2"
            }
            towerTargetingEffectDefinition: embed = SkinCharacterDataProperties_CharacterIdleEffect {
                effectName: string = "Yikes-Tower.troy"
                boneName: string = "joint2"
            }
            champTargetingEffectDefinition: embed = SkinCharacterDataProperties_CharacterIdleEffect {
                effectName: string = "yikes-champ.troy"
                boneName: string = "C_Buffbone_Glb_Head_Loc"
            }
        }
        baseHP: f32 = 5000
        baseStaticHPRegen: f32 = 0
        healthBarHeight: f32 = 525
        healthBarFullParallax: bool = true
        primaryAbilityResource: embed = AbilityResourceSlotInfo {
            arType: u8 = 7
            arBase: f32 = 3
            arBaseStaticRegen: f32 = 0
            arIncrements: f32 = 1
            arMaxSegments: i32 = 3
            arHasRegenText: bool = false
            0xa9d3a87c: bool = true
        }
        secondaryAbilityResource: embed = AbilityResourceSlotInfo {
            arType: u8 = 7
            arBase: f32 = 3
            arBaseStaticRegen: f32 = 0
            arIncrements: f32 = 1
            arMaxSegments: i32 = 3
        }
        baseDamage: f32 = 182
        baseArmor: f32 = 15
        baseSpellBlock: f32 = 15
        baseMoveSpeed: f32 = 0
        attackRange: f32 = 750
        attackSpeed: f32 = 0.833000004
        attackSpeedRatio: f32 = 0.833000004
        attackSpeedPerLevel: f32 = 2.125
        basicAttack: embed = AttackSlotData {
            mAttackDelayCastOffsetPercent: option[f32] = {
                -0.160999998
            }
            mAttackProbability: option[f32] = {
                0
            }
            mAttackName: option[string] = {
                "TurretBasicAttack"
            }
        }
        extraAttacks: list[embed] = {
            AttackSlotData {
                mAttackProbability: option[f32] = {
                    0
                }
                mAttackName: option[string] = {
                    "TurretBasicAttack2"
                }
            }
            AttackSlotData {
                mAttackProbability: option[f32] = {
                    0
                }
                mAttackName: option[string] = {
                    "TurretBasicAttack3"
                }
            }
            AttackSlotData {
                mAttackProbability: option[f32] = {
                    0
                }
                mAttackName: option[string] = {
                    "TurretBasicAttack4"
                }
            }
        }
        expGivenOnDeath: f32 = 0
        goldGivenOnDeath: f32 = 0
        localGoldGivenOnDeath: f32 = 250
        localGoldSplitWithLastHitter: bool = true
        globalGoldGivenOnDeath: f32 = 50
        name: string = "game_character_displayname_TurretOuter"
        hitFxScale: f32 = 0.5
        selectionHeight: f32 = 200
        selectionRadius: f32 = 130
        pathfindingCollisionRadius: f32 = 125
        overrideGameplayCollisionRadius: option[f32] = {
            88.4000015
        }
        unitTagsString: string = "Structure | Structure_Turret | Structure_Turret_Outer"
        characterToolData: embed = characterToolData {
            mapAIPresence: map[u32,embed] = {
                0 = ToolAiPresence {}
                1 = ToolAiPresence {}
                2 = ToolAiPresence {}
            }
            description: string = "game_character_description_OuterTurret"
        }
        mClientSideItemInventory: list[hash] = {
            "Items/1500"
            "Items/1502"
            "Items/1503"
            "Items/1501"
            "Items/1515"
            "Items/1517"
            0x51d3d599
        }
        occludedUnitSelectableDistance: f32 = 500
    }
    0x0affaac0 = CharacterRecord {
        mCharacterName: string = "Turret"
        mFallbackCharacterName: string = "HA_Turret"
        targetLaserEffects: pointer = TargetLaserComponentEffects {
            beamEffectDefinition: embed = SkinCharacterDataProperties_CharacterIdleEffect {
                effectKey: hash = 0xb6e0e814
                boneName: string = "joint2"
            }
            towerTargetingEffectDefinition: embed = SkinCharacterDataProperties_CharacterIdleEffect {
                effectName: string = "Yikes-Tower.troy"
                boneName: string = "joint2"
            }
            champTargetingEffectDefinition: embed = SkinCharacterDataProperties_CharacterIdleEffect {
                effectName: string = "yikes-champ.troy"
                boneName: string = "C_Buffbone_Glb_Head_Loc"
            }
        }
        DisabledTargetLaserEffects: pointer = TargetLaserComponentEffects {
            beamEffectDefinition: embed = SkinCharacterDataProperties_CharacterIdleEffect {
                effectKey: hash = "LaserSight_Beam_Disabled"
                boneName: string = "joint2"
            }
            towerTargetingEffectDefinition: embed = SkinCharacterDataProperties_CharacterIdleEffect {
                effectName: string = "Yikes-Tower.troy"
                boneName: string = "joint2"
            }
            champTargetingEffectDefinition: embed = SkinCharacterDataProperties_CharacterIdleEffect {
                effectName: string = "yikes-champ.troy"
                boneName: string = "C_Buffbone_Glb_Head_Loc"
            }
        }
        baseHP: f32 = 1700
        baseStaticHPRegen: f32 = 0
        healthBarHeight: f32 = 625
        healthBarFullParallax: bool = true
        primaryAbilityResource: embed = AbilityResourceSlotInfo {
            arType: u8 = 7
            arBase: f32 = 3
            arBaseStaticRegen: f32 = 0
            arIncrements: f32 = 1
            arMaxSegments: i32 = 3
            arHasRegenText: bool = false
            0xa9d3a87c: bool = true
        }
        baseDamage: f32 = 185
        baseArmor: f32 = 70
        baseSpellBlock: f32 = 75
        baseMoveSpeed: f32 = 0
        attackRange: f32 = 750
        attackSpeed: f32 = 0.833000004
        attackSpeedRatio: f32 = 0.833000004
        attackSpeedPerLevel: f32 = 2.125
        basicAttack: embed = AttackSlotData {
            mAttackDelayCastOffsetPercent: option[f32] = {
                -0.160999998
            }
            mAttackProbability: option[f32] = {
                0
            }
            mAttackName: option[string] = {
                "TurretBasicAttack"
            }
        }
        extraAttacks: list[embed] = {
            AttackSlotData {
                mAttackProbability: option[f32] = {
                    0
                }
                mAttackName: option[string] = {
                    "TurretBasicAttack2"
                }
            }
            AttackSlotData {
                mAttackProbability: option[f32] = {
                    0
                }
                mAttackName: option[string] = {
                    "TurretBasicAttack3"
                }
            }
            AttackSlotData {
                mAttackProbability: option[f32] = {
                    0
                }
                mAttackName: option[string] = {
                    "TurretBasicAttack4"
                }
            }
        }
        expGivenOnDeath: f32 = 0
        goldGivenOnDeath: f32 = 0
        localGoldSplitWithLastHitter: bool = true
        globalGoldGivenOnDeath: f32 = 150
        globalExpGivenOnDeath: f32 = 30
        name: string = "game_character_displayname_TurretNormal"
        hitFxScale: f32 = 0.5
        selectionHeight: f32 = 200
        selectionRadius: f32 = 130
        pathfindingCollisionRadius: f32 = 125
        overrideGameplayCollisionRadius: option[f32] = {
            88.4000015
        }
        unitTagsString: string = "Structure | Structure_Turret | Structure_Turret_Outer"
        characterToolData: embed = characterToolData {
            mapAIPresence: map[u32,embed] = {
                0 = ToolAiPresence {}
                1 = ToolAiPresence {}
                2 = ToolAiPresence {}
            }
            description: string = "game_character_description_HATurret"
        }
        mClientSideItemInventory: list[hash] = {
            "Items/1500"
            "Items/1502"
            "Items/1503"
        }
        occludedUnitSelectableDistance: f32 = 700
    }
    0x0d44e839 = CharacterRecord {
        mCharacterName: string = "Turret"
        mFallbackCharacterName: string = "HA_Turret"
        targetLaserEffects: pointer = TargetLaserComponentEffects {
            beamEffectDefinition: embed = SkinCharacterDataProperties_CharacterIdleEffect {
                effectKey: hash = 0xb6e0e814
                boneName: string = "joint2"
            }
            towerTargetingEffectDefinition: embed = SkinCharacterDataProperties_CharacterIdleEffect {
                effectName: string = "Yikes-Tower.troy"
                boneName: string = "joint2"
            }
            champTargetingEffectDefinition: embed = SkinCharacterDataProperties_CharacterIdleEffect {
                effectName: string = "yikes-champ.troy"
                boneName: string = "C_Buffbone_Glb_Head_Loc"
            }
        }
        DisabledTargetLaserEffects: pointer = TargetLaserComponentEffects {
            beamEffectDefinition: embed = SkinCharacterDataProperties_CharacterIdleEffect {
                effectKey: hash = "LaserSight_Beam_Disabled"
                boneName: string = "joint2"
            }
            towerTargetingEffectDefinition: embed = SkinCharacterDataProperties_CharacterIdleEffect {
                effectName: string = "Yikes-Tower.troy"
                boneName: string = "joint2"
            }
            champTargetingEffectDefinition: embed = SkinCharacterDataProperties_CharacterIdleEffect {
                effectName: string = "yikes-champ.troy"
                boneName: string = "C_Buffbone_Glb_Head_Loc"
            }
        }
        baseHP: f32 = 3500
        baseStaticHPRegen: f32 = 0
        healthBarHeight: f32 = 625
        healthBarFullParallax: bool = true
        primaryAbilityResource: embed = AbilityResourceSlotInfo {
            arType: u8 = 7
            arBase: f32 = 3
            arBaseStaticRegen: f32 = 0
            arIncrements: f32 = 1
            arMaxSegments: i32 = 3
            arHasRegenText: bool = false
            0xa9d3a87c: bool = true
        }
        baseDamage: f32 = 195
        baseArmor: f32 = 60
        baseSpellBlock: f32 = 60
        baseMoveSpeed: f32 = 0
        attackRange: f32 = 750
        attackSpeed: f32 = 0.833000004
        attackSpeedRatio: f32 = 0.833000004
        attackSpeedPerLevel: f32 = 2.125
        basicAttack: embed = AttackSlotData {
            mAttackDelayCastOffsetPercent: option[f32] = {
                -0.160999998
            }
            mAttackProbability: option[f32] = {
                0
            }
            mAttackName: option[string] = {
                "TurretBasicAttack"
            }
        }
        extraAttacks: list[embed] = {
            AttackSlotData {
                mAttackProbability: option[f32] = {
                    0
                }
                mAttackName: option[string] = {
                    "TurretBasicAttack2"
                }
            }
            AttackSlotData {
                mAttackProbability: option[f32] = {
                    0
                }
                mAttackName: option[string] = {
                    "TurretBasicAttack3"
                }
            }
            AttackSlotData {
                mAttackProbability: option[f32] = {
                    0
                }
                mAttackName: option[string] = {
                    "TurretBasicAttack4"
                }
            }
        }
        expGivenOnDeath: f32 = 0
        goldGivenOnDeath: f32 = 0
        localGoldSplitWithLastHitter: bool = true
        globalGoldGivenOnDeath: f32 = 150
        globalExpGivenOnDeath: f32 = 70
        name: string = "game_character_displayname_TurretInhibitor"
        hitFxScale: f32 = 0.5
        selectionHeight: f32 = 200
        selectionRadius: f32 = 130
        pathfindingCollisionRadius: f32 = 125
        overrideGameplayCollisionRadius: option[f32] = {
            88.4000015
        }
        unitTagsString: string = "Structure | Structure_Turret | Structure_Turret_Inhib"
        characterToolData: embed = characterToolData {
            mapAIPresence: map[u32,embed] = {
                0 = ToolAiPresence {}
                1 = ToolAiPresence {}
                2 = ToolAiPresence {}
            }
            description: string = "game_character_description_InhibitorTurret"
        }
        mClientSideItemInventory: list[hash] = {
            "Items/1500"
            "Items/1502"
            "Items/1503"
            "Items/1520"
            "Items/1522"
            "Items/1521"
        }
        occludedUnitSelectableDistance: f32 = 700
    }
    0x1604393f = CharacterRecord {
        mCharacterName: string = "Turret"
        mFallbackCharacterName: string = "SRUAP_Turret"
        targetLaserEffects: pointer = TargetLaserComponentEffects {
            beamEffectDefinition: embed = SkinCharacterDataProperties_CharacterIdleEffect {
                effectKey: hash = 0xb6e0e814
                boneName: string = "joint2"
            }
            towerTargetingEffectDefinition: embed = SkinCharacterDataProperties_CharacterIdleEffect {
                effectName: string = "Yikes-Tower.troy"
                boneName: string = "joint2"
            }
            champTargetingEffectDefinition: embed = SkinCharacterDataProperties_CharacterIdleEffect {
                effectName: string = "yikes-champ.troy"
                boneName: string = "C_Buffbone_Glb_Head_Loc"
            }
        }
        DisabledTargetLaserEffects: pointer = TargetLaserComponentEffects {
            beamEffectDefinition: embed = SkinCharacterDataProperties_CharacterIdleEffect {
                effectKey: hash = "LaserSight_Beam_Disabled"
                boneName: string = "joint2"
            }
            towerTargetingEffectDefinition: embed = SkinCharacterDataProperties_CharacterIdleEffect {
                effectName: string = "Yikes-Tower.troy"
                boneName: string = "joint2"
            }
            champTargetingEffectDefinition: embed = SkinCharacterDataProperties_CharacterIdleEffect {
                effectName: string = "yikes-champ.troy"
                boneName: string = "C_Buffbone_Glb_Head_Loc"
            }
        }
        baseHP: f32 = 3000
        baseStaticHPRegen: f32 = 0
        healthBarHeight: f32 = 525
        healthBarFullParallax: bool = true
        primaryAbilityResource: embed = AbilityResourceSlotInfo {
            arType: u8 = 7
            arBase: f32 = 3
            arBaseStaticRegen: f32 = 0
            arIncrements: f32 = 1
            arMaxSegments: i32 = 3
            arHasRegenText: bool = false
            0xa9d3a87c: bool = true
        }
        baseDamage: f32 = 152
        baseArmor: f32 = 15
        baseSpellBlock: f32 = 15
        baseMoveSpeed: f32 = 0
        attackRange: f32 = 750
        attackSpeed: f32 = 0.833000004
        attackSpeedRatio: f32 = 0.833000004
        attackSpeedPerLevel: f32 = 2.125
        basicAttack: embed = AttackSlotData {
            mAttackDelayCastOffsetPercent: option[f32] = {
                -0.160999998
            }
            mAttackProbability: option[f32] = {
                0
            }
            mAttackName: option[string] = {
                "TurretBasicAttack"
            }
        }
        extraAttacks: list[embed] = {
            AttackSlotData {
                mAttackProbability: option[f32] = {
                    0
                }
                mAttackName: option[string] = {
                    "TurretBasicAttack2"
                }
            }
            AttackSlotData {
                mAttackProbability: option[f32] = {
                    0
                }
                mAttackName: option[string] = {
                    "TurretBasicAttack3"
                }
            }
            AttackSlotData {
                mAttackProbability: option[f32] = {
                    0
                }
                mAttackName: option[string] = {
                    "TurretBasicAttack4"
                }
            }
        }
        expGivenOnDeath: f32 = 0
        goldGivenOnDeath: f32 = 0
        localGoldGivenOnDeath: f32 = 250
        localGoldSplitWithLastHitter: bool = true
        globalGoldGivenOnDeath: f32 = 50
        name: string = "game_character_displayname_TurretNormal"
        hitFxScale: f32 = 0.5
        selectionHeight: f32 = 200
        selectionRadius: f32 = 130
        pathfindingCollisionRadius: f32 = 125
        overrideGameplayCollisionRadius: option[f32] = {
            88.4000015
        }
        unitTagsString: string = "Structure | Structure_Turret | Structure_Turret_Outer"
        characterToolData: embed = characterToolData {
            mapAIPresence: map[u32,embed] = {
                0 = ToolAiPresence {}
                1 = ToolAiPresence {}
                2 = ToolAiPresence {}
            }
            description: string = "game_character_description_SRTurret"
        }
        mClientSideItemInventory: list[hash] = {
            "Items/1500"
            "Items/1502"
            "Items/1503"
            "Items/1501"
            "Items/1515"
            "Items/1517"
        }
        occludedUnitSelectableDistance: f32 = 500
    }
    0x1bbcdf96 = CharacterRecord {
        mCharacterName: string = "Turret"
        mFallbackCharacterName: string = "SRUAP_Turret"
        targetLaserEffects: pointer = TargetLaserComponentEffects {
            beamEffectDefinition: embed = SkinCharacterDataProperties_CharacterIdleEffect {
                effectKey: hash = 0xb6e0e814
                boneName: string = "joint2"
            }
            towerTargetingEffectDefinition: embed = SkinCharacterDataProperties_CharacterIdleEffect {
                effectName: string = "Yikes-Tower.troy"
                boneName: string = "joint2"
            }
            champTargetingEffectDefinition: embed = SkinCharacterDataProperties_CharacterIdleEffect {
                effectName: string = "yikes-champ.troy"
                boneName: string = "C_Buffbone_Glb_Head_Loc"
            }
        }
        DisabledTargetLaserEffects: pointer = TargetLaserComponentEffects {
            beamEffectDefinition: embed = SkinCharacterDataProperties_CharacterIdleEffect {
                effectKey: hash = "LaserSight_Beam_Disabled"
                boneName: string = "joint2"
            }
            towerTargetingEffectDefinition: embed = SkinCharacterDataProperties_CharacterIdleEffect {
                effectName: string = "Yikes-Tower.troy"
                boneName: string = "joint2"
            }
            champTargetingEffectDefinition: embed = SkinCharacterDataProperties_CharacterIdleEffect {
                effectName: string = "yikes-champ.troy"
                boneName: string = "C_Buffbone_Glb_Head_Loc"
            }
        }
        baseHP: f32 = 5000
        baseStaticHPRegen: f32 = 0
        healthBarHeight: f32 = 525
        healthBarFullParallax: bool = true
        primaryAbilityResource: embed = AbilityResourceSlotInfo {
            arType: u8 = 7
            arBase: f32 = 3
            arBaseStaticRegen: f32 = 0
            arIncrements: f32 = 1
            arMaxSegments: i32 = 3
            arHasRegenText: bool = false
            0xa9d3a87c: bool = true
        }
        baseDamage: f32 = 152
        baseArmor: f32 = 15
        baseSpellBlock: f32 = 15
        baseMoveSpeed: f32 = 0
        attackRange: f32 = 750
        attackSpeed: f32 = 0.833000004
        attackSpeedRatio: f32 = 0.833000004
        attackSpeedPerLevel: f32 = 2.125
        basicAttack: embed = AttackSlotData {
            mAttackDelayCastOffsetPercent: option[f32] = {
                -0.160999998
            }
            mAttackProbability: option[f32] = {
                0
            }
            mAttackName: option[string] = {
                "TurretBasicAttack"
            }
        }
        extraAttacks: list[embed] = {
            AttackSlotData {
                mAttackProbability: option[f32] = {
                    0
                }
                mAttackName: option[string] = {
                    "TurretBasicAttack2"
                }
            }
            AttackSlotData {
                mAttackProbability: option[f32] = {
                    0
                }
                mAttackName: option[string] = {
                    "TurretBasicAttack3"
                }
            }
            AttackSlotData {
                mAttackProbability: option[f32] = {
                    0
                }
                mAttackName: option[string] = {
                    "TurretBasicAttack4"
                }
            }
        }
        expGivenOnDeath: f32 = 0
        goldGivenOnDeath: f32 = 0
        localGoldGivenOnDeath: f32 = 250
        localGoldSplitWithLastHitter: bool = true
        globalGoldGivenOnDeath: f32 = 50
        name: string = "game_character_displayname_TurretNormal"
        hitFxScale: f32 = 0.5
        selectionHeight: f32 = 200
        selectionRadius: f32 = 130
        pathfindingCollisionRadius: f32 = 125
        overrideGameplayCollisionRadius: option[f32] = {
            88.4000015
        }
        unitTagsString: string = "Structure | Structure_Turret | Structure_Turret_Outer"
        characterToolData: embed = characterToolData {
            mapAIPresence: map[u32,embed] = {
                0 = ToolAiPresence {}
                1 = ToolAiPresence {}
                2 = ToolAiPresence {}
            }
            description: string = "game_character_description_SRTurret"
        }
        mClientSideItemInventory: list[hash] = {
            "Items/1500"
            "Items/1502"
            "Items/1503"
            "Items/1501"
            "Items/1515"
            "Items/1517"
        }
        occludedUnitSelectableDistance: f32 = 500
    }
    0x209ac1e0 = CharacterRecord {
        mCharacterName: string = "HA_AP_ChaosTurretTutorial"
        mFallbackCharacterName: string = "HA_AP_ChaosTurret"
        targetLaserEffects: pointer = TargetLaserComponentEffects {
            beamEffectDefinition: embed = SkinCharacterDataProperties_CharacterIdleEffect {
                effectName: string = "LaserSight_beam.troy"
                boneName: string = "joint2"
            }
            towerTargetingEffectDefinition: embed = SkinCharacterDataProperties_CharacterIdleEffect {
                effectName: string = "Yikes-Tower.troy"
                boneName: string = "joint2"
            }
            champTargetingEffectDefinition: embed = SkinCharacterDataProperties_CharacterIdleEffect {
                effectName: string = "yikes-champ.troy"
                boneName: string = "C_Buffbone_Glb_Head_Loc"
            }
        }
        DisabledTargetLaserEffects: pointer = TargetLaserComponentEffects {
            beamEffectDefinition: embed = SkinCharacterDataProperties_CharacterIdleEffect {
                effectKey: hash = "LaserSight_Beam_Disabled"
                boneName: string = "joint2"
            }
            towerTargetingEffectDefinition: embed = SkinCharacterDataProperties_CharacterIdleEffect {
                effectName: string = "Yikes-Tower.troy"
                boneName: string = "joint2"
            }
            champTargetingEffectDefinition: embed = SkinCharacterDataProperties_CharacterIdleEffect {
                effectName: string = "yikes-champ.troy"
                boneName: string = "C_Buffbone_Glb_Head_Loc"
            }
        }
        baseHP: f32 = 1300
        baseStaticHPRegen: f32 = 0
        healthBarHeight: f32 = 600
        healthBarFullParallax: bool = true
        primaryAbilityResource: embed = AbilityResourceSlotInfo {
            arBase: f32 = 0
            arBaseStaticRegen: f32 = 0
        }
        baseDamage: f32 = 150
        damagePerLevel: f32 = 0.100000001
        baseArmor: f32 = 0
        baseSpellBlock: f32 = 75
        baseMoveSpeed: f32 = 0
        attackRange: f32 = 700
        attackSpeed: f32 = 1
        attackSpeedRatio: f32 = 0.833000004
        attackSpeedPerLevel: f32 = 2.125
        acquisitionRange: f32 = 700
        basicAttack: embed = AttackSlotData {
            mAttackDelayCastOffsetPercent: option[f32] = {
                0
            }
        }
        extraAttacks: list[embed] = {
            AttackSlotData {
                mAttackProbability: option[f32] = {
                    0
                }
                mAttackName: option[string] = {
                    "TurretBasicAttack2"
                }
            }
            AttackSlotData {
                mAttackProbability: option[f32] = {
                    0
                }
                mAttackName: option[string] = {
                    "TurretBasicAttack3"
                }
            }
            AttackSlotData {
                mAttackProbability: option[f32] = {
                    0
                }
                mAttackName: option[string] = {
                    "TurretBasicAttack4"
                }
            }
        }
        expGivenOnDeath: f32 = 0
        goldGivenOnDeath: f32 = 0
        localGoldSplitWithLastHitter: bool = true
        globalGoldGivenOnDeath: f32 = 100
        globalExpGivenOnDeath: f32 = 300
        name: string = "game_character_displayname_ChaosTurretTutorial"
        hitFxScale: f32 = 0.5
        selectionHeight: f32 = 200
        selectionRadius: f32 = 130
        pathfindingCollisionRadius: f32 = 125
        overrideGameplayCollisionRadius: option[f32] = {
            88.4000015
        }
        unitTagsString: string = "Structure | Structure_Turret | Structure_Turret_Outer"
        characterToolData: embed = characterToolData {
            mapAIPresence: map[u32,embed] = {
                0 = ToolAiPresence {}
                1 = ToolAiPresence {}
                2 = ToolAiPresence {}
            }
            description: string = "game_character_description_ChaosTurretTutorial"
        }
        mClientSideItemInventory: list[hash] = {
            "Items/1500"
            "Items/1502"
            "Items/1503"
        }
        occludedUnitSelectableDistance: f32 = 700
    }
    0x325fd17c = CharacterRecord {
        mCharacterName: string = "NexusTurret"
        mFallbackCharacterName: string = "SRUAP_Turret"
        targetLaserEffects: pointer = TargetLaserComponentEffects {
            beamEffectDefinition: embed = SkinCharacterDataProperties_CharacterIdleEffect {
                effectKey: hash = 0xb6e0e814
                boneName: string = "joint2"
            }
            towerTargetingEffectDefinition: embed = SkinCharacterDataProperties_CharacterIdleEffect {
                effectName: string = "Yikes-Tower.troy"
                boneName: string = "joint2"
            }
            champTargetingEffectDefinition: embed = SkinCharacterDataProperties_CharacterIdleEffect {
                effectName: string = "yikes-champ.troy"
                boneName: string = "C_Buffbone_Glb_Head_Loc"
            }
        }
        DisabledTargetLaserEffects: pointer = TargetLaserComponentEffects {
            beamEffectDefinition: embed = SkinCharacterDataProperties_CharacterIdleEffect {
                effectKey: hash = "LaserSight_Beam_Disabled"
                boneName: string = "joint2"
            }
            towerTargetingEffectDefinition: embed = SkinCharacterDataProperties_CharacterIdleEffect {
                effectName: string = "Yikes-Tower.troy"
                boneName: string = "joint2"
            }
            champTargetingEffectDefinition: embed = SkinCharacterDataProperties_CharacterIdleEffect {
                effectName: string = "yikes-champ.troy"
                boneName: string = "C_Buffbone_Glb_Head_Loc"
            }
        }
        baseHP: f32 = 3000
        baseStaticHPRegen: f32 = 15
        healthBarHeight: f32 = 525
        healthBarFullParallax: bool = true
        primaryAbilityResource: embed = AbilityResourceSlotInfo {
            arType: u8 = 7
            arBase: f32 = 3
            arBaseStaticRegen: f32 = 0
            arIncrements: f32 = 1
            arMaxSegments: i32 = 3
            arHasRegenText: bool = false
            0xa9d3a87c: bool = true
        }
        baseDamage: f32 = 170
        baseArmor: f32 = 75
        baseSpellBlock: f32 = 75
        baseMoveSpeed: f32 = 0
        attackRange: f32 = 550
        attackSpeed: f32 = 1.35000002
        attackSpeedRatio: f32 = 0
        acquisitionRange: f32 = 700
        basicAttack: embed = AttackSlotData {
            mAttackDelayCastOffsetPercent: option[f32] = {
                -0.160999998
            }
            mAttackProbability: option[f32] = {
                0
            }
            mAttackName: option[string] = {
                "TurretBasicAttack"
            }
        }
        extraAttacks: list[embed] = {
            AttackSlotData {
                mAttackProbability: option[f32] = {
                    0
                }
                mAttackName: option[string] = {
                    "TurretBasicAttack2"
                }
            }
            AttackSlotData {
                mAttackProbability: option[f32] = {
                    0
                }
                mAttackName: option[string] = {
                    "TurretBasicAttack3"
                }
            }
            AttackSlotData {
                mAttackProbability: option[f32] = {
                    0
                }
                mAttackName: option[string] = {
                    "TurretBasicAttack4"
                }
            }
        }
        expGivenOnDeath: f32 = 0
        goldGivenOnDeath: f32 = 0
        localGoldGivenOnDeath: f32 = 250
        localGoldSplitWithLastHitter: bool = true
        globalGoldGivenOnDeath: f32 = 50
        name: string = "game_character_displayname_TurretNexus"
        hitFxScale: f32 = 0.5
        selectionHeight: f32 = 200
        selectionRadius: f32 = 130
        pathfindingCollisionRadius: f32 = 125
        overrideGameplayCollisionRadius: option[f32] = {
            88.4000015
        }
        unitTagsString: string = "Structure | Structure_Turret | Structure_Turret_Nexus"
        characterToolData: embed = characterToolData {
            mapAIPresence: map[u32,embed] = {
                0 = ToolAiPresence {}
                1 = ToolAiPresence {}
                2 = ToolAiPresence {}
            }
            description: string = "game_character_description_NexusTurret"
        }
        mClientSideItemInventory: list[hash] = {
            "Items/1500"
            "Items/1502"
            "Items/1503"
            "Items/1501"
            "Items/1515"
            "Items/1517"
            "Items/1507"
        }
        occludedUnitSelectableDistance: f32 = 500
    }
    0x3e2fe8a7 = CharacterRecord {
        mCharacterName: string = "Turret"
        mFallbackCharacterName: string = "SRUAP_Turret"
        targetLaserEffects: pointer = TargetLaserComponentEffects {
            beamEffectDefinition: embed = SkinCharacterDataProperties_CharacterIdleEffect {
                effectKey: hash = 0xb6e0e814
                boneName: string = "joint2"
            }
            towerTargetingEffectDefinition: embed = SkinCharacterDataProperties_CharacterIdleEffect {
                effectName: string = "Yikes-Tower.troy"
                boneName: string = "joint2"
            }
            champTargetingEffectDefinition: embed = SkinCharacterDataProperties_CharacterIdleEffect {
                effectName: string = "yikes-champ.troy"
                boneName: string = "C_Buffbone_Glb_Head_Loc"
            }
        }
        DisabledTargetLaserEffects: pointer = TargetLaserComponentEffects {
            beamEffectDefinition: embed = SkinCharacterDataProperties_CharacterIdleEffect {
                effectKey: hash = "LaserSight_Beam_Disabled"
                boneName: string = "joint2"
            }
            towerTargetingEffectDefinition: embed = SkinCharacterDataProperties_CharacterIdleEffect {
                effectName: string = "Yikes-Tower.troy"
                boneName: string = "joint2"
            }
            champTargetingEffectDefinition: embed = SkinCharacterDataProperties_CharacterIdleEffect {
                effectName: string = "yikes-champ.troy"
                boneName: string = "C_Buffbone_Glb_Head_Loc"
            }
        }
        baseHP: f32 = 4000
        baseStaticHPRegen: f32 = 0
        healthBarHeight: f32 = 485
        healthBarFullParallax: bool = true
        primaryAbilityResource: embed = AbilityResourceSlotInfo {
            arType: u8 = 7
            arBase: f32 = 3
            arBaseStaticRegen: f32 = 0
            arIncrements: f32 = 1
            arMaxSegments: i32 = 3
            arHasRegenText: bool = false
            0xa9d3a87c: bool = true
        }
        baseDamage: f32 = 187
        baseArmor: f32 = 50
        baseSpellBlock: f32 = 50
        baseMoveSpeed: f32 = 0
        attackRange: f32 = 750
        attackSpeed: f32 = 0.833000004
        attackSpeedRatio: f32 = 0.833000004
        attackSpeedPerLevel: f32 = 2.125
        basicAttack: embed = AttackSlotData {
            mAttackDelayCastOffsetPercent: option[f32] = {
                -0.160999998
            }
            mAttackProbability: option[f32] = {
                0
            }
            mAttackName: option[string] = {
                "TurretBasicAttack"
            }
        }
        extraAttacks: list[embed] = {
            AttackSlotData {
                mAttackProbability: option[f32] = {
                    0
                }
                mAttackName: option[string] = {
                    "TurretBasicAttack2"
                }
            }
            AttackSlotData {
                mAttackProbability: option[f32] = {
                    0
                }
                mAttackName: option[string] = {
                    "TurretBasicAttack3"
                }
            }
            AttackSlotData {
                mAttackProbability: option[f32] = {
                    0
                }
                mAttackName: option[string] = {
                    "TurretBasicAttack4"
                }
            }
        }
        expGivenOnDeath: f32 = 0
        goldGivenOnDeath: f32 = 0
        localGoldGivenOnDeath: f32 = 425
        localGoldSplitWithLastHitter: bool = true
        globalGoldGivenOnDeath: f32 = 25
        name: string = "game_character_displayname_TurretInner"
        hitFxScale: f32 = 0.5
        selectionHeight: f32 = 200
        selectionRadius: f32 = 130
        pathfindingCollisionRadius: f32 = 125
        overrideGameplayCollisionRadius: option[f32] = {
            88.4000015
        }
        unitTagsString: string = "Structure | Structure_Turret | Structure_Turret_Inner"
        characterToolData: embed = characterToolData {
            mapAIPresence: map[u32,embed] = {
                0 = ToolAiPresence {}
                1 = ToolAiPresence {}
                2 = ToolAiPresence {}
            }
            description: string = "game_character_description_InnerTurret"
        }
        mClientSideItemInventory: list[hash] = {
            "Items/1500"
            "Items/1502"
            "Items/1503"
            "Items/1516"
            "Items/1519"
            0x51d3d599
        }
        occludedUnitSelectableDistance: f32 = 500
    }
    0x4003641c = CharacterRecord {
        mCharacterName: string = "Turret"
        mFallbackCharacterName: string = "HA_Turret"
        targetLaserEffects: pointer = TargetLaserComponentEffects {
            beamEffectDefinition: embed = SkinCharacterDataProperties_CharacterIdleEffect {
                effectKey: hash = 0xb6e0e814
                boneName: string = "joint2"
            }
            towerTargetingEffectDefinition: embed = SkinCharacterDataProperties_CharacterIdleEffect {
                effectName: string = "Yikes-Tower.troy"
                boneName: string = "joint2"
            }
            champTargetingEffectDefinition: embed = SkinCharacterDataProperties_CharacterIdleEffect {
                effectName: string = "yikes-champ.troy"
                boneName: string = "C_Buffbone_Glb_Head_Loc"
            }
        }
        DisabledTargetLaserEffects: pointer = TargetLaserComponentEffects {
            beamEffectDefinition: embed = SkinCharacterDataProperties_CharacterIdleEffect {
                effectKey: hash = "LaserSight_Beam_Disabled"
                boneName: string = "joint2"
            }
            towerTargetingEffectDefinition: embed = SkinCharacterDataProperties_CharacterIdleEffect {
                effectName: string = "Yikes-Tower.troy"
                boneName: string = "joint2"
            }
            champTargetingEffectDefinition: embed = SkinCharacterDataProperties_CharacterIdleEffect {
                effectName: string = "yikes-champ.troy"
                boneName: string = "C_Buffbone_Glb_Head_Loc"
            }
        }
        baseHP: f32 = 1700
        baseStaticHPRegen: f32 = 0
        healthBarHeight: f32 = 625
        healthBarFullParallax: bool = true
        primaryAbilityResource: embed = AbilityResourceSlotInfo {
            arType: u8 = 7
            arBase: f32 = 3
            arBaseStaticRegen: f32 = 0
            arIncrements: f32 = 1
            arMaxSegments: i32 = 3
            arHasRegenText: bool = false
            0xa9d3a87c: bool = true
        }
        baseDamage: f32 = 185
        baseArmor: f32 = 60
        baseSpellBlock: f32 = 60
        baseMoveSpeed: f32 = 0
        attackRange: f32 = 750
        attackSpeed: f32 = 0.833000004
        attackSpeedRatio: f32 = 0.833000004
        attackSpeedPerLevel: f32 = 2.125
        basicAttack: embed = AttackSlotData {
            mAttackDelayCastOffsetPercent: option[f32] = {
                -0.160999998
            }
            mAttackProbability: option[f32] = {
                0
            }
            mAttackName: option[string] = {
                "TurretBasicAttack"
            }
        }
        extraAttacks: list[embed] = {
            AttackSlotData {
                mAttackProbability: option[f32] = {
                    0
                }
                mAttackName: option[string] = {
                    "TurretBasicAttack2"
                }
            }
            AttackSlotData {
                mAttackProbability: option[f32] = {
                    0
                }
                mAttackName: option[string] = {
                    "TurretBasicAttack3"
                }
            }
            AttackSlotData {
                mAttackProbability: option[f32] = {
                    0
                }
                mAttackName: option[string] = {
                    "TurretBasicAttack4"
                }
            }
        }
        expGivenOnDeath: f32 = 0
        goldGivenOnDeath: f32 = 0
        localGoldSplitWithLastHitter: bool = true
        globalGoldGivenOnDeath: f32 = 150
        globalExpGivenOnDeath: f32 = 30
        name: string = "game_character_displayname_TurretOuter"
        hitFxScale: f32 = 0.5
        selectionHeight: f32 = 200
        selectionRadius: f32 = 130
        pathfindingCollisionRadius: f32 = 125
        overrideGameplayCollisionRadius: option[f32] = {
            88.4000015
        }
        unitTagsString: string = "Structure | Structure_Turret | Structure_Turret_Outer"
        characterToolData: embed = characterToolData {
            mapAIPresence: map[u32,embed] = {
                0 = ToolAiPresence {}
                1 = ToolAiPresence {}
                2 = ToolAiPresence {}
            }
            description: string = "game_character_description_OuterTurret"
        }
        mClientSideItemInventory: list[hash] = {
            "Items/1500"
            "Items/1502"
            "Items/1503"
            "Items/1520"
            "Items/1522"
        }
        occludedUnitSelectableDistance: f32 = 700
    }
    0x640bb061 = CharacterRecord {
        mCharacterName: string = "Turret"
        mFallbackCharacterName: string = "SRUAP_Turret"
        targetLaserEffects: pointer = TargetLaserComponentEffects {
            beamEffectDefinition: embed = SkinCharacterDataProperties_CharacterIdleEffect {
                effectKey: hash = 0xb6e0e814
                boneName: string = "joint2"
            }
            towerTargetingEffectDefinition: embed = SkinCharacterDataProperties_CharacterIdleEffect {
                effectName: string = "Yikes-Tower.troy"
                boneName: string = "joint2"
            }
            champTargetingEffectDefinition: embed = SkinCharacterDataProperties_CharacterIdleEffect {
                effectName: string = "yikes-champ.troy"
                boneName: string = "C_Buffbone_Glb_Head_Loc"
            }
        }
        DisabledTargetLaserEffects: pointer = TargetLaserComponentEffects {
            beamEffectDefinition: embed = SkinCharacterDataProperties_CharacterIdleEffect {
                effectKey: hash = "LaserSight_Beam_Disabled"
                boneName: string = "joint2"
            }
            towerTargetingEffectDefinition: embed = SkinCharacterDataProperties_CharacterIdleEffect {
                effectName: string = "Yikes-Tower.troy"
                boneName: string = "joint2"
            }
            champTargetingEffectDefinition: embed = SkinCharacterDataProperties_CharacterIdleEffect {
                effectName: string = "yikes-champ.troy"
                boneName: string = "C_Buffbone_Glb_Head_Loc"
            }
        }
        baseHP: f32 = 3500
        baseStaticHPRegen: f32 = 0
        healthBarHeight: f32 = 485
        healthBarFullParallax: bool = true
        primaryAbilityResource: embed = AbilityResourceSlotInfo {
            arType: u8 = 7
            arBase: f32 = 3
            arBaseStaticRegen: f32 = 0
            arIncrements: f32 = 1
            arMaxSegments: i32 = 3
            arHasRegenText: bool = false
            0xa9d3a87c: bool = true
        }
        secondaryAbilityResource: embed = AbilityResourceSlotInfo {
            arBase: f32 = 0
            arBaseStaticRegen: f32 = 0
        }
        baseDamage: f32 = 187
        baseArmor: f32 = 50
        baseSpellBlock: f32 = 50
        baseMoveSpeed: f32 = 0
        attackRange: f32 = 750
        attackSpeed: f32 = 0.833000004
        attackSpeedRatio: f32 = 0.833000004
        attackSpeedPerLevel: f32 = 2.125
        basicAttack: embed = AttackSlotData {
            mAttackDelayCastOffsetPercent: option[f32] = {
                -0.160999998
            }
            mAttackProbability: option[f32] = {
                0
            }
            mAttackName: option[string] = {
                "TurretBasicAttack"
            }
        }
        extraAttacks: list[embed] = {
            AttackSlotData {
                mAttackProbability: option[f32] = {
                    0
                }
                mAttackName: option[string] = {
                    "TurretBasicAttack2"
                }
            }
            AttackSlotData {
                mAttackProbability: option[f32] = {
                    0
                }
                mAttackName: option[string] = {
                    "TurretBasicAttack3"
                }
            }
            AttackSlotData {
                mAttackProbability: option[f32] = {
                    0
                }
                mAttackName: option[string] = {
                    "TurretBasicAttack4"
                }
            }
        }
        expGivenOnDeath: f32 = 0
        goldGivenOnDeath: f32 = 0
        localGoldGivenOnDeath: f32 = 375
        localGoldSplitWithLastHitter: bool = true
        globalGoldGivenOnDeath: f32 = 25
        name: string = "game_character_displayname_TurretInhibitor"
        hitFxScale: f32 = 0.5
        selectionHeight: f32 = 200
        selectionRadius: f32 = 130
        pathfindingCollisionRadius: f32 = 125
        overrideGameplayCollisionRadius: option[f32] = {
            88.4000015
        }
        unitTagsString: string = "Structure | Structure_Turret | Structure_Turret_Inhib"
        characterToolData: embed = characterToolData {
            mapAIPresence: map[u32,embed] = {
                0 = ToolAiPresence {}
                1 = ToolAiPresence {}
                2 = ToolAiPresence {}
            }
            description: string = "game_character_description_InhibitorTurret"
        }
        mClientSideItemInventory: list[hash] = {
            "Items/1500"
            "Items/1506"
            "Items/1503"
            "Items/1518"
            0x51d3d599
        }
        occludedUnitSelectableDistance: f32 = 500
    }
    0x689ec240 = CharacterRecord {
        mCharacterName: string = "HA_AP_OrderTurretTutorial"
        mFallbackCharacterName: string = "HA_AP_OrderTurret"
        targetLaserEffects: pointer = TargetLaserComponentEffects {
            beamEffectDefinition: embed = SkinCharacterDataProperties_CharacterIdleEffect {
                effectName: string = "LaserSight_beam.troy"
                boneName: string = "joint2"
            }
            towerTargetingEffectDefinition: embed = SkinCharacterDataProperties_CharacterIdleEffect {
                effectName: string = "Yikes-Tower.troy"
                boneName: string = "joint2"
            }
            champTargetingEffectDefinition: embed = SkinCharacterDataProperties_CharacterIdleEffect {
                effectName: string = "yikes-champ.troy"
                boneName: string = "C_Buffbone_Glb_Head_Loc"
            }
        }
        DisabledTargetLaserEffects: pointer = TargetLaserComponentEffects {
            beamEffectDefinition: embed = SkinCharacterDataProperties_CharacterIdleEffect {
                effectKey: hash = "LaserSight_Beam_Disabled"
                boneName: string = "joint2"
            }
            towerTargetingEffectDefinition: embed = SkinCharacterDataProperties_CharacterIdleEffect {
                effectName: string = "Yikes-Tower.troy"
                boneName: string = "joint2"
            }
            champTargetingEffectDefinition: embed = SkinCharacterDataProperties_CharacterIdleEffect {
                effectName: string = "yikes-champ.troy"
                boneName: string = "C_Buffbone_Glb_Head_Loc"
            }
        }
        baseHP: f32 = 400
        baseStaticHPRegen: f32 = 0
        healthBarHeight: f32 = 625
        healthBarFullParallax: bool = true
        primaryAbilityResource: embed = AbilityResourceSlotInfo {
            arBase: f32 = 0
            arBaseStaticRegen: f32 = 0
        }
        baseDamage: f32 = 0.100000001
        baseArmor: f32 = 0
        baseSpellBlock: f32 = 75
        baseMoveSpeed: f32 = 0
        attackRange: f32 = 700
        attackSpeed: f32 = 1
        attackSpeedRatio: f32 = 0.833000004
        attackSpeedPerLevel: f32 = 2.125
        acquisitionRange: f32 = 700
        basicAttack: embed = AttackSlotData {
            mAttackDelayCastOffsetPercent: option[f32] = {
                0
            }
        }
        extraAttacks: list[embed] = {
            AttackSlotData {
                mAttackProbability: option[f32] = {
                    0
                }
                mAttackName: option[string] = {
                    "TurretBasicAttack2"
                }
            }
            AttackSlotData {
                mAttackProbability: option[f32] = {
                    0
                }
                mAttackName: option[string] = {
                    "TurretBasicAttack3"
                }
            }
            AttackSlotData {
                mAttackProbability: option[f32] = {
                    0
                }
                mAttackName: option[string] = {
                    "TurretBasicAttack4"
                }
            }
        }
        expGivenOnDeath: f32 = 0
        goldGivenOnDeath: f32 = 0
        localGoldSplitWithLastHitter: bool = true
        globalGoldGivenOnDeath: f32 = 100
        globalExpGivenOnDeath: f32 = 300
        name: string = "game_character_displayname_OrderTurretTutorial"
        hitFxScale: f32 = 0.5
        selectionHeight: f32 = 200
        selectionRadius: f32 = 130
        pathfindingCollisionRadius: f32 = 125
        overrideGameplayCollisionRadius: option[f32] = {
            88.4000015
        }
        unitTagsString: string = "Structure | Structure_Turret | Structure_Turret_Outer"
        characterToolData: embed = characterToolData {
            mapAIPresence: map[u32,embed] = {
                0 = ToolAiPresence {}
                1 = ToolAiPresence {}
                2 = ToolAiPresence {}
            }
            description: string = "game_character_description_OrderTurretTutorial"
        }
        mClientSideItemInventory: list[hash] = {
            "Items/1500"
            "Items/1502"
            "Items/1503"
        }
        occludedUnitSelectableDistance: f32 = 700
    }
    "Characters/Turret/CharacterRecords/Root" = CharacterRecord {
        mCharacterName: string = "Turret"
        targetLaserEffects: pointer = TargetLaserComponentEffects {
            beamEffectDefinition: embed = SkinCharacterDataProperties_CharacterIdleEffect {
                effectKey: hash = 0xb6e0e814
                boneName: string = "joint2"
            }
            towerTargetingEffectDefinition: embed = SkinCharacterDataProperties_CharacterIdleEffect {
                effectName: string = "Yikes-Tower.troy"
                boneName: string = "joint2"
            }
            champTargetingEffectDefinition: embed = SkinCharacterDataProperties_CharacterIdleEffect {
                effectName: string = "yikes-champ.troy"
                boneName: string = "C_Buffbone_Glb_Head_Loc"
            }
        }
        DisabledTargetLaserEffects: pointer = TargetLaserComponentEffects {
            beamEffectDefinition: embed = SkinCharacterDataProperties_CharacterIdleEffect {
                effectKey: hash = "LaserSight_Beam_Disabled"
                boneName: string = "joint2"
            }
            towerTargetingEffectDefinition: embed = SkinCharacterDataProperties_CharacterIdleEffect {
                effectName: string = "Yikes-Tower.troy"
                boneName: string = "joint2"
            }
            champTargetingEffectDefinition: embed = SkinCharacterDataProperties_CharacterIdleEffect {
                effectName: string = "yikes-champ.troy"
                boneName: string = "C_Buffbone_Glb_Head_Loc"
            }
        }
        baseHP: f32 = 5000
        baseStaticHPRegen: f32 = 0
        healthBarHeight: f32 = 525
        healthBarFullParallax: bool = true
        primaryAbilityResource: embed = AbilityResourceSlotInfo {
            arType: u8 = 7
            arBase: f32 = 3
            arBaseStaticRegen: f32 = 0
            arIncrements: f32 = 1
            arMaxSegments: i32 = 3
            arHasRegenText: bool = false
            0xa9d3a87c: bool = true
        }
        baseDamage: f32 = 152
        baseArmor: f32 = 15
        baseSpellBlock: f32 = 15
        baseMoveSpeed: f32 = 0
        attackRange: f32 = 750
        attackSpeed: f32 = 0.833000004
        attackSpeedRatio: f32 = 0.833000004
        attackSpeedPerLevel: f32 = 2.125
        basicAttack: embed = AttackSlotData {
            mAttackDelayCastOffsetPercent: option[f32] = {
                -0.160999998
            }
            mAttackProbability: option[f32] = {
                0
            }
            mAttackName: option[string] = {
                "TurretBasicAttack"
            }
        }
        extraAttacks: list[embed] = {
            AttackSlotData {
                mAttackProbability: option[f32] = {
                    0
                }
                mAttackName: option[string] = {
                    "TurretBasicAttack2"
                }
            }
            AttackSlotData {
                mAttackProbability: option[f32] = {
                    0
                }
                mAttackName: option[string] = {
                    "TurretBasicAttack3"
                }
            }
            AttackSlotData {
                mAttackProbability: option[f32] = {
                    0
                }
                mAttackName: option[string] = {
                    "TurretBasicAttack4"
                }
            }
        }
        expGivenOnDeath: f32 = 0
        goldGivenOnDeath: f32 = 0
        localGoldGivenOnDeath: f32 = 250
        localGoldSplitWithLastHitter: bool = true
        globalGoldGivenOnDeath: f32 = 50
        name: string = "game_character_displayname_TurretNormal"
        hitFxScale: f32 = 0.5
        selectionHeight: f32 = 200
        selectionRadius: f32 = 130
        pathfindingCollisionRadius: f32 = 125
        overrideGameplayCollisionRadius: option[f32] = {
            88.4000015
        }
        unitTagsString: string = "Structure | Structure_Turret | Structure_Turret_Outer"
        characterToolData: embed = characterToolData {
            mapAIPresence: map[u32,embed] = {
                0 = ToolAiPresence {}
                1 = ToolAiPresence {}
                2 = ToolAiPresence {}
            }
            description: string = "game_character_description_RootTurret"
        }
        mClientSideItemInventory: list[hash] = {
            "Items/1500"
            "Items/1502"
            "Items/1503"
            "Items/1501"
            "Items/1515"
            "Items/1517"
        }
        occludedUnitSelectableDistance: f32 = 500
    }
    0x9d71ab2e = CharacterRecord {
        mCharacterName: string = "Turret"
        mFallbackCharacterName: string = "SRUAP_Turret"
        targetLaserEffects: pointer = TargetLaserComponentEffects {
            beamEffectDefinition: embed = SkinCharacterDataProperties_CharacterIdleEffect {
                effectKey: hash = 0xb6e0e814
                boneName: string = "joint2"
            }
            towerTargetingEffectDefinition: embed = SkinCharacterDataProperties_CharacterIdleEffect {
                effectName: string = "Yikes-Tower.troy"
                boneName: string = "joint2"
            }
            champTargetingEffectDefinition: embed = SkinCharacterDataProperties_CharacterIdleEffect {
                effectName: string = "yikes-champ.troy"
                boneName: string = "C_Buffbone_Glb_Head_Loc"
            }
        }
        DisabledTargetLaserEffects: pointer = TargetLaserComponentEffects {
            beamEffectDefinition: embed = SkinCharacterDataProperties_CharacterIdleEffect {
                effectKey: hash = "LaserSight_Beam_Disabled"
                boneName: string = "joint2"
            }
            towerTargetingEffectDefinition: embed = SkinCharacterDataProperties_CharacterIdleEffect {
                effectName: string = "Yikes-Tower.troy"
                boneName: string = "joint2"
            }
            champTargetingEffectDefinition: embed = SkinCharacterDataProperties_CharacterIdleEffect {
                effectName: string = "yikes-champ.troy"
                boneName: string = "C_Buffbone_Glb_Head_Loc"
            }
        }
        baseHP: f32 = 5000
        baseStaticHPRegen: f32 = 0
        healthBarHeight: f32 = 525
        healthBarFullParallax: bool = true
        primaryAbilityResource: embed = AbilityResourceSlotInfo {
            arType: u8 = 7
            arBase: f32 = 3
            arBaseStaticRegen: f32 = 0
            arIncrements: f32 = 1
            arMaxSegments: i32 = 3
            arHasRegenText: bool = false
            0xa9d3a87c: bool = true
        }
        secondaryAbilityResource: embed = AbilityResourceSlotInfo {
            arType: u8 = 7
            arBase: f32 = 3
            arBaseStaticRegen: f32 = 0
            arIncrements: f32 = 1
            arMaxSegments: i32 = 3
        }
        baseDamage: f32 = 182
        baseArmor: f32 = 15
        baseSpellBlock: f32 = 15
        baseMoveSpeed: f32 = 0
        attackRange: f32 = 750
        attackSpeed: f32 = 0.833000004
        attackSpeedRatio: f32 = 0.833000004
        attackSpeedPerLevel: f32 = 2.125
        basicAttack: embed = AttackSlotData {
            mAttackDelayCastOffsetPercent: option[f32] = {
                -0.160999998
            }
            mAttackProbability: option[f32] = {
                0
            }
            mAttackName: option[string] = {
                "TurretBasicAttack"
            }
        }
        extraAttacks: list[embed] = {
            AttackSlotData {
                mAttackProbability: option[f32] = {
                    0
                }
                mAttackName: option[string] = {
                    "TurretBasicAttack2"
                }
            }
            AttackSlotData {
                mAttackProbability: option[f32] = {
                    0
                }
                mAttackName: option[string] = {
                    "TurretBasicAttack3"
                }
            }
            AttackSlotData {
                mAttackProbability: option[f32] = {
                    0
                }
                mAttackName: option[string] = {
                    "TurretBasicAttack4"
                }
            }
        }
        expGivenOnDeath: f32 = 0
        goldGivenOnDeath: f32 = 0
        localGoldGivenOnDeath: f32 = 250
        localGoldSplitWithLastHitter: bool = true
        globalGoldGivenOnDeath: f32 = 50
        name: string = "game_character_displayname_TurretOuter"
        hitFxScale: f32 = 0.5
        selectionHeight: f32 = 200
        selectionRadius: f32 = 130
        pathfindingCollisionRadius: f32 = 125
        overrideGameplayCollisionRadius: option[f32] = {
            88.4000015
        }
        unitTagsString: string = "Structure | Structure_Turret | Structure_Turret_Outer"
        characterToolData: embed = characterToolData {
            mapAIPresence: map[u32,embed] = {
                0 = ToolAiPresence {}
                1 = ToolAiPresence {}
                2 = ToolAiPresence {}
            }
            description: string = "game_character_description_OuterTurret"
        }
        mClientSideItemInventory: list[hash] = {
            "Items/1500"
            "Items/1502"
            "Items/1503"
            "Items/1501"
            "Items/1515"
            "Items/1517"
            "Items/1507"
        }
        occludedUnitSelectableDistance: f32 = 500
    }
    0xa1f8429b = CharacterRecord {
        mCharacterName: string = "Turret"
        mFallbackCharacterName: string = "SRUAP_Turret"
        targetLaserEffects: pointer = TargetLaserComponentEffects {
            beamEffectDefinition: embed = SkinCharacterDataProperties_CharacterIdleEffect {
                effectKey: hash = 0xb6e0e814
                boneName: string = "joint2"
            }
            towerTargetingEffectDefinition: embed = SkinCharacterDataProperties_CharacterIdleEffect {
                effectName: string = "Yikes-Tower.troy"
                boneName: string = "joint2"
            }
            champTargetingEffectDefinition: embed = SkinCharacterDataProperties_CharacterIdleEffect {
                effectName: string = "yikes-champ.troy"
                boneName: string = "C_Buffbone_Glb_Head_Loc"
            }
        }
        DisabledTargetLaserEffects: pointer = TargetLaserComponentEffects {
            beamEffectDefinition: embed = SkinCharacterDataProperties_CharacterIdleEffect {
                effectKey: hash = "LaserSight_Beam_Disabled"
                boneName: string = "joint2"
            }
            towerTargetingEffectDefinition: embed = SkinCharacterDataProperties_CharacterIdleEffect {
                effectName: string = "Yikes-Tower.troy"
                boneName: string = "joint2"
            }
            champTargetingEffectDefinition: embed = SkinCharacterDataProperties_CharacterIdleEffect {
                effectName: string = "yikes-champ.troy"
                boneName: string = "C_Buffbone_Glb_Head_Loc"
            }
        }
        baseHP: f32 = 3500
        baseStaticHPRegen: f32 = 0
        healthBarHeight: f32 = 485
        healthBarFullParallax: bool = true
        primaryAbilityResource: embed = AbilityResourceSlotInfo {
            arType: u8 = 7
            arBase: f32 = 3
            arBaseStaticRegen: f32 = 0
            arIncrements: f32 = 1
            arMaxSegments: i32 = 3
            arHasRegenText: bool = false
            0xa9d3a87c: bool = true
        }
        secondaryAbilityResource: embed = AbilityResourceSlotInfo {
            arBase: f32 = 0
            arBaseStaticRegen: f32 = 0
        }
        baseDamage: f32 = 187
        baseArmor: f32 = 70
        baseSpellBlock: f32 = 70
        baseMoveSpeed: f32 = 0
        attackRange: f32 = 750
        attackSpeed: f32 = 0.833000004
        attackSpeedRatio: f32 = 0.833000004
        attackSpeedPerLevel: f32 = 2.125
        basicAttack: embed = AttackSlotData {
            mAttackDelayCastOffsetPercent: option[f32] = {
                -0.160999998
            }
            mAttackProbability: option[f32] = {
                0
            }
            mAttackName: option[string] = {
                "TurretBasicAttack"
            }
        }
        extraAttacks: list[embed] = {
            AttackSlotData {
                mAttackProbability: option[f32] = {
                    0
                }
                mAttackName: option[string] = {
                    "TurretBasicAttack2"
                }
            }
            AttackSlotData {
                mAttackProbability: option[f32] = {
                    0
                }
                mAttackName: option[string] = {
                    "TurretBasicAttack3"
                }
            }
            AttackSlotData {
                mAttackProbability: option[f32] = {
                    0
                }
                mAttackName: option[string] = {
                    "TurretBasicAttack4"
                }
            }
        }
        expGivenOnDeath: f32 = 0
        goldGivenOnDeath: f32 = 0
        localGoldGivenOnDeath: f32 = 375
        localGoldSplitWithLastHitter: bool = true
        globalGoldGivenOnDeath: f32 = 25
        name: string = "game_character_displayname_TurretInhibitor"
        hitFxScale: f32 = 0.5
        selectionHeight: f32 = 200
        selectionRadius: f32 = 130
        pathfindingCollisionRadius: f32 = 125
        overrideGameplayCollisionRadius: option[f32] = {
            88.4000015
        }
        unitTagsString: string = "Structure | Structure_Turret | Structure_Turret_Inhib"
        characterToolData: embed = characterToolData {
            mapAIPresence: map[u32,embed] = {
                0 = ToolAiPresence {}
                1 = ToolAiPresence {}
                2 = ToolAiPresence {}
            }
            description: string = "game_character_description_InhibitorTurret"
        }
        mClientSideItemInventory: list[hash] = {
            "Items/1500"
            "Items/1506"
            "Items/1503"
            "Items/1518"
            "Items/1507"
        }
        occludedUnitSelectableDistance: f32 = 500
    }
    0xe1f854f5 = CharacterRecord {
        mCharacterName: string = "Turret"
        mFallbackCharacterName: string = "SRUAP_Turret"
        targetLaserEffects: pointer = TargetLaserComponentEffects {
            beamEffectDefinition: embed = SkinCharacterDataProperties_CharacterIdleEffect {
                effectKey: hash = 0xb6e0e814
                boneName: string = "joint2"
            }
            towerTargetingEffectDefinition: embed = SkinCharacterDataProperties_CharacterIdleEffect {
                effectName: string = "Yikes-Tower.troy"
                boneName: string = "joint2"
            }
            champTargetingEffectDefinition: embed = SkinCharacterDataProperties_CharacterIdleEffect {
                effectName: string = "yikes-champ.troy"
                boneName: string = "C_Buffbone_Glb_Head_Loc"
            }
        }
        DisabledTargetLaserEffects: pointer = TargetLaserComponentEffects {
            beamEffectDefinition: embed = SkinCharacterDataProperties_CharacterIdleEffect {
                effectKey: hash = "LaserSight_Beam_Disabled"
                boneName: string = "joint2"
            }
            towerTargetingEffectDefinition: embed = SkinCharacterDataProperties_CharacterIdleEffect {
                effectName: string = "Yikes-Tower.troy"
                boneName: string = "joint2"
            }
            champTargetingEffectDefinition: embed = SkinCharacterDataProperties_CharacterIdleEffect {
                effectName: string = "yikes-champ.troy"
                boneName: string = "C_Buffbone_Glb_Head_Loc"
            }
        }
        baseHP: f32 = 4000
        baseStaticHPRegen: f32 = 0
        healthBarHeight: f32 = 485
        healthBarFullParallax: bool = true
        primaryAbilityResource: embed = AbilityResourceSlotInfo {
            arType: u8 = 7
            arBase: f32 = 3
            arBaseStaticRegen: f32 = 0
            arIncrements: f32 = 1
            arMaxSegments: i32 = 3
            arHasRegenText: bool = false
            0xa9d3a87c: bool = true
        }
        baseDamage: f32 = 187
        baseArmor: f32 = 55
        baseSpellBlock: f32 = 55
        baseMoveSpeed: f32 = 0
        attackRange: f32 = 750
        attackSpeed: f32 = 0.833000004
        attackSpeedRatio: f32 = 0.833000004
        attackSpeedPerLevel: f32 = 2.125
        basicAttack: embed = AttackSlotData {
            mAttackDelayCastOffsetPercent: option[f32] = {
                -0.160999998
            }
            mAttackProbability: option[f32] = {
                0
            }
            mAttackName: option[string] = {
                "TurretBasicAttack"
            }
        }
        extraAttacks: list[embed] = {
            AttackSlotData {
                mAttackProbability: option[f32] = {
                    0
                }
                mAttackName: option[string] = {
                    "TurretBasicAttack2"
                }
            }
            AttackSlotData {
                mAttackProbability: option[f32] = {
                    0
                }
                mAttackName: option[string] = {
                    "TurretBasicAttack3"
                }
            }
            AttackSlotData {
                mAttackProbability: option[f32] = {
                    0
                }
                mAttackName: option[string] = {
                    "TurretBasicAttack4"
                }
            }
        }
        expGivenOnDeath: f32 = 0
        goldGivenOnDeath: f32 = 0
        localGoldGivenOnDeath: f32 = 425
        localGoldSplitWithLastHitter: bool = true
        globalGoldGivenOnDeath: f32 = 25
        name: string = "game_character_displayname_TurretInner"
        hitFxScale: f32 = 0.5
        selectionHeight: f32 = 200
        selectionRadius: f32 = 130
        pathfindingCollisionRadius: f32 = 125
        overrideGameplayCollisionRadius: option[f32] = {
            88.4000015
        }
        unitTagsString: string = "Structure | Structure_Turret | Structure_Turret_Inner"
        characterToolData: embed = characterToolData {
            mapAIPresence: map[u32,embed] = {
                0 = ToolAiPresence {}
                1 = ToolAiPresence {}
                2 = ToolAiPresence {}
            }
            description: string = "game_character_description_InnerTurret"
        }
        mClientSideItemInventory: list[hash] = {
            "Items/1500"
            "Items/1502"
            "Items/1503"
            "Items/1516"
            "Items/1519"
            "Items/1507"
        }
        occludedUnitSelectableDistance: f32 = 500
    }
    0xedd2bd52 = CharacterRecord {
        mCharacterName: string = "Turret"
        mFallbackCharacterName: string = "SRUAP_Turret"
        targetLaserEffects: pointer = TargetLaserComponentEffects {
            beamEffectDefinition: embed = SkinCharacterDataProperties_CharacterIdleEffect {
                effectKey: hash = 0xb6e0e814
                boneName: string = "joint2"
            }
            towerTargetingEffectDefinition: embed = SkinCharacterDataProperties_CharacterIdleEffect {
                effectName: string = "Yikes-Tower.troy"
                boneName: string = "joint2"
            }
            champTargetingEffectDefinition: embed = SkinCharacterDataProperties_CharacterIdleEffect {
                effectName: string = "yikes-champ.troy"
                boneName: string = "C_Buffbone_Glb_Head_Loc"
            }
        }
        DisabledTargetLaserEffects: pointer = TargetLaserComponentEffects {
            beamEffectDefinition: embed = SkinCharacterDataProperties_CharacterIdleEffect {
                effectKey: hash = "LaserSight_Beam_Disabled"
                boneName: string = "joint2"
            }
            towerTargetingEffectDefinition: embed = SkinCharacterDataProperties_CharacterIdleEffect {
                effectName: string = "Yikes-Tower.troy"
                boneName: string = "joint2"
            }
            champTargetingEffectDefinition: embed = SkinCharacterDataProperties_CharacterIdleEffect {
                effectName: string = "yikes-champ.troy"
                boneName: string = "C_Buffbone_Glb_Head_Loc"
            }
        }
        baseHP: f32 = 3000
        baseStaticHPRegen: f32 = 0
        healthBarHeight: f32 = 485
        healthBarFullParallax: bool = true
        primaryAbilityResource: embed = AbilityResourceSlotInfo {
            arType: u8 = 7
            arBase: f32 = 3
            arBaseStaticRegen: f32 = 0
            arIncrements: f32 = 1
            arMaxSegments: i32 = 3
            arHasRegenText: bool = false
            0xa9d3a87c: bool = true
        }
        baseDamage: f32 = 165
        baseArmor: f32 = 70
        baseSpellBlock: f32 = 70
        baseMoveSpeed: f32 = 0
        attackRange: f32 = 750
        attackSpeed: f32 = 0.833000004
        attackSpeedRatio: f32 = 0.833000004
        attackSpeedPerLevel: f32 = 2.125
        basicAttack: embed = AttackSlotData {
            mAttackDelayCastOffsetPercent: option[f32] = {
                -0.160999998
            }
            mAttackProbability: option[f32] = {
                0
            }
            mAttackName: option[string] = {
                "TurretBasicAttack"
            }
        }
        extraAttacks: list[embed] = {
            AttackSlotData {
                mAttackProbability: option[f32] = {
                    0
                }
                mAttackName: option[string] = {
                    "TurretBasicAttack2"
                }
            }
            AttackSlotData {
                mAttackProbability: option[f32] = {
                    0
                }
                mAttackName: option[string] = {
                    "TurretBasicAttack3"
                }
            }
            AttackSlotData {
                mAttackProbability: option[f32] = {
                    0
                }
                mAttackName: option[string] = {
                    "TurretBasicAttack4"
                }
            }
        }
        expGivenOnDeath: f32 = 0
        goldGivenOnDeath: f32 = 0
        localGoldSplitWithLastHitter: bool = true
        globalGoldGivenOnDeath: f32 = 50
        name: string = "game_character_displayname_TurretNexus"
        hitFxScale: f32 = 0.5
        selectionHeight: f32 = 200
        selectionRadius: f32 = 130
        pathfindingCollisionRadius: f32 = 125
        overrideGameplayCollisionRadius: option[f32] = {
            88.4000015
        }
        unitTagsString: string = "Structure | Structure_Turret | Structure_Turret_Nexus"
        characterToolData: embed = characterToolData {
            mapAIPresence: map[u32,embed] = {
                0 = ToolAiPresence {}
                1 = ToolAiPresence {}
                2 = ToolAiPresence {}
            }
            description: string = "game_character_description_NexusTurret"
        }
        mClientSideItemInventory: list[hash] = {
            "Items/1500"
            "Items/1506"
            "Items/1503"
            "Items/1507"
        }
        occludedUnitSelectableDistance: f32 = 500
    }
    0xf3b4a818 = CharacterRecord {
        mCharacterName: string = "Turret"
        mFallbackCharacterName: string = "SRUAP_Turret"
        targetLaserEffects: pointer = TargetLaserComponentEffects {
            beamEffectDefinition: embed = SkinCharacterDataProperties_CharacterIdleEffect {
                effectKey: hash = 0xb6e0e814
                boneName: string = "joint2"
            }
            towerTargetingEffectDefinition: embed = SkinCharacterDataProperties_CharacterIdleEffect {
                effectName: string = "Yikes-Tower.troy"
                boneName: string = "joint2"
            }
            champTargetingEffectDefinition: embed = SkinCharacterDataProperties_CharacterIdleEffect {
                effectName: string = "yikes-champ.troy"
                boneName: string = "C_Buffbone_Glb_Head_Loc"
            }
        }
        DisabledTargetLaserEffects: pointer = TargetLaserComponentEffects {
            beamEffectDefinition: embed = SkinCharacterDataProperties_CharacterIdleEffect {
                effectKey: hash = "LaserSight_Beam_Disabled"
                boneName: string = "joint2"
            }
            towerTargetingEffectDefinition: embed = SkinCharacterDataProperties_CharacterIdleEffect {
                effectName: string = "Yikes-Tower.troy"
                boneName: string = "joint2"
            }
            champTargetingEffectDefinition: embed = SkinCharacterDataProperties_CharacterIdleEffect {
                effectName: string = "yikes-champ.troy"
                boneName: string = "C_Buffbone_Glb_Head_Loc"
            }
        }
        baseHP: f32 = 3000
        baseStaticHPRegen: f32 = 0
        healthBarHeight: f32 = 485
        healthBarFullParallax: bool = true
        primaryAbilityResource: embed = AbilityResourceSlotInfo {
            arType: u8 = 7
            arBase: f32 = 3
            arBaseStaticRegen: f32 = 0
            arIncrements: f32 = 1
            arMaxSegments: i32 = 3
            arHasRegenText: bool = false
            0xa9d3a87c: bool = true
        }
        baseDamage: f32 = 165
        baseArmor: f32 = 50
        baseSpellBlock: f32 = 50
        baseMoveSpeed: f32 = 0
        attackRange: f32 = 750
        attackSpeed: f32 = 0.833000004
        attackSpeedRatio: f32 = 0.833000004
        attackSpeedPerLevel: f32 = 2.125
        basicAttack: embed = AttackSlotData {
            mAttackDelayCastOffsetPercent: option[f32] = {
                -0.160999998
            }
            mAttackProbability: option[f32] = {
                0
            }
            mAttackName: option[string] = {
                "TurretBasicAttack"
            }
        }
        extraAttacks: list[embed] = {
            AttackSlotData {
                mAttackProbability: option[f32] = {
                    0
                }
                mAttackName: option[string] = {
                    "TurretBasicAttack2"
                }
            }
            AttackSlotData {
                mAttackProbability: option[f32] = {
                    0
                }
                mAttackName: option[string] = {
                    "TurretBasicAttack3"
                }
            }
            AttackSlotData {
                mAttackProbability: option[f32] = {
                    0
                }
                mAttackName: option[string] = {
                    "TurretBasicAttack4"
                }
            }
        }
        expGivenOnDeath: f32 = 0
        goldGivenOnDeath: f32 = 0
        localGoldSplitWithLastHitter: bool = true
        globalGoldGivenOnDeath: f32 = 50
        name: string = "game_character_displayname_TurretNexus"
        hitFxScale: f32 = 0.5
        selectionHeight: f32 = 200
        selectionRadius: f32 = 130
        pathfindingCollisionRadius: f32 = 125
        overrideGameplayCollisionRadius: option[f32] = {
            88.4000015
        }
        unitTagsString: string = "Structure | Structure_Turret | Structure_Turret_Nexus"
        characterToolData: embed = characterToolData {
            mapAIPresence: map[u32,embed] = {
                0 = ToolAiPresence {}
                1 = ToolAiPresence {}
                2 = ToolAiPresence {}
            }
            description: string = "game_character_description_NexusTurret"
        }
        mClientSideItemInventory: list[hash] = {
            "Items/1500"
            "Items/1506"
            "Items/1503"
            0x51d3d599
        }
        occludedUnitSelectableDistance: f32 = 500
    }
    0xf5d2fa50 = CharacterRecord {
        mCharacterName: string = "Turret"
        mFallbackCharacterName: string = "HA_Turret"
        targetLaserEffects: pointer = TargetLaserComponentEffects {
            beamEffectDefinition: embed = SkinCharacterDataProperties_CharacterIdleEffect {
                effectKey: hash = 0xb6e0e814
                boneName: string = "joint2"
            }
            towerTargetingEffectDefinition: embed = SkinCharacterDataProperties_CharacterIdleEffect {
                effectName: string = "Yikes-Tower.troy"
                boneName: string = "joint2"
            }
            champTargetingEffectDefinition: embed = SkinCharacterDataProperties_CharacterIdleEffect {
                effectName: string = "yikes-champ.troy"
                boneName: string = "C_Buffbone_Glb_Head_Loc"
            }
        }
        DisabledTargetLaserEffects: pointer = TargetLaserComponentEffects {
            beamEffectDefinition: embed = SkinCharacterDataProperties_CharacterIdleEffect {
                effectKey: hash = "LaserSight_Beam_Disabled"
                boneName: string = "joint2"
            }
            towerTargetingEffectDefinition: embed = SkinCharacterDataProperties_CharacterIdleEffect {
                effectName: string = "Yikes-Tower.troy"
                boneName: string = "joint2"
            }
            champTargetingEffectDefinition: embed = SkinCharacterDataProperties_CharacterIdleEffect {
                effectName: string = "yikes-champ.troy"
                boneName: string = "C_Buffbone_Glb_Head_Loc"
            }
        }
        baseHP: f32 = 1800
        baseStaticHPRegen: f32 = 0
        healthBarHeight: f32 = 625
        healthBarFullParallax: bool = true
        primaryAbilityResource: embed = AbilityResourceSlotInfo {
            arType: u8 = 7
            arBase: f32 = 3
            arBaseStaticRegen: f32 = 0
            arIncrements: f32 = 1
            arMaxSegments: i32 = 3
            arHasRegenText: bool = false
            0xa9d3a87c: bool = true
        }
        baseDamage: f32 = 195
        baseArmor: f32 = 60
        baseSpellBlock: f32 = 60
        baseMoveSpeed: f32 = 0
        attackRange: f32 = 750
        attackSpeed: f32 = 0.833000004
        attackSpeedRatio: f32 = 0.833000004
        attackSpeedPerLevel: f32 = 2.125
        basicAttack: embed = AttackSlotData {
            mAttackDelayCastOffsetPercent: option[f32] = {
                -0.160999998
            }
            mAttackProbability: option[f32] = {
                0
            }
            mAttackName: option[string] = {
                "TurretBasicAttack"
            }
        }
        extraAttacks: list[embed] = {
            AttackSlotData {
                mAttackProbability: option[f32] = {
                    0
                }
                mAttackName: option[string] = {
                    "TurretBasicAttack2"
                }
            }
            AttackSlotData {
                mAttackProbability: option[f32] = {
                    0
                }
                mAttackName: option[string] = {
                    "TurretBasicAttack3"
                }
            }
            AttackSlotData {
                mAttackProbability: option[f32] = {
                    0
                }
                mAttackName: option[string] = {
                    "TurretBasicAttack4"
                }
            }
        }
        expGivenOnDeath: f32 = 0
        goldGivenOnDeath: f32 = 0
        localGoldSplitWithLastHitter: bool = true
        globalGoldGivenOnDeath: f32 = 150
        globalExpGivenOnDeath: f32 = 120
        name: string = "game_character_displayname_TurretNexus"
        hitFxScale: f32 = 0.5
        selectionHeight: f32 = 200
        selectionRadius: f32 = 130
        pathfindingCollisionRadius: f32 = 125
        overrideGameplayCollisionRadius: option[f32] = {
            88.4000015
        }
        unitTagsString: string = "Structure | Structure_Turret | Structure_Turret_Nexus"
        characterToolData: embed = characterToolData {
            mapAIPresence: map[u32,embed] = {
                0 = ToolAiPresence {}
                1 = ToolAiPresence {}
                2 = ToolAiPresence {}
            }
            description: string = "game_character_description_NexusTurret"
        }
        mClientSideItemInventory: list[hash] = {
            "Items/1500"
            "Items/1502"
            "Items/1503"
            "Items/1520"
            "Items/1522"
        }
        occludedUnitSelectableDistance: f32 = 700
    }
    "Characters/Turret/Spells/TurretBasicAttack" = SpellObject {
        mScriptName: string = "TurretBasicAttack"
        mSpell: pointer = SpellDataResource {
            mAffectsTypeFlags: u32 = 5375
            mAlternateName: string = "OrderTurretNormalBasicAttack"
            mAnimationName: string = "attack1"
            bHaveHitEffect: bool = true
            castConeDistance: f32 = 100
            mMissileSpec: pointer = MissileSpecification {
                movementComponent: pointer = FixedSpeedMovement {
                    mTargetHeightAugment: f32 = 100
                    mOffsetInitialTargetHeight: f32 = 100
                    mStartBoneName: string = "joint2"
                    mSpeed: f32 = 1200
                }
                verticalFacing: pointer = VeritcalFacingMatchVelocity {}
                behaviors: list[pointer] = {
                    CastOnMovementComplete {}
                    DestroyOnMovementComplete {}
                }
            }
            mCastType: u32 = 1
            castFrame: f32 = 4.94999981
            missileSpeed: f32 = 1200
            mMissileEffectKey: hash = 0xec90fddd
            mMissileEffectPlayerKey: hash = 0xf118ff29
            mHitEffectKey: hash = 0x91922da4
            bHaveHitBone: bool = true
            mHitBoneName: string = "C_Buffbone_Glb_Chest_Loc"
            mClientData: embed = SpellDataResourceClient {
                mTargeterDefinitions: list[pointer] = {
                    TargeterDefinitionRange {
                        useCasterBoundingBox: option[bool] = {
                            false
                        }
                    }
                }
            }
        }
    }
    0x712d04c6 = SpellObject {
        mScriptName: string = "TurretBasicAttack3"
        mSpell: pointer = SpellDataResource {
            mAffectsTypeFlags: u32 = 5375
            mAlternateName: string = "OrderTurretNormalBasicAttack"
            mAnimationName: string = "attack1"
            bHaveHitEffect: bool = true
            castConeDistance: f32 = 100
            mMissileSpec: pointer = MissileSpecification {
                movementComponent: pointer = FixedSpeedMovement {
                    mTargetHeightAugment: f32 = 100
                    mOffsetInitialTargetHeight: f32 = 100
                    mStartBoneName: string = "joint2"
                    mSpeed: f32 = 1200
                }
                verticalFacing: pointer = VeritcalFacingMatchVelocity {}
                behaviors: list[pointer] = {
                    CastOnMovementComplete {}
                    DestroyOnMovementComplete {}
                }
            }
            mCastType: u32 = 1
            castFrame: f32 = 4.94999981
            missileSpeed: f32 = 1200
            mMissileEffectKey: hash = 0x246d001f
            mMissileEffectPlayerKey: hash = 0x246d001f
            mHitEffectKey: hash = 0x92922f37
            bHaveHitBone: bool = true
            mHitBoneName: string = "C_Buffbone_Glb_Chest_Loc"
            mClientData: embed = SpellDataResourceClient {
                mTargeterDefinitions: list[pointer] = {
                    TargeterDefinitionRange {
                        useCasterBoundingBox: option[bool] = {
                            false
                        }
                    }
                }
            }
        }
    }
    0x722d0659 = SpellObject {
        mScriptName: string = "TurretBasicAttack2"
        mSpell: pointer = SpellDataResource {
            mAffectsTypeFlags: u32 = 5375
            mAlternateName: string = "OrderTurretNormalBasicAttack"
            mAnimationName: string = "attack1"
            bHaveHitEffect: bool = true
            castConeDistance: f32 = 100
            mMissileSpec: pointer = MissileSpecification {
                movementComponent: pointer = FixedSpeedMovement {
                    mTargetHeightAugment: f32 = 100
                    mOffsetInitialTargetHeight: f32 = 100
                    mStartBoneName: string = "joint2"
                    mSpeed: f32 = 1200
                }
                verticalFacing: pointer = VeritcalFacingMatchVelocity {}
                behaviors: list[pointer] = {
                    CastOnMovementComplete {}
                    DestroyOnMovementComplete {}
                }
            }
            mCastType: u32 = 1
            castFrame: f32 = 4.94999981
            missileSpeed: f32 = 1200
            mMissileEffectKey: hash = 0x236cfe8c
            mMissileEffectPlayerKey: hash = 0x236cfe8c
            mHitEffectKey: hash = 0x91922da4
            bHaveHitBone: bool = true
            mHitBoneName: string = "C_Buffbone_Glb_Chest_Loc"
            mClientData: embed = SpellDataResourceClient {
                mTargeterDefinitions: list[pointer] = {
                    TargeterDefinitionRange {
                        useCasterBoundingBox: option[bool] = {
                            false
                        }
                    }
                }
            }
        }
    }
    0x742d097f = SpellObject {
        mScriptName: string = "TurretBasicAttack4"
        mSpell: pointer = SpellDataResource {
            mAffectsTypeFlags: u32 = 5375
            mAlternateName: string = "OrderTurretNormalBasicAttack"
            mAnimationName: string = "attack1"
            bHaveHitEffect: bool = true
            castConeDistance: f32 = 100
            mMissileSpec: pointer = MissileSpecification {
                movementComponent: pointer = FixedSpeedMovement {
                    mTargetHeightAugment: f32 = 100
                    mOffsetInitialTargetHeight: f32 = 100
                    mStartBoneName: string = "joint2"
                    mSpeed: f32 = 1200
                }
                verticalFacing: pointer = VeritcalFacingMatchVelocity {}
                behaviors: list[pointer] = {
                    CastOnMovementComplete {}
                    DestroyOnMovementComplete {}
                }
            }
            mCastType: u32 = 1
            castFrame: f32 = 4.94999981
            missileSpeed: f32 = 1200
            mMissileEffectKey: hash = 0x216cfb66
            mMissileEffectPlayerKey: hash = 0x216cfb66
            mHitEffectKey: hash = 0x8f922a7e
            bHaveHitBone: bool = true
            mHitBoneName: string = "C_Buffbone_Glb_Chest_Loc"
            mClientData: embed = SpellDataResourceClient {
                mTargeterDefinitions: list[pointer] = {
                    TargeterDefinitionRange {
                        useCasterBoundingBox: option[bool] = {
                            false
                        }
                    }
                }
            }
        }
    }
    0xf1119862 = SpellObject {
        mScriptName: string = "NexusTurretBasicAttack"
        mSpell: pointer = SpellDataResource {
            mAffectsTypeFlags: u32 = 5375
            mAlternateName: string = "OrderTurretNormalBasicAttack"
            mAnimationName: string = "attack1"
            bHaveHitEffect: bool = true
            castConeDistance: f32 = 100
            mMissileSpec: pointer = MissileSpecification {
                movementComponent: pointer = FixedSpeedMovement {
                    mTargetHeightAugment: f32 = 100
                    mOffsetInitialTargetHeight: f32 = 100
                    mStartBoneName: string = "joint2"
                    mSpeed: f32 = 1200
                }
                verticalFacing: pointer = VeritcalFacingMatchVelocity {}
                behaviors: list[pointer] = {
                    CastOnMovementComplete {}
                    DestroyOnMovementComplete {}
                }
            }
            mCastType: u32 = 1
            castFrame: f32 = 4.94999981
            missileSpeed: f32 = 1200
            mMissileEffectKey: hash = 0xec90fddd
            mMissileEffectPlayerKey: hash = 0xf118ff29
            mHitEffectKey: hash = 0x9ef2bde5
            bHaveHitBone: bool = true
            mHitBoneName: string = "C_Buffbone_Glb_Chest_Loc"
            mClientData: embed = SpellDataResourceClient {
                mTargeterDefinitions: list[pointer] = {
                    TargeterDefinitionRange {
                        useCasterBoundingBox: option[bool] = {
                            false
                        }
                    }
                }
            }
        }
    }
    "Characters/Turret/Skins/Meta" = SkinCharacterMetaDataProperties {
        relativeColorSwapTable: list[i32] = {
            1
            0
            3
            2
            5
            4
            7
            6
            9
            8
            11
            10
            13
            12
            15
            14
            17
            16
            19
            18
            21
            20
            23
            22
            25
            24
            27
            26
            29
            28
            31
            30
            33
            32
            35
            34
            37
            36
            39
            38
            41
            40
        }
    }
}
