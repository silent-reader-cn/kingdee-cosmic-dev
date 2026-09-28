# 预测计划-mds_forecastplandata

## 需求明细-子表 t_mds_fcdatatsentry

- **表名称：** 需求明细-子表
- **表名：** t_mds_fcdatatsentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | freceive1 | S1 | numeric | 23 | 10 | √ | 0.0000000000 | S1 |
| 3 | fbizunit | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 4 | freceive2 | S2 | numeric | 23 | 10 | √ | 0.0000000000 | S2 |
| 5 | fmatverid | 物料版本 | int8 | 64 |  | √ | 0 | [物料版本 bd_bomversion_new](../basedata_files/bd_bomversion_new.md) |
| 6 | freceive3 | S3 | numeric | 23 | 10 | √ | 0.0000000000 | S3 |
| 7 | freceive4 | S4 | numeric | 23 | 10 | √ | 0.0000000000 | S4 |
| 8 | freceive5 | S5 | numeric | 23 | 10 | √ | 0.0000000000 | S5 |
| 9 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 10 | freceive6 | S6 | numeric | 23 | 10 | √ | 0.0000000000 | S6 |
| 11 | freceive7 | S7 | numeric | 23 | 10 | √ | 0.0000000000 | S7 |
| 12 | freceive8 | S8 | numeric | 23 | 10 | √ | 0.0000000000 | S8 |
| 13 | fqty78 | T78 | numeric | 23 | 10 | √ | 0.0000000000 | T78 |
| 14 | freceive9 | S9 | numeric | 23 | 10 | √ | 0.0000000000 | S9 |
| 15 | fqty77 | T77 | numeric | 23 | 10 | √ | 0.0000000000 | T77 |
| 16 | fqty79 | T79 | numeric | 23 | 10 | √ | 0.0000000000 | T79 |
| 17 | fqty74 | T74 | numeric | 23 | 10 | √ | 0.0000000000 | T74 |
| 18 | fqty73 | T73 | numeric | 23 | 10 | √ | 0.0000000000 | T73 |
| 19 | fqty76 | T76 | numeric | 23 | 10 | √ | 0.0000000000 | T76 |
| 20 | fqty75 | T75 | numeric | 23 | 10 | √ | 0.0000000000 | T75 |
| 21 | fqty70 | T70 | numeric | 23 | 10 | √ | 0.0000000000 | T70 |
| 22 | fqty72 | T72 | numeric | 23 | 10 | √ | 0.0000000000 | T72 |
| 23 | fqty71 | T71 | numeric | 23 | 10 | √ | 0.0000000000 | T71 |
| 24 | feditcreatedate | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 25 | fqty67 | T67 | numeric | 23 | 10 | √ | 0.0000000000 | T67 |
| 26 | fqty66 | T66 | numeric | 23 | 10 | √ | 0.0000000000 | T66 |
| 27 | fqty69 | T69 | numeric | 23 | 10 | √ | 0.0000000000 | T69 |
| 28 | fqty68 | T68 | numeric | 23 | 10 | √ | 0.0000000000 | T68 |
| 29 | fqty63 | T63 | numeric | 23 | 10 | √ | 0.0000000000 | T63 |
| 30 | fqty62 | T62 | numeric | 23 | 10 | √ | 0.0000000000 | T62 |
| 31 | fqty65 | T65 | numeric | 23 | 10 | √ | 0.0000000000 | T65 |
| 32 | fqty64 | T64 | numeric | 23 | 10 | √ | 0.0000000000 | T64 |
| 33 | fqty61 | T61 | numeric | 23 | 10 | √ | 0.0000000000 | T61 |
| 34 | fqty60 | T60 | numeric | 23 | 10 | √ | 0.0000000000 | T60 |
| 35 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 36 | flicenseno | 许可证编号 | int8 | 64 |  | √ | 0 | [许可证 bd_licence](../sbd_files/bd_licence.md) |
| 37 | fqty108 | T108 | numeric | 23 | 10 | √ | 0.0000000000 | T108 |
| 38 | fqty107 | T107 | numeric | 23 | 10 | √ | 0.0000000000 | T107 |
| 39 | fprodorg | 供应组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 40 | fplangp | 计划组 | int8 | 64 |  | √ | 0 | [计划业务组 mpdm_demandgroup](../mpdm_files/mpdm_demandgroup.md) |
| 41 | fqty109 | T109 | numeric | 23 | 10 | √ | 0.0000000000 | T109 |
| 42 | fqty100 | T100 | numeric | 23 | 10 | √ | 0.0000000000 | T100 |
| 43 | fqty59 | T59 | numeric | 23 | 10 | √ | 0.0000000000 | T59 |
| 44 | fqty102 | T102 | numeric | 23 | 10 | √ | 0.0000000000 | T102 |
| 45 | fqty101 | T101 | numeric | 23 | 10 | √ | 0.0000000000 | T101 |
| 46 | fqty56 | T56 | numeric | 23 | 10 | √ | 0.0000000000 | T56 |
| 47 | fqty104 | T104 | numeric | 23 | 10 | √ | 0.0000000000 | T104 |
| 48 | fqty55 | T55 | numeric | 23 | 10 | √ | 0.0000000000 | T55 |
| 49 | fqty103 | T103 | numeric | 23 | 10 | √ | 0.0000000000 | T103 |
| 50 | fqty58 | T58 | numeric | 23 | 10 | √ | 0.0000000000 | T58 |
| 51 | fqty106 | T106 | numeric | 23 | 10 | √ | 0.0000000000 | T106 |
| 52 | fqty57 | T57 | numeric | 23 | 10 | √ | 0.0000000000 | T57 |
| 53 | fqty105 | T105 | numeric | 23 | 10 | √ | 0.0000000000 | T105 |
| 54 | fqty52 | T52 | numeric | 23 | 10 | √ | 0.0000000000 | T52 |
| 55 | fqty51 | T51 | numeric | 23 | 10 | √ | 0.0000000000 | T51 |
| 56 | fqty54 | T54 | numeric | 23 | 10 | √ | 0.0000000000 | T54 |
| 57 | fqty53 | T53 | numeric | 23 | 10 | √ | 0.0000000000 | T53 |
| 58 | fqty50 | T50 | numeric | 23 | 10 | √ | 0.0000000000 | T50 |
| 59 | fremark | 备注 | varchar | 300 |  | √ | ' ' | 备注 |
| 60 | fqty49 | T49 | numeric | 23 | 10 | √ | 0.0000000000 | T49 |
| 61 | freceive10 | S10 | numeric | 23 | 10 | √ | 0.0000000000 | S10 |
| 62 | fqty48 | T48 | numeric | 23 | 10 | √ | 0.0000000000 | T48 |
| 63 | fqty45 | T45 | numeric | 23 | 10 | √ | 0.0000000000 | T45 |
| 64 | fqty44 | T44 | numeric | 23 | 10 | √ | 0.0000000000 | T44 |
| 65 | fqty47 | T47 | numeric | 23 | 10 | √ | 0.0000000000 | T47 |
| 66 | fqty46 | T46 | numeric | 23 | 10 | √ | 0.0000000000 | T46 |
| 67 | fqty2 | T2 | numeric | 23 | 10 | √ | 0.0000000000 | T2 |
| 68 | fqty41 | T41 | numeric | 23 | 10 | √ | 0.0000000000 | T41 |
| 69 | fqty3 | T3 | numeric | 23 | 10 | √ | 0.0000000000 | T3 |
| 70 | fqty40 | T40 | numeric | 23 | 10 | √ | 0.0000000000 | T40 |
| 71 | fqty43 | T43 | numeric | 23 | 10 | √ | 0.0000000000 | T43 |
| 72 | fqty1 | T1 | numeric | 23 | 10 | √ | 0.0000000000 | T1 |
| 73 | fqty42 | T42 | numeric | 23 | 10 | √ | 0.0000000000 | T42 |
| 74 | fqty6 | T6 | numeric | 23 | 10 | √ | 0.0000000000 | T6 |
| 75 | fqty7 | T7 | numeric | 23 | 10 | √ | 0.0000000000 | T7 |
| 76 | flevel1edit | flevel1edit | varchar | 200 |  | √ | ' ' |  |
| 77 | fqty4 | T4 | numeric | 23 | 10 | √ | 0.0000000000 | T4 |
| 78 | fqty5 | T5 | numeric | 23 | 10 | √ | 0.0000000000 | T5 |
| 79 | fqty8 | T8 | numeric | 23 | 10 | √ | 0.0000000000 | T8 |
| 80 | fqty9 | T9 | numeric | 23 | 10 | √ | 0.0000000000 | T9 |
| 81 | fid2 | fid2 | int8 | 64 |  | √ | 0 |  |
| 82 | fqty129 | T129 | numeric | 23 | 10 | √ | 0.0000000000 | T129 |
| 83 | fqty38 | T38 | numeric | 23 | 10 | √ | 0.0000000000 | T38 |
| 84 | fqty122 | T122 | numeric | 23 | 10 | √ | 0.0000000000 | T122 |
| 85 | fqty37 | T37 | numeric | 23 | 10 | √ | 0.0000000000 | T37 |
| 86 | fqty121 | T121 | numeric | 23 | 10 | √ | 0.0000000000 | T121 |
| 87 | fqty124 | T124 | numeric | 23 | 10 | √ | 0.0000000000 | T124 |
| 88 | fqty39 | T39 | numeric | 23 | 10 | √ | 0.0000000000 | T39 |
| 89 | fqty123 | T123 | numeric | 23 | 10 | √ | 0.0000000000 | T123 |
| 90 | fqty34 | T34 | numeric | 23 | 10 | √ | 0.0000000000 | T34 |
| 91 | fqty126 | T126 | numeric | 23 | 10 | √ | 0.0000000000 | T126 |
| 92 | fqty33 | T33 | numeric | 23 | 10 | √ | 0.0000000000 | T33 |
| 93 | fqty125 | T125 | numeric | 23 | 10 | √ | 0.0000000000 | T125 |
| 94 | fqty36 | T36 | numeric | 23 | 10 | √ | 0.0000000000 | T36 |
| 95 | fqty128 | T128 | numeric | 23 | 10 | √ | 0.0000000000 | T128 |
| 96 | fmdsuser | fmdsuser | int8 | 64 |  | √ | 0 |  |
| 97 | fqty35 | T35 | numeric | 23 | 10 | √ | 0.0000000000 | T35 |
| 98 | fqty127 | T127 | numeric | 23 | 10 | √ | 0.0000000000 | T127 |
| 99 | fqty30 | T30 | numeric | 23 | 10 | √ | 0.0000000000 | T30 |
| 100 | fauxproperty | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 101 | fqty32 | T32 | numeric | 23 | 10 | √ | 0.0000000000 | T32 |
| 102 | fqty31 | T31 | numeric | 23 | 10 | √ | 0.0000000000 | T31 |
| 103 | fqty131 | T131 | numeric | 23 | 10 | √ | 0.0000000000 | T131 |
| 104 | fqty130 | T130 | numeric | 23 | 10 | √ | 0.0000000000 | T130 |
| 105 | fofferingedit | fofferingedit | varchar | 200 |  | √ | ' ' |  |
| 106 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 107 | ftracknumber | 跟踪号 | int8 | 64 |  | √ | 0 | [跟踪号 bd_tracknumber](../sbd_files/bd_tracknumber.md) |
| 108 | fqty119 | T119 | numeric | 23 | 10 | √ | 0.0000000000 | T119 |
| 109 | fqty118 | T118 | numeric | 23 | 10 | √ | 0.0000000000 | T118 |
| 110 | fprojectid | 项目编码 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 111 | fqty27 | T27 | numeric | 23 | 10 | √ | 0.0000000000 | T27 |
| 112 | fqty111 | T111 | numeric | 23 | 10 | √ | 0.0000000000 | T111 |
| 113 | fqty26 | T26 | numeric | 23 | 10 | √ | 0.0000000000 | T26 |
| 114 | fqty110 | T110 | numeric | 23 | 10 | √ | 0.0000000000 | T110 |
| 115 | fqty29 | T29 | numeric | 23 | 10 | √ | 0.0000000000 | T29 |
| 116 | fqty113 | T113 | numeric | 23 | 10 | √ | 0.0000000000 | T113 |
| 117 | fqty28 | T28 | numeric | 23 | 10 | √ | 0.0000000000 | T28 |
| 118 | fqty112 | T112 | numeric | 23 | 10 | √ | 0.0000000000 | T112 |
| 119 | fqty23 | T23 | numeric | 23 | 10 | √ | 0.0000000000 | T23 |
| 120 | fqty115 | T115 | numeric | 23 | 10 | √ | 0.0000000000 | T115 |
| 121 | fqty22 | T22 | numeric | 23 | 10 | √ | 0.0000000000 | T22 |
| 122 | fqty114 | T114 | numeric | 23 | 10 | √ | 0.0000000000 | T114 |
| 123 | fqty25 | T25 | numeric | 23 | 10 | √ | 0.0000000000 | T25 |
| 124 | fqty117 | T117 | numeric | 23 | 10 | √ | 0.0000000000 | T117 |
| 125 | fqty24 | T24 | numeric | 23 | 10 | √ | 0.0000000000 | T24 |
| 126 | fqty116 | T116 | numeric | 23 | 10 | √ | 0.0000000000 | T116 |
| 127 | fqty21 | T21 | numeric | 23 | 10 | √ | 0.0000000000 | T21 |
| 128 | fqty20 | T20 | numeric | 23 | 10 | √ | 0.0000000000 | T20 |
| 129 | fbom | BOM编码 | int8 | 64 |  | √ | 0 | [BOM维护 pdm_mftbom](../fmm_files/pdm_mftbom.md) |
| 130 | fqty120 | T120 | numeric | 23 | 10 | √ | 0.0000000000 | T120 |
| 131 | fcustomerid | 客户 | int8 | 64 |  | √ | 0 | [客户 bd_customer](../basedata_files/bd_customer.md) |
| 132 | fspdt | fspdt | varchar | 100 |  | √ | ' ' |  |
| 133 | fentrymodifier | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 134 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 135 | fqty19 | T19 | numeric | 23 | 10 | √ | 0.0000000000 | T19 |
| 136 | fqty16 | T16 | numeric | 23 | 10 | √ | 0.0000000000 | T16 |
| 137 | fqty144 | T144 | numeric | 23 | 10 | √ | 0.0000000000 | T144 |
| 138 | fqty15 | T15 | numeric | 23 | 10 | √ | 0.0000000000 | T15 |
| 139 | fqty143 | T143 | numeric | 23 | 10 | √ | 0.0000000000 | T143 |
| 140 | fqty18 | T18 | numeric | 23 | 10 | √ | 0.0000000000 | T18 |
| 141 | fqty146 | T146 | numeric | 23 | 10 | √ | 0.0000000000 | T146 |
| 142 | fseq2 | fseq2 | int8 | 64 |  | √ | 0 |  |
| 143 | fqty17 | T17 | numeric | 23 | 10 | √ | 0.0000000000 | T17 |
| 144 | fqty145 | T145 | numeric | 23 | 10 | √ | 0.0000000000 | T145 |
| 145 | fqty12 | T12 | numeric | 23 | 10 | √ | 0.0000000000 | T12 |
| 146 | fqty148 | T148 | numeric | 23 | 10 | √ | 0.0000000000 | T148 |
| 147 | fqty11 | T11 | numeric | 23 | 10 | √ | 0.0000000000 | T11 |
| 148 | fqty99 | T99 | numeric | 23 | 10 | √ | 0.0000000000 | T99 |
| 149 | fqty147 | T147 | numeric | 23 | 10 | √ | 0.0000000000 | T147 |
| 150 | fqty14 | T14 | numeric | 23 | 10 | √ | 0.0000000000 | T14 |
| 151 | fbonded | 保税 | bpchar | 1 |  | √ | '0' | 保税 |
| 152 | fqty13 | T13 | numeric | 23 | 10 | √ | 0.0000000000 | T13 |
| 153 | fqty149 | T149 | numeric | 23 | 10 | √ | 0.0000000000 | T149 |
| 154 | fqty96 | T96 | numeric | 23 | 10 | √ | 0.0000000000 | T96 |
| 155 | fqty95 | T95 | numeric | 23 | 10 | √ | 0.0000000000 | T95 |
| 156 | fqty10 | T10 | numeric | 23 | 10 | √ | 0.0000000000 | T10 |
| 157 | fqty98 | T98 | numeric | 23 | 10 | √ | 0.0000000000 | T98 |
| 158 | fqty97 | T97 | numeric | 23 | 10 | √ | 0.0000000000 | T97 |
| 159 | fqty92 | T92 | numeric | 23 | 10 | √ | 0.0000000000 | T92 |
| 160 | fqty91 | T91 | numeric | 23 | 10 | √ | 0.0000000000 | T91 |
| 161 | fqty150 | T150 | numeric | 23 | 10 | √ | 0.0000000000 | T150 |
| 162 | fqty94 | T94 | numeric | 23 | 10 | √ | 0.0000000000 | T94 |
| 163 | feditdate | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 164 | fqty93 | T93 | numeric | 23 | 10 | √ | 0.0000000000 | T93 |
| 165 | fqty90 | T90 | numeric | 23 | 10 | √ | 0.0000000000 | T90 |
| 166 | fqty133 | T133 | numeric | 23 | 10 | √ | 0.0000000000 | T133 |
| 167 | fqty132 | T132 | numeric | 23 | 10 | √ | 0.0000000000 | T132 |
| 168 | fqty135 | T135 | numeric | 23 | 10 | √ | 0.0000000000 | T135 |
| 169 | fqty134 | T134 | numeric | 23 | 10 | √ | 0.0000000000 | T134 |
| 170 | fedituser | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 171 | fqty89 | T89 | numeric | 23 | 10 | √ | 0.0000000000 | T89 |
| 172 | fqty137 | T137 | numeric | 23 | 10 | √ | 0.0000000000 | T137 |
| 173 | fqty88 | T88 | numeric | 23 | 10 | √ | 0.0000000000 | T88 |
| 174 | fqty136 | T136 | numeric | 23 | 10 | √ | 0.0000000000 | T136 |
| 175 | fqty139 | T139 | numeric | 23 | 10 | √ | 0.0000000000 | T139 |
| 176 | fqty138 | T138 | numeric | 23 | 10 | √ | 0.0000000000 | T138 |
| 177 | fqty85 | T85 | numeric | 23 | 10 | √ | 0.0000000000 | T85 |
| 178 | fqty84 | T84 | numeric | 23 | 10 | √ | 0.0000000000 | T84 |
| 179 | fqty87 | T87 | numeric | 23 | 10 | √ | 0.0000000000 | T87 |
| 180 | fqty86 | T86 | numeric | 23 | 10 | √ | 0.0000000000 | T86 |
| 181 | fqty81 | T81 | numeric | 23 | 10 | √ | 0.0000000000 | T81 |
| 182 | fqty140 | T140 | numeric | 23 | 10 | √ | 0.0000000000 | T140 |
| 183 | fqty80 | T80 | numeric | 23 | 10 | √ | 0.0000000000 | T80 |
| 184 | fqty83 | T83 | numeric | 23 | 10 | √ | 0.0000000000 | T83 |
| 185 | fqty142 | T142 | numeric | 23 | 10 | √ | 0.0000000000 | T142 |
| 186 | fqty82 | T82 | numeric | 23 | 10 | √ | 0.0000000000 | T82 |
| 187 | fqty141 | T141 | numeric | 23 | 10 | √ | 0.0000000000 | T141 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_mds_fcdatatsentry |  | fentryid |
| 2 | idx_mds_fcdatatsentry |  | fid,fseq,fid2,fseq2 |

---

## 日期字段对照表-子表 t_mds_dateentry

- **表名称：** 日期字段对照表-子表
- **表名：** t_mds_dateentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdeliverycolumn | 固定发货列 | bpchar | 1 |  | √ | '1' | 固定发货列 |
| 3 | ftargetdate | 目标日期 | timestamp | 0 |  |  | null | 目标日期 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | fid2 | fid2 | int8 | 64 |  | √ | 0 |  |
| 7 | ffieldkey | 字段标识 | varchar | 50 |  | √ | ' ' | 字段标识 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mds_dateentry |  | fid,fseq,fid2 |
| 2 | pk_t_mds_dateentry |  | fentryid |

---

## 预测计划-主表 t_mds_fcdatats

- **表名称：** 预测计划-主表
- **表名：** t_mds_fcdatats

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fenablestatus | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: A :可用 B :禁用 |
| 4 | fbillstatus | 确认状态 | varchar | 50 |  | √ | ' ' | 确认状态,枚举: A :暂存 B :已提交 C :已确认 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | forgid | 计划组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fauditdate | 确认日期 | timestamp | 0 |  |  | null | 确认日期 |
| 8 | ffcvrnnum | 版本编码 | int8 | 64 |  | √ | 0 | [版本定义 mds_vrds](../mds_files/mds_vrds.md) |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | finvaldate | 失效日期 | timestamp | 0 |  |  | null | 失效日期 |
| 12 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 13 | fauditorid | 确认人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_mds_fcdatats |  | fid |
| 2 | idx_mds_fcdatats |  | fbillno |
