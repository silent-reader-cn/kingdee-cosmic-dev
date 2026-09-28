# 匹配规则-msmod_matchrule

## 匹配规则-多语言表 t_msmod_matchrule_l

- **表名称：** 匹配规则-多语言表
- **表名：** t_msmod_matchrule_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 150 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fdescription | 描述 | varchar | 512 |  | √ | ' ' | 描述 |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_msmod_matchrule_l |  | fpkid |
| 2 | idx_t_msmod_matchrule_l_id |  | fid,flocaleid |

---

## 匹配条件-子表 t_msmod_matchcdit_e

- **表名称：** 匹配条件-子表
- **表名：** t_msmod_matchcdit_e

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fsrcbillfieldname | 源单据字段名称 | varchar | 50 |  | √ | ' ' | 源单据字段名称 |
| 2 | fmseispreset | 系统预设 | bpchar | 1 |  | √ | '0' | 系统预设 |
| 3 | fsrcbillfieldkey | 源单据字段 | varchar | 50 |  | √ | ' ' | 源单据字段 |
| 4 | ftargetbillfieldkey | 目标单据字段 | varchar | 50 |  | √ | ' ' | 目标单据字段 |
| 5 | fcomparison | 比较符 | varchar | 30 |  | √ | ' ' | 比较符,枚举: = :等于 != :不等于 > :大于 = :大于等于 |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | ftargetbillfieldname | 目标单据字段名称 | varchar | 50 |  | √ | ' ' | 目标单据字段名称 |
| 8 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 9 | femptyequal | 空值相等匹配 | bpchar | 1 |  | √ | '1' | 空值相等匹配 |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_msmod_matchcdit_e |  | fdetailid |
| 2 | idx_matchcdit_e_fentryid |  | fentryid |

---

## 匹配规则-主表 t_msmod_matchrule

- **表名称：** 匹配规则-主表
- **表名：** t_msmod_matchrule

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fstatus | 数据状态 | bpchar | 1 |  | √ | 'C' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 8 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 9 | fispreset | 系统预设 | bpchar | 1 |  | √ | '0' | 系统预设 |
| 10 | fwriteofftypeid | 核销类别 | int8 | 64 |  | √ | 0 | 核销类别 msmod_writeofftype |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_msmod_matchrule |  | fid |
| 2 | idx_t_msmod_matchrule_fnumber |  | fnumber |

---

## 插件列表-子表 t_msmod_match_plugin

- **表名称：** 插件列表-子表
- **表名：** t_msmod_match_plugin

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmatchplugin | 插件实现类 | varchar | 255 |  | √ | ' ' | 插件实现类 |
| 3 | fmpeispreset | 系统预设 | bpchar | 1 |  | √ | '0' | 系统预设 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | fpluginenabled | 启用 | bpchar | 1 |  | √ | '0' | 启用 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_msmod_match_plugin |  | fentryid |

---

## 匹配关系-子表 t_msmod_matchrelate_e

- **表名称：** 匹配关系-子表
- **表名：** t_msmod_matchrelate_e

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftargetbilltypeid | 目标单据 | int8 | 64 |  | √ | 0 | 核销单据类型 msmod_billtype |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 5 | fsrcbilltypeid | 源单据 | int8 | 64 |  | √ | 0 | 核销单据类型 msmod_billtype |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_msmod_matchrelate_e |  | fentryid |
| 2 | idx_t_msmod_matchrelate_e_fid |  | fid |
