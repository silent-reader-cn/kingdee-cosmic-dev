# 成本BOM设置（废弃）-cad_bomsetting

## 成本BOM设置（废弃）-主表 t_cad_bomsetting

- **表名称：** 成本BOM设置（废弃）-主表
- **表名：** t_cad_bomsetting

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fbomtypeid | BOM类型 | int8 | 64 |  | √ | 0 | [BOM类型 mpdm_bomtype](../mpdm_files/mpdm_bomtype.md) |
| 3 | fauxpropid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 4 | fmaterialid | 产品编码 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 5 | fexpdate | 失效日期 | timestamp | 0 |  |  | null | 失效日期 |
| 6 | fconfiguredcodeid | 配置号 | int8 | 64 |  | √ | 0 | [配置号（废弃） bd_configuredcode](../sbd_files/bd_configuredcode.md) |
| 7 | fistoupdate | 是否待更新 | bpchar | 1 |  | √ | '0' | 是否待更新 |
| 8 | feffectdate | 生效日期 | timestamp | 0 |  |  | null | 生效日期 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 11 | fbomid | BOM编码 | int8 | 64 |  | √ | 0 | [分组基础资料带组织模板 cad_costbom](../basedata_files/cad_costbom.md) |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 14 | fisdowncalc | 向下卷算 | bpchar | 1 |  | √ | '1' | 向下卷算 |
| 15 | ftracknumberid | 跟踪号 | int8 | 64 |  | √ | 0 | [跟踪号 bd_tracknumber](../sbd_files/bd_tracknumber.md) |
| 16 | fkeycolid | 卷算维度数据 | int8 | 64 |  | √ | 0 | [卷算维度数据表 cad_keycol](../cad_files/cad_keycol.md) |
| 17 | fchargedefsubelement | 物料费用默认子要素 | int8 | 64 |  | √ | 0 | [成本子要素 cad_subelement](../basedata_files/cad_subelement.md) |
| 18 | flot | 批号 | varchar | 80 |  | √ | ' ' | 批号 |
| 19 | fbomversionid | 物料版本 | int8 | 64 |  | √ | 0 | [BOM版本 bd_bomversion](../basedata_files/bd_bomversion.md) |
| 20 | fauditid | fauditid | int8 | 64 |  | √ | 0 |  |
| 21 | fforbidderid | 禁用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 22 | fconsidersubmaterialloss | 考虑子物料损耗 | bpchar | 1 |  | √ | '1' | 考虑子物料损耗 |
| 23 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 24 | fconsidervalidperiod | 考虑子物料有效期 | bpchar | 1 |  | √ | '1' | 考虑子物料有效期 |
| 25 | fprojectid | 项目号 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 26 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 27 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 28 | fchargestdrate | 物料费用标准费率 (%) | numeric | 23 | 10 | √ | 0.0000000000 | 物料费用标准费率 (%) |
| 29 | fmatcalcprop | 物料卷算属性 | varchar | 20 |  | √ | ' ' | 物料卷算属性,枚举: A :自制 B :外购 C :委外 |
| 30 | fcosttypeid | 标准成本方案 | int8 | 64 |  | √ | 0 | [标准成本方案 cad_costtype](../basedata_files/cad_costtype.md) |
| 31 | fforbidddate | 禁用日期 | timestamp | 0 |  |  | null | 禁用日期 |
| 32 | fenable | 使用状态 | varchar | 30 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 33 | fnumber | 单据编码 | varchar | 60 |  | √ | ' ' | 单据编码 |
| 34 | fconsideryieldrate | 考虑成品率 | bpchar | 1 |  | √ | '1' | 考虑成品率 |
| 35 | flossrateformula | 损耗率计算 | varchar | 30 |  | √ | '1' | 损耗率计算,枚举: 1 :子项标准用量 *（1 + 损耗率） 2 :子项标准用量 / (1 - 损耗率) |
| 36 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 37 | fkeycol | 维度字段 | varchar | 255 |  | √ | ' ' | 维度字段 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_cad_bomsetting_pkey |  | fid |
| 2 | idx_cad_bomsetting_kc |  | fkeycol |
| 3 | index_cad_bomsetting_df |  | fcosttypeid,fmaterialid,fbomversionid,fauxpropid |

---

## 成本BOM设置（废弃）-多语言表 t_cad_bomsetting_l

- **表名称：** 成本BOM设置（废弃）-多语言表
- **表名：** t_cad_bomsetting_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 30 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_cad_bomsetting_l_pkey |  | fpkid |
| 2 | index_cad_bomsetting_l_id |  | fid,flocaleid |
