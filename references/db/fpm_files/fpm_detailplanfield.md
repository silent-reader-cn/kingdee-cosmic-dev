# 明细计划字段（废弃）-fpm_detailplanfield

## 明细计划字段（废弃）-主表 t_fpm_detailplanfield

- **表名称：** 明细计划字段（废弃）-主表
- **表名：** t_fpm_detailplanfield

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 最后更新人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fcomment | fcomment | varchar | 255 |  | √ | ' ' |  |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fenabledate | 启用日期 | timestamp | 0 |  |  | null | 启用日期 |
| 6 | fdisabledate | 禁用日期 | timestamp | 0 |  |  | null | 禁用日期 |
| 7 | fdisablerid | 禁用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 8 | fmodifytime | 最后更新时间 | timestamp | 0 |  |  | null | 最后更新时间 |
| 9 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 10 | fdetaildimtype | fdetaildimtype | varchar | 50 |  | √ | ' ' |  |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 13 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 14 | fenablerid | 启用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 16 | fbodysys | 体系 | int8 | 64 |  | √ | 0 | [体系管理1（废弃） fpm_bodysysmanage](../fpm_files/fpm_bodysysmanage.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_fpm_detailplanfield |  | fid |
| 2 | idx_fpm_detailplanfield |  | fbodysys |

---

## 明细计划字段（废弃）-多语言表 t_fpm_detailplanfield_l

- **表名称：** 明细计划字段（废弃）-多语言表
- **表名：** t_fpm_detailplanfield_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | fcomment | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 4 | flocaleid | flocaleid | varchar | 50 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_fpm_detailplanfield_l |  | fpkid |
| 2 | idx_fpm_detailplanfield_l |  | fid |

---

## 单据体-子表 t_fpm_detailplanfield_ent

- **表名称：** 单据体-子表
- **表名：** t_fpm_detailplanfield_ent

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | foptiondetail | 选项 | varchar | 500 |  | √ | ' ' | 选项 |
| 3 | foptiondetail_tag | 选项_详情 | text | 0 |  |  | null | 选项_详情 |
| 4 | ffieldshowname | 显示名称 | varchar | 50 |  | √ | ' ' | 显示名称 |
| 5 | fsyssetpre | 系统预置 | bpchar | 1 |  | √ | '0' | 系统预置 |
| 6 | ffieldname | 字段名称 | varchar | 50 |  | √ | ' ' | 字段名称 |
| 7 | fismustinput | 必录 | bpchar | 1 |  | √ | '0' | 必录 |
| 8 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 10 | foption | 选项 | varchar | 500 |  | √ | ' ' | 选项 |
| 11 | fdatatype | 数据类型 | varchar | 50 |  | √ | ' ' | 数据类型,枚举: text :文本 date :日期 amount :金额 basedata :基础资料f7选择 enum :枚举选择 mutibasedata :多类别基础资料 |
| 12 | fisshow | 可见 | bpchar | 1 |  | √ | '0' | 可见 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_fpm_detailplanfield_ent |  | fentryid |
| 2 | idx_fpm_detailplanfield_ent |  | fid |
