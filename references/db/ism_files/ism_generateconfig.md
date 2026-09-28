# 组织间结算处理配置（暂不启用）-ism_generateconfig

## 单据转换处理器-子表 t_ism_generateconfig_tf

- **表名称：** 单据转换处理器-子表
- **表名：** t_ism_generateconfig_tf

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 3 | ftransfertargetbilltype | 目标单据类型 | varchar | 100 |  | √ | ' ' | [单据主实体 bos_billmainentity](../mdl_files/bos_billmainentity.md) |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 5 | ftransferclassid | 单据转换处理器 | int8 | 64 |  | √ | 0 | [组织间结算插件 ism_settlebillprocessor](../ism_files/ism_settlebillprocessor.md) |
| 6 | ftransferclass | 处理器类名 | varchar | 255 |  | √ | ' ' | 处理器类名 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ism_gen_tf_fid |  | fid |
| 2 | t_ism_generateconfig_tf_pkey |  | fentryid |

---

## 组织间结算处理配置（暂不启用）-多语言表 t_ism_generateconfig_l

- **表名称：** 组织间结算处理配置（暂不启用）-多语言表
- **表名：** t_ism_generateconfig_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_ism_generateconfig_l_pkey |  | fpkid |
| 2 | idx_ism_gencf |  | fid,flocaleid |

---

## 组织间结算处理配置（暂不启用）-主表 t_ism_generateconfig

- **表名称：** 组织间结算处理配置（暂不启用）-主表
- **表名：** t_ism_generateconfig

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fstatus | 数据状态 | varchar | 60 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fissysinit | 系统预设 | bpchar | 1 |  | √ | ' ' | 系统预设 |
| 8 | fenable | 使用状态 | varchar | 60 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 9 | fbillsaverclassid | 单据保存处理器 | int8 | 64 |  | √ | 0 | [组织间结算插件 ism_settlebillprocessor](../ism_files/ism_settlebillprocessor.md) |
| 10 | fnumber | 编码 | varchar | 120 |  | √ | ' ' | 编码 |
| 11 | fisdefault | 默认 | bpchar | 1 |  | √ | ' ' | 默认 |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_ism_generateconfig_pkey |  | fid |
| 2 | idx_ism_gencf_fno |  | fnumber |
