# 折旧政策-fa_assetpolicy

## 折旧政策-主表 t_fa_assetpolicy

- **表名称：** 折旧政策-主表
- **表名：** t_fa_assetpolicy

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | LOCALTIMESTAMP | 创建时间 |
| 7 | fenable | 使用状态 | bpchar | 1 |  | √ | '0' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 8 | fnumber | 编号 | varchar | 30 |  | √ | ' ' | 编号 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | LOCALTIMESTAMP | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_fa_assetpolicy_pkey |  | fid |
| 2 | idx_fa_asspol_fnumber |  | fnumber |

---

## 资产政策分录-子表 t_fa_assetpolicyentry

- **表名称：** 资产政策分录-子表
- **表名：** t_fa_assetpolicyentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdepremethodid | 折旧方法 | int8 | 64 |  | √ | 0 | [折旧方法 fa_depremethod](../fa_files/fa_depremethod.md) |
| 3 | fdepretime | 计提时点 | varchar | 50 |  | √ | ' ' | 计提时点,枚举: CLEAR :新增不提，清理计提 NEW :新增计提，清理不提 NEW_AND_CLEAR :新增计提，清理计提 |
| 4 | fdepreeffect | 变动影响 | varchar | 50 |  | √ | ' ' | 变动影响,枚举: NEXT :影响下期 CUR :影响当期 |
| 5 | fassetcatid | 资产类别 | int8 | 64 |  | √ | 0 | [资产类别 fa_assetcategory](../fa_files/fa_assetcategory.md) |
| 6 | fdeprepolicyid | fdeprepolicyid | int8 | 64 |  | √ | 0 |  |
| 7 | fnetresidualvalrate | 净残值率(%) | numeric | 19 | 6 | √ | 0.000000 | 净残值率(%) |
| 8 | fuseyear | 预计使用年限 | int8 | 64 |  | √ | 0 | 预计使用年限 |
| 9 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 11 | fdecpolicyid | 减值政策 | varchar | 50 |  | √ | ' ' | 减值政策,枚举: 1 :不减值 2 :减值，可转回 3 :减值，不可转回 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_fa_assetpolicyentry_pkey |  | fentryid |
| 2 | idx_fa_asspolent_fseq |  | fseq |

---

## 折旧政策-多语言表 t_fa_assetpolicy_l

- **表名称：** 折旧政策-多语言表
- **表名：** t_fa_assetpolicy_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  |  | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_fa_assetpolicy_l_pkey |  | fpkid |
| 2 | idx_fa_asspol_l_fid |  | fid |
