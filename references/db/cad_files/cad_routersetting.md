# 成本工艺路线设置-cad_routersetting

## 成本工艺路线设置-主表 t_cad_routersetting

- **表名称：** 成本工艺路线设置-主表
- **表名：** t_cad_routersetting

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 4 | fexpdate | 失效日期 | timestamp | 0 |  |  | null | 失效日期 |
| 5 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 6 | feffectdate | 生效日期 | timestamp | 0 |  |  | null | 生效日期 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 11 | fcosttypeid | 成本类型 | int8 | 64 |  | √ | 0 | [标准成本方案 cad_costtype](../basedata_files/cad_costtype.md) |
| 12 | fforbidddate | 禁用日期 | timestamp | 0 |  |  | null | 禁用日期 |
| 13 | fconsiderpreparetime | 考虑准备工时 | bpchar | 1 |  | √ | '1' | 考虑准备工时 |
| 14 | fenable | 使用状态 | varchar | 30 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 15 | fnumber | 单据编码 | varchar | 60 |  | √ | ' ' | 单据编码 |
| 16 | froutertype | 工艺类型 | varchar | 30 |  | √ | ' ' | 工艺类型,枚举: A :物料 B :物料组 C :通用 |
| 17 | fauditid | fauditid | int8 | 64 |  | √ | 0 |  |
| 18 | fforbidderid | 禁用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 19 | frouterid | 工艺路线 | int8 | 64 |  | √ | 0 | [分组基础资料带组织模板 cad_router](../basedata_files/cad_router.md) |
| 20 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | index_cad_routersetting |  | fcosttypeid,frouterid |
| 2 | t_cad_routersetting_pkey |  | fid |

---

## 物料单据体-子表 t_cad_routersetting_entry

- **表名称：** 物料单据体-子表
- **表名：** t_cad_routersetting_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fprojectid | 项目号 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 3 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 4 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 5 | ftracknumberid | 跟踪号 | int8 | 64 |  | √ | 0 | [跟踪号 bd_tracknumber](../sbd_files/bd_tracknumber.md) |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fkeycolid | 卷算维度数据 | int8 | 64 |  | √ | 0 | [卷算维度数据表 cad_keycol](../cad_files/cad_keycol.md) |
| 8 | fconfiguredcodeid | 配置号 | int8 | 64 |  | √ | 0 | [配置号（废弃） bd_configuredcode](../sbd_files/bd_configuredcode.md) |
| 9 | flot | 批号 | varchar | 80 |  | √ | ' ' | 批号 |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 11 | fkeycol | 维度字段 | varchar | 255 |  | √ | ' ' | 维度字段 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cad_routersettingen_kc |  | fkeycol |
| 2 | t_cad_routersetting_entry_pkey |  | fentryid |
| 3 | index_cad_routersettingen_id |  | fid,fmaterialid |

---

## 成本工艺路线设置-多语言表 t_cad_routersetting_l

- **表名称：** 成本工艺路线设置-多语言表
- **表名：** t_cad_routersetting_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 510 |  | √ | ' ' | 备注 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_cad_routersetting_l_pkey |  | fpkid |
| 2 | index_cad_routersetting_l |  | fid,flocaleid |
