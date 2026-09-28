# 移动方案基础资料-msmob_scheme

## 移动方案基础资料-多语言表 t_msmob_scheme_l

- **表名称：** 移动方案基础资料-多语言表
- **表名：** t_msmob_scheme_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname |  | varchar | 50 |  | √ | ' ' |  |
| 3 | flocaleid | flocaleid | varchar | 36 |  | √ | ' ' | localeid |
| 4 | fdescription | fdescription | varchar | 255 |  | √ | ' ' |  |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_msmob_scheme_l |  | fpkid |
| 2 | idx_msmob_scheme_l_fid_locale |  | fid,flocaleid |

---

## 移动方案基础资料-主表 t_msmob_scheme

- **表名称：** 移动方案基础资料-主表
- **表名：** t_msmob_scheme

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname |  | varchar | 50 |  | √ | ' ' |  |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fdescription | 方案描述 | varchar | 255 |  | √ | ' ' | 方案描述 |
| 6 | fschemetype | 方案类型 | varchar | 50 |  | √ | ' ' | 方案类型 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fschemename | 方案名称 | varchar | 50 |  | √ | ' ' | 方案名称 |
| 9 | fdefault | 是否最近方案 | bpchar | 1 |  | √ | '0' | 是否最近方案 |
| 10 | fstatus | 数据状态 | bpchar | 1 |  | √ | 'A' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 13 | fcontent_tag | 方案内容_详情 | text | 0 |  |  | null | 方案内容_详情 |
| 14 | frecentusetime | 最近使用时间 | timestamp | 0 |  |  | null | 最近使用时间 |
| 15 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 16 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 17 | fcontent | 方案内容 | varchar | 255 |  | √ | ' ' | 方案内容 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_msmob_scheme |  | fid |
| 2 | idx_mscheme_creator_type_name |  | fcreatorid,fschemetype,fschemename |
