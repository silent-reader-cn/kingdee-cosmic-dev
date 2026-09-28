# 匹配映射配置-invp_matchmapping_config

## 匹配映射配置-多语言表 t_invp_matchconfig_l

- **表名称：** 匹配映射配置-多语言表
- **表名：** t_invp_matchconfig_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  |  | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_invp_mcl_flocal |  | fid,flocaleid |
| 2 | pk_t_invp_matchconfig_l |  | fpkid |

---

## 字段映射-子表 t_invp_matchconfig_entry

- **表名称：** 字段映射-子表
- **表名：** t_invp_matchconfig_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fleftbracket | 左括号 | varchar | 50 |  | √ | ' ' | 左括号,枚举: :空 ( :( (( :(( ((( :((( :空 : : |
| 3 | fsrcmatchfield | 来源实体字段 | varchar | 100 |  | √ | ' ' | 来源实体字段 |
| 4 | fmatchtype | 匹配类型 | varchar | 50 |  | √ | ' ' | 匹配类型,枚举: A :直接匹配 B :分组匹配 |
| 5 | ftgtmatchfield | 目标实体字段 | varchar | 100 |  | √ | ' ' | 目标实体字段 |
| 6 | ftgtmatchfieldkey | 目标实体字段标识 | varchar | 255 |  | √ | ' ' | 目标实体字段标识 |
| 7 | fsrcmatchfieldkey | 来源实体字段标识 | varchar | 255 |  | √ | ' ' | 来源实体字段标识 |
| 8 | frightbracket | 右括号 | varchar | 50 |  | √ | ' ' | 右括号,枚举: :空 ) :) )) :)) ))) :))) :空 : : |
| 9 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 10 | flogic | 逻辑 | varchar | 50 |  | √ | ' ' | 逻辑,枚举: and :并且 or :或者 |
| 11 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 12 | fmatchgroupid | 分组关系 | int8 | 64 |  | √ | 0 | 数据分组关系 msmod_datagrouprelation |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_invp_matchconfig_entry |  | fentryid |
| 2 | idx_invp_mcentry_fid |  | fid |

---

## 匹配映射配置-主表 t_invp_matchconfig

- **表名称：** 匹配映射配置-主表
- **表名：** t_invp_matchconfig

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fdisabledate | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 6 | fdisablerid | 禁用人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 7 | fsrcentity | 来源实体 | varchar | 80 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 8 | fispreset | 系统预设 | bpchar | 1 |  | √ | '0' | 系统预设 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 11 | ftgtentity | 目标实体 | varchar | 80 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 12 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 14 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 15 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_invp_matchconfig |  | fid |
| 2 | idx_invp_mc_fnum |  | fnumber |
