# 内部单据生成方案-ism_botpconfig

## 生成配置-子表 t_ism_botpconfig_detail

- **表名称：** 生成配置-子表
- **表名：** t_ism_botpconfig_detail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbillfieldresetrule | 虚单字段重置规则 | int8 | 64 |  | √ | 0 | [虚单字段重置规则 ism_billfieldresetrule](../ism_files/ism_billfieldresetrule.md) |
| 3 | fsourcebilltype | 源单据对象 | varchar | 80 |  | √ | ' ' | [单据主实体 bos_billmainentity](../mdl_files/bos_billmainentity.md) |
| 4 | fbillgenerator | 单据生成处理器 | int8 | 64 |  | √ | 0 | [组织间结算插件 ism_settlebillprocessor](../ism_files/ism_settlebillprocessor.md) |
| 5 | fbotpid | BOTP转换规则标识 | varchar | 40 |  | √ | ' ' | [转换规则 botp_crlist](../botp_files/botp_crlist.md) |
| 6 | fbizflow | 业务流程 | int8 | 64 |  | √ | 0 | [流程设计 wf_model](../wf_files/wf_model.md) |
| 7 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 8 | ftargetbilltype | 生成目标单据对象 | varchar | 80 |  | √ | ' ' | [单据主实体 bos_billmainentity](../mdl_files/bos_billmainentity.md) |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_ism_botpconfig_detail_pkey |  | fentryid |
| 2 | idx_ism_botp_d_fid |  | fid |

---

## 内部单据生成方案-多语言表 t_ism_botpconfig_l

- **表名称：** 内部单据生成方案-多语言表
- **表名：** t_ism_botpconfig_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 200 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fdescription | 描述 | varchar | 500 |  | √ | ' ' | 描述 |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_ism_botpconfig_l_pkey |  | fpkid |
| 2 | idx_ism_botpc_l_flid |  | fid,flocaleid |

---

## 内部单据生成方案-主表 t_ism_botpconfig

- **表名称：** 内部单据生成方案-主表
- **表名：** t_ism_botpconfig

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fissysinit | 系统预设 | bpchar | 1 |  | √ | '0' | 系统预设 |
| 6 | fdescription | 描述 | varchar | 500 |  | √ | ' ' | 描述 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 11 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 12 | fplantype | 方案类型 | bpchar | 1 |  | √ | 'A' | 方案类型,枚举: A :通用单据生成方案 B :供应方单据生成方案 C :需求方单据生成方案 D :对外单据生成方案 |
| 13 | fnumber | 编码 | varchar | 120 |  | √ | ' ' | 编码 |
| 14 | fisdefault | 是否默认 | bpchar | 1 |  | √ | '0' | 是否默认 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_ism_botpconfig_pkey |  | fid |
| 2 | idx_ism_botpc_fno |  | fnumber |
