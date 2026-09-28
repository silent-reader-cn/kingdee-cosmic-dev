# 指标分类目录-ipo_quota_type

## 指标分类目录-主表 t_ipo_quota_type

- **表名称：** 指标分类目录-主表
- **表名：** t_ipo_quota_type

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | findicatorscenario | 所属指标场景 | varchar | 50 |  | √ | ' ' | 所属指标场景,枚举: |
| 3 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | fisleaf | 是否叶子 | bpchar | 1 |  | √ | '1' | 是否叶子 |
| 6 | fterm | 释义条款 | varchar | 259 |  | √ | ' ' | 释义条款 |
| 7 | fshowrows | 显示顺序 | int8 | 64 |  | √ | 0 | 显示顺序 |
| 8 | fparentid | 上级分类 | int8 | 64 |  | √ | 0 | 指标分类目录 ipo_quota_type |
| 9 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 10 | fdescribe | 描述 | varchar | 250 |  | √ | ' ' | 描述 |
| 11 | flongnumber | 长编码 | varchar | 50 |  | √ | ' ' | 长编码 |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 14 | flevel | 级次 | int8 | 64 |  | √ | 0 | 级次 |
| 15 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 16 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 17 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 18 | fterm_tag | 释义条款_详情 | text | 0 |  |  | null | 释义条款_详情 |
| 19 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 20 | fisdefault | 系统预设 | bpchar | 1 |  | √ | '1' | 系统预设 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ipo_quota_type_name |  | fname |
| 2 | idx_ipo_quota_type_number |  | fnumber |
| 3 | pk_ipo_quota_type |  | fid |

---

## 指标分类目录-多语言表 t_ipo_quota_type_l

- **表名称：** 指标分类目录-多语言表
- **表名：** t_ipo_quota_type_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | ffullname | 长名称 | varchar | 50 |  | √ | ' ' | 长名称 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ipo_quota_type_l |  | fpkid |
| 2 | idx_ipo_quota_type_l |  | fid |
