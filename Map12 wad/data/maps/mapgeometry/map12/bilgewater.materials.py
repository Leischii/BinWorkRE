#PROP_text
type: string = "PROP"
version: u32 = 3
linked: list[string] = {}
entries: map[hash,embed] = {
    "Maps/KitPieces/HA_Bilgewater/Materials/BW_Perif_Cliff_A22_inst" = StaticMaterialDef {
        name: string = "Maps/KitPieces/HA_Bilgewater/Materials/BW_Perif_Cliff_A22_inst"
        type: u32 = 0
        samplerValues: list2[embed] = {
            StaticMaterialShaderSamplerDef {
                textureName: string = "DiffuseTexture"
                texturePath: string = "ASSETS/Maps/KitPieces/HA_Bilgewater/textures/bw_perif_cliff_a.dds"
                addressW: u32 = 1
            }
        }
        paramValues: list2[embed] = {
            StaticMaterialShaderParamDef {
                name: string = "TintColor"
                value: vec4 = { 0.5, 0.5, 0.5, 1 }
            }
            StaticMaterialShaderParamDef {
                name: string = "PitchFactor"
            }
        }
        techniques: list[embed] = {
            StaticMaterialTechniqueDef {
                name: string = "normal"
                passes: list[embed] = {
                    StaticMaterialPassDef {
                        shader: link = "Shaders/StaticMesh/DefaultEnv_Flat"
                    }
                }
            }
        }
    }
    "Maps/KitPieces/HA_Bilgewater/Materials/mod_house_tall_b14_inst" = StaticMaterialDef {
        name: string = "Maps/KitPieces/HA_Bilgewater/Materials/mod_house_tall_b14_inst"
        type: u32 = 0
        samplerValues: list2[embed] = {
            StaticMaterialShaderSamplerDef {
                textureName: string = "DiffuseTexture"
                texturePath: string = "ASSETS/Maps/KitPieces/HA_Bilgewater/textures/house_tall_b.dds"
                addressW: u32 = 1
            }
        }
        paramValues: list2[embed] = {
            StaticMaterialShaderParamDef {
                name: string = "TintColor"
                value: vec4 = { 0.5, 0.5, 0.5, 1 }
            }
            StaticMaterialShaderParamDef {
                name: string = "PitchFactor"
            }
        }
        techniques: list[embed] = {
            StaticMaterialTechniqueDef {
                name: string = "normal"
                passes: list[embed] = {
                    StaticMaterialPassDef {
                        shader: link = "Shaders/StaticMesh/DefaultEnv_Flat"
                    }
                }
            }
        }
    }
    "Maps/KitPieces/HA_Bilgewater/Materials/lambert175301_inst" = StaticMaterialDef {
        name: string = "Maps/KitPieces/HA_Bilgewater/Materials/lambert175301_inst"
        type: u32 = 0
        samplerValues: list2[embed] = {
            StaticMaterialShaderSamplerDef {
                textureName: string = "DiffuseTexture"
                texturePath: string = "ASSETS/Maps/KitPieces/HA_Bilgewater/textures/bw_struc_chimney_01.dds"
                addressW: u32 = 1
            }
        }
        paramValues: list2[embed] = {
            StaticMaterialShaderParamDef {
                name: string = "TintColor"
                value: vec4 = { 0.5, 0.5, 0.5, 1 }
            }
            StaticMaterialShaderParamDef {
                name: string = "PitchFactor"
            }
        }
        techniques: list[embed] = {
            StaticMaterialTechniqueDef {
                name: string = "normal"
                passes: list[embed] = {
                    StaticMaterialPassDef {
                        shader: link = "Shaders/StaticMesh/DefaultEnv_Flat"
                    }
                }
            }
        }
    }
    "Maps/KitPieces/HA_Bilgewater/Materials/wood_addons135_inst" = StaticMaterialDef {
        name: string = "Maps/KitPieces/HA_Bilgewater/Materials/wood_addons135_inst"
        type: u32 = 0
        samplerValues: list2[embed] = {
            StaticMaterialShaderSamplerDef {
                textureName: string = "DiffuseTexture"
                texturePath: string = "ASSETS/Maps/KitPieces/HA_Bilgewater/textures/bw_wood_scaffolding_modular.dds"
                addressW: u32 = 1
            }
        }
        paramValues: list2[embed] = {
            StaticMaterialShaderParamDef {
                name: string = "TintColor"
                value: vec4 = { 0.5, 0.5, 0.5, 1 }
            }
            StaticMaterialShaderParamDef {
                name: string = "PitchFactor"
            }
        }
        techniques: list[embed] = {
            StaticMaterialTechniqueDef {
                name: string = "normal"
                passes: list[embed] = {
                    StaticMaterialPassDef {
                        shader: link = "Shaders/StaticMesh/DefaultEnv_Flat"
                    }
                }
            }
        }
    }
    "Maps/KitPieces/HA_Bilgewater/Materials/BW_Tarps_021_inst" = StaticMaterialDef {
        name: string = "Maps/KitPieces/HA_Bilgewater/Materials/BW_Tarps_021_inst"
        type: u32 = 0
        samplerValues: list2[embed] = {
            StaticMaterialShaderSamplerDef {
                textureName: string = "DiffuseTexture"
                texturePath: string = "ASSETS/Maps/KitPieces/HA_Bilgewater/textures/bw_tarps_01.dds"
                addressW: u32 = 1
            }
        }
        paramValues: list2[embed] = {
            StaticMaterialShaderParamDef {
                name: string = "TintColor"
                value: vec4 = { 0.5, 0.5, 0.5, 1 }
            }
            StaticMaterialShaderParamDef {
                name: string = "PitchFactor"
            }
        }
        techniques: list[embed] = {
            StaticMaterialTechniqueDef {
                name: string = "normal"
                passes: list[embed] = {
                    StaticMaterialPassDef {
                        shader: link = "Shaders/StaticMesh/DefaultEnv_Flat"
                    }
                }
            }
        }
    }
    "Maps/KitPieces/HA_Bilgewater/Materials/BW_N_Shop_Barrier_011_inst" = StaticMaterialDef {
        name: string = "Maps/KitPieces/HA_Bilgewater/Materials/BW_N_Shop_Barrier_011_inst"
        type: u32 = 0
        samplerValues: list2[embed] = {
            StaticMaterialShaderSamplerDef {
                textureName: string = "DiffuseTexture"
                texturePath: string = "ASSETS/Maps/KitPieces/HA_Bilgewater/textures/bw_n_shop_barrier_01.dds"
                addressW: u32 = 1
            }
        }
        paramValues: list2[embed] = {
            StaticMaterialShaderParamDef {
                name: string = "AlphaTestValue"
                value: vec4 = { 0.899999976, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "TintColor"
                value: vec4 = { 0.5, 0.5, 0.5, 1 }
            }
        }
        techniques: list[embed] = {
            StaticMaterialTechniqueDef {
                name: string = "normal"
                passes: list[embed] = {
                    StaticMaterialPassDef {
                        shader: link = "Shaders/StaticMesh/DefaultEnv_Flat_AlphaTest"
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    }
                }
            }
        }
    }
    "Maps/KitPieces/HA_Bilgewater/Materials/props_coffin35_inst" = StaticMaterialDef {
        name: string = "Maps/KitPieces/HA_Bilgewater/Materials/props_coffin35_inst"
        type: u32 = 0
        samplerValues: list2[embed] = {
            StaticMaterialShaderSamplerDef {
                textureName: string = "DiffuseTexture"
                texturePath: string = "ASSETS/Maps/KitPieces/HA_Bilgewater/textures/props_coffin_a.dds"
                addressW: u32 = 1
            }
        }
        paramValues: list2[embed] = {
            StaticMaterialShaderParamDef {
                name: string = "TintColor"
                value: vec4 = { 0.5, 0.5, 0.5, 1 }
            }
            StaticMaterialShaderParamDef {
                name: string = "PitchFactor"
            }
        }
        techniques: list[embed] = {
            StaticMaterialTechniqueDef {
                name: string = "normal"
                passes: list[embed] = {
                    StaticMaterialPassDef {
                        shader: link = "Shaders/StaticMesh/DefaultEnv_Flat"
                    }
                }
            }
        }
    }
    "Maps/KitPieces/HA_Bilgewater/Materials/BW_OLD_bridge_side_elements_Wood_Posts19_inst" = StaticMaterialDef {
        name: string = "Maps/KitPieces/HA_Bilgewater/Materials/BW_OLD_bridge_side_elements_Wood_Posts19_inst"
        type: u32 = 0
        samplerValues: list2[embed] = {
            StaticMaterialShaderSamplerDef {
                textureName: string = "DiffuseTexture"
                texturePath: string = "ASSETS/Maps/KitPieces/HA_Bilgewater/textures/bw_wood_posts_01.dds"
                addressW: u32 = 1
            }
        }
        paramValues: list2[embed] = {
            StaticMaterialShaderParamDef {
                name: string = "TintColor"
                value: vec4 = { 0.5, 0.5, 0.5, 1 }
            }
            StaticMaterialShaderParamDef {
                name: string = "PitchFactor"
            }
        }
        techniques: list[embed] = {
            StaticMaterialTechniqueDef {
                name: string = "normal"
                passes: list[embed] = {
                    StaticMaterialPassDef {
                        shader: link = "Shaders/StaticMesh/DefaultEnv_Flat"
                    }
                }
            }
        }
    }
    "Maps/KitPieces/HA_Bilgewater/Materials/lambert175206_inst" = StaticMaterialDef {
        name: string = "Maps/KitPieces/HA_Bilgewater/Materials/lambert175206_inst"
        type: u32 = 0
        samplerValues: list2[embed] = {
            StaticMaterialShaderSamplerDef {
                textureName: string = "DiffuseTexture"
                texturePath: string = "ASSETS/Maps/KitPieces/HA_Bilgewater/textures/bw_hanging_fish_01.dds"
                addressW: u32 = 1
            }
        }
        paramValues: list2[embed] = {
            StaticMaterialShaderParamDef {
                name: string = "TintColor"
                value: vec4 = { 0.5, 0.5, 0.5, 1 }
            }
            StaticMaterialShaderParamDef {
                name: string = "PitchFactor"
            }
        }
        techniques: list[embed] = {
            StaticMaterialTechniqueDef {
                name: string = "normal"
                passes: list[embed] = {
                    StaticMaterialPassDef {
                        shader: link = "Shaders/StaticMesh/DefaultEnv_Flat"
                    }
                }
            }
        }
    }
    "Maps/KitPieces/HA_Bilgewater/Materials/bridge_with_fishys_lambert_alpha38_inst" = StaticMaterialDef {
        name: string = "Maps/KitPieces/HA_Bilgewater/Materials/bridge_with_fishys_lambert_alpha38_inst"
        type: u32 = 0
        samplerValues: list2[embed] = {
            StaticMaterialShaderSamplerDef {
                textureName: string = "DiffuseTexture"
                texturePath: string = "ASSETS/Maps/KitPieces/HA_Bilgewater/textures/nets.dds"
                addressW: u32 = 1
            }
        }
        paramValues: list2[embed] = {
            StaticMaterialShaderParamDef {
                name: string = "AlphaTestValue"
                value: vec4 = { 0.899999976, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "TintColor"
                value: vec4 = { 0.5, 0.5, 0.5, 1 }
            }
        }
        techniques: list[embed] = {
            StaticMaterialTechniqueDef {
                name: string = "normal"
                passes: list[embed] = {
                    StaticMaterialPassDef {
                        shader: link = "Shaders/StaticMesh/DefaultEnv_Flat_AlphaTest"
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    }
                }
            }
        }
    }
    "Maps/KitPieces/HA_Bilgewater/Materials/mod_house_tall_a37_inst" = StaticMaterialDef {
        name: string = "Maps/KitPieces/HA_Bilgewater/Materials/mod_house_tall_a37_inst"
        type: u32 = 0
        samplerValues: list2[embed] = {
            StaticMaterialShaderSamplerDef {
                textureName: string = "DiffuseTexture"
                texturePath: string = "ASSETS/Maps/KitPieces/HA_Bilgewater/textures/house_tall_a1.dds"
                addressW: u32 = 1
            }
        }
        paramValues: list2[embed] = {
            StaticMaterialShaderParamDef {
                name: string = "TintColor"
                value: vec4 = { 0.5, 0.5, 0.5, 1 }
            }
            StaticMaterialShaderParamDef {
                name: string = "PitchFactor"
            }
        }
        techniques: list[embed] = {
            StaticMaterialTechniqueDef {
                name: string = "normal"
                passes: list[embed] = {
                    StaticMaterialPassDef {
                        shader: link = "Shaders/StaticMesh/DefaultEnv_Flat"
                    }
                }
            }
        }
    }
    "Maps/KitPieces/HA_Bilgewater/Materials/lambert173617_inst" = StaticMaterialDef {
        name: string = "Maps/KitPieces/HA_Bilgewater/Materials/lambert173617_inst"
        type: u32 = 0
        samplerValues: list2[embed] = {
            StaticMaterialShaderSamplerDef {
                textureName: string = "DiffuseTexture"
                texturePath: string = "ASSETS/Maps/KitPieces/HA_Bilgewater/textures/bw_bridge_door_a.dds"
                addressW: u32 = 1
            }
        }
        paramValues: list2[embed] = {
            StaticMaterialShaderParamDef {
                name: string = "TintColor"
                value: vec4 = { 0.5, 0.5, 0.5, 1 }
            }
            StaticMaterialShaderParamDef {
                name: string = "PitchFactor"
            }
        }
        techniques: list[embed] = {
            StaticMaterialTechniqueDef {
                name: string = "normal"
                passes: list[embed] = {
                    StaticMaterialPassDef {
                        shader: link = "Shaders/StaticMesh/DefaultEnv_Flat"
                    }
                }
            }
        }
    }
    "Maps/KitPieces/HA_Bilgewater/Materials/bw_bridge_statue_a19_inst" = StaticMaterialDef {
        name: string = "Maps/KitPieces/HA_Bilgewater/Materials/bw_bridge_statue_a19_inst"
        type: u32 = 0
        samplerValues: list2[embed] = {
            StaticMaterialShaderSamplerDef {
                textureName: string = "DiffuseTexture"
                texturePath: string = "ASSETS/Maps/KitPieces/HA_Bilgewater/textures/bw_bridge_statue_a.dds"
                addressW: u32 = 1
            }
        }
        paramValues: list2[embed] = {
            StaticMaterialShaderParamDef {
                name: string = "TintColor"
                value: vec4 = { 0.5, 0.5, 0.5, 1 }
            }
            StaticMaterialShaderParamDef {
                name: string = "PitchFactor"
            }
        }
        techniques: list[embed] = {
            StaticMaterialTechniqueDef {
                name: string = "normal"
                passes: list[embed] = {
                    StaticMaterialPassDef {
                        shader: link = "Shaders/StaticMesh/DefaultEnv_Flat"
                    }
                }
            }
        }
    }
    "Maps/KitPieces/HA_Bilgewater/Materials/prop_banner_a_b58_inst" = StaticMaterialDef {
        name: string = "Maps/KitPieces/HA_Bilgewater/Materials/prop_banner_a_b58_inst"
        type: u32 = 0
        samplerValues: list2[embed] = {
            StaticMaterialShaderSamplerDef {
                textureName: string = "DiffuseTexture"
                texturePath: string = "ASSETS/Maps/KitPieces/HA_Bilgewater/textures/bw_prop_banner_01.dds"
                addressW: u32 = 1
            }
        }
        paramValues: list2[embed] = {
            StaticMaterialShaderParamDef {
                name: string = "AlphaTestValue"
                value: vec4 = { 0.899999976, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "TintColor"
                value: vec4 = { 0.5, 0.5, 0.5, 1 }
            }
        }
        techniques: list[embed] = {
            StaticMaterialTechniqueDef {
                name: string = "normal"
                passes: list[embed] = {
                    StaticMaterialPassDef {
                        shader: link = "Shaders/StaticMesh/DefaultEnv_Flat_AlphaTest"
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    }
                }
            }
        }
    }
    "Maps/KitPieces/HA_Bilgewater/Materials/BW_Perif_Statue_A42_inst" = StaticMaterialDef {
        name: string = "Maps/KitPieces/HA_Bilgewater/Materials/BW_Perif_Statue_A42_inst"
        type: u32 = 0
        samplerValues: list2[embed] = {
            StaticMaterialShaderSamplerDef {
                textureName: string = "DiffuseTexture"
                texturePath: string = "ASSETS/Maps/KitPieces/HA_Bilgewater/textures/bw_perif_statue_a.dds"
                addressW: u32 = 1
            }
        }
        paramValues: list2[embed] = {
            StaticMaterialShaderParamDef {
                name: string = "TintColor"
                value: vec4 = { 0.5, 0.5, 0.5, 1 }
            }
            StaticMaterialShaderParamDef {
                name: string = "PitchFactor"
            }
        }
        techniques: list[embed] = {
            StaticMaterialTechniqueDef {
                name: string = "normal"
                passes: list[embed] = {
                    StaticMaterialPassDef {
                        shader: link = "Shaders/StaticMesh/DefaultEnv_Flat"
                    }
                }
            }
        }
    }
    "Maps/KitPieces/HA_Bilgewater/Materials/lambert2_inst" = StaticMaterialDef {
        name: string = "Maps/KitPieces/HA_Bilgewater/Materials/lambert2_inst"
        type: u32 = 0
        samplerValues: list2[embed] = {
            StaticMaterialShaderSamplerDef {
                textureName: string = "DiffuseTexture"
                texturePath: string = "ASSETS/Maps/KitPieces/HA_Bilgewater/textures/BW_props_signs_01.dds"
                addressW: u32 = 1
            }
        }
        paramValues: list2[embed] = {
            StaticMaterialShaderParamDef {
                name: string = "TintColor"
                value: vec4 = { 0.5, 0.5, 0.5, 1 }
            }
            StaticMaterialShaderParamDef {
                name: string = "PitchFactor"
            }
        }
        techniques: list[embed] = {
            StaticMaterialTechniqueDef {
                name: string = "normal"
                passes: list[embed] = {
                    StaticMaterialPassDef {
                        shader: link = "Shaders/StaticMesh/DefaultEnv_Flat"
                    }
                }
            }
        }
    }
    "Maps/KitPieces/HA_Bilgewater/Materials/lambert175307_inst" = StaticMaterialDef {
        name: string = "Maps/KitPieces/HA_Bilgewater/Materials/lambert175307_inst"
        type: u32 = 0
        samplerValues: list2[embed] = {
            StaticMaterialShaderSamplerDef {
                textureName: string = "DiffuseTexture"
                texturePath: string = "ASSETS/Maps/KitPieces/HA_Bilgewater/textures/house_tall_skinny_b.dds"
                addressW: u32 = 1
            }
        }
        paramValues: list2[embed] = {
            StaticMaterialShaderParamDef {
                name: string = "TintColor"
                value: vec4 = { 0.5, 0.5, 0.5, 1 }
            }
            StaticMaterialShaderParamDef {
                name: string = "PitchFactor"
            }
        }
        techniques: list[embed] = {
            StaticMaterialTechniqueDef {
                name: string = "normal"
                passes: list[embed] = {
                    StaticMaterialPassDef {
                        shader: link = "Shaders/StaticMesh/DefaultEnv_Flat"
                    }
                }
            }
        }
    }
    "Maps/KitPieces/HA_Bilgewater/Materials/lambert175215_inst" = StaticMaterialDef {
        name: string = "Maps/KitPieces/HA_Bilgewater/Materials/lambert175215_inst"
        type: u32 = 0
        samplerValues: list2[embed] = {
            StaticMaterialShaderSamplerDef {
                textureName: string = "DiffuseTexture"
                texturePath: string = "ASSETS/Maps/KitPieces/HA_Bilgewater/textures/bw_periph_cards_01.dds"
                addressW: u32 = 1
            }
        }
        paramValues: list2[embed] = {
            StaticMaterialShaderParamDef {
                name: string = "AlphaTestValue"
                value: vec4 = { 0.899999976, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "TintColor"
                value: vec4 = { 0.5, 0.5, 0.5, 1 }
            }
        }
        techniques: list[embed] = {
            StaticMaterialTechniqueDef {
                name: string = "normal"
                passes: list[embed] = {
                    StaticMaterialPassDef {
                        shader: link = "Shaders/StaticMesh/DefaultEnv_Flat_AlphaTest"
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    }
                }
            }
        }
    }
    "Maps/KitPieces/HA_Bilgewater/Materials/lambert173833_inst" = StaticMaterialDef {
        name: string = "Maps/KitPieces/HA_Bilgewater/Materials/lambert173833_inst"
        type: u32 = 0
        samplerValues: list2[embed] = {
            StaticMaterialShaderSamplerDef {
                textureName: string = "DiffuseTexture"
                texturePath: string = "ASSETS/Maps/KitPieces/HA_Bilgewater/textures/bw_bridge_shipside_destroyed_a.dds"
                addressW: u32 = 1
            }
        }
        paramValues: list2[embed] = {
            StaticMaterialShaderParamDef {
                name: string = "TintColor"
                value: vec4 = { 0.5, 0.5, 0.5, 1 }
            }
            StaticMaterialShaderParamDef {
                name: string = "PitchFactor"
            }
        }
        techniques: list[embed] = {
            StaticMaterialTechniqueDef {
                name: string = "normal"
                passes: list[embed] = {
                    StaticMaterialPassDef {
                        shader: link = "Shaders/StaticMesh/DefaultEnv_Flat"
                    }
                }
            }
        }
    }
    "Maps/KitPieces/HA_Bilgewater/Materials/LM_Bridgecutaway14_inst" = StaticMaterialDef {
        name: string = "Maps/KitPieces/HA_Bilgewater/Materials/LM_Bridgecutaway14_inst"
        type: u32 = 0
        samplerValues: list2[embed] = {
            StaticMaterialShaderSamplerDef {
                textureName: string = "DiffuseTexture"
                texturePath: string = "ASSETS/Maps/KitPieces/HA_Bilgewater/textures/bw_bridge_cutout_b.dds"
                addressW: u32 = 1
            }
        }
        paramValues: list2[embed] = {
            StaticMaterialShaderParamDef {
                name: string = "TintColor"
                value: vec4 = { 0.5, 0.5, 0.5, 1 }
            }
            StaticMaterialShaderParamDef {
                name: string = "PitchFactor"
            }
        }
        techniques: list[embed] = {
            StaticMaterialTechniqueDef {
                name: string = "normal"
                passes: list[embed] = {
                    StaticMaterialPassDef {
                        shader: link = "Shaders/StaticMesh/DefaultEnv_Flat"
                    }
                }
            }
        }
    }
    "Maps/KitPieces/HA_Bilgewater/Materials/S_Base_Laser_Turret13_inst" = StaticMaterialDef {
        name: string = "Maps/KitPieces/HA_Bilgewater/Materials/S_Base_Laser_Turret13_inst"
        type: u32 = 0
        samplerValues: list2[embed] = {
            StaticMaterialShaderSamplerDef {
                textureName: string = "DiffuseTexture"
                texturePath: string = "ASSETS/Maps/KitPieces/HA_Bilgewater/textures/bw_s_base_laser_turret.dds"
                addressW: u32 = 1
            }
        }
        paramValues: list2[embed] = {
            StaticMaterialShaderParamDef {
                name: string = "TintColor"
                value: vec4 = { 0.5, 0.5, 0.5, 1 }
            }
            StaticMaterialShaderParamDef {
                name: string = "PitchFactor"
            }
        }
        techniques: list[embed] = {
            StaticMaterialTechniqueDef {
                name: string = "normal"
                passes: list[embed] = {
                    StaticMaterialPassDef {
                        shader: link = "Shaders/StaticMesh/DefaultEnv_Flat"
                    }
                }
            }
        }
    }
    "Maps/KitPieces/HA_Bilgewater/Materials/block_and_tackle_flat4_inst" = StaticMaterialDef {
        name: string = "Maps/KitPieces/HA_Bilgewater/Materials/block_and_tackle_flat4_inst"
        type: u32 = 0
        samplerValues: list2[embed] = {
            StaticMaterialShaderSamplerDef {
                textureName: string = "DiffuseTexture"
                texturePath: string = "ASSETS/Maps/KitPieces/HA_Bilgewater/textures/block_and_tackle_flat.dds"
                addressW: u32 = 1
            }
        }
        paramValues: list2[embed] = {
            StaticMaterialShaderParamDef {
                name: string = "TintColor"
                value: vec4 = { 0.5, 0.5, 0.5, 1 }
            }
            StaticMaterialShaderParamDef {
                name: string = "PitchFactor"
            }
        }
        techniques: list[embed] = {
            StaticMaterialTechniqueDef {
                name: string = "normal"
                passes: list[embed] = {
                    StaticMaterialPassDef {
                        shader: link = "Shaders/StaticMesh/DefaultEnv_Flat"
                    }
                }
            }
        }
    }
    "Maps/KitPieces/HA_Bilgewater/Materials/lambert175057_inst" = StaticMaterialDef {
        name: string = "Maps/KitPieces/HA_Bilgewater/Materials/lambert175057_inst"
        type: u32 = 0
        samplerValues: list2[embed] = {
            StaticMaterialShaderSamplerDef {
                textureName: string = "DiffuseTexture"
                texturePath: string = "ASSETS/Maps/KitPieces/HA_Bilgewater/textures/bw_props_lantern_01.dds"
                addressW: u32 = 1
            }
        }
        paramValues: list2[embed] = {
            StaticMaterialShaderParamDef {
                name: string = "TintColor"
                value: vec4 = { 0.5, 0.5, 0.5, 1 }
            }
            StaticMaterialShaderParamDef {
                name: string = "PitchFactor"
            }
        }
        techniques: list[embed] = {
            StaticMaterialTechniqueDef {
                name: string = "normal"
                passes: list[embed] = {
                    StaticMaterialPassDef {
                        shader: link = "Shaders/StaticMesh/DefaultEnv_Flat"
                    }
                }
            }
        }
    }
    "Maps/KitPieces/HA_Bilgewater/Materials/lambert173613_inst" = StaticMaterialDef {
        name: string = "Maps/KitPieces/HA_Bilgewater/Materials/lambert173613_inst"
        type: u32 = 0
        samplerValues: list2[embed] = {
            StaticMaterialShaderSamplerDef {
                textureName: string = "DiffuseTexture"
                texturePath: string = "ASSETS/Maps/KitPieces/HA_Bilgewater/textures/bw_bridge_statue_base_a.dds"
                addressW: u32 = 1
            }
        }
        paramValues: list2[embed] = {
            StaticMaterialShaderParamDef {
                name: string = "TintColor"
                value: vec4 = { 0.5, 0.5, 0.5, 1 }
            }
            StaticMaterialShaderParamDef {
                name: string = "PitchFactor"
            }
        }
        techniques: list[embed] = {
            StaticMaterialTechniqueDef {
                name: string = "normal"
                passes: list[embed] = {
                    StaticMaterialPassDef {
                        shader: link = "Shaders/StaticMesh/DefaultEnv_Flat"
                    }
                }
            }
        }
    }
    "Maps/KitPieces/HA_Bilgewater/Materials/LM_ground_base_south_B1_inst" = StaticMaterialDef {
        name: string = "Maps/KitPieces/HA_Bilgewater/Materials/LM_ground_base_south_B1_inst"
        type: u32 = 0
        samplerValues: list2[embed] = {
            StaticMaterialShaderSamplerDef {
                textureName: string = "DiffuseTexture"
                texturePath: string = "ASSETS/Maps/KitPieces/HA_Bilgewater/textures/BW_ground_base_south_b.dds"
                addressW: u32 = 1
            }
        }
        paramValues: list2[embed] = {
            StaticMaterialShaderParamDef {
                name: string = "TintColor"
                value: vec4 = { 0.5, 0.5, 0.5, 1 }
            }
            StaticMaterialShaderParamDef {
                name: string = "PitchFactor"
            }
        }
        techniques: list[embed] = {
            StaticMaterialTechniqueDef {
                name: string = "normal"
                passes: list[embed] = {
                    StaticMaterialPassDef {
                        shader: link = "Shaders/StaticMesh/DefaultEnv_Flat"
                    }
                }
            }
        }
    }
    "Maps/KitPieces/HA_Bilgewater/Materials/LM_Ground_Lane_A38_inst" = StaticMaterialDef {
        name: string = "Maps/KitPieces/HA_Bilgewater/Materials/LM_Ground_Lane_A38_inst"
        type: u32 = 0
        samplerValues: list2[embed] = {
            StaticMaterialShaderSamplerDef {
                textureName: string = "DiffuseTexture"
                texturePath: string = "ASSETS/Maps/KitPieces/HA_Bilgewater/textures/bw_ground_lane_a.dds"
                addressW: u32 = 1
            }
        }
        paramValues: list2[embed] = {
            StaticMaterialShaderParamDef {
                name: string = "TintColor"
                value: vec4 = { 0.5, 0.5, 0.5, 1 }
            }
            StaticMaterialShaderParamDef {
                name: string = "PitchFactor"
            }
        }
        techniques: list[embed] = {
            StaticMaterialTechniqueDef {
                name: string = "normal"
                passes: list[embed] = {
                    StaticMaterialPassDef {
                        shader: link = "Shaders/StaticMesh/DefaultEnv_Flat"
                    }
                }
            }
        }
    }
    "Maps/KitPieces/HA_Bilgewater/Materials/BW_Perif_Cliff_C8_inst" = StaticMaterialDef {
        name: string = "Maps/KitPieces/HA_Bilgewater/Materials/BW_Perif_Cliff_C8_inst"
        type: u32 = 0
        samplerValues: list2[embed] = {
            StaticMaterialShaderSamplerDef {
                textureName: string = "DiffuseTexture"
                texturePath: string = "ASSETS/Maps/KitPieces/HA_Bilgewater/textures/bw_perif_cliff_c.dds"
                addressW: u32 = 1
            }
        }
        paramValues: list2[embed] = {
            StaticMaterialShaderParamDef {
                name: string = "TintColor"
                value: vec4 = { 0.5, 0.5, 0.5, 1 }
            }
            StaticMaterialShaderParamDef {
                name: string = "PitchFactor"
            }
        }
        techniques: list[embed] = {
            StaticMaterialTechniqueDef {
                name: string = "normal"
                passes: list[embed] = {
                    StaticMaterialPassDef {
                        shader: link = "Shaders/StaticMesh/DefaultEnv_Flat"
                    }
                }
            }
        }
    }
    "Maps/KitPieces/HA_Bilgewater/Materials/BW_bridge_mid_crest_a_inst" = StaticMaterialDef {
        name: string = "Maps/KitPieces/HA_Bilgewater/Materials/BW_bridge_mid_crest_a_inst"
        type: u32 = 0
        samplerValues: list2[embed] = {
            StaticMaterialShaderSamplerDef {
                textureName: string = "DiffuseTexture"
                texturePath: string = "ASSETS/Maps/KitPieces/HA_Bilgewater/textures/bw_bridge_mid_crest_a.dds"
                addressW: u32 = 1
            }
        }
        paramValues: list2[embed] = {
            StaticMaterialShaderParamDef {
                name: string = "TintColor"
                value: vec4 = { 0.5, 0.5, 0.5, 1 }
            }
            StaticMaterialShaderParamDef {
                name: string = "PitchFactor"
            }
        }
        techniques: list[embed] = {
            StaticMaterialTechniqueDef {
                name: string = "normal"
                passes: list[embed] = {
                    StaticMaterialPassDef {
                        shader: link = "Shaders/StaticMesh/DefaultEnv_Flat"
                    }
                }
            }
        }
    }
    "Maps/KitPieces/HA_Bilgewater/Materials/bw_bridge_mid_crest_rope_a_inst" = StaticMaterialDef {
        name: string = "Maps/KitPieces/HA_Bilgewater/Materials/bw_bridge_mid_crest_rope_a_inst"
        type: u32 = 0
        samplerValues: list2[embed] = {
            StaticMaterialShaderSamplerDef {
                textureName: string = "DiffuseTexture"
                texturePath: string = "ASSETS/Maps/KitPieces/HA_Bilgewater/textures/bw_bridge_mid_crest_rope_a.dds"
                addressW: u32 = 1
            }
        }
        paramValues: list2[embed] = {
            StaticMaterialShaderParamDef {
                name: string = "AlphaTestValue"
                value: vec4 = { 0.899999976, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "TintColor"
                value: vec4 = { 0.5, 0.5, 0.5, 1 }
            }
        }
        techniques: list[embed] = {
            StaticMaterialTechniqueDef {
                name: string = "normal"
                passes: list[embed] = {
                    StaticMaterialPassDef {
                        shader: link = "Shaders/StaticMesh/DefaultEnv_Flat_AlphaTest"
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    }
                }
            }
        }
    }
    "Maps/KitPieces/HA_Bilgewater/Materials/bridge_with_fishys_lambert172937_inst" = StaticMaterialDef {
        name: string = "Maps/KitPieces/HA_Bilgewater/Materials/bridge_with_fishys_lambert172937_inst"
        type: u32 = 0
        samplerValues: list2[embed] = {
            StaticMaterialShaderSamplerDef {
                textureName: string = "DiffuseTexture"
                texturePath: string = "ASSETS/Maps/KitPieces/HA_Bilgewater/textures/bw_struc_roof_tile_01.dds"
                addressW: u32 = 1
            }
        }
        paramValues: list2[embed] = {
            StaticMaterialShaderParamDef {
                name: string = "TintColor"
                value: vec4 = { 0.5, 0.5, 0.5, 1 }
            }
            StaticMaterialShaderParamDef {
                name: string = "PitchFactor"
            }
        }
        techniques: list[embed] = {
            StaticMaterialTechniqueDef {
                name: string = "normal"
                passes: list[embed] = {
                    StaticMaterialPassDef {
                        shader: link = "Shaders/StaticMesh/DefaultEnv_Flat"
                    }
                }
            }
        }
    }
    "Maps/KitPieces/HA_Bilgewater/Materials/Bridge_Shipside49_inst" = StaticMaterialDef {
        name: string = "Maps/KitPieces/HA_Bilgewater/Materials/Bridge_Shipside49_inst"
        type: u32 = 0
        samplerValues: list2[embed] = {
            StaticMaterialShaderSamplerDef {
                textureName: string = "DiffuseTexture"
                texturePath: string = "ASSETS/Maps/KitPieces/HA_Bilgewater/textures/bw_bridge_shipside_a.dds"
                addressW: u32 = 1
            }
        }
        paramValues: list2[embed] = {
            StaticMaterialShaderParamDef {
                name: string = "TintColor"
                value: vec4 = { 0.5, 0.5, 0.5, 1 }
            }
            StaticMaterialShaderParamDef {
                name: string = "PitchFactor"
            }
        }
        techniques: list[embed] = {
            StaticMaterialTechniqueDef {
                name: string = "normal"
                passes: list[embed] = {
                    StaticMaterialPassDef {
                        shader: link = "Shaders/StaticMesh/DefaultEnv_Flat"
                    }
                }
            }
        }
    }
    "Maps/KitPieces/HA_Bilgewater/Materials/beach8_inst" = StaticMaterialDef {
        name: string = "Maps/KitPieces/HA_Bilgewater/Materials/beach8_inst"
        type: u32 = 0
        samplerValues: list2[embed] = {
            StaticMaterialShaderSamplerDef {
                textureName: string = "DiffuseTexture"
                texturePath: string = "ASSETS/Maps/KitPieces/HA_Bilgewater/textures/bw_beachrocks_01.dds"
                addressW: u32 = 1
            }
        }
        paramValues: list2[embed] = {
            StaticMaterialShaderParamDef {
                name: string = "TintColor"
                value: vec4 = { 0.5, 0.5, 0.5, 1 }
            }
            StaticMaterialShaderParamDef {
                name: string = "PitchFactor"
            }
        }
        techniques: list[embed] = {
            StaticMaterialTechniqueDef {
                name: string = "normal"
                passes: list[embed] = {
                    StaticMaterialPassDef {
                        shader: link = "Shaders/StaticMesh/DefaultEnv_Flat"
                    }
                }
            }
        }
    }
    "Maps/KitPieces/HA_Bilgewater/Materials/lambert175173_inst" = StaticMaterialDef {
        name: string = "Maps/KitPieces/HA_Bilgewater/Materials/lambert175173_inst"
        type: u32 = 0
        samplerValues: list2[embed] = {
            StaticMaterialShaderSamplerDef {
                textureName: string = "DiffuseTexture"
                texturePath: string = "ASSETS/Maps/KitPieces/HA_Bilgewater/textures/bw_struc_stairs_a.dds"
                addressW: u32 = 1
            }
        }
        paramValues: list2[embed] = {
            StaticMaterialShaderParamDef {
                name: string = "TintColor"
                value: vec4 = { 0.5, 0.5, 0.5, 1 }
            }
            StaticMaterialShaderParamDef {
                name: string = "PitchFactor"
            }
        }
        techniques: list[embed] = {
            StaticMaterialTechniqueDef {
                name: string = "normal"
                passes: list[embed] = {
                    StaticMaterialPassDef {
                        shader: link = "Shaders/StaticMesh/DefaultEnv_Flat"
                    }
                }
            }
        }
    }
    "Maps/KitPieces/HA_Bilgewater/Materials/LM_BridgeCutout16_inst" = StaticMaterialDef {
        name: string = "Maps/KitPieces/HA_Bilgewater/Materials/LM_BridgeCutout16_inst"
        type: u32 = 0
        samplerValues: list2[embed] = {
            StaticMaterialShaderSamplerDef {
                textureName: string = "DiffuseTexture"
                texturePath: string = "ASSETS/Maps/KitPieces/HA_Bilgewater/textures/bw_bridge_mid_cutout_a.dds"
                addressW: u32 = 1
            }
        }
        paramValues: list2[embed] = {
            StaticMaterialShaderParamDef {
                name: string = "TintColor"
                value: vec4 = { 0.5, 0.5, 0.5, 1 }
            }
            StaticMaterialShaderParamDef {
                name: string = "PitchFactor"
            }
        }
        techniques: list[embed] = {
            StaticMaterialTechniqueDef {
                name: string = "normal"
                passes: list[embed] = {
                    StaticMaterialPassDef {
                        shader: link = "Shaders/StaticMesh/DefaultEnv_Flat"
                    }
                }
            }
        }
    }
    "Maps/KitPieces/HA_Bilgewater/Materials/lambert175222_inst" = StaticMaterialDef {
        name: string = "Maps/KitPieces/HA_Bilgewater/Materials/lambert175222_inst"
        type: u32 = 0
        samplerValues: list2[embed] = {
            StaticMaterialShaderSamplerDef {
                textureName: string = "DiffuseTexture"
                texturePath: string = "ASSETS/Maps/KitPieces/HA_Bilgewater/textures/prop_barnicle.dds"
                addressW: u32 = 1
            }
        }
        paramValues: list2[embed] = {
            StaticMaterialShaderParamDef {
                name: string = "TintColor"
                value: vec4 = { 0.5, 0.5, 0.5, 1 }
            }
            StaticMaterialShaderParamDef {
                name: string = "PitchFactor"
            }
        }
        techniques: list[embed] = {
            StaticMaterialTechniqueDef {
                name: string = "normal"
                passes: list[embed] = {
                    StaticMaterialPassDef {
                        shader: link = "Shaders/StaticMesh/DefaultEnv_Flat"
                    }
                }
            }
        }
    }
    "Maps/KitPieces/HA_Bilgewater/Materials/bathysphere_SHOP21_inst" = StaticMaterialDef {
        name: string = "Maps/KitPieces/HA_Bilgewater/Materials/bathysphere_SHOP21_inst"
        type: u32 = 0
        samplerValues: list2[embed] = {
            StaticMaterialShaderSamplerDef {
                textureName: string = "DiffuseTexture"
                texturePath: string = "ASSETS/Maps/KitPieces/HA_Bilgewater/textures/bw_prop_crate_01.dds"
                addressW: u32 = 1
            }
        }
        paramValues: list2[embed] = {
            StaticMaterialShaderParamDef {
                name: string = "TintColor"
                value: vec4 = { 0.5, 0.5, 0.5, 1 }
            }
            StaticMaterialShaderParamDef {
                name: string = "PitchFactor"
            }
        }
        techniques: list[embed] = {
            StaticMaterialTechniqueDef {
                name: string = "normal"
                passes: list[embed] = {
                    StaticMaterialPassDef {
                        shader: link = "Shaders/StaticMesh/DefaultEnv_Flat"
                    }
                }
            }
        }
    }
    "Maps/KitPieces/HA_Bilgewater/Materials/lambert175169_inst" = StaticMaterialDef {
        name: string = "Maps/KitPieces/HA_Bilgewater/Materials/lambert175169_inst"
        type: u32 = 0
        samplerValues: list2[embed] = {
            StaticMaterialShaderSamplerDef {
                textureName: string = "DiffuseTexture"
                texturePath: string = "ASSETS/Maps/KitPieces/HA_Bilgewater/textures/bw_s_base_shop_cage_02.dds"
                addressW: u32 = 1
            }
        }
        paramValues: list2[embed] = {
            StaticMaterialShaderParamDef {
                name: string = "TintColor"
                value: vec4 = { 0.5, 0.5, 0.5, 1 }
            }
            StaticMaterialShaderParamDef {
                name: string = "PitchFactor"
            }
        }
        techniques: list[embed] = {
            StaticMaterialTechniqueDef {
                name: string = "normal"
                passes: list[embed] = {
                    StaticMaterialPassDef {
                        shader: link = "Shaders/StaticMesh/DefaultEnv_Flat"
                    }
                }
            }
        }
    }
    "Maps/KitPieces/HA_Bilgewater/Materials/lambert175297_inst" = StaticMaterialDef {
        name: string = "Maps/KitPieces/HA_Bilgewater/Materials/lambert175297_inst"
        type: u32 = 0
        samplerValues: list2[embed] = {
            StaticMaterialShaderSamplerDef {
                textureName: string = "DiffuseTexture"
                texturePath: string = "ASSETS/Maps/KitPieces/HA_Bilgewater/textures/bw_struc_boat_roof_a.dds"
                addressW: u32 = 1
            }
        }
        paramValues: list2[embed] = {
            StaticMaterialShaderParamDef {
                name: string = "TintColor"
                value: vec4 = { 0.5, 0.5, 0.5, 1 }
            }
            StaticMaterialShaderParamDef {
                name: string = "PitchFactor"
            }
        }
        techniques: list[embed] = {
            StaticMaterialTechniqueDef {
                name: string = "normal"
                passes: list[embed] = {
                    StaticMaterialPassDef {
                        shader: link = "Shaders/StaticMesh/DefaultEnv_Flat"
                    }
                }
            }
        }
    }
    "Maps/KitPieces/HA_Bilgewater/Materials/lambert175202_inst" = StaticMaterialDef {
        name: string = "Maps/KitPieces/HA_Bilgewater/Materials/lambert175202_inst"
        type: u32 = 0
        samplerValues: list2[embed] = {
            StaticMaterialShaderSamplerDef {
                textureName: string = "DiffuseTexture"
                texturePath: string = "ASSETS/Maps/KitPieces/HA_Bilgewater/textures/bw_props_harpoon_a.dds"
                addressW: u32 = 1
            }
        }
        paramValues: list2[embed] = {
            StaticMaterialShaderParamDef {
                name: string = "TintColor"
                value: vec4 = { 0.5, 0.5, 0.5, 1 }
            }
            StaticMaterialShaderParamDef {
                name: string = "PitchFactor"
            }
        }
        techniques: list[embed] = {
            StaticMaterialTechniqueDef {
                name: string = "normal"
                passes: list[embed] = {
                    StaticMaterialPassDef {
                        shader: link = "Shaders/StaticMesh/DefaultEnv_Flat"
                    }
                }
            }
        }
    }
    "Maps/KitPieces/HA_Bilgewater/Materials/LM_Ground_Lane_B37_inst" = StaticMaterialDef {
        name: string = "Maps/KitPieces/HA_Bilgewater/Materials/LM_Ground_Lane_B37_inst"
        type: u32 = 0
        samplerValues: list2[embed] = {
            StaticMaterialShaderSamplerDef {
                textureName: string = "DiffuseTexture"
                texturePath: string = "ASSETS/Maps/KitPieces/HA_Bilgewater/textures/bw_ground_lane_b.dds"
                addressW: u32 = 1
            }
        }
        paramValues: list2[embed] = {
            StaticMaterialShaderParamDef {
                name: string = "TintColor"
                value: vec4 = { 0.5, 0.5, 0.5, 1 }
            }
            StaticMaterialShaderParamDef {
                name: string = "PitchFactor"
            }
        }
        techniques: list[embed] = {
            StaticMaterialTechniqueDef {
                name: string = "normal"
                passes: list[embed] = {
                    StaticMaterialPassDef {
                        shader: link = "Shaders/StaticMesh/DefaultEnv_Flat"
                    }
                }
            }
        }
    }
    "Maps/KitPieces/HA_Bilgewater/Materials/lambert175294_inst" = StaticMaterialDef {
        name: string = "Maps/KitPieces/HA_Bilgewater/Materials/lambert175294_inst"
        type: u32 = 0
        samplerValues: list2[embed] = {
            StaticMaterialShaderSamplerDef {
                textureName: string = "DiffuseTexture"
                texturePath: string = "ASSETS/Maps/KitPieces/HA_Bilgewater/textures/bw_smallpipechimney_01.dds"
                addressW: u32 = 1
            }
        }
        paramValues: list2[embed] = {
            StaticMaterialShaderParamDef {
                name: string = "TintColor"
                value: vec4 = { 0.5, 0.5, 0.5, 1 }
            }
            StaticMaterialShaderParamDef {
                name: string = "PitchFactor"
            }
        }
        techniques: list[embed] = {
            StaticMaterialTechniqueDef {
                name: string = "normal"
                passes: list[embed] = {
                    StaticMaterialPassDef {
                        shader: link = "Shaders/StaticMesh/DefaultEnv_Flat"
                    }
                }
            }
        }
    }
    "Maps/KitPieces/HA_Bilgewater/Materials/cannon_lambert35_inst" = StaticMaterialDef {
        name: string = "Maps/KitPieces/HA_Bilgewater/Materials/cannon_lambert35_inst"
        type: u32 = 0
        samplerValues: list2[embed] = {
            StaticMaterialShaderSamplerDef {
                textureName: string = "DiffuseTexture"
                texturePath: string = "ASSETS/Maps/KitPieces/HA_Bilgewater/textures/props_cannon_01.dds"
                addressW: u32 = 1
            }
        }
        paramValues: list2[embed] = {
            StaticMaterialShaderParamDef {
                name: string = "TintColor"
                value: vec4 = { 0.5, 0.5, 0.5, 1 }
            }
            StaticMaterialShaderParamDef {
                name: string = "PitchFactor"
            }
        }
        techniques: list[embed] = {
            StaticMaterialTechniqueDef {
                name: string = "normal"
                passes: list[embed] = {
                    StaticMaterialPassDef {
                        shader: link = "Shaders/StaticMesh/DefaultEnv_Flat"
                    }
                }
            }
        }
    }
    "Maps/KitPieces/HA_Bilgewater/Materials/LM_ground_base_north_A1_inst" = StaticMaterialDef {
        name: string = "Maps/KitPieces/HA_Bilgewater/Materials/LM_ground_base_north_A1_inst"
        type: u32 = 0
        samplerValues: list2[embed] = {
            StaticMaterialShaderSamplerDef {
                textureName: string = "DiffuseTexture"
                texturePath: string = "ASSETS/Maps/KitPieces/HA_Bilgewater/textures/bw_ground_base_north_a.dds"
                addressW: u32 = 1
            }
        }
        paramValues: list2[embed] = {
            StaticMaterialShaderParamDef {
                name: string = "TintColor"
                value: vec4 = { 0.5, 0.5, 0.5, 1 }
            }
            StaticMaterialShaderParamDef {
                name: string = "PitchFactor"
            }
        }
        techniques: list[embed] = {
            StaticMaterialTechniqueDef {
                name: string = "normal"
                passes: list[embed] = {
                    StaticMaterialPassDef {
                        shader: link = "Shaders/StaticMesh/DefaultEnv_Flat"
                    }
                }
            }
        }
    }
    "Maps/KitPieces/HA_Bilgewater/Materials/lambert173614_inst" = StaticMaterialDef {
        name: string = "Maps/KitPieces/HA_Bilgewater/Materials/lambert173614_inst"
        type: u32 = 0
        samplerValues: list2[embed] = {
            StaticMaterialShaderSamplerDef {
                textureName: string = "DiffuseTexture"
                texturePath: string = "ASSETS/Maps/KitPieces/HA_Bilgewater/textures/bw_bridge_columns_03.dds"
                addressW: u32 = 1
            }
        }
        paramValues: list2[embed] = {
            StaticMaterialShaderParamDef {
                name: string = "TintColor"
                value: vec4 = { 0.5, 0.5, 0.5, 1 }
            }
            StaticMaterialShaderParamDef {
                name: string = "PitchFactor"
            }
        }
        techniques: list[embed] = {
            StaticMaterialTechniqueDef {
                name: string = "normal"
                passes: list[embed] = {
                    StaticMaterialPassDef {
                        shader: link = "Shaders/StaticMesh/DefaultEnv_Flat"
                    }
                }
            }
        }
    }
    "Maps/KitPieces/HA_Bilgewater/Materials/lambert175178_inst" = StaticMaterialDef {
        name: string = "Maps/KitPieces/HA_Bilgewater/Materials/lambert175178_inst"
        type: u32 = 0
        samplerValues: list2[embed] = {
            StaticMaterialShaderSamplerDef {
                textureName: string = "DiffuseTexture"
                texturePath: string = "ASSETS/Maps/KitPieces/HA_Bilgewater/textures/props_canon_vista.dds"
                addressW: u32 = 1
            }
        }
        paramValues: list2[embed] = {
            StaticMaterialShaderParamDef {
                name: string = "TintColor"
                value: vec4 = { 0.5, 0.5, 0.5, 1 }
            }
            StaticMaterialShaderParamDef {
                name: string = "PitchFactor"
            }
        }
        techniques: list[embed] = {
            StaticMaterialTechniqueDef {
                name: string = "normal"
                passes: list[embed] = {
                    StaticMaterialPassDef {
                        shader: link = "Shaders/StaticMesh/DefaultEnv_Flat"
                    }
                }
            }
        }
    }
    "Maps/KitPieces/HA_Bilgewater/Materials/ancienthouses2_inst" = StaticMaterialDef {
        name: string = "Maps/KitPieces/HA_Bilgewater/Materials/ancienthouses2_inst"
        type: u32 = 0
        samplerValues: list2[embed] = {
            StaticMaterialShaderSamplerDef {
                textureName: string = "DiffuseTexture"
                texturePath: string = "ASSETS/Maps/KitPieces/HA_Bilgewater/textures/bw_perif_cliffhouses_a.dds"
                addressW: u32 = 1
            }
        }
        paramValues: list2[embed] = {
            StaticMaterialShaderParamDef {
                name: string = "TintColor"
                value: vec4 = { 0.5, 0.5, 0.5, 1 }
            }
            StaticMaterialShaderParamDef {
                name: string = "PitchFactor"
            }
        }
        techniques: list[embed] = {
            StaticMaterialTechniqueDef {
                name: string = "normal"
                passes: list[embed] = {
                    StaticMaterialPassDef {
                        shader: link = "Shaders/StaticMesh/DefaultEnv_Flat"
                    }
                }
            }
        }
    }
    "Maps/KitPieces/HA_Bilgewater/Materials/lambert175179_inst" = StaticMaterialDef {
        name: string = "Maps/KitPieces/HA_Bilgewater/Materials/lambert175179_inst"
        type: u32 = 0
        samplerValues: list2[embed] = {
            StaticMaterialShaderSamplerDef {
                textureName: string = "DiffuseTexture"
                texturePath: string = "ASSETS/Maps/KitPieces/HA_Bilgewater/textures/bw_deck_card_a.dds"
                addressW: u32 = 1
            }
        }
        paramValues: list2[embed] = {
            StaticMaterialShaderParamDef {
                name: string = "AlphaTestValue"
                value: vec4 = { 0.899999976, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "TintColor"
                value: vec4 = { 0.5, 0.5, 0.5, 1 }
            }
        }
        techniques: list[embed] = {
            StaticMaterialTechniqueDef {
                name: string = "normal"
                passes: list[embed] = {
                    StaticMaterialPassDef {
                        shader: link = "Shaders/StaticMesh/DefaultEnv_Flat_AlphaTest"
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    }
                }
            }
        }
    }
    "Maps/KitPieces/HA_Bilgewater/Materials/LM_Ground_Lane_D39_inst" = StaticMaterialDef {
        name: string = "Maps/KitPieces/HA_Bilgewater/Materials/LM_Ground_Lane_D39_inst"
        type: u32 = 0
        samplerValues: list2[embed] = {
            StaticMaterialShaderSamplerDef {
                textureName: string = "DiffuseTexture"
                texturePath: string = "ASSETS/Maps/KitPieces/HA_Bilgewater/textures/bw_ground_lane_d.dds"
                addressW: u32 = 1
            }
        }
        paramValues: list2[embed] = {
            StaticMaterialShaderParamDef {
                name: string = "TintColor"
                value: vec4 = { 0.5, 0.5, 0.5, 1 }
            }
            StaticMaterialShaderParamDef {
                name: string = "PitchFactor"
            }
        }
        techniques: list[embed] = {
            StaticMaterialTechniqueDef {
                name: string = "normal"
                passes: list[embed] = {
                    StaticMaterialPassDef {
                        shader: link = "Shaders/StaticMesh/DefaultEnv_Flat"
                    }
                }
            }
        }
    }
    "Maps/KitPieces/HA_Bilgewater/Materials/LM_ground_base_north_C1_inst" = StaticMaterialDef {
        name: string = "Maps/KitPieces/HA_Bilgewater/Materials/LM_ground_base_north_C1_inst"
        type: u32 = 0
        samplerValues: list2[embed] = {
            StaticMaterialShaderSamplerDef {
                textureName: string = "DiffuseTexture"
                texturePath: string = "ASSETS/Maps/KitPieces/HA_Bilgewater/textures/bw_ground_base_north_c.dds"
                addressW: u32 = 1
            }
        }
        paramValues: list2[embed] = {
            StaticMaterialShaderParamDef {
                name: string = "TintColor"
                value: vec4 = { 0.5, 0.5, 0.5, 1 }
            }
            StaticMaterialShaderParamDef {
                name: string = "PitchFactor"
            }
        }
        techniques: list[embed] = {
            StaticMaterialTechniqueDef {
                name: string = "normal"
                passes: list[embed] = {
                    StaticMaterialPassDef {
                        shader: link = "Shaders/StaticMesh/DefaultEnv_Flat"
                    }
                }
            }
        }
    }
    "Maps/KitPieces/HA_Bilgewater/Materials/lambert175171_inst" = StaticMaterialDef {
        name: string = "Maps/KitPieces/HA_Bilgewater/Materials/lambert175171_inst"
        type: u32 = 0
        samplerValues: list2[embed] = {
            StaticMaterialShaderSamplerDef {
                textureName: string = "DiffuseTexture"
                texturePath: string = "ASSETS/Maps/KitPieces/HA_Bilgewater/textures/bw_prop_sack1.dds"
                addressW: u32 = 1
            }
        }
        paramValues: list2[embed] = {
            StaticMaterialShaderParamDef {
                name: string = "TintColor"
                value: vec4 = { 0.5, 0.5, 0.5, 1 }
            }
            StaticMaterialShaderParamDef {
                name: string = "PitchFactor"
            }
        }
        techniques: list[embed] = {
            StaticMaterialTechniqueDef {
                name: string = "normal"
                passes: list[embed] = {
                    StaticMaterialPassDef {
                        shader: link = "Shaders/StaticMesh/DefaultEnv_Flat"
                    }
                }
            }
        }
    }
    "Maps/KitPieces/HA_Bilgewater/Materials/BW_wood_mast_inst" = StaticMaterialDef {
        name: string = "Maps/KitPieces/HA_Bilgewater/Materials/BW_wood_mast_inst"
        type: u32 = 0
        samplerValues: list2[embed] = {
            StaticMaterialShaderSamplerDef {
                textureName: string = "DiffuseTexture"
                texturePath: string = "ASSETS/Maps/KitPieces/HA_Bilgewater/textures/BW_wood_mast.dds"
                addressW: u32 = 1
            }
        }
        paramValues: list2[embed] = {
            StaticMaterialShaderParamDef {
                name: string = "TintColor"
                value: vec4 = { 0.5, 0.5, 0.5, 1 }
            }
            StaticMaterialShaderParamDef {
                name: string = "PitchFactor"
            }
        }
        techniques: list[embed] = {
            StaticMaterialTechniqueDef {
                name: string = "normal"
                passes: list[embed] = {
                    StaticMaterialPassDef {
                        shader: link = "Shaders/StaticMesh/DefaultEnv_Flat"
                    }
                }
            }
        }
    }
    "Maps/KitPieces/HA_Bilgewater/Materials/new_tex11_inst" = StaticMaterialDef {
        name: string = "Maps/KitPieces/HA_Bilgewater/Materials/new_tex11_inst"
        type: u32 = 0
        samplerValues: list2[embed] = {
            StaticMaterialShaderSamplerDef {
                textureName: string = "DiffuseTexture"
                texturePath: string = "ASSETS/Maps/KitPieces/HA_Bilgewater/textures/bw_palm_frond_a.dds"
                addressW: u32 = 1
            }
        }
        paramValues: list2[embed] = {
            StaticMaterialShaderParamDef {
                name: string = "AlphaTestValue"
                value: vec4 = { 0.899999976, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "TintColor"
                value: vec4 = { 0.5, 0.5, 0.5, 1 }
            }
        }
        techniques: list[embed] = {
            StaticMaterialTechniqueDef {
                name: string = "normal"
                passes: list[embed] = {
                    StaticMaterialPassDef {
                        shader: link = "Shaders/StaticMesh/DefaultEnv_Flat_AlphaTest"
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    }
                }
            }
        }
    }
    "Maps/KitPieces/HA_Bilgewater/Materials/lambert175309_inst" = StaticMaterialDef {
        name: string = "Maps/KitPieces/HA_Bilgewater/Materials/lambert175309_inst"
        type: u32 = 0
        samplerValues: list2[embed] = {
            StaticMaterialShaderSamplerDef {
                textureName: string = "DiffuseTexture"
                texturePath: string = "ASSETS/Maps/KitPieces/HA_Bilgewater/textures/house_comp_mid_c.dds"
                addressW: u32 = 1
            }
        }
        paramValues: list2[embed] = {
            StaticMaterialShaderParamDef {
                name: string = "TintColor"
                value: vec4 = { 0.5, 0.5, 0.5, 1 }
            }
            StaticMaterialShaderParamDef {
                name: string = "PitchFactor"
            }
        }
        techniques: list[embed] = {
            StaticMaterialTechniqueDef {
                name: string = "normal"
                passes: list[embed] = {
                    StaticMaterialPassDef {
                        shader: link = "Shaders/StaticMesh/DefaultEnv_Flat"
                    }
                }
            }
        }
    }
    "Maps/KitPieces/HA_Bilgewater/Materials/BW_N_Base_Shrine10_inst" = StaticMaterialDef {
        name: string = "Maps/KitPieces/HA_Bilgewater/Materials/BW_N_Base_Shrine10_inst"
        type: u32 = 0
        samplerValues: list2[embed] = {
            StaticMaterialShaderSamplerDef {
                textureName: string = "DiffuseTexture"
                texturePath: string = "ASSETS/Maps/KitPieces/HA_Bilgewater/textures/bw_n_base_shrine.dds"
                addressW: u32 = 1
            }
        }
        paramValues: list2[embed] = {
            StaticMaterialShaderParamDef {
                name: string = "TintColor"
                value: vec4 = { 0.5, 0.5, 0.5, 1 }
            }
            StaticMaterialShaderParamDef {
                name: string = "PitchFactor"
            }
        }
        techniques: list[embed] = {
            StaticMaterialTechniqueDef {
                name: string = "normal"
                passes: list[embed] = {
                    StaticMaterialPassDef {
                        shader: link = "Shaders/StaticMesh/DefaultEnv_Flat"
                    }
                }
            }
        }
    }
    "Maps/KitPieces/HA_Bilgewater/Materials/LM_ground_base_north_B1_inst" = StaticMaterialDef {
        name: string = "Maps/KitPieces/HA_Bilgewater/Materials/LM_ground_base_north_B1_inst"
        type: u32 = 0
        samplerValues: list2[embed] = {
            StaticMaterialShaderSamplerDef {
                textureName: string = "DiffuseTexture"
                texturePath: string = "ASSETS/Maps/KitPieces/HA_Bilgewater/textures/bw_ground_base_north_b.dds"
                addressW: u32 = 1
            }
        }
        paramValues: list2[embed] = {
            StaticMaterialShaderParamDef {
                name: string = "TintColor"
                value: vec4 = { 0.5, 0.5, 0.5, 1 }
            }
            StaticMaterialShaderParamDef {
                name: string = "PitchFactor"
            }
        }
        techniques: list[embed] = {
            StaticMaterialTechniqueDef {
                name: string = "normal"
                passes: list[embed] = {
                    StaticMaterialPassDef {
                        shader: link = "Shaders/StaticMesh/DefaultEnv_Flat"
                    }
                }
            }
        }
    }
    "Maps/KitPieces/HA_Bilgewater/Materials/BW_struc_wood_trim_03_inst" = StaticMaterialDef {
        name: string = "Maps/KitPieces/HA_Bilgewater/Materials/BW_struc_wood_trim_03_inst"
        type: u32 = 0
        samplerValues: list2[embed] = {
            StaticMaterialShaderSamplerDef {
                textureName: string = "DiffuseTexture"
                texturePath: string = "ASSETS/Maps/KitPieces/HA_Bilgewater/textures/BW_struc_wood_trim_01.dds"
                addressW: u32 = 1
            }
        }
        paramValues: list2[embed] = {
            StaticMaterialShaderParamDef {
                name: string = "TintColor"
                value: vec4 = { 0.5, 0.5, 0.5, 1 }
            }
            StaticMaterialShaderParamDef {
                name: string = "PitchFactor"
            }
        }
        techniques: list[embed] = {
            StaticMaterialTechniqueDef {
                name: string = "normal"
                passes: list[embed] = {
                    StaticMaterialPassDef {
                        shader: link = "Shaders/StaticMesh/DefaultEnv_Flat"
                    }
                }
            }
        }
    }
    "Maps/KitPieces/HA_Bilgewater/Materials/lambert175172_inst" = StaticMaterialDef {
        name: string = "Maps/KitPieces/HA_Bilgewater/Materials/lambert175172_inst"
        type: u32 = 0
        samplerValues: list2[embed] = {
            StaticMaterialShaderSamplerDef {
                textureName: string = "DiffuseTexture"
                texturePath: string = "ASSETS/Maps/KitPieces/HA_Bilgewater/textures/structure_building_kit01.dds"
                addressW: u32 = 1
            }
        }
        paramValues: list2[embed] = {
            StaticMaterialShaderParamDef {
                name: string = "AlphaTestValue"
                value: vec4 = { 0.899999976, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "TintColor"
                value: vec4 = { 0.5, 0.5, 0.5, 1 }
            }
        }
        techniques: list[embed] = {
            StaticMaterialTechniqueDef {
                name: string = "normal"
                passes: list[embed] = {
                    StaticMaterialPassDef {
                        shader: link = "Shaders/StaticMesh/DefaultEnv_Flat_AlphaTest"
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    }
                }
            }
        }
    }
    "Maps/KitPieces/HA_Bilgewater/Materials/BW_Decor_A_inst" = StaticMaterialDef {
        name: string = "Maps/KitPieces/HA_Bilgewater/Materials/BW_Decor_A_inst"
        type: u32 = 0
        samplerValues: list2[embed] = {
            StaticMaterialShaderSamplerDef {
                textureName: string = "DiffuseTexture"
                texturePath: string = "ASSETS/Maps/KitPieces/HA_Bilgewater/textures/bw_decor_a.dds"
                addressW: u32 = 1
            }
        }
        paramValues: list2[embed] = {
            StaticMaterialShaderParamDef {
                name: string = "TintColor"
                value: vec4 = { 0.5, 0.5, 0.5, 1 }
            }
            StaticMaterialShaderParamDef {
                name: string = "PitchFactor"
            }
        }
        techniques: list[embed] = {
            StaticMaterialTechniqueDef {
                name: string = "normal"
                passes: list[embed] = {
                    StaticMaterialPassDef {
                        shader: link = "Shaders/StaticMesh/DefaultEnv_Flat"
                    }
                }
            }
        }
    }
    "Maps/KitPieces/HA_Bilgewater/Materials/LM_BaseGroundTrim_inst" = StaticMaterialDef {
        name: string = "Maps/KitPieces/HA_Bilgewater/Materials/LM_BaseGroundTrim_inst"
        type: u32 = 0
        samplerValues: list2[embed] = {
            StaticMaterialShaderSamplerDef {
                textureName: string = "DiffuseTexture"
                texturePath: string = "ASSETS/Maps/KitPieces/HA_Bilgewater/textures/bw_bridge_railing_b.dds"
                addressW: u32 = 1
            }
        }
        paramValues: list2[embed] = {
            StaticMaterialShaderParamDef {
                name: string = "TintColor"
                value: vec4 = { 0.5, 0.5, 0.5, 1 }
            }
            StaticMaterialShaderParamDef {
                name: string = "PitchFactor"
            }
        }
        techniques: list[embed] = {
            StaticMaterialTechniqueDef {
                name: string = "normal"
                passes: list[embed] = {
                    StaticMaterialPassDef {
                        shader: link = "Shaders/StaticMesh/DefaultEnv_Flat"
                    }
                }
            }
        }
    }
    "Maps/KitPieces/HA_Bilgewater/Materials/hing_temp_bk_lambert174751_inst" = StaticMaterialDef {
        name: string = "Maps/KitPieces/HA_Bilgewater/Materials/hing_temp_bk_lambert174751_inst"
        type: u32 = 0
        samplerValues: list2[embed] = {
            StaticMaterialShaderSamplerDef {
                textureName: string = "DiffuseTexture"
                texturePath: string = "ASSETS/Maps/KitPieces/HA_Bilgewater/textures/bw_vista_02.dds"
                addressW: u32 = 1
            }
        }
        paramValues: list2[embed] = {
            StaticMaterialShaderParamDef {
                name: string = "AlphaTestValue"
                value: vec4 = { 0.899999976, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "TintColor"
                value: vec4 = { 0.5, 0.5, 0.5, 1 }
            }
        }
        techniques: list[embed] = {
            StaticMaterialTechniqueDef {
                name: string = "normal"
                passes: list[embed] = {
                    StaticMaterialPassDef {
                        shader: link = "Shaders/StaticMesh/DefaultEnv_Flat_AlphaTest"
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    }
                }
            }
        }
    }
    "Maps/KitPieces/HA_Bilgewater/Materials/lambert175304_inst" = StaticMaterialDef {
        name: string = "Maps/KitPieces/HA_Bilgewater/Materials/lambert175304_inst"
        type: u32 = 0
        samplerValues: list2[embed] = {
            StaticMaterialShaderSamplerDef {
                textureName: string = "DiffuseTexture"
                texturePath: string = "ASSETS/Maps/KitPieces/HA_Bilgewater/textures/bw_props_crows_nest_a.dds"
                addressW: u32 = 1
            }
        }
        paramValues: list2[embed] = {
            StaticMaterialShaderParamDef {
                name: string = "AlphaTestValue"
                value: vec4 = { 0.899999976, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "TintColor"
                value: vec4 = { 0.5, 0.5, 0.5, 1 }
            }
        }
        techniques: list[embed] = {
            StaticMaterialTechniqueDef {
                name: string = "normal"
                passes: list[embed] = {
                    StaticMaterialPassDef {
                        shader: link = "Shaders/StaticMesh/DefaultEnv_Flat_AlphaTest"
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    }
                }
            }
        }
    }
    "Maps/KitPieces/HA_Bilgewater/Materials/pilings_lambert14_inst" = StaticMaterialDef {
        name: string = "Maps/KitPieces/HA_Bilgewater/Materials/pilings_lambert14_inst"
        type: u32 = 0
        samplerValues: list2[embed] = {
            StaticMaterialShaderSamplerDef {
                textureName: string = "DiffuseTexture"
                texturePath: string = "ASSETS/Maps/KitPieces/HA_Bilgewater/textures/bw_props_pilings.dds"
                addressW: u32 = 1
            }
        }
        paramValues: list2[embed] = {
            StaticMaterialShaderParamDef {
                name: string = "TintColor"
                value: vec4 = { 0.5, 0.5, 0.5, 1 }
            }
            StaticMaterialShaderParamDef {
                name: string = "PitchFactor"
            }
        }
        techniques: list[embed] = {
            StaticMaterialTechniqueDef {
                name: string = "normal"
                passes: list[embed] = {
                    StaticMaterialPassDef {
                        shader: link = "Shaders/StaticMesh/DefaultEnv_Flat"
                    }
                }
            }
        }
    }
    "Maps/KitPieces/HA_Bilgewater/Materials/BW_OLD_bridge_side_elements_prop_sails18_inst" = StaticMaterialDef {
        name: string = "Maps/KitPieces/HA_Bilgewater/Materials/BW_OLD_bridge_side_elements_prop_sails18_inst"
        type: u32 = 0
        samplerValues: list2[embed] = {
            StaticMaterialShaderSamplerDef {
                textureName: string = "DiffuseTexture"
                texturePath: string = "ASSETS/Maps/KitPieces/HA_Bilgewater/textures/prop_sails.dds"
                addressW: u32 = 1
            }
        }
        paramValues: list2[embed] = {
            StaticMaterialShaderParamDef {
                name: string = "AlphaTestValue"
                value: vec4 = { 0.899999976, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "TintColor"
                value: vec4 = { 0.5, 0.5, 0.5, 1 }
            }
        }
        techniques: list[embed] = {
            StaticMaterialTechniqueDef {
                name: string = "normal"
                passes: list[embed] = {
                    StaticMaterialPassDef {
                        shader: link = "Shaders/StaticMesh/DefaultEnv_Flat_AlphaTest"
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    }
                }
            }
        }
    }
    "Maps/KitPieces/HA_Bilgewater/Materials/S_Base_Harpoon13_inst" = StaticMaterialDef {
        name: string = "Maps/KitPieces/HA_Bilgewater/Materials/S_Base_Harpoon13_inst"
        type: u32 = 0
        samplerValues: list2[embed] = {
            StaticMaterialShaderSamplerDef {
                textureName: string = "DiffuseTexture"
                texturePath: string = "ASSETS/Maps/KitPieces/HA_Bilgewater/textures/bw_s_base_harpoon.dds"
                addressW: u32 = 1
            }
        }
        paramValues: list2[embed] = {
            StaticMaterialShaderParamDef {
                name: string = "TintColor"
                value: vec4 = { 0.5, 0.5, 0.5, 1 }
            }
            StaticMaterialShaderParamDef {
                name: string = "PitchFactor"
            }
        }
        techniques: list[embed] = {
            StaticMaterialTechniqueDef {
                name: string = "normal"
                passes: list[embed] = {
                    StaticMaterialPassDef {
                        shader: link = "Shaders/StaticMesh/DefaultEnv_Flat"
                    }
                }
            }
        }
    }
    "Maps/KitPieces/HA_Bilgewater/Materials/props_anchor_07_inst" = StaticMaterialDef {
        name: string = "Maps/KitPieces/HA_Bilgewater/Materials/props_anchor_07_inst"
        type: u32 = 0
        samplerValues: list2[embed] = {
            StaticMaterialShaderSamplerDef {
                textureName: string = "DiffuseTexture"
                texturePath: string = "ASSETS/Maps/KitPieces/HA_Bilgewater/textures/props_anchor_01.dds"
                addressW: u32 = 1
            }
        }
        paramValues: list2[embed] = {
            StaticMaterialShaderParamDef {
                name: string = "TintColor"
                value: vec4 = { 0.5, 0.5, 0.5, 1 }
            }
            StaticMaterialShaderParamDef {
                name: string = "PitchFactor"
            }
        }
        techniques: list[embed] = {
            StaticMaterialTechniqueDef {
                name: string = "normal"
                passes: list[embed] = {
                    StaticMaterialPassDef {
                        shader: link = "Shaders/StaticMesh/DefaultEnv_Flat"
                    }
                }
            }
        }
    }
    "Maps/KitPieces/HA_Bilgewater/Materials/lambert173688_inst" = StaticMaterialDef {
        name: string = "Maps/KitPieces/HA_Bilgewater/Materials/lambert173688_inst"
        type: u32 = 0
        samplerValues: list2[embed] = {
            StaticMaterialShaderSamplerDef {
                textureName: string = "DiffuseTexture"
                texturePath: string = "ASSETS/Maps/KitPieces/HA_Bilgewater/textures/bw_prop_pulley_a.dds"
                addressW: u32 = 1
            }
        }
        paramValues: list2[embed] = {
            StaticMaterialShaderParamDef {
                name: string = "TintColor"
                value: vec4 = { 0.5, 0.5, 0.5, 1 }
            }
            StaticMaterialShaderParamDef {
                name: string = "PitchFactor"
            }
        }
        techniques: list[embed] = {
            StaticMaterialTechniqueDef {
                name: string = "normal"
                passes: list[embed] = {
                    StaticMaterialPassDef {
                        shader: link = "Shaders/StaticMesh/DefaultEnv_Flat"
                    }
                }
            }
        }
    }
    "Maps/KitPieces/HA_Bilgewater/Materials/bridge_with_fishys_lambert172938_inst" = StaticMaterialDef {
        name: string = "Maps/KitPieces/HA_Bilgewater/Materials/bridge_with_fishys_lambert172938_inst"
        type: u32 = 0
        samplerValues: list2[embed] = {
            StaticMaterialShaderSamplerDef {
                textureName: string = "DiffuseTexture"
                texturePath: string = "ASSETS/Maps/KitPieces/HA_Bilgewater/textures/bw_struc_brick_base_01.dds"
                addressW: u32 = 1
            }
        }
        paramValues: list2[embed] = {
            StaticMaterialShaderParamDef {
                name: string = "TintColor"
                value: vec4 = { 0.5, 0.5, 0.5, 1 }
            }
            StaticMaterialShaderParamDef {
                name: string = "PitchFactor"
            }
        }
        techniques: list[embed] = {
            StaticMaterialTechniqueDef {
                name: string = "normal"
                passes: list[embed] = {
                    StaticMaterialPassDef {
                        shader: link = "Shaders/StaticMesh/DefaultEnv_Flat"
                    }
                }
            }
        }
    }
    "Maps/KitPieces/HA_Bilgewater/Materials/lambert175205_inst" = StaticMaterialDef {
        name: string = "Maps/KitPieces/HA_Bilgewater/Materials/lambert175205_inst"
        type: u32 = 0
        samplerValues: list2[embed] = {
            StaticMaterialShaderSamplerDef {
                textureName: string = "DiffuseTexture"
                texturePath: string = "ASSETS/Maps/KitPieces/HA_Bilgewater/textures/bw_props_bottle_a.dds"
                addressW: u32 = 1
            }
        }
        paramValues: list2[embed] = {
            StaticMaterialShaderParamDef {
                name: string = "TintColor"
                value: vec4 = { 0.5, 0.5, 0.5, 1 }
            }
            StaticMaterialShaderParamDef {
                name: string = "PitchFactor"
            }
        }
        techniques: list[embed] = {
            StaticMaterialTechniqueDef {
                name: string = "normal"
                passes: list[embed] = {
                    StaticMaterialPassDef {
                        shader: link = "Shaders/StaticMesh/DefaultEnv_Flat"
                    }
                }
            }
        }
    }
    "Maps/KitPieces/HA_Bilgewater/Materials/BW_OLD_bridge_side_elements_bow_beam86_inst" = StaticMaterialDef {
        name: string = "Maps/KitPieces/HA_Bilgewater/Materials/BW_OLD_bridge_side_elements_bow_beam86_inst"
        type: u32 = 0
        samplerValues: list2[embed] = {
            StaticMaterialShaderSamplerDef {
                textureName: string = "DiffuseTexture"
                texturePath: string = "ASSETS/Maps/KitPieces/HA_Bilgewater/textures/bow_beam.dds"
                addressW: u32 = 1
            }
        }
        paramValues: list2[embed] = {
            StaticMaterialShaderParamDef {
                name: string = "TintColor"
                value: vec4 = { 0.5, 0.5, 0.5, 1 }
            }
            StaticMaterialShaderParamDef {
                name: string = "PitchFactor"
            }
        }
        techniques: list[embed] = {
            StaticMaterialTechniqueDef {
                name: string = "normal"
                passes: list[embed] = {
                    StaticMaterialPassDef {
                        shader: link = "Shaders/StaticMesh/DefaultEnv_Flat"
                    }
                }
            }
        }
    }
    "Maps/KitPieces/HA_Bilgewater/Materials/BW_Perif_Cliff_B16_inst" = StaticMaterialDef {
        name: string = "Maps/KitPieces/HA_Bilgewater/Materials/BW_Perif_Cliff_B16_inst"
        type: u32 = 0
        samplerValues: list2[embed] = {
            StaticMaterialShaderSamplerDef {
                textureName: string = "DiffuseTexture"
                texturePath: string = "ASSETS/Maps/KitPieces/HA_Bilgewater/textures/bw_perif_cliff_b.dds"
                addressW: u32 = 1
            }
        }
        paramValues: list2[embed] = {
            StaticMaterialShaderParamDef {
                name: string = "TintColor"
                value: vec4 = { 0.5, 0.5, 0.5, 1 }
            }
            StaticMaterialShaderParamDef {
                name: string = "PitchFactor"
            }
        }
        techniques: list[embed] = {
            StaticMaterialTechniqueDef {
                name: string = "normal"
                passes: list[embed] = {
                    StaticMaterialPassDef {
                        shader: link = "Shaders/StaticMesh/DefaultEnv_Flat"
                    }
                }
            }
        }
    }
    "Maps/KitPieces/HA_Bilgewater/Materials/lambert175311_inst" = StaticMaterialDef {
        name: string = "Maps/KitPieces/HA_Bilgewater/Materials/lambert175311_inst"
        type: u32 = 0
        samplerValues: list2[embed] = {
            StaticMaterialShaderSamplerDef {
                textureName: string = "DiffuseTexture"
                texturePath: string = "ASSETS/Maps/KitPieces/HA_Bilgewater/textures/bw_struc_roof_slaughter_01.dds"
                addressW: u32 = 1
            }
        }
        paramValues: list2[embed] = {
            StaticMaterialShaderParamDef {
                name: string = "TintColor"
                value: vec4 = { 0.5, 0.5, 0.5, 1 }
            }
            StaticMaterialShaderParamDef {
                name: string = "PitchFactor"
            }
        }
        techniques: list[embed] = {
            StaticMaterialTechniqueDef {
                name: string = "normal"
                passes: list[embed] = {
                    StaticMaterialPassDef {
                        shader: link = "Shaders/StaticMesh/DefaultEnv_Flat"
                    }
                }
            }
        }
    }
    "Maps/KitPieces/HA_Bilgewater/Materials/LM_ground_base_south_A1_inst" = StaticMaterialDef {
        name: string = "Maps/KitPieces/HA_Bilgewater/Materials/LM_ground_base_south_A1_inst"
        type: u32 = 0
        samplerValues: list2[embed] = {
            StaticMaterialShaderSamplerDef {
                textureName: string = "DiffuseTexture"
                texturePath: string = "ASSETS/Maps/KitPieces/HA_Bilgewater/textures/BW_ground_base_south_a.dds"
                addressW: u32 = 1
            }
        }
        paramValues: list2[embed] = {
            StaticMaterialShaderParamDef {
                name: string = "TintColor"
                value: vec4 = { 0.5, 0.5, 0.5, 1 }
            }
            StaticMaterialShaderParamDef {
                name: string = "PitchFactor"
            }
        }
        techniques: list[embed] = {
            StaticMaterialTechniqueDef {
                name: string = "normal"
                passes: list[embed] = {
                    StaticMaterialPassDef {
                        shader: link = "Shaders/StaticMesh/DefaultEnv_Flat"
                    }
                }
            }
        }
    }
    "Maps/KitPieces/HA_Bilgewater/Materials/BW_rope_lambert_inst" = StaticMaterialDef {
        name: string = "Maps/KitPieces/HA_Bilgewater/Materials/BW_rope_lambert_inst"
        type: u32 = 0
        samplerValues: list2[embed] = {
            StaticMaterialShaderSamplerDef {
                textureName: string = "DiffuseTexture"
                texturePath: string = "ASSETS/Maps/KitPieces/HA_Bilgewater/textures/props_ropes.dds"
                addressW: u32 = 1
            }
        }
        paramValues: list2[embed] = {
            StaticMaterialShaderParamDef {
                name: string = "AlphaTestValue"
                value: vec4 = { 0.899999976, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "TintColor"
                value: vec4 = { 0.5, 0.5, 0.5, 1 }
            }
        }
        techniques: list[embed] = {
            StaticMaterialTechniqueDef {
                name: string = "normal"
                passes: list[embed] = {
                    StaticMaterialPassDef {
                        shader: link = "Shaders/StaticMesh/DefaultEnv_Flat_AlphaTest"
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    }
                }
            }
        }
    }
    "Maps/KitPieces/HA_Bilgewater/Materials/lambert175174_inst" = StaticMaterialDef {
        name: string = "Maps/KitPieces/HA_Bilgewater/Materials/lambert175174_inst"
        type: u32 = 0
        samplerValues: list2[embed] = {
            StaticMaterialShaderSamplerDef {
                textureName: string = "DiffuseTexture"
                texturePath: string = "ASSETS/Maps/KitPieces/HA_Bilgewater/textures/props_cannonballpile.dds"
                addressW: u32 = 1
            }
        }
        paramValues: list2[embed] = {
            StaticMaterialShaderParamDef {
                name: string = "TintColor"
                value: vec4 = { 0.5, 0.5, 0.5, 1 }
            }
            StaticMaterialShaderParamDef {
                name: string = "PitchFactor"
            }
        }
        techniques: list[embed] = {
            StaticMaterialTechniqueDef {
                name: string = "normal"
                passes: list[embed] = {
                    StaticMaterialPassDef {
                        shader: link = "Shaders/StaticMesh/DefaultEnv_Flat"
                    }
                }
            }
        }
    }
    "Maps/KitPieces/HA_Bilgewater/Materials/house_tall_skinny_a7_inst" = StaticMaterialDef {
        name: string = "Maps/KitPieces/HA_Bilgewater/Materials/house_tall_skinny_a7_inst"
        type: u32 = 0
        samplerValues: list2[embed] = {
            StaticMaterialShaderSamplerDef {
                textureName: string = "DiffuseTexture"
                texturePath: string = "ASSETS/Maps/KitPieces/HA_Bilgewater/textures/house_tall_skinny_a.dds"
                addressW: u32 = 1
            }
        }
        paramValues: list2[embed] = {
            StaticMaterialShaderParamDef {
                name: string = "TintColor"
                value: vec4 = { 0.5, 0.5, 0.5, 1 }
            }
            StaticMaterialShaderParamDef {
                name: string = "PitchFactor"
            }
        }
        techniques: list[embed] = {
            StaticMaterialTechniqueDef {
                name: string = "normal"
                passes: list[embed] = {
                    StaticMaterialPassDef {
                        shader: link = "Shaders/StaticMesh/DefaultEnv_Flat"
                    }
                }
            }
        }
    }
    "Maps/KitPieces/HA_Bilgewater/Materials/lambert175303_inst" = StaticMaterialDef {
        name: string = "Maps/KitPieces/HA_Bilgewater/Materials/lambert175303_inst"
        type: u32 = 0
        samplerValues: list2[embed] = {
            StaticMaterialShaderSamplerDef {
                textureName: string = "DiffuseTexture"
                texturePath: string = "ASSETS/Maps/KitPieces/HA_Bilgewater/textures/bw_struc_roof_stripedtarp_01.dds"
                addressW: u32 = 1
            }
        }
        paramValues: list2[embed] = {
            StaticMaterialShaderParamDef {
                name: string = "TintColor"
                value: vec4 = { 0.5, 0.5, 0.5, 1 }
            }
            StaticMaterialShaderParamDef {
                name: string = "PitchFactor"
            }
        }
        techniques: list[embed] = {
            StaticMaterialTechniqueDef {
                name: string = "normal"
                passes: list[embed] = {
                    StaticMaterialPassDef {
                        shader: link = "Shaders/StaticMesh/DefaultEnv_Flat"
                    }
                }
            }
        }
    }
    "Maps/KitPieces/HA_Bilgewater/Materials/lambert175159_inst" = StaticMaterialDef {
        name: string = "Maps/KitPieces/HA_Bilgewater/Materials/lambert175159_inst"
        type: u32 = 0
        samplerValues: list2[embed] = {
            StaticMaterialShaderSamplerDef {
                textureName: string = "DiffuseTexture"
                texturePath: string = "ASSETS/Maps/KitPieces/HA_Bilgewater/textures/bw_prop_pulley_b.dds"
                addressW: u32 = 1
            }
        }
        paramValues: list2[embed] = {
            StaticMaterialShaderParamDef {
                name: string = "TintColor"
                value: vec4 = { 0.5, 0.5, 0.5, 1 }
            }
            StaticMaterialShaderParamDef {
                name: string = "PitchFactor"
            }
        }
        techniques: list[embed] = {
            StaticMaterialTechniqueDef {
                name: string = "normal"
                passes: list[embed] = {
                    StaticMaterialPassDef {
                        shader: link = "Shaders/StaticMesh/DefaultEnv_Flat"
                    }
                }
            }
        }
    }
    "Maps/KitPieces/HA_Bilgewater/Materials/lambert173875_inst" = StaticMaterialDef {
        name: string = "Maps/KitPieces/HA_Bilgewater/Materials/lambert173875_inst"
        type: u32 = 0
        samplerValues: list2[embed] = {
            StaticMaterialShaderSamplerDef {
                textureName: string = "DiffuseTexture"
                texturePath: string = "ASSETS/Maps/KitPieces/HA_Bilgewater/textures/bw_bridgefull_01.dds"
                addressW: u32 = 1
            }
        }
        paramValues: list2[embed] = {
            StaticMaterialShaderParamDef {
                name: string = "TintColor"
                value: vec4 = { 0.5, 0.5, 0.5, 1 }
            }
            StaticMaterialShaderParamDef {
                name: string = "PitchFactor"
            }
        }
        techniques: list[embed] = {
            StaticMaterialTechniqueDef {
                name: string = "normal"
                passes: list[embed] = {
                    StaticMaterialPassDef {
                        shader: link = "Shaders/StaticMesh/DefaultEnv_Flat"
                    }
                }
            }
        }
    }
    "Maps/KitPieces/HA_Bilgewater/Materials/lambert175298_inst" = StaticMaterialDef {
        name: string = "Maps/KitPieces/HA_Bilgewater/Materials/lambert175298_inst"
        type: u32 = 0
        samplerValues: list2[embed] = {
            StaticMaterialShaderSamplerDef {
                textureName: string = "DiffuseTexture"
                texturePath: string = "ASSETS/Maps/KitPieces/HA_Bilgewater/textures/house_tall_skinny_c1.dds"
                addressW: u32 = 1
            }
        }
        paramValues: list2[embed] = {
            StaticMaterialShaderParamDef {
                name: string = "TintColor"
                value: vec4 = { 0.5, 0.5, 0.5, 1 }
            }
            StaticMaterialShaderParamDef {
                name: string = "PitchFactor"
            }
        }
        techniques: list[embed] = {
            StaticMaterialTechniqueDef {
                name: string = "normal"
                passes: list[embed] = {
                    StaticMaterialPassDef {
                        shader: link = "Shaders/StaticMesh/DefaultEnv_Flat"
                    }
                }
            }
        }
    }
    "Maps/KitPieces/HA_Bilgewater/Materials/lambert175058_inst" = StaticMaterialDef {
        name: string = "Maps/KitPieces/HA_Bilgewater/Materials/lambert175058_inst"
        type: u32 = 0
        samplerValues: list2[embed] = {
            StaticMaterialShaderSamplerDef {
                textureName: string = "DiffuseTexture"
                texturePath: string = "ASSETS/Maps/KitPieces/HA_Bilgewater/textures/bw_base_shipwalls_a.dds"
                addressW: u32 = 1
            }
        }
        paramValues: list2[embed] = {
            StaticMaterialShaderParamDef {
                name: string = "TintColor"
                value: vec4 = { 0.5, 0.5, 0.5, 1 }
            }
            StaticMaterialShaderParamDef {
                name: string = "PitchFactor"
            }
        }
        techniques: list[embed] = {
            StaticMaterialTechniqueDef {
                name: string = "normal"
                passes: list[embed] = {
                    StaticMaterialPassDef {
                        shader: link = "Shaders/StaticMesh/DefaultEnv_Flat"
                    }
                }
            }
        }
    }
    "Maps/KitPieces/HA_Bilgewater/Materials/LM_ground_base_south_C1_inst" = StaticMaterialDef {
        name: string = "Maps/KitPieces/HA_Bilgewater/Materials/LM_ground_base_south_C1_inst"
        type: u32 = 0
        samplerValues: list2[embed] = {
            StaticMaterialShaderSamplerDef {
                textureName: string = "DiffuseTexture"
                texturePath: string = "ASSETS/Maps/KitPieces/HA_Bilgewater/textures/BW_ground_base_south_c.dds"
                addressW: u32 = 1
            }
        }
        paramValues: list2[embed] = {
            StaticMaterialShaderParamDef {
                name: string = "TintColor"
                value: vec4 = { 0.5, 0.5, 0.5, 1 }
            }
            StaticMaterialShaderParamDef {
                name: string = "PitchFactor"
            }
        }
        techniques: list[embed] = {
            StaticMaterialTechniqueDef {
                name: string = "normal"
                passes: list[embed] = {
                    StaticMaterialPassDef {
                        shader: link = "Shaders/StaticMesh/DefaultEnv_Flat"
                    }
                }
            }
        }
    }
    "Maps/KitPieces/HA_Bilgewater/Materials/lambert175056_inst" = StaticMaterialDef {
        name: string = "Maps/KitPieces/HA_Bilgewater/Materials/lambert175056_inst"
        type: u32 = 0
        samplerValues: list2[embed] = {
            StaticMaterialShaderSamplerDef {
                textureName: string = "DiffuseTexture"
                texturePath: string = "ASSETS/Maps/KitPieces/HA_Bilgewater/textures/bw_bridge_door_statue_a.dds"
                addressW: u32 = 1
            }
        }
        paramValues: list2[embed] = {
            StaticMaterialShaderParamDef {
                name: string = "TintColor"
                value: vec4 = { 0.5, 0.5, 0.5, 1 }
            }
            StaticMaterialShaderParamDef {
                name: string = "PitchFactor"
            }
        }
        techniques: list[embed] = {
            StaticMaterialTechniqueDef {
                name: string = "normal"
                passes: list[embed] = {
                    StaticMaterialPassDef {
                        shader: link = "Shaders/StaticMesh/DefaultEnv_Flat"
                    }
                }
            }
        }
    }
    "Maps/KitPieces/HA_Bilgewater/Materials/LM_Ground_Lane_C39_inst" = StaticMaterialDef {
        name: string = "Maps/KitPieces/HA_Bilgewater/Materials/LM_Ground_Lane_C39_inst"
        type: u32 = 0
        samplerValues: list2[embed] = {
            StaticMaterialShaderSamplerDef {
                textureName: string = "DiffuseTexture"
                texturePath: string = "ASSETS/Maps/KitPieces/HA_Bilgewater/textures/bw_ground_lane_c.dds"
                addressW: u32 = 1
            }
        }
        paramValues: list2[embed] = {
            StaticMaterialShaderParamDef {
                name: string = "TintColor"
                value: vec4 = { 0.5, 0.5, 0.5, 1 }
            }
            StaticMaterialShaderParamDef {
                name: string = "PitchFactor"
            }
        }
        techniques: list[embed] = {
            StaticMaterialTechniqueDef {
                name: string = "normal"
                passes: list[embed] = {
                    StaticMaterialPassDef {
                        shader: link = "Shaders/StaticMesh/DefaultEnv_Flat"
                    }
                }
            }
        }
    }
    "Maps/KitPieces/HA_Bilgewater/Materials/BW_struc_wall_plaster_0115_inst" = StaticMaterialDef {
        name: string = "Maps/KitPieces/HA_Bilgewater/Materials/BW_struc_wall_plaster_0115_inst"
        type: u32 = 0
        samplerValues: list2[embed] = {
            StaticMaterialShaderSamplerDef {
                textureName: string = "DiffuseTexture"
                texturePath: string = "ASSETS/Maps/KitPieces/HA_Bilgewater/textures/bw_struc_wall_plaster_01.dds"
                addressW: u32 = 1
            }
        }
        paramValues: list2[embed] = {
            StaticMaterialShaderParamDef {
                name: string = "TintColor"
                value: vec4 = { 0.5, 0.5, 0.5, 1 }
            }
            StaticMaterialShaderParamDef {
                name: string = "PitchFactor"
            }
        }
        techniques: list[embed] = {
            StaticMaterialTechniqueDef {
                name: string = "normal"
                passes: list[embed] = {
                    StaticMaterialPassDef {
                        shader: link = "Shaders/StaticMesh/DefaultEnv_Flat"
                    }
                }
            }
        }
    }
    "Maps/KitPieces/HA_Bilgewater/Materials/BW_Crates_01_inst" = StaticMaterialDef {
        name: string = "Maps/KitPieces/HA_Bilgewater/Materials/BW_Crates_01_inst"
        type: u32 = 0
        samplerValues: list2[embed] = {
            StaticMaterialShaderSamplerDef {
                textureName: string = "DiffuseTexture"
                texturePath: string = "ASSETS/Maps/KitPieces/HA_Bilgewater/textures/BW_Crates_01.dds"
                addressW: u32 = 1
            }
        }
        paramValues: list2[embed] = {
            StaticMaterialShaderParamDef {
                name: string = "TintColor"
                value: vec4 = { 0.5, 0.5, 0.5, 1 }
            }
            StaticMaterialShaderParamDef {
                name: string = "PitchFactor"
            }
        }
        techniques: list[embed] = {
            StaticMaterialTechniqueDef {
                name: string = "normal"
                passes: list[embed] = {
                    StaticMaterialPassDef {
                        shader: link = "Shaders/StaticMesh/DefaultEnv_Flat"
                    }
                }
            }
        }
    }
    "Maps/KitPieces/HA_Bilgewater/Materials/bw_ship_ribs40_inst" = StaticMaterialDef {
        name: string = "Maps/KitPieces/HA_Bilgewater/Materials/bw_ship_ribs40_inst"
        type: u32 = 0
        samplerValues: list2[embed] = {
            StaticMaterialShaderSamplerDef {
                textureName: string = "DiffuseTexture"
                texturePath: string = "ASSETS/Maps/KitPieces/HA_Bilgewater/textures/bw_ship_ribs.dds"
                addressW: u32 = 1
            }
        }
        paramValues: list2[embed] = {
            StaticMaterialShaderParamDef {
                name: string = "TintColor"
                value: vec4 = { 0.5, 0.5, 0.5, 1 }
            }
            StaticMaterialShaderParamDef {
                name: string = "PitchFactor"
            }
        }
        techniques: list[embed] = {
            StaticMaterialTechniqueDef {
                name: string = "normal"
                passes: list[embed] = {
                    StaticMaterialPassDef {
                        shader: link = "Shaders/StaticMesh/DefaultEnv_Flat"
                    }
                }
            }
        }
    }
    "Maps/KitPieces/HA_Bilgewater/Materials/hing_temp_lambert174705_inst" = StaticMaterialDef {
        name: string = "Maps/KitPieces/HA_Bilgewater/Materials/hing_temp_lambert174705_inst"
        type: u32 = 0
        samplerValues: list2[embed] = {
            StaticMaterialShaderSamplerDef {
                textureName: string = "DiffuseTexture"
                texturePath: string = "ASSETS/Maps/KitPieces/HA_Bilgewater/textures/bw_struc_roof_wood_01.dds"
                addressW: u32 = 1
            }
        }
        paramValues: list2[embed] = {
            StaticMaterialShaderParamDef {
                name: string = "TintColor"
                value: vec4 = { 0.5, 0.5, 0.5, 1 }
            }
            StaticMaterialShaderParamDef {
                name: string = "PitchFactor"
            }
        }
        techniques: list[embed] = {
            StaticMaterialTechniqueDef {
                name: string = "normal"
                passes: list[embed] = {
                    StaticMaterialPassDef {
                        shader: link = "Shaders/StaticMesh/DefaultEnv_Flat"
                    }
                }
            }
        }
    }
    "Maps/KitPieces/HA_Bilgewater/Materials/S_Base_Stern13_inst" = StaticMaterialDef {
        name: string = "Maps/KitPieces/HA_Bilgewater/Materials/S_Base_Stern13_inst"
        type: u32 = 0
        samplerValues: list2[embed] = {
            StaticMaterialShaderSamplerDef {
                textureName: string = "DiffuseTexture"
                texturePath: string = "ASSETS/Maps/KitPieces/HA_Bilgewater/textures/bw_s_base_stern.dds"
                addressW: u32 = 1
            }
        }
        paramValues: list2[embed] = {
            StaticMaterialShaderParamDef {
                name: string = "TintColor"
                value: vec4 = { 0.5, 0.5, 0.5, 1 }
            }
            StaticMaterialShaderParamDef {
                name: string = "PitchFactor"
            }
        }
        techniques: list[embed] = {
            StaticMaterialTechniqueDef {
                name: string = "normal"
                passes: list[embed] = {
                    StaticMaterialPassDef {
                        shader: link = "Shaders/StaticMesh/DefaultEnv_Flat"
                    }
                }
            }
        }
    }
    "Maps/KitPieces/HA_Bilgewater/Materials/LM_ground_base_south_D1_inst" = StaticMaterialDef {
        name: string = "Maps/KitPieces/HA_Bilgewater/Materials/LM_ground_base_south_D1_inst"
        type: u32 = 0
        samplerValues: list2[embed] = {
            StaticMaterialShaderSamplerDef {
                textureName: string = "DiffuseTexture"
                texturePath: string = "ASSETS/Maps/KitPieces/HA_Bilgewater/textures/BW_ground_base_south_d.dds"
                addressW: u32 = 1
            }
        }
        paramValues: list2[embed] = {
            StaticMaterialShaderParamDef {
                name: string = "TintColor"
                value: vec4 = { 0.5, 0.5, 0.5, 1 }
            }
            StaticMaterialShaderParamDef {
                name: string = "PitchFactor"
            }
        }
        techniques: list[embed] = {
            StaticMaterialTechniqueDef {
                name: string = "normal"
                passes: list[embed] = {
                    StaticMaterialPassDef {
                        shader: link = "Shaders/StaticMesh/DefaultEnv_Flat"
                    }
                }
            }
        }
    }
    "Maps/KitPieces/HA_Bilgewater/Materials/lambert175176_inst" = StaticMaterialDef {
        name: string = "Maps/KitPieces/HA_Bilgewater/Materials/lambert175176_inst"
        type: u32 = 0
        samplerValues: list2[embed] = {
            StaticMaterialShaderSamplerDef {
                textureName: string = "DiffuseTexture"
                texturePath: string = "ASSETS/Maps/KitPieces/HA_Bilgewater/textures/bw_windows_doors_01.dds"
                addressW: u32 = 1
            }
        }
        paramValues: list2[embed] = {
            StaticMaterialShaderParamDef {
                name: string = "TintColor"
                value: vec4 = { 0.5, 0.5, 0.5, 1 }
            }
            StaticMaterialShaderParamDef {
                name: string = "PitchFactor"
            }
        }
        techniques: list[embed] = {
            StaticMaterialTechniqueDef {
                name: string = "normal"
                passes: list[embed] = {
                    StaticMaterialPassDef {
                        shader: link = "Shaders/StaticMesh/DefaultEnv_Flat"
                    }
                }
            }
        }
    }
    "Maps/KitPieces/HA_Bilgewater/Materials/BW_vertical_bayside_lambert173063_inst" = StaticMaterialDef {
        name: string = "Maps/KitPieces/HA_Bilgewater/Materials/BW_vertical_bayside_lambert173063_inst"
        type: u32 = 0
        samplerValues: list2[embed] = {
            StaticMaterialShaderSamplerDef {
                textureName: string = "DiffuseTexture"
                texturePath: string = "ASSETS/Maps/KitPieces/HA_Bilgewater/textures/grey_temp.dds"
                addressW: u32 = 1
            }
        }
        paramValues: list2[embed] = {
            StaticMaterialShaderParamDef {
                name: string = "TintColor"
                value: vec4 = { 0.5, 0.5, 0.5, 1 }
            }
            StaticMaterialShaderParamDef {
                name: string = "PitchFactor"
            }
        }
        techniques: list[embed] = {
            StaticMaterialTechniqueDef {
                name: string = "normal"
                passes: list[embed] = {
                    StaticMaterialPassDef {
                        shader: link = "Shaders/StaticMesh/DefaultEnv_Flat"
                    }
                }
            }
        }
    }
    "Maps/KitPieces/HA_Bilgewater/Materials/LM_ground_base_north_D1_inst" = StaticMaterialDef {
        name: string = "Maps/KitPieces/HA_Bilgewater/Materials/LM_ground_base_north_D1_inst"
        type: u32 = 0
        samplerValues: list2[embed] = {
            StaticMaterialShaderSamplerDef {
                textureName: string = "DiffuseTexture"
                texturePath: string = "ASSETS/Maps/KitPieces/HA_Bilgewater/textures/bw_ground_base_north_d.dds"
                addressW: u32 = 1
            }
        }
        paramValues: list2[embed] = {
            StaticMaterialShaderParamDef {
                name: string = "TintColor"
                value: vec4 = { 0.5, 0.5, 0.5, 1 }
            }
            StaticMaterialShaderParamDef {
                name: string = "PitchFactor"
            }
        }
        techniques: list[embed] = {
            StaticMaterialTechniqueDef {
                name: string = "normal"
                passes: list[embed] = {
                    StaticMaterialPassDef {
                        shader: link = "Shaders/StaticMesh/DefaultEnv_Flat"
                    }
                }
            }
        }
    }
    "Maps/KitPieces/HA_Bilgewater/Materials/BW_Trash_031_inst" = StaticMaterialDef {
        name: string = "Maps/KitPieces/HA_Bilgewater/Materials/BW_Trash_031_inst"
        type: u32 = 0
        samplerValues: list2[embed] = {
            StaticMaterialShaderSamplerDef {
                textureName: string = "DiffuseTexture"
                texturePath: string = "ASSETS/Maps/KitPieces/HA_Bilgewater/textures/bw_trash_01.dds"
                addressW: u32 = 1
            }
        }
        paramValues: list2[embed] = {
            StaticMaterialShaderParamDef {
                name: string = "AlphaTestValue"
                value: vec4 = { 0.899999976, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "TintColor"
                value: vec4 = { 0.5, 0.5, 0.5, 1 }
            }
        }
        techniques: list[embed] = {
            StaticMaterialTechniqueDef {
                name: string = "normal"
                passes: list[embed] = {
                    StaticMaterialPassDef {
                        shader: link = "Shaders/StaticMesh/DefaultEnv_Flat_AlphaTest"
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    }
                }
            }
        }
    }
    "Maps/KitPieces/HA_Bilgewater/Materials/LM_LaneTrim_Wood3_inst" = StaticMaterialDef {
        name: string = "Maps/KitPieces/HA_Bilgewater/Materials/LM_LaneTrim_Wood3_inst"
        type: u32 = 0
        samplerValues: list2[embed] = {
            StaticMaterialShaderSamplerDef {
                textureName: string = "DiffuseTexture"
                texturePath: string = "ASSETS/Maps/KitPieces/HA_Bilgewater/textures/bw_bridge_railing_a.dds"
                addressW: u32 = 1
            }
        }
        paramValues: list2[embed] = {
            StaticMaterialShaderParamDef {
                name: string = "TintColor"
                value: vec4 = { 0.5, 0.5, 0.5, 1 }
            }
            StaticMaterialShaderParamDef {
                name: string = "PitchFactor"
            }
        }
        techniques: list[embed] = {
            StaticMaterialTechniqueDef {
                name: string = "normal"
                passes: list[embed] = {
                    StaticMaterialPassDef {
                        shader: link = "Shaders/StaticMesh/DefaultEnv_Flat"
                    }
                }
            }
        }
    }
    "Maps/KitPieces/HA_Bilgewater/Materials/bathysphere_south_periph_old_props_barrels_texture28_inst" = StaticMaterialDef {
        name: string = "Maps/KitPieces/HA_Bilgewater/Materials/bathysphere_south_periph_old_props_barrels_texture28_inst"
        type: u32 = 0
        samplerValues: list2[embed] = {
            StaticMaterialShaderSamplerDef {
                textureName: string = "DiffuseTexture"
                texturePath: string = "ASSETS/Maps/KitPieces/HA_Bilgewater/textures/props_barrels.dds"
                addressW: u32 = 1
            }
        }
        paramValues: list2[embed] = {
            StaticMaterialShaderParamDef {
                name: string = "TintColor"
                value: vec4 = { 0.5, 0.5, 0.5, 1 }
            }
            StaticMaterialShaderParamDef {
                name: string = "PitchFactor"
            }
        }
        techniques: list[embed] = {
            StaticMaterialTechniqueDef {
                name: string = "normal"
                passes: list[embed] = {
                    StaticMaterialPassDef {
                        shader: link = "Shaders/StaticMesh/DefaultEnv_Flat"
                    }
                }
            }
        }
    }
    "Maps/KitPieces/HA_Bilgewater/Materials/bridge_with_fishys_lambert172939_inst" = StaticMaterialDef {
        name: string = "Maps/KitPieces/HA_Bilgewater/Materials/bridge_with_fishys_lambert172939_inst"
        type: u32 = 0
        samplerValues: list2[embed] = {
            StaticMaterialShaderSamplerDef {
                textureName: string = "DiffuseTexture"
                texturePath: string = "ASSETS/Maps/KitPieces/HA_Bilgewater/textures/bw_struc_ancientstucco_tile_01.dds"
                addressW: u32 = 1
            }
        }
        paramValues: list2[embed] = {
            StaticMaterialShaderParamDef {
                name: string = "TintColor"
                value: vec4 = { 0.5, 0.5, 0.5, 1 }
            }
            StaticMaterialShaderParamDef {
                name: string = "PitchFactor"
            }
        }
        techniques: list[embed] = {
            StaticMaterialTechniqueDef {
                name: string = "normal"
                passes: list[embed] = {
                    StaticMaterialPassDef {
                        shader: link = "Shaders/StaticMesh/DefaultEnv_Flat"
                    }
                }
            }
        }
    }
    0xc3698a8c = StaticMaterialDef {
        name: string = "Maps/KitPieces/Howling_Abyss/Base/Materials/Default/BW_Brush"
        type: u32 = 0
        samplerValues: list2[embed] = {
            StaticMaterialShaderSamplerDef {
                textureName: string = "DiffuseTexture"
                texturePath: string = "ASSETS/Maps/KitPieces/Howling_Abyss/Base/Textures/BW_Brush.dds"
            }
        }
        paramValues: list2[embed] = {
            StaticMaterialShaderParamDef {
                name: string = "WaveFrequency"
                value: vec4 = { 1.5, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "WaveAmplitude"
                value: vec4 = { 8, 8, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "WaveOffset"
                value: vec4 = { 1, 1, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "VelocityStrength"
            }
            StaticMaterialShaderParamDef {
                name: string = "DistControlFactor"
                value: vec4 = { 200, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "MinDistance"
                value: vec4 = { 150, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "SpreadStrength"
                value: vec4 = { 1.5, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "SeeThroughAlphaMin"
                value: vec4 = { 0.25, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "SeeThroughAlphaMax"
                value: vec4 = { 1, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "SeeThroughRangeScale"
                value: vec4 = { 1, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "ScaleOutFactor"
                value: vec4 = { 10, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "ScaleInFactor"
                value: vec4 = { 0.200000003, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "TintColor"
                value: vec4 = { 0.636362255, 0.640817881, 0.722728312, 1 }
            }
        }
        switches: list2[embed] = {
            StaticMaterialSwitchDef {
                name: string = "USE_GRASS_TINT_MAP"
                on: bool = false
            }
        }
        shaderMacros: map[string,string] = {
            "NO_BAKED_LIGHTING" = "1"
            "DISABLE_DEPTH_FOG" = "1"
        }
        techniques: list[embed] = {
            StaticMaterialTechniqueDef {
                name: string = "normal"
                passes: list[embed] = {
                    StaticMaterialPassDef {
                        shader: link = "Shaders/StaticMesh/VertexDeform"
                        blendEnable: bool = true
                        srcColorBlendFactor: u32 = 6
                        srcAlphaBlendFactor: u32 = 6
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    }
                }
            }
        }
        childTechniques: list[embed] = {
            StaticMaterialChildTechniqueDef {
                name: string = "env_transition"
                parentName: string = "normal"
                shaderMacros: map[string,string] = {
                    "ENV_TRANSITION" = "1"
                }
            }
        }
    }
    "Maps/Particles/HA/Bilgewater/BW_Peref_Fog_Distant" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 0.0670000017
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 20
                }
                emitterName: string = "Basic"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Shared/Particles/BW_Peref_Fog_Distant.scb"
                    }
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    constantValue: vec4 = { 1, 0.964706004, 0.466666996, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            0.25
                            0.400000006
                            0.649999976
                            0.800000012
                            1
                        }
                        values: list[vec4] = {
                            { 1, 0.964706004, 0.466666996, 0 }
                            { 1, 0.964706004, 0.466666996, 0.449999988 }
                            { 1, 0.964706004, 0.466666996, 0.824999988 }
                            { 1, 0.964706004, 0.466666996, 0.654901981 }
                            { 1, 0.964706004, 0.466666996, 0.449999988 }
                            { 1, 0.964706004, 0.466666996, 0.200000003 }
                            { 1, 0.964706004, 0.466666996, 0 }
                        }
                    }
                }
                particleIsLocalOrientation: flag = true
                texture: string = "ASSETS/Shared/Particles/BW_Peref_Fog_Distant.dds"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { -0.0399999991, 0 }
                }
                birthUVOffset: embed = ValueVector2 {
                    constantValue: vec2 = { 1, 1 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 1, 1 }
                        }
                    }
                }
            }
        }
        particleName: string = "BW_Peref_Fog_Distant"
        particlePath: string = "Maps/Particles/HA/Bilgewater/BW_Peref_Fog_Distant"
    }
    "Maps/Particles/HA/Bilgewater/BW_Order_Inhibitor_runeTimer" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 320
                }
                isSingleParticle: flag = true
                emitterName: string = "runeTimeGlow"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                0x563d4a22: embed = ValueVector3 {
                    constantValue: vec3 = { 10, 50, -29 }
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Shared/Particles/BW_order_inhibitor_respawn_base.scb"
                    }
                }
                blendMode: u8 = 4
                pass: i16 = 3
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, -45, 0 }
                }
                isLocalOrientation: flag = false
                texture: string = "ASSETS/Shared/Particles/BW_Order_Inhibitor_RuneCountdown_glow.dds"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { -0.00300000003, 0 }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 0.25
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 6
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.800000012
                                    1.20000005
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            6
                        }
                    }
                }
                emitterName: string = "pulseTimer"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                0x563d4a22: embed = ValueVector3 {
                    constantValue: vec3 = { 10, 30, -29 }
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Shared/Particles/BW_order_inhibitor_respawn_base2.scb"
                    }
                }
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.329411775 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 0, 0, 1, -0 }
                            { 1, 1, 1, 1 }
                            { 0, 0, 1, -0 }
                        }
                    }
                }
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, -45, 0 }
                }
                isLocalOrientation: flag = false
                texture: string = "ASSETS/Shared/Particles/BW_Order_Inhibitor_RuneCountdown.dds"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0.00999999978, 0 }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 320
                }
                isSingleParticle: flag = true
                emitterName: string = "runeTimeGlow1"
                disabled: bool = true
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                0x563d4a22: embed = ValueVector3 {
                    constantValue: vec3 = { 10, 50, -29 }
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Shared/Particles/BW_order_inhibitor_respawn_base2.scb"
                    }
                }
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.149019614 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.0307100005
                            0.0748559982
                            0.150000006
                            0.165067002
                            0.261036009
                            0.309980989
                            0.356045991
                            0.394434005
                            0.448500007
                            0.449140012
                            0.512476027
                            0.539346993
                            0.600000024
                            0.642993987
                            0.722648978
                            0.800000012
                            0.850000024
                            0.904990017
                            0.952014983
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, -45, 0 }
                }
                isLocalOrientation: flag = false
                texture: string = "ASSETS/Shared/Particles/BW_Order_Inhibitor_RuneCountdown.dds"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { -0.0500000007, 0 }
                }
            }
        }
        particleName: string = "BW_Order_Inhibitor_runeTimer"
        particlePath: string = "Maps/Particles/HA/Bilgewater/BW_Order_Inhibitor_runeTimer"
        flags: u16 = 133
        assetRemappingTable: list[embed] = {
            VfxAssetRemap {
                oldAsset: hash = 0x2588d2d3
                newAsset: string = "ASSETS/Shared/Particles/BW_Chaos_Inhibitor_RuneCountdown.dds"
            }
            VfxAssetRemap {
                oldAsset: hash = 0x47c4e4cf
                newAsset: string = "ASSETS/Shared/Particles/BW_Chaos_Inhibitor_RuneCountdown_glow.dds"
            }
        }
    }
    "Maps/Particles/HA/Bilgewater/BW_Braziers_Fire" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 10
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.400000006
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.800000012
                                    1.39999998
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            0.400000006
                        }
                    }
                }
                particleLinger: option[f32] = {
                    2
                }
                emitterName: string = "Fire"
                birthAcceleration: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 300, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.100000001
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.800000012
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 300, 0 }
                        }
                    }
                }
                0x3bf0b4ed: pointer = 0x4f4e2ed7 {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 20, 10, 20 }
                        dynamics: pointer = VfxAnimatedVector3fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        -1
                                        1
                                    }
                                }
                                VfxProbabilityTableData {}
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        -1
                                        1
                                    }
                                }
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { 20, 10, 20 }
                            }
                        }
                    }
                    emitRotationAngles: list[embed] = {
                        ValueFloat {
                            constantValue: f32 = 45
                        }
                    }
                    emitRotationAxes: list[vec3] = {
                        { 0, 1.00000012, 0 }
                    }
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.300000012
                            0.800000012
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0.800000012 }
                            { 1, 0, 0, 0 }
                        }
                    }
                }
                pass: i16 = 2
                isUniformScale: flag = true
                isRandomStartFrame: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 0, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    360
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 1, 0, 0 }
                        }
                    }
                }
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 0, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    0
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 1, 0, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 45, 45, 45 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.800000012
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 45, 45, 45 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            1
                        }
                        values: list[vec3] = {
                            { 0.600000024, 0.600000024, 0.600000024 }
                            { 1, 1, 1 }
                            { 0.600000024, 0.600000024, 0.600000024 }
                        }
                    }
                }
                texture: string = "ASSETS/Shared/Particles/SRU_Brazier_Flame_Temp_01.DDS"
                numFrames: u16 = 8
                texDiv: vec2 = { 4, 2 }
                textureMult: pointer = 0xb097c1bd {
                    textureMult: string = "ASSETS/Shared/Particles/Env_MB_brazierFire_mult.dds"
                    texDivMult: vec2 = { 2, 2 }
                    birthUvScrollRateMult: embed = ValueVector2 {
                        constantValue: vec2 = { 0, -1.25 }
                    }
                    birthUVOffsetMult: embed = ValueVector2 {
                        constantValue: vec2 = { 1, 1 }
                        dynamics: pointer = VfxAnimatedVector2fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        1
                                        -1
                                    }
                                }
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        1
                                        -1
                                    }
                                }
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec2] = {
                                { 1, 1 }
                            }
                        }
                    }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 2.5
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            2.5
                        }
                    }
                }
                emitterName: string = "baseGlow"
                0x3bf0b4ed: pointer = 0xee39916f {
                    emitOffset: vec3 = { 0, -1, 0 }
                }
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                blendMode: u8 = 1
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 0.5, 0.5, 0.5 }
                            { 1, 0, 0, 0 }
                        }
                    }
                }
                pass: i16 = 1
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 90, 0, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 80, 80, 80 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 0.5, 0.5, 0.5 }
                            { 0.75, 0.75, 0.75 }
                        }
                    }
                }
                texture: string = "ASSETS/Shared/Particles/SRU_brazierFire_glow.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 5
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1.20000005
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            1.20000005
                        }
                    }
                }
                particleLinger: option[f32] = {
                    11.1999998
                }
                emitterName: string = "sparks"
                birthOrbitalVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0.400000006, 0.400000006, 0.400000006 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0.400000006, 0.400000006, 0.400000006 }
                        }
                    }
                }
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 250, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 250, 0 }
                        }
                    }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 0.600000024, 0.600000024, 0.600000024 }
                }
                0x3bf0b4ed: pointer = 0x4f4e2ed7 {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 25, -25, 25 }
                        dynamics: pointer = VfxAnimatedVector3fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        -1
                                        1
                                    }
                                }
                                VfxProbabilityTableData {}
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        -1
                                        1
                                    }
                                }
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { 25, -25, 25 }
                            }
                        }
                    }
                    emitRotationAngles: list[embed] = {
                        ValueFloat {
                            constantValue: f32 = 45
                        }
                    }
                    emitRotationAxes: list[vec3] = {
                        { 0, 1.00000012, 0 }
                    }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.300000012
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 0, 0, 0 }
                        }
                    }
                }
                pass: i16 = 1
                isDirectionOriented: flag = true
                isRandomStartFrame: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 20, 20, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1.5
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 20, 20, 0 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.300000012
                            1
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                            { 1, 0.5, 0 }
                            { 0.200000003, 0.200000003, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Shared/Particles/Env_MB_brazierFire_Ash_01.dds"
                numFrames: u16 = 4
                texDiv: vec2 = { 2, 2 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 3
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1.5
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.800000012
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            1.5
                        }
                    }
                }
                emitterName: string = "Smoke"
                disabled: bool = true
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 1, 0 }
                }
                birthAcceleration: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 150, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.800000012
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 150, 0 }
                        }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                0x3bf0b4ed: pointer = 0x4f4e2ed7 {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 30, 20, 10 }
                        dynamics: pointer = VfxAnimatedVector3fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        -1
                                        1
                                    }
                                }
                                VfxProbabilityTableData {}
                                VfxProbabilityTableData {}
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { 30, 20, 10 }
                            }
                        }
                    }
                    emitRotationAngles: list[embed] = {
                        ValueFloat {
                            constantValue: f32 = 25
                        }
                    }
                    emitRotationAxes: list[vec3] = {
                        { 0, 1.00000012, 0 }
                    }
                }
                0x563d4a22: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 30, 0 }
                }
                blendMode: u8 = 1
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.300000012
                            0.600000024
                            1
                        }
                        values: list[vec4] = {
                            { 0.713724971, 0.713724971, 0.160784006, 0 }
                            { 0.560783982, 0.552941024, 0.44313699, 0.294117987 }
                            { 0.49019599, 0.482353002, 0.36470601, 0.0941179991 }
                            { 0.0980390012, 0.164706007, 0.349020004, 0 }
                        }
                    }
                }
                disableBackfaceCull: bool = true
                isDirectionOriented: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 1, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    360
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 1, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 70, 70, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.800000012
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.800000012
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.800000012
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 70, 70, 0 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.400000006
                            1
                        }
                        values: list[vec3] = {
                            { 0.600000024, 0.200000003, 0.600000024 }
                            { 0.800000012, 0.800000012, 0.800000012 }
                            { 1, 1, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/Shared/Particles/Env_MB_brazier_dust.dds"
                uvMode: u8 = 2
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0, 0.400000006 }
                }
                textureMult: pointer = 0xb097c1bd {
                    textureMult: string = "ASSETS/Shared/Particles/Env_MB_brazier_dust_mult.dds"
                    birthUvScrollRateMult: embed = ValueVector2 {
                        constantValue: vec2 = { 0, 0.25 }
                    }
                    birthUVOffsetMult: embed = ValueVector2 {
                        constantValue: vec2 = { 1, 1 }
                        dynamics: pointer = VfxAnimatedVector2fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        1
                                        0
                                    }
                                }
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        1
                                        0
                                    }
                                }
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec2] = {
                                { 1, 1 }
                            }
                        }
                    }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 0.0799999982
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 22
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            22
                        }
                    }
                }
                particleLinger: option[f32] = {
                    32
                }
                emitterName: string = "FireGlow"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                0x3bf0b4ed: pointer = 0xee39916f {
                    emitOffset: vec3 = { 0, 65, 0 }
                }
                0x563d4a22: embed = ValueVector3 {
                    constantValue: vec3 = { 0, -20, 0 }
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.200000003
                            0.349999994
                            0.449999988
                            0.550000012
                            0.649999976
                            0.800000012
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 0.550000012 }
                            { 1, 1, 1, 0.850000024 }
                            { 1, 1, 1, 0.600000024 }
                            { 1, 1, 1, 0.600000024 }
                            { 1, 1, 1, 0.850000024 }
                            { 1, 1, 1, 0.550000012 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                pass: i16 = 5
                softParticleParams: pointer = VfxSoftParticleDefinitionData {
                    deltaIn: f32 = 50
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 151, 151, 151 }
                }
                texture: string = "ASSETS/Shared/Particles/SRU_Brazier_Glow_01.dds"
            }
        }
        particleName: string = "BW_Braziers_Fire"
        particlePath: string = "Maps/Particles/HA/Bilgewater/BW_Braziers_Fire"
        soundPersistentDefault: string = "Play_sfx_Env_Map14_Emitter_firebig"
    }
    "Maps/Particles/HA/Bilgewater/BW_AP_Chaos_Inhib_Rubble_Dust" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 5
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 2.5
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.800000012
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.600000024
                                    0.699999988
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            2.5
                        }
                    }
                }
                particleLinger: option[f32] = {
                    1
                }
                emitterName: string = "sparkles1"
                birthOrbitalVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, -1.5, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.899999976
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.100000001
                                    0.200000003
                                    0.5
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, -1.5, 0 }
                        }
                    }
                }
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 20, 0, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 20, 0, 0 }
                        }
                    }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 1, 1 }
                }
                worldAcceleration: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 0, -6, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, -6, 0 }
                        }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                0x3bf0b4ed: pointer = 0x3dbe415d {
                    radius: f32 = 75
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.737254918 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 0.516078413 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                pass: i16 = 7
                isUniformScale: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 1, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    360
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    360
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 1, 1, 0 }
                        }
                    }
                }
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 45, 45, 45 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.800000012
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    0.600000024
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 45, 45, 45 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.300000012
                            1
                        }
                        values: list[vec3] = {
                            { 0, 1, 1 }
                            { 1.39999998, 1, 1 }
                            { 0, 1, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/Shared/Particles/SRU_Chaos_brightSparks.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 3
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 6
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.400000006
                                }
                                keyValues: list[f32] = {
                                    0.300000012
                                    0.600000024
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            6
                        }
                    }
                }
                particleLinger: option[f32] = {
                    16
                }
                emitterName: string = "DustCloud"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 50, 1 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    5
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    5
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 1, 50, 1 }
                        }
                    }
                }
                velocity: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.449999988
                            1
                        }
                        values: list[vec3] = {
                            { -0, 0, 0 }
                            { -0, 0, -0 }
                            { -0, 0, -0 }
                        }
                    }
                }
                worldAcceleration: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 0, 30, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.5
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    0.400000006
                                    1.5
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 30, 0 }
                        }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                0x3bf0b4ed: pointer = 0x4f4e2ed7 {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 70, 75, 0 }
                        dynamics: pointer = VfxAnimatedVector3fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        -1
                                        1
                                    }
                                }
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        -1
                                        1
                                    }
                                }
                                VfxProbabilityTableData {}
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { 70, 75, 0 }
                            }
                        }
                    }
                }
                0x563d4a22: embed = ValueVector3 {
                    constantValue: vec3 = { 0, -100, 0 }
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.470588267, 0.313725501, 0.321568638, 0.800000072 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec4] = {
                            { 0.470588267, 0.313725501, 0.321568638, 0.800000072 }
                        }
                    }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.800000012 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.0500000007
                            0.550000012
                            0.699999988
                            0.850000024
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 0.800000012 }
                            { 1, 1, 1, 0.800000012 }
                            { 1, 1, 1, 0.320000023 }
                            { 1, 1, 1, 0.100000001 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                pass: i16 = -15
                particleIsLocalOrientation: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 0, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    360
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 1, 0, 0 }
                        }
                    }
                }
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 30, 0, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 30, 0, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 220, 220, 1 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.300000012
                                    0.5
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.300000012
                                    0.5
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 220, 220, 1 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.200000003
                            0.649999976
                            1
                        }
                        values: list[vec3] = {
                            { 0.300000012, 0.300000012, 1 }
                            { 0.5, 0.5, 1 }
                            { 1, 1, 1 }
                            { 1, 1, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/Shared/Particles/SRU_OrderTurret1_Rubble_dustCloud.dds"
                textureMult: pointer = 0xb097c1bd {
                    textureMult: string = "ASSETS/Shared/Particles/SRU_dustCloud_mult.dds"
                    birthUVOffsetMult: embed = ValueVector2 {
                        constantValue: vec2 = { 1, 1 }
                        dynamics: pointer = VfxAnimatedVector2fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        0
                                        1
                                    }
                                }
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        0
                                        1
                                    }
                                }
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec2] = {
                                { 1, 1 }
                            }
                        }
                    }
                }
            }
        }
        particleName: string = "BW_AP_Chaos_Inhib_Rubble_Dust"
        particlePath: string = "Maps/Particles/HA/Bilgewater/BW_AP_Chaos_Inhib_Rubble_Dust"
        flags: u16 = 135
        assetRemappingTable: list[embed] = {
            VfxAssetRemap {
                oldAsset: hash = 0x081f36ac
                newAsset: string = "ASSETS/Shared/Particles/SRU_Order_brightSparks.dds"
            }
        }
    }
    "Maps/Particles/HA/Bilgewater/BW_River_WaterEdge_08" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 0.400000006
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 5
                }
                emitterName: string = "Shore_02"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Shared/Particles/BW_River_WaterEdge_08.scb"
                    }
                }
                blendMode: u8 = 1
                color: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.889998019 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.25
                            0.800000012
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 0.645248592 }
                            { 1, 1, 1, 0.645248592 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                particleIsLocalOrientation: flag = true
                texture: string = "ASSETS/Shared/Particles/BW_River_WaterEdge_01.dds"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0.100000001, 0.100000001 }
                }
                birthUVOffset: embed = ValueVector2 {
                    constantValue: vec2 = { 1, 1 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    2
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    2
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 1, 1 }
                        }
                    }
                }
                textureMult: pointer = 0xb097c1bd {
                    textureMult: string = "ASSETS/Shared/Particles/BW_River_WaterEdge_01_Mult.dds"
                    birthUvScrollRateMult: embed = ValueVector2 {
                        constantValue: vec2 = { 0, 0.300000012 }
                    }
                    birthUVOffsetMult: embed = ValueVector2 {
                        constantValue: vec2 = { 1, 1 }
                        dynamics: pointer = VfxAnimatedVector2fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        0
                                        1
                                    }
                                }
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        0
                                        1
                                    }
                                }
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec2] = {
                                { 1, 1 }
                            }
                        }
                    }
                }
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.109999999
                rate: embed = ValueFloat {
                    constantValue: f32 = 0.600000024
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 4
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    1.5
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            4
                        }
                    }
                }
                emitterName: string = "Poolsplat_BorderV3"
                disabled: bool = true
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 10, 0 }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Shared/Particles/BW_River_WaterEdge_08.scb"
                    }
                }
                blendMode: u8 = 1
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.984314024, 1, 0.976471007, 0.506995976 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            0.330000013
                            0.800000012
                            1
                        }
                        values: list[vec4] = {
                            { 0.984314024, 1, 0.976471007, 0 }
                            { 0.984314024, 1, 0.976471007, 0 }
                            { 0.984314024, 1, 0.976471007, 0.506995976 }
                            { 0.984314024, 1, 0.976471007, 0.506995976 }
                            { 0.984314024, 1, 0.976471007, 0 }
                        }
                    }
                }
                alphaRef: u8 = 10
                isRandomStartFrame: flag = true
                texture: string = "ASSETS/Shared/Particles/BW_River_WaterEdge_01.dds"
                birthFrameRate: embed = ValueFloat {
                    constantValue: f32 = 0
                }
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0.0799999982, 0.100000001 }
                }
                textureMult: pointer = 0xb097c1bd {
                    textureMult: string = "ASSETS/Shared/Particles/BW_River_WaterEdge_01_Mult.dds"
                    birthUvScrollRateMult: embed = ValueVector2 {
                        constantValue: vec2 = { 1, 0.100000001 }
                    }
                    birthUVOffsetMult: embed = ValueVector2 {
                        constantValue: vec2 = { 1, 1 }
                        dynamics: pointer = VfxAnimatedVector2fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        0
                                        1
                                    }
                                }
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        0
                                        1
                                    }
                                }
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec2] = {
                                { 1, 1 }
                            }
                        }
                    }
                }
            }
        }
        visibilityRadius: f32 = 450
        particleName: string = "BW_River_WaterEdge_08"
        particlePath: string = "Maps/Particles/HA/Bilgewater/BW_River_WaterEdge_08"
        overrideScaleCap: option[f32] = {
            450
        }
        flags: u16 = 193
    }
    "Maps/Particles/HA/Bilgewater/BW_Audio_Emitter_ShipMast" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLinger: option[f32] = {
                    10
                }
                emitterName: string = "empty"
                particleColorTexture: string = "ASSETS/Shared/Particles/black.SKINS_Kindred_Skin34.dds"
                meshRenderFlags: u8 = 0
                isUniformScale: flag = true
                texture: string = "ASSETS/Shared/Particles/black.SKINS_Kindred_Skin34.dds"
            }
        }
        visibilityRadius: f32 = 1000
        particleName: string = "BW_Audio_Emitter_ShipMast"
        particlePath: string = "Maps/Particles/HA/Bilgewater/BW_Audio_Emitter_ShipMast"
        soundPersistentDefault: string = "Play_sfx_Env_Map14_Ambience_Emitter_ShipMast"
        flags: u16 = 229
    }
    "Maps/Particles/HA/Bilgewater/BW_Peref_WindowGlow_1" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1.5
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[f32] = {
                            0.75
                            7.5
                        }
                    }
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 7
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.800000012
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.400000006
                                    0.5
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            7
                        }
                    }
                }
                particleLinger: option[f32] = {
                    0.200000003
                }
                emitterName: string = "ambientGlow2"
                worldAcceleration: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 0, 0.25, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 0.25, 0 }
                        }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                emissionMeshScale: f32 = 1.29999995
                0x563d4a22: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 1, 0 }
                }
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                blendMode: u8 = 4
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.300000012
                            0.699999988
                            1
                        }
                        values: list[vec4] = {
                            { 1, 0.666666985, 0, 0 }
                            { 1, 0.819607973, 0.0823530033, 1 }
                            { 1, 0.774861991, 0.0582589991, 1 }
                            { 1, 0.666666985, 0, 0 }
                        }
                    }
                }
                pass: i16 = 1
                particleIsLocalOrientation: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 70, 70, 70 }
                }
                texture: string = "ASSETS/Shared/Particles/BW_Peref_WindowGlow_01.dds"
            }
        }
        particleName: string = "BW_Peref_WindowGlow_1"
        particlePath: string = "Maps/Particles/HA/Bilgewater/BW_Peref_WindowGlow_1"
        flags: u16 = 132
    }
    "Maps/Particles/HA/Bilgewater/BW_River_WaterEdge_01" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.109999999
                rate: embed = ValueFloat {
                    constantValue: f32 = 0.400000006
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 4
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    1.5
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            4
                        }
                    }
                }
                emitterName: string = "Poolsplat_BorderV2"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 10, 0 }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Shared/Particles/BW_River_WaterEdge_01.scb"
                    }
                }
                blendMode: u8 = 1
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.984314024, 1, 0.976471007, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            0.330000013
                            0.800000012
                            0.899999976
                            1
                        }
                        values: list[vec4] = {
                            { 0.984314024, 1, 0.976471007, 0 }
                            { 0.984314024, 1, 0.976471007, 0.400000006 }
                            { 0.984314024, 1, 0.976471007, 1 }
                            { 0.984314024, 1, 0.976471007, 1 }
                            { 0.984314024, 1, 0.976471007, 0.649999976 }
                            { 0.984314024, 1, 0.976471007, 0 }
                        }
                    }
                }
                alphaRef: u8 = 10
                isRandomStartFrame: flag = true
                texture: string = "ASSETS/Shared/Particles/BW_River_WaterEdge_01.dds"
                birthFrameRate: embed = ValueFloat {
                    constantValue: f32 = 0
                }
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0.0500000007, -0.0199999996 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1.5
                                    2
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1.5
                                    2
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 0.0500000007, -0.0199999996 }
                        }
                    }
                }
                birthUVOffset: embed = ValueVector2 {
                    constantValue: vec2 = { 1, 1 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 1, 1 }
                        }
                    }
                }
                textureMult: pointer = 0xb097c1bd {
                    textureMult: string = "ASSETS/Shared/Particles/BW_River_WaterEdge_01_Mult.dds"
                    birthUvScrollRateMult: embed = ValueVector2 {
                        constantValue: vec2 = { -0.100000001, -0.100000001 }
                    }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 0.400000006
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 2
                }
                emitterName: string = "Shore_02"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Shared/Particles/BW_River_WaterEdge_01.scb"
                    }
                }
                blendMode: u8 = 1
                color: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.383993 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.800000012
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 0.222872227 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                particleIsLocalOrientation: flag = true
                texture: string = "ASSETS/Shared/Particles/BW_River_WaterEdge_01.dds"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { -0.0299999993, 0.00999999978 }
                }
                textureMult: pointer = 0xb097c1bd {
                    textureMult: string = "ASSETS/Shared/Particles/BW_River_WaterEdge_01_Mult.dds"
                    birthUvScrollRateMult: embed = ValueVector2 {
                        constantValue: vec2 = { -0.100000001, -0.129999995 }
                    }
                }
            }
        }
        visibilityRadius: f32 = 350
        particleName: string = "BW_River_WaterEdge_01"
        particlePath: string = "Maps/Particles/HA/Bilgewater/BW_River_WaterEdge_01"
        overrideScaleCap: option[f32] = {
            350
        }
        flags: u16 = 193
    }
    "Maps/Particles/HA/Bilgewater/BW_River_WaterEdge_02" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.109999999
                rate: embed = ValueFloat {
                    constantValue: f32 = 0.400000006
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 4
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    1.5
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            4
                        }
                    }
                }
                emitterName: string = "Poolsplat_BorderV2"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 10, 0 }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Shared/Particles/BW_River_WaterEdge_02.scb"
                    }
                }
                blendMode: u8 = 1
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.984314024, 1, 0.976471007, 0.506995976 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            0.330000013
                            0.800000012
                            0.899999976
                            1
                        }
                        values: list[vec4] = {
                            { 0.984314024, 1, 0.976471007, 0 }
                            { 0.984314024, 1, 0.976471007, 0.202798396 }
                            { 0.984314024, 1, 0.976471007, 0.330052376 }
                            { 0.984314024, 1, 0.976471007, 0.334005386 }
                            { 0.984314024, 1, 0.976471007, 0.329547375 }
                            { 0.984314024, 1, 0.976471007, 0 }
                        }
                    }
                }
                alphaRef: u8 = 10
                isRandomStartFrame: flag = true
                texture: string = "ASSETS/Shared/Particles/BW_River_WaterEdge_01.dds"
                birthFrameRate: embed = ValueFloat {
                    constantValue: f32 = 0
                }
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0.0500000007, -0.0199999996 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1.5
                                    2
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1.5
                                    2
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 0.0500000007, -0.0199999996 }
                        }
                    }
                }
                birthUVOffset: embed = ValueVector2 {
                    constantValue: vec2 = { 1, 1 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 1, 1 }
                        }
                    }
                }
                textureMult: pointer = 0xb097c1bd {
                    textureMult: string = "ASSETS/Shared/Particles/BW_River_WaterEdge_01_Mult.dds"
                    birthUvScrollRateMult: embed = ValueVector2 {
                        constantValue: vec2 = { -0.100000001, -0.100000001 }
                    }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 0.400000006
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 2
                }
                emitterName: string = "Shore_02"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Shared/Particles/BW_River_WaterEdge_02.scb"
                    }
                }
                blendMode: u8 = 1
                color: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.383993 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.800000012
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 0.222872227 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                particleIsLocalOrientation: flag = true
                texture: string = "ASSETS/Shared/Particles/BW_River_WaterEdge_01.dds"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { -0.0299999993, 0.00999999978 }
                }
                textureMult: pointer = 0xb097c1bd {
                    textureMult: string = "ASSETS/Shared/Particles/BW_River_WaterEdge_01_Mult.dds"
                    birthUvScrollRateMult: embed = ValueVector2 {
                        constantValue: vec2 = { -0.100000001, -0.129999995 }
                    }
                }
            }
        }
        visibilityRadius: f32 = 350
        particleName: string = "BW_River_WaterEdge_02"
        particlePath: string = "Maps/Particles/HA/Bilgewater/BW_River_WaterEdge_02"
        overrideScaleCap: option[f32] = {
            350
        }
        flags: u16 = 193
    }
    "Maps/Particles/HA/Bilgewater/BW_River_WaterEdge_03" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.109999999
                rate: embed = ValueFloat {
                    constantValue: f32 = 0.5
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 4
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    1.5
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            4
                        }
                    }
                }
                emitterName: string = "Poolsplat_BorderV2"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 10, 0 }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Shared/Particles/BW_River_WaterEdge_03.scb"
                    }
                }
                blendMode: u8 = 1
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.984314024, 1, 0.976471007, 0.370000988 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            0.330000013
                            0.800000012
                            1
                        }
                        values: list[vec4] = {
                            { 0.984314024, 1, 0.976471007, 0 }
                            { 0.984314024, 1, 0.976471007, 0 }
                            { 0.984314024, 1, 0.976471007, 0.370000988 }
                            { 0.984314024, 1, 0.976471007, 0.370000988 }
                            { 0.984314024, 1, 0.976471007, 0 }
                        }
                    }
                }
                alphaRef: u8 = 10
                isRandomStartFrame: flag = true
                texture: string = "ASSETS/Shared/Particles/BW_River_WaterEdge_01.dds"
                birthFrameRate: embed = ValueFloat {
                    constantValue: f32 = 0
                }
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0.0500000007, -0.0199999996 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1.5
                                    2
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1.5
                                    2
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 0.0500000007, -0.0199999996 }
                        }
                    }
                }
                textureMult: pointer = 0xb097c1bd {
                    textureMult: string = "ASSETS/Shared/Particles/BW_River_WaterEdge_01_Mult.dds"
                    birthUvScrollRateMult: embed = ValueVector2 {
                        constantValue: vec2 = { -0.100000001, -0.100000001 }
                    }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 0.400000006
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 2
                }
                emitterName: string = "Shore_02"
                disabled: bool = true
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Shared/Particles/BW_River_WaterEdge_03.scb"
                    }
                }
                blendMode: u8 = 1
                color: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.383993 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.800000012
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 0.222872227 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                particleIsLocalOrientation: flag = true
                texture: string = "ASSETS/Shared/Particles/BW_River_WaterEdge_01.dds"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { -0.0299999993, 0.00999999978 }
                }
                textureMult: pointer = 0xb097c1bd {
                    textureMult: string = "ASSETS/Shared/Particles/BW_River_WaterEdge_01_Mult.dds"
                    birthUvScrollRateMult: embed = ValueVector2 {
                        constantValue: vec2 = { -0.100000001, -0.129999995 }
                    }
                }
            }
        }
        particleName: string = "BW_River_WaterEdge_03"
        particlePath: string = "Maps/Particles/HA/Bilgewater/BW_River_WaterEdge_03"
        flags: u16 = 193
    }
    "Maps/Particles/HA/Bilgewater/BW_River_WaterEdge_04" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.109999999
                rate: embed = ValueFloat {
                    constantValue: f32 = 0.449999988
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 4
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    1.5
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            4
                        }
                    }
                }
                emitterName: string = "Poolsplat_BorderV2"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 10, 0 }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Shared/Particles/BW_River_WaterEdge_04.scb"
                    }
                }
                blendMode: u8 = 1
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.984314024, 1, 0.976471007, 0.534004986 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            0.330000013
                            0.800000012
                            1
                        }
                        values: list[vec4] = {
                            { 0.984314024, 1, 0.976471007, 0 }
                            { 0.984314024, 1, 0.976471007, 0 }
                            { 0.984314024, 1, 0.976471007, 0.534004986 }
                            { 0.984314024, 1, 0.976471007, 0.534004986 }
                            { 0.984314024, 1, 0.976471007, 0 }
                        }
                    }
                }
                alphaRef: u8 = 10
                isRandomStartFrame: flag = true
                texture: string = "ASSETS/Shared/Particles/BW_River_WaterEdge_01.dds"
                birthFrameRate: embed = ValueFloat {
                    constantValue: f32 = 0
                }
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0.0500000007, 0.0199999996 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1.5
                                    2
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1.5
                                    2
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 0.0500000007, 0.0199999996 }
                        }
                    }
                }
                textureMult: pointer = 0xb097c1bd {
                    textureMult: string = "ASSETS/Shared/Particles/BW_River_WaterEdge_01_Mult.dds"
                    birthUvScrollRateMult: embed = ValueVector2 {
                        constantValue: vec2 = { -0.100000001, -0.100000001 }
                    }
                    birthUVOffsetMult: embed = ValueVector2 {
                        constantValue: vec2 = { 1, 1 }
                        dynamics: pointer = VfxAnimatedVector2fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        0
                                        1
                                    }
                                }
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        0
                                        1
                                    }
                                }
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec2] = {
                                { 1, 1 }
                            }
                        }
                    }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 0.449999988
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 2
                }
                emitterName: string = "Shore_02"
                disabled: bool = true
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Shared/Particles/BW_River_WaterEdge_04.scb"
                    }
                }
                blendMode: u8 = 1
                color: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.562004983 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.800000012
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 0.326191634 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                particleIsLocalOrientation: flag = true
                texture: string = "ASSETS/Shared/Particles/BW_River_WaterEdge_01.dds"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { -0.0299999993, 0.00999999978 }
                }
                textureMult: pointer = 0xb097c1bd {
                    textureMult: string = "ASSETS/Shared/Particles/BW_River_WaterEdge_01_Mult.dds"
                    birthUvScrollRateMult: embed = ValueVector2 {
                        constantValue: vec2 = { 0, -0.129999995 }
                    }
                    birthUVOffsetMult: embed = ValueVector2 {
                        constantValue: vec2 = { 1, 1 }
                        dynamics: pointer = VfxAnimatedVector2fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        0
                                        1
                                    }
                                }
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        0
                                        1
                                    }
                                }
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec2] = {
                                { 1, 1 }
                            }
                        }
                    }
                }
            }
        }
        particleName: string = "BW_River_WaterEdge_04"
        particlePath: string = "Maps/Particles/HA/Bilgewater/BW_River_WaterEdge_04"
        flags: u16 = 197
    }
    "Maps/Particles/HA/Bilgewater/BW_River_WaterEdge_05" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.109999999
                rate: embed = ValueFloat {
                    constantValue: f32 = 0.400000006
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 4
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    1.5
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            4
                        }
                    }
                }
                emitterName: string = "Poolsplat_BorderV2"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 10, 0 }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Shared/Particles/BW_River_WaterEdge_05.scb"
                    }
                }
                blendMode: u8 = 1
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.984314024, 1, 0.976471007, 0.506995976 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            0.330000013
                            0.800000012
                            1
                        }
                        values: list[vec4] = {
                            { 0.984314024, 1, 0.976471007, 0 }
                            { 0.984314024, 1, 0.976471007, 0 }
                            { 0.984314024, 1, 0.976471007, 0.506995976 }
                            { 0.984314024, 1, 0.976471007, 0.506995976 }
                            { 0.984314024, 1, 0.976471007, 0 }
                        }
                    }
                }
                alphaRef: u8 = 10
                isRandomStartFrame: flag = true
                texture: string = "ASSETS/Shared/Particles/BW_River_WaterEdge_01.dds"
                birthFrameRate: embed = ValueFloat {
                    constantValue: f32 = 0
                }
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0.0500000007, -0.0500000007 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1.5
                                    2
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1.5
                                    2
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 0.0500000007, -0.0500000007 }
                        }
                    }
                }
                textureMult: pointer = 0xb097c1bd {
                    textureMult: string = "ASSETS/Shared/Particles/BW_River_WaterEdge_01_Mult.dds"
                    texDivMult: vec2 = { 2, 1 }
                    birthUvScrollRateMult: embed = ValueVector2 {
                        constantValue: vec2 = { -0.0199999996, -0.100000001 }
                    }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 0.5
                }
                emitterName: string = "Shore_02"
                disabled: bool = true
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Shared/Particles/BW_River_WaterEdge_05.scb"
                    }
                }
                blendMode: u8 = 1
                color: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.917998016 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.800000012
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 0.532812476 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                particleIsLocalOrientation: flag = true
                texture: string = "ASSETS/Shared/Particles/BW_River_WaterEdge_01.dds"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { -0.0500000007, -0.0500000007 }
                }
                birthUVOffset: embed = ValueVector2 {
                    constantValue: vec2 = { 1, 1 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    2
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    2
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 1, 1 }
                        }
                    }
                }
                textureMult: pointer = 0xb097c1bd {
                    textureMult: string = "ASSETS/Shared/Particles/BW_River_WaterEdge_01_Mult.dds"
                    birthUvScrollRateMult: embed = ValueVector2 {
                        constantValue: vec2 = { -0.00499999989, 0 }
                    }
                    birthUVOffsetMult: embed = ValueVector2 {
                        constantValue: vec2 = { 1, 1 }
                        dynamics: pointer = VfxAnimatedVector2fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        0
                                        1
                                    }
                                }
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        0
                                        1
                                    }
                                }
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec2] = {
                                { 1, 1 }
                            }
                        }
                    }
                }
            }
        }
        visibilityRadius: f32 = 1650
        particleName: string = "BW_River_WaterEdge_05"
        particlePath: string = "Maps/Particles/HA/Bilgewater/BW_River_WaterEdge_05"
        overrideScaleCap: option[f32] = {
            450
        }
        flags: u16 = 193
    }
    "Maps/Particles/HA/Bilgewater/BW_River_WaterEdge_06" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.109999999
                rate: embed = ValueFloat {
                    constantValue: f32 = 0.400000006
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 4
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    1.5
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            4
                        }
                    }
                }
                emitterName: string = "Poolsplat_BorderV2"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 10, 0 }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Shared/Particles/BW_River_WaterEdge_06.scb"
                    }
                }
                blendMode: u8 = 1
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.984314024, 1, 0.976471007, 0.355993003 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            0.330000013
                            0.800000012
                            1
                        }
                        values: list[vec4] = {
                            { 0.984314024, 1, 0.976471007, 0 }
                            { 0.984314024, 1, 0.976471007, 0 }
                            { 0.984314024, 1, 0.976471007, 0.355993003 }
                            { 0.984314024, 1, 0.976471007, 0.355993003 }
                            { 0.984314024, 1, 0.976471007, 0 }
                        }
                    }
                }
                alphaRef: u8 = 10
                isRandomStartFrame: flag = true
                texture: string = "ASSETS/Shared/Particles/BW_River_WaterEdge_01.dds"
                birthFrameRate: embed = ValueFloat {
                    constantValue: f32 = 0
                }
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0.0500000007, -0.0199999996 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1.5
                                    2
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1.5
                                    2
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 0.0500000007, -0.0199999996 }
                        }
                    }
                }
                textureMult: pointer = 0xb097c1bd {
                    textureMult: string = "ASSETS/Shared/Particles/BW_River_WaterEdge_01_Mult.dds"
                    birthUvScrollRateMult: embed = ValueVector2 {
                        constantValue: vec2 = { -0.100000001, -0.100000001 }
                    }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 0.400000006
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 2
                }
                emitterName: string = "Shore_02"
                disabled: bool = true
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Shared/Particles/BW_River_WaterEdge_06.scb"
                    }
                }
                blendMode: u8 = 1
                color: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.396993995 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.800000012
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 0.230418101 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                particleIsLocalOrientation: flag = true
                texture: string = "ASSETS/Shared/Particles/BW_River_WaterEdge_01.dds"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { -0.0299999993, 0.00999999978 }
                }
                textureMult: pointer = 0xb097c1bd {
                    textureMult: string = "ASSETS/Shared/Particles/BW_River_WaterEdge_01_Mult.dds"
                    birthUvScrollRateMult: embed = ValueVector2 {
                        constantValue: vec2 = { 0, 0.129999995 }
                    }
                }
            }
        }
        visibilityRadius: f32 = 450
        particleName: string = "BW_River_WaterEdge_06"
        particlePath: string = "Maps/Particles/HA/Bilgewater/BW_River_WaterEdge_06"
        overrideScaleCap: option[f32] = {
            450
        }
        flags: u16 = 193
    }
    "Maps/Particles/HA/Bilgewater/BW_River_WaterEdge_07" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.109999999
                rate: embed = ValueFloat {
                    constantValue: f32 = 0.400000006
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 4
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    1.5
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            4
                        }
                    }
                }
                emitterName: string = "Poolsplat_BorderV2"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 10, 0 }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Shared/Particles/BW_River_WaterEdge_07.scb"
                    }
                }
                blendMode: u8 = 1
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.984314024, 1, 0.976471007, 0.506995976 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            0.330000013
                            0.800000012
                            1
                        }
                        values: list[vec4] = {
                            { 0.984314024, 1, 0.976471007, 0 }
                            { 0.984314024, 1, 0.976471007, 0 }
                            { 0.984314024, 1, 0.976471007, 0.506995976 }
                            { 0.984314024, 1, 0.976471007, 0.506995976 }
                            { 0.984314024, 1, 0.976471007, 0 }
                        }
                    }
                }
                alphaRef: u8 = 10
                isRandomStartFrame: flag = true
                texture: string = "ASSETS/Shared/Particles/BW_River_WaterEdge_01.dds"
                birthFrameRate: embed = ValueFloat {
                    constantValue: f32 = 0
                }
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0.0500000007, 0.0500000007 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1.5
                                    2
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1.5
                                    2
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 0.0500000007, 0.0500000007 }
                        }
                    }
                }
                textureMult: pointer = 0xb097c1bd {
                    textureMult: string = "ASSETS/Shared/Particles/BW_River_WaterEdge_01_Mult.dds"
                    texDivMult: vec2 = { 1, 3 }
                    birthUvScrollRateMult: embed = ValueVector2 {
                        constantValue: vec2 = { 0.200000003, -0.300000012 }
                    }
                    birthUVOffsetMult: embed = ValueVector2 {
                        constantValue: vec2 = { 1, 1 }
                        dynamics: pointer = VfxAnimatedVector2fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        0
                                        1
                                    }
                                }
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        0
                                        1
                                    }
                                }
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec2] = {
                                { 1, 1 }
                            }
                        }
                    }
                }
            }
        }
        particleName: string = "BW_River_WaterEdge_07"
        particlePath: string = "Maps/Particles/HA/Bilgewater/BW_River_WaterEdge_07"
        flags: u16 = 193
    }
    "Maps/Particles/HA/Bilgewater/BW_Peref_Godrays" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 0.300000012
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 7
                }
                particleLinger: option[f32] = {
                    17
                }
                emitterName: string = "Godray"
                0x3bf0b4ed: pointer = 0x4f4e2ed7 {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 1, 1, 1 }
                        dynamics: pointer = VfxAnimatedVector3fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        500
                                        -100
                                    }
                                }
                                VfxProbabilityTableData {}
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        -300
                                        300
                                    }
                                }
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { 1, 1, 1 }
                            }
                        }
                    }
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Shared/Particles/sru_peref_godrays_01.scb"
                    }
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.200000003
                            0.5
                            0.800000012
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 0.649999976 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0.649999976 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                pass: i16 = 100
                particleIsLocalOrientation: flag = true
                isUniformScale: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 2, 1 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.899999976
                                    2
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 1, 2, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/Shared/Particles/SRU_Peref_GodRays.dds"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0.25, 0 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.5
                                    0.511099994
                                    1
                                }
                                keyValues: list[f32] = {
                                    -0.0500000007
                                    -0.0500000007
                                    0.0500000007
                                    0.0500000007
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 0.25, 0 }
                        }
                    }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    1.5
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            1
                        }
                    }
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 6
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            6
                        }
                    }
                }
                particleLinger: option[f32] = {
                    16
                }
                emitterName: string = "dust_Parts2"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 20, -35, -10 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 20, -35, -10 }
                        }
                    }
                }
                acceleration: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 1, 1 }
                }
                worldAcceleration: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 1, 1, 1 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -115
                                    115
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    900
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -115
                                    115
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                            0.100000001
                            0.25
                            0.395161003
                            0.567972004
                            0.775115013
                            0.899538994
                            1
                        }
                        values: list[vec3] = {
                            { 100, 0, 100 }
                            { -100, 0, -100 }
                            { 100, 0, 100 }
                            { -100, 0, -100 }
                            { 100, 0, 100 }
                            { -100, 0, -100 }
                            { 100, 0, 100 }
                            { -100, 0, -100 }
                        }
                    }
                }
                0x3bf0b4ed: pointer = 0x4f4e2ed7 {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 350, 1000, 300 }
                        dynamics: pointer = VfxAnimatedVector3fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        1
                                        -1
                                    }
                                }
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        -1
                                        1
                                    }
                                }
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        -1
                                        1
                                    }
                                }
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { 350, 1000, 300 }
                            }
                        }
                    }
                    emitRotationAngles: list[embed] = {
                        ValueFloat {
                            constantValue: f32 = 45
                        }
                        ValueFloat {
                            constantValue: f32 = 18.5
                        }
                    }
                    emitRotationAxes: list[vec3] = {
                        { 0, 0, 1.00000012 }
                        { 1.00000012, 0, 0 }
                    }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.300000012
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 0.5 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                isUniformScale: flag = true
                isRandomStartFrame: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 20, 90 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 5, 5, 5 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.800000012
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.300000012
                                    0.300000012
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 5, 5, 5 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            0.500999987
                            0.800000012
                            1
                        }
                        values: list[vec3] = {
                            { 1, 1, 1 }
                            { 2, 2, 2 }
                            { 1, 1, 1 }
                            { 1, 1, 1 }
                            { 0, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Shared/Particles/SRU_Godray_Dustparticles_01.dds"
                numFrames: u16 = 4
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 2
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    1.5
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            2
                        }
                    }
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 6
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.600000024
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.100000001
                                    1
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            6
                        }
                    }
                }
                particleLinger: option[f32] = {
                    16
                }
                fieldCollectionDefinition: pointer = VfxFieldCollectionDefinitionData {
                    fieldNoiseDefinitions: list[embed] = {
                        VfxFieldNoiseDefinitionData {
                            radius: embed = ValueFloat {
                                constantValue: f32 = 250
                            }
                            frequency: embed = ValueFloat {
                                constantValue: f32 = 2
                            }
                            velocityDelta: embed = ValueFloat {
                                constantValue: f32 = 50
                            }
                            axisFraction: vec3 = { 2, 1, 0 }
                        }
                    }
                }
                emitterName: string = "dust_Parts"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 20, -35, -10 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.899999976
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                    222
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 20, -35, -10 }
                        }
                    }
                }
                0x3bf0b4ed: pointer = 0x4f4e2ed7 {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 350, 1000, 300 }
                        dynamics: pointer = VfxAnimatedVector3fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        1
                                        -1
                                    }
                                }
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        -1
                                        1
                                    }
                                }
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        -1
                                        1
                                    }
                                }
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { 350, 1000, 300 }
                            }
                        }
                    }
                    emitRotationAngles: list[embed] = {
                        ValueFloat {
                            constantValue: f32 = 45
                        }
                        ValueFloat {
                            constantValue: f32 = 18.5
                        }
                    }
                    emitRotationAxes: list[vec3] = {
                        { 0, 0, 1.00000012 }
                        { 1.00000012, 0, 0 }
                    }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.300000012
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 0.5 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                isUniformScale: flag = true
                isRandomStartFrame: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 20, 90 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 5, 5, 5 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.800000012
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.300000012
                                    0.300000012
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 5, 5, 5 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            0.500999987
                            0.800000012
                            1
                        }
                        values: list[vec3] = {
                            { 1, 1, 1 }
                            { 2, 2, 2 }
                            { 1, 1, 1 }
                            { 1, 1, 1 }
                            { 0, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Shared/Particles/SRU_Godray_Dustparticles_01.dds"
                numFrames: u16 = 4
            }
        }
        visibilityRadius: f32 = 1000
        particleName: string = "BW_Peref_Godrays"
        particlePath: string = "Maps/Particles/HA/Bilgewater/BW_Peref_Godrays"
        flags: u16 = 197
    }
    "Maps/Particles/HA/Bilgewater/BW_AP_Chaos_Inhib_Idle_2" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 2
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 2
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.800000012
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            2
                        }
                    }
                }
                particleLinger: option[f32] = {
                    12
                }
                emitterName: string = "pitGlow1"
                worldAcceleration: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 0, 30, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    2
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 30, 0 }
                        }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                0x3bf0b4ed: pointer = 0xee39916f {
                    emitOffset: vec3 = { 0, 100, 0 }
                }
                primitive: pointer = VfxPrimitiveRay {}
                blendMode: u8 = 1
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.300000012
                            0.649999976
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, -0 }
                        }
                    }
                }
                particleIsLocalOrientation: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 90, 0, 0 }
                }
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 5, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 600, 800, 1 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 600, 800, 1 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.26730001
                            0.449999988
                            0.75
                            1
                        }
                        values: list[vec3] = {
                            { 1, 0.5, 1 }
                            { 1, 1, 1 }
                            { 1, 1.35000002, 1 }
                            { 1, 2.17499995, 1 }
                            { 1, 3.375, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/Shared/Particles/SRUAP_ChaosInhibitor_respawn_glow.dds"
            }
        }
        particleName: string = "BW_AP_Chaos_Inhib_Idle_2"
        particlePath: string = "Maps/Particles/HA/Bilgewater/BW_AP_Chaos_Inhib_Idle_2"
        assetRemappingTable: list[embed] = {
            VfxAssetRemap {
                oldAsset: hash = 0x98452aad
                newAsset: string = "ASSETS/Shared/Particles/SRUAP_ChaosInhibitor_respawn_glow.dds"
            }
        }
    }
    "Maps/Particles/HA/Bilgewater/BW_AP_Order_Inhib_Idle2" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 2
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 2
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.800000012
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            2
                        }
                    }
                }
                particleLinger: option[f32] = {
                    12
                }
                emitterName: string = "pitGlow1"
                worldAcceleration: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 0, 30, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    2
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 30, 0 }
                        }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                0x3bf0b4ed: pointer = 0xee39916f {
                    emitOffset: vec3 = { 0, 100, 0 }
                }
                primitive: pointer = VfxPrimitiveRay {}
                blendMode: u8 = 1
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.300000012
                            0.649999976
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, -0 }
                        }
                    }
                }
                particleIsLocalOrientation: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 90, 0, 0 }
                }
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 5, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 600, 800, 1 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 600, 800, 1 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.26730001
                            0.449999988
                            0.75
                            1
                        }
                        values: list[vec3] = {
                            { 1, 0.5, 1 }
                            { 1, 1, 1 }
                            { 1, 1.35000002, 1 }
                            { 1, 2.17499995, 1 }
                            { 1, 3.375, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/Shared/Particles/BW_AP_Order_Inhib_Pitglow.dds"
            }
        }
        particleName: string = "BW_AP_Order_Inhib_Idle2"
        particlePath: string = "Maps/Particles/HA/Bilgewater/BW_AP_Order_Inhib_Idle2"
        assetRemappingTable: list[embed] = {
            VfxAssetRemap {
                oldAsset: hash = 0xb57899c8
                newAsset: string = "ASSETS/Shared/Particles/SRUAP_ChaosInhibitor_respawn_glow.dds"
            }
        }
    }
    "Maps/Particles/HA/Bilgewater/BW_Audio_Emitter_Fire" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLinger: option[f32] = {
                    10
                }
                emitterName: string = "empty"
                particleColorTexture: string = "ASSETS/Shared/Particles/black.SKINS_Kindred_Skin34.dds"
                meshRenderFlags: u8 = 0
                isUniformScale: flag = true
                texture: string = "ASSETS/Shared/Particles/black.SKINS_Kindred_Skin34.dds"
            }
        }
        particleName: string = "BW_Audio_Emitter_Fire"
        particlePath: string = "Maps/Particles/HA/Bilgewater/BW_Audio_Emitter_Fire"
        soundPersistentDefault: string = "Play_sfx_Env_Map14_Ambience_Emitter_Fire"
        flags: u16 = 229
    }
    "Maps/Particles/HA/Bilgewater/BW_Order_StartingPlatform_GodRays" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 0.100000001
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 16
                }
                particleLinger: option[f32] = {
                    26
                }
                emitterName: string = "Godray"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                0x3bf0b4ed: pointer = 0x4f4e2ed7 {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 1, 1, 1 }
                        dynamics: pointer = VfxAnimatedVector3fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        450
                                        -170
                                    }
                                }
                                VfxProbabilityTableData {}
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        -260
                                        260
                                    }
                                }
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { 1, 1, 1 }
                            }
                        }
                    }
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Shared/Particles/BW_StartingPlatform_Godrays.scb"
                    }
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.200000003
                            0.5
                            0.800000012
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 0.649999976 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0.649999976 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                pass: i16 = 100
                isUniformScale: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 2, 1 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.899999976
                                    2
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 1, 2, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/Shared/Particles/BW_StartingPlatform_Godrays.dds"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0.25, 0 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.5
                                    0.511099994
                                    1
                                }
                                keyValues: list[f32] = {
                                    -0.0500000007
                                    -0.0500000007
                                    0.0500000007
                                    0.0500000007
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 0.25, 0 }
                        }
                    }
                }
            }
        }
        visibilityRadius: f32 = 1000
        particleName: string = "BW_Order_StartingPlatform_GodRays"
        particlePath: string = "Maps/Particles/HA/Bilgewater/BW_Order_StartingPlatform_GodRays"
        flags: u16 = 197
    }
    "Maps/Particles/HA/Bilgewater/BW_Motes_WespFly_01" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 3
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 6
                }
                particleLinger: option[f32] = {
                    16
                }
                emitterName: string = "wispFly"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                emissionMeshScale: f32 = 15
                emissionMeshName: string = "ASSETS/Shared/Particles/sru_emitter_plane.scb"
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Shared/Particles/sru_order_wispfly.scb"
                    }
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.200000003 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 0.200000003 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                isUniformScale: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 225, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 1.20000005, 1.20000005, 1.20000005 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.800000012
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.699999988
                                    0.800000012
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 1.20000005, 1.20000005, 1.20000005 }
                        }
                    }
                }
                texture: string = "ASSETS/Shared/Particles/BW_WispFly_01.dds"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0.150000006, 0 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.800000012
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                    5
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 0.150000006, 0 }
                        }
                    }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 10
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 20
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            20
                        }
                    }
                }
                particleLinger: option[f32] = {
                    30
                }
                emitterName: string = "motes"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 0, 1 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.699999988
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    0
                                    40
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.699999988
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    0
                                    40
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 1, 0, 1 }
                        }
                    }
                }
                worldAcceleration: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 2, 0, 2 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 2, 0, 2 }
                        }
                    }
                }
                emissionMeshScale: f32 = 15
                emissionMeshName: string = "ASSETS/Shared/Particles/sru_emitter_plane.scb"
                0x3bf0b4ed: pointer = 0x4f4e2ed7 {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 0, 500, 0 }
                    }
                    emitRotationAngles: list[embed] = {
                        ValueFloat {
                            constantValue: f32 = 1
                            dynamics: pointer = VfxAnimatedFloatVariableData {
                                probabilityTables: list[pointer] = {
                                    VfxProbabilityTableData {
                                        keyTimes: list[f32] = {
                                            0
                                            1
                                        }
                                        keyValues: list[f32] = {
                                            0
                                            360
                                        }
                                    }
                                }
                                times: list[f32] = {
                                    0
                                }
                                values: list[f32] = {
                                    1
                                }
                            }
                        }
                        ValueFloat {
                            constantValue: f32 = 1
                            dynamics: pointer = VfxAnimatedFloatVariableData {
                                probabilityTables: list[pointer] = {
                                    VfxProbabilityTableData {
                                        keyTimes: list[f32] = {
                                            0
                                            1
                                        }
                                        keyValues: list[f32] = {
                                            0
                                            360
                                        }
                                    }
                                }
                                times: list[f32] = {
                                    0
                                }
                                values: list[f32] = {
                                    1
                                }
                            }
                        }
                    }
                    emitRotationAxes: list[vec3] = {
                        { 1.00000012, 0, 0 }
                        { 0, 1.00000012, 0 }
                    }
                }
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.149019614 }
                }
                isUniformScale: flag = true
                isRandomStartFrame: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 25, 25, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 25, 25, 0 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec3] = {
                            { 0, 1, 1 }
                            { 1, 1, 1 }
                            { 0, 1, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/Shared/Particles/BW_Motes_01.dds"
                numFrames: u16 = 4
                texDiv: vec2 = { 2, 2 }
            }
        }
        visibilityRadius: f32 = 500
        particleName: string = "BW_Motes_WespFly_01"
        particlePath: string = "Maps/Particles/HA/Bilgewater/BW_Motes_WespFly_01"
    }
    "Maps/Particles/HA/Bilgewater/BW_Order_Rain_and_Puddels" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 290
                }
                particleLinger: option[f32] = {
                    30
                }
                isSingleParticle: flag = true
                emitterLinger: option[f32] = {
                    30
                }
                emitterName: string = "GroundPuddles"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Shared/Particles/BW_Order_RainPuddles.scb"
                    }
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.698039234 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            0.899999976
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                pass: i16 = -32768
                particleIsLocalOrientation: flag = true
                texture: string = "ASSETS/Shared/Particles/bw_Order_Puddles.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 50
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1.20000005
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            1.20000005
                        }
                    }
                }
                particleLinger: option[f32] = {
                    11.1999998
                }
                emitterName: string = "RainDrops"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { -120, -6000, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.400000006
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { -120, -6000, 0 }
                        }
                    }
                }
                emissionMeshName: string = "ASSETS/Shared/Particles/BW_RainImmter.scb"
                0x3bf0b4ed: pointer = 0x4f4e2ed7 {
                    emitRotationAngles: list[embed] = {
                        ValueFloat {
                            constantValue: f32 = 20
                        }
                    }
                    emitRotationAxes: list[vec3] = {
                        { 0, 0, 1.00000012 }
                    }
                }
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                blendMode: u8 = 1
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.300000012
                            1
                        }
                        values: list[vec4] = {
                            { 0, 0.835294008, 0.670588017, 0 }
                            { 0.00392200006, 0.941175997, 0.756862998, 0.300000012 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                isDirectionOriented: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 90, 90 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 15, 90, 0 }
                }
                texture: string = "ASSETS/Shared/Particles/SRU_EastJungle_RainFalling_01.StrawberryRebuild.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 13
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    3
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            13
                        }
                    }
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.5
                }
                emitterName: string = "GlowRocks_BearRock"
                importance: u8 = 0
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                emissionMeshName: string = "ASSETS/Shared/Particles/BW_Order_RainPuddles.scb"
                0x3bf0b4ed: pointer = 0x4f4e2ed7 {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 10, 0, 10 }
                        dynamics: pointer = VfxAnimatedVector3fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        -8
                                        8
                                    }
                                }
                                VfxProbabilityTableData {}
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        -8
                                        8
                                    }
                                }
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { 10, 0, 10 }
                            }
                        }
                    }
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Shared/Particles/sru_raindrops_01.StrawberryRebuild.scb"
                    }
                }
                blendMode: u8 = 1
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            0.75
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 0.815702021 }
                            { 1, 1, 1, 0.807797015 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                particleIsLocalOrientation: flag = true
                isUniformScale: flag = true
                isRandomStartFrame: flag = true
                uvScrollClamp: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 1.39999998, 1.39999998, 1.39999998 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    0.5
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 1.39999998, 1.39999998, 1.39999998 }
                        }
                    }
                }
                texture: string = "ASSETS/Shared/Particles/BW_RainDrops_01.dds"
                numFrames: u16 = 2
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { -2, 0 }
                }
                texAddressModeBase: u8 = 2
                texDiv: vec2 = { 1, 2 }
            }
        }
        visibilityRadius: f32 = 11150
        particleName: string = "BW_Order_Rain_and_Puddels"
        particlePath: string = "Maps/Particles/HA/Bilgewater/BW_Order_Rain_and_Puddels"
    }
    "Maps/Particles/HA/Bilgewater/BW_Audio_Emitter_PubSouth" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLinger: option[f32] = {
                    10
                }
                emitterName: string = "empty"
                particleColorTexture: string = "ASSETS/Shared/Particles/black.SKINS_Kindred_Skin34.dds"
                meshRenderFlags: u8 = 0
                isUniformScale: flag = true
                texture: string = "ASSETS/Shared/Particles/black.SKINS_Kindred_Skin34.dds"
            }
        }
        visibilityRadius: f32 = 2000
        particleName: string = "BW_Audio_Emitter_PubSouth"
        particlePath: string = "Maps/Particles/HA/Bilgewater/BW_Audio_Emitter_PubSouth"
        soundPersistentDefault: string = "Play_sfx_Env_Map14_Ambience_Emitter_PubSouth"
        flags: u16 = 229
    }
    "Maps/Particles/HA/Bilgewater/BW_Audio_Emitter_Pub" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLinger: option[f32] = {
                    10
                }
                emitterName: string = "empty"
                particleColorTexture: string = "ASSETS/Shared/Particles/black.SKINS_Kindred_Skin34.dds"
                meshRenderFlags: u8 = 0
                isUniformScale: flag = true
                texture: string = "ASSETS/Shared/Particles/black.SKINS_Kindred_Skin34.dds"
            }
        }
        visibilityRadius: f32 = 2000
        particleName: string = "BW_Audio_Emitter_Pub"
        particlePath: string = "Maps/Particles/HA/Bilgewater/BW_Audio_Emitter_Pub"
        soundPersistentDefault: string = "Play_sfx_Env_Map14_Ambience_Emitter_PubBrew"
        flags: u16 = 229
    }
    "Maps/Particles/HA/Bilgewater/BW_Cannon_Smoke" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = -1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = -1
                }
                isSingleParticle: flag = true
                emitterName: string = "Brazier_Blueside_Smoke2"
                importance: u8 = 0
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                0x3bf0b4ed: pointer = 0xee39916f {
                    emitOffset: vec3 = { -10, 40, -40 }
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Shared/Particles/BW_Smoke_Cannon.scb"
                    }
                }
                blendMode: u8 = 1
                disableBackfaceCull: bool = true
                particleIsLocalOrientation: flag = true
                isLocalOrientation: flag = false
                texture: string = "ASSETS/Shared/Particles/BW_Smoke_02.dds"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0.0189999994, 0.100000001 }
                }
                textureMult: pointer = 0xb097c1bd {
                    textureMult: string = "ASSETS/Shared/Particles/SRU_Braziers_Smoke_Blueside_01_Mult.dds"
                    birthUvScrollRateMult: embed = ValueVector2 {
                        constantValue: vec2 = { 0.0250000004, 0 }
                    }
                }
            }
        }
        particleName: string = "BW_Cannon_Smoke"
        particlePath: string = "Maps/Particles/HA/Bilgewater/BW_Cannon_Smoke"
    }
    "Maps/Particles/HA/Bilgewater/BW_RiverPlain_01" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 0.200000003
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 10
                }
                emitterName: string = "WaterPlaneNorth1"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Shared/Particles/BW_RiverPlain.scb"
                    }
                }
                blendMode: u8 = 1
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                pass: i16 = -10000
                particleIsLocalOrientation: flag = true
                texture: string = "ASSETS/Shared/Particles/BW_RiverPlaine_01.dds"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0, 0.0439999998 }
                }
                textureMult: pointer = 0xb097c1bd {
                    birthUvScrollRateMult: embed = ValueVector2 {
                        constantValue: vec2 = { 0, 0.0350000001 }
                    }
                }
            }
        }
        visibilityRadius: f32 = 5000
        particleName: string = "BW_RiverPlain_01"
        particlePath: string = "Maps/Particles/HA/Bilgewater/BW_RiverPlain_01"
    }
    "Maps/Particles/HA/Bilgewater/BW_Audio_Emitter_PubShark" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLinger: option[f32] = {
                    10
                }
                emitterName: string = "empty"
                particleColorTexture: string = "ASSETS/Shared/Particles/black.SKINS_Kindred_Skin34.dds"
                meshRenderFlags: u8 = 0
                isUniformScale: flag = true
                texture: string = "ASSETS/Shared/Particles/black.SKINS_Kindred_Skin34.dds"
            }
        }
        visibilityRadius: f32 = 2000
        particleName: string = "BW_Audio_Emitter_PubShark"
        particlePath: string = "Maps/Particles/HA/Bilgewater/BW_Audio_Emitter_PubShark"
        soundPersistentDefault: string = "Play_sfx_Env_Map14_Ambience_Emitter_PubShark"
        flags: u16 = 229
    }
    "Maps/Particles/HA/Bilgewater/BW_AP_Order_Inhib_Rubble_Dust" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 3
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 2.5
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.800000012
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.600000024
                                    0.699999988
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            2.5
                        }
                    }
                }
                particleLinger: option[f32] = {
                    1
                }
                emitterName: string = "sparkles1"
                birthOrbitalVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, -1.5, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.899999976
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.100000001
                                    0.200000003
                                    0.5
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, -1.5, 0 }
                        }
                    }
                }
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 20, 0, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 20, 0, 0 }
                        }
                    }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 1, 1 }
                }
                drag: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 1, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.600000024
                            1
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                            { 0, -0.875, 0 }
                            { 0, -2.20000005, 0 }
                        }
                    }
                }
                worldAcceleration: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 0, 30, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 30, 0 }
                        }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                0x3bf0b4ed: pointer = 0x3dbe415d {
                    radius: f32 = 75
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.737254918 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 0.516078413 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                isUniformScale: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 1, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    360
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    360
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 1, 1, 0 }
                        }
                    }
                }
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 45, 45, 45 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.800000012
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.300000012
                                    0.400000006
                                    0.800000012
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 45, 45, 45 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.300000012
                            1
                        }
                        values: list[vec3] = {
                            { 0, 1, 1 }
                            { 1, 1, 1 }
                            { 0, 1, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/Shared/Particles/SRU_brightSparks_teal.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.800000012
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            1
                        }
                    }
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 4
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.800000012
                                    1.39999998
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            4
                        }
                    }
                }
                particleLinger: option[f32] = {
                    14
                }
                emitterName: string = "pitGlow"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 35, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 35, 0 }
                        }
                    }
                }
                worldAcceleration: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 0, 15, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 15, 0 }
                        }
                    }
                }
                0x3bf0b4ed: pointer = 0x4f4e2ed7 {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 3, 3, 3 }
                        dynamics: pointer = VfxAnimatedVector3fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        -30
                                        30
                                    }
                                }
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        -30
                                        30
                                    }
                                }
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        -10
                                        10
                                    }
                                }
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { 3, 3, 3 }
                            }
                        }
                    }
                }
                0x563d4a22: embed = ValueVector3 {
                    constantValue: vec3 = { 0, -100, 0 }
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.737254918 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            0.25
                            0.349999994
                            0.5
                            0.75
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, -0 }
                            { 1, 1, 1, 0.387058794 }
                            { 1, 1, 1, 0.571372509 }
                            { 1, 1, 1, 0.534509838 }
                            { 1, 1, 1, 0.368627459 }
                            { 1, 1, 1, 0.20274511 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                pass: i16 = -100
                isUniformScale: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { -90, 45, 90 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { -90, 45, 90 }
                        }
                    }
                }
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { -10, 0, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -10
                                    10
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { -10, 0, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 150, 150, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.800000012
                                    0.899999976
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.800000012
                                    0.899999976
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 150, 150, 0 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { -0, -0, 0 }
                            { 0.949999988, 0.975000024, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Shared/Particles/SRUAP_ChaosTurret1_ambientGlow.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 3
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 6
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.400000006
                                }
                                keyValues: list[f32] = {
                                    0.300000012
                                    0.600000024
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            6
                        }
                    }
                }
                particleLinger: option[f32] = {
                    16
                }
                emitterName: string = "DustCloud"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 50, 1 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    5
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    5
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 1, 50, 1 }
                        }
                    }
                }
                velocity: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.449999988
                            1
                        }
                        values: list[vec3] = {
                            { -0, 0, 0 }
                            { -0, 0, -0 }
                            { -0, 0, -0 }
                        }
                    }
                }
                worldAcceleration: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 0, 30, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.5
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    0.400000006
                                    1.5
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 30, 0 }
                        }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                0x3bf0b4ed: pointer = 0x4f4e2ed7 {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 75, 75, 0 }
                        dynamics: pointer = VfxAnimatedVector3fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        -1
                                        1
                                    }
                                }
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        -1
                                        1
                                    }
                                }
                                VfxProbabilityTableData {}
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { 75, 75, 0 }
                            }
                        }
                    }
                }
                0x563d4a22: embed = ValueVector3 {
                    constantValue: vec3 = { 0, -200, 0 }
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.615686297, 0.615686297, 0.615686297, 0.800000012 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec4] = {
                            { 0.615686297, 0.615686297, 0.615686297, 0.800000012 }
                        }
                    }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.0500000007
                            0.550000012
                            0.699999988
                            0.850000024
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0.400000006 }
                            { 1, 1, 1, 0.125 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                pass: i16 = -15
                particleIsLocalOrientation: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 0, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    360
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 1, 0, 0 }
                        }
                    }
                }
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 30, 0, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 30, 0, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 240, 240, 1 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.300000012
                                    0.5
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.300000012
                                    0.5
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 240, 240, 1 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.200000003
                            0.649999976
                            1
                        }
                        values: list[vec3] = {
                            { 0.300000012, 0.300000012, 1 }
                            { 0.5, 0.5, 1 }
                            { 1, 1, 1 }
                            { 1, 1, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/Shared/Particles/SRU_OrderTurret1_Rubble_dustCloud.dds"
                textureMult: pointer = 0xb097c1bd {
                    textureMult: string = "ASSETS/Shared/Particles/SRU_dustCloud_mult.dds"
                    birthUVOffsetMult: embed = ValueVector2 {
                        constantValue: vec2 = { 1, 1 }
                        dynamics: pointer = VfxAnimatedVector2fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        0
                                        1
                                    }
                                }
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        0
                                        1
                                    }
                                }
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec2] = {
                                { 1, 1 }
                            }
                        }
                    }
                }
            }
        }
        particleName: string = "BW_AP_Order_Inhib_Rubble_Dust"
        particlePath: string = "Maps/Particles/HA/Bilgewater/BW_AP_Order_Inhib_Rubble_Dust"
        flags: u16 = 135
        assetRemappingTable: list[embed] = {
            VfxAssetRemap {
                oldAsset: hash = 0xfd39f12e
                newAsset: string = "ASSETS/Shared/Particles/SRU_Chaos_brightSparks.dds"
            }
        }
    }
    "Maps/Particles/HA/Bilgewater/BW_Chimney_Smoke" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 4
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 2
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    0.800000012
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            2
                        }
                    }
                }
                particleLinger: option[f32] = {
                    12
                }
                emitterName: string = "sparks"
                birthOrbitalVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0.200000003, 0.200000003, 0.200000003 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0.200000003, 0.200000003, 0.200000003 }
                        }
                    }
                }
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 20, 500, 20 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.25
                                    2
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 20, 500, 20 }
                        }
                    }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 0.400000006, 0.400000006, 0.400000006 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -0.5
                                    3
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                            0.300000012
                            0.699999988
                            1
                        }
                        values: list[vec3] = {
                            { 0.400000006, 0.400000006, 0.400000006 }
                            { 0.160000011, 0.160000011, 0.160000011 }
                            { 0.0800000057, 0.0800000057, 0.0800000057 }
                            { 0, 0, 0 }
                        }
                    }
                }
                birthAcceleration: embed = ValueVector3 {
                    constantValue: vec3 = { 30, 30, 30 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.699999988
                                    0.709999979
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.300000012
                                    0.300000012
                                    1
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.300000012
                                    0.310000002
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    -0.5
                                    2
                                    2.5
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.699999988
                                    0.709999979
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.300000012
                                    0.300000012
                                    1
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 30, 30, 30 }
                        }
                    }
                }
                velocity: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 1, 1 }
                }
                drag: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 1, 1 }
                }
                worldAcceleration: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 1, 1, 1 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.300000012
                            1
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                            { 0, 0, 0 }
                            { 2111, 0, 2111 }
                        }
                    }
                }
                0x3bf0b4ed: pointer = 0x4f4e2ed7 {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 15, 0, 15 }
                        dynamics: pointer = VfxAnimatedVector3fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        -1
                                        1
                                    }
                                }
                                VfxProbabilityTableData {}
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        -1
                                        1
                                    }
                                }
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { 15, 0, 15 }
                            }
                        }
                    }
                    emitRotationAngles: list[embed] = {
                        ValueFloat {
                            constantValue: f32 = 45
                        }
                        ValueFloat {
                            constantValue: f32 = 360
                            dynamics: pointer = VfxAnimatedFloatVariableData {
                                probabilityTables: list[pointer] = {
                                    VfxProbabilityTableData {
                                        keyTimes: list[f32] = {
                                            0
                                            1
                                        }
                                        keyValues: list[f32] = {
                                            0
                                            1
                                        }
                                    }
                                }
                                times: list[f32] = {
                                    0
                                }
                                values: list[f32] = {
                                    360
                                }
                            }
                        }
                    }
                    emitRotationAxes: list[vec3] = {
                        { 0, 1.00000012, 0 }
                        { 0, 1.00000012, 0 }
                    }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.300000012
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 0, 0, 0 }
                        }
                    }
                }
                pass: i16 = 1
                isDirectionOriented: flag = true
                isRandomStartFrame: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 40, 40, 40 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                            { 0, 0, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 15, 15, 15 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.699999988
                                    1.5
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.699999988
                                    1.5
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 15, 15, 15 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.300000012
                            1
                        }
                        values: list[vec3] = {
                            { 0.300000012, 0.300000012, 0.300000012 }
                            { 1, 0.5, 0 }
                            { 0.200000003, 0.200000003, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Shared/Particles/SRU_Chaos_shopkeeper_Ash_orange.dds"
                numFrames: u16 = 4
                texDiv: vec2 = { 2, 2 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = -1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = -1
                }
                isSingleParticle: flag = true
                emitterName: string = "Brazier_Blueside_Smoke1"
                importance: u8 = 0
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                0x3bf0b4ed: pointer = 0xee39916f {
                    emitOffset: vec3 = { -10, 40, -40 }
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Shared/Particles/BW_Smoke_Chimney_01.scb"
                    }
                }
                blendMode: u8 = 1
                disableBackfaceCull: bool = true
                isLocalOrientation: flag = false
                texture: string = "ASSETS/Shared/Particles/SRU_Braziers_Smoke_Blueside_01.dds"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0.0189999994, 0.150000006 }
                }
                textureMult: pointer = 0xb097c1bd {
                    textureMult: string = "ASSETS/Shared/Particles/SRU_Braziers_Smoke_Blueside_01_Mult.dds"
                    birthUvScrollRateMult: embed = ValueVector2 {
                        constantValue: vec2 = { 0.0250000004, 0 }
                    }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 0.300000012
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 4
                }
                particleLinger: option[f32] = {
                    14
                }
                emitterName: string = "Basic"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                0x3bf0b4ed: pointer = 0x4f4e2ed7 {
                    emitRotationAngles: list[embed] = {
                        ValueFloat {
                            constantValue: f32 = 1
                            dynamics: pointer = VfxAnimatedFloatVariableData {
                                probabilityTables: list[pointer] = {
                                    VfxProbabilityTableData {
                                        keyTimes: list[f32] = {
                                            0
                                            1
                                        }
                                        keyValues: list[f32] = {
                                            0
                                            360
                                        }
                                    }
                                }
                                times: list[f32] = {
                                    0
                                }
                                values: list[f32] = {
                                    1
                                }
                            }
                        }
                        ValueFloat {
                            constantValue: f32 = 1
                            dynamics: pointer = VfxAnimatedFloatVariableData {
                                probabilityTables: list[pointer] = {
                                    VfxProbabilityTableData {
                                        keyTimes: list[f32] = {
                                            0
                                            1
                                        }
                                        keyValues: list[f32] = {
                                            0
                                            360
                                        }
                                    }
                                }
                                times: list[f32] = {
                                    0
                                }
                                values: list[f32] = {
                                    1
                                }
                            }
                        }
                    }
                    emitRotationAxes: list[vec3] = {
                        { 1.00000012, 0, 0 }
                        { 0, 1.00000012, 0 }
                    }
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Shared/Particles/BW_Chimney_Glow.scb"
                    }
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.300000012
                            0.800000012
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 0, 0 }
                            { 1, 0.643136978, 0.235293999, 0.615701973 }
                            { 1, 0.647059023, 0.243137002, 0.615701973 }
                            { 1, 1, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Shared/Particles/SRU_brazierFire_glow.dds"
            }
        }
        particleName: string = "BW_Chimney_Smoke"
        particlePath: string = "Maps/Particles/HA/Bilgewater/BW_Chimney_Smoke"
    }
    "Maps/Particles/HA/Bilgewater/BW_Peref_Steam_Generic" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 0.0799999982
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 19.8999996
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1.20000005
                                    1.79999995
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            19.8999996
                        }
                    }
                }
                emitterName: string = "SteamBot"
                importance: u8 = 0
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 10, 1 }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 1, 0 }
                }
                velocity: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 0, 1 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                            { 94.6371002, 0, 39.0370979 }
                        }
                    }
                }
                drag: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 1, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 0, 1, 0 }
                            { 0, 5, 0 }
                        }
                    }
                }
                0x3bf0b4ed: pointer = 0x4f4e2ed7 {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 1, 0, 1 }
                        dynamics: pointer = VfxAnimatedVector3fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        -150
                                        150
                                    }
                                }
                                VfxProbabilityTableData {}
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        -500
                                        500
                                    }
                                }
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { 1, 0, 1 }
                            }
                        }
                    }
                    emitRotationAngles: list[embed] = {
                        ValueFloat {
                            constantValue: f32 = 1
                            dynamics: pointer = VfxAnimatedFloatVariableData {
                                times: list[f32] = {
                                    0
                                }
                                values: list[f32] = {
                                    -25
                                }
                            }
                        }
                    }
                    emitRotationAxes: list[vec3] = {
                        { 0, 1.00000012, 0 }
                    }
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.796078503 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            0.200000003
                            0.622841001
                            0.850000024
                            1
                        }
                        values: list[vec4] = {
                            { 0.725489974, 1, 0.980391979, 0 }
                            { 0.776471019, 1, 0.952941, 0.647059023 }
                            { 0.811765015, 1, 0.952941, 1 }
                            { 0.772548974, 1, 0.93333298, 0.899194002 }
                            { 0.596077979, 1, 0.847059011, 0.447059005 }
                            { 0.392156988, 0.454901993, 0.431373, 0 }
                        }
                    }
                }
                pass: i16 = 1
                alphaRef: u8 = 0
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { -40, 0, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 130, 50, 150 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.699999988
                                    1.5
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.699999988
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 130, 50, 150 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0.00575800007
                            1
                        }
                        values: list[vec3] = {
                            { 11.3225803, 11.3225803, 11.3225803 }
                            { 15, 15, 15 }
                        }
                    }
                }
                texture: string = "ASSETS/Shared/Particles/BW_Peref_Clouds.dds"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { -0.100000001, 0 }
                }
                textureMult: pointer = 0xb097c1bd {
                    textureMult: string = "ASSETS/Shared/Particles/BW_Peref_Waterfall_Steam_Mult.dds"
                    birthUvScrollRateMult: embed = ValueVector2 {
                        constantValue: vec2 = { 0, -0.100000001 }
                    }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 10
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 5
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    2
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            5
                        }
                    }
                }
                emitterName: string = "SteamBot1"
                disabled: bool = true
                importance: u8 = 0
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 31, 180, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.699999988
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    1
                                    1.20000005
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    2.5
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 31, 180, 0 }
                        }
                    }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 2, 0 }
                }
                acceleration: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 46, 0 }
                }
                blendMode: u8 = 1
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            0.200000003
                            0.600000024
                            0.850000024
                            1
                        }
                        values: list[vec4] = {
                            { 0.745097995, 0.800000012, 1, 0 }
                            { 0.879643023, 0.905565977, 1, 0.649999976 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0.774999976 }
                            { 1, 1, 1, 0.449999988 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                pass: i16 = 1
                alphaRef: u8 = 0
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 15, 0, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 33, 33, 33 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    2
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 33, 33, 33 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 1, 1, 1 }
                            { 6, 15, 6 }
                        }
                    }
                }
                texture: string = "ASSETS/Shared/Particles/SRU_EastJungle_Waterfall_Swirlsteam_01.dds"
                uvMode: u8 = 2
                birthUVOffset: embed = ValueVector2 {
                    constantValue: vec2 = { 1, 1 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    2
                                }
                                keyValues: list[f32] = {
                                    0
                                    2
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    2
                                }
                                keyValues: list[f32] = {
                                    0
                                    2
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 1, 1 }
                        }
                    }
                }
                textureMult: pointer = 0xb097c1bd {
                    textureMult: string = "ASSETS/Shared/Particles/BW_Peref_Waterfall_Steam_Mult.dds"
                    birthUvScrollRateMult: embed = ValueVector2 {
                        constantValue: vec2 = { 0, 0.200000003 }
                    }
                }
            }
        }
        visibilityRadius: f32 = 5250
        particleName: string = "BW_Peref_Steam_Generic"
        particlePath: string = "Maps/Particles/HA/Bilgewater/BW_Peref_Steam_Generic"
        flags: u16 = 197
    }
    "Maps/Particles/HA/Bilgewater/BW_Chaos_Rain_and_Puddles" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 50
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1.20000005
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            1.20000005
                        }
                    }
                }
                particleLinger: option[f32] = {
                    11.1999998
                }
                emitterName: string = "RainDrops"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { -120, -6000, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.400000006
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { -120, -6000, 0 }
                        }
                    }
                }
                emissionMeshName: string = "ASSETS/Shared/Particles/BW_RainImmter.scb"
                0x3bf0b4ed: pointer = 0x4f4e2ed7 {
                    emitRotationAngles: list[embed] = {
                        ValueFloat {
                            constantValue: f32 = 20
                        }
                    }
                    emitRotationAxes: list[vec3] = {
                        { 0, 0, 1.00000012 }
                    }
                }
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                blendMode: u8 = 1
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.300000012
                            1
                        }
                        values: list[vec4] = {
                            { 0, 0.835294008, 0.670588017, 0 }
                            { 0.00392200006, 0.941175997, 0.756862998, 0.300000012 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                isDirectionOriented: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 90, 90 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 15, 90, 0 }
                }
                texture: string = "ASSETS/Shared/Particles/SRU_EastJungle_RainFalling_01.StrawberryRebuild.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 295
                }
                particleLinger: option[f32] = {
                    30
                }
                isSingleParticle: flag = true
                emitterLinger: option[f32] = {
                    30
                }
                emitterName: string = "GroundPuddles"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Shared/Particles/BW_Chaos_RainPuddles.scb"
                    }
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.698039234 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            0.899999976
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                pass: i16 = -32768
                particleIsLocalOrientation: flag = true
                texture: string = "ASSETS/Shared/Particles/bw_Chaos_Puddles.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 13
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    3
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            13
                        }
                    }
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.5
                }
                emitterName: string = "GlowRocks_BearRock"
                importance: u8 = 0
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                emissionMeshName: string = "ASSETS/Shared/Particles/BW_Chaos_RainPuddles.scb"
                0x3bf0b4ed: pointer = 0x4f4e2ed7 {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 10, 0, 10 }
                        dynamics: pointer = VfxAnimatedVector3fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        -8
                                        8
                                    }
                                }
                                VfxProbabilityTableData {}
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        -8
                                        8
                                    }
                                }
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { 10, 0, 10 }
                            }
                        }
                    }
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Shared/Particles/sru_raindrops_01.StrawberryRebuild.scb"
                    }
                }
                blendMode: u8 = 1
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            0.75
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 0.815702021 }
                            { 1, 1, 1, 0.807797015 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                particleIsLocalOrientation: flag = true
                isUniformScale: flag = true
                isRandomStartFrame: flag = true
                uvScrollClamp: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 1.39999998, 1.39999998, 1.39999998 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    0.5
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 1.39999998, 1.39999998, 1.39999998 }
                        }
                    }
                }
                texture: string = "ASSETS/Shared/Particles/BW_RainDrops_01.dds"
                numFrames: u16 = 2
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { -2, 0 }
                }
                texAddressModeBase: u8 = 2
                texDiv: vec2 = { 1, 2 }
            }
        }
        visibilityRadius: f32 = 11150
        particleName: string = "BW_Chaos_Rain_and_Puddles"
        particlePath: string = "Maps/Particles/HA/Bilgewater/BW_Chaos_Rain_and_Puddles"
    }
    "Maps/Particles/HA/Bilgewater/BW_Audio_Emitter_Rope" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLinger: option[f32] = {
                    10
                }
                emitterName: string = "empty"
                particleColorTexture: string = "ASSETS/Shared/Particles/black.SKINS_Kindred_Skin34.dds"
                meshRenderFlags: u8 = 0
                isUniformScale: flag = true
                texture: string = "ASSETS/Shared/Particles/black.SKINS_Kindred_Skin34.dds"
            }
        }
        particleName: string = "BW_Audio_Emitter_Rope"
        particlePath: string = "Maps/Particles/HA/Bilgewater/BW_Audio_Emitter_Rope"
        soundPersistentDefault: string = "Play_sfx_Env_Map14_Ambience_Emitter_Rope"
        flags: u16 = 229
    }
    "Maps/Particles/HA/Bilgewater/BW_AP_Chaos_Nexus_Idle" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 10
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 10
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.800000012
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.600000024
                                    0.699999988
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            10
                        }
                    }
                }
                particleLinger: option[f32] = {
                    20
                }
                emitterName: string = "sparkles1"
                birthOrbitalVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, -0.5, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.899999976
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.100000001
                                    0.300000012
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, -0.5, 0 }
                        }
                    }
                }
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 20, 0, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 20, 0, 0 }
                        }
                    }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 1, 1 }
                }
                worldAcceleration: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 0, 3, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 3, 0 }
                        }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                emissionMeshScale: f32 = 1.10000002
                emissionMeshName: string = "ASSETS/Shared/Particles/sru_order_crystalemitter.scb"
                blendMode: u8 = 4
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                        }
                    }
                }
                isUniformScale: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 1, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    360
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    360
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 1, 1, 0 }
                        }
                    }
                }
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 45, 45, 45 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.800000012
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.300000012
                                    0.400000006
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 45, 45, 45 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.300000012
                            1
                        }
                        values: list[vec3] = {
                            { 0, 1, 1 }
                            { 1, 1, 1 }
                            { 0, 1, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/Shared/Particles/SRU_Chaos_brightSparks.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 0.200000003
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 7
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.800000012
                                    1.20000005
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            7
                        }
                    }
                }
                particleLinger: option[f32] = {
                    17
                }
                emitterName: string = "structureGlow"
                0x563d4a22: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 10, 0 }
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Shared/Particles/sru_structureglow.scb"
                    }
                }
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.21960786 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.449999988
                            0.600000024
                            0.699999988
                            0.850000024
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, -0 }
                            { 1, 1, 1, 0.449999988 }
                            { 1, 1, 1, 0.699999988 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0.649999976 }
                            { 1, 1, 1, -0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 1.29999995, 1.29999995, 1.29999995 }
                }
                texture: string = "ASSETS/Shared/Particles/BW_Chaos_Color.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 0.600000024
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 10
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.600000024
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            10
                        }
                    }
                }
                particleLinger: option[f32] = {
                    20
                }
                emitterName: string = "Temp_Mesh"
                0x563d4a22: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 200, 0 }
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Shared/Particles/sru_order_nexus_ambientglowgeo.scb"
                    }
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 0, 0, 0, 1 }
                            { 1, 1, 1, 1 }
                            { 0, 0, 0, 1 }
                        }
                    }
                }
                reflectionDefinition: pointer = VfxReflectionDefinitionData {
                    fresnelColor: vec4 = { -1, -1, -1, 0 }
                }
                isUniformScale: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 5, 5, 5 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.899999976
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 5, 5, 5 }
                        }
                    }
                }
                texture: string = "ASSETS/Shared/Particles/SRU_Chaos_wispies.dds"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { -0.100000001, 0 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { -0.100000001, 0 }
                        }
                    }
                }
                birthUVOffset: embed = ValueVector2 {
                    constantValue: vec2 = { 1, 1 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 1, 1 }
                        }
                    }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 0.200000003
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 10
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.600000024
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            10
                        }
                    }
                }
                particleLinger: option[f32] = {
                    20
                }
                emitterName: string = "Temp_Mesh1"
                0x563d4a22: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 200, 0 }
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Shared/Particles/sru_order_nexus_ambientglowgeo.scb"
                    }
                }
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.635294139, 0.549019635, 0.501960814, 1 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 0, 0, 0, 1 }
                            { 1, 1, 1, 1 }
                            { 0, 0, 0, 1 }
                        }
                    }
                }
                reflectionDefinition: pointer = VfxReflectionDefinitionData {
                    fresnelColor: vec4 = { -1, -1, -1, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 5, 5, 5 }
                }
                texture: string = "ASSETS/Shared/Particles/SRUAP_ChaosNexus_redSquare.dds"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { -0.200000003, 0 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { -0.200000003, 0 }
                        }
                    }
                }
                birthUVOffset: embed = ValueVector2 {
                    constantValue: vec2 = { 1, 1 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 1, 1 }
                        }
                    }
                }
                texDiv: vec2 = { 0.5, 0.5 }
            }
        }
        particleName: string = "BW_AP_Chaos_Nexus_Idle"
        particlePath: string = "Maps/Particles/HA/Bilgewater/BW_AP_Chaos_Nexus_Idle"
        buildUpTime: f32 = 5
        assetRemappingTable: list[embed] = {
            VfxAssetRemap {
                oldAsset: hash = 0x081f36ac
                newAsset: string = "ASSETS/Shared/Particles/SRU_Order_brightSparks.dds"
            }
            VfxAssetRemap {
                oldAsset: hash = 0x0e85be02
                newAsset: string = "ASSETS/Shared/Particles/SRU_Order_Color.dds"
            }
            VfxAssetRemap {
                oldAsset: hash = 0x5707855a
                newAsset: string = "ASSETS/Shared/Particles/SRU_Order_wispies.dds"
            }
            VfxAssetRemap {
                oldAsset: hash = 0x136256a4
                newAsset: string = "ASSETS/Shared/Particles/SRUAP_OrderNexus_blueSquare.dds"
            }
        }
    }
    "Maps/Particles/HA/Bilgewater/BW_Order_StartingPlatform_Pearl" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 0.100000001
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 12
                }
                particleLinger: option[f32] = {
                    22
                }
                emitterName: string = "structureGlow"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Shared/Particles/BW_BlueGlow.scb"
                    }
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.200000003
                            0.5
                            0.75
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 0.699999988 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0.725000024 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 0.349999994, 0.349999994, 0.349999994 }
                }
                texture: string = "ASSETS/Shared/Particles/SRU_Order_Color.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 8
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.600000024
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            8
                        }
                    }
                }
                particleLinger: option[f32] = {
                    18
                }
                emitterName: string = "Pearl"
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Shared/Particles/BW_Order_StartingPLatform_Pearl.scb"
                    }
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.300000012
                            0.800000012
                            1
                        }
                        values: list[vec4] = {
                            { 0, 0, 0, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 0, 0, 0, 0 }
                        }
                    }
                }
                reflectionDefinition: pointer = VfxReflectionDefinitionData {
                    fresnelColor: vec4 = { -1, -1, -1, 0 }
                }
                particleIsLocalOrientation: flag = true
                isUniformScale: flag = true
                birthScale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.899999976
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 1, 1, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/Shared/Particles/SRU_Order_wispies.dds"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0.100000001, 0 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 0.100000001, 0 }
                        }
                    }
                }
                birthUVOffset: embed = ValueVector2 {
                    constantValue: vec2 = { 1, 1 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 1, 1 }
                        }
                    }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 10
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.800000012
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.600000024
                                    0.699999988
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            10
                        }
                    }
                }
                particleLinger: option[f32] = {
                    20
                }
                emitterName: string = "orbitSparks"
                birthOrbitalVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, -0.300000012, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.899999976
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.100000001
                                    0.300000012
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, -0.300000012, 0 }
                        }
                    }
                }
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 20, 0, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 20, 0, 0 }
                        }
                    }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 1, 1 }
                }
                worldAcceleration: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 0, 3, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 3, 0 }
                        }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                emissionMeshScale: f32 = 1.10000002
                emissionMeshName: string = "ASSETS/Shared/Particles/BW_Order_StartingPLatform_Pearl.scb"
                blendMode: u8 = 4
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                        }
                    }
                }
                isUniformScale: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 1, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    360
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    360
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 1, 1, 0 }
                        }
                    }
                }
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 45, 45, 45 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.800000012
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.300000012
                                    0.400000006
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 45, 45, 45 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.300000012
                            1
                        }
                        values: list[vec3] = {
                            { 0, 1, 1 }
                            { 1, 1, 1 }
                            { 0, 1, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/Shared/Particles/SRU_Order_brightSparks.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 10
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.800000012
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.100000001
                                    0.300000012
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            10
                        }
                    }
                }
                particleLinger: option[f32] = {
                    20
                }
                emitterName: string = "sparkles4"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 100, 0, 60 }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 1, 1 }
                }
                worldAcceleration: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 0, 3, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 3, 0 }
                        }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                emissionMeshScale: f32 = 1.10000002
                emissionMeshName: string = "ASSETS/Shared/Particles/BW_Order_StartingPLatform_Pearl.scb"
                blendMode: u8 = 4
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                        }
                    }
                }
                isUniformScale: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 1, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    360
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    360
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 1, 1, 0 }
                        }
                    }
                }
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 45, 45, 45 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.800000012
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.300000012
                                    0.400000006
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 45, 45, 45 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.300000012
                            1
                        }
                        values: list[vec3] = {
                            { 0, 1, 1 }
                            { 1, 1, 1 }
                            { 0, 1, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/Shared/Particles/SRU_Order_brightSparks.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 5
                }
                particleLinger: option[f32] = {
                    11
                }
                emitterName: string = "Temp_Mesh"
                0x3bf0b4ed: pointer = 0xee39916f {
                    emitOffset: vec3 = { 0, -5, -10 }
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Maps/Particles/BilgeWater/BW_BasePearl.scb"
                    }
                }
                blendMode: u8 = 3
                isUniformScale: flag = true
                texture: string = "ASSETS/Maps/Particles/BilgeWater/BW_BasePearl_Blue.dds"
            }
        }
        particleName: string = "BW_Order_StartingPlatform_Pearl"
        particlePath: string = "Maps/Particles/HA/Bilgewater/BW_Order_StartingPlatform_Pearl"
        buildUpTime: f32 = 5
        assetRemappingTable: list[embed] = {
            VfxAssetRemap {
                oldAsset: hash = 0xf982576c
                newAsset: string = "ASSETS/Shared/Particles/SRU_Chaos_brightSparks.dds"
            }
            VfxAssetRemap {
                oldAsset: hash = 0xb24905ab
                newAsset: string = "ASSETS/Shared/Particles/SRU_Chaos_Color.dds"
            }
            VfxAssetRemap {
                oldAsset: hash = 0xd106221a
                newAsset: string = "ASSETS/Shared/Particles/SRU_Chaos_wispies.dds"
            }
            VfxAssetRemap {
                oldAsset: hash = 0x476d3129
                newAsset: string = "ASSETS/Shared/Particles/SRUAP_ChaosNexus_redSquare.dds"
            }
            VfxAssetRemap {
                oldAsset: hash = 0x5ccecf8d
                newAsset: string = "ASSETS/Maps/Particles/BilgeWater/BW_BasePearl_Red.dds"
            }
        }
    }
    "Maps/Particles/HA/Bilgewater/BW_Audio_Emitter_Waterfall" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLinger: option[f32] = {
                    10
                }
                emitterName: string = "empty"
                particleColorTexture: string = "ASSETS/Shared/Particles/black.SKINS_Kindred_Skin34.dds"
                meshRenderFlags: u8 = 0
                isUniformScale: flag = true
                texture: string = "ASSETS/Shared/Particles/black.SKINS_Kindred_Skin34.dds"
            }
        }
        visibilityRadius: f32 = 2000
        particleName: string = "BW_Audio_Emitter_Waterfall"
        particlePath: string = "Maps/Particles/HA/Bilgewater/BW_Audio_Emitter_Waterfall"
        soundPersistentDefault: string = "Play_sfx_Env_Map14_Ambience_Emitter_Waterfall"
        flags: u16 = 229
    }
    "Maps/Particles/HA/Bilgewater/BW_Braziers_Fire_Bigger" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 10
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.600000024
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.800000012
                                    2.5
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            0.600000024
                        }
                    }
                }
                particleLinger: option[f32] = {
                    2
                }
                emitterName: string = "Fire"
                birthAcceleration: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 300, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.100000001
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.800000012
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 300, 0 }
                        }
                    }
                }
                0x3bf0b4ed: pointer = 0x4f4e2ed7 {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 20, 10, 20 }
                        dynamics: pointer = VfxAnimatedVector3fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        -1
                                        1
                                    }
                                }
                                VfxProbabilityTableData {}
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        -1
                                        1
                                    }
                                }
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { 20, 10, 20 }
                            }
                        }
                    }
                    emitRotationAngles: list[embed] = {
                        ValueFloat {
                            constantValue: f32 = 45
                        }
                    }
                    emitRotationAxes: list[vec3] = {
                        { 0, 1.00000012, 0 }
                    }
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.300000012
                            0.800000012
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0.800000012 }
                            { 1, 0, 0, 0 }
                        }
                    }
                }
                pass: i16 = 2
                isUniformScale: flag = true
                isRandomStartFrame: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 0, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    360
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 1, 0, 0 }
                        }
                    }
                }
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 0, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    0
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 1, 0, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 105, 105, 105 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.800000012
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 105, 105, 105 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            1
                        }
                        values: list[vec3] = {
                            { 0.600000024, 0.600000024, 0.600000024 }
                            { 1, 1, 1 }
                            { 0.600000024, 0.600000024, 0.600000024 }
                        }
                    }
                }
                texture: string = "ASSETS/Shared/Particles/SRU_Brazier_Flame_Temp_01.DDS"
                birthFrameRate: embed = ValueFloat {
                    constantValue: f32 = 0.5
                }
                numFrames: u16 = 8
                texDiv: vec2 = { 4, 2 }
                textureMult: pointer = 0xb097c1bd {
                    textureMult: string = "ASSETS/Shared/Particles/Env_MB_brazierFire_mult.dds"
                    texDivMult: vec2 = { 2, 2 }
                    birthUvScrollRateMult: embed = ValueVector2 {
                        constantValue: vec2 = { 0, -1.25 }
                    }
                    birthUVOffsetMult: embed = ValueVector2 {
                        constantValue: vec2 = { 1, 1 }
                        dynamics: pointer = VfxAnimatedVector2fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        1
                                        -1
                                    }
                                }
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        1
                                        -1
                                    }
                                }
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec2] = {
                                { 1, 1 }
                            }
                        }
                    }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 2.5
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            2.5
                        }
                    }
                }
                emitterName: string = "baseGlow"
                0x3bf0b4ed: pointer = 0xee39916f {
                    emitOffset: vec3 = { 0, -1, 0 }
                }
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                blendMode: u8 = 1
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 0.5, 0.5, 0.5 }
                            { 1, 0, 0, 0 }
                        }
                    }
                }
                pass: i16 = 1
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 90, 0, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 280, 280, 280 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 0.5, 0.5, 0.5 }
                            { 0.75, 0.75, 0.75 }
                        }
                    }
                }
                texture: string = "ASSETS/Shared/Particles/SRU_brazierFire_glow.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 5
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1.20000005
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            1.20000005
                        }
                    }
                }
                particleLinger: option[f32] = {
                    11.1999998
                }
                emitterName: string = "sparks"
                disabled: bool = true
                birthOrbitalVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0.400000006, 0.400000006, 0.400000006 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0.400000006, 0.400000006, 0.400000006 }
                        }
                    }
                }
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 250, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 250, 0 }
                        }
                    }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 0.600000024, 0.600000024, 0.600000024 }
                }
                0x3bf0b4ed: pointer = 0x4f4e2ed7 {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 25, -25, 25 }
                        dynamics: pointer = VfxAnimatedVector3fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        -1
                                        1
                                    }
                                }
                                VfxProbabilityTableData {}
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        -1
                                        1
                                    }
                                }
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { 25, -25, 25 }
                            }
                        }
                    }
                    emitRotationAngles: list[embed] = {
                        ValueFloat {
                            constantValue: f32 = 45
                        }
                    }
                    emitRotationAxes: list[vec3] = {
                        { 0, 1.00000012, 0 }
                    }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.300000012
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 0, 0, 0 }
                        }
                    }
                }
                pass: i16 = 1
                isDirectionOriented: flag = true
                isRandomStartFrame: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 20, 20, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1.5
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 20, 20, 0 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.300000012
                            1
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                            { 1, 0.5, 0 }
                            { 0.200000003, 0.200000003, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Shared/Particles/Env_MB_brazierFire_Ash_01.dds"
                numFrames: u16 = 4
                texDiv: vec2 = { 2, 2 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 3
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1.5
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.800000012
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            1.5
                        }
                    }
                }
                emitterName: string = "Smoke"
                disabled: bool = true
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 1, 0 }
                }
                birthAcceleration: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 150, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.800000012
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 150, 0 }
                        }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                0x3bf0b4ed: pointer = 0x4f4e2ed7 {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 30, 20, 10 }
                        dynamics: pointer = VfxAnimatedVector3fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        -1
                                        1
                                    }
                                }
                                VfxProbabilityTableData {}
                                VfxProbabilityTableData {}
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { 30, 20, 10 }
                            }
                        }
                    }
                    emitRotationAngles: list[embed] = {
                        ValueFloat {
                            constantValue: f32 = 25
                        }
                    }
                    emitRotationAxes: list[vec3] = {
                        { 0, 1.00000012, 0 }
                    }
                }
                0x563d4a22: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 30, 0 }
                }
                blendMode: u8 = 1
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.300000012
                            0.600000024
                            1
                        }
                        values: list[vec4] = {
                            { 0.713724971, 0.713724971, 0.160784006, 0 }
                            { 0.560783982, 0.552941024, 0.44313699, 0.294117987 }
                            { 0.49019599, 0.482353002, 0.36470601, 0.0941179991 }
                            { 0.0980390012, 0.164706007, 0.349020004, 0 }
                        }
                    }
                }
                disableBackfaceCull: bool = true
                isDirectionOriented: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 1, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    360
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 1, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 70, 70, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.800000012
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.800000012
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.800000012
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 70, 70, 0 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.400000006
                            1
                        }
                        values: list[vec3] = {
                            { 0.600000024, 0.200000003, 0.600000024 }
                            { 0.800000012, 0.800000012, 0.800000012 }
                            { 1, 1, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/Shared/Particles/Env_MB_brazier_dust.dds"
                uvMode: u8 = 2
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0, 0.400000006 }
                }
                textureMult: pointer = 0xb097c1bd {
                    textureMult: string = "ASSETS/Shared/Particles/Env_MB_brazier_dust_mult.dds"
                    birthUvScrollRateMult: embed = ValueVector2 {
                        constantValue: vec2 = { 0, 0.25 }
                    }
                    birthUVOffsetMult: embed = ValueVector2 {
                        constantValue: vec2 = { 1, 1 }
                        dynamics: pointer = VfxAnimatedVector2fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        1
                                        0
                                    }
                                }
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        1
                                        0
                                    }
                                }
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec2] = {
                                { 1, 1 }
                            }
                        }
                    }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 0.0799999982
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 22
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            22
                        }
                    }
                }
                particleLinger: option[f32] = {
                    32
                }
                emitterName: string = "FireGlow"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                0x3bf0b4ed: pointer = 0xee39916f {
                    emitOffset: vec3 = { 0, 65, 0 }
                }
                0x563d4a22: embed = ValueVector3 {
                    constantValue: vec3 = { 0, -20, 0 }
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.200000003
                            0.349999994
                            0.449999988
                            0.550000012
                            0.649999976
                            0.800000012
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 0.550000012 }
                            { 1, 1, 1, 0.850000024 }
                            { 1, 1, 1, 0.600000024 }
                            { 1, 1, 1, 0.600000024 }
                            { 1, 1, 1, 0.850000024 }
                            { 1, 1, 1, 0.550000012 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                pass: i16 = 5
                softParticleParams: pointer = VfxSoftParticleDefinitionData {
                    deltaIn: f32 = 50
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 151, 151, 151 }
                }
                texture: string = "ASSETS/Shared/Particles/SRU_Brazier_Glow_01.dds"
            }
        }
        particleName: string = "BW_Braziers_Fire_Bigger"
        particlePath: string = "Maps/Particles/HA/Bilgewater/BW_Braziers_Fire_Bigger"
        soundPersistentDefault: string = "Play_sfx_Env_Map14_Emitter_firebig"
    }
    "Maps/Particles/HA/Bilgewater/BW_Audio_Emitter_River" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLinger: option[f32] = {
                    10
                }
                emitterName: string = "empty"
                particleColorTexture: string = "ASSETS/Shared/Particles/black.SKINS_Kindred_Skin34.dds"
                meshRenderFlags: u8 = 0
                isUniformScale: flag = true
                texture: string = "ASSETS/Shared/Particles/black.SKINS_Kindred_Skin34.dds"
            }
        }
        particleName: string = "BW_Audio_Emitter_River"
        particlePath: string = "Maps/Particles/HA/Bilgewater/BW_Audio_Emitter_River"
        soundPersistentDefault: string = "Play_sfx_Env_Map14_Ambience_Emitter_River"
        flags: u16 = 229
    }
    "Maps/Particles/HA/Bilgewater/BW_Chaos_Inhibitor_runeTimer" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 320
                }
                isSingleParticle: flag = true
                emitterName: string = "runeTimeGlow"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Shared/Particles/BW_Chaos_inhibitor_respawn_base.scb"
                    }
                }
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.643137276 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.0172739998
                            0.989443004
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                pass: i16 = 3
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, -45, 0 }
                }
                isLocalOrientation: flag = false
                texture: string = "ASSETS/Shared/Particles/BW_Chaos_Inhibitor_RuneCountdown_glow.dds"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { -0.00270000007, -0.100000001 }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 320
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.800000012
                                    1.20000005
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            320
                        }
                    }
                }
                isSingleParticle: flag = true
                emitterName: string = "pulseTimer"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                0x563d4a22: embed = ValueVector3 {
                    constantValue: vec3 = { 10, 30, -29 }
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Shared/Particles/BW_Chaos_inhibitor_respawn_base2.scb"
                    }
                }
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.533333361 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.00300000003
                            0.0844530016
                            0.187140003
                            0.294625998
                            0.357964993
                            0.438580006
                            0.5
                            0.613243997
                            0.699616015
                            0.758157015
                            0.864682972
                            0.935701013
                            0.997120976
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 0, 0 }
                            { 1, 1, 1, 0.75 }
                            { 1, 1, 0.361701995, 0.326240987 }
                            { 1, 1, 0.907800972, 0.889548004 }
                            { 1, 1, 0.411347985, 0.411347985 }
                            { 1, 1, 0.843972027, 0.843972027 }
                            { 1, 1, 0.539007008, 0.553191006 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 0.503546, 0.496454 }
                            { 1, 1, 0.858156025, 0.858156025 }
                            { 1, 1, 0.411347985, 0.411347985 }
                            { 1, 1, 0.807955027, 0.801418006 }
                            { 1, 1, 0.380095989, 0.418440014 }
                            { 1, 1, 1, 0.72340399 }
                            { 1, 1, 0, 0 }
                        }
                    }
                }
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, -45, 0 }
                }
                isLocalOrientation: flag = false
                texture: string = "ASSETS/Shared/Particles/BW_Chaos_Inhibitor_RuneCountdown.dds"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0.00999999978, 0 }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 320
                }
                isSingleParticle: flag = true
                emitterName: string = "runeTimeGlow1"
                disabled: bool = true
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                0x563d4a22: embed = ValueVector3 {
                    constantValue: vec3 = { 10, 50, -29 }
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Shared/Particles/BW_order_inhibitor_respawn_base2.scb"
                    }
                }
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.149019614 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.0307100005
                            0.0748559982
                            0.150000006
                            0.165067002
                            0.261036009
                            0.309980989
                            0.356045991
                            0.394434005
                            0.448500007
                            0.449140012
                            0.512476027
                            0.539346993
                            0.600000024
                            0.642993987
                            0.722648978
                            0.800000012
                            0.850000024
                            0.904990017
                            0.952014983
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, -45, 0 }
                }
                isLocalOrientation: flag = false
                texture: string = "ASSETS/Shared/Particles/BW_Chaos_Inhibitor_RuneCountdown.dds"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { -0.0500000007, 0 }
                }
            }
        }
        particleName: string = "BW_Chaos_Inhibitor_runeTimer"
        particlePath: string = "Maps/Particles/HA/Bilgewater/BW_Chaos_Inhibitor_runeTimer"
        flags: u16 = 133
        assetRemappingTable: list[embed] = {
            VfxAssetRemap {
                oldAsset: hash = 0x0a23fd0b
                newAsset: string = "ASSETS/Shared/Particles/BW_Order_Inhibitor_RuneCountdown.dds"
            }
            VfxAssetRemap {
                oldAsset: hash = 0xbf2092e7
                newAsset: string = "ASSETS/Shared/Particles/BW_Order_Inhibitor_RuneCountdown_glow.dds"
            }
        }
    }
    "Maps/Particles/HA/Bilgewater/BW_Chaos_StartingPlatform_RedGem" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 0.300000012
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.5
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    2.5
                                    3
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            0.5
                        }
                    }
                }
                emitterName: string = "Temp_Mesh"
                disabled: bool = true
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Shared/Particles/BW_Chaos_StartingPlatform_RedGem.scb"
                    }
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.300000012
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 0.752894998 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                particleIsLocalOrientation: flag = true
                texture: string = "ASSETS/Shared/Particles/BW_Chaos_StartingPlatform_RedGem.dds"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 2, 0 }
                }
                birthUVOffset: embed = ValueVector2 {
                    constantValue: vec2 = { 1, 1 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec2] = {
                            { 0, 0 }
                            { 1, 1 }
                        }
                    }
                }
                textureMult: pointer = 0xb097c1bd {
                    textureMult: string = "ASSETS/Shared/Particles/BW_Chaos_StartingPlatform_GemMult.dds"
                    birthUvScrollRateMult: embed = ValueVector2 {
                        constantValue: vec2 = { 1, 1 }
                        dynamics: pointer = VfxAnimatedVector2fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        1
                                        -1
                                    }
                                }
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        1
                                        -1
                                    }
                                }
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec2] = {
                                { 1, 1 }
                            }
                        }
                    }
                    birthUVOffsetMult: embed = ValueVector2 {
                        constantValue: vec2 = { 1, 1 }
                        dynamics: pointer = VfxAnimatedVector2fVariableData {
                            times: list[f32] = {
                                0
                                1
                            }
                            values: list[vec2] = {
                                { 0, 0 }
                                { 1, 1 }
                            }
                        }
                    }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 0.0500000007
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 25
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.800000012
                                    1.20000005
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            25
                        }
                    }
                }
                particleLinger: option[f32] = {
                    35
                }
                emitterName: string = "structureGlow"
                0x563d4a22: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 10, 0 }
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Shared/Particles/BW_Chaos_StartingPlatform_RedGlow.scb"
                    }
                }
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.34117648 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.449999988
                            0.600000024
                            0.699999988
                            0.850000024
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, -0 }
                            { 1, 1, 1, 0.449999988 }
                            { 1, 1, 1, 0.699999988 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0.649999976 }
                            { 1, 1, 1, -0 }
                        }
                    }
                }
                miscRenderFlags: u8 = 1
                texture: string = "ASSETS/Shared/Particles/BW_Chaos_Color.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 0.5
                }
                particleLifetime: embed = ValueFloat {
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.800000012
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.600000024
                                    0.699999988
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            3
                        }
                    }
                }
                particleLinger: option[f32] = {
                    13
                }
                emitterName: string = "sparkles1"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 20, 0, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 20, 0, 0 }
                        }
                    }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 1, 1 }
                }
                worldAcceleration: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { -5, 12, -5 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { -5, 12, -5 }
                        }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                emissionMeshName: string = "ASSETS/Shared/Particles/BW_Chaos_StartingPlatform_RedGem.scb"
                blendMode: u8 = 4
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                        }
                    }
                }
                particleIsLocalOrientation: flag = true
                isUniformScale: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 1, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    360
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    360
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 1, 1, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 45, 45, 45 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.800000012
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.300000012
                                    0.400000006
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 45, 45, 45 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.300000012
                            1
                        }
                        values: list[vec3] = {
                            { 0, 1, 1 }
                            { 1, 1, 1 }
                            { 0, 1, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/Shared/Particles/SRU_Chaos_brightSparks.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1.5
                }
                particleLifetime: embed = ValueFloat {
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.699999988
                                    0.800000012
                                    0.879999995
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.600000024
                                    0.699999988
                                    0.699999988
                                    2
                                    2
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            3
                        }
                    }
                }
                particleLinger: option[f32] = {
                    13
                }
                emitterName: string = "sparkles2"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 20, 0, 20 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 20, 0, 20 }
                        }
                    }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 1, 1 }
                }
                worldAcceleration: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { -3, 0, -3 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { -3, 0, -3 }
                        }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                emissionMeshName: string = "ASSETS/Shared/Particles/BW_Chaos_StartingPlatform_RedGem.scb"
                blendMode: u8 = 4
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                        }
                    }
                }
                particleIsLocalOrientation: flag = true
                isUniformScale: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 1, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    360
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    360
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 1, 1, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 45, 45, 45 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.800000012
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.300000012
                                    0.400000006
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 45, 45, 45 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.300000012
                            1
                        }
                        values: list[vec3] = {
                            { 0, 1, 1 }
                            { 1, 1, 1 }
                            { 0, 1, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/Shared/Particles/SRU_Chaos_brightSparks.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 0.5
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.899999976
                                    0.901000023
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.200000003
                                    0.200000003
                                    1.29999995
                                    1.5
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            0.5
                        }
                    }
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1.5
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.800000012
                                    0.899999976
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            1.5
                        }
                    }
                }
                emitterName: string = "whitesparks"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                emissionMeshName: string = "ASSETS/Shared/Particles/BW_Chaos_StartingPlatform_RedGem.scb"
                particleColorTexture: string = "ASSETS/Shared/Particles/color-hold.SKINS_Seraphine_Skin50.dds"
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 0.53725493, 0.53725493, 1 }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.800000012 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 0.800000012 }
                            { 1, 1, 1, 0.128639996 }
                            { 1, 0.968626976, 0, 0 }
                        }
                    }
                }
                colorLookUpScales: vec2 = { 1, 0.400000006 }
                disableBackfaceCull: bool = true
                miscRenderFlags: u8 = 1
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 0, 1 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    90
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    90
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 1, 0, 1 }
                        }
                    }
                }
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 90, 0, 90 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 90, 0, 90 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 20, 35, 1 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.400000006
                                    0.600000024
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.400000006
                                    0.600000024
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.400000006
                                    0.600000024
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 20, 35, 1 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            1
                        }
                        values: list[vec3] = {
                            { 0.5, 0.5, 0.5 }
                            { 0.899999976, 0.899999976, 0.899999976 }
                            { 0.200000003, 0.200000003, 0.200000003 }
                        }
                    }
                }
                texture: string = "ASSETS/Shared/Particles/SRU_Chaos_Shopkeeper_weaponRack_sparkle.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 0.200000003
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 7.5
                }
                particleLinger: option[f32] = {
                    17.5
                }
                emitterName: string = "Temp_Mesh1"
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Shared/Particles/sru_order_nexus_ambientglowgeo.scb"
                    }
                }
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.635294139, 0.549019635, 0.501960814, 1 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 0, 0, 0, 1 }
                            { 1, 1, 1, 1 }
                            { 0, 0, 0, 1 }
                        }
                    }
                }
                reflectionDefinition: pointer = VfxReflectionDefinitionData {
                    fresnelColor: vec4 = { -1, -1, -1, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 3, 3, 3 }
                }
                texture: string = "ASSETS/Shared/Particles/SRUAP_ChaosNexus_redSquare.dds"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { -0.200000003, 0 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { -0.200000003, 0 }
                        }
                    }
                }
                birthUVOffset: embed = ValueVector2 {
                    constantValue: vec2 = { 1, 1 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 1, 1 }
                        }
                    }
                }
                texDiv: vec2 = { 0.5, 0.5 }
            }
        }
        particleName: string = "BW_Chaos_StartingPlatform_RedGem"
        particlePath: string = "Maps/Particles/HA/Bilgewater/BW_Chaos_StartingPlatform_RedGem"
    }
    "Maps/Particles/HA/Bilgewater/BW_LanternGlow_02" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = -1
                }
                particleLinger: option[f32] = {
                    9
                }
                isSingleParticle: flag = true
                emitterName: string = "Basic"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                0x3bf0b4ed: pointer = 0x4f4e2ed7 {
                    emitRotationAngles: list[embed] = {
                        ValueFloat {
                            constantValue: f32 = 1
                            dynamics: pointer = VfxAnimatedFloatVariableData {
                                probabilityTables: list[pointer] = {
                                    VfxProbabilityTableData {
                                        keyTimes: list[f32] = {
                                            0
                                            1
                                        }
                                        keyValues: list[f32] = {
                                            0
                                            360
                                        }
                                    }
                                }
                                times: list[f32] = {
                                    0
                                }
                                values: list[f32] = {
                                    1
                                }
                            }
                        }
                        ValueFloat {
                            constantValue: f32 = 1
                            dynamics: pointer = VfxAnimatedFloatVariableData {
                                probabilityTables: list[pointer] = {
                                    VfxProbabilityTableData {
                                        keyTimes: list[f32] = {
                                            0
                                            1
                                        }
                                        keyValues: list[f32] = {
                                            0
                                            360
                                        }
                                    }
                                }
                                times: list[f32] = {
                                    0
                                }
                                values: list[f32] = {
                                    1
                                }
                            }
                        }
                    }
                    emitRotationAxes: list[vec3] = {
                        { 1.00000012, 0, 0 }
                        { 0, 1.00000012, 0 }
                    }
                }
                blendMode: u8 = 1
                miscRenderFlags: u8 = 1
                isUniformScale: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 180, 182, 0 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.326296002
                            0.644913971
                            1
                        }
                        values: list[vec3] = {
                            { 0.814516127, 0.814516127, 0.814516127 }
                            { 0.983870983, 0.983870983, 0.983870983 }
                            { 0.975806475, 0.975806475, 0.975806475 }
                            { 0.814516127, 0.814516127, 0.814516127 }
                        }
                    }
                }
                texture: string = "ASSETS/Shared/Particles/BW_Lantern_GreenGlow.dds"
                textureMult: pointer = 0xb097c1bd {
                    textureMult: string = "ASSETS/Shared/Particles/BW_LanternCloud.dds"
                    birthUvScrollRateMult: embed = ValueVector2 {
                        constantValue: vec2 = { 0.0500000007, 0.100000001 }
                    }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 0.150000006
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 18
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.800000012
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    0.699999988
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            18
                        }
                    }
                }
                particleLinger: option[f32] = {
                    1
                }
                emitterName: string = "fireLine"
                disabled: bool = true
                0x563d4a22: embed = ValueVector3 {
                    constantValue: vec3 = { 0, -180, 0 }
                }
                primitive: pointer = VfxPrimitiveRay {}
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.933333397 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.300000012
                            1
                        }
                        values: list[vec4] = {
                            { 0.243137002, 1, 0.937255025, 0 }
                            { 0.0392160006, 1, 0.807843029, 1 }
                            { 0.164706007, 1, 0.650979996, 0 }
                        }
                    }
                }
                pass: i16 = 3
                miscRenderFlags: u8 = 1
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { -90, 0, 90 }
                }
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 600, 450, 0 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.300000012
                            1
                        }
                        values: list[vec3] = {
                            { 1, 0.899999976, 0 }
                            { 1, 1, 0 }
                            { 0, 1.10000002, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Shared/Particles/BW_ambientGlow_Blue.dds"
            }
        }
        particleName: string = "BW_LanternGlow_02"
        particlePath: string = "Maps/Particles/HA/Bilgewater/BW_LanternGlow_02"
        flags: u16 = 132
        buildUpTime: f32 = 10
    }
    "Maps/Particles/HA/Bilgewater/BW_FogLow_01" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 16
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.600000024
                                    0.600099981
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    1
                                    2
                                    2
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            16
                        }
                    }
                }
                particleLinger: option[f32] = {
                    26
                }
                emitterName: string = "Basic"
                disabled: bool = true
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { -10, 1, 11 }
                }
                velocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 1, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.162187994
                            0.222648993
                            0.517274022
                            1
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                            { 0, 5.55810118, 0 }
                            { 0, 32.4446869, 0 }
                            { 0, -88.5449448, 0 }
                            { 0, -150, 0 }
                        }
                    }
                }
                drag: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 1, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 0, 165, 0 }
                            { 0, 0, 0 }
                        }
                    }
                }
                emissionMeshName: string = "ASSETS/Shared/Particles/bw_fog_linespawn_01.scb"
                blendMode: u8 = 1
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.300000012
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 0, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.500100017
                                    1
                                }
                                keyValues: list[f32] = {
                                    2
                                    2
                                    5
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 1, 0, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 120, 120, 120 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.402110994
                            0.793666005
                            1
                        }
                        values: list[vec3] = {
                            { 0.672380924, 0.672380924, 0.672380924 }
                            { 1.64380956, 1.64380956, 1.64380956 }
                            { 1.94333339, 1.94333339, 1.94333339 }
                            { 1.27952385, 1.27952385, 1.27142859 }
                        }
                    }
                }
                texture: string = "ASSETS/Shared/Particles/BW_FogLow_01.dds"
                uvMode: u8 = 2
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0.00100000005, 0.00100000005 }
                }
                textureMult: pointer = 0xb097c1bd {
                    textureMult: string = "ASSETS/Shared/Particles/BW_RollingFog_Mult_01.dds"
                    birthUvScrollRateMult: embed = ValueVector2 {
                        constantValue: vec2 = { 0.0500000007, 0.0399999991 }
                    }
                    birthUVOffsetMult: embed = ValueVector2 {
                        constantValue: vec2 = { 1, 1 }
                        dynamics: pointer = VfxAnimatedVector2fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        0
                                        1
                                    }
                                }
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        0
                                        1
                                    }
                                }
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec2] = {
                                { 0, 0 }
                            }
                        }
                    }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 0.200000003
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 15
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.800000012
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    1
                                    2
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            15
                        }
                    }
                }
                particleLinger: option[f32] = {
                    25
                }
                emitterName: string = "Temp_Mesh1"
                0x563d4a22: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 0, 1 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -500
                                    500
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    500
                                    -500
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 1, 0, 1 }
                        }
                    }
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Shared/Particles/BW_Fog_edgeFog.scb"
                    }
                }
                blendMode: u8 = 1
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.114202999
                            0.5
                            0.885797024
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 0.604839027 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0.576613009 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, -45, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    1.5
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.699999988
                                    0.700100005
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    1
                                    1.5
                                    1.5
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 1, 1, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/Shared/Particles/BW_RollingFog_01.dds"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0, 0.0500000007 }
                }
                birthUVOffset: embed = ValueVector2 {
                    constantValue: vec2 = { 1, 1 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 1, 1 }
                        }
                    }
                }
                textureMult: pointer = 0xb097c1bd {
                    textureMult: string = "ASSETS/Shared/Particles/BW_RollingFog_Mult_01.dds"
                    texDivMult: vec2 = { 0.00999999978, 1 }
                    birthUvScrollRateMult: embed = ValueVector2 {
                        constantValue: vec2 = { 0, 0.100000001 }
                    }
                    birthUVOffsetMult: embed = ValueVector2 {
                        dynamics: pointer = VfxAnimatedVector2fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        -1
                                        1
                                    }
                                }
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        -1
                                        1
                                    }
                                }
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec2] = {
                                { 0, 0 }
                            }
                        }
                    }
                }
            }
        }
        particleName: string = "BW_FogLow_01"
        particlePath: string = "Maps/Particles/HA/Bilgewater/BW_FogLow_01"
    }
    "Maps/Particles/HA/Bilgewater/BW_FogLow_02" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 16
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.600000024
                                    0.600099981
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    1
                                    2
                                    2
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            16
                        }
                    }
                }
                particleLinger: option[f32] = {
                    26
                }
                emitterName: string = "Basic"
                disabled: bool = true
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { -10, 1, 11 }
                }
                velocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 1, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.162187994
                            0.222648993
                            0.517274022
                            1
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                            { 0, 5.55810118, 0 }
                            { 0, 32.4446869, 0 }
                            { 0, -88.5449448, 0 }
                            { 0, -150, 0 }
                        }
                    }
                }
                drag: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 1, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 0, 165, 0 }
                            { 0, 0, 0 }
                        }
                    }
                }
                emissionMeshName: string = "ASSETS/Shared/Particles/bw_fog_linespawn_01.scb"
                blendMode: u8 = 1
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.300000012
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 0, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.500100017
                                    1
                                }
                                keyValues: list[f32] = {
                                    2
                                    2
                                    5
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 1, 0, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 120, 120, 120 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.402110994
                            0.793666005
                            1
                        }
                        values: list[vec3] = {
                            { 0.672380924, 0.672380924, 0.672380924 }
                            { 1.64380956, 1.64380956, 1.64380956 }
                            { 1.94333339, 1.94333339, 1.94333339 }
                            { 1.27952385, 1.27952385, 1.27142859 }
                        }
                    }
                }
                texture: string = "ASSETS/Shared/Particles/BW_FogLow_01.dds"
                uvMode: u8 = 2
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0.00100000005, 0.00100000005 }
                }
                textureMult: pointer = 0xb097c1bd {
                    textureMult: string = "ASSETS/Shared/Particles/BW_RollingFog_Mult_01.dds"
                    birthUvScrollRateMult: embed = ValueVector2 {
                        constantValue: vec2 = { 0.0500000007, 0.0399999991 }
                    }
                    birthUVOffsetMult: embed = ValueVector2 {
                        constantValue: vec2 = { 1, 1 }
                        dynamics: pointer = VfxAnimatedVector2fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        0
                                        1
                                    }
                                }
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        0
                                        1
                                    }
                                }
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec2] = {
                                { 0, 0 }
                            }
                        }
                    }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 0.400000006
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 10
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.800000012
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    1
                                    2
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            10
                        }
                    }
                }
                particleLinger: option[f32] = {
                    20
                }
                emitterName: string = "Temp_Mesh1"
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Shared/Particles/bw_foggeo_02.scb"
                    }
                }
                blendMode: u8 = 1
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, -85, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    0.899999976
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    1.5
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 1, 1, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/Shared/Particles/BW_RollingFog_01.dds"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0, 0.0500000007 }
                }
                birthUVOffset: embed = ValueVector2 {
                    constantValue: vec2 = { 1, 1 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 1, 1 }
                        }
                    }
                }
                textureMult: pointer = 0xb097c1bd {
                    textureMult: string = "ASSETS/Shared/Particles/BW_RollingFog_Mult_01.dds"
                    birthUvScrollRateMult: embed = ValueVector2 {
                        constantValue: vec2 = { 0, 1 }
                        dynamics: pointer = VfxAnimatedVector2fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {}
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        0.0799999982
                                        0.00999999978
                                    }
                                }
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec2] = {
                                { 0, 1 }
                            }
                        }
                    }
                }
            }
        }
        particleName: string = "BW_FogLow_02"
        particlePath: string = "Maps/Particles/HA/Bilgewater/BW_FogLow_02"
    }
    "Maps/Particles/HA/Bilgewater/BW_BrazierDoor_Smoke" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 4
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 2
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    0.800000012
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            2
                        }
                    }
                }
                particleLinger: option[f32] = {
                    12
                }
                emitterName: string = "sparks"
                birthOrbitalVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0.200000003, 0.200000003, 0.200000003 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0.200000003, 0.200000003, 0.200000003 }
                        }
                    }
                }
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 20, 500, 20 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.25
                                    2
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 20, 500, 20 }
                        }
                    }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 0.400000006, 0.400000006, 0.400000006 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -0.5
                                    3
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                            0.300000012
                            0.699999988
                            1
                        }
                        values: list[vec3] = {
                            { 0.400000006, 0.400000006, 0.400000006 }
                            { 0.160000011, 0.160000011, 0.160000011 }
                            { 0.0800000057, 0.0800000057, 0.0800000057 }
                            { 0, 0, 0 }
                        }
                    }
                }
                birthAcceleration: embed = ValueVector3 {
                    constantValue: vec3 = { 30, 30, 30 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.699999988
                                    0.709999979
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.300000012
                                    0.300000012
                                    1
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.300000012
                                    0.310000002
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    -0.5
                                    2
                                    2.5
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.699999988
                                    0.709999979
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.300000012
                                    0.300000012
                                    1
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 30, 30, 30 }
                        }
                    }
                }
                velocity: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 1, 1 }
                }
                drag: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 1, 1 }
                }
                worldAcceleration: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 1, 1, 1 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.300000012
                            1
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                            { 0, 0, 0 }
                            { 2111, 0, 2111 }
                        }
                    }
                }
                0x3bf0b4ed: pointer = 0x4f4e2ed7 {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 15, 0, 15 }
                        dynamics: pointer = VfxAnimatedVector3fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        -1
                                        1
                                    }
                                }
                                VfxProbabilityTableData {}
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        -1
                                        1
                                    }
                                }
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { 15, 0, 15 }
                            }
                        }
                    }
                    emitRotationAngles: list[embed] = {
                        ValueFloat {
                            constantValue: f32 = 45
                        }
                        ValueFloat {
                            constantValue: f32 = 360
                            dynamics: pointer = VfxAnimatedFloatVariableData {
                                probabilityTables: list[pointer] = {
                                    VfxProbabilityTableData {
                                        keyTimes: list[f32] = {
                                            0
                                            1
                                        }
                                        keyValues: list[f32] = {
                                            0
                                            1
                                        }
                                    }
                                }
                                times: list[f32] = {
                                    0
                                }
                                values: list[f32] = {
                                    360
                                }
                            }
                        }
                    }
                    emitRotationAxes: list[vec3] = {
                        { 0, 1.00000012, 0 }
                        { 0, 1.00000012, 0 }
                    }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.300000012
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 0, 0, 0 }
                        }
                    }
                }
                pass: i16 = 1
                isDirectionOriented: flag = true
                isRandomStartFrame: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 40, 40, 40 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                            { 0, 0, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 15, 15, 15 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.699999988
                                    1.5
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.699999988
                                    1.5
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 15, 15, 15 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.300000012
                            1
                        }
                        values: list[vec3] = {
                            { 0.300000012, 0.300000012, 0.300000012 }
                            { 1, 0.5, 0 }
                            { 0.200000003, 0.200000003, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Shared/Particles/SRU_Chaos_shopkeeper_Ash_orange.dds"
                numFrames: u16 = 4
                texDiv: vec2 = { 2, 2 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 0.150000006
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 10
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    1.20000005
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            10
                        }
                    }
                }
                emitterName: string = "Brazier_Blueside_Smoke1"
                importance: u8 = 0
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                0x3bf0b4ed: pointer = 0xee39916f {
                    emitOffset: vec3 = { -10, 40, -40 }
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Shared/Particles/BW_Smoke_DoorBraziers.scb"
                    }
                }
                blendMode: u8 = 1
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.870588005, 0.709803998, 0.568627, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.200000003
                            0.800000012
                            1
                        }
                        values: list[vec4] = {
                            { 0.870588005, 0.709803998, 0.568627, 0 }
                            { 0.870588005, 0.709803998, 0.568627, 1 }
                            { 0.870588005, 0.709803998, 0.568627, 1 }
                            { 0.870588005, 0.709803998, 0.568627, 0 }
                        }
                    }
                }
                disableBackfaceCull: bool = true
                isLocalOrientation: flag = false
                texture: string = "ASSETS/Shared/Particles/SRU_Braziers_Smoke_Blueside_01.dds"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0.300000012, 0.100000001 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    0.5
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 0.300000012, 0.100000001 }
                        }
                    }
                }
                birthUVOffset: embed = ValueVector2 {
                    constantValue: vec2 = { 1, 1 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 1, 1 }
                        }
                    }
                }
                textureMult: pointer = 0xb097c1bd {
                    textureMult: string = "ASSETS/Shared/Particles/SRU_Braziers_Smoke_Blueside_01_Mult.dds"
                    birthUvScrollRateMult: embed = ValueVector2 {
                        constantValue: vec2 = { 0.0250000004, 0 }
                    }
                }
            }
        }
        particleName: string = "BW_BrazierDoor_Smoke"
        particlePath: string = "Maps/Particles/HA/Bilgewater/BW_BrazierDoor_Smoke"
    }
    "Maps/Particles/HA/Bilgewater/BW_Audio_Emitter_Shootout_Guns" = VfxSystemDefinitionData {
        simpleEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0
                }
                particleLinger: option[f32] = {
                    10
                }
                emitterName: string = "empty"
                particleColorTexture: string = "ASSETS/Shared/Particles/black.SKINS_Kindred_Skin34.dds"
                meshRenderFlags: u8 = 0
                texture: string = "ASSETS/Shared/Particles/black.SKINS_Kindred_Skin34.dds"
                0xbc022424: pointer = 0x7f70a2b2 {
                    birthScale: embed = ValueFloat {
                        constantValue: f32 = 0
                    }
                }
            }
        }
        visibilityRadius: f32 = 1000
        particleName: string = "BW_Audio_Emitter_Shootout_Guns"
        particlePath: string = "Maps/Particles/HA/Bilgewater/BW_Audio_Emitter_Shootout_Guns"
        soundPersistentDefault: string = "Play_sfx_Env_Map14_Ambience_Emitter_Shootout_Guns"
        flags: u16 = 229
    }
    "Maps/Particles/HA/Bilgewater/BW_Audio_Emitter_BridgeCreak" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLinger: option[f32] = {
                    10
                }
                emitterName: string = "empty"
                particleColorTexture: string = "ASSETS/Shared/Particles/black.SKINS_Kindred_Skin34.dds"
                meshRenderFlags: u8 = 0
                isUniformScale: flag = true
                texture: string = "ASSETS/Shared/Particles/black.SKINS_Kindred_Skin34.dds"
            }
        }
        visibilityRadius: f32 = 2000
        particleName: string = "BW_Audio_Emitter_BridgeCreak"
        particlePath: string = "Maps/Particles/HA/Bilgewater/BW_Audio_Emitter_BridgeCreak"
        soundPersistentDefault: string = "Play_sfx_Env_Map14_Ambience_Emitter_BridgeCreak"
        flags: u16 = 229
    }
    "Maps/Particles/HA/Bilgewater/BW_Peref_WaterFall_01" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = -1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = -1
                }
                isSingleParticle: flag = true
                emitterName: string = "Waterfall_plane"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Shared/Particles/BW_Peref_Waterfall_Ledge.scb"
                    }
                }
                blendMode: u8 = 1
                texture: string = "ASSETS/Shared/Particles/SRU_EastJungle_Waterfall_plane_01.dds"
                uvMode: u8 = 2
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0, -0.800000012 }
                }
                textureMult: pointer = 0xb097c1bd {
                    textureMult: string = "ASSETS/Shared/Particles/SRU_EastJungle_Waterfall_plane_Mult_01.dds"
                    birthUvScrollRateMult: embed = ValueVector2 {
                        constantValue: vec2 = { 0, -0.699999988 }
                    }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = -1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = -1
                }
                isSingleParticle: flag = true
                emitterName: string = "Bott_WhiteFalls"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                0x563d4a22: embed = ValueVector3 {
                    constantValue: vec3 = { 5, 0, 0 }
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Shared/Particles/BW_Peref_Waterfall_Ledge_Pale.scb"
                    }
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.725993991 }
                }
                pass: i16 = 20
                texture: string = "ASSETS/Shared/Particles/SRU_EastJungle_Waterfall_WhiteFalls_01.dds"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0, -0.400000006 }
                }
                textureMult: pointer = 0xb097c1bd {
                    textureMult: string = "ASSETS/Shared/Particles/SRU_EastJungle_Waterfall_WhiteFalls_Mult_01.dds"
                    birthUvScrollRateMult: embed = ValueVector2 {
                        constantValue: vec2 = { 0, -0.600000024 }
                    }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = -1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = -1
                }
                isSingleParticle: flag = true
                emitterName: string = "Waterfall_plane_Botfalls1"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Shared/Particles/BW_Peref_Waterfall_BottFalls.scb"
                    }
                }
                blendMode: u8 = 1
                texture: string = "ASSETS/Shared/Particles/SRU_EastJungle_Waterfall_plane_Botfalls_01.dds"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0, -0.5 }
                }
                birthUVOffset: embed = ValueVector2 {
                    constantValue: vec2 = { 1, 1 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 1, 1 }
                        }
                    }
                }
                textureMult: pointer = 0xb097c1bd {
                    textureMult: string = "ASSETS/Shared/Particles/SRU_EastJungle_Waterfall_plane_Botfalls_Mult_01.dds"
                    birthUvScrollRateMult: embed = ValueVector2 {
                        constantValue: vec2 = { 0, -0.800000012 }
                    }
                    birthUVOffsetMult: embed = ValueVector2 {
                        constantValue: vec2 = { 1, 1 }
                        dynamics: pointer = VfxAnimatedVector2fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        0
                                        1
                                    }
                                }
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        0
                                        1
                                    }
                                }
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec2] = {
                                { 1, 1 }
                            }
                        }
                    }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = -1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = -1
                }
                isSingleParticle: flag = true
                emitterName: string = "WhiteFalls_botfalls"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                0x563d4a22: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 0, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 10, 0, 0 }
                            { 30, 0, 0 }
                        }
                    }
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Shared/Particles/BW_Peref_Waterfall_BottFalls.scb"
                    }
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.725993991 }
                }
                pass: i16 = 20
                texture: string = "ASSETS/Shared/Particles/SRU_EastJungle_Waterfall_WhiteFalls_botfalls_01.dds"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0, -0.5 }
                }
                birthUVOffset: embed = ValueVector2 {
                    constantValue: vec2 = { 1, 1 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 1, 1 }
                        }
                    }
                }
                textureMult: pointer = 0xb097c1bd {
                    textureMult: string = "ASSETS/Shared/Particles/SRU_EastJungle_Waterfall_WhiteFalls_Botfalls_Mult_01.dds"
                    birthUvScrollRateMult: embed = ValueVector2 {
                        constantValue: vec2 = { 0, -0.800000012 }
                    }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 0.899999976
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1.29999995
                }
                emitterName: string = "TopEdgeHightlight"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Shared/Particles/BW_Peref_Waterfall_HighLight.scb"
                    }
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.300000012
                            0.699999988
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                pass: i16 = 30
                disableBackfaceCull: bool = true
                isUniformScale: flag = true
                isRandomStartFrame: flag = true
                texture: string = "ASSETS/Shared/Particles/SRU_WaterFall_Test_Small_Highlight_02.dds"
                numFrames: u16 = 2
                texDiv: vec2 = { 2, 1 }
                textureMult: pointer = 0xb097c1bd {
                    textureMult: string = "ASSETS/Shared/Particles/SRU_DragonPit_waterfall_TopEdgeHightlight_Mult_01.dds"
                    birthUvScrollRateMult: embed = ValueVector2 {
                        constantValue: vec2 = { 0, -0.5 }
                        dynamics: pointer = VfxAnimatedVector2fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {}
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        0.300000012
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        1
                                        1
                                        2
                                    }
                                }
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec2] = {
                                { 0, -0.5 }
                            }
                        }
                    }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = -1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = -1
                }
                isSingleParticle: flag = true
                emitterName: string = "SideFoam"
                importance: u8 = 0
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Shared/Particles/BW_Peref_Waterfall_SideEdge.scb"
                    }
                }
                blendMode: u8 = 1
                particleIsLocalOrientation: flag = true
                texture: string = "ASSETS/Shared/Particles/BW_Peref_Waterfall_SideFoam_01.dds"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0, -0.800000012 }
                }
                textureMult: pointer = 0xb097c1bd {
                    textureMult: string = "ASSETS/Shared/Particles/SRU_DragonPit_waterfall_SideFoam_Mult_01.dds"
                    birthUvScrollRateMult: embed = ValueVector2 {
                        constantValue: vec2 = { 0, -1 }
                    }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    1.29999995
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            1
                        }
                    }
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 5
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    2
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            5
                        }
                    }
                }
                emitterName: string = "SteamBot"
                importance: u8 = 0
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 31, 280, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.699999988
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    1
                                    1.20000005
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    2.5
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 31, 280, 0 }
                        }
                    }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 2, 0 }
                }
                acceleration: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 166, 0 }
                }
                emissionMeshName: string = "ASSETS/Shared/Particles/BW_Peref_Waterfall_SteamMeshEmitter.scb"
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                blendMode: u8 = 1
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            0.200000003
                            0.600000024
                            0.850000024
                            1
                        }
                        values: list[vec4] = {
                            { 0.745097995, 0.800000012, 1, 0 }
                            { 0.879643023, 0.905565977, 1, 0.649999976 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0.774999976 }
                            { 1, 1, 1, 0.449999988 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                pass: i16 = 1
                alphaRef: u8 = 0
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, -51, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 33, 33, 33 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    2
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 33, 33, 33 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 1, 1, 1 }
                            { 6, 15, 6 }
                        }
                    }
                }
                texture: string = "ASSETS/Shared/Particles/SRU_EastJungle_Waterfall_Swirlsteam_01.dds"
                uvMode: u8 = 2
                birthUVOffset: embed = ValueVector2 {
                    constantValue: vec2 = { 1, 1 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    2
                                }
                                keyValues: list[f32] = {
                                    0
                                    2
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    2
                                }
                                keyValues: list[f32] = {
                                    0
                                    2
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 1, 1 }
                        }
                    }
                }
                textureMult: pointer = 0xb097c1bd {
                    textureMult: string = "ASSETS/Shared/Particles/BW_Peref_Waterfall_Steam_Mult.dds"
                    birthUvScrollRateMult: embed = ValueVector2 {
                        constantValue: vec2 = { -0.5, 0 }
                    }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 2.4000001
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    1.29999995
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            2.4000001
                        }
                    }
                }
                emitterName: string = "SteamBot1"
                disabled: bool = true
                importance: u8 = 0
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 180, -20 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    2.5
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 180, -20 }
                        }
                    }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 1, 0 }
                }
                acceleration: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 266, 0 }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                0x3bf0b4ed: pointer = 0xee39916f {
                    emitOffset: vec3 = { 410, -1300, 350 }
                }
                blendMode: u8 = 1
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.800000012
                            1
                        }
                        values: list[vec4] = {
                            { 0.0352940001, 0.043136999, 0.164706007, 0 }
                            { 0.631372988, 0.917647004, 0.886274993, 0.643136978 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                alphaRef: u8 = 0
                isRotationEnabled: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 0, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    360
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 1, 0, 0 }
                        }
                    }
                }
                rotation0: embed = IntegratedValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                            { 0, 0, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { -53, 53, 53 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { -53, 53, 53 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 1, 1, 1 }
                            { 2, 2, 2 }
                        }
                    }
                }
                texture: string = "ASSETS/Shared/Particles/SRU_EastJungle_Waterfall_Swirlsteam_01.dds"
                uvMode: u8 = 2
                birthUVOffset: embed = ValueVector2 {
                    constantValue: vec2 = { 1, 1 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    2
                                }
                                keyValues: list[f32] = {
                                    0
                                    2
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    2
                                }
                                keyValues: list[f32] = {
                                    0
                                    2
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 1, 1 }
                        }
                    }
                }
                textureMult: pointer = 0xb097c1bd {
                    textureMult: string = "ASSETS/Shared/Particles/SRU_EastJungle_Waterfall_Swirlsteam_Mult_01.dds"
                    birthUvScrollRateMult: embed = ValueVector2 {
                        constantValue: vec2 = { 0.100000001, 0.100000001 }
                    }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 5
                }
                emitterName: string = "SteamBot2"
                disabled: bool = true
                importance: u8 = 0
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Shared/Particles/sru_dragonpit_steam_bot_01.scb"
                    }
                }
                blendMode: u8 = 1
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.800000012
                            1
                        }
                        values: list[vec4] = {
                            { 0.0352940001, 0.043136999, 0.164706007, 0 }
                            { 0.631372988, 0.917647004, 0.886274993, 0.643136978 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                alphaRef: u8 = 0
                texture: string = "ASSETS/Shared/Particles/SRU_EastJungle_Waterfall_Swirlsteam_01.dds"
                uvMode: u8 = 2
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { -0.5, 0 }
                }
                textureMult: pointer = 0xb097c1bd {
                    textureMult: string = "ASSETS/Shared/Particles/SRU_EastJungle_Waterfall_Swirlsteam_Mult_01.dds"
                    birthUvScrollRateMult: embed = ValueVector2 {
                        constantValue: vec2 = { -0.100000001, 0 }
                    }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 5
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.550000012
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.600000024
                                    0.800000012
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    1.5
                                    2
                                    2
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            0.550000012
                        }
                    }
                }
                emitterName: string = "WaterFoamHead1"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, -41, 0 }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 2, 0, 2 }
                }
                birthAcceleration: embed = ValueVector3 {
                    constantValue: vec3 = { 0, -150, 0 }
                }
                0x3bf0b4ed: pointer = 0x4f4e2ed7 {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 1, 1, 0 }
                        dynamics: pointer = VfxAnimatedVector3fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        -111
                                        132
                                    }
                                }
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        0
                                        -700
                                    }
                                }
                                VfxProbabilityTableData {}
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { 1, 1, 0 }
                            }
                        }
                    }
                    emitRotationAngles: list[embed] = {
                        ValueFloat {
                            constantValue: f32 = 1
                        }
                    }
                    emitRotationAxes: list[vec3] = {
                        { 0, 0, 1.00000012 }
                    }
                }
                0x563d4a22: embed = ValueVector3 {
                    constantValue: vec3 = { 50, -109.900002, -70 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.800000012
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 50, -109.900002, -70 }
                        }
                    }
                }
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                blendMode: u8 = 4
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.200000003
                            0.400000006
                            0.800000012
                            1
                        }
                        values: list[vec4] = {
                            { 0.333332986, 0.498039007, 0.431373, 0 }
                            { 0.333332986, 0.498039007, 0.431373, 1 }
                            { 0.352941006, 0.427451015, 0.427451015, 1 }
                            { 0.752941012, 1, 1, 0.325489998 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                pass: i16 = 9
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 128, 270 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 90, 90, 130 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.400000006
                                    0.699999988
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    0.5
                                    1
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.400000006
                                    0.699999988
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    0.5
                                    1
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.400000006
                                    0.699999988
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    0.5
                                    1
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 90, 90, 130 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            1
                        }
                        values: list[vec3] = {
                            { 1, 1, 1 }
                            { 1, 1, 1 }
                            { 8.80000019, 1.5, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/Shared/Particles/SRU_DragonPit_WaterSplash_anim.dds"
                frameRate: f32 = 14
                numFrames: u16 = 24
                texDiv: vec2 = { 4, 4 }
            }
        }
        visibilityRadius: f32 = 580
        particleName: string = "BW_Peref_WaterFall_01"
        particlePath: string = "Maps/Particles/HA/Bilgewater/BW_Peref_WaterFall_01"
    }
    "Maps/Particles/HA/Bilgewater/BW_Audio_Emitter_Shootout_Cannons" = VfxSystemDefinitionData {
        simpleEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0
                }
                particleLinger: option[f32] = {
                    10
                }
                emitterName: string = "empty"
                particleColorTexture: string = "ASSETS/Shared/Particles/black.SKINS_Kindred_Skin34.dds"
                meshRenderFlags: u8 = 0
                texture: string = "ASSETS/Shared/Particles/black.SKINS_Kindred_Skin34.dds"
                0xbc022424: pointer = 0x7f70a2b2 {
                    birthScale: embed = ValueFloat {
                        constantValue: f32 = 0
                    }
                }
            }
        }
        visibilityRadius: f32 = 1000
        particleName: string = "BW_Audio_Emitter_Shootout_Cannons"
        particlePath: string = "Maps/Particles/HA/Bilgewater/BW_Audio_Emitter_Shootout_Cannons"
        soundPersistentDefault: string = "Play_sfx_Env_Map14_Ambience_Emitter_Shootout_Cannons"
        flags: u16 = 229
    }
    "Maps/Particles/HA/Base/HA_Audio_Emitter_FireMed_Big" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLinger: option[f32] = {
                    10
                }
                emitterName: string = "empty"
                particleColorTexture: string = "ASSETS/Shared/Particles/black.SKINS_Kindred_Skin34.dds"
                meshRenderFlags: u8 = 0
                isUniformScale: flag = true
                texture: string = "ASSETS/Shared/Particles/black.SKINS_Kindred_Skin34.dds"
            }
        }
        particleName: string = "HA_Audio_Emitter_FireMed_Big"
        particlePath: string = "Maps/Particles/HA/Base/HA_Audio_Emitter_FireMed_Big"
        soundPersistentDefault: string = "Play_sfx_Env_map12_fire_med_big"
        flags: u16 = 132
    }
    0x1943dee0 = MapPointLightType {
        lightColor: vec4 = { 0.964705944, 0.862745166, 0.0352941193, 1 }
        radius: f32 = 76
    }
    0x1a43e073 = MapPointLightType {
        lightColor: vec4 = { 0.0392156877, 0.176470593, 0.121568635, 1 }
        radius: f32 = 342
    }
    0x1b43e206 = MapPointLightType {
        lightColor: vec4 = { 0.717647076, 0.00392156886, 0.00392156886, 1 }
        radius: f32 = 852
    }
    0x1b52ec90 = MapPointLightType {
        lightColor: vec4 = { 0.180392161, 0.168627456, 0.129411772, 1 }
        radius: f32 = 4000
    }
    0x1c43e399 = MapPointLightType {
        lightColor: vec4 = { 0.623529434, 0.470588267, 0.00392156886, 1 }
        radius: f32 = 276
    }
    0x1c52ee23 = MapPointLightType {
        lightColor: vec4 = { 0.454901993, 0.427451015, 0.376470625, 1 }
        radius: f32 = 1184
        castStaticShadows: bool = false
    }
    0x1d43e52c = MapPointLightType {
        lightColor: vec4 = { 0.411764741, 0.36470589, 0.149019614, 1 }
        radius: f32 = 2936
        castStaticShadows: bool = false
    }
    0x1d52efb6 = MapPointLightType {
        lightColor: vec4 = { 0.533333361, 0.501960814, 0.400000036, 1 }
        radius: f32 = 1583
        castStaticShadows: bool = false
    }
    0x1e43e6bf = MapPointLightType {
        lightColor: vec4 = { 0.878431439, 0.392156899, 0.0980392247, 1 }
        radius: f32 = 1827
    }
    0x1e52f149 = MapPointLightType {
        lightColor: vec4 = { 0.34117648, 0.588235319, 0.34117648, 1 }
        radius: f32 = 1162
        castStaticShadows: bool = false
    }
    0x1e552fe0 = MapPointLightType {
        lightColor: vec4 = { 0.0156862754, 0.203921586, 0.196078449, 1 }
        radius: f32 = 2625
    }
    0x1f43e852 = MapPointLightType {
        lightColor: vec4 = { 0.890196145, 0.639215708, 0.0392156877, 1 }
        radius: f32 = 320
    }
    0x1f486580 = MapPointLightType {
        lightColor: vec4 = { 0.254901975, 0.262745112, 0.270588249, 1 }
        radius: f32 = 852
        castStaticShadows: bool = false
    }
    0x1f52f2dc = MapPointLightType {
        lightColor: vec4 = { 0.10980393, 0.137254909, 0.149019614, 1 }
        radius: f32 = 342
        castStaticShadows: bool = false
    }
    0x1f553173 = MapPointLightType {
        lightColor: vec4 = { 0.0235294141, 0.309803933, 0.321568638, 1 }
        radius: f32 = 719
        castStaticShadows: bool = false
    }
    0x2043e9e5 = MapPointLightType {
        lightColor: vec4 = { 0.890196145, 0.600000024, 0.0392156877, 1 }
        radius: f32 = 320
    }
    0x20486713 = MapPointLightType {
        lightColor: vec4 = { 0.890196145, 0.698039234, 0.0392156877, 1 }
        radius: f32 = 320
    }
    0x2052f46f = MapPointLightType {
        lightColor: vec4 = { 0.466666698, 0.36470589, 0.254901975, 1 }
        radius: f32 = 1007
        castStaticShadows: bool = false
    }
    0x20553306 = MapPointLightType {
        lightColor: vec4 = { 0.580392182, 0.58431375, 0.419607878, 1 }
        radius: f32 = 2758
        castStaticShadows: bool = false
    }
    0x2152f602 = MapPointLightType {
        lightColor: vec4 = { 0.454901993, 0.494117677, 0.521568656, 1 }
        radius: f32 = 4000
        castStaticShadows: bool = false
    }
    0x21553499 = MapPointLightType {
        lightColor: vec4 = { 0.43921569, 0.411764711, 0.333333343, 1 }
        radius: f32 = 2670
        castStaticShadows: bool = false
    }
    0x2252f795 = MapPointLightType {
        lightColor: vec4 = { 0.00392156886, 0.192156881, 0.223529428, 1 }
        radius: f32 = 4000
    }
    0x2255362c = MapPointLightType {
        lightColor: vec4 = { 0.203921586, 0.235294133, 0.223529428, 1 }
        radius: f32 = 4000
        castStaticShadows: bool = false
    }
    0x235537bf = MapPointLightType {
        lightColor: vec4 = { 0.156862751, 0.725490212, 0.384313732, 1 }
        radius: f32 = 342
    }
    0x24553952 = MapPointLightType {
        lightColor: vec4 = { 0.00392156886, 0.223529428, 0.156862751, 1 }
        radius: f32 = 4000
        castStaticShadows: bool = false
    }
    0x25553ae5 = MapPointLightType {
        lightColor: vec4 = { 0.972549021, 0.329411775, 0.0274509806, 1 }
        radius: f32 = 808
    }
    0x27487218 = MapPointLightType {
        lightColor: vec4 = { 0.258823544, 0.24313727, 0.196078449, 1 }
        radius: f32 = 1628
        castStaticShadows: bool = false
    }
    0x2752ff74 = MapPointLightType {
        lightColor: vec4 = { 0.117647067, 0.152941182, 0.200000018, 1 }
        radius: f32 = 941
        castStaticShadows: bool = false
    }
    0x284873ab = MapPointLightType {
        lightColor: vec4 = { 0.513725519, 0.835294187, 0.549019635, 1 }
        radius: f32 = 2071
        castStaticShadows: bool = false
    }
    0x28530107 = MapPointLightType {
        lightColor: vec4 = { 0.0784313753, 0.380392194, 0.0784313753, 1 }
        radius: f32 = 1207
    }
    0x2859bccc = MapPointLightType {
        lightColor: vec4 = { 0.976470649, 0.603921592, 0.0156862754, 1 }
        radius: f32 = 808
    }
    0x2948753e = MapPointLightType {
        lightColor: vec4 = { 0.345098048, 0.356862754, 0.247058839, 1 }
        radius: f32 = 2071
        castStaticShadows: bool = false
    }
    0x2959be5f = MapPointLightType {
        lightColor: vec4 = { 0.65882355, 0.56078434, 0.525490224, 1 }
        radius: f32 = 1162
        castStaticShadows: bool = false
    }
    0x2a4876d1 = MapPointLightType {
        lightColor: vec4 = { 0.239215702, 0.235294133, 0.21960786, 1 }
        radius: f32 = 1229
        castStaticShadows: bool = false
    }
    0x2b487864 = MapPointLightType {
        lightColor: vec4 = { 0.854901969, 0.533333361, 0.266666681, 1 }
        radius: f32 = 785
        castStaticShadows: bool = false
    }
    0x2c4879f7 = MapPointLightType {
        lightColor: vec4 = { 0.58431375, 0.478431404, 0.203921586, 1 }
        radius: f32 = 1074
        castStaticShadows: bool = false
    }
    0x2c5545ea = MapPointLightType {
        lightColor: vec4 = { 0.494117677, 0.894117713, 0.68235296, 1 }
        radius: f32 = 4000
        castStaticShadows: bool = false
    }
    0x2c59c318 = MapPointLightType {
        lightColor: vec4 = { 0.0274509825, 0.0156862754, 0.200000018, 1 }
        radius: f32 = 1362
        castStaticShadows: bool = false
    }
    0x2d487b8a = MapPointLightType {
        lightColor: vec4 = { 0.411764741, 0.396078467, 0.333333343, 1 }
        radius: f32 = 2647
        castStaticShadows: bool = false
    }
    0x2d55477d = MapPointLightType {
        lightColor: vec4 = { 0.588235319, 0.290196091, 0.0705882385, 1 }
        radius: f32 = 918
    }
    0x2d59c4ab = MapPointLightType {
        lightColor: vec4 = { 0.458823532, 0.403921574, 0.298039228, 1 }
        radius: f32 = 1606
        castStaticShadows: bool = false
    }
    0x2e487d1d = MapPointLightType {
        lightColor: vec4 = { 0.215686291, 0.278431386, 0.305882365, 1 }
        radius: f32 = 941
        castStaticShadows: bool = false
    }
    0x2e59c63e = MapPointLightType {
        lightColor: vec4 = { 0.623529434, 0.56078434, 0.482352942, 1 }
        radius: f32 = 1118
        castStaticShadows: bool = false
    }
    0x2f59c7d1 = MapPointLightType {
        lightColor: vec4 = { 0.529411793, 0.470588237, 0.294117659, 1 }
        radius: f32 = 1384
        castStaticShadows: bool = false
    }
    0x3059c964 = MapPointLightType {
        lightColor: vec4 = { 0.490196109, 0.470588267, 0.392156899, 1 }
        radius: f32 = 785
        castStaticShadows: bool = false
    }
    0x3159caf7 = MapPointLightType {
        lightColor: vec4 = { 0.580392182, 0.313725501, 0.125490203, 1 }
        radius: f32 = 719
        castStaticShadows: bool = false
    }
    0x3259cc8a = MapPointLightType {
        lightColor: vec4 = { 0, 0.0980392247, 0.149019614, 1 }
        radius: f32 = 896
        castStaticShadows: bool = false
    }
    0x3359ce1d = MapPointLightType {
        lightColor: vec4 = { 0.647058845, 0.541176498, 0.321568638, 1 }
        radius: f32 = 386
        castStaticShadows: bool = false
    }
    0x83cb7192 = MapPointLightType {
        lightColor: vec4 = { 0.0392156877, 0.145098045, 0.10980393, 1 }
        radius: f32 = 3423
        castStaticShadows: bool = false
    }
    0x84cb7325 = MapPointLightType {
        lightColor: vec4 = { 0.247058824, 0.235294119, 0.203921571, 1 }
        radius: f32 = 1606
        castStaticShadows: bool = false
    }
    0x85cb74b8 = MapPointLightType {
        lightColor: vec4 = { 0, 0.121568635, 0.156862751, 1 }
        radius: f32 = 1761
        castStaticShadows: bool = false
    }
    0x86cb764b = MapPointLightType {
        lightColor: vec4 = { 0.00784313772, 0.117647067, 0.203921586, 1 }
        radius: f32 = 918
        castStaticShadows: bool = false
    }
    0x87cb77de = MapPointLightType {
        lightColor: vec4 = { 0.141176477, 0.141176477, 0.168627456, 1 }
        radius: f32 = 941
        castStaticShadows: bool = false
    }
    0x88cb7971 = MapPointLightType {
        lightColor: vec4 = { 0.0156862754, 0.164705887, 0.274509817, 1 }
        radius: f32 = 1495
    }
    0x89cb7b04 = MapPointLightType {
        lightColor: vec4 = { 0.207843155, 0.207843155, 0.211764723, 1 }
        radius: f32 = 785
        castStaticShadows: bool = false
    }
    0x8acb7c97 = MapPointLightType {
        lightColor: vec4 = { 0.0392156877, 0.0627451017, 0.145098045, 1 }
        radius: f32 = 1295
        castStaticShadows: bool = false
    }
    0x8bcb7e2a = MapPointLightType {
        lightColor: vec4 = { 0.403921574, 0.388235301, 0.313725501, 1 }
        radius: f32 = 1739
        castStaticShadows: bool = false
    }
    0x8ccb7fbd = MapPointLightType {
        lightColor: vec4 = { 0.0392156877, 0.176470593, 0.0392156877, 1 }
        radius: f32 = 741
        castStaticShadows: bool = false
    }
    0x984fdfc0 = MapPointLightType {
        lightColor: vec4 = { 0.576470613, 0.662745118, 0.011764707, 1 }
        radius: f32 = 165
    }
    0x994fe153 = MapPointLightType {
        lightColor: vec4 = { 0.345098048, 0.13333334, 0.0705882385, 1 }
        radius: f32 = 386
        castStaticShadows: bool = false
    }
    0x9a4fe2e6 = MapPointLightType {
        lightColor: vec4 = { 0.396078438, 0.41568628, 0.239215687, 1 }
        radius: f32 = 1739
        castStaticShadows: bool = false
    }
    0x9b4fe479 = MapPointLightType {
        lightColor: vec4 = { 0.192156881, 0.196078449, 0.141176477, 1 }
        radius: f32 = 4000
        castStaticShadows: bool = false
    }
    0x9c4fe60c = MapPointLightType {
        lightColor: vec4 = { 0.0941176564, 0.13333334, 0.113725498, 1 }
        radius: f32 = 963
        castStaticShadows: bool = false
    }
    0x9d4fe79f = MapPointLightType {
        lightColor: vec4 = { 0.505882382, 0.337254912, 0.011764707, 1 }
        radius: f32 = 519
    }
    0x9e4fe932 = MapPointLightType {
        lightColor: vec4 = { 0.823529422, 0.498039216, 0.0352941193, 1 }
        radius: f32 = 165
    }
    0x9f4feac5 = MapPointLightType {
        lightColor: vec4 = { 0.898039281, 0.933333397, 0.0235294141, 1 }
        radius: f32 = 165
    }
    0xa04fec58 = MapPointLightType {
        lightColor: vec4 = { 0.372549027, 0.274509817, 0.200000018, 1 }
        radius: f32 = 1184
        castStaticShadows: bool = false
    }
    0xa14fedeb = MapPointLightType {
        lightColor: vec4 = { 0.525490224, 0.623529434, 0.00392156886, 1 }
        radius: f32 = 165
    }
    0xa44b7576 = MapPointLightType {
        lightColor: vec4 = { 0.717647076, 0.454901963, 0, 1 }
        radius: f32 = 852
    }
    0xa54b7709 = MapPointLightType {
        lightColor: vec4 = { 0.984313786, 0.423529446, 0.00784313772, 1 }
        radius: f32 = 719
    }
    0xaa4b7ee8 = MapPointLightType {
        lightColor: vec4 = { 0.466666669, 0.470588237, 0.266666681, 1 }
        radius: f32 = 3091
        castStaticShadows: bool = false
    }
    0xab4b807b = MapPointLightType {
        lightColor: vec4 = { 0.972549081, 0.517647088, 0.0274509825, 1 }
        radius: f32 = 852
    }
    0xab4dbf12 = MapPointLightType {
        lightColor: vec4 = { 0.164705887, 0.0627451017, 0.0392156877, 1 }
        radius: f32 = 874
        castStaticShadows: bool = false
    }
    0xac4b820e = MapPointLightType {
        lightColor: vec4 = { 0.345098048, 0.278431386, 0.223529428, 1 }
        radius: f32 = 542
    }
    0xac4dc0a5 = MapPointLightType {
        lightColor: vec4 = { 0.368627459, 0.0352941193, 0.0274509825, 1 }
        radius: f32 = 453
    }
    0xad4b83a1 = MapPointLightType {
        lightColor: vec4 = { 0.156862751, 0.207843155, 0.231372565, 1 }
        radius: f32 = 3157
        castStaticShadows: bool = false
    }
    0xae4b8534 = MapPointLightType {
        lightColor: vec4 = { 1, 0.360784322, 0.0431372561, 1 }
        radius: f32 = 719
    }
    0xae4dc3cb = MapPointLightType {
        lightColor: vec4 = { 0.21960786, 0.207843155, 0.13333334, 1 }
        radius: f32 = 1473
        castStaticShadows: bool = false
    }
    0xaf4b86c7 = MapPointLightType {
        lightColor: vec4 = { 0.00392156886, 0.250980407, 0.105882362, 1 }
        radius: f32 = 409
        castStaticShadows: bool = false
    }
    0xaf4dc55e = MapPointLightType {
        lightColor: vec4 = { 0.207843155, 0.235294133, 0.250980407, 1 }
        radius: f32 = 2958
        castStaticShadows: bool = false
    }
    0xb04b885a = MapPointLightType {
        lightColor: vec4 = { 0.00392156886, 0.250980407, 0.160784319, 1 }
        radius: f32 = 453
        castStaticShadows: bool = false
    }
    0xb04dc6f1 = MapPointLightType {
        lightColor: vec4 = { 0.282352954, 0.278431386, 0.21960786, 1 }
        radius: f32 = 3290
        castStaticShadows: bool = false
    }
    0xb14b89ed = MapPointLightType {
        lightColor: vec4 = { 0.149019614, 0.345098048, 0.411764741, 1 }
        radius: f32 = 2803
        castStaticShadows: bool = false
    }
    0xb14dc884 = MapPointLightType {
        lightColor: vec4 = { 0.262745112, 0.305882365, 0.321568638, 1 }
        radius: f32 = 985
        castStaticShadows: bool = false
    }
    0xb24dca17 = MapPointLightType {
        lightColor: vec4 = { 0.00392156886, 0.223529428, 0.117647067, 1 }
        radius: f32 = 1162
        castStaticShadows: bool = false
    }
    0xb34dcbaa = MapPointLightType {
        lightColor: vec4 = { 0.290196091, 0.258823544, 0.176470593, 1 }
        radius: f32 = 1162
        castStaticShadows: bool = false
    }
    0xb44dcd3d = MapPointLightType {
        lightColor: vec4 = { 0.223529428, 0.168627456, 0.00392156886, 1 }
        radius: f32 = 985
        castStaticShadows: bool = false
    }
    "Maps/MapGeometry/Map12/Bilgewater" = mapContainer {
        mapPath: string = "Maps/MapGeometry/Map12/Bilgewater"
        components: list[pointer] = {
            MapBakeProperties {
                lightGridSize: u32 = 256
                lightGridFileName: string = "ASSETS/Maps/Lightmaps/Maps/MapGeometry/Map12/Bilgewater/LightGrid.dat"
            }
            MapSunProperties {
                sunColor: vec4 = { 0.525490224, 0.372549027, 0.227450982, 1 }
                sunDirection: vec3 = { -0.237114802, 0.969246686, 0.065860562 }
                skyLightColor: vec4 = { 0.568627477, 0.784313738, 0.925490201, 1 }
                horizonColor: vec4 = { 0.815686285, 0.819607854, 1, 1 }
                skyLightScale: f32 = 0.800000012
                lightMapColorScale: f32 = 2
                fogEnabled: bool = false
                fogColor: vec4 = { 0.39000535, 0.409994662, 0.310002297, 0.500007629 }
                fogAlternateColor: vec4 = { 0.319996953, 0.409994662, 0.330006868, 0.500007629 }
                fogStartAndEnd: vec2 = { -1000, -10000 }
            }
            MapLightingV2 {
                0xee91017d: f32 = 0.800000012
            }
        }
        boundsMin: vec2 = { -28.4299812, -19.0282936 }
        boundsMax: vec2 = { 12849.0957, 12858.4971 }
        lowestWalkableHeight: f32 = -220
        0xd4edb891: bool = false
        chunks: map[hash,link] = {
            "DefaultBilgewater" = "Maps/MapGeometry/Map12/Chunks/DefaultBilgewater"
        }
    }
    "Maps/MapGeometry/Map12/Chunks/DefaultBilgewater" = MapPlaceableContainer {
        items: map[hash,pointer] = {
            0xcc682dce = null
            0x0b3343b3 = null
            0xe791a27b = null
            0x9e03827c = null
            0x89983d00 = null
            0x9314ec2a = null
            0xadc2eaad = null
            0x4e295de0 = null
            0xfc37b57f = null
            0xfe55b7da = null
            0x8aea3fd1 = null
            0x183903f9 = null
            0x52dcff98 = null
            0xc581c724 = null
            0x97bbcd81 = null
            0xdf8543ec = null
            0x77ac7f76 = null
            0x8afa7960 = null
            0x86ac99a4 = null
            0xb31e4e6c = null
            0x84f89947 = null
            0x72d1b2df = null
            0x536bcee1 = null
            0xb0d3e77b = null
            0x63c94be5 = null
            0x658de10c = null
            0x412300d7 = null
            0x8aaba693 = null
            0x5c20b453 = null
            0xc13990e3 = null
            0xc7b64afd = null
            0xd0800aad = null
            0x9a85b10c = null
            0x14cdadf4 = null
            0xdb45b49f = null
            0xecbdb7f3 = null
            0xa706337a = null
            0xb288ecbf = null
            0x5860b498 = null
            0xbb3e5c33 = null
            0x5ea5a0e5 = null
            0x736932e9 = null
            0xd85976eb = null
            0x3b6037ff = null
            0xa13ac227 = null
            0xee1b088f = null
            0x9390305b = null
            0xdcb9ab59 = null
            0xc82f0024 = null
            0x172aab88 = null
            0x7bd7a689 = null
            0x12406d3f = null
            0xc93443e3 = null
            0xb9275da3 = null
            0xf08c4967 = null
            0xf81f45f4 = null
            0x3389f1b3 = null
            0x93ceb83e = null
            0x264885e8 = null
            0x7fe40166 = null
            0x37db2ce7 = null
            0x75f8902b = null
            0x1f46941a = null
            0xe57b96fc = null
            0xec3809ca = null
            0xa1220053 = null
            0x7ae1b56e = null
            0x050353e5 = null
            0x4be07eee = null
            0xb4bfda21 = null
            0x73bf6537 = null
            0xa6014b21 = null
            0x71369425 = null
            0x8f42446f = null
            0x00bc2ffd = null
            0xb529da6c = null
            0x78a938f4 = null
            0x28ff7988 = null
            0xc5e659e7 = null
            0x3ed5e39d = null
            0xd48639f6 = null
            0xed4a2f3e = null
            0x52a250d0 = null
            0x04a1c11d = null
            0x74890a98 = null
            0x39e525a8 = null
            0xa93a71cb = null
            0x6f4a4efe = null
            0xfb9a9807 = null
            0x0e7f58b5 = null
            0x3356a5a6 = null
            0xf140fae6 = null
            0xee08a83f = null
            0x2934fe3b = null
            0xdf3588d5 = null
            0x2df7c8f1 = null
            0x2e8698e2 = null
            0xe9082f1e = null
            0x037d79f0 = null
            0x2c351d75 = null
            0x0aecc50c = null
            0x48d136ee = null
            0xdf119cb9 = null
            0x10fb9cb3 = null
            0xcbbb6444 = null
            0x8cf4831e = null
            0x8fed8e50 = null
            0xd0900c39 = null
            0x357a5cea = null
            0x0a90dbba = null
            0xdb339d06 = null
            0x36bd7687 = null
            0xa75c3487 = null
            0x24f0dd08 = null
            0xe6172fef = null
            0x2b20f458 = null
            0xc9fbae78 = null
            0x29a5523f = null
            0x9c38d2e2 = null
            0xd5e91a3c = null
            0xae9ad8c0 = null
            0x329322a0 = null
            0x23f7aeff = null
            0x5844abba = null
            0x7ef39aaf = null
            0xc04368f4 = null
            0x3986f325 = null
            0x548a8707 = null
            0x54f600c8 = null
            0xdfab3cbc = null
            0xa44f4229 = null
            0x72d49390 = null
            0x03373694 = null
            0x9b7d3ec9 = null
            0xe476a150 = null
            0x2a97ada4 = null
            0x0c808498 = null
            0xe6c7c0eb = null
            0xec064f86 = null
            0x5322f85e = null
            0xaf8b5a5f = null
            0xc96b8c3a = null
            0x04edcb52 = null
            0x9c14ba50 = null
            0x18f2da31 = null
            0x6fdc7932 = null
            0x04786d8d = null
            0xe538148f = null
            0xc8cca7e2 = null
            0x585763c6 = null
            0xba624ab7 = null
            0x30463a09 = null
            0x6a992110 = null
            0x326e7d4a = null
            0x6752f7d1 = null
            0x5af7d49c = null
            0x533fd5af = null
            0x507915ff = null
            0x0c4f1c3f = null
            0xbb00440d = null
            0xf20d0ab0 = null
            0xe9aa11c1 = null
            0x4494fb82 = null
            0x98c4af9c = null
            0xf5b5b282 = null
            0x7a622a19 = null
            0xfc249b57 = null
            0xe9670866 = null
            0x139b2c6d = null
            0x32396961 = null
            0xbcc2c6e6 = null
            0xf29574f2 = null
            0xdbb53696 = null
            0x5f14757e = null
            0xd14f5249 = null
            0x08ab304b = null
            0x168debf2 = null
            0xf1d948cc = null
            0xae2d26d6 = null
            0x4e1d4699 = null
            0xc1a49a94 = null
            0x1bb0f1b5 = null
            0x3520515c = null
            0x9fd354e2 = null
            0x6ce7b89e = null
            0xe93c3757 = null
            0xff6a7996 = null
            0x0a65698f = null
            0x39238027 = null
            0x5cea950c = null
            0xb754556e = null
            0x061d1d8c = null
            0x39f66207 = null
            0xdc86bc61 = null
            0xf2594e5a = null
            0x128df9d7 = null
            0x8715dee1 = null
            0xd1bcba22 = null
            0xfc74ab4b = null
            0x53f96b5b = null
            0x723731fa = null
            0xde4dd2d1 = null
            0x46da9ab5 = null
            0xcc7f9b75 = null
            0x7f8bd0e6 = null
            0x1b7f67a9 = null
            0x0d275c5f = null
            0x2356c59e = null
            0xb018a3f2 = null
            0x60ea2a26 = null
            0x8c3cd052 = null
            0xddb8446f = null
            0xa2c82555 = null
            0x50083043 = null
            0xad10bf5f = null
            0x9ba3ce4d = null
            0xad866bf4 = null
            0x0d362fbb = null
            0x4ab7a908 = null
            0xf9750b70 = null
            0x63813e4d = null
            0x2b925aab = null
            0x198ca23f = null
            0xc7ae2822 = null
            0xe24e2e4f = null
            0xda412288 = null
            0x741bbecc = null
            0xd85fe09e = null
            0x4d4a6f84 = null
            0x4bbba68a = null
            0x1a35f4bc = null
            0xf559dd54 = null
            0x403d0842 = null
            0x7749fc80 = null
            0x10fafacb = null
            0x51d50107 = null
            0x9f0e596e = null
            0x6db4a5d3 = null
            0x179f59ef = null
            0xd677431c = null
            0xff36440e = null
            0x09a5eecc = null
            0x1945fba7 = null
            0xdf22f89d = null
            0x74c5ca33 = null
            0xc5ed9431 = null
            0xa04c4842 = null
            0x9d7b125c = null
            0x58aac6b0 = null
            0x15aea057 = null
            0xff9475f3 = null
            0x4a886217 = null
            0xbf545f06 = null
            0x0bfba503 = null
            0x1db9c99e = null
            0x59d024c8 = null
            0xedf4b5b7 = null
            0x19f222b1 = null
            0x5c26c548 = null
            0x53d8d5ad = null
            0x8190546a = null
            0xf36ac874 = null
            0xed1ba147 = null
            0x5b9efcfc = null
            0x8d64de63 = null
            0x95a8b71c = null
            0x9062365c = null
            0xd5f849cf = null
            0xea11ddf8 = null
            0xf3006530 = null
            0xeb37b12c = null
            0x278c81ed = null
            0x532598fc = null
            0x6bb7c12a = null
            0x9dd27a8a = null
            0xd17b9e7a = null
            0xa12e1950 = null
            0xd0de968b = null
            0x4e57f824 = null
            0x6e9ecb00 = null
            0xa41ddcc1 = null
            0x57acb8bc = null
            0x60cf0d22 = null
            0x88a72168 = null
            0xa6fd2658 = null
            0x73b560a0 = null
            0xa1322951 = null
            0x817b0c4b = null
            0x7b7184e7 = null
            0x9ef2d6c6 = null
            0xb9498637 = null
            0x7c91e93c = null
            0x4e8f7f35 = null
            0x62357f56 = null
            0xff11bdb0 = null
            0x89b8eff2 = null
            0xcb277a32 = null
            0x422d666c = null
            0x73c906d7 = null
            0xe78e3f87 = null
            0x79c2b19f = null
            0x7624cb9e = null
            0x28d7278d = null
            0x4251f9b1 = null
            0xf6975b35 = null
            0x5b636dbd = null
            0x70d085ad = null
            0xcea8ddc4 = null
            0xe299ee7b = null
            0x5db47465 = null
            0x460257a6 = null
            0x39274bf9 = null
            0xce408ed6 = null
            0x5ced13c5 = null
            0xa4bc55b5 = null
            0x14efc25c = null
            0xe864da1e = null
            0x174d735a = null
            0xb17fbe1d = null
            0x1a63c822 = null
            0xc1e82691 = null
            0x902baf47 = null
            0x23f157b6 = null
            0x561e3a96 = null
            0x9d1f579a = null
            0x7740a4cd = null
            0xaee64215 = null
            0xe51f01b1 = null
            0x685c0307 = null
            0xeee09ab9 = null
            0xa9a9eb02 = null
            0x40fb53af = null
            0x0a61c3de = null
            0x4a09e2d2 = null
            0xb9e3d565 = null
            0xeb443b26 = null
            0xf9963ac9 = null
            0x5c5e6958 = null
            0x365f8395 = null
            0xbc433f3d = null
            0x7343f7b6 = null
            0xda3be10e = null
            0x27c76723 = null
            0x91a85d1a = null
            0x9be9e193 = MapParticle {
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2014.21997, 1584.04004, 3266.82007, 1
                }
                name: string = "Audio-Emitter_map12_FireMed-Big1"
                system: link = "Maps/Particles/HA/Base/HA_Audio_Emitter_FireMed_Big"
            }
            0x08baebaa = MapParticle {
                transform: mtx44 = {
                    0.920504868, 0, 0.390731126, 0
                    0, 1, 0, 0
                    -0.390731126, 0, 0.920504868, 0
                    2339.3501, -57.158699, 2519.72998, 1
                }
                name: string = "BW_Motes_WespFly_01_1"
                system: link = "Maps/Particles/HA/Bilgewater/BW_Motes_WespFly_01"
            }
            0xcf9f7275 = MapParticle {
                transform: mtx44 = {
                    0.719339788, 0, 0.694658399, 0
                    0, 1, 0, 0
                    -0.694658399, 0, 0.719339788, 0
                    10414.4004, -183.662994, 9972.34961, 1
                }
                name: string = "BW_Chaos_Rain_and_Puddles1"
                system: link = "Maps/Particles/HA/Bilgewater/BW_Chaos_Rain_and_Puddles"
                groupName: string = "RUNETIMER_CHAOS"
            }
            0x19cef27e = MapParticle {
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    8084.45996, -175.488998, 8011.6001, 1
                }
                name: string = "BW_Motes_WespFly_01_3"
                system: link = "Maps/Particles/HA/Bilgewater/BW_Motes_WespFly_01"
            }
            0xf99ab7b9 = MapParticle {
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2079.75, -6317.77002, 9421.96973, 1
                }
                name: string = "BW_RiverPlain_01_1"
                system: link = "Maps/Particles/HA/Bilgewater/BW_RiverPlain_01"
            }
            0xccd96a5d = MapParticle {
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    3306.78003, -175.404999, 1577.19995, 1
                }
                name: string = "BW_FogLow_01_1"
                system: link = "Maps/Particles/HA/Bilgewater/BW_FogLow_01"
            }
            0x126d9f9c = MapParticle {
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2528.07007, -48.9864998, 556.247986, 1
                }
                name: string = "BW_FogLow_01_2"
                system: link = "Maps/Particles/HA/Bilgewater/BW_FogLow_01"
            }
            0x26f4dd7c = MapParticle {
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    4014.15991, -53.5881996, 2405.95996, 1
                }
                name: string = "BW_FogLow_02_1"
                system: link = "Maps/Particles/HA/Bilgewater/BW_FogLow_02"
            }
            0xd1b93697 = MapParticle {
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2901.83008, 107.461998, 4200.6499, 1
                }
                name: string = "BW_LanternGlow_02_1"
                system: link = "Maps/Particles/HA/Bilgewater/BW_LanternGlow_02"
            }
            0x97c7464b = MapParticle {
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    9146.16016, -66.3460999, 7883.8501, 1
                }
                name: string = "BW_Braziers_Fire1"
                system: link = "Maps/Particles/HA/Bilgewater/BW_Braziers_Fire"
            }
            0x5ad8d0a0 = MapParticle {
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    7836.7002, -112.855003, 6630.12988, 1
                }
                name: string = "BW_Braziers_Fire2"
                system: link = "Maps/Particles/HA/Bilgewater/BW_Braziers_Fire"
            }
            0x7fe44250 = MapParticle {
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    6103.8999, -86.3234024, 4882.64014, 1
                }
                name: string = "BW_Braziers_Fire3"
                system: link = "Maps/Particles/HA/Bilgewater/BW_Braziers_Fire"
            }
            0xd5bce353 = MapParticle {
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    3445.86011, -119.512001, 4769.06982, 1
                }
                name: string = "BW_Braziers_Fire4"
                system: link = "Maps/Particles/HA/Bilgewater/BW_Braziers_Fire"
            }
            0x4006929b = MapParticle {
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    3496.38989, -77.1283035, 4774.79004, 1
                }
                name: string = "BW_Braziers_Fire5"
                system: link = "Maps/Particles/HA/Bilgewater/BW_Braziers_Fire"
            }
            0x66a71a05 = MapParticle {
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    4851.81982, -99.8569031, 6099.9502, 1
                }
                name: string = "BW_Braziers_Fire6"
                system: link = "Maps/Particles/HA/Bilgewater/BW_Braziers_Fire"
            }
            0x447855d1 = MapParticle {
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    4870.85986, -114.887001, 6166.02979, 1
                }
                name: string = "BW_Braziers_Fire7"
                system: link = "Maps/Particles/HA/Bilgewater/BW_Braziers_Fire"
            }
            0xa324511e = MapParticle {
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    6610.47021, -132.126999, 7830.50977, 1
                }
                name: string = "BW_Braziers_Fire8"
                system: link = "Maps/Particles/HA/Bilgewater/BW_Braziers_Fire"
            }
            0xa78ea68f = MapParticle {
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    6654.2998, -95.4529037, 7837.66992, 1
                }
                name: string = "BW_Braziers_Fire9"
                system: link = "Maps/Particles/HA/Bilgewater/BW_Braziers_Fire"
            }
            0x0ba67e2a = MapParticle {
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    9251.91992, -177.641998, 8019.85986, 1
                }
                name: string = "BW_Braziers_Fire10"
                system: link = "Maps/Particles/HA/Bilgewater/BW_Braziers_Fire"
            }
            0x2666b5c6 = MapParticle {
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    8018.43018, -131.559006, 9171.61035, 1
                }
                name: string = "BW_Braziers_Fire11"
                system: link = "Maps/Particles/HA/Bilgewater/BW_Braziers_Fire"
            }
            0x463a2e9b = MapParticle {
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    8045.00977, -121.889, 9216.09961, 1
                }
                name: string = "BW_Braziers_Fire12"
                system: link = "Maps/Particles/HA/Bilgewater/BW_Braziers_Fire"
            }
            0x7f16537e = MapParticle {
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    7104.58984, -3653.41992, 3930.08008, 1
                }
                name: string = "BW_Braziers_Fire_Bigger1"
                system: link = "Maps/Particles/HA/Bilgewater/BW_Braziers_Fire_Bigger"
            }
            0x373bc6ec = MapParticle {
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    8623.30957, 116.434998, 9735.88965, 1
                }
                name: string = "BW_LanternGlow_02_2"
                system: link = "Maps/Particles/HA/Bilgewater/BW_LanternGlow_02"
            }
            0xc56fda1c = MapParticle {
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    8587.70996, 142.520996, 10650.0996, 1
                }
                name: string = "BW_LanternGlow_02_3"
                system: link = "Maps/Particles/HA/Bilgewater/BW_LanternGlow_02"
            }
            0xc847a1e6 = MapParticle {
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    -1351.97998, -4412.25, 12628.4004, 1
                }
                name: string = "BW_Peref_WaterFall_01_1"
                system: link = "Maps/Particles/HA/Bilgewater/BW_Peref_WaterFall_01"
            }
            0xc7988a74 = MapParticle {
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    3090.23999, -2074.12012, 7903.3999, 1
                }
                name: string = "BW_Peref_Steam_Generic1"
                system: link = "Maps/Particles/HA/Bilgewater/BW_Peref_Steam_Generic"
            }
            0xc1ee207c = MapParticle {
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    -1356.92004, -1749.06006, 8459.33008, 1
                }
                name: string = "BW_Peref_Steam_Generic2"
                system: link = "Maps/Particles/HA/Bilgewater/BW_Peref_Steam_Generic"
            }
            0x7205c962 = MapParticle {
                transform: mtx44 = {
                    0.992546141, 0, 0.121869348, 0
                    0, 1, 0, 0
                    -0.121869348, 0, 0.992546141, 0
                    -93.5196991, 167.029999, 4744.99023, 1
                }
                name: string = "BW_Peref_Godrays1"
                system: link = "Maps/Particles/HA/Bilgewater/BW_Peref_Godrays"
            }
            0x4c484dc5 = MapParticle {
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    -157.604996, 344.121002, 6446.52979, 1
                }
                name: string = "BW_Peref_Godrays2"
                system: link = "Maps/Particles/HA/Bilgewater/BW_Peref_Godrays"
            }
            0x6770adad = MapParticle {
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    6286.18994, 414.015015, 1022.97998, 1
                }
                name: string = "BW_Peref_Godrays3"
                system: link = "Maps/Particles/HA/Bilgewater/BW_Peref_Godrays"
            }
            0x4bb9ec11 = MapParticle {
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    7067.1499, -1725.29004, 1414.39001, 1
                }
                name: string = "BW_Peref_Steam_Generic3"
                system: link = "Maps/Particles/HA/Bilgewater/BW_Peref_Steam_Generic"
            }
            0x124cb069 = MapParticle {
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    5583.83984, 416.700989, 12992.7002, 1
                }
                name: string = "BW_Peref_Godrays4"
                system: link = "Maps/Particles/HA/Bilgewater/BW_Peref_Godrays"
            }
            0x77d92c1e = MapParticle {
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    -333.295013, 7.12902021, 12943.7002, 1
                }
                name: string = "BW_Peref_Godrays5"
                system: link = "Maps/Particles/HA/Bilgewater/BW_Peref_Godrays"
            }
            0x5cce8c20 = MapParticle {
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    549.16803, -1149.66003, 13277.7998, 1
                }
                name: string = "BW_Peref_Steam_Generic4"
                system: link = "Maps/Particles/HA/Bilgewater/BW_Peref_Steam_Generic"
            }
            0xf4cc64d5 = MapParticle {
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2609.84009, 417.582001, 10856.2002, 1
                }
                name: string = "BW_Peref_Godrays6"
                system: link = "Maps/Particles/HA/Bilgewater/BW_Peref_Godrays"
            }
            0x94decc70 = MapParticle {
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    105.248001, 375.78299, 7870.20996, 1
                }
                name: string = "BW_Peref_Godrays7"
                system: link = "Maps/Particles/HA/Bilgewater/BW_Peref_Godrays"
            }
            0x66d8cb6f = MapParticle {
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    -143.259995, 187.651993, 11088.7002, 1
                }
                name: string = "BW_Peref_Godrays8"
                system: link = "Maps/Particles/HA/Bilgewater/BW_Peref_Godrays"
            }
            0xb8db3cc8 = MapParticle {
                transform: mtx44 = {
                    0.629320443, 0, -0.777145922, 0
                    0, 1, 0, 0
                    0.777145922, 0, 0.629320443, 0
                    7088.91016, -892.359985, 11485.4004, 1
                }
                name: string = "BW_Peref_WindowGlow_1_1"
                system: link = "Maps/Particles/HA/Bilgewater/BW_Peref_WindowGlow_1"
            }
            0x2e139911 = MapParticle {
                transform: mtx44 = {
                    0.707106769, 0, -0.707106769, 0
                    0, 1, 0, 0
                    0.707106769, 0, 0.707106769, 0
                    6817.12012, -879.382019, 11841.2998, 1
                }
                name: string = "BW_Peref_WindowGlow_1_2"
                system: link = "Maps/Particles/HA/Bilgewater/BW_Peref_WindowGlow_1"
            }
            0x970835c1 = MapParticle {
                transform: mtx44 = {
                    0.920504868, 0, -0.390731126, 0
                    0, 1, 0, 0
                    0.390731126, 0, 0.920504868, 0
                    8692.33008, -448.614014, 13095.2002, 1
                }
                name: string = "BW_Peref_WindowGlow_1_3"
                system: link = "Maps/Particles/HA/Bilgewater/BW_Peref_WindowGlow_1"
            }
            0xe5b2db3a = MapParticle {
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    5338.93018, -2083.30005, 13948.5996, 1
                }
                name: string = "BW_Peref_WindowGlow_1_4"
                system: link = "Maps/Particles/HA/Bilgewater/BW_Peref_WindowGlow_1"
            }
            0x212ee425 = MapParticle {
                transform: mtx44 = {
                    0.453990519, 0, 0.891006529, 0
                    0, 1, 0, 0
                    -0.891006529, 0, 0.453990519, 0
                    -470.554993, -686.049011, 3115.8501, 1
                }
                name: string = "BW_Peref_WindowGlow_1_5"
                system: link = "Maps/Particles/HA/Bilgewater/BW_Peref_WindowGlow_1"
            }
            0x0d04e191 = MapParticle {
                transform: mtx44 = {
                    -0.406736642, 0, -0.91354543, 0
                    0, 1, 0, 0
                    0.91354543, 0, -0.406736642, 0
                    -408.407013, -713.872009, 3268.44995, 1
                }
                name: string = "BW_Peref_WindowGlow_1_6"
                system: link = "Maps/Particles/HA/Bilgewater/BW_Peref_WindowGlow_1"
            }
            0x8fda192d = MapParticle {
                transform: mtx44 = {
                    0.857167304, 0, -0.515038073, 0
                    0, 1, 0, 0
                    0.515038073, 0, 0.857167304, 0
                    13142.5, -1191.64001, 7716, 1
                }
                name: string = "BW_Peref_WindowGlow_1_7"
                system: link = "Maps/Particles/HA/Bilgewater/BW_Peref_WindowGlow_1"
            }
            0xc20773f6 = MapParticle {
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1512.16003, 185.600998, 3800.09009, 1
                }
                name: string = "BW_LanternGlow_02_4"
                system: link = "Maps/Particles/HA/Bilgewater/BW_LanternGlow_02"
            }
            0xa8d8d50f = MapParticle {
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1049.19995, 173.957001, 3342.91992, 1
                }
                name: string = "BW_LanternGlow_02_5"
                system: link = "Maps/Particles/HA/Bilgewater/BW_LanternGlow_02"
            }
            0xd4aaeef8 = MapParticle {
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    555.999023, 176.580994, 2874.83008, 1
                }
                name: string = "BW_LanternGlow_02_6"
                system: link = "Maps/Particles/HA/Bilgewater/BW_LanternGlow_02"
            }
            0xdc859166 = MapParticle {
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1990.08997, 174.449997, 4260.04004, 1
                }
                name: string = "BW_LanternGlow_02_7"
                system: link = "Maps/Particles/HA/Bilgewater/BW_LanternGlow_02"
            }
            0xe6d125e6 = MapParticle {
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2241.70996, 173.690002, 162.574997, 1
                }
                name: string = "BW_LanternGlow_02_8"
                system: link = "Maps/Particles/HA/Bilgewater/BW_LanternGlow_02"
            }
            0x83585842 = MapParticle {
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2719.88989, 189.401001, 636.135986, 1
                }
                name: string = "BW_LanternGlow_02_9"
                system: link = "Maps/Particles/HA/Bilgewater/BW_LanternGlow_02"
            }
            0x9b336539 = MapParticle {
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    3201.03003, 170.723007, 1091.88, 1
                }
                name: string = "BW_LanternGlow_02_10"
                system: link = "Maps/Particles/HA/Bilgewater/BW_LanternGlow_02"
            }
            0x9382c4aa = MapParticle {
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    3684.82007, 180.507996, 1545.60999, 1
                }
                name: string = "BW_LanternGlow_02_11"
                system: link = "Maps/Particles/HA/Bilgewater/BW_LanternGlow_02"
            }
            0xd14e29a2 = MapParticle {
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    4162.68018, 158.341995, 2017.48999, 1
                }
                name: string = "BW_LanternGlow_02_12"
                system: link = "Maps/Particles/HA/Bilgewater/BW_LanternGlow_02"
            }
            0xd539fc96 = MapParticle {
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    9062.55957, 155.212006, 11110.5, 1
                }
                name: string = "BW_LanternGlow_02_13"
                system: link = "Maps/Particles/HA/Bilgewater/BW_LanternGlow_02"
            }
            0xe7a3fe7e = MapParticle {
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    9538.08984, 151.440002, 11560.7002, 1
                }
                name: string = "BW_LanternGlow_02_14"
                system: link = "Maps/Particles/HA/Bilgewater/BW_LanternGlow_02"
            }
            0xa7cda2e5 = MapParticle {
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    4081.84009, 101.053001, 2967.38989, 1
                }
                name: string = "BW_LanternGlow_02_15"
                system: link = "Maps/Particles/HA/Bilgewater/BW_LanternGlow_02"
            }
            0x313af9fb = MapParticle {
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    10017.2998, 151.434998, 12026.5, 1
                }
                name: string = "BW_LanternGlow_02_16"
                system: link = "Maps/Particles/HA/Bilgewater/BW_LanternGlow_02"
            }
            0x17d8bd31 = MapParticle {
                transform: mtx44 = {
                    0.77199918, 0.0839802027, -0.630051196, 0
                    0.183577999, 0.919532955, 0.347502887, 0
                    0.608536184, -0.383935511, 0.694461823, 0
                    12662.6094, 185.607925, 10120.9365, 1
                }
                name: string = "BW_LanternGlow_02_17"
                system: link = "Maps/Particles/HA/Bilgewater/BW_LanternGlow_02"
            }
            0xa4c1e1cc = MapParticle {
                transform: mtx44 = {
                    0.272060037, 0.00533525739, -0.962265491, 0
                    0.726548314, 0.654543817, 0.209045127, 0
                    0.630960226, -0.756005168, 0.174198896, 0
                    12193.2998, 192.570007, 9763.08008, 1
                }
                name: string = "BW_LanternGlow_02_18"
                system: link = "Maps/Particles/HA/Bilgewater/BW_LanternGlow_02"
            }
            0x09d7c4f7 = MapParticle {
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    11713, 123.236, 9303.69043, 1
                }
                name: string = "BW_LanternGlow_02_19"
                system: link = "Maps/Particles/HA/Bilgewater/BW_LanternGlow_02"
            }
            0x0e6a3d8d = MapParticle {
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    11235.9004, 140.692993, 8862.66016, 1
                }
                name: string = "BW_LanternGlow_02_20"
                system: link = "Maps/Particles/HA/Bilgewater/BW_LanternGlow_02"
            }
            0x5da680aa = MapParticle {
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    10756.2998, 163.348007, 8374.48047, 1
                }
                name: string = "BW_LanternGlow_02_21"
                system: link = "Maps/Particles/HA/Bilgewater/BW_LanternGlow_02"
            }
            0x44ac2de4 = MapParticle {
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    9813.66016, 121.480003, 8491.80957, 1
                }
                name: string = "BW_LanternGlow_02_22"
                system: link = "Maps/Particles/HA/Bilgewater/BW_LanternGlow_02"
            }
            0xf8b19fb2 = MapParticle {
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    13248.3965, 141.201279, 10659.0742, 1
                }
                name: string = "BW_LanternGlow_02_23"
                system: link = "Maps/Particles/HA/Bilgewater/BW_LanternGlow_02"
            }
            0x8cc0d48e = MapParticle {
                transform: mtx44 = {
                    0.906307757, 0, 0.42261827, 0
                    0, 1, 0, 0
                    -0.42261827, 0, 0.906307757, 0
                    11873.7002, -6315.22021, 1746.92004, 1
                }
                name: string = "BW_River_WaterEdge_01_1"
                system: link = "Maps/Particles/HA/Bilgewater/BW_River_WaterEdge_01"
            }
            0x4e1f9545 = MapParticle {
                transform: mtx44 = {
                    0.707106769, 0, 0.707106769, 0
                    0, 1, 0, 0
                    -0.707106769, 0, 0.707106769, 0
                    9296.01953, -6289.97021, 4827.3501, 1
                }
                name: string = "BW_River_WaterEdge_02_1"
                system: link = "Maps/Particles/HA/Bilgewater/BW_River_WaterEdge_02"
            }
            0xe7d8435b = MapParticle {
                transform: mtx44 = {
                    0.819152057, 0, 0.57357645, 0
                    0, 1, 0, 0
                    -0.57357645, 0, 0.819152057, 0
                    7795.56006, -6349.52979, 4996.37988, 1
                }
                name: string = "BW_River_WaterEdge_03_1"
                system: link = "Maps/Particles/HA/Bilgewater/BW_River_WaterEdge_03"
            }
            0x3a3da510 = MapParticle {
                transform: mtx44 = {
                    0.777145922, 0, 0.629320383, 0
                    0, 1, 0, 0
                    -0.629320383, 0, 0.777145922, 0
                    6963.68018, -6311.33008, 2609.79004, 1
                }
                name: string = "BW_River_WaterEdge_04_1"
                system: link = "Maps/Particles/HA/Bilgewater/BW_River_WaterEdge_04"
            }
            0x27727846 = MapParticle {
                transform: mtx44 = {
                    0.681998372, 0, 0.7313537, 0
                    0, 1, 0, 0
                    -0.7313537, 0, 0.681998372, 0
                    5441, -6258.37012, 7500.25, 1
                }
                name: string = "BW_River_WaterEdge_05_1"
                system: link = "Maps/Particles/HA/Bilgewater/BW_River_WaterEdge_05"
            }
            0xb78825bf = MapParticle {
                transform: mtx44 = {
                    0.927183867, 0, -0.37460658, 0
                    0, 1, 0, 0
                    0.37460658, 0, 0.927183867, 0
                    2309.83008, -6193.74023, 12386.2998, 1
                }
                name: string = "BW_River_WaterEdge_05_2"
                system: link = "Maps/Particles/HA/Bilgewater/BW_River_WaterEdge_05"
            }
            0x8a6e67cf = MapParticle {
                transform: mtx44 = {
                    0.74314481, 0, 0.669130623, 0
                    0, 1, 0, 0
                    -0.669130623, 0, 0.74314481, 0
                    2395.78003, -6295.20996, 10109, 1
                }
                name: string = "BW_River_WaterEdge_06_1"
                system: link = "Maps/Particles/HA/Bilgewater/BW_River_WaterEdge_06"
            }
            0x1e476d9a = MapParticle {
                transform: mtx44 = {
                    0.848048091, 0, -0.529919267, 0
                    0, 1, 0, 0
                    0.529919267, 0, 0.848048091, 0
                    2575.55005, -6059.56006, 14686.5996, 1
                }
                name: string = "BW_River_WaterEdge_06_2"
                system: link = "Maps/Particles/HA/Bilgewater/BW_River_WaterEdge_06"
            }
            0xf53c45bc = MapParticle {
                transform: mtx44 = {
                    0.601815045, 0, 0.798635542, 0
                    0, 1, 0, 0
                    -0.798635542, 0, 0.601815045, 0
                    2885.34009, -6353.68018, 16002.5, 1
                }
                name: string = "BW_River_WaterEdge_07_1"
                system: link = "Maps/Particles/HA/Bilgewater/BW_River_WaterEdge_07"
            }
            0xc0d3b8a9 = MapParticle {
                transform: mtx44 = {
                    0.694658399, 0, 0.719339788, 0
                    0, 1, 0, 0
                    -0.719339788, 0, 0.694658399, 0
                    49.3007011, -6283.56982, 16969.9004, 1
                }
                name: string = "BW_River_WaterEdge_08_1"
                system: link = "Maps/Particles/HA/Bilgewater/BW_River_WaterEdge_08"
            }
            0x5c0f971b = MapParticle {
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    12211, -1757.06995, 5289.02979, 1
                }
                name: string = "BW_Chimney_Smoke1"
                system: link = "Maps/Particles/HA/Bilgewater/BW_Chimney_Smoke"
            }
            0x294cd3b0 = MapParticle {
                transform: mtx44 = {
                    0.754709601, 0, 0.656059027, 0
                    0, 1, 0, 0
                    -0.656059027, 0, 0.754709601, 0
                    4781.56006, -791.419983, 2820.55005, 1
                }
                name: string = "BW_Cannon_Smoke1"
                system: link = "Maps/Particles/HA/Bilgewater/BW_Cannon_Smoke"
            }
            0x7dede0a9 = MapParticle {
                transform: mtx44 = {
                    0.629320443, 0, 0.777145922, 0
                    0, 1, 0, 0
                    -0.777145922, 0, 0.629320443, 0
                    9992.41992, -775.502991, 7834.8999, 1
                }
                name: string = "BW_Cannon_Smoke2"
                system: link = "Maps/Particles/HA/Bilgewater/BW_Cannon_Smoke"
            }
            0x1d5007f1 = MapParticle {
                transform: mtx44 = {
                    0.981627166, 0, -0.190808997, 0
                    0.0493850037, 0.965925813, 0.254063815, 0
                    0.184307337, -0.258819044, 0.948179007, 0
                    8515.36035, -416.523987, 6979.08008, 1
                }
                name: string = "BW_Cannon_Smoke3"
                system: link = "Maps/Particles/HA/Bilgewater/BW_Cannon_Smoke"
            }
            0x764b1e27 = MapParticle {
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    12108.7354, 251.28125, 12186.3057, 1
                }
                name: string = "BW_Braziers_Fire13"
                system: link = "Maps/Particles/HA/Bilgewater/BW_Braziers_Fire"
            }
            0xff019570 = MapParticle {
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    8761.19043, -3637.41992, 5526.1001, 1
                }
                name: string = "BW_BrazierDoor_Smoke1"
                system: link = "Maps/Particles/HA/Bilgewater/BW_BrazierDoor_Smoke"
            }
            0x92dffc9b = MapParticle {
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    7100.25, -3675.78003, 3997.12988, 1
                }
                name: string = "BW_BrazierDoor_Smoke2"
                system: link = "Maps/Particles/HA/Bilgewater/BW_BrazierDoor_Smoke"
            }
            0xafde032b = MapParticle {
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    12559.9746, 261.327301, 11704.9863, 1
                }
                name: string = "BW_Braziers_Fire14"
                system: link = "Maps/Particles/HA/Bilgewater/BW_Braziers_Fire"
            }
            0xbee63841 = MapParticle {
                transform: mtx44 = {
                    0.529919267, 0, -0.848048091, 0
                    -0.344932228, 0.91354543, -0.215537578, 0
                    0.774730444, 0.406736642, 0.484105319, 0
                    12592.2002, -67.2109985, 11205.0996, 1
                }
                name: string = "BW_Cannon_Smoke4"
                system: link = "Maps/Particles/HA/Bilgewater/BW_Cannon_Smoke"
            }
            0x0a898f81 = MapParticle {
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    10942.9004, -110.828003, 10728.2002, 1
                }
                name: string = "BW_AP_Chaos_Nexus_Idle1"
                system: link = "Maps/Particles/HA/Bilgewater/BW_AP_Chaos_Nexus_Idle"
            }
            0x892dc02a = MapParticle {
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    9696.2002, 61.3362999, 9480.75, 1
                }
                name: string = "BW_AP_Chaos_Inhib_Idle_2_1"
                system: link = "Maps/Particles/HA/Bilgewater/BW_AP_Chaos_Inhib_Idle_2"
            }
            0x7261e8a0 = MapParticle {
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    3113.48999, -60.901001, 3158.76001, 1
                }
                name: string = "BW_AP_Order_Inhib_Idle2_1"
                system: link = "Maps/Particles/HA/Bilgewater/BW_AP_Order_Inhib_Idle2"
            }
            0xcc0dfae8 = MapParticle {
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    4844.7998, -169.138, 6156.64014, 1
                }
                name: string = "BW_Audio-Emitter_Fire1"
                system: link = "Maps/Particles/HA/Bilgewater/BW_Audio_Emitter_Fire"
            }
            0x7b5cbe37 = MapParticle {
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    3486.98999, -169.138, 4841.06006, 1
                }
                name: string = "BW_Audio-Emitter_Fire2"
                system: link = "Maps/Particles/HA/Bilgewater/BW_Audio_Emitter_Fire"
            }
            0xe4653b69 = MapParticle {
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    6630.1499, -176.339005, 7871.2002, 1
                }
                name: string = "BW_Audio-Emitter_Fire3"
                system: link = "Maps/Particles/HA/Bilgewater/BW_Audio_Emitter_Fire"
            }
            0xf40bc70d = MapParticle {
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    6155.7998, -169.138, 4820.47021, 1
                }
                name: string = "BW_Audio-Emitter_Fire4"
                system: link = "Maps/Particles/HA/Bilgewater/BW_Audio_Emitter_Fire"
            }
            0x904ea1c1 = MapParticle {
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    9300.65039, -169.138, 7893.93994, 1
                }
                name: string = "BW_Audio-Emitter_Fire5"
                system: link = "Maps/Particles/HA/Bilgewater/BW_Audio_Emitter_Fire"
            }
            0xa6d809bf = MapParticle {
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    8033.0498, -169.138, 9230.9502, 1
                }
                name: string = "BW_Audio-Emitter_Fire6"
                system: link = "Maps/Particles/HA/Bilgewater/BW_Audio_Emitter_Fire"
            }
            0xbb798ae8 = MapParticle {
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    7930.85986, -169.138, 6553.75977, 1
                }
                name: string = "BW_Audio-Emitter_Fire7"
                system: link = "Maps/Particles/HA/Bilgewater/BW_Audio_Emitter_Fire"
            }
            0x09042142 = MapParticle {
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    4778.0498, -169.138, 3522.27002, 1
                }
                name: string = "BW_Audio-Emitter_Fire8"
                system: link = "Maps/Particles/HA/Bilgewater/BW_Audio_Emitter_Fire"
            }
            0x51573c73 = MapParticle {
                transform: mtx44 = {
                    0.886617362, 0.0849636197, 0.45463264, 0
                    -0.452600807, -0.0429356806, 0.890678942, 0
                    0.0951952636, -0.995458484, 0.000387083215, 0
                    12071.6689, 191.751129, 12207.5381, 1
                }
                name: string = "BW_Audio-Emitter_Fire9"
                system: link = "Maps/Particles/HA/Bilgewater/BW_Audio_Emitter_Fire"
            }
            0x447ac893 = MapParticle {
                transform: mtx44 = {
                    0.38801837, -0.00324979634, 0.921645939, 0
                    0.921598911, 0.0120710414, -0.387955993, 0
                    -0.00986444764, 0.999921918, 0.00767879374, 0
                    12577.5137, 209.699951, 11671.6982, 1
                }
                name: string = "BW_Audio-Emitter_Fire10"
                system: link = "Maps/Particles/HA/Bilgewater/BW_Audio_Emitter_Fire"
            }
            0xef4be341 = MapParticle {
                transform: mtx44 = {
                    0.748410523, -0.0309016109, 0.662515461, 0
                    0.495327294, 0.690330029, -0.527347505, 0
                    -0.441058397, 0.722834408, 0.531956673, 0
                    12891.5, 256.800995, 9435.75, 1
                }
                name: string = "BW_Audio-Emitter_Pub1"
                system: link = "Maps/Particles/HA/Bilgewater/BW_Audio_Emitter_Pub"
            }
            0x42290b4e = MapParticle {
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    8456.59961, -306.391998, 12171.2998, 1
                }
                name: string = "BW_Audio-Emitter_Shootout_Cannons1"
                system: link = "Maps/Particles/HA/Bilgewater/BW_Audio_Emitter_Shootout_Cannons"
            }
            0xaea5b212 = MapParticle {
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    -171.408997, -169.138, 3544.51001, 1
                }
                name: string = "BW_Audio-Emitter_Shootout_Cannons2"
                system: link = "Maps/Particles/HA/Bilgewater/BW_Audio_Emitter_Shootout_Cannons"
            }
            0xa2ecd40d = MapParticle {
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    13620.4004, -169.138, 4723.45996, 1
                }
                name: string = "BW_Audio-Emitter_Shootout_Cannons3"
                system: link = "Maps/Particles/HA/Bilgewater/BW_Audio_Emitter_Shootout_Cannons"
            }
            0x31be23ea = MapParticle {
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    13478.2998, -169.138, 1171.93005, 1
                }
                name: string = "BW_Audio-Emitter_Shootout_Cannons4"
                system: link = "Maps/Particles/HA/Bilgewater/BW_Audio_Emitter_Shootout_Cannons"
            }
            0x3752dc10 = MapParticle {
                transform: mtx44 = {
                    0.871194959, 0.104726426, -0.479637057, 0
                    -0.486375034, 0.316997111, -0.81421876, 0
                    0.0667733401, 0.942626774, 0.327102602, 0
                    8484.48047, 284.147003, 6966.93018, 1
                }
                name: string = "BW_Audio-Emitter_BridgeCreak1"
                system: link = "Maps/Particles/HA/Bilgewater/BW_Audio_Emitter_BridgeCreak"
            }
            0x7704c26f = MapParticle {
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    5020.81006, -169.138, 3678.08008, 1
                }
                name: string = "BW_Audio-Emitter_BridgeCreak2"
                system: link = "Maps/Particles/HA/Bilgewater/BW_Audio_Emitter_BridgeCreak"
            }
            0xa6d2da10 = MapParticle {
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    5745.99023, -68.979599, 836.552002, 1
                }
                name: string = "BW_Audio-Emitter_ShipMast1"
                system: link = "Maps/Particles/HA/Bilgewater/BW_Audio_Emitter_ShipMast"
            }
            0x1e8be098 = MapParticle {
                transform: mtx44 = {
                    0.886965752, 0.432889551, 0.160929993, 0
                    0.0831073821, 0.193163097, -0.977640629, 0
                    -0.454296142, 0.880508184, 0.135352731, 0
                    230.669998, 896.041016, 243.813004, 1
                }
                name: string = "BW_Audio-Emitter_ShipMast2"
                system: link = "Maps/Particles/HA/Bilgewater/BW_Audio_Emitter_ShipMast"
            }
            0xbacea36b = MapParticle {
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    12655.5996, -169.138, 6683.25, 1
                }
                name: string = "BW_Audio-Emitter_ShipMast3"
                system: link = "Maps/Particles/HA/Bilgewater/BW_Audio_Emitter_ShipMast"
            }
            0xe7aaaa4e = MapParticle {
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2368.22998, -169.138, 4864.4502, 1
                }
                name: string = "BW_Audio-Emitter_ShipMast4"
                system: link = "Maps/Particles/HA/Bilgewater/BW_Audio_Emitter_ShipMast"
            }
            0xb71f5eb8 = MapParticle {
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    9684.26953, 389.52301, 12760.2002, 1
                }
                name: string = "BW_Audio-Emitter_ShipMast5"
                system: link = "Maps/Particles/HA/Bilgewater/BW_Audio_Emitter_ShipMast"
            }
            0x565638cb = MapParticle {
                transform: mtx44 = {
                    0.852361739, -0.336450428, 0.40035063, 0
                    0.440429062, 0.0490787774, -0.896444976, 0
                    0.281960577, 0.940421402, 0.19001542, 0
                    -1131.33997, -2934.83008, 12420.4004, 1
                }
                name: string = "BW_Audio-Emitter_Waterfall1"
                system: link = "Maps/Particles/HA/Bilgewater/BW_Audio_Emitter_Waterfall"
            }
            0x58d69fd4 = MapParticle {
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2678.22998, -965.245972, 7097.6499, 1
                }
                name: string = "BW_Audio-Emitter_River1"
                system: link = "Maps/Particles/HA/Bilgewater/BW_Audio_Emitter_River"
            }
            0xc3837728 = MapParticle {
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2303.01001, -169.138, 11942, 1
                }
                name: string = "BW_Audio-Emitter_River2"
                system: link = "Maps/Particles/HA/Bilgewater/BW_Audio_Emitter_River"
            }
            0x05e50d1a = MapParticle {
                transform: mtx44 = {
                    0.826236427, -0.00517085707, -0.563299716, 0
                    -0.556037426, 0.152821362, -0.816987097, 0
                    0.0903087631, 0.988240302, 0.123391405, 0
                    2066.84009, -1149.39001, 10311.4004, 1
                }
                name: string = "BW_Audio-Emitter_River3"
                system: link = "Maps/Particles/HA/Bilgewater/BW_Audio_Emitter_River"
            }
            0x9b80e5a0 = MapParticle {
                transform: mtx44 = {
                    0.827852666, 0.233906031, -0.509850919, 0
                    -0.0499089956, 0.936022222, 0.348384082, 0
                    0.558720946, -0.262964547, 0.786562443, 0
                    7992.22998, -2069.37012, 3477.18994, 1
                }
                name: string = "BW_Audio-Emitter_River4"
                system: link = "Maps/Particles/HA/Bilgewater/BW_Audio_Emitter_River"
            }
            0xba12a710 = MapParticle {
                transform: mtx44 = {
                    0.592546105, 9.8256045e-05, 0.805536509, 0
                    -0.805526078, 0.00516700046, 0.592537761, 0
                    -0.00410398701, -0.999986649, 0.00314083369, 0
                    432.802002, 876.765991, 1951.15002, 1
                }
                name: string = "BW_Audio-Emitter_Rope1"
                system: link = "Maps/Particles/HA/Bilgewater/BW_Audio_Emitter_Rope"
            }
            0xbf14ee2e = MapParticle {
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2895.04004, -1008.71002, 283.723999, 1
                }
                name: string = "BW_Audio-Emitter_PubSouth1"
                system: link = "Maps/Particles/HA/Bilgewater/BW_Audio_Emitter_PubSouth"
            }
            0x3dd14be9 = MapParticle {
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    9607.91016, -169.138, 12889.7002, 1
                }
                name: string = "BW_Audio-Emitter_PubShark1"
                system: link = "Maps/Particles/HA/Bilgewater/BW_Audio_Emitter_PubShark"
            }
            0x3c0d5061 = MapParticle {
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    9689.87988, -190.740005, 9516.04004, 1
                }
                name: string = "BW_Chaos_Inhibitor_runeTimer1"
                system: link = "Maps/Particles/HA/Bilgewater/BW_Chaos_Inhibitor_runeTimer"
                groupName: string = "RUNETIMER_CHAOS"
            }
            0x6b229184 = MapParticle {
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    9689.87988, -190.740005, 9516.04004, 1
                }
                name: string = "BW_AP_Chaos_Inhib_Rubble_Dust1"
                system: link = "Maps/Particles/HA/Bilgewater/BW_AP_Chaos_Inhib_Rubble_Dust"
                groupName: string = "RUNETIMER_CHAOS"
            }
            0xb2a6a647 = MapParticle {
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    3099.44995, -199.671005, 3194.15991, 1
                }
                name: string = "BW_Order_Inhibitor_runeTimer1"
                system: link = "Maps/Particles/HA/Bilgewater/BW_Order_Inhibitor_runeTimer"
                groupName: string = "RUNETIMER_ORDER"
            }
            0xdb13dcf0 = MapParticle {
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    3099.44995, -199.671005, 3194.15991, 1
                }
                name: string = "BW_AP_Order_Inhib_Rubble_Dust1"
                system: link = "Maps/Particles/HA/Bilgewater/BW_AP_Order_Inhib_Rubble_Dust"
                groupName: string = "RUNETIMER_ORDER"
            }
            0x3b0ee82e = MapParticle {
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    661.400024, 455.769989, 745.125977, 1
                }
                name: string = "BW_Order_StartingPlatform_Pearl1"
                system: link = "Maps/Particles/HA/Bilgewater/BW_Order_StartingPlatform_Pearl"
            }
            0x31a71fb0 = MapParticle {
                transform: mtx44 = {
                    0.777145922, 0, 0.629320383, 0
                    0, 1, 0, 0
                    -0.629320383, 0, 0.777145922, 0
                    12339.2881, 380.676025, 11939.0742, 1
                }
                name: string = "BW_Chaos_StartingPlatform_RedGem1"
                system: link = "Maps/Particles/HA/Bilgewater/BW_Chaos_StartingPlatform_RedGem"
            }
            0x00444ccc = MapParticle {
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    11752.5996, -1107.08997, 9459.83008, 1
                }
                name: string = "BW_Audio-Emitter_BridgeCreak3"
                system: link = "Maps/Particles/HA/Bilgewater/BW_Audio_Emitter_BridgeCreak"
            }
            0x26c704cc = MapParticle {
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    -258.481995, -169.138, 4657.02002, 1
                }
                name: string = "BW_Audio-Emitter_BridgeCreak4"
                system: link = "Maps/Particles/HA/Bilgewater/BW_Audio_Emitter_BridgeCreak"
            }
            0x3f0adc6c = MapParticle {
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2194.53003, -684.23999, 499.875, 1
                }
                name: string = "BW_Audio-Emitter_BridgeCreak5"
                system: link = "Maps/Particles/HA/Bilgewater/BW_Audio_Emitter_BridgeCreak"
            }
            0x66534d44 = MapParticle {
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    9974.99023, -169.138, 11741.5, 1
                }
                name: string = "BW_Audio-Emitter_BridgeCreak6"
                system: link = "Maps/Particles/HA/Bilgewater/BW_Audio_Emitter_BridgeCreak"
            }
            0x2da51ac7 = MapParticle {
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    13517.2998, -169.138, 7353.95996, 1
                }
                name: string = "BW_Audio-Emitter_Shootout_Cannons5"
                system: link = "Maps/Particles/HA/Bilgewater/BW_Audio_Emitter_Shootout_Cannons"
            }
            0x0600e29a = MapParticle {
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    10685.7002, -169.138, 13420.2002, 1
                }
                name: string = "BW_Audio-Emitter_Shootout_Cannons6"
                system: link = "Maps/Particles/HA/Bilgewater/BW_Audio_Emitter_Shootout_Cannons"
            }
            0xb0106f5f = MapParticle {
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    6906.54004, -169.138, 4025.58008, 1
                }
                name: string = "BW_Audio-Emitter_ShipMast6"
                system: link = "Maps/Particles/HA/Bilgewater/BW_Audio_Emitter_ShipMast"
            }
            0x49c4fe65 = MapParticle {
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1682.46997, -1670.62, 4568.27002, 1
                }
                name: string = "BW_Audio-Emitter_Shootout_Cannons7"
                system: link = "Maps/Particles/HA/Bilgewater/BW_Audio_Emitter_Shootout_Cannons"
            }
            0x2bb43691 = MapParticle {
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    10123.7002, -169.138, 7072.62988, 1
                }
                name: string = "BW_Audio-Emitter_ShipMast7"
                system: link = "Maps/Particles/HA/Bilgewater/BW_Audio_Emitter_ShipMast"
            }
            0xe7606dd6 = MapParticle {
                transform: mtx44 = {
                    0.933580399, 0, -0.35836795, 0
                    -0.0187555309, 0.99862951, -0.0488598272, 0
                    0.357876807, 0.0523359589, 0.932300925, 0
                    5978.02002, -1219.62, 12651.2998, 1
                }
                name: string = "BW_Peref_WindowGlow_1_8"
                system: link = "Maps/Particles/HA/Bilgewater/BW_Peref_WindowGlow_1"
            }
            0x40d1c4a8 = MapParticle {
                transform: mtx44 = {
                    0.615661502, 0, -0.788010716, 0
                    0, 1, 0, 0
                    0.788010716, 0, 0.615661502, 0
                    7064.45996, -453.747009, 11743.2002, 1
                }
                name: string = "BW_Peref_WindowGlow_1_9"
                system: link = "Maps/Particles/HA/Bilgewater/BW_Peref_WindowGlow_1"
            }
            0xa1067f71 = MapParticle {
                transform: mtx44 = {
                    0.7313537, 0, -0.681998372, 0
                    0, 1, 0, 0
                    0.681998372, 0, 0.7313537, 0
                    6580.52002, -1268.69995, 10918.0996, 1
                }
                name: string = "BW_Peref_WindowGlow_1_10"
                system: link = "Maps/Particles/HA/Bilgewater/BW_Peref_WindowGlow_1"
            }
            0xd8b54093 = MapParticle {
                transform: mtx44 = {
                    0.681998372, 0, -0.7313537, 0
                    0, 1, 0, 0
                    0.7313537, 0, 0.681998372, 0
                    4927.6001, -2235.04004, 11647.9004, 1
                }
                name: string = "BW_Peref_WindowGlow_1_11"
                system: link = "Maps/Particles/HA/Bilgewater/BW_Peref_WindowGlow_1"
            }
            0x4ae8178d = MapParticle {
                transform: mtx44 = {
                    0.669130564, 0, -0.74314487, 0
                    0, 1, 0, 0
                    0.74314487, 0, 0.669130564, 0
                    6537.35986, -1669.75, 11009.7002, 1
                }
                name: string = "BW_Peref_WindowGlow_1_12"
                system: link = "Maps/Particles/HA/Bilgewater/BW_Peref_WindowGlow_1"
            }
            0x96c8e871 = MapParticle {
                transform: mtx44 = {
                    0.920504868, 0, -0.390731126, 0
                    0, 1, 0, 0
                    0.390731126, 0, 0.920504868, 0
                    8211.49023, -474.901001, 13321.9004, 1
                }
                name: string = "BW_Peref_WindowGlow_1_13"
                system: link = "Maps/Particles/HA/Bilgewater/BW_Peref_WindowGlow_1"
            }
            0xbc96ab23 = MapParticle {
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    5111.93018, -169.138, 4453.5498, 1
                }
                name: string = "BW_FogLow_01_3"
                system: link = "Maps/Particles/HA/Bilgewater/BW_FogLow_01"
            }
            0x6edc2047 = MapParticle {
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    8637.26953, -56.6828003, 7405.33008, 1
                }
                name: string = "BW_FogLow_01_4"
                system: link = "Maps/Particles/HA/Bilgewater/BW_FogLow_01"
            }
            0x03d857cd = MapParticle {
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    10807.9004, -169.138, 8891.37988, 1
                }
                name: string = "BW_FogLow_01_5"
                system: link = "Maps/Particles/HA/Bilgewater/BW_FogLow_01"
            }
            0x099ffee2 = MapParticle {
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    12073.0996, -0.127747998, 9759.96973, 1
                }
                name: string = "BW_FogLow_01_6"
                system: link = "Maps/Particles/HA/Bilgewater/BW_FogLow_01"
            }
            0xdab6333e = MapParticle {
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    367.351013, 683.065979, 1183.35999, 1
                }
                name: string = "BW_Order_StartingPlatform_GodRays1"
                system: link = "Maps/Particles/HA/Bilgewater/BW_Order_StartingPlatform_GodRays"
            }
            0x839481f2 = MapParticle {
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    10966, 717.828979, 11827.7002, 1
                }
                name: string = "BW_Order_StartingPlatform_GodRays2"
                system: link = "Maps/Particles/HA/Bilgewater/BW_Order_StartingPlatform_GodRays"
            }
            0xf1d98a91 = MapParticle {
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    -376, -2635, 5263.43018, 1
                }
                name: string = "BW_Peref_Steam_Generic5"
                system: link = "Maps/Particles/HA/Bilgewater/BW_Peref_Steam_Generic"
            }
            0x05d55ec4 = MapParticle {
                transform: mtx44 = {
                    0.933580399, 0, -0.35836795, 0
                    0, 1, 0, 0
                    0.35836795, 0, 0.933580399, 0
                    844.257996, -3225.38989, 16454, 1
                }
                name: string = "BW_Peref_Fog_Distant1"
                system: link = "Maps/Particles/HA/Bilgewater/BW_Peref_Fog_Distant"
            }
            0xce2678d9 = MapParticle {
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    -254.369003, -378.470001, 6898.81982, 1
                }
                name: string = "BW_Audio-Emitter_Shootout_Cannons8"
                system: link = "Maps/Particles/HA/Bilgewater/BW_Audio_Emitter_Shootout_Cannons"
            }
            0x178ce8f5 = MapParticle {
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    12739.0996, -169.138, 7368.91992, 1
                }
                name: string = "BW_Audio-Emitter_Shootout_Guns1"
                system: link = "Maps/Particles/HA/Bilgewater/BW_Audio_Emitter_Shootout_Guns"
            }
            0x73622c54 = MapParticle {
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    13758.9004, -169.138, 3269.66992, 1
                }
                name: string = "BW_Audio-Emitter_Shootout_Guns2"
                system: link = "Maps/Particles/HA/Bilgewater/BW_Audio_Emitter_Shootout_Guns"
            }
            0xd0ddb869 = MapParticle {
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2489.02002, -532.447021, 227.278, 1
                }
                name: string = "BW_Audio-Emitter_Shootout_Guns3"
                system: link = "Maps/Particles/HA/Bilgewater/BW_Audio_Emitter_Shootout_Guns"
            }
            0xce0f9f22 = MapParticle {
                transform: mtx44 = {
                    0.071604073, -0.00314801303, -0.997428179, 0
                    -0.691274166, 0.720726311, -0.0519003756, 0
                    0.719036102, 0.693212569, 0.0494307987, 0
                    5709.58984, -812.223999, 8377.36035, 1
                }
                name: string = "BW_Audio-Emitter_Shootout_Guns4"
                system: link = "Maps/Particles/HA/Bilgewater/BW_Audio_Emitter_Shootout_Guns"
            }
            0xce71c100 = MapParticle {
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    8752.41992, -3685.84009, 5511.08008, 1
                }
                name: string = "BW_Braziers_Fire_Bigger2"
                system: link = "Maps/Particles/HA/Bilgewater/BW_Braziers_Fire_Bigger"
            }
            0xa1abab21 = MapParticle {
                transform: mtx44 = {
                    0.719339788, 0, 0.694658399, 0
                    0, 1, 0, 0
                    -0.694658399, 0, 0.719339788, 0
                    2236.27002, -182.639999, 2206.95996, 1
                }
                name: string = "BW_Order_Rain_and_Puddels1"
                system: link = "Maps/Particles/HA/Bilgewater/BW_Order_Rain_and_Puddels"
                groupName: string = "RUNETIMER_ORDER"
            }
            0xd9f2fa97 = null
            0xefcee571 = null
            0x4d3ef05a = null
            0x7dba7c66 = null
            0x16f408f8 = GdsMapObject {
                transform: mtx44 = {
                    0.704599321, 0, -0.709605396, 0
                    0, 1, 0, 0
                    0.709605396, 0, 0.704599321, 0
                    9460, -174, 9721, 1
                }
                name: string = "__NAV_C015"
                type: u8 = 8
                boxMin: vec3 = { 9408.33398, -125.289566, 9669.33398 }
                boxMax: vec3 = { 9511.66602, -19.9582062, 9772.66602 }
            }
            0xe735a986 = GdsMapObject {
                transform: mtx44 = {
                    0.704599321, 0, -0.709605396, 0
                    0, 1, 0, 0
                    0.709605396, 0, 0.704599321, 0
                    6802, -160, 6730, 1
                }
                name: string = "__NAV_C010"
                type: u8 = 8
                boxMin: vec3 = { 6750.33398, -111.289566, 6678.33398 }
                boxMax: vec3 = { 6853.66602, -5.95820618, 6781.66602 }
            }
            0x4af247f4 = GdsMapObject {
                transform: mtx44 = {
                    0.829382002, 0, 0, 0
                    0, -0.829382002, -1.01570004e-16, 0
                    0, 1.01570004e-16, -0.829382002, 0
                    3151, -265, 1418, 1
                }
                name: string = "Info_OrderRandomThingy02"
                type: u8 = 9
                boxMin: vec3 = { 3112.98193, -347.068085, 1379.98206 }
                boxMax: vec3 = { 3189.01807, -265, 1456.01794 }
            }
            0x67e24b30 = GdsMapObject {
                transform: mtx44 = {
                    0.704599321, 0, -0.709605396, 0
                    0, 1, 0, 0
                    0.709605396, 0, 0.704599321, 0
                    8133, -174, 8372, 1
                }
                name: string = "__NAV_C013"
                type: u8 = 8
                boxMin: vec3 = { 8081.33398, -125.289566, 8320.33398 }
                boxMax: vec3 = { 8184.66602, -19.9582062, 8423.66602 }
            }
            0x633b5042 = GdsMapObject {
                transform: mtx44 = {
                    0.829382002, 0, 0, 0
                    0, -0.829382002, -1.01570004e-16, 0
                    0, 1.01570004e-16, -0.829382002, 0
                    4790, -188, 3934, 1
                }
                name: string = "Info_HealthPack03"
                type: u8 = 9
                boxMin: vec3 = { 4751.98193, -270.068085, 3895.98193 }
                boxMax: vec3 = { 4828.01807, -188, 3972.01807 }
            }
            0x1bc76a40 = GdsMapObject {
                transform: mtx44 = {
                    0.704599321, 0, -0.709605396, 0
                    0, 1, 0, 0
                    0.709605396, 0, 0.704599321, 0
                    1866, -172, 1982, 1
                }
                name: string = "HQ_T1"
                type: u8 = 4
                boxMin: vec3 = { 1561.91028, -260.008514, 1656.03674 }
                boxMax: vec3 = { 2198.78076, -84.4602814, 2297.70605 }
            }
            0xc3805315 = GdsMapObject {
                transform: mtx44 = {
                    0.704599321, 0, -0.709605396, 0
                    0, 1, 0, 0
                    0.709605396, 0, 0.704599321, 0
                    9690, -166, 9520, 1
                }
                name: string = "Barracks_T2_C1"
                type: u8 = 3
                boxMin: vec3 = { 9487.96289, -201.591461, 9316.68555 }
                boxMax: vec3 = { 9892.01562, -130.776611, 9732.18945 }
            }
            0x23f027ad = GdsMapObject {
                transform: mtx44 = {
                    0.829382002, 0, 0, 0
                    0, -0.829382002, -1.01570004e-16, 0
                    0, 1.01570004e-16, -0.829382002, 0
                    5929, -193, 5190, 1
                }
                name: string = "Info_HealthPack01"
                type: u8 = 9
                boxMin: vec3 = { 5890.98193, -275.068085, 5151.98193 }
                boxMax: vec3 = { 5967.01807, -193, 5228.01807 }
            }
            0x8ca9d529 = GdsMapObject {
                transform: mtx44 = {
                    0.704599321, 0, -0.709605396, 0
                    0, 1, 0, 0
                    0.709605396, 0, 0.704599321, 0
                    7202, -160, 7295, 1
                }
                name: string = "__NAV_C011"
                type: u8 = 8
                boxMin: vec3 = { 7150.33398, -111.289566, 7243.33398 }
                boxMax: vec3 = { 7253.66602, -5.95820618, 7346.66602 }
            }
            0xc16405e6 = GdsMapObject {
                transform: mtx44 = {
                    0.704599321, 0, -0.709605396, 0
                    0, 1, 0, 0
                    0.709605396, 0, 0.704599321, 0
                    10644, -182, 10499, 1
                }
                name: string = "____P_Chaos_Spawn_Barracks__C01"
                boxMin: vec3 = { 10505.4414, -182.639496, 10360.4414 }
                boxMax: vec3 = { 10782.5586, -18.3764648, 10637.5586 }
            }
            0x02d4ebb1 = GdsMapObject {
                transform: mtx44 = {
                    0.704599321, 0, -0.709605396, 0
                    0, 1, 0, 0
                    0.709605396, 0, 0.704599321, 0
                    4764, -154, 5066, 1
                }
                name: string = "__NAV_C06"
                type: u8 = 8
                boxMin: vec3 = { 4712.33398, -105.289566, 5014.33398 }
                boxMax: vec3 = { 4815.66602, 0.0417938232, 5117.66602 }
            }
            0x863a76c5 = GdsMapObject {
                transform: mtx44 = {
                    0.704599321, 0, -0.709605396, 0
                    0, 1, 0, 0
                    0.709605396, 0, 0.704599321, 0
                    10187, -174, 10271, 1
                }
                name: string = "__NAV_C016"
                type: u8 = 8
                boxMin: vec3 = { 10135.334, -125.289566, 10219.334 }
                boxMax: vec3 = { 10238.666, -19.9582062, 10322.666 }
            }
            0x1283d5ee = GdsMapObject {
                transform: mtx44 = {
                    0.829382002, 0, 0, 0
                    0, -0.829382002, -1.01570004e-16, 0
                    0, 1.01570004e-16, -0.829382002, 0
                    11311, -265, 11029, 1
                }
                name: string = "Info_ChaosRandomThingy01"
                type: u8 = 9
                boxMin: vec3 = { 11272.9824, -347.068085, 10990.9824 }
                boxMax: vec3 = { 11349.0176, -265, 11067.0176 }
            }
            0x55ca5026 = GdsMapObject {
                transform: mtx44 = {
                    0.704599321, 0, -0.709605396, 0
                    0, 1, 0, 0
                    0.709605396, 0, 0.704599321, 0
                    5309, -160, 5482, 1
                }
                name: string = "__NAV_C07"
                type: u8 = 8
                boxMin: vec3 = { 5257.33398, -111.289566, 5430.33398 }
                boxMax: vec3 = { 5360.66602, -5.95820618, 5533.66602 }
            }
            0x0fe345fc = GdsMapObject {
                transform: mtx44 = {
                    0.704599321, 0, -0.709605396, 0
                    0, 1, 0, 0
                    0.709605396, 0, 0.704599321, 0
                    2213, -162, 2685, 1
                }
                name: string = "__NAV_C02"
                type: u8 = 8
                boxMin: vec3 = { 2161.33398, -113.289566, 2633.33398 }
                boxMax: vec3 = { 2264.66602, -7.95820618, 2736.66602 }
            }
            0x21c4e30f = GdsMapObject {
                transform: mtx44 = {
                    0.704599321, 0, -0.709605396, 0
                    0, 1, 0, 0
                    0.709605396, 0, 0.704599321, 0
                    7595, -174, 7858, 1
                }
                name: string = "__NAV_C012"
                type: u8 = 8
                boxMin: vec3 = { 7543.33398, -125.289566, 7806.33398 }
                boxMax: vec3 = { 7646.66602, -19.9582062, 7909.66602 }
            }
            0x30d96a45 = GdsMapObject {
                transform: mtx44 = {
                    0.704599321, 0, -0.709605396, 0
                    0, 1, 0, 0
                    0.709605396, 0, 0.704599321, 0
                    6434, -160, 6214, 1
                }
                name: string = "__NAV_C09"
                type: u8 = 8
                boxMin: vec3 = { 6382.33398, -111.289566, 6162.33398 }
                boxMax: vec3 = { 6485.66602, -5.95820618, 6265.66602 }
            }
            0x3f4540bc = GdsMapObject {
                transform: mtx44 = {
                    0.704599321, 0, -0.709605396, 0
                    0, 1, 0, 0
                    0.709605396, 0, 0.704599321, 0
                    8743, -174, 8985, 1
                }
                name: string = "__NAV_C014"
                type: u8 = 8
                boxMin: vec3 = { 8691.33398, -125.289566, 8933.33398 }
                boxMax: vec3 = { 8794.66602, -19.9582062, 9036.66602 }
            }
            0x4cdaaa27 = GdsMapObject {
                transform: mtx44 = {
                    0.99984771, 0, -0.0174524058, 0
                    0, 1, 0, 0
                    0.0174524058, 0, 0.99984771, 0
                    3119, -167, 3176, 1
                }
                name: string = "Barracks_T1_C1"
                type: u8 = 3
                boxMin: vec3 = { 2930.36182, -217.72168, 2997.23242 }
                boxMax: vec3 = { 3308.16016, -117.44883, 3355.92139 }
            }
            0x86e7393f = GdsMapObject {
                transform: mtx44 = {
                    0.829382002, 0, 0, 0
                    0, -0.829382002, -1.01570004e-16, 0
                    0, 1.01570004e-16, -0.829382002, 0
                    7582, -193, 6785, 1
                }
                name: string = "Info_HealthPack04"
                type: u8 = 9
                boxMin: vec3 = { 7543.98193, -275.068085, 6746.98193 }
                boxMax: vec3 = { 7620.01807, -193, 6823.01807 }
            }
            0xb6e96be5 = GdsMapObject {
                transform: mtx44 = {
                    0.704599321, 0, -0.709605396, 0
                    0, 1, 0, 0
                    0.709605396, 0, 0.704599321, 0
                    3663, -154, 4127, 1
                }
                name: string = "__NAV_C04"
                type: u8 = 8
                boxMin: vec3 = { 3611.33398, -105.289566, 4075.33398 }
                boxMax: vec3 = { 3714.66602, 0.0417938232, 4178.66602 }
            }
            0x5983e221 = GdsMapObject {
                transform: mtx44 = {
                    0.785826504, 0, -0.618447006, 0
                    0, 1, 0, 0
                    0.618447006, 0, 0.785826504, 0
                    10935, -174, 10725, 1
                }
                name: string = "HQ_T2"
                type: u8 = 4
                boxMin: vec3 = { 10628.4668, -252.00676, 10404.5781 }
                boxMax: vec3 = { 11269.7168, -97.7425079, 11038.9727 }
            }
            0x799e2b9d = GdsMapObject {
                transform: mtx44 = {
                    0.704599321, 0, -0.709605396, 0
                    0, 1, 0, 0
                    0.709605396, 0, 0.704599321, 0
                    936, -106, 1060, 1
                }
                name: string = "__Spawn_T1"
                type: u8 = 1
                boxMin: vec3 = { 869.608398, -106, 993.608398 }
                boxMax: vec3 = { 1002.3916, 177.725891, 1126.3916 }
            }
            0xe0ed2af8 = GdsMapObject {
                transform: mtx44 = {
                    0.704599321, 0, -0.709605396, 0
                    0, 1, 0, 0
                    0.709605396, 0, 0.704599321, 0
                    11860, -114, 11596, 1
                }
                name: string = "__Spawn_T2"
                type: u8 = 1
                boxMin: vec3 = { 11793.6084, -114, 11529.6084 }
                boxMax: vec3 = { 11926.3916, 169.725891, 11662.3916 }
            }
            0x33802c27 = GdsMapObject {
                transform: mtx44 = {
                    0.704599321, 0, -0.709605396, 0
                    0, 1, 0, 0
                    0.709605396, 0, 0.704599321, 0
                    4193, -152, 4555, 1
                }
                name: string = "__NAV_C05"
                type: u8 = 8
                boxMin: vec3 = { 4141.33398, -103.289566, 4503.33398 }
                boxMax: vec3 = { 4244.66602, 2.04179382, 4606.66602 }
            }
            0xddf6a37a = GdsMapObject {
                transform: mtx44 = {
                    0.829382002, 0, 0, 0
                    0, -0.829382002, -1.01570004e-16, 0
                    0, 1.01570004e-16, -0.829382002, 0
                    8893, -187, 7889, 1
                }
                name: string = "Info_HealthPack02"
                type: u8 = 9
                boxMin: vec3 = { 8854.98242, -269.068085, 7850.98193 }
                boxMax: vec3 = { 8931.01758, -187, 7927.01807 }
            }
            0x54dfd5c9 = GdsMapObject {
                transform: mtx44 = {
                    0.704599321, 0, -0.709605396, 0
                    0, 1, 0, 0
                    0.709605396, 0, 0.704599321, 0
                    2903, -155, 3411, 1
                }
                name: string = "__NAV_C03"
                type: u8 = 8
                boxMin: vec3 = { 2851.33398, -106.289566, 3359.33398 }
                boxMax: vec3 = { 2954.66602, -0.958206177, 3462.66602 }
            }
            0xdeb7e64d = GdsMapObject {
                transform: mtx44 = {
                    0.829382002, 0, 0, 0
                    0, -0.829382002, -1.01570004e-16, 0
                    0, 1.01570004e-16, -0.829382002, 0
                    1501, -265, 1620, 1
                }
                name: string = "Info_OrderRandomThingy01"
                type: u8 = 9
                boxMin: vec3 = { 1462.98206, -347.068085, 1581.98206 }
                boxMax: vec3 = { 1539.01794, -265, 1658.01794 }
            }
            0x23e606e9 = GdsMapObject {
                transform: mtx44 = {
                    0.704597056, 0, -0.709607601, 0
                    0, 1, 0, 0
                    0.709607601, 0, 0.704597056, 0
                    2179.17212, -182.000122, 2289.84424, 1
                }
                name: string = "____P_Order_Spawn_Barracks__C01"
                boxMin: vec3 = { 2040.61365, -182.639618, 2151.28564 }
                boxMax: vec3 = { 2317.73047, -18.3765869, 2428.40283 }
            }
            0x5d193a76 = GdsMapObject {
                transform: mtx44 = {
                    0.704599321, 0, -0.709605396, 0
                    0, 1, 0, 0
                    0.709605396, 0, 0.704599321, 0
                    5906, -160, 5869, 1
                }
                name: string = "__NAV_C08"
                type: u8 = 8
                boxMin: vec3 = { 5854.33398, -111.289566, 5817.33398 }
                boxMax: vec3 = { 5957.66602, -5.95820618, 5920.66602 }
            }
            0x29e9c9b9 = GdsMapObject {
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    11065, -184, 12306, 1
                }
                name: string = "ChaosShop01"
                type: u8 = 6
                boxMin: vec3 = { 10488.1729, -187.462204, 11733.2324 }
                boxMax: vec3 = { 11633.8604, 0, 12879.7344 }
            }
            0x7e3f4540 = GdsMapObject {
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    6528, 355, 7928, 1
                }
                name: string = "LevelProp_bw_anclantern1"
                type: u8 = 10
                boxMin: vec3 = { 6460.10645, 252.767303, 7860.77441 }
                boxMax: vec3 = { 6596.16699, 457.259613, 7996.83594 }
            }
            0x1aafe182 = GdsMapObject {
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    9335, 355, 7820, 1
                }
                name: string = "LevelProp_bw_anclantern2"
                type: u8 = 10
                boxMin: vec3 = { 9267.02148, 252.767303, 7752.68359 }
                boxMax: vec3 = { 9403.08301, 457.259613, 7888.74463 }
            }
            0xe895f18a = GdsMapObject {
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    7932, 355, 6465, 1
                }
                name: string = "LevelProp_bw_anclantern3"
                type: u8 = 10
                boxMin: vec3 = { 7864.02832, 252.767303, 6397.82764 }
                boxMax: vec3 = { 8000.08887, 457.259613, 6533.88867 }
            }
            0x3122d0ff = GdsMapObject {
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    6189, 355, 4783, 1
                }
                name: string = "LevelProp_bw_anclantern4"
                type: u8 = 10
                boxMin: vec3 = { 6121.90039, 252.767303, 4715.4751 }
                boxMax: vec3 = { 6257.96191, 457.259613, 4851.53613 }
            }
            0x138c7b1e = GdsMapObject {
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    4794, 355, 3435, 1
                }
                name: string = "LevelProp_bw_anclantern5"
                type: u8 = 10
                boxMin: vec3 = { 4726.49463, 252.767303, 3367.94727 }
                boxMax: vec3 = { 4862.55566, 457.259613, 3504.0083 }
            }
            0x996fe0c1 = GdsMapObject {
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    7926, 355, 9279, 1
                }
                name: string = "LevelProp_bw_anclantern6"
                type: u8 = 10
                boxMin: vec3 = { 7858.76953, 252.767303, 9210.9707 }
                boxMax: vec3 = { 7994.83057, 457.259613, 9347.03223 }
            }
            0x157ba830 = GdsMapObject {
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    4766, 355, 6227, 1
                }
                name: string = "LevelProp_bw_anclantern8"
                type: u8 = 10
                boxMin: vec3 = { 4698.71777, 252.767303, 6159.34473 }
                boxMax: vec3 = { 4834.7793, 457.259613, 6295.40576 }
            }
            0xb3725714 = GdsMapObject {
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    3386, 355, 4894, 1
                }
                name: string = "LevelProp_bw_anclantern9"
                type: u8 = 10
                boxMin: vec3 = { 3318.24219, 252.767303, 4826.23486 }
                boxMax: vec3 = { 3454.30322, 457.259613, 4962.2959 }
            }
            0x5362af97 = GdsMapObject {
                transform: mtx44 = {
                    -0.74314481, 0, -0.669130623, 0
                    0, 1, 0, 0
                    0.669130623, 0, -0.74314481, 0
                    605, -264, 1766, 1
                }
                name: string = "LevelProp_BW_AP_Bubbs"
                type: u8 = 10
                boxMin: vec3 = { 487.368591, -454.723602, 1848.46021 }
                boxMax: vec3 = { 523.039429, 0, 1884.13147 }
            }
            0x7b55dfa2 = GdsMapObject {
                transform: mtx44 = {
                    -0.898794055, 0, -0.438371152, 0
                    0, 1, 0, 0
                    0.438371152, 0, -0.898794055, 0
                    11129, -152, 11829, 1
                }
                name: string = "LevelProp_BW_AP_Finn"
                type: u8 = 10
                boxMin: vec3 = { 11103.5723, -227.564896, 11980.9316 }
                boxMax: vec3 = { 11156.1406, 0, 12033.502 }
            }
            0x8fb93b12 = GdsMapObject {
                transform: mtx44 = {
                    -0.615661502, 0, -0.788010776, 0
                    0, 1, 0, 0
                    0.788010776, 0, -0.615661502, 0
                    798, -6209, 7939, 1
                }
                name: string = "LevelProp_BW_boat1"
                type: u8 = 10
                boxMin: vec3 = { 682.156921, -6260.46143, 7761.98438 }
                boxMax: vec3 = { 914.367676, 0, 8116.63965 }
            }
            0x0fdfd00c = GdsMapObject {
                transform: mtx44 = {
                    -0.91354543, 0, -0.406736642, 0
                    0, 1, 0, 0
                    0.406736642, 0, -0.91354543, 0
                    51, -6209, 7910, 1
                }
                name: string = "LevelProp_BW_boat2"
                type: u8 = 10
                boxMin: vec3 = { -113.165703, -6260.46143, 7741.20215 }
                boxMax: vec3 = { 216.345001, 0, 8078.82324 }
            }
            0x4a9b5082 = GdsMapObject {
                transform: mtx44 = {
                    0.104528464, 0, -0.994521916, 0
                    0, 1, 0, 0
                    0.994521916, 0, 0.104528464, 0
                    455, -6242, 12493, 1
                }
                name: string = "LevelProp_BW_boat3"
                type: u8 = 10
                boxMin: vec3 = { 363.555206, -6260.46143, 12322.5322 }
                boxMax: vec3 = { 546.513428, 0, 12664.334 }
            }
            0x3d19224a = GdsMapObject {
                transform: mtx44 = {
                    -0.866025388, 0, -0.5, 0
                    0, 1, 0, 0
                    0.5, 0, -0.866025388, 0
                    10809, -6209, 3325, 1
                }
                name: string = "LevelProp_BW_boat4"
                type: u8 = 10
                boxMin: vec3 = { 10620.3955, -6257.24854, 2975.74341 }
                boxMax: vec3 = { 10997.625, 0, 3675.03784 }
            }
            0x97a2223c = GdsMapObject {
                transform: mtx44 = {
                    0.0697564706, 0, -0.997564077, 0
                    0, 1, 0, 0
                    0.997564077, 0, 0.0697564706, 0
                    7179, -6145, 2294, 1
                }
                name: string = "LevelProp_BW_boat5"
                type: u8 = 10
                boxMin: vec3 = { 7180.29395, -6147.91895, 1945.3363 }
                boxMax: vec3 = { 7557.52344, 0, 2644.63086 }
            }
            0x82cc560d = GdsMapObject {
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1790, -6176, 6016, 1
                }
                name: string = "LevelProp_BW_boat6"
                type: u8 = 10
                boxMin: vec3 = { 1674.20923, -6260.46143, 5839.40918 }
                boxMax: vec3 = { 1906.42017, 0, 6194.06445 }
            }
            0x0fcaa3e0 = GdsMapObject {
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    919.749084, -181.269287, 2485.06323, 1
                }
                name: string = "LevelProp_bw_bottle"
                type: u8 = 10
                boxMin: vec3 = { 895.148682, -181.257019, 2460.46289 }
                boxMax: vec3 = { 944.349487, -91.6140518, 2509.66357 }
            }
            0xc117dd7f = GdsMapObject {
                transform: mtx44 = {
                    -0.529919267, 0, 0.848048091, 0
                    0, 1, 0, 0
                    -0.848048091, 0, -0.529919267, 0
                    2039, -175, 549, 1
                }
                name: string = "LevelProp_bw_bottle1"
                type: u8 = 10
                boxMin: vec3 = { 2022.71875, -208.059601, 533.562927 }
                boxMax: vec3 = { 2055.2832, 0, 566.12738 }
            }
            0x560e5b95 = GdsMapObject {
                transform: mtx44 = {
                    -0.469471574, 0, 0.882947564, 0
                    0, 1, 0, 0
                    -0.882947564, 0, -0.469471574, 0
                    3380, -175, 1794, 1
                }
                name: string = "LevelProp_bw_bottle2"
                type: u8 = 10
                boxMin: vec3 = { 3360.33325, -208.059601, 1774.17773 }
                boxMax: vec3 = { 3401.18481, 0, 1815.02954 }
            }
            0x44f91bab = GdsMapObject {
                transform: mtx44 = {
                    -0.559192896, 0, -0.829037547, 0
                    0, 1, 0, 0
                    0.829037547, 0, -0.559192896, 0
                    12277, -175, 11032, 1
                }
                name: string = "LevelProp_bw_bottle3"
                type: u8 = 10
                boxMin: vec3 = { 12260.6016, -208.059601, 11016.2959 }
                boxMax: vec3 = { 12293.5596, 0, 11049.2539 }
            }
            0x07e77683 = GdsMapObject {
                transform: mtx44 = {
                    0.207911685, 0, -0.978147626, 0
                    0, 1, 0, 0
                    0.978147626, 0, 0.207911685, 0
                    11662, -157.515503, 11848, 1
                }
                name: string = "LevelProp_bw_bottle4"
                type: u8 = 10
                boxMin: vec3 = { 11632.8223, -157.503235, 11818.8223 }
                boxMax: vec3 = { 11691.1777, -67.8602676, 11877.1777 }
            }
            0xb95d4172 = GdsMapObject {
                transform: mtx44 = {
                    -0.95105654, 0, 0.309017003, 0
                    0, 1, 0, 0
                    -0.309017003, 0, -0.95105654, 0
                    12125, -175, 10160, 1
                }
                name: string = "LevelProp_bw_bottle5"
                type: u8 = 10
                boxMin: vec3 = { 12273.0234, -208.059601, 10141.5557 }
                boxMax: vec3 = { 12311.5, 0, 10180.0312 }
            }
            0xb44ad6de = GdsMapObject {
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    730, -128.874786, 1049, 1
                }
                name: string = "LevelProp_bw_bottle6"
                type: u8 = 10
                boxMin: vec3 = { 705.399597, -128.862518, 1024.39954 }
                boxMax: vec3 = { 754.600403, -39.2195511, 1073.60046 }
            }
            0x008522a7 = GdsMapObject {
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    999, -130.467957, 646.503662, 1
                }
                name: string = "LevelProp_bw_bottle7"
                type: u8 = 10
                boxMin: vec3 = { 974.399597, -130.455688, 621.903259 }
                boxMax: vec3 = { 1023.6004, -40.8127213, 671.104065 }
            }
            0x3388eeda = GdsMapObject {
                transform: mtx44 = {
                    0.719339788, 0, 0.694658399, 0
                    0, 1, 0, 0
                    -0.694658399, 0, 0.719339788, 0
                    7592, -6416, 5071, 1
                }
                name: string = "LevelProp_BW_brdgdoor1"
                type: u8 = 10
                boxMin: vec3 = { 6859.95605, -8551.83398, 4498.71973 }
                boxMax: vec3 = { 8170.45947, 0, 5778.28369 }
            }
            0x7bd09c93 = GdsMapObject {
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    4060, -181, 1668, 1
                }
                name: string = "LevelProp_BW_dblrope1"
                type: u8 = 10
                boxMin: vec3 = { 3859.22656, -331.599396, 1417.39258 }
                boxMax: vec3 = { 4308.50977, 0, 1854.27612 }
            }
            0x114bc4ec = GdsMapObject {
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    11147, -187, 8465, 1
                }
                name: string = "LevelProp_BW_dblrope2"
                type: u8 = 10
                boxMin: vec3 = { 10922.7881, -337.586487, 8246.75586 }
                boxMax: vec3 = { 11372.0723, 0, 8683.63965 }
            }
            0x0b034e00 = GdsMapObject {
                transform: mtx44 = {
                    0.939692616, 0, -0.342020154, 0
                    0, 1, 0, 0
                    0.342020154, 0, 0.939692616, 0
                    5820, -676, 3956, 1
                }
                name: string = "LevelProp_BW_dblrope3"
                type: u8 = 10
                boxMin: vec3 = { 5542.29785, -804.370483, 3840.36523 }
                boxMax: vec3 = { 6098.55908, 0, 4073.33057 }
            }
            0xbe240723 = GdsMapObject {
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    8933, -616, 6846, 1
                }
                name: string = "LevelProp_BW_dblrope4"
                type: u8 = 10
                boxMin: vec3 = { 8764.01367, -766.83197, 6587.38525 }
                boxMax: vec3 = { 9102.57324, 0, 7106.146 }
            }
            0x91dabe38 = GdsMapObject {
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1629, -160, 4171, 1
                }
                name: string = "LevelProp_BW_dblrope5"
                type: u8 = 10
                boxMin: vec3 = { 1404.82397, -310.542694, 3953.3855 }
                boxMax: vec3 = { 1854.10718, 0, 4390.26953 }
            }
            0x023ba647 = GdsMapObject {
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    7203, -1189, 10106, 1
                }
                name: string = "LevelProp_BW_fishhk2"
                type: u8 = 10
                boxMin: vec3 = { 7044.36621, -1572.09131, 9947.83301 }
                boxMax: vec3 = { 7361.69531, 0, 10265.0908 }
            }
            0xda67dc89 = GdsMapObject {
                transform: mtx44 = {
                    0.52361089, 0, 0.85195756, 0
                    0, 1, 0, 0
                    -0.85195756, 0, 0.52361089, 0
                    958.995605, 317.76828, 32, 1
                }
                name: string = "LevelProp_bw_hcannon"
                type: u8 = 10
                boxMin: vec3 = { 886.357422, 317.76828, -40.6381683 }
                boxMax: vec3 = { 1031.63379, 870.564819, 104.638168 }
            }
            0xd46dce86 = GdsMapObject {
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2823, 482, 4523, 1
                }
                name: string = "LevelProp_BW_Lantern1"
                type: u8 = 10
                boxMin: vec3 = { 2779.51147, 332.318512, 4479.30957 }
                boxMax: vec3 = { 2867.40918, 632.42627, 4567.20752 }
            }
            0x21c9355d = GdsMapObject {
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    3930, 482, 5448, 1
                }
                name: string = "LevelProp_BW_Lantern2"
                type: u8 = 10
                boxMin: vec3 = { 3886.39697, 332.586395, 5404.86426 }
                boxMax: vec3 = { 3974.29443, 632.694214, 5492.76172 }
            }
            0x2048ba71 = GdsMapObject {
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    3064, 482, 4755, 1
                }
                name: string = "LevelProp_BW_Lantern3"
                type: u8 = 10
                boxMin: vec3 = { 3020.41528, 332.318512, 4711.94775 }
                boxMax: vec3 = { 3108.31299, 632.42627, 4799.84521 }
            }
            0xba7733d7 = GdsMapObject {
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    4177, 482, 5687, 1
                }
                name: string = "LevelProp_BW_Lantern4"
                type: u8 = 10
                boxMin: vec3 = { 4133.4873, 332.586395, 5643.47607 }
                boxMax: vec3 = { 4221.38428, 632.694214, 5731.37402 }
            }
            0x63e214b2 = GdsMapObject {
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    7345, 482, 8746, 1
                }
                name: string = "LevelProp_BW_Lantern5"
                type: u8 = 10
                boxMin: vec3 = { 7301.4751, 332.586395, 8702.76758 }
                boxMax: vec3 = { 7389.37256, 632.694214, 8790.66504 }
            }
            0x69139466 = GdsMapObject {
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    7098, 482, 8508, 1
                }
                name: string = "LevelProp_BW_Lantern6"
                type: u8 = 10
                boxMin: vec3 = { 7054.38525, 332.586395, 8464.1543 }
                boxMax: vec3 = { 7142.28271, 632.694214, 8552.05273 }
            }
            0x241a1c60 = GdsMapObject {
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    8374, 482, 9740, 1
                }
                name: string = "LevelProp_BW_Lantern7"
                type: u8 = 10
                boxMin: vec3 = { 8330.31934, 332.318512, 9696.27051 }
                boxMax: vec3 = { 8418.2168, 632.42627, 9784.16797 }
            }
            0xe0daa020 = GdsMapObject {
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    8127, 482, 9501, 1
                }
                name: string = "LevelProp_BW_Lantern8"
                type: u8 = 10
                boxMin: vec3 = { 8083.625, 332.318512, 9458.04004 }
                boxMax: vec3 = { 8171.52246, 632.42627, 9545.9375 }
            }
            0xe6a82005 = GdsMapObject {
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    0, -118, 0, 1
                }
                name: string = "LevelProp_bw_seagull1"
                type: u8 = 10
                boxMin: vec3 = { -51.7145004, -152.561401, -51.7145004 }
                boxMax: vec3 = { 51.7145004, 0, 51.7145004 }
            }
            0x1fd8ede8 = GdsMapObject {
                transform: mtx44 = {
                    0.713250458, 0, 0.700909257, 0
                    0, 1, 0, 0
                    -0.700909257, 0, 0.713250458, 0
                    0, 204, 0, 1
                }
                name: string = "LevelProp_bw_shadowshark1"
                type: u8 = 10
                boxMin: vec3 = { -51.7145004, -360.362701, -51.7145004 }
                boxMax: vec3 = { 51.7145004, 122.417297, 51.7145004 }
            }
            0x942c5bb1 = GdsMapObject {
                transform: mtx44 = {
                    0.713250458, 0, 0.700909257, 0
                    0, 1, 0, 0
                    -0.700909257, 0, 0.713250458, 0
                    0, 204, 0, 1
                }
                name: string = "LevelProp_bw_shadowshark2"
                type: u8 = 10
                boxMin: vec3 = { -51.7145004, -360.362701, -51.7145004 }
                boxMax: vec3 = { 51.7145004, 122.417297, 51.7145004 }
            }
            0xfd242fef = GdsMapObject {
                transform: mtx44 = {
                    0.713250458, 0, 0.700909257, 0
                    0, 1, 0, 0
                    -0.700909257, 0, 0.713250458, 0
                    0, 204, 0, 1
                }
                name: string = "LevelProp_bw_shadowshark3"
                type: u8 = 10
                boxMin: vec3 = { -51.7145004, -360.362701, -51.7145004 }
                boxMax: vec3 = { 51.7145004, 122.417297, 51.7145004 }
            }
            0x6e3ca8b1 = GdsMapObject {
                transform: mtx44 = {
                    0.713250458, 0, 0.700909257, 0
                    0, 1, 0, 0
                    -0.700909257, 0, 0.713250458, 0
                    0, 204, 0, 1
                }
                name: string = "LevelProp_bw_shadowshark4"
                type: u8 = 10
                boxMin: vec3 = { -51.7145004, -360.362701, -51.7145004 }
                boxMax: vec3 = { 51.7145004, 122.417297, 51.7145004 }
            }
            0x718dc2b7 = GdsMapObject {
                transform: mtx44 = {
                    0.713250458, 0, 0.700909257, 0
                    0, 1, 0, 0
                    -0.700909257, 0, 0.713250458, 0
                    0, 204, 0, 1
                }
                name: string = "LevelProp_bw_shadowshark5"
                type: u8 = 10
                boxMin: vec3 = { -51.7145004, -360.362701, -51.7145004 }
                boxMax: vec3 = { 51.7145004, 122.417297, 51.7145004 }
            }
            0x0ec8927b = GdsMapObject {
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2606, -120, 283, 1
                }
                name: string = "LevelProp_BW_shortrope1"
                type: u8 = 10
                boxMin: vec3 = { 2381.81299, -270.853912, 64.9990997 }
                boxMax: vec3 = { 2831.09619, 29.2539005, 501.882812 }
            }
            0x34f00da0 = GdsMapObject {
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    3087, -120, 744, 1
                }
                name: string = "LevelProp_BW_shortrope2"
                type: u8 = 10
                boxMin: vec3 = { 2862.96094, -270.853912, 525.966125 }
                boxMax: vec3 = { 3312.24414, 29.2539005, 962.849792 }
            }
            0xdadb048c = GdsMapObject {
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    3575, -120, 1190, 1
                }
                name: string = "LevelProp_BW_shortrope3"
                type: u8 = 10
                boxMin: vec3 = { 3351.30737, -270.853912, 972.31897 }
                boxMax: vec3 = { 3800.59058, 29.2539005, 1409.20251 }
            }
            0x319d94e0 = GdsMapObject {
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    11609, -126, 8957, 1
                }
                name: string = "LevelProp_BW_shortrope4"
                type: u8 = 10
                boxMin: vec3 = { 11385.3184, -276.841003, 8738.83398 }
                boxMax: vec3 = { 11834.6006, 23.2668991, 9175.7168 }
            }
            0xb24c1d65 = GdsMapObject {
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1149, -123, 3707, 1
                }
                name: string = "LevelProp_BW_shortrope5"
                type: u8 = 10
                boxMin: vec3 = { 936.658691, -251.511597, 3488.61914 }
                boxMax: vec3 = { 1385.94189, 48.5964012, 3925.50317 }
            }
            0x4073850b = GdsMapObject {
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    673, -100, 3236, 1
                }
                name: string = "LevelProp_BW_shortrope6"
                type: u8 = 10
                boxMin: vec3 = { 416.718811, -250.146103, 2987.18701 }
                boxMax: vec3 = { 930.914429, 49.9617996, 3486.75537 }
            }
            0x3417b57f = GdsMapObject {
                transform: mtx44 = {
                    -0.241921902, 0, -0.970295727, 0
                    0, 1, 0, 0
                    0.970295727, 0, -0.241921902, 0
                    9015, -457, 11888, 1
                }
                name: string = "LevelProp_BW_shrkhk1"
                type: u8 = 10
                boxMin: vec3 = { 8407.19141, -1206.56201, 11546.2412 }
                boxMax: vec3 = { 9092.12012, 445.854614, 12231.0176 }
            }
            0x8ecad32d = GdsMapObject {
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    12589, 672, 8743, 1
                }
                name: string = "LevelProp_BW_signa1"
                type: u8 = 10
                boxMin: vec3 = { 12400.9229, 487.71759, 8560.29395 }
                boxMax: vec3 = { 12777.4795, 856.795105, 8926.74219 }
            }
            0x69851128 = GdsMapObject {
                transform: mtx44 = {
                    0.866025388, 0, 0.5, 0
                    0, 1, 0, 0
                    -0.5, 0, 0.866025388, 0
                    577, -12, 3477, 1
                }
                name: string = "LevelProp_BW_squid1"
                type: u8 = 10
                boxMin: vec3 = { -131.232803, -1806.79858, 3413.34521 }
                boxMax: vec3 = { 553.696472, 734.992981, 4098.12109 }
            }
            0xd9549051 = GdsMapObject {
                transform: mtx44 = {
                    0.719339788, 0, 0.694658399, 0
                    0, 1, 0, 0
                    -0.694658399, 0, 0.719339788, 0
                    7534, -1331, 5149, 1
                }
                name: string = "LevelProp_BW_statlant1"
                type: u8 = 10
                boxMin: vec3 = { 6604.86182, -1665.97656, 4232.24658 }
                boxMax: vec3 = { 8464.5752, 0, 6067.64893 }
            }
            0x7b258ed2 = GdsMapObject {
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    226, 327, 1411, 1
                }
                name: string = "LevelProp_bw_tooth1"
                type: u8 = 10
                boxMin: vec3 = { 158.464905, 225.004807, 1343.05591 }
                boxMax: vec3 = { 294.525909, 429.497192, 1479.11694 }
            }
            0xca794c4b = GdsMapObject {
                transform: mtx44 = {
                    0.956318736, 0, 0.292325884, 0
                    0, 1, 0, 0
                    -0.292325884, 0, 0.956318736, 0
                    420.821899, 275.846924, 3156.30103, 1
                }
                name: string = "LevelProp_bw_tooth2"
                type: u8 = 10
                boxMin: vec3 = { 333.892426, 275.846924, 3069.37158 }
                boxMax: vec3 = { 507.751373, 1660.65393, 3243.23047 }
            }
            0x32bc155d = GdsMapObject {
                transform: mtx44 = {
                    0.642787635, 0, 0.766044438, 0
                    0, 1, 0, 0
                    -0.766044438, 0, 0.642787635, 0
                    -2264.24683, -6498, 12026.6309, 1
                }
                name: string = "LevelProp_BW_vship1"
                type: u8 = 10
                boxMin: vec3 = { -704418304, -6498, -704403968 }
                boxMax: vec3 = { 704413760, 999993472, 704428032 }
            }
            0x06f511ab = GdsMapObject {
                transform: mtx44 = {
                    0.788010776, 0, -0.615661502, 0
                    0, 1, 0, 0
                    0.615661502, 0, 0.788010776, 0
                    1498.75317, -6579, 9897.63086, 1
                }
                name: string = "LevelProp_BW_vship2"
                type: u8 = 10
                boxMin: vec3 = { -701834624, -6579, -701826240 }
                boxMax: vec3 = { 701837632, 999993408, 701846016 }
            }
            0x302f56cf = GdsMapObject {
                transform: mtx44 = {
                    0.999390841, 0, 0.0348994955, 0
                    0, 1, 0, 0
                    -0.0348994955, 0, 0.999390841, 0
                    6106.75293, -6539, 5902.63086, 1
                }
                name: string = "LevelProp_BW_vship3"
                type: u8 = 10
                boxMin: vec3 = { -517139072, -6539, -517139296 }
                boxMax: vec3 = { 517151264, 999993472, 517151072 }
            }
            0xea95cb9a = GdsMapObject {
                transform: mtx44 = {
                    0.719339788, 0, 0.694658399, 0
                    0, 1, 0, 0
                    -0.694658399, 0, 0.719339788, 0
                    5422, -773, 2758, 1
                }
                name: string = "LevelProp_HABW_Banner1"
                type: u8 = 10
                boxMin: vec3 = { 5280.6709, -1389.39172, 2613.05835 }
                boxMax: vec3 = { 5565.19922, 0, 2903.68213 }
            }
            0xf7b4f71c = GdsMapObject {
                transform: mtx44 = {
                    0.719339788, 0, 0.694658399, 0
                    0, 1, 0, 0
                    -0.694658399, 0, 0.719339788, 0
                    6821, -781, 4108, 1
                }
                name: string = "LevelProp_HABW_Banner2"
                type: u8 = 10
                boxMin: vec3 = { 6678.81934, -1397.23083, 3963.23511 }
                boxMax: vec3 = { 6963.34766, 0, 4253.85889 }
            }
            0xf9ceaac3 = GdsMapObject {
                transform: mtx44 = {
                    0.719339788, 0, 0.694658399, 0
                    0, 1, 0, 0
                    -0.694658399, 0, 0.719339788, 0
                    8570, -773, 5798, 1
                }
                name: string = "LevelProp_HABW_Banner3"
                type: u8 = 10
                boxMin: vec3 = { 8428.40527, -1389.39172, 5652.79004 }
                boxMax: vec3 = { 8712.93359, 0, 5943.41406 }
            }
            0x6d9bb744 = GdsMapObject {
                transform: mtx44 = {
                    0.719339788, 0, 0.694658399, 0
                    0, 1, 0, 0
                    -0.694658399, 0, 0.719339788, 0
                    9964, -773, 7144, 1
                }
                name: string = "LevelProp_HABW_Banner4"
                type: u8 = 10
                boxMin: vec3 = { 9822.55762, -1389.39172, 6999.10791 }
                boxMax: vec3 = { 10107.0859, 0, 7289.73193 }
            }
            0x46a44755 = GdsMapObject {
                transform: mtx44 = {
                    -0.0345598571, -0.00485707121, -0.999390841, 0
                    -0.0349625535, 0.999381959, -0.00364799076, 0
                    0.99879086, 0.034815181, -0.0347083136, 0
                    959, 849, 91, 1
                }
                name: string = "LevelProp_HA_AP_Poro"
                type: u8 = 10
                boxMin: vec3 = { 904.036621, 831.123718, -53.1058998 }
                boxMax: vec3 = { 1083.67688, 958.633606, 126.534302 }
            }
            0xdc886a0f = GdsMapObject {
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    937, -167, 2938, 1
                }
                name: string = "LevelProp_HA_AP_Poro1"
                type: u8 = 10
                boxMin: vec3 = { 892.8172, -198.101593, 2915.66772 }
                boxMax: vec3 = { 938.39032, 0, 2961.24097 }
            }
            0x06e5ec83 = GdsMapObject {
                transform: mtx44 = {
                    0.98480773, 0, -0.173648179, 0
                    0, 1, 0, 0
                    0.173648179, 0, 0.98480773, 0
                    2170, 38, 4293, 1
                }
                name: string = "LevelProp_HA_AP_Poro2"
                type: u8 = 10
                boxMin: vec3 = { 2239.16846, 19.8418999, 4273.91406 }
                boxMax: vec3 = { 2279.03271, 57.6361008, 4313.77832 }
            }
            0xa5ee1847 = GdsMapObject {
                transform: mtx44 = {
                    -0.970295727, 0, -0.241921902, 0
                    0, 1, 0, 0
                    0.241921902, 0, -0.970295727, 0
                    8718, 45, 10777, 1
                }
                name: string = "LevelProp_HA_AP_Poro3"
                type: u8 = 10
                boxMin: vec3 = { 8638.42383, 26.8957996, 10718.7539 }
                boxMax: vec3 = { 8689.42578, 64.6900024, 10769.7559 }
            }
            0xc97f3db1 = GdsMapObject {
                transform: mtx44 = {
                    -0.809017003, 0, -0.587785244, 0
                    0, 1, 0, 0
                    0.587785244, 0, -0.809017003, 0
                    11241, -840, 8584, 1
                }
                name: string = "LevelProp_HA_AP_Poro4"
                type: u8 = 10
                boxMin: vec3 = { 11085.9863, -904.241272, 8528.37305 }
                boxMax: vec3 = { 11265.626, 0, 8708.01367 }
            }
            0xd1f4abb9 = GdsMapObject {
                transform: mtx44 = {
                    -0.999390841, 0, 0.0348994955, 0
                    0, 1, 0, 0
                    -0.0348994955, 0, -0.999390841, 0
                    12953, -181, 11006, 1
                }
                name: string = "LevelProp_HA_AP_Poro5"
                type: u8 = 10
                boxMin: vec3 = { 13082.7178, -178.531403, 10879.7314 }
                boxMax: vec3 = { 13135.9238, 0, 10932.9365 }
            }
            0x37b7e027 = GdsMapObject {
                transform: mtx44 = {
                    -0.642787635, 0, -0.766044438, 0
                    0, 1, 0, 0
                    0.766044438, 0, -0.642787635, 0
                    6955, 57, 5697, 1
                }
                name: string = "LevelProp_HA_AP_Poro6"
                type: u8 = 10
                boxMin: vec3 = { 6888.56885, 5.35230017, 5608.05176 }
                boxMax: vec3 = { 7068.20947, 132.862198, 5787.69238 }
            }
            0x41ac4655 = GdsMapObject {
                transform: mtx44 = {
                    0.74314481, 0, 0.669130623, 0
                    0, 1, 0, 0
                    -0.669130623, 0, 0.74314481, 0
                    2399, 60, 285, 1
                }
                name: string = "LevelProp_HA_AP_Poro7"
                type: u8 = 10
                boxMin: vec3 = { 2379.99365, 19.8418999, 265.579498 }
                boxMax: vec3 = { 2419.85791, 57.6361008, 305.443695 }
            }
            0xbb097fa2 = GdsMapObject {
                transform: mtx44 = {
                    -0.642787635, 0, -0.766044438, 0
                    0, 1, 0, 0
                    0.766044438, 0, -0.642787635, 0
                    8801, -992, 6698, 1
                }
                name: string = "LevelProp_HA_AP_Poro8"
                type: u8 = 10
                boxMin: vec3 = { 8615.4082, -1011.62592, 6578.63672 }
                boxMax: vec3 = { 8655.27246, 0, 6618.50098 }
            }
            0x4412e6e0 = GdsMapObject {
                transform: mtx44 = {
                    -0.927183867, 0, -0.37460658, 0
                    0, 1, 0, 0
                    0.37460658, 0, -0.927183867, 0
                    11151, -174, 11818, 1
                }
                name: string = "LevelProp_HA_AP_ShpNorth"
                type: u8 = 10
                boxMin: vec3 = { 11103.5723, -227.564896, 11980.9316 }
                boxMax: vec3 = { 11156.1406, 0, 12033.502 }
                mapObjectSkinID: u32 = 1
            }
            0xcefbe45c = GdsMapObject {
                transform: mtx44 = {
                    -0.74314481, 0, -0.669130623, 0
                    0, 1, 0, 0
                    0.669130623, 0, -0.74314481, 0
                    605, -264, 1766, 1
                }
                name: string = "LevelProp_HA_AP_ShpSouth"
                type: u8 = 10
                boxMin: vec3 = { 487.395203, -454.723602, 1848.48669 }
                boxMax: vec3 = { 523.012573, 0, 1884.10486 }
                mapObjectSkinID: u32 = 1
            }
            0x699f78ed = GdsMapObject {
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    491, -250, 1949, 1
                }
                name: string = "OrderShop01"
                type: u8 = 6
                boxMin: vec3 = { 103.280296, -584.163574, 1547.81787 }
                boxMax: vec3 = { 890.844604, 225.239899, 2317.48584 }
            }
            0x784c681a = GdsMapObject {
                transform: mtx44 = {
                    0.694658399, 0, -0.719339788, 0
                    0, 1, 0, 0
                    0.719339788, 0, 0.694658399, 0
                    12183, 27, 11844, 1
                }
                name: string = "Turret_ChaosTurretShrine"
                type: u8 = 5
                boxMin: vec3 = { 12121.748, -124.417198, 11866.3105 }
                boxMax: vec3 = { 12215.7051, 0, 11945.4102 }
            }
            0x025653f2 = GdsMapObject {
                transform: mtx44 = {
                    -0.642787635, 0, 0.766044438, 0
                    0, 1, 0, 0
                    -0.766044438, 0, -0.642787635, 0
                    648, -150, 764, 1
                }
                name: string = "Turret_OrderTurretShrine"
                type: u8 = 5
                boxMin: vec3 = { 601.112915, -124.417099, 717.248413 }
                boxMax: vec3 = { 695.07019, 0, 796.348328 }
            }
            0x620d1bba = GdsMapObject {
                transform: mtx44 = {
                    -0.694658339, 0, 0.719339848, 0
                    0, 1, 0, 0
                    -0.719339848, 0, -0.694658339, 0
                    2051, -179, 2560, 1
                }
                name: string = "Turret_T1_C_010"
                type: u8 = 5
                boxMin: vec3 = { 1825.41931, -179.283798, 2341.44189 }
                boxMax: vec3 = { 2247.89331, 0, 2763.91992 }
            }
            0xc87e8800 = GdsMapObject {
                transform: mtx44 = {
                    -0.694658339, 0, 0.719339848, 0
                    0, 1, 0, 0
                    -0.719339848, 0, -0.694658339, 0
                    3809, -155, 3829, 1
                }
                name: string = "Turret_T1_C_07"
                type: u8 = 5
                boxMin: vec3 = { 3634.63403, -155.493301, 3654.62256 }
                boxMax: vec3 = { 3983.48779, 0, 4003.479 }
            }
            0xce298113 = GdsMapObject {
                transform: mtx44 = {
                    -0.694658339, 0, 0.719339848, 0
                    0, 1, 0, 0
                    -0.719339848, 0, -0.694658339, 0
                    4943, -159, 4929, 1
                }
                name: string = "Turret_T1_C_08"
                type: u8 = 5
                boxMin: vec3 = { 4769.05225, -159.769897, 4755.39746 }
                boxMax: vec3 = { 5117.90332, 0, 5104.24854 }
            }
            0x2c05ccdb = GdsMapObject {
                transform: mtx44 = {
                    -0.694658339, 0, 0.719339848, 0
                    0, 1, 0, 0
                    -0.719339848, 0, -0.694658339, 0
                    2493, -182, 2101, 1
                }
                name: string = "Turret_T1_C_09"
                type: u8 = 5
                boxMin: vec3 = { 2281.99854, -182.657303, 1889.94556 }
                boxMax: vec3 = { 2704.46436, 0, 2312.41528 }
            }
            0x527fa2db = GdsMapObject {
                transform: mtx44 = {
                    0.694658399, 0, -0.719339788, 0
                    0, 1, 0, 0
                    0.719339788, 0, 0.694658399, 0
                    7883, -159, 7767, 1
                }
                name: string = "Turret_T2_L_01"
                type: u8 = 5
                boxMin: vec3 = { 7698.27832, -159.114197, 7593.98291 }
                boxMax: vec3 = { 8059.92969, 0, 7884.13428 }
            }
            0x77bd86cf = GdsMapObject {
                transform: mtx44 = {
                    0.694658399, 0, -0.719339788, 0
                    0, 1, 0, 0
                    0.719339788, 0, 0.694658399, 0
                    9017, -161, 8871, 1
                }
                name: string = "Turret_T2_L_02"
                type: u8 = 5
                boxMin: vec3 = { 8835.2998, -161.747498, 8689.03711 }
                boxMax: vec3 = { 9199.95898, 0, 9053.68359 }
            }
            0x95bd47bd = GdsMapObject {
                transform: mtx44 = {
                    0.694658399, 0, -0.719339788, 0
                    0, 1, 0, 0
                    0.719339788, 0, 0.694658399, 0
                    10785, -169, 10117, 1
                }
                name: string = "Turret_T2_L_03"
                type: u8 = 5
                boxMin: vec3 = { 10602.8467, -169.333298, 9935.26367 }
                boxMax: vec3 = { 10967.5059, 0, 10299.9092 }
            }
            0x9723a58d = GdsMapObject {
                transform: mtx44 = {
                    0.694658399, 0, -0.719339788, 0
                    0, 1, 0, 0
                    0.719339788, 0, 0.694658399, 0
                    10353, -177, 10574, 1
                }
                name: string = "Turret_T2_L_04"
                type: u8 = 5
                boxMin: vec3 = { 10142.8916, -177.966599, 10425.874 }
                boxMax: vec3 = { 10507.5508, 0, 10790.5215 }
            }
            0xd894aab9 = null
            0xc4591d42 = null
            0x4a531af9 = null
            0x76800393 = null
            0x14428779 = null
            0xf7e76655 = null
            0xd095358a = null
            0xc7d9ae12 = null
            0x173542b1 = null
            0x52c5028d = null
            0xae413001 = null
            0xc3471ada = null
            0xb9df55cb = null
            0x393b80ce = null
            0xc00eb184 = null
            0x5ab0e415 = null
            0x9c2b7a89 = null
            0x5de80512 = null
            0xebda6303 = null
            0xfeff1b50 = null
            0xb7ffd484 = null
            0x5bb404d5 = null
            0x9859c2c9 = null
            0x2d47b66f = null
            0xbc579f29 = null
            0x2032a816 = null
            0xce6eaaf2 = null
            0xbcc6ad1f = null
            0xe5d07f93 = null
            0xb42d7344 = null
            0x706e24c1 = null
            0x64e068c6 = null
            0x476f378e = null
            0xeb24c613 = null
            0x3ac144d3 = null
            0xb0e2ad3c = null
            0xc2045a74 = null
            0x0388847c = null
            0x19341a94 = null
            0x79e2c9b6 = null
            0xf354a2c3 = null
            0x9b8e1e0c = null
            0x62a2b88b = null
            0x318674d5 = null
            0x16d7f22a = null
            0x8d6b4834 = null
            0xdeb40986 = null
            0xf7fc2549 = null
            0x45f23165 = null
            0x8dc7b61f = null
            0x18236849 = null
            0xc1633a5e = null
            0x6f143ab0 = null
            0x2db14169 = null
            0xd1f2d5d7 = null
            0xc97e71c4 = null
            0x3a569757 = null
            0x262aa2cd = null
            0x11067973 = null
            0xc6910162 = null
            0x7c97a1d0 = null
            0x64104a67 = null
            0x4729f9b6 = null
            0xc10a592b = null
            0x8083d383 = null
            0x5282a5bf = null
            0xafe17908 = null
            0xd0ee3d5d = null
            0x117ff038 = null
            0x9730e527 = null
            0x3802ca01 = null
            0x6ebd7cd9 = null
            0x1cc1f251 = null
            0x3ab859ec = null
            0xad28b19b = null
            0xd463e00e = null
            0xaefeb1cc = null
            0x998ead98 = null
            0x1af1614b = null
            0x11644088 = null
            0xb286611e = null
            0xb03f38bd = null
            0x5833a1a7 = null
            0x713a8fec = null
            0x6b2d855c = null
            0xb83e1403 = null
            0x9854807a = null
            0xe75100c1 = null
            0xe55c9c58 = null
            0x7b97389f = null
            0xf853a087 = null
            0x15ba56ab = null
            0xb223e43c = null
            0xa21addb1 = null
            0xe26b635e = null
            0xe32ad868 = null
            0x230b0764 = null
            0x63c7b243 = null
            0x1f8a28f2 = null
            0x5f375317 = null
            0x9152eb49 = null
            0x1484207e = null
            0xe1adefdc = null
            0xa3b7616d = null
            0xe542bd10 = null
            0x8c51cc90 = null
            0x4d0b82d3 = null
            0x88a16112 = null
            0x886305a9 = null
            0x0aac2f84 = null
            0x383255de = null
            0x3cab7ae0 = null
            0xd5bcb3e4 = null
            0xb980f96d = null
            0x3eca47aa = null
            0x86194591 = null
            0x6a735c66 = null
            0x12c8d012 = null
            0x2ecb6ca6 = null
            0x2934b6f8 = null
            0xdb830559 = null
            0xe6a6c383 = null
            0x52f2c505 = null
            0x65c89386 = null
            0x1aa30287 = null
            0x6524e15d = null
            0x53f7fc1b = null
            0x36bc5047 = null
            0x5f0b1da0 = null
            0xec72b8da = null
            0xf5755802 = null
            0xc5c5b0e8 = null
            0xc42637bb = null
            0xddd46ad5 = null
            0x783cbf04 = null
            0x5ecbbc38 = null
            0x2aeb16cb = null
            0xd0246f00 = null
            0xa814dc9e = null
            0x6b265f4c = null
            0xf05786e1 = null
            0xded9dd63 = null
            0x4833f830 = null
            0xccad91f4 = null
            0x639119dc = null
            0x11e7bcfc = null
            0x8b9c4c98 = null
            0xb80025c1 = null
            0x6ee456c1 = null
            0xf7098fc8 = null
            0x746a583e = null
            0x8d0ac3e9 = null
            0xaea161f9 = null
            0x30cbc82f = null
            0x7c05e9b3 = null
            0x0fa28b01 = null
            0xb9908ec8 = null
            0xf1a00ab2 = null
            0xaf14a22e = null
            0x732938f4 = null
            0x8c0e3517 = null
            0x03e4e265 = null
            0x9a6a2059 = null
            0x1c4b1533 = null
            0xf34c1e98 = null
            0x0b2113be = null
            0x3218461f = null
            0x012d1a57 = null
            0x9179070b = null
            0x4c1aaad0 = null
            0x6528717e = null
            0xaee96fd9 = null
            0x15d51b61 = null
            0x3ba355db = null
            0xb786fdf0 = null
            0x486c21ba = null
            0x3a17fd26 = null
            0xb825f4d8 = null
            0x7f24a336 = null
            0x282c8378 = null
            0x0ac32493 = null
            0xd8592b1f = null
            0x02fba2b3 = null
            0xc1670c60 = null
            0x004e8c40 = null
            0x66332a58 = null
            0xd8dfdc2b = null
            0x09fdeb38 = null
            0x638fd5d2 = null
            0xa4db5f77 = null
            0x8f8e0a80 = null
            0x9f11ae9a = null
            0xba5deb36 = null
            0x481503a1 = null
            0xd6b055fd = null
            0x8e5899ec = null
            0xfdf5b6d7 = null
            0x7415f7b7 = null
            0x96c5f113 = null
            0x0164e04a = null
            0xed03485b = null
            0x34d5f6e7 = null
            0x2541faa9 = null
            0x19ecc3eb = null
            0x3efe4d6e = null
            0x39046019 = null
            0x1d10e76e = null
            0x305c540b = null
            0x4062f23f = null
            0x7c2df4ed = null
            0xabc22b29 = null
            0xca1fec82 = null
            0xea04f182 = null
            0x0e52857c = null
            0x7867b097 = null
            0x78327598 = null
            0xda5e85c8 = null
            0x290befe1 = null
            0x6f75e6a2 = null
            0xa9d97e08 = null
            0x74215c57 = null
            0x222be3c1 = null
            0xb2d8e663 = null
            0x3ffb8f3f = null
            0x0f85f97f = null
            0x7e105fda = null
            0x011f55ca = null
            0x61dc9f06 = null
            0x19853122 = null
            0xab239eed = null
            0x6e19cdad = null
            0xf7e2bdfe = null
            0xe3150c17 = null
            0x3964f585 = null
            0xed0e7d00 = null
            0xb86ce58a = null
            0x1142b6bc = null
            0x228dc6ab = null
            0x35feb017 = null
            0xf961d75d = null
            0xba0c2172 = null
            0x68d5ba38 = null
            0x568571b0 = null
            0xff627920 = null
            0xf03a5827 = null
            0x64554080 = null
            0xaab2e607 = null
            0x4f096b41 = null
            0x4b0307dc = null
            0x8e11d7a8 = null
            0x173ae141 = null
            0x2fae2bbb = null
            0xba445d91 = null
            0x70857576 = null
            0x1e5a40c8 = null
            0xecb88c49 = null
            0xbcb5d17f = null
            0x324d40de = null
            0x683db32e = null
            0x6a8c9bf9 = null
            0x790933e2 = null
            0xd6dc8ace = null
            0xe05771cc = null
            0xcfdd7f62 = null
            0x43f23a8d = null
            0x12fded64 = null
            0x931c0dcb = null
            0x2a93c586 = null
            0xad0479a7 = null
            0xce608d32 = null
            0xdfe49d2b = null
            0x774aa671 = null
            0x696ae098 = null
            0xafa05067 = null
            0xdc544118 = null
            0x08775673 = null
            0x10ded08e = null
            0xc49bbbf4 = null
            0x7725f441 = null
            0x78757265 = null
            0xb494d47d = null
            0x0d115d51 = null
            0xc5a1cfee = null
            0x54d6d7f9 = null
            0x4a4e30e6 = null
            0x36242864 = null
            0xabcfef0a = null
            0x24b848d4 = null
            0xe794fb6d = null
            0xf127935a = null
            0x335194ef = null
            0xccc79e1f = null
            0x1536e402 = null
            0x1e48858f = null
            0x0c436e7a = null
            0xa9d02f0d = null
            0x7836b187 = null
            0x3fd2572f = null
            0x0294f61f = null
            0x2ca8d676 = null
            0xe7fda40e = null
            0x8b319289 = null
            0xba421ccb = null
            0xfc9881e8 = null
            0xb2fb45d6 = null
            0x550f3c71 = null
            0x66459b33 = null
            0x5c7ade9e = null
            0x6b7e061c = null
            0x49886aee = null
            0xf5673fc1 = null
            0x50469abe = null
            0x0c992bd8 = null
            0x7cbbc8a6 = null
            0xf21985c2 = null
            0xcb8be892 = null
            0xc0fe5c22 = null
            0xff1fbd09 = null
            0xb957210d = null
            0x06d3f702 = null
            0x9a1fa80e = null
            0x082ad524 = null
            0xd9dea9ca = null
            0x2e032a50 = null
            0xf9f0f132 = null
            0xd674e595 = null
            0xd43fd718 = null
            0xad0d1b07 = null
            0x7a8361cc = null
            0x6e125a50 = null
            0x7a521f1a = null
            0x595d9bee = null
            0x077a03fd = null
            0xdcce076b = null
            0xad5f780a = null
            0xbcded727 = null
            0xb8d5ea90 = null
            0x074ae47b = null
            0x79e17a8a = null
            0x2896ac41 = null
            0xd9337575 = null
            0x21b84374 = null
            0x4abda284 = null
            0x09f16d4e = null
            0xd1f362e8 = null
            0x6b067caa = null
            0x154c66b5 = null
            0x2ff276a1 = null
            0xc64af566 = null
            0x5db91d2b = null
            0x27b23fd5 = null
            0xc5e861c7 = null
            0x3749ef9e = null
            0x3e94acf5 = null
            0xff0f8826 = null
            0x6027bdf3 = null
            0x9fdafb20 = null
            0xd190a216 = null
            0x13c34854 = null
            0x0dbcb277 = null
            0x2e5cc3c5 = null
            0xd97e3c1a = null
            0xd9733cd1 = null
            0x2993e0e8 = null
            0x1b76265e = null
            0xeb0e977e = null
            0xf75f6c84 = MapParticle {
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    4690.18018, -104.679001, 4693.6499, 1
                }
                name: string = "BW_Motes_WespFly_01_2"
                system: link = "Maps/Particles/HA/Bilgewater/BW_Motes_WespFly_01"
            }
            0xb637199e = MapLocator {
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    5929.7002, -194, 5190.8999, 1
                }
                name: string = "HA_AP_HealthRelic_Order_Outer"
            }
            0xf0aee321 = MapLocator {
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    4790.2002, -188.5, 3934.30005, 1
                }
                name: string = "HA_AP_HealthRelic_Order_Inner"
            }
            0xf8485de4 = MapLocator {
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    8893.90039, -187.699997, 7889, 1
                }
                name: string = "HA_AP_HealthRelic_Chaos_Inner"
            }
            0x6b781a48 = null
            0xe2b41083 = null
            0x7ae735ac = null
            0x76905ef1 = null
            0xea7897ca = null
            0xfe2feaac = null
            0x4f3b6d0c = null
            0xf689a4d3 = null
            0xbcf99d35 = null
            0x0e46f339 = null
            0x6cfc0c60 = null
            0xe84f45f6 = null
            0x4631d5b0 = null
            0xb74671df = null
            0x4678087c = null
            0xdae71b85 = null
            0x2aa0edfe = null
            0x494f894a = null
            0x282bfabc = null
            0x0e05aa11 = null
            0xda5edc9a = null
            0x3cf8574f = null
            0x1af752bc = null
            0x1abfe2aa = null
            0xe790002f = null
            0x51a8f8b5 = null
            0x8bf553b6 = null
            0xe8915d48 = null
            0x676ec870 = null
            0xbd00dde5 = null
            0x58caaa3d = null
            0x2ae44b09 = null
            0x44fc0497 = null
            0x3f795aa4 = null
            0xbf093870 = null
            0x625a306e = null
            0x1af64270 = null
            0x54c9bb0f = null
            0xc5c27c68 = null
            0x03d55c59 = null
            0x292ff1c5 = null
            0xe0f86624 = null
            0x1997e2d4 = null
            0x82b83779 = null
            0x941b9a8b = null
            0x2a81947e = null
            0x892f31b0 = null
            0xf75220ed = null
            0x4e51f254 = null
            0x6ead99d4 = null
            0xc6922dab = null
            0xa8b63163 = null
            0x4ca4b8d7 = null
            0x3460a7df = null
            0xb16731e7 = null
            0xc2c4349e = null
            0x75f07b29 = null
            0x7216cd09 = null
            0x00bd8960 = null
            0x6db3428f = null
            0x0f3f5eb0 = null
            0x1a44fc50 = null
            0x48fbc521 = null
            0x5e397e7b = null
            0x5a706ec3 = null
            0x541dc41b = null
            0x30124049 = null
            0xf9907f0e = null
            0xaec3a6d3 = null
            0x126b5211 = null
            0xd554ffa5 = null
            0x92bc65e9 = null
            0xc9136319 = null
            0x2a3588b9 = null
            0xa65c2d62 = null
            0xe36ef38d = null
            0xaccaf848 = null
            0x225620a0 = null
            0x87feb87d = null
            0xb801f84f = null
            0xf32bb576 = null
            0xa3789ae5 = null
            0x0ef3cc73 = null
            0xa007ffd0 = null
            0x03c8436e = null
            0x3c4ca2ef = null
            0xa96d867c = null
            0xdc263833 = null
            0x674119a9 = null
            0xb5008b1d = null
            0x8958445f = null
            0xf0b74599 = null
            0x66d64b10 = null
            0x2e25ce89 = null
            0x2f1e3323 = null
            0x0f7e5713 = null
            0x97825ae8 = null
            0xe67fe38f = null
            0x1d08f2e9 = null
            0xe8246f23 = null
            0xac09e282 = null
            0x913b8636 = null
            0xf5150eed = null
            0xe97f073f = null
            0xe17ab034 = null
            0x60a375f0 = null
            0x7a22a256 = null
            0x00c21710 = null
            0x3ebd27e4 = null
            0x221780ab = null
            0x2e7012ae = null
            0xeb6a1482 = MapLocator {
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    7585.32129, -193.800064, 6798.5625, 1
                }
                name: string = "HA_AP_HealthRelic_Chaos_Outer"
            }
            0x8fdd32d2 = null
            0x15d960c4 = null
            0x20a2fb39 = null
            0x706e0b24 = null
            0x61203bac = null
            0xfb069e8c = null
            0x04c92c97 = null
            0xc9538d7e = null
            0xd555d8ee = null
            0x73d4b0ee = null
            0xefe4ac8a = null
            0x27dabaf2 = null
            0xbd1a3e00 = null
            0x3bc7efcc = null
            0x6f60a4ec = null
            0xb2677026 = null
            0x32429991 = null
            0x0ab35e95 = null
            0x4ba953d8 = null
            0xb1b3710b = null
            0x7d3a5206 = null
            0x683c126b = null
            0x49fd8636 = null
            0x16852f10 = null
            0xa8798538 = null
            0x3854caeb = null
            0x412fceb5 = null
            0xe3379708 = null
            0x0a1affdc = null
            0xddaf3080 = null
            0x9b78e6b6 = null
            0x3c31c16d = null
            0x82234a6e = MapParticle {
                transform: mtx44 = {
                    0.710171103, 0, -0.704029143, 0
                    0, 1, 0, 0
                    0.704029143, 0, 0.710171103, 0
                    12487.5312, -205.267639, 8633.75, 1
                }
                name: string = "BW_Peref_WindowGlow_1_14"
                system: link = "Maps/Particles/HA/Bilgewater/BW_Peref_WindowGlow_1"
            }
            0xf19324d7 = MapParticle {
                transform: mtx44 = {
                    0.710171103, 0, -0.704029143, 0
                    0, 1, 0, 0
                    0.704029143, 0, 0.710171103, 0
                    13051.249, 405.357239, 8969.83789, 1
                }
                name: string = "BW_Peref_WindowGlow_1_15"
                system: link = "Maps/Particles/HA/Bilgewater/BW_Peref_WindowGlow_1"
            }
            0x582b9a99 = MapParticle {
                transform: mtx44 = {
                    0.710171103, 0, -0.704029143, 0
                    0, 1, 0, 0
                    0.704029143, 0, 0.710171103, 0
                    11888.4092, -711.165466, 8150.03564, 1
                }
                name: string = "BW_Peref_WindowGlow_1_16"
                system: link = "Maps/Particles/HA/Bilgewater/BW_Peref_WindowGlow_1"
            }
            0xfe38a59e = MapParticle {
                transform: mtx44 = {
                    0.710171103, 0, -0.704029143, 0
                    0, 1, 0, 0
                    0.704029143, 0, 0.710171103, 0
                    12025.4111, -960.951233, 7997.50049, 1
                }
                name: string = "BW_Peref_WindowGlow_1_17"
                system: link = "Maps/Particles/HA/Bilgewater/BW_Peref_WindowGlow_1"
            }
            0xd88d8cef = MapParticle {
                transform: mtx44 = {
                    -0.527685523, 0, 0.849440098, 0
                    0, 1, 0, 0
                    -0.849440098, 0, -0.527685523, 0
                    14984.5938, -425.156281, 7156.73877, 1
                }
                name: string = "BW_Chimney_Smoke2"
                system: link = "Maps/Particles/HA/Bilgewater/BW_Chimney_Smoke"
            }
            0x3c37c4f9 = MapParticle {
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    7148.61475, -1328.09106, 10577.6416, 1
                }
                name: string = "BW_Chimney_Smoke3"
                system: link = "Maps/Particles/HA/Bilgewater/BW_Chimney_Smoke"
            }
            0x8388286e = MapParticle {
                transform: mtx44 = {
                    0.774495423, 0, -0.632579505, 0
                    0, 1, 0, 0
                    0.632579505, 0, 0.774495423, 0
                    5482.93506, -1838.44299, 11564.9736, 1
                }
                name: string = "BW_Chimney_Smoke4"
                system: link = "Maps/Particles/HA/Bilgewater/BW_Chimney_Smoke"
            }
            0x7789889e = null
            0x60bb0c90 = null
            0x33a8f1aa = null
            0xc8b189a2 = null
            0x41c1561c = null
            0xfd9dea87 = null
            0x92c2c8e4 = null
            0xfbd9bff1 = null
            0x9b63d28a = null
            0xdf8dcb3a = null
            0xbef7f8c0 = null
            0x378bbb70 = null
            0x907e6da2 = null
            0x4270b263 = null
            0x89684503 = null
            0xce157bd9 = null
            0x3df8bf18 = null
            0xf7458704 = null
            0x99da349b = null
            0xf60c5d4f = null
            0xc7615622 = null
            0xf227ef4d = null
            0x5b856c21 = null
            0x6bd4cf2e = null
            0xec5f4312 = null
            0x2c9a1b56 = null
            0xd3ac9ce4 = null
            0x5d35ee9e = null
            0x1e592195 = null
            0xfb06ff7a = null
            0xfbfa57b9 = null
            0x683623de = null
            0xff610e13 = null
            0x6b66915c = null
            0x422f9f19 = null
            0x02022bf9 = null
            0xb68d7fb9 = null
            0xe7c5c006 = null
            0x4533d5c1 = null
            0x728f92f1 = null
            0x1233da50 = null
            0x12193704 = null
            0x34b71891 = null
            0x3df86daa = null
            0x012333a6 = null
            0xb6cacfa6 = null
            0xb6f55b8b = null
            0x658ecc6f = null
            0x451a202c = null
            0x817627f5 = null
            0x63ad2ee6 = null
            0x07c8b3c0 = null
            0x8f8a1745 = null
            0x5d0e86b6 = null
            0x68b6d0ba = null
            0xe8a07b47 = null
            0x6b6cc914 = null
            0x90703693 = null
            0x11fd2f0b = null
            0x9e9e88e8 = null
            0x22d6d37b = null
            0xec584428 = null
            0x8d7cbaa8 = null
            0x8ae7b5c6 = null
            0x205fbb81 = null
            0xed4acb8b = null
            0x2dba876d = null
            0xbeb5e980 = null
            0xe6688660 = null
            0xe9a30d95 = null
            0x0d0963fb = null
            0xde3c2365 = null
            0xe8c29848 = null
            0x19a25fae = null
            0x97da1a6f = null
            0xe2b89716 = null
            0xbf95727a = null
            0xfd2687a3 = null
            0xf25da3b1 = null
            0xc2e1e137 = null
            0x684a82f3 = null
            0x37805675 = null
            0x92e9d71e = null
            0xfc806123 = null
            0xe4fd7641 = null
            0xe7d95acd = null
            0x6426d161 = null
            0x45dc0984 = null
            0x19006a90 = null
            0xefb47052 = null
            0xb869a0e4 = null
            0x8d77d7bc = null
            0xf4e81afb = null
            0x16394f2e = null
            0x19a76258 = null
            0x9f3ed27a = null
            0x8f0e5af4 = null
            0x3c88284a = null
            0x58a4fb7b = null
        }
    }
}
